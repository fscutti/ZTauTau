import ROOT

import array
import histmgr
import funcs
import os
import math

from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *


#--------- one and three prong ------------#

f = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_nominal_sub_ztt')

g = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_nominal_sub_ztt_25med')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_data.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_nominal_sub_ztt_35med')

h = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_nominal_Zttjets')

i = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_25med_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_35med_nominal_Zttjets')

#hist_SR_subztt_pretrig1.Print("all")
"""
#    ONE PRONG

f = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau1Track_data.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau1Track_nominal_sub_ztt_1Track')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau1Track_data.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_Tau1Track_nominal_sub_ztt_25med_1Track')

g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau1Track_data.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_Tau1Track_nominal_sub_ztt_35med_1Track')

h = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau1Track_MC.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau1Track_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau1Track_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_25med_Tau1Track_nominal_Zttjets')

i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau1Track_MC.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_35med_Tau1Track_nominal_Zttjets')
"""
"""
#    THREE PRONG

f = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau3Track_data.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau3Track_nominal_sub_ztt_3Track')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau3Track_data.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_Tau3Track_nominal_sub_ztt_25med_3Track')

g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau3Track_data.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_Tau3Track_nominal_sub_ztt_35med_3Track')

h = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau3Track_MC.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau3Track_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau3Track_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_25med_Tau3Track_nominal_Zttjets')

i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau3Track_MC.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_35med_Tau3Track_nominal_Zttjets')
"""
#print hist_SR_subztt_pretrig1, hist_SR_subztt_posttrig1, hist_SR_MC_pretrig1, hist_SR_MC_posttrig1

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

xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))

h_efficiency_simple_subztt_nominal = hist_SR_subztt_posttrig.Clone()

h_efficiency_simple_subztt_nominal.Divide(hist_SR_subztt_posttrig, hist_SR_subztt_pretrig, 1.0, 1.0, "B")

h_efficiency_simple_mc_nominal = hist_SR_MC_posttrig.Clone()

h_efficiency_simple_mc_nominal.Divide(hist_SR_MC_posttrig, hist_SR_MC_pretrig, 1.0, 1.0, "B")

print "****************************"
print "nominal hists"
print ""
h_efficiency_simple_subztt_nominal.Print("all")
h_efficiency_simple_mc_nominal.Print("all")
print "****************************"

outfile = ROOT.TFile('simple_outputnew.root','recreate')
h_efficiency_simple_subztt_nominal.Write()
h_efficiency_simple_mc_nominal.Write()
outfile.Close()

sys_up = ['MUID_UP', 'MUMS_UP']#, 'MUSCALE_UP', 'TAUSF_SYS_UP', 'TAUSF_STAT_UP', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP', 'RQCD_AntiIsoCR_lowPT_UP', 'RQCD_AntiIsoCR_highPT_UP']
sys_dn = ['MUID_DN', 'MUMS_DN']#, 'MUSCALE_DN', 'TAUSF_SYS_DN', 'TAUSF_STAT_DN', 'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN', 'RQCD_AntiIsoCR_lowPT_DN', 'RQCD_AntiIsoCR_highPT_DN']

sys_up_dict = {}
sys_dn_dict = {}

