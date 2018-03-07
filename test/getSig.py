import os, sys, math
import ROOT
from itertools import product

folder = sys.argv[1]
#ROOT.TFile.Open(sys.argv[1])

if sys.argv[2] == 'ff':
    samples = ['lfvh_ggH', 'lfvh_VBF', 'FF_Fake', 'Ztautau', 'Zleplep', 'Wjets', 'top', 'smh', 'diboson']
else:
    samples = ['lfvh_ggH', 'lfvh_VBF', 'Fake',    'Ztautau', 'Zleplep', 'Wjets', 'top', 'smh', 'diboson']

histname = ['NN_input_mcoll', 'output_BDT', 'output_comb', 'output_Fake', 'output_Z']
#histname = ['NN_input_mcoll']#, 'output_BDT', 'output_comb', 'output_Fake', 'output_Z']
histalias = {'NN_input_mcoll': '$m_{coll}$', 'output_BDT': 'BDT score', 'output_comb': 'NN combined score', 'output_Fake': 'NN (Fake vs LFV) score', 'output_Z': 'NN ($Z\\tau\\tau$ vs LFV) score'}
#histname = ['NN_input_mcoll', 'output_BDT', 'output_comb']#, 'output_Fake', 'output_Z']
region = ['presel', 'sr1', 'sr2', 'sr3']
#region = ['presel']#, 'sr1', 'sr2', 'sr3']
leps = ['el', 'mu']
#leps = ['el']
lepalias = {'el': '$e$', 'mu': '$\\mu$'}

def getFiles(folder, histname, region, leps):
    combs = list(product(histname, region, leps))
    files = {}
    for c in combs:
        filename = 'out_hists_'+'_'.join(c)+'allinc.root'
        files[filename] = {'file': ROOT.TFile.Open(folder+'/'+filename), 'config': c, 'value': None, 'hists': []}
    return files

def getHists(file, debug = False):
    if debug:
        print file['config'], file['file']
    hists = {}
    if debug:
        file['file'].ls()
    lep = 'mu' if 'mu' in file['config'] else 'el'
    for samp in samples:
        if debug:
            print samp, lep
        if   'sr1' in file['config']:
            hists[samp] = file['file'].Get(   'h_sr1_%sallinc_nominal_%s' % (lep, samp)).Clone()
        elif 'sr2' in file['config']:
            hists[samp] = file['file'].Get(   'h_sr2_%sallinc_nominal_%s' % (lep, samp)).Clone()
        elif 'sr3' in file['config']:
            hists[samp] = file['file'].Get(   'h_sr3_%sallinc_nominal_%s' % (lep, samp)).Clone()
        elif 'presel' in file['config']:
            hists[samp] = file['file'].Get('h_presel_%sallinc_nominal_%s' % (lep, samp)).Clone()
        else:
            print "What region are you trying to run over?"
            sys.exit()
    return hists

def getValues(hists, debug = False):
    total = 0

    if debug:
        print hists
    bins = hists['Ztautau'].GetNbinsX()

    tot_sig, tot_bkg = 0, 0
    for bin in range(bins):
        bin += 1
        bkg = 0
        sig = 0
        for samp in samples:
            #print samp
            if 'lfvh' in samp: sig += hists[samp].GetBinContent(bin)#/10#0
            else: bkg += hists[samp].GetBinContent(bin)
            #print 'content', hists[samp].GetBinContent(bin) 
        if debug:
            print 'bin', bin, 'bkg', bkg, 'sig', sig
        tot_sig += sig
        tot_bkg += bkg
        if sig == 0 and bkg ==0:
            Z = 0
        elif sig == 0:
            Z = math.sqrt(2*((bkg)*math.log(1) - sig))
        elif bkg <= 0:
            print "No bkg!"
            Z = 0
        else:
            Z = math.sqrt(2*((sig+bkg)*math.log(1+sig/bkg) - sig))
        total += Z*Z
        if debug:
            print 'Z', Z, 'total', total
    if debug:
        print 'bkg', tot_bkg, 'sig', tot_sig
        print 'total', math.sqrt(total)
    return math.sqrt(total)

def resortDict(hist_dicts, histname, region, leps):
    new_dict = {}
    combs = list(product(histname, region, leps))
    for x in histname:
        new_dict[x] = {}
        for y in leps:
            new_dict[x][y] = {}
            for z in region:
                new_dict[x][y][z] = None
    for c in combs:
        new_dict[c[0]][c[2]][c[1]] = [hist_dicts[key]['value'] for key in hist_dicts.keys() if c[0] in key and c[1] in key and c[2]+'all'  in key]
    return new_dict


hist_dicts = getFiles(folder, histname, region, leps)
for key, hist_dict in hist_dicts.iteritems():
    hist_dict['hists'] = getHists(hist_dict, debug=True)
    #print hist_dict['config'], getValues(hist_dict['hists'])
    hist_dict['value'] = getValues(hist_dict['hists'], debug = True)

#print hist_dicts
tmp = """
\\documentclass{article}
\\begin{document}
    \\begin{table}
        \\begin{tabular}{l | c | c c c | c}
            Distribution (channel) & Presel & SR1 & SR2 & SR3 & Total \\\\
            \hline
"""
print hist_dicts.keys()
hist_dicts = resortDict(hist_dicts, histname, region, leps)

for x in histname:
    for y in leps:
        presel = hist_dicts[x][y]['presel'][0]
        sr1    = hist_dicts[x][y]['sr1'][0]
        sr2    = hist_dicts[x][y]['sr2'][0]
        sr3    = hist_dicts[x][y]['sr3'][0]
        total  = math.sqrt(sr1*sr1+sr2*sr2+sr3*sr3)
        tmp+='              '
        tmp+=' & '.join([histalias[x]+' ('+lepalias[y]+')', '%.2f' % presel, '%.2f' % sr1, '%.2f' % sr2, '%.2f' % sr3, '%.2f' % total])#+' \\\\\n'
        tmp+=' \\\\\n'
        #tmp+=' & '.join([lepalias[y]+' '+histalias[x], '%.2f' % presel, '%.2f' % sr1, '%.2f' % sr2, '%.2f' % sr3, '%.2f' % total])+' \\\\\n'
tmp+="""        \\end{tabular}
    \\end{table}
\\end{document}
"""

out_file = open(sys.argv[3], 'w')
out_file.write(tmp)
out_file.close()
os.system("pdflatex %s" % sys.argv[3])
os.system(("rm %s" % sys.argv[3]).replace('.tex','.aux'))
os.system(("rm %s" % sys.argv[3]).replace('.tex','.log'))

