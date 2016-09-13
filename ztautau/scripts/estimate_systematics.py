import ROOT

import array
import histmgr
import funcs
import os
import math
from pyplot import histutils
from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *

#trax = None
trax = "1Track"
#trax = "3Track"

#trig = "25"
trig = "35"

# YIELDS
y = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
wjets = y.Get('h_SR_nominal_Wjets')
top = y.Get('h_SR_nominal_top')
zlljets = y.Get('h_SR_nominal_Zlljets')
zttjets = y.Get('h_SR_nominal_Zttjets')
data = y.Get('h_SR_nominal_data')
subztt = y.Get('h_SR_nominal_sub_ztt')

Wjets,wjets_int_err = histutils.full_integral_and_error(wjets)
print "Wjets integral", Wjets, wjets_int_err
Top,top_int_err = histutils.full_integral_and_error(top)
print "top", Top, top_int_err
Zlljets,zll_int_err = histutils.full_integral_and_error(zlljets)
print "zlljets", Zlljets, zll_int_err
Data,data_int_err = histutils.full_integral_and_error(data)
print "data", Data, data_int_err
Zttjets,ztt_int_err = histutils.full_integral_and_error(zttjets)
print "zttjets", Zttjets, ztt_int_err
Subztt,subztt_int_err = histutils.full_integral_and_error(subztt)
print "subztt", Subztt, subztt_int_err
ssdata = Data-Subztt-Wjets-Top-Zlljets
ssdata_err = math.sqrt( wjets_int_err**2 + top_int_err**2 + zll_int_err**2 + data_int_err**2 + subztt_int_err**2 ) 
print "ssdata", ssdata, ssdata_err
print "expected", Wjets+Top+Zlljets+Zttjets+ssdata, math.sqrt( wjets_int_err**2 + top_int_err**2 + zll_int_err**2 + data_int_err**2 + ztt_int_err**2 )
#--------- inclusive ------------#
"""
f = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_nominal_sub_ztt')

g = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_'+str(trig)+'med_nominal_sub_ztt_'+str(trig)+'med')

h = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_nominal_Zttjets')

i = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_'+str(trig)+'med_nominal_Zttjets')
"""

#--------- 1 vs 3 prong ------------#

f = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

g = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'med_'+str(trax))

h = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau'+str(trax)+'_nominal_Zttjets')

i = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_Zttjets')

hist_SR_subztt_pretrig1.SetXTitle('')
hist_SR_subztt_pretrig1.SetYTitle('Efficiency')
hist_SR_subztt_pretrig1.SetTitle('')
hist_SR_subztt_posttrig1.SetXTitle('')
hist_SR_subztt_posttrig1.SetYTitle('Efficiency')
hist_SR_subztt_posttrig1.SetTitle('')
hist_SR_MC_pretrig1.SetXTitle('')
hist_SR_MC_pretrig1.SetYTitle('Efficiency')
hist_SR_MC_pretrig1.SetTitle('')
hist_SR_MC_posttrig1.SetXTitle('')
hist_SR_MC_posttrig1.SetYTitle('Efficiency')
hist_SR_MC_posttrig1.SetTitle('')

xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))

h_efficiency_simple_subztt_nominal = hist_SR_subztt_posttrig.Clone()
h_efficiency_simple_subztt_nominal.Divide(hist_SR_subztt_posttrig, hist_SR_subztt_pretrig, 1.0, 1.0, "B")

h_efficiency_simple_mc_nominal = hist_SR_MC_posttrig.Clone()
h_efficiency_simple_mc_nominal.Divide(hist_SR_MC_posttrig, hist_SR_MC_pretrig, 1.0, 1.0, "B")
"""

print "****************************"
print "nominal hists"
print ""
h_efficiency_simple_subztt_nominal.Print("all")
h_efficiency_simple_mc_nominal.Print("all")
print "****************************"
"""

outfile = ROOT.TFile('simple_outputnew.root','recreate')
h_efficiency_simple_subztt_nominal.Write()
h_efficiency_simple_mc_nominal.Write()
outfile.Close()