for i in range(len(sys_dn)):
	
	nom_sub_dn = []
	
	print sys_dn[i]

	#--------- one and three prong ------------#
	
	f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
	hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_dn[i])+'_sub_ztt')
	"""
        if sys_dn[i] == 'RQCD_AntiIsoCR_lowPT_DN':
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_RQCD_AntiIsoCR_25med_lowPT_DN_sub_ztt_25med')

        elif sys_dn[i] == 'RQCD_AntiIsoCR_highPT_DN':
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_RQCD_AntiIsoCR_25med_highPT_DN_sub_ztt_25med')

        else:
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_'+str(sys_dn[i])+'_sub_ztt_25med')

	#g0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_data.root')
	#hist_SR_subztt_posttrig1 = g0.Get('h_SR_35med_nominal_sub_ztt_35med')
	"""

        #f0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/no_trig/hists_tau_pt_SR_data.root')
        #hist_SR_subztt_pretrig1 = f0.Get('h_SR_nominal_sub_ztt')

        g0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/25med/hists_tau_pt_SR_25med_data.root')
        hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_nominal_sub_ztt_25med')

	h0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')

        if sys_dn[i] == 'RQCD_AntiIsoCR_lowPT_DN':
		hist_SR_MC_pretrig1 = h0.Get('h_SR_nominal_Zttjets')

        elif sys_dn[i] == 'RQCD_AntiIsoCR_highPT_DN':
                hist_SR_MC_pretrig1 = h0.Get('h_SR_nominal_Zttjets')

	else:
	        hist_SR_MC_pretrig1 = h0.Get('h_SR_'+str(sys_up[i])+'_Zttjets')

	j0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')

        if sys_dn[i] == 'RQCD_AntiIsoCR_lowPT_DN':
                hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_nominal_Zttjets')

        elif sys_dn[i] == 'RQCD_AntiIsoCR_highPT_DN':
                hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_nominal_Zttjets')

        else:    
		hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_'+str(sys_dn[i])+'_Zttjets')

	#j0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_MC.root')
	#hist_SR_MC_posttrig1 = j0.Get('h_SR_35med_nominal_Zttjets')

	#hist_SR_subztt_pretrig1.Print("all")
	
	"""
	#    ONE PRONG

	f1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/no_trig/hists_tau_pt_SR_Tau1Track_data.root')
	hist_SR_subztt_pretrig1 = f1.Get('h_SR_Tau1Track_nominal_sub_ztt_1Track')

	#g1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/25med/hists_tau_pt_SR_25med_Tau1Track_data.root')
	#hist_SR_subztt_posttrig1 = g1.Get('h_SR_25med_Tau1Track_nominal_sub_ztt_25med_1Track')

	g1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_Tau1Track_data.root')
	hist_SR_subztt_posttrig1 = g1.Get('h_SR_35med_Tau1Track_nominal_sub_ztt_35med_1Track')

	h1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/no_trig/hists_tau_pt_SR_Tau1Track_MC.root')
	hist_SR_MC_pretrig1 = h1.Get('h_SR_Tau1Track_nominal_Zttjets')

	#j1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/25med/hists_tau_pt_SR_25med_Tau1Track_MC.root')
	#hist_SR_MC_posttrig1 = j1.Get('h_SR_25med_Tau1Track_nominal_Zttjets')

	j1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_Tau1Track_MC.root')
	hist_SR_MC_posttrig1 = j1.Get('h_SR_35med_Tau1Track_nominal_Zttjets')

	"""
	"""
	#    THREE PRONG

	f3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/no_trig/hists_tau_pt_SR_Tau3Track_data.root')
	hist_SR_subztt_pretrig1 = f3.Get('h_SR_Tau3Track_nominal_sub_ztt_3Track')

	#g3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/25med/hists_tau_pt_SR_25med_Tau3Track_data.root')
	#hist_SR_subztt_posttrig1 = g3.Get('h_SR_25med_Tau3Track_nominal_sub_ztt_25med_3Track')

	g3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_Tau3Track_data.root')
	hist_SR_subztt_posttrig1 = g3.Get('h_SR_35med_Tau3Track_nominal_sub_ztt_35med_3Track')

	h3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/no_trig/hists_tau_pt_SR_Tau3Track_MC.root')
	hist_SR_MC_pretrig1 = h3.Get('h_SR_Tau3Track_nominal_Zttjets')

	#j3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/25med/hists_tau_pt_SR_25med_Tau3Track_MC.root')
	#hist_SR_MC_posttrig1 = j3.Get('h_SR_25med_Tau3Track_nominal_Zttjets')

	j3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_dn[i])+'/35med/hists_tau_pt_SR_35med_Tau3Track_MC.root')
	hist_SR_MC_posttrig1 = j3.Get('h_SR_35med_Tau3Track_nominal_Zttjets')
	"""	
	#print hist_SR_subztt_pretrig1, hist_SR_subztt_posttrig1, hist_SR_MC_pretrig1, hist_SR_MC_posttrig1

        hist_SR_subztt_pretrig =  hist_SR_subztt_pretrig1.Clone()
        hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Clone()
        hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Clone()
        hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Clone()

	hist_SR_subztt_pretrig.SetXTitle('')
	hist_SR_subztt_pretrig.SetYTitle('Efficiency')
	hist_SR_subztt_pretrig.SetTitle('')
	hist_SR_subztt_posttrig.SetXTitle('')
	hist_SR_subztt_posttrig.SetYTitle('Efficiency')
	hist_SR_subztt_posttrig.SetTitle('')
	hist_SR_MC_pretrig.SetXTitle('')
	hist_SR_MC_pretrig.SetYTitle('Efficiency')
	hist_SR_MC_pretrig.SetTitle('')
	hist_SR_MC_posttrig.SetXTitle('')
	hist_SR_MC_posttrig.SetYTitle('Efficiency')
	hist_SR_MC_posttrig.SetTitle('')


	xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
	hist_SR_subztt_pretrig = hist_SR_subztt_pretrig.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
	hist_SR_subztt_posttrig = hist_SR_subztt_posttrig.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
	hist_SR_MC_pretrig = hist_SR_MC_pretrig.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
	hist_SR_MC_posttrig = hist_SR_MC_posttrig.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))
	
	h_efficiency_simple_subztt = hist_SR_subztt_posttrig.Clone()
        h_efficiency_simple_subztt_divide = hist_SR_subztt_pretrig.Clone()	
	h_efficiency_simple_subztt.Divide(h_efficiency_simple_subztt, h_efficiency_simple_subztt_divide, 1.0, 1.0, "B")

	h_efficiency_simple_mc = hist_SR_MC_posttrig.Clone()
	h_efficiency_simple_mc_divide = hist_SR_MC_pretrig.Clone()
	h_efficiency_simple_mc.Divide(hist_SR_MC_posttrig, h_efficiency_simple_mc_divide, 1.0, 1.0, "B")

        print "**************** RESULT"
        h_efficiency_simple_subztt.Print("all")
        h_efficiency_simple_mc.Print("all")


	outfile = ROOT.TFile('systematics_'+str(sys_dn[i])+'.root','recreate')
	h_efficiency_simple_subztt.Write()
	h_efficiency_simple_mc.Write()
	outfile.Close()
        
	
	nom_file = ROOT.TFile('simple_outputnew.root')
        h_efficiency_simple_subztt_nominal = nom_file.Get('hist_SR_subztt_posttrig')
	for j in range(1,14):

        	e_nom = h_efficiency_simple_subztt_nominal.GetBinContent(j)
        	e_dn = h_efficiency_simple_subztt.GetBinContent(j)
		diff = e_nom-e_dn
		nom_sub_dn.append(diff)

	sys_dn_dict[str(sys_dn[i])] = nom_sub_dn

