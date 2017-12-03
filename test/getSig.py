import os, sys, math
import ROOT

file = ROOT.TFile.Open(sys.argv[1])

samples = ['lfvh', 'FF_Fake', 'Ztautau', 'Zleplep', 'top', 'smh']

hists = {}
file.ls()
for samp in samples:
    hists[samp] = file.Get('h_presel_muallinc_nominal_'+samp)

total = 0

bins = hists['lfvh'].GetNbinsX()

tot_sig, tot_bkg = 0, 0
for bin in range(bins):
    bin += 1
    bkg = 0
    for samp in samples:
        #print samp
        if samp == 'lfvh': sig = hists[samp].GetBinContent(bin)/100
        else: bkg += hists[samp].GetBinContent(bin)
        #print 'content', hists[samp].GetBinContent(bin) 
    print 'bin', bin, 'bkg', bkg, 'sig', sig
    Z = math.sqrt(2*((sig+bkg)*math.log(1+sig/bkg) - sig))
    total += Z*Z
    tot_sig += sig
    tot_bkg += bkg
    print 'Z', Z
print 'bkg', tot_bkg, 'sig', tot_sig
print 'total', math.sqrt(total)