"""
sys_up = ['MUID_UP', 'MUMS_UP', 'MUSCALE_UP', 'TAUSF_SYS_UP',  'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP', 'RQCD_AntiIsoCR_UP', 'RQCD_AntiIsoCR_lowPT_UP', 'RQCD_AntiIsoCR_highPT_UP']
sys_dn = ['MUID_DN', 'MUMS_DN', 'MUSCALE_DN', 'TAUSF_SYS_DN',  'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN', 'RQCD_AntiIsoCR_DN', 'RQCD_AntiIsoCR_lowPT_DN', 'RQCD_AntiIsoCR_highPT_DN']
"""
sys_up = ['pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP', 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP', 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP', 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP', 'MUID_UP', 'MUMS_UP', 'MUSCALE_UP', 'TAUSF_SYS_UP', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP']
sys_dn = ['pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN', 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN', 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN', 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN', 'MUID_DN', 'MUMS_DN', 'MUSCALE_DN', 'TAUSF_SYS_DN', 'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN']

sys_up_dict = {}
sys_dn_dict = {}

for i in range(len(sys_dn)):
	
	nom_sub_dn = []
	
	print sys_dn[i]
         
	#--------- incl ------------#
        """	
	f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
	sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_dn[i])+'_sub_ztt')

	g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med.root')	
        if sys_dn[i] == 'RQCD_AntiIsoCR_lowPT_DN':
                sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_RQCD_AntiIsoCR_'+str(trig)+'med_lowPT_DN_sub_ztt_'+str(trig)+'med')
	
        elif sys_dn[i] == 'RQCD_AntiIsoCR_highPT_DN':
                sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_RQCD_AntiIsoCR_'+str(trig)+'med_highPT_DN_sub_ztt_'+str(trig)+'med')
	
        else:
                sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_'+str(sys_dn[i])+'_sub_ztt_'+str(trig)+'med')

	"""
	#--------- 1 vs 3 prong ------------#

        if sys_dn[i] == 'pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'med_'+str(trax))

	elif sys_dn[i] == 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'med_'+str(trax))

        elif sys_dn[i] == 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN':
	        f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
        	sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_RQCD_AntiIsoCR_'+str(trig)+'med_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'med_'+str(trax))

	elif sys_dn[i] == 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))
                
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_RQCD_AntiIsoCR_'+str(trig)+'med_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'med_'+str(trax))


	else:
	        f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
	        sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_'+str(sys_dn[i])+'_sub_ztt_'+str(trax))
		g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_'+str(sys_dn[i])+'_sub_ztt_'+str(trig)+'med_'+str(trax))
        	
        sys_dn_hist_SR_subztt_pretrig =  sys_dn_hist_SR_subztt_pretrig1.Clone()
        sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig1.Clone()

	sys_dn_hist_SR_subztt_pretrig.SetXTitle('')
	sys_dn_hist_SR_subztt_pretrig.SetYTitle('Efficiency')
	sys_dn_hist_SR_subztt_pretrig.SetTitle('')
	sys_dn_hist_SR_subztt_posttrig.SetXTitle('')
	sys_dn_hist_SR_subztt_posttrig.SetYTitle('Efficiency')
	sys_dn_hist_SR_subztt_posttrig.SetTitle('')


	xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
	sys_dn_hist_SR_subztt_pretrig = sys_dn_hist_SR_subztt_pretrig.Rebin(13,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_pretrig",array.array('d',xlow))
	sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig.Rebin(13,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_posttrig",array.array('d',xlow))
	
	sys_dn_h_efficiency_subztt = sys_dn_hist_SR_subztt_posttrig.Clone()
        sys_dn_h_efficiency_subztt_divide = sys_dn_hist_SR_subztt_pretrig.Clone()	
	sys_dn_h_efficiency_subztt.Divide(sys_dn_h_efficiency_subztt, sys_dn_h_efficiency_subztt_divide, 1.0, 1.0, "B")

	"""
        print "**************** RESULT"
        h_efficiency_simple_subztt.Print("all")
	"""

	outfile = ROOT.TFile('systematics_'+str(sys_dn[i])+'.root','recreate')
	sys_dn_h_efficiency_subztt.Write()
	outfile.Close()
        
	
	nom_file = ROOT.TFile('simple_outputnew.root')
        h_efficiency_simple_subztt_nominal = nom_file.Get('hist_SR_subztt_posttrig')
	for j in range(1,14):

        	e_nom = h_efficiency_simple_subztt_nominal.GetBinContent(j)
        	e_dn = sys_dn_h_efficiency_subztt.GetBinContent(j)
		diff = e_nom-e_dn
		nom_sub_dn.append(diff)
		print "difference is", diff
	sys_dn_dict[str(sys_dn[i])] = nom_sub_dn

for i in range(len(sys_up)):
	print sys_up[i]
	nom_sub_up = []

	#--------- one and three prong ------------#
	"""	
        f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
        sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_up[i])+'_sub_ztt')

        g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med.root')
        if sys_up[i] == 'RQCD_AntiIsoCR_lowPT_UP':
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_RQCD_AntiIsoCR_'+str(trig)+'med_lowPT_UP_sub_ztt_'+str(trig)+'med')
        
        elif sys_up[i] == 'RQCD_AntiIsoCR_highPT_UP':
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_RQCD_AntiIsoCR_'+str(trig)+'med_highPT_UP_sub_ztt_'+str(trig)+'med')
        
        else:
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_'+str(sys_up[i])+'_sub_ztt_'+str(trig)+'med')


	"""


        if sys_up[i] == 'pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'med_'+str(trax))

        elif sys_up[i] == 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'med_'+str(trax))

        elif sys_up[i] == 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_RQCD_AntiIsoCR_'+str(trig)+'med_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'med_'+str(trax))

        elif sys_up[i] == 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP':
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_RQCD_AntiIsoCR_'+str(trig)+'med_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'med_'+str(trax))


        else:
                f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_'+str(sys_up[i])+'_sub_ztt_'+str(trax))
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_'+str(trig)+'med_Tau'+str(trax)+'.root')
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'med_Tau'+str(trax)+'_'+str(sys_up[i])+'_sub_ztt_'+str(trig)+'med_'+str(trax))

        	
	sys_up_hist_SR_subztt_pretrig1.SetXTitle('')
	sys_up_hist_SR_subztt_pretrig1.SetYTitle('Efficiency')
	sys_up_hist_SR_subztt_pretrig1.SetTitle('')
	sys_up_hist_SR_subztt_posttrig1.SetXTitle('')
	sys_up_hist_SR_subztt_posttrig1.SetYTitle('Efficiency')
	sys_up_hist_SR_subztt_posttrig1.SetTitle('')


	xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
	sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(13,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
	sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(13,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
	sys_up_hist_SR_subztt_posttrig = sys_up_hist_SR_subztt_posttrig1.Rebin(13,"sys_up_hist_SR_subztt_posttrig",array.array('d',xlow))

	h_efficiency_simple_subztt = sys_up_hist_SR_subztt_posttrig.Clone()
	
	h_efficiency_simple_subztt.Divide(sys_up_hist_SR_subztt_posttrig, sys_up_hist_SR_subztt_pretrig, 1.0, 1.0, "B")

	outfile = ROOT.TFile('systematics_'+str(sys_up[i])+'.root','recreate')
	h_efficiency_simple_subztt.Write()
	outfile.Close()

        #h_efficiency_simple_subztt.Print("all") 	
	nom_file = ROOT.TFile('simple_outputnew.root')
        h_efficiency_simple_subztt_nominal = nom_file.Get('hist_SR_subztt_posttrig')
	for j in range(1,14):

        	e_nom = h_efficiency_simple_subztt_nominal.GetBinContent(j)
        	e_up = h_efficiency_simple_subztt.GetBinContent(j)
		diff = e_nom-e_up
		print "difference is", diff
		nom_sub_up.append(diff)
	sys_up_dict[str(sys_up[i])] = nom_sub_up
	#print len(nom_sub_up)

# Quadratic sum all the entries of the hists
total_sys_up_data1 = ROOT.TH1F("total_sys_up_data", "total_sys_up_data", 100, 0, 1000.)
total_sys_dn_data1 = ROOT.TH1F("total_sys_dn_data", "total_sys_dn_data", 100, 0, 1000.)

xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
total_sys_up_data = total_sys_up_data1.Rebin(13,"total_sys_up_data",array.array('d',xlow))
total_sys_dn_data = total_sys_dn_data1.Rebin(13,"total_sys_dn_data",array.array('d',xlow))

for k in range(len(nom_sub_up)):
	sys_up_k = 0
	sys_dn_k = 0
	for j in range(len(sys_up)):
		#print sys_up[j]
		#print sys_dn[j]
		list_up = sys_up_dict[sys_up[j]]	
		list_dn = sys_dn_dict[sys_dn[j]]

		x = list_up[k]
		y = list_dn[k]

		val_up_k = max(x,y)
		val_dn_k = min(x,y)
		
		sys_up_k += val_up_k**2
		sys_dn_k += val_dn_k**2

	total_sys_up = math.sqrt(sys_up_k)
	total_sys_dn = math.sqrt(sys_dn_k)

	total_sys_up_data.SetBinContent(k, total_sys_up)
	total_sys_dn_data.SetBinContent(k, total_sys_dn)

total_sys_up_data.Print("all")
total_sys_dn_data.Print("all")

nom_hists_file = ROOT.TFile('simple_outputnew.root')
h_efficiency_simple_mc_nominal = nom_hists_file.Get('hist_SR_MC_posttrig')
h_efficiency_simple_subztt_nominal = nom_hists_file.Get('hist_SR_subztt_posttrig')

#----- Make stat plots ----#

h_samp_list_mc = []
h_samp_list_mc.append(h_efficiency_simple_mc_nominal)
h_total_mc = funcs.histutils.add_hists(h_samp_list_mc)
h_total_stat_mc = funcs.make_stat_hist(h_total_mc)

h_samp_list_data = []
h_samp_list_data.append(h_efficiency_simple_subztt_nominal)
h_total_data = funcs.histutils.add_hists(h_samp_list_data)
h_total_stat_data = funcs.make_stat_hist(h_total_data)

# data and mc stat ratio plots
mc_stat = funcs.make_band_graph_from_hist(h_total_stat_mc)
mc_stat.SetFillColor(ROOT.kRed)

data_stat = funcs.make_band_graph_from_hist(h_total_stat_data)
data_stat.SetFillColor(ROOT.kSpring+5)

#----- Make sys plots ----#

#data sys ratio plot
data_sys_band = funcs.make_band_graph_from_hist(total_sys_up_data,total_sys_dn_data)
data_sys_band.SetFillColor(ROOT.kBlue-4) 

#data sys efficiency plot
data_sys_error_plot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal, total_sys_up_data, total_sys_dn_data)
data_sys_error_plot.SetFillColor(ROOT.kBlue-4)

# ----- Make total data sys + stat plots ----#

total_up_data1 = ROOT.TH1F("total_up_data", "total_sys_up_data", 100, 0, 1000.)
total_dn_data1 = ROOT.TH1F("total_dn_data", "total_sys_dn_data", 100, 0, 1000.)

xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
total_up_data = total_up_data1.Rebin(13,"total_up_data",array.array('d',xlow))
total_dn_data = total_dn_data1.Rebin(13,"total_dn_data",array.array('d',xlow))

total_err_up_ratio1 = ROOT.TH1F("total_err_up_ratio", "total_err_up_ratio", 100, 0, 1000.)
total_err_dn_ratio1 = ROOT.TH1F("total_err_dn_ratio", "total_err_dn_ratio", 100, 0, 1000.)

xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
total_err_up_ratio = total_err_up_ratio1.Rebin(13,"total_err_up_ratio",array.array('d',xlow))
total_err_dn_ratio = total_err_dn_ratio1.Rebin(13,"total_err_dn_ratio",array.array('d',xlow))

for i in range(1,h_total_stat_data.GetNbinsX()+1):

	tot_sys_up = total_sys_up_data.GetBinContent(i)
	tot_sys_dn = total_sys_dn_data.GetBinContent(i)

	dat_err = h_efficiency_simple_subztt_nominal.GetBinError(i)
	#dat = h_efficiency_simple_subztt_nominal.GetBinContent(i)

	mc_stat = h_total_stat_mc.GetBinContent(i)
	stat = dat_err

        #stat = h_total_stat_data.GetBinContent(i)

        #tot_UP = math.sqrt(pow(tot_sys_up,2)+pow(stat,2))
        #tot_DN = math.sqrt(pow(tot_sys_up,2)+pow(stat,2))

	tot_UP = math.sqrt(tot_sys_up**2 + stat**2)
	tot_DN = math.sqrt(tot_sys_dn**2 + stat**2)

	tot_ratio_UP = math.sqrt(tot_sys_up**2 + stat**2 + mc_stat**2)
	tot_ratio_DN = math.sqrt(tot_sys_dn**2 + stat**2 + mc_stat**2)

        total_up_data.SetBinContent(i,tot_UP)
        total_dn_data.SetBinContent(i,tot_DN)

	total_err_up_ratio.SetBinContent(i,tot_ratio_UP)
        total_err_dn_ratio.SetBinContent(i,tot_ratio_DN)


# total uncertainty ratio plot
g_tot  = funcs.make_band_graph_from_hist(total_up_data,total_dn_data)
g_tot.SetFillColor(ROOT.kCyan-9)

g_tot_error_plot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal,total_up_data,total_dn_data) 
g_tot_error_plot.SetFillColor(ROOT.kCyan-9)