for i in range(len(sys_up)):

	nom_sub_up = []
	print sys_up[i]
	#--------- one and three prong ------------#
	
	f0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')
	hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_up[i])+'_sub_ztt')

        if sys_up[i] == 'RQCD_AntiIsoCR_lowPT_UP':
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_RQCD_AntiIsoCR_25med_lowPT_UP_sub_ztt_25med')

        elif sys_up[i] == 'RQCD_AntiIsoCR_highPT_UP':
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_RQCD_AntiIsoCR_25med_highPT_UP_sub_ztt_25med')

        else:
                g0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')
                hist_SR_subztt_posttrig1 = g0.Get('h_SR_25med_'+str(sys_up[i])+'_sub_ztt_25med')

	#g0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_data.root')
	#hist_SR_subztt_posttrig1 = g0.Get('h_SR_35med_nominal_sub_ztt_35med')

	h0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR.root')

        if sys_up[i] == 'RQCD_AntiIsoCR_lowPT_UP':
                hist_SR_MC_pretrig1 = h0.Get('h_SR_nominal_Zttjets')

        elif sys_up[i] == 'RQCD_AntiIsoCR_highPT_UP':
                hist_SR_MC_pretrig1 = h0.Get('h_SR_nominal_Zttjets')

	else:
		hist_SR_MC_pretrig1 = h0.Get('h_SR_'+str(sys_up[i])+'_Zttjets')

	j0 = ROOT.TFile('../../test/hists_systematics/hists_tau_pt_SR_25med.root')

        if sys_up[i] == 'RQCD_AntiIsoCR_lowPT_UP':
		hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_nominal_Zttjets')

        elif sys_up[i] == 'RQCD_AntiIsoCR_highPT_UP':
                hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_nominal_Zttjets')

	else:
		hist_SR_MC_posttrig1 = j0.Get('h_SR_25med_'+str(sys_up[i])+'_Zttjets')


	#j0 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_MC.root')
	#hist_SR_MC_posttrig1 = j0.Get('h_SR_35med_nominal_Zttjets')

	#hist_SR_subztt_pretrig1.Print("all")
	
	"""
	#    ONE PRONG

	f1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/no_trig/hists_tau_pt_SR_Tau1Track_data.root')
	hist_SR_subztt_pretrig1 = f1.Get('h_SR_Tau1Track_nominal_sub_ztt_1Track')

	#g1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/25med/hists_tau_pt_SR_25med_Tau1Track_data.root')
	#hist_SR_subztt_posttrig1 = g1.Get('h_SR_25med_Tau1Track_nominal_sub_ztt_25med_1Track')

	g1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_Tau1Track_data.root')
	hist_SR_subztt_posttrig1 = g1.Get('h_SR_35med_Tau1Track_nominal_sub_ztt_35med_1Track')

	h1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/no_trig/hists_tau_pt_SR_Tau1Track_MC.root')
	hist_SR_MC_pretrig1 = h1.Get('h_SR_Tau1Track_nominal_Zttjets')

	#j1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/25med/hists_tau_pt_SR_25med_Tau1Track_MC.root')
	#hist_SR_MC_posttrig1 = j1.Get('h_SR_25med_Tau1Track_nominal_Zttjets')

	j1 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_Tau1Track_MC.root')
	hist_SR_MC_posttrig1 = j1.Get('h_SR_35med_Tau1Track_nominal_Zttjets')

	"""
	"""
	#    THREE PRONG

	f3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/no_trig/hists_tau_pt_SR_Tau3Track_data.root')
	hist_SR_subztt_pretrig1 = f3.Get('h_SR_Tau3Track_nominal_sub_ztt_3Track')

	#g3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/25med/hists_tau_pt_SR_25med_Tau3Track_data.root')
	#hist_SR_subztt_posttrig1 = g3.Get('h_SR_25med_Tau3Track_nominal_sub_ztt_25med_3Track')

	g3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_Tau3Track_data.root')
	hist_SR_subztt_posttrig1 = g3.Get('h_SR_35med_Tau3Track_nominal_sub_ztt_35med_3Track')

	h3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/no_trig/hists_tau_pt_SR_Tau3Track_MC.root')
	hist_SR_MC_pretrig1 = h3.Get('h_SR_Tau3Track_nominal_Zttjets')

	#j3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/25med/hists_tau_pt_SR_25med_Tau3Track_MC.root')
	#hist_SR_MC_posttrig1 = j3.Get('h_SR_25med_Tau3Track_nominal_Zttjets')

	j3 = ROOT.TFile('../../test/2016/efficiency_calculations_'+str(sys_up[i])+'/35med/hists_tau_pt_SR_35med_Tau3Track_MC.root')
	hist_SR_MC_posttrig1 = j3.Get('h_SR_35med_Tau3Track_nominal_Zttjets')
	"""	
	#print hist_SR_subztt_pretrig1, hist_SR_subztt_posttrig1, hist_SR_MC_pretrig1, hist_SR_MC_posttrig1

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


	xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
	hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
	hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
	hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
	hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
	hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))

	h_efficiency_simple_subztt = hist_SR_subztt_posttrig.Clone()
	
	h_efficiency_simple_subztt.Divide(hist_SR_subztt_posttrig, hist_SR_subztt_pretrig, 1.0, 1.0, "B")

	h_efficiency_simple_mc = hist_SR_MC_posttrig.Clone()
	
	h_efficiency_simple_mc.Divide(hist_SR_MC_posttrig, hist_SR_MC_pretrig, 1.0, 1.0, "B")
	test_bin = h_efficiency_simple_mc.GetBinContent(1)

	outfile = ROOT.TFile('systematics_'+str(sys_up[i])+'.root','recreate')
	'''
	h_efficiency_subztt.Write()
	h_efficiency_mc.Write()
	'''
	h_efficiency_simple_subztt.Write()
	h_efficiency_simple_mc.Write()
	outfile.Close()

        #h_efficiency_simple_subztt.Print("all") 	
	nom_file = ROOT.TFile('simple_outputnew.root')
        h_efficiency_simple_subztt_nominal = nom_file.Get('hist_SR_subztt_posttrig')
	for j in range(1,14):

        	e_nom = h_efficiency_simple_subztt_nominal.GetBinContent(j)
        	e_up = h_efficiency_simple_subztt.GetBinContent(j)
		diff = e_nom-e_up
		nom_sub_up.append(diff)
	sys_up_dict[str(sys_up[i])] = nom_sub_up
	print len(nom_sub_up)