h_data = h_efficiency_simple_subztt_nominal.Clone()
h_ratio = h_data.Clone()
h_ratio.Divide(h_efficiency_simple_mc_nominal)
h_data.SetStats(0)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerColor(ROOT.kBlack)

# make "scatter" error bands for the ratio plot

g_tot_ratio_error_plot = funcs.make_error_scatter_graph(h_ratio, total_up_data,total_dn_data)
mc_stat_ratio_error_plot = funcs.make_stat_scatter(h_efficiency_simple_mc_nominal, h_ratio)
data_sys_ratio_error_plot = funcs.make_error_scatter_graph(h_ratio, total_sys_up_data,total_sys_dn_data)
mc_data_tot_err_ratio = funcs.make_error_scatter_graph(h_ratio,total_err_up_ratio, total_err_dn_ratio)
print mc_data_tot_err_ratio

g_tot_ratio_error_plot.SetFillColor(ROOT.kCyan-9)
mc_data_tot_err_ratio.SetFillColor(ROOT.kSpring)
mc_stat_ratio_error_plot.SetFillColor(ROOT.kRed)
data_sys_ratio_error_plot.SetFillColor(ROOT.kBlue-4) 

yaxistitle = ""

nLegend = 2
x_legend = 0.63
x_leg_shift = 0
y_leg_shift = 0.0
legYCompr = 8.0
legYMax = 0.5
legYMin = legYMax - (legYMax - (0.2 + y_leg_shift)) / legYCompr * nLegend
legXMin = x_legend + x_leg_shift
legXMax = legXMin + 0.4