# Quadratic sum all the entries of the hists
total_sys_up_data1 = ROOT.TH1F("total_sys_up_data", "total_sys_up_data", 13, 25., 300.)
total_sys_dn_data1 = ROOT.TH1F("total_sys_dn_data", "total_sys_dn_data", 13, 25., 300.)

xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
total_sys_up_data = total_sys_up_data1.Rebin(13,"total_sys_up_data",array.array('d',xlow))
total_sys_dn_data = total_sys_dn_data1.Rebin(13,"total_sys_dn_data",array.array('d',xlow))

for k in range(len(nom_sub_up)):
	sys_up_k = 0
	sys_dn_k = 0
	print "bin", k
	for j in range(len(sys_up)):

		list_up = sys_up_dict[sys_up[j]]	
		list_dn = sys_dn_dict[sys_dn[j]]

		x = list_up[k]
		y = list_dn[k]

		print x, y

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
h_efficiency_simple_subztt_nominal = nom_hists_file.Get('hist_SR_MC_posttrig')
h_efficiency_simple_mc_nominal = nom_hists_file.Get('hist_SR_subztt_posttrig')

h_samp_list_mc = []
h_samp_list_mc.append(h_efficiency_simple_mc_nominal)

h_total_mc = funcs.histutils.add_hists(h_samp_list_mc)
h_total_stat_mc = funcs.make_stat_hist(h_total_mc)

h_samp_list_data = []
h_samp_list_data.append(h_efficiency_simple_subztt_nominal)
h_total_data = funcs.histutils.add_hists(h_samp_list_data)
h_total_stat_data = funcs.make_stat_hist(h_total_data)

data_sys_band = funcs.make_band_graph_from_hist(total_sys_up_data,total_sys_dn_data)
data_sys_band.SetFillColor(ROOT.kAzure+1) 

mc_stat = funcs.make_band_graph_from_hist(h_total_stat_mc)
mc_stat.SetFillColor(ROOT.kGray+1)

data_stat = funcs.make_band_graph_from_hist(h_total_stat_data)
data_stat.SetFillColor(ROOT.kSpring+5)

total_up_data1 = ROOT.TH1F("total_up_data", "total_sys_up_data", 13, 25., 300.)
total_dn_data1 = ROOT.TH1F("total_dn_data", "total_sys_dn_data", 13, 25., 300.)

xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
total_up_data = total_up_data1.Rebin(13,"total_up_data",array.array('d',xlow))
total_dn_data = total_dn_data1.Rebin(13,"total_dn_data",array.array('d',xlow))

for i in range(1,h_total_stat_data.GetNbinsX()+1):
	tot_sys_up = total_sys_up_data.GetBinContent(i)
	tot_sys_dn = total_sys_dn_data.GetBinContent(i)
        stat = data_stat.GetBinContent(i)
        tot_UP = sqrt(pow(tot_sys_up,2)+pow(stat,2))
        tot_DN = sqrt(pow(tot_sys_up,2)+pow(stat,2))
        total_up_data.SetBinContent(i,tot_UP)
        total_dn_data.SetBinContent(i,tot_DN)