h_efficiency_simple_mc_nominal.SetMarkerStyle(22)
h_efficiency_simple_mc_nominal.SetMarkerColor(ROOT.kRed)
h_efficiency_simple_mc_nominal.SetLineColor(ROOT.kRed)

h_efficiency_simple_subztt_nominal.SetMarkerStyle(20)
h_efficiency_simple_subztt_nominal.SetMarkerColor(ROOT.kBlack)

leg = ROOT.TLegend(0.5,0.4,0.7,0.6) #ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(h_efficiency_simple_subztt_nominal,"Data 2016",'PL')
leg.AddEntry(h_efficiency_simple_mc_nominal,"MC Z#rightarrow#tau#tau",'PL')
leg.AddEntry(g_tot_error_plot, "Data Sys.+Stat.", 'F')
leg.AddEntry(data_sys_error_plot, "Data Sys.", 'F')
leg.AddEntry(mc_data_tot_err_ratio, "Total Unc.", 'F')

c = ROOT.TCanvas("efficiency","efficiency",750,800)
xmin = h_total_stat_data.GetBinLowEdge(1)
xmax = 300
ymin = 0
ymax = 1.1 #h_total.GetMaximum()
#ymax *= 1.8
xtitle = ""

rsplit = 0.3
pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
pad1.SetLeftMargin(0.15)
pad1.SetTicky()
pad1.SetTickx()
pad1.SetBottomMargin(0.04)
pad1.SetLogx()
pad1.Draw()

pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
pad2.SetTopMargin(0.04)
pad2.SetBottomMargin(0.40)
pad2.SetLeftMargin(0.15)
pad2.SetTicky()
pad2.SetTickx()
pad2.SetGridy()
pad2.SetLogx()
pad2.Draw()
pad1.cd()

ytitle = "Efficiency"
#ytitle = yaxistitle


fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
fr1.GetXaxis().SetTitleSize(0)
fr1.GetXaxis().SetLabelSize(0)
xaxis1 = fr1.GetXaxis()
xaxis1.SetRangeUser(20,300)
yaxis1 = fr1.GetYaxis()
scale = (1.3+rsplit)
yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
yaxis1.SetTitleOffset( 1 )
yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
xaxis1.SetNdivisions(510)
yaxis1.SetNdivisions(510)
yaxis1.SetTitle("Efficiency")

g_tot_error_plot.Draw("E2")
data_sys_error_plot.Draw("E2 Same")
h_efficiency_simple_subztt_nominal.Draw("same")
h_efficiency_simple_mc_nominal.Draw("same")

leg.Draw()
pad1.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextSize(0.05)
lx = 0.5 # for ATLAS internal
ly = 0.845
tlatex.SetTextFont(42)

ty = 0.4
th = 0.1
tx = 0.5
latex_y = ty-2.*th
latex_yb = ty-4.*th
#tlatex.SetTextAlign(10)
tlatex.SetTextSize(0.035)
tlatex.DrawLatex(0.5,0.26,'#intL dt = 11.5 fb^{-1}, #sqrt{s} = 13 TeV' ) #(tx,latex_y,'#intL dt = 3.2 fb^{-1}, #sqrt{s} = 13 TeV}' )
tlatex.DrawLatex(0.5,0.20,'HLT_tau'+str(trig)+'_medium1_tracktwo') #(tx,latex_yb,'HLT_tau35_medium1_tracktwo')
if trax:
	if str(trax) == '1Track':
		tlatex.DrawLatex(0.5,0.14,'1-prong')
	elif str(trax) == '3Track':
		tlatex.DrawLatex(0.5,0.14,'3-prong')

pad2.cd()

fr2 = pad2.DrawFrame(xmin,0.8,xmax,1.2,';%s;SF'%('Offline Tau P_{T} [GeV]'))

xaxis2 = fr2.GetXaxis()
yaxis2 = fr2.GetYaxis()

scale = (1. / rsplit)
yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
yaxis2.SetLabelSize( yaxis2.GetLabelSize() * scale )
yaxis2.SetTitleOffset( 2.1* yaxis2.GetTitleOffset() / scale  )
yaxis2.SetLabelOffset(0.2 * yaxis2.GetLabelOffset() * scale )
xaxis2.SetTitleSize( xaxis2.GetTitleSize() * scale )
xaxis2.SetLabelSize( 0.8 * xaxis2.GetLabelSize() * scale )
xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
xaxis2.SetTitleOffset(0.5)
xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
xaxis2.SetRangeUser(20,300)
yaxis2.SetRangeUser(0.6,1.4)
yaxis2.SetNdivisions(4)
xaxis2.SetNdivisions(510)
xaxis2.SetMoreLogLabels()
xaxis2.SetTitleOffset(1)
yaxis2.SetTitle("SF")
yaxis2.SetTitleOffset(0.5)
"""
g_tot.Draw("E2")
mc_stat.Draw("E2 Same")
data_sys_band.Draw("E2 Same")
"""
#g_tot_ratio_error_plot.Draw("E2")
mc_data_tot_err_ratio.Draw("E2")
mc_stat_ratio_error_plot.Draw("E2 Same")
data_sys_ratio_error_plot.Draw("E2 Same")
h_ratio.Draw("Same")

pad2.RedrawAxis()
if trax:
	plotsfile = os.path.join("./","TEST_"+str(trax)+"_"+str(trig)+"med_SYS.root")
else:
	plotsfile = os.path.join("./","TEST_inclusive_"+str(trig)+"med_SYS.root")
#c.SaveAs("Test")
fout = ROOT.TFile.Open(plotsfile,'UPDATE')
fout.WriteTObject(c)
fout.Close()






	
	