g_tot  = make_band_graph_from_hist(total_up_data,total_dn_data)
g_tot.SetFillColor(46)


h_data = h_efficiency_simple_subztt.Clone()
h_ratio = h_data.Clone()
h_ratio.Divide(h_efficiency_simple_mc)
h_data.SetStats(0)

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

leg = ROOT.TLegend(0.6,0.5,0.7,0.6) #ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(h_efficiency_simple_subztt,"Data",'PL')
leg.AddEntry(h_efficiency_simple_mc,"Z#rightarrow#tau#tau",'F')

c = ROOT.TCanvas("efficiency","efficiency",750,800)
xmin = h_total.GetBinLowEdge(1)
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
yaxis1 = fr1.GetYaxis()
scale = (1.3+rsplit)
yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
yaxis1.SetTitleOffset( 2.1 * yaxis1.GetTitleOffset() / scale )
yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
xaxis1.SetNdivisions(510)
yaxis1.SetNdivisions(510)
yaxis1.SetTitle("Efficiency")

h_efficiency_simple_mc.Draw("E2")
h_efficiency_simple_subztt.Draw("same")

leg.Draw()
pad1.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextSize(0.05)
lx = 0.5 # for ATLAS internal
ly = 0.845
tlatex.SetTextFont(42)

ty = 0.4
th = 0.05
tx = 0.5
latex_y = ty-2.*th
latex_yb = ty-4.*th
#tlatex.SetTextAlign(10)
tlatex.DrawLatex(0.6,0.3,'#intL dt = 3.2 fb^{-1}, #sqrt{s} = 13 TeV}' ) #(tx,latex_y,'#intL dt = 3.2 fb^{-1}, #sqrt{s} = 13 TeV}' )
tlatex.DrawLatex(0.6,0.2,'HLT_tau35_medium1_tracktwo') #(tx,latex_yb,'HLT_tau35_medium1_tracktwo')
tlatex.SetTextSize=0.001
pad2.cd()

fr2 = pad2.DrawFrame(xmin,0.8,xmax,1.2,';%s;SF'%('Tau Pt'))

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
xaxis2.SetTitleOffset( 3.2* xaxis2.GetTitleOffset() / scale  )
xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
yaxis2.SetNdivisions(510)
xaxis2.SetNdivisions(510)
yaxis2.SetTitle("SF")

g_stat.Draw("E2")
data_sys_band.Draw("E2")

h_ratio.Draw("Same")
pad2.RedrawAxis()
plotsfile = os.path.join("./","TEST_SYS.root")
#c.SaveAs("Test")
fout = ROOT.TFile.Open(plotsfile,'UPDATE')
fout.WriteTObject(c)
fout.Close()






	
	
