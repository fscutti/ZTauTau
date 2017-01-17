import ROOT

import array
import histmgr
import funcs
import os
import math
from pyplot import histutils
#from ztautau.samples import samples
#from ztautau.plots   import vars
from systematics     import *
import numpy as np

#bdt = "loose"
bdt = "medium"
#bdt = "tight"

variable = "tau_pt"
#variable = "tau_eta"
#variable = "pileup"

#trax = None
#trax = "1Track"
trax = "3Track"

chain = None
#chain = "ptonly"
#chain = "tracktwo"
#chain = "L1TAU12IMmed"

trig = "25med"
#trig = "35med"
#trig = "50L1TAU12med"
#trig = "80med"
#trig = "80L1TAU60med"
#trig = "125med"
#trig = "160med"
#trig = "L1TAU12IMmed"
#trig = "ptonly"
#trig = "tracktwo"

"""
y = ROOT.TFile('../../test/Hists_systematics/BDT_medium/hists_tau_pt_SR.root')
wjets = y.Get('h_SR_nominal_Wjets')
top_truth = y.Get('h_SR_nominal_top_truth')
top_antitruth = y.Get('h_SR_nominal_top_antitruth')
zlljets = y.Get('h_SR_nominal_Zlljets')
zttjets_truth = y.Get('h_SR_nominal_Zttjets_truth')
zttjets_antitruth = y.Get('h_SR_nominal_Zttjets_antitruth')
data = y.Get('h_SR_nominal_data')
#subztt = y.Get('h_SR_nominal_sub_ztt')

# YIELDS
Wjets,wjets_int_err = histutils.full_integral_and_error(wjets)
print "Wjets integral", Wjets, wjets_int_err
Top_truth,top_truth_int_err = histutils.full_integral_and_error(top_truth)
print "top_truth", Top_truth, top_truth_int_err
Top_antitruth,top_antitruth_int_err = histutils.full_integral_and_error(top_antitruth)
print "top_antitruth", Top_antitruth, top_antitruth_int_err
Zlljets,zll_int_err = histutils.full_integral_and_error(zlljets)
print "zlljets", Zlljets, zll_int_err
SS_data,SS_data_int_err = histutils.full_integral_and_error(data)
print "ssdata", SS_data, SS_data_int_err
Zttjets_antitruth,ztt_antitruth_int_err = histutils.full_integral_and_error(zttjets_antitruth)
print "zttjets antitruth", Zttjets_antitruth, ztt_antitruth_int_err
Zttjets_truth,ztt_truth_int_err = histutils.full_integral_and_error(zttjets_truth)
print "zttjets truth", Zttjets_truth, ztt_truth_int_err
#Subztt,subztt_int_err = histutils.full_integral_and_error(subztt)
#print "subztt", Subztt, subztt_int_err
#Data = Subztt+SS_data+Zlljets+Top+Wjets
#print "data", Data
#print "expected", Wjets+Top+Zlljets+Zttjets+SS_data, math.sqrt( wjets_int_err**2 + top_int_err**2 + zll_int_err**2 + SS_data_int_err**2 + ztt_int_err**2 )
"""
#--------- inclusive ------------#
"""
f = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_nominal_sub_ztt')

g = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR_'+str(trig)+'.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_'+str(trig)+'_nominal_sub_ztt_'+str(trig)+'')

h = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_nominal_Zttjets')

i = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR_'+str(trig)+'.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_'+str(trig)+'_nominal_Zttjets')
"""

#--------- 1 vs 3 prong ------------#

f = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

g = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

if trig and chain:
	print "TRIGGER PERFORMANCE STUDY:"
	g_chain = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(chain)+'_Tau'+str(trax)+'.root')
	hist_SR_subztt_posttrig1_chain = g_chain.Get('h_SR_'+str(chain)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(chain)+'_'+str(trax))

h = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau'+str(trax)+'_nominal_truth_taus')

i = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_truth_taus')

if trig and chain:
	i_chain = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(chain)+'_Tau'+str(trax)+'.root')
	hist_SR_MC_posttrig1_chain = i_chain.Get('h_SR_'+str(chain)+'_Tau'+str(trax)+'_nominal_truth_taus')

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

if trig and chain:
	hist_SR_subztt_pretrig1_chain = hist_SR_subztt_pretrig1.Clone()
	hist_SR_MC_pretrig1_chain = hist_SR_MC_pretrig1.Clone()
	hist_SR_subztt_pretrig1_chain.SetXTitle('')
	hist_SR_subztt_pretrig1_chain.SetYTitle('Efficiency')
	hist_SR_subztt_pretrig1_chain.SetTitle('')
	hist_SR_MC_pretrig1_chain.SetXTitle('')
	hist_SR_MC_pretrig1_chain.SetYTitle('Efficiency')
	hist_SR_MC_pretrig1_chain.SetTitle('')
	hist_SR_subztt_posttrig1_chain.SetXTitle('')
	hist_SR_subztt_posttrig1_chain.SetYTitle('Efficiency')
	hist_SR_subztt_posttrig1_chain.SetTitle('')
	hist_SR_MC_posttrig1_chain.SetXTitle('')
	hist_SR_MC_posttrig1_chain.SetYTitle('Efficiency')
	hist_SR_MC_posttrig1_chain.SetTitle('')

if str(variable) == "tau_pt":

	xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
        if str(trig) == "160med":
            xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
	#xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
	hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
	hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
	hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
	hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))
	hist_SR_subztt_posttrig.Print("all")
	if trig and chain:
		hist_SR_subztt_pretrig_chain = hist_SR_subztt_pretrig1_chain.Rebin(13,"hist_SR_subztt_pretrig_chain",array.array('d',xlow))
		hist_SR_MC_pretrig_chain = hist_SR_MC_pretrig1_chain.Rebin(13,"hist_SR_MC_pretrig_chain",array.array('d',xlow))
		hist_SR_subztt_posttrig_chain = hist_SR_subztt_posttrig1_chain.Rebin(13,"hist_SR_subztt_posttrig_chain",array.array('d',xlow))
		hist_SR_MC_posttrig_chain = hist_SR_MC_posttrig1_chain.Rebin(13,"hist_SR_MC_posttrig_chain",array.array('d',xlow))

elif str(variable) == "tau_eta":
	print "eta!"

	xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
	hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(10,"hist_SR_subztt_pretrig",array.array('d',xlow))
	hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(10,"hist_SR_subztt_posttrig",array.array('d',xlow))
	hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(10,"hist_SR_MC_pretrig",array.array('d',xlow))
	hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(10,"hist_SR_MC_posttrig",array.array('d',xlow))

	if trig and chain:
		hist_SR_subztt_pretrig_chain = hist_SR_subztt_pretrig1_chain.Rebin(10,"hist_SR_subztt_pretrig_chain",array.array('d',xlow))
		hist_SR_MC_pretrig_chain = hist_SR_MC_pretrig1_chain.Rebin(10,"hist_SR_MC_pretrig_chain",array.array('d',xlow))
		hist_SR_subztt_posttrig_chain = hist_SR_subztt_posttrig1_chain.Rebin(10,"hist_SR_subztt_posttrig_chain",array.array('d',xlow))
		hist_SR_MC_posttrig_chain = hist_SR_MC_posttrig1_chain.Rebin(10,"hist_SR_MC_posttrig_chain",array.array('d',xlow))

elif str(variable) == "pileup":
	print "pileup!"
	if str(trax) == "3Track":
		xlow = [0,12.,16.,18.,22.,24.,30.,50.]
		n = 7
		hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(7,"hist_SR_subztt_pretrig",array.array('d',xlow))
		hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(7,"hist_SR_subztt_posttrig",array.array('d',xlow))
		hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(7,"hist_SR_MC_pretrig",array.array('d',xlow))
		hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(7,"hist_SR_MC_posttrig",array.array('d',xlow))
	else:
		xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
		n = 8
		hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(8,"hist_SR_subztt_pretrig",array.array('d',xlow))
		hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(8,"hist_SR_subztt_posttrig",array.array('d',xlow))
		hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(8,"hist_SR_MC_pretrig",array.array('d',xlow))
		hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(8,"hist_SR_MC_posttrig",array.array('d',xlow))
	if trig and chain:
		hist_SR_subztt_pretrig_chain = hist_SR_subztt_pretrig1_chain.Rebin(n,"hist_SR_subztt_pretrig_chain",array.array('d',xlow))
		hist_SR_MC_pretrig_chain = hist_SR_MC_pretrig1_chain.Rebin(n,"hist_SR_MC_pretrig_chain",array.array('d',xlow))
		hist_SR_subztt_posttrig_chain = hist_SR_subztt_posttrig1_chain.Rebin(n,"hist_SR_subztt_posttrig_chain",array.array('d',xlow))
		hist_SR_MC_posttrig_chain = hist_SR_MC_posttrig1_chain.Rebin(n,"hist_SR_MC_posttrig_chain",array.array('d',xlow))

data_post = hist_SR_subztt_posttrig.Clone()
data_pre = hist_SR_subztt_pretrig.Clone()

mc_post = hist_SR_MC_posttrig.Clone()
mc_pre = hist_SR_MC_pretrig.Clone()

# HISTOGRAM FOR RATIO
h_efficiency_simple_subztt_nominal = hist_SR_subztt_posttrig.Clone()
h_efficiency_simple_subztt_nominal.Divide(data_post, data_pre, 1.0, 1.0, "B")

h_efficiency_simple_mc_nominal = hist_SR_MC_posttrig.Clone()
h_efficiency_simple_mc_nominal.Divide(mc_post, mc_pre, 1.0, 1.0, "B")

data_post.Print("all")
data_pre.Print("all")

# CORRECT ANY EFFICIENCY ISSUES THAT MAY ARISE DUE TO STATISTICAL FLUCTUATIONS
for k in range(1,data_post.GetNbinsX()+2):
	print k, data_pre.GetBinContent(k)
	tot_val = data_pre.GetBinContent(k)
	trig_val = data_post.GetBinContent(k)
	if trig_val<0:
		trig_val = 0
		data_post.SetBinContent(k,0)
	if trig_val>tot_val:
		print "oh whoops", trig_val, "is bigger than", tot_val
		data_pre.SetBinContent(k,trig_val)
		trig_err = data_post.GetBinError(k)
		data_pre.SetBinError(k,trig_err)
	tot_val_mc = mc_pre.GetBinContent(k)
	trig_val_mc = mc_post.GetBinContent(k)
	if trig_val_mc<0:
		trig_val_mc = 0
		mc_post.SetBinContent(k,0)
	if trig_val_mc>tot_val_mc:
		print "oh whoops", trig_val_mc, "is bigger than", tot_val_mc
		mc_pre.SetBinContent(k,trig_val_mc)
		trig_err_mc = mc_post.GetBinError(k)
		mc_pre.SetBinError(k,trig_err_mc)

data_post.Print("all")
data_pre.Print("all")

data_post1 = data_post.Clone()
data_pre1 = data_pre.Clone()

# EFFICIENCY GRAPH
g_efficiency = ROOT.TGraphAsymmErrors()
g_efficiency.Divide(data_post1,data_pre1,"cl=0.683 b(1,1) mode")
g_efficiency.SetName("data")
g_efficiency.Print("all")

if str(bdt) == "medium":
    g_efficiency_medium = g_efficiency.Clone()
    g_efficiency_medium.SetName("data_medium"+str(trax)+str(trig))

g_efficiency_mc = ROOT.TGraphAsymmErrors()
g_efficiency_mc.Divide(mc_post, mc_pre, "cl=0.683 b(1,1) mode")
g_efficiency_mc.SetName("mc")

if trig and chain:
	data_pre_chain = hist_SR_subztt_pretrig_chain.Clone()
	mc_pre_chain = hist_SR_MC_pretrig_chain.Clone()
	data_post_chain = hist_SR_subztt_posttrig_chain.Clone()
	mc_post_chain = hist_SR_MC_posttrig_chain.Clone()

	for k in range(1,data_post_chain.GetNbinsX()+2):
		print k, data_pre_chain.GetBinContent(k)
		tot_val_chain = data_pre_chain.GetBinContent(k)
		trig_val_chain = data_post_chain.GetBinContent(k)
		if trig_val_chain<0:
			trig_val_chain = 0
			data_post_chain.SetBinContent(k,0)
		if trig_val_chain>tot_val_chain:
			print "oh whoops", trig_val_chain, "is bigger than", tot_val_chain
			data_pre_chain.SetBinContent(k,trig_val_chain)
			trig_err_chain = data_post_chain.GetBinError(k)
			data_pre_chain.SetBinError(k,trig_err_chain)

	data_post1_chain = data_post_chain.Clone()
	data_pre1_chain = data_pre_chain.Clone()

	g_efficiency_chain = ROOT.TGraphAsymmErrors()
	g_efficiency_chain.Divide(data_post1_chain,data_pre1_chain,"cl=0.683 b(1,1) mode")

	g_efficiency_chain.SetName("data_chain")

	g_efficiency_mc_chain = ROOT.TGraphAsymmErrors()
	g_efficiency_mc_chain.Divide(mc_post_chain, mc_pre_chain, "cl=0.683 b(1,1) mode")
	g_efficiency_mc_chain.SetName("mc_chain")

	# HIST FOR TRIGGER CHAIN RATIO
	h_efficiency_simple_subztt_nominal_chain = hist_SR_subztt_posttrig_chain.Clone()
	h_efficiency_simple_subztt_nominal_chain.Divide(h_efficiency_simple_subztt_nominal_chain,hist_SR_subztt_pretrig_chain, 1.0, 1.0, "B")

	h_efficiency_simple_mc_nominal_chain = hist_SR_MC_posttrig_chain.Clone()
	h_efficiency_simple_mc_nominal_chain.Divide(h_efficiency_simple_mc_nominal_chain,hist_SR_MC_pretrig_chain, 1.0, 1.0, "B")

	h_ratio_for_chain = h_efficiency_simple_subztt_nominal.Clone()
	h_ratio_for_chain.Divide(h_efficiency_simple_subztt_nominal,h_efficiency_simple_subztt_nominal_chain, 1.0, 1.0, "B")
	h_ratio_for_chain.SetName('chain_ratio')

	h_ratio_MC_for_chain = h_efficiency_simple_mc_nominal.Clone()
	h_ratio_MC_for_chain.Divide(h_efficiency_simple_mc_nominal,h_efficiency_simple_mc_nominal_chain, 1.0, 1.0, "B")
	h_ratio_MC_for_chain.SetName('MC_chain_ratio')

	# TO GET RATIO FOR RATIO PLOT IN CHAIN EVALUATION
	h_efficiency_simple_subztt_nominal.SetName('eff_ratio_num')
	h_efficiency_simple_subztt_nominal_chain.SetName('eff_ratio_den')

	h_efficiency_simple_mc_nominal.SetName('MC_eff_ratio_num')
	h_efficiency_simple_mc_nominal_chain.SetName('MC_eff_ratio_den')
# h_ratio_for_chain == data ratio to calculate bdt efficiency
# h_ratio_for_chain_mc = mc ""
print "********** NOMINAL EFF *************"
h_efficiency_simple_subztt_nominal.Print("all")
outfile = ROOT.TFile('simple_outputnew.root','recreate')
h_efficiency_simple_subztt_nominal.Write()
g_efficiency.Write()
g_efficiency_mc.Write()
if trig and chain:
	g_efficiency_chain.Write()
	g_efficiency_mc_chain.Write()
	h_ratio_for_chain.Write()
	h_ratio_MC_for_chain.Write()
	h_efficiency_simple_subztt_nominal_chain.Write()
	h_efficiency_simple_mc_nominal_chain.Write()
	h_efficiency_simple_mc_nominal.Write()
outfile.Close()

outfile = ROOT.TFile('simple_outputnew_medium_bdt.root','recreate')
g_efficiency_medium.Write()
outfile.Close()

#sys_up =['pretrig_kW_SS_lowPT_Tau'+str(trax)+'_UP','pretrig_kW_SS_highPT_Tau'+str(trax)+'_UP', 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_UP', 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_UP','pretrig_kW_OS_lowPT_Tau'+str(trax)+'_UP','pretrig_kW_OS_highPT_Tau'+str(trax)+'_UP', 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_UP', 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_UP','pretrig_fw_lowPT_Tau'+str(trax)+'_UP','pretrig_fw_highPT_Tau'+str(trax)+'_UP', 'posttrig_fw_lowPT_Tau'+str(trax)+'_UP', 'posttrig_fw_highPT_Tau'+str(trax)+'_UP',  'MUID_UP', 'MUMS_UP', 'MUSCALE_UP', 'TAUSF_SYS_UP', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP']

#sys_dn = ['pretrig_kW_SS_lowPT_Tau'+str(trax)+'_DN','pretrig_kW_SS_highPT_Tau'+str(trax)+'_DN', 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_DN', 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_DN','pretrig_kW_OS_lowPT_Tau'+str(trax)+'_DN','pretrig_kW_OS_highPT_Tau'+str(trax)+'_DN', 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_DN', 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_DN','pretrig_fw_lowPT_Tau'+str(trax)+'_DN','pretrig_fw_highPT_Tau'+str(trax)+'_DN', 'posttrig_fw_lowPT_Tau'+str(trax)+'_DN', 'posttrig_fw_highPT_Tau'+str(trax)+'_DN','MUID_DN', 'MUMS_DN', 'MUSCALE_DN', 'TAUSF_SYS_DN', 'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN']

sys_up = ['pretrig_kW_SS_lowPT_Tau'+str(trax)+'_UP','pretrig_kW_SS_highPT_Tau'+str(trax)+'_UP', 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_UP', 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_UP','pretrig_kW_OS_lowPT_Tau'+str(trax)+'_UP','pretrig_kW_OS_highPT_Tau'+str(trax)+'_UP', 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_UP', 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_UP','pretrig_fw_lowPT_Tau'+str(trax)+'_UP','pretrig_fw_highPT_Tau'+str(trax)+'_UP', 'posttrig_fw_lowPT_Tau'+str(trax)+'_UP', 'posttrig_fw_highPT_Tau'+str(trax)+'_UP',  'pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP', 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP', 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP', 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP', 'MUID_UP', 'MUMS_UP', 'MUSCALE_UP', 'TAUSF_SYS_UP', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP']

sys_dn = ['pretrig_kW_SS_lowPT_Tau'+str(trax)+'_DN','pretrig_kW_SS_highPT_Tau'+str(trax)+'_DN', 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_DN', 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_DN','pretrig_kW_OS_lowPT_Tau'+str(trax)+'_DN','pretrig_kW_OS_highPT_Tau'+str(trax)+'_DN', 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_DN', 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_DN','pretrig_fw_lowPT_Tau'+str(trax)+'_DN','pretrig_fw_highPT_Tau'+str(trax)+'_DN', 'posttrig_fw_lowPT_Tau'+str(trax)+'_DN', 'posttrig_fw_highPT_Tau'+str(trax)+'_DN','pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN', 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN', 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN', 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN', 'MUID_DN', 'MUMS_DN', 'MUSCALE_DN', 'TAUSF_SYS_DN', 'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN']


#sys_up = ['MUID_UP', 'MUMS_UP', 'MUSCALE_UP', 'TAUSF_SYS_UP', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'METSCALE_UP']

#sys_dn = ['MUID_DN', 'MUMS_DN', 'MUSCALE_DN', 'TAUSF_SYS_DN', 'MUSF_SYS_DN', 'MUSF_STAT_DN', 'METSCALE_DN']

sys_up_dict = {}
sys_dn_dict = {}
sys_up_dict_chain = {}
sys_dn_dict_chain = {}

for i in range(len(sys_dn)):

	nom_sub_dn = []

	nom_sub_dn_chain = []

	print sys_dn[i]

	#--------- incl ------------#
	"""
	f0 = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR.root')
	sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_dn[i])+'_sub_ztt')

	g0 = ROOT.TFile('../../test/Hists_systematics/hists_'+str(variable)+'_SR_'+str(trig)+'.root')
	if sys_dn[i] == 'RQCD_AntiIsoCR_lowPT_DN':
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_RQCD_AntiIsoCR_'+str(trig)+'_lowPT_DN_sub_ztt_'+str(trig)+'')

	elif sys_dn[i] == 'RQCD_AntiIsoCR_highPT_DN':
	sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_RQCD_AntiIsoCR_'+str(trig)+'_highPT_DN_sub_ztt_'+str(trig)+'')

	else:
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_'+str(sys_dn[i])+'_sub_ztt_'+str(trig)+'')

	"""
	#--------- 1 vs 3 prong ------------#

	if sys_dn[i] == 'pretrig_fw_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_fw_lowPT_'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_dn[i] == 'pretrig_fw_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_fw_highPT_'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_fw_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_fw_lowPT_'+str(trax)+'_25med_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_fw_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_fw_highPT_'+str(trax)+'_25med_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'pretrig_kW_OS_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_OS_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_dn[i] == 'pretrig_kW_OS_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_OS_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_OS_25med_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_OS_25med_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'pretrig_kW_SS_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_SS_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))
		print 'h_SR_Tau'+str(trax)+'_kW_SS_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax
)
		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_dn[i] == 'pretrig_kW_SS_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_SS_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_SS_25med_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))
		print 'h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_SS_25med_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax)

	elif sys_dn[i] == 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_SS_25med_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_RQCD_AntiIsoCR_25med_lowPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_dn[i] == 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_DN':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_RQCD_AntiIsoCR_25med_highPT_Tau'+str(trax)+'_DN_sub_ztt_'+str(trig)+'_'+str(trax))

	else:
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_'+str(sys_dn[i])+'_sub_ztt_'+str(trax))
		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_dn_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_'+str(sys_dn[i])+'_sub_ztt_'+str(trig)+'_'+str(trax))

	sys_dn_hist_SR_subztt_pretrig =  sys_dn_hist_SR_subztt_pretrig1.Clone()
	sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig1.Clone()
	sys_dn_hist_SR_subztt_pretrig.SetXTitle('')
	sys_dn_hist_SR_subztt_pretrig.SetYTitle('Efficiency')
	sys_dn_hist_SR_subztt_pretrig.SetTitle('')
	sys_dn_hist_SR_subztt_posttrig.SetXTitle('')
	sys_dn_hist_SR_subztt_posttrig.SetYTitle('Efficiency')
	sys_dn_hist_SR_subztt_posttrig.SetTitle('')

	if str(variable) == "tau_pt":

		xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
                if str(trig) == "160med":
                    xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
		sys_dn_hist_SR_subztt_pretrig = sys_dn_hist_SR_subztt_pretrig.Rebin(13,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_pretrig",array.array('d',xlow))
		sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig.Rebin(13,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_posttrig",array.array('d',xlow))

	if str(variable) == "tau_eta":

		xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
		sys_dn_hist_SR_subztt_pretrig = sys_dn_hist_SR_subztt_pretrig.Rebin(10,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_pretrig",array.array('d',xlow))
		sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig.Rebin(10,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_posttrig",array.array('d',xlow))

	if str(variable) == "pileup":
		if str(trax) == "3Track":
			xlow = [0,12.,16.,18.,22.,24.,30.,50.]
			sys_dn_hist_SR_subztt_pretrig = sys_dn_hist_SR_subztt_pretrig.Rebin(7,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_pretrig",array.array('d',xlow))
			sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig.Rebin(7,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_posttrig",array.array('d',xlow))
		else:
			xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
			sys_dn_hist_SR_subztt_pretrig = sys_dn_hist_SR_subztt_pretrig.Rebin(8,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_pretrig",array.array('d',xlow))
			sys_dn_hist_SR_subztt_posttrig = sys_dn_hist_SR_subztt_posttrig.Rebin(8,"sys_dn_"+str(sys_dn[i])+"_hist_SR_subztt_posttrig",array.array('d',xlow))

	sys_dn_h_efficiency_subztt = sys_dn_hist_SR_subztt_posttrig.Clone()
	sys_dn_h_efficiency_subztt_divide = sys_dn_hist_SR_subztt_pretrig.Clone()


	for k in range(1,sys_dn_h_efficiency_subztt.GetNbinsX()+2):
		tot_val = sys_dn_h_efficiency_subztt_divide.GetBinContent(k)
		trig_val = sys_dn_h_efficiency_subztt.GetBinContent(k)

		if trig_val<0:
			trig_val = 0
			sys_dn_h_efficiency_subztt.SetBinContent(k,0)

		if trig_val>tot_val:
			sys_dn_h_efficiency_subztt_divide.SetBinContent(k,trig_val)
                        trig_err = sys_dn_h_efficiency_subztt.GetBinError(k)
			sys_dn_h_efficiency_subztt_divide.SetBinError(k,trig_err)

	sys_dn_g_efficiency = ROOT.TGraphAsymmErrors()
	sys_dn_g_efficiency.Divide(sys_dn_h_efficiency_subztt, sys_dn_h_efficiency_subztt_divide,"cl=0.683 b(1,1) mode")

	sys_dn_g_efficiency.SetName("sys_dn_data")

	outfile = ROOT.TFile('systematics_'+str(sys_dn[i])+'.root','recreate')

	sys_dn_g_efficiency.Write()
	outfile.Close()

	nom_file = ROOT.TFile('simple_outputnew.root')

	g_efficiency_simple_subztt_nominal = nom_file.Get('data')

	if str(variable) == "tau_pt" or str(variable) == "pileup":
		for j in range(0,sys_dn_h_efficiency_subztt.GetNbinsX()):

			e_nom = g_efficiency_simple_subztt_nominal.GetY()[j]
			e_dn = sys_dn_g_efficiency.GetY()[j]

			diff = e_nom-e_dn
			nom_sub_dn.append(diff)
			print "diff = ", diff

	elif str(variable) == "tau_eta":
		boost_dn = 0
		for j in range(0,sys_dn_h_efficiency_subztt.GetNbinsX()):

			e_nom = g_efficiency_simple_subztt_nominal.GetY()[j-boost_dn]
			e_dn = sys_dn_g_efficiency.GetY()[j-boost_dn]
			n_bin = sys_dn_h_efficiency_subztt.GetBinCenter(j+1)
			if n_bin == -1.445:
				diff = 0
				boost_dn = 1
                        elif n_bin == 1.445:
                                diff = 0
                                boost_dn = 2
			else:
				diff = e_nom-e_dn
			nom_sub_dn.append(diff)
			print "diff = ", diff
	sys_dn_dict[str(sys_dn[i])] = nom_sub_dn

for i in range(len(sys_up)):
	print sys_up[i]
	nom_sub_up = []

	#--------- one and three prong ------------#
	"""
       	f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR.root')
        sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_'+str(sys_up[i])+'_sub_ztt')

        g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'.root')
        if sys_up[i] == 'RQCD_AntiIsoCR_lowPT_UP':
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_RQCD_AntiIsoCR_'+str(trig)+'_lowPT_UP_sub_ztt_'+str(trig)+'')

        elif sys_up[i] == 'RQCD_AntiIsoCR_highPT_UP':
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_RQCD_AntiIsoCR_'+str(trig)+'_highPT_UP_sub_ztt_'+str(trig)+'')

        else:
                sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_'+str(sys_up[i])+'_sub_ztt_'+str(trig)+'')


	"""

	if sys_up[i] == 'pretrig_fw_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_fw_lowPT_'+str(trax)+'_UP_sub_ztt_'+str(trax))
		print 'h_SR_Tau'+str(trax)+'_fw_lowPT_'+str(trax)+'_UP_sub_ztt_'+str(trax)

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_up[i] == 'pretrig_fw_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_fw_highPT_'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_fw_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_fw_lowPT_'+str(trax)+'_25med_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_fw_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_fw_highPT_'+str(trax)+'_25med_UP_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_up[i] == 'pretrig_kW_OS_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_OS_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_up[i] == 'pretrig_kW_OS_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_OS_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_kW_OS_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_OS_25med_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_kW_OS_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_OS_25med_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_up[i] == 'pretrig_kW_SS_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_SS_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))

	elif sys_up[i] == 'pretrig_kW_SS_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_kW_SS_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_kW_SS_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_SS_25med_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_kW_SS_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_kW_SS_25med_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'pretrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'pretrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_RQCD_AntiIsoCR_lowPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_RQCD_AntiIsoCR_25med_lowPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	elif sys_up[i] == 'posttrig_RQCD_AntiIsoCR_highPT_Tau'+str(trax)+'_UP':
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_nominal_sub_ztt_'+str(trax))

		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_RQCD_AntiIsoCR_25med_highPT_Tau'+str(trax)+'_UP_sub_ztt_'+str(trig)+'_'+str(trax))


	else:
		f0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_pretrig1 = f0.Get('h_SR_Tau'+str(trax)+'_'+str(sys_up[i])+'_sub_ztt_'+str(trax))
		g0 = ROOT.TFile('../../test/Hists_systematics/BDT_'+str(bdt)+'/'+str(trig)+'/hists_'+str(variable)+'_SR_'+str(trig)+'_Tau'+str(trax)+'.root')
		sys_up_hist_SR_subztt_posttrig1 = g0.Get('h_SR_'+str(trig)+'_Tau'+str(trax)+'_'+str(sys_up[i])+'_sub_ztt_'+str(trig)+'_'+str(trax))

	sys_up_hist_SR_subztt_pretrig1.SetXTitle('')
	sys_up_hist_SR_subztt_pretrig1.SetYTitle('Efficiency')
	sys_up_hist_SR_subztt_pretrig1.SetTitle('')
	sys_up_hist_SR_subztt_posttrig1.SetXTitle('')
	sys_up_hist_SR_subztt_posttrig1.SetYTitle('Efficiency')
	sys_up_hist_SR_subztt_posttrig1.SetTitle('')

	if str(variable) == "tau_pt":

		xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
                if str(trig) == "160med":
                    xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
		sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(13,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
		sys_up_hist_SR_subztt_posttrig = sys_up_hist_SR_subztt_posttrig1.Rebin(13,"sys_up_hist_SR_subztt_posttrig",array.array('d',xlow))

	if str(variable) == "tau_eta":

		xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
		sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(10,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
		sys_up_hist_SR_subztt_posttrig = sys_up_hist_SR_subztt_posttrig1.Rebin(10,"sys_up_hist_SR_subztt_posttrig",array.array('d',xlow))

	if str(variable) == "pileup":
		if str(trax) == "3Track":
			xlow = [0,12.,16.,18.,22.,24.,30.,50.]
			sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(7,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
			sys_up_hist_SR_subztt_posttrig = sys_up_hist_SR_subztt_posttrig1.Rebin(7,"sys_up_hist_SR_subztt_posttrig",array.array('d',xlow))
		else:
			xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
			sys_up_hist_SR_subztt_pretrig = sys_up_hist_SR_subztt_pretrig1.Rebin(8,"sys_up_hist_SR_subztt_pretrig",array.array('d',xlow))
			sys_up_hist_SR_subztt_posttrig = sys_up_hist_SR_subztt_posttrig1.Rebin(8,"sys_up_hist_SR_subztt_posttrig",array.array('d',xlow))

	sys_up_h_efficiency_subztt_divide = sys_up_hist_SR_subztt_pretrig.Clone()
	sys_up_h_efficiency_subztt = sys_up_hist_SR_subztt_posttrig.Clone()

	for k in range(1,sys_up_h_efficiency_subztt.GetNbinsX()+2):
		tot_val = sys_up_h_efficiency_subztt_divide.GetBinContent(k)
		trig_val = sys_up_h_efficiency_subztt.GetBinContent(k)
		if trig_val<0:
			trig_val = 0
			sys_up_h_efficiency_subztt.SetBinContent(k,0)
		if trig_val>tot_val:
			sys_up_h_efficiency_subztt_divide.SetBinContent(k,trig_val)
			trig_err = sys_up_h_efficiency_subztt.GetBinError(k)
			sys_up_h_efficiency_subztt_divide.SetBinError(k,trig_err)

	sys_up_g_efficiency = ROOT.TGraphAsymmErrors()
	sys_up_g_efficiency.Divide(sys_up_h_efficiency_subztt, sys_up_h_efficiency_subztt_divide,"cl=0.683 b(1,1) mode")

	sys_up_g_efficiency.SetName("sys_up_data")

	outfile = ROOT.TFile('systematics_'+str(sys_up[i])+'.root','recreate')

	sys_up_g_efficiency.Write()
	outfile.Close()

	nom_file = ROOT.TFile('simple_outputnew.root')

	g_efficiency_simple_subztt_nominal = nom_file.Get('data')

	if str(variable) == "tau_pt" or str(variable) == "pileup":

		for j in range(0,sys_up_hist_SR_subztt_pretrig.GetNbinsX()):

			e_nom = g_efficiency_simple_subztt_nominal.GetY()[j]
			e_up = sys_up_g_efficiency.GetY()[j]

			diff = e_nom-e_up
			nom_sub_up.append(diff)
			print "diff = ", diff

        elif str(variable) == "tau_eta":
                boost_up = 0
                for j in range(0,sys_up_h_efficiency_subztt.GetNbinsX()):

                        e_nom = g_efficiency_simple_subztt_nominal.GetY()[j-boost_up]
                        e_up = sys_up_g_efficiency.GetY()[j-boost_up]
                        n_bin = sys_up_h_efficiency_subztt.GetBinCenter(j+1)
                        if n_bin == -1.445:
                                diff = 0
                                boost_up = 1
                        elif n_bin == 1.445:
                                diff = 0
                                boost_up = 2
                        else:
                                diff = e_nom-e_up
                        nom_sub_up.append(diff)
                        print "diff = ", diff

	sys_up_dict[str(sys_up[i])] = nom_sub_up



# Quadratic sum all the entries of the hists
total_sys_up_data1 = ROOT.TH1F("total_sys_up_data", "total_sys_up_data", 100, 0, 1000.)
total_sys_dn_data1 = ROOT.TH1F("total_sys_dn_data", "total_sys_dn_data", 100, 0, 1000.)

if str(variable) == "tau_pt":

	xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
        if str(trig) == "160med":
            xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
	total_sys_up_data = total_sys_up_data1.Rebin(13,"total_sys_up_data",array.array('d',xlow))
	total_sys_dn_data = total_sys_dn_data1.Rebin(13,"total_sys_dn_data",array.array('d',xlow))

if str(variable) == "tau_eta":

	xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
	total_sys_up_data = total_sys_up_data1.Rebin(10,"total_sys_up_data",array.array('d',xlow))
	total_sys_dn_data = total_sys_dn_data1.Rebin(10,"total_sys_dn_data",array.array('d',xlow))

if str(variable) == "pileup":
	if str(trax) == "3Track":

		xlow = [0,12.,16.,18.,22.,24.,30.,50.]
		total_sys_up_data = total_sys_up_data1.Rebin(7,"total_sys_up_data",array.array('d',xlow))
		total_sys_dn_data = total_sys_dn_data1.Rebin(7,"total_sys_dn_data",array.array('d',xlow))
	else:
		xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
		total_sys_up_data = total_sys_up_data1.Rebin(8,"total_sys_up_data",array.array('d',xlow))
		total_sys_dn_data = total_sys_dn_data1.Rebin(8,"total_sys_dn_data",array.array('d',xlow))

print len(nom_sub_up)
for k in range(len(nom_sub_up)):
	print "k", k

	sys_up_k = 0
	sys_dn_k = 0
	for j in range(len(sys_up)):
		print sys_up[j]

		list_up = sys_up_dict[sys_up[j]]
		list_dn = sys_dn_dict[sys_dn[j]]

		x = list_up[k]
		y = list_dn[k]
		print x,y

		val_up_k = max(x,y)
		val_dn_k = min(x,y)
		if np.isnan(val_up_k):
			val_up_k = 0
                if np.isnan(val_dn_k):
                        val_dn_k = 0
		if abs(val_up_k) > 1:
			val_up_k = 0
		if abs(val_dn_k) > 1:
                        val_dn_k = 0
		sys_up_k += val_up_k**2
		sys_dn_k += val_dn_k**2

	total_sys_up = math.sqrt(sys_up_k)
	total_sys_dn = math.sqrt(sys_dn_k)
	print "bin", k+1, "set to", total_sys_up, total_sys_dn
	total_sys_up_data.SetBinContent(k+1, total_sys_up)
	total_sys_dn_data.SetBinContent(k+1, total_sys_dn)

#if str(variable) == "tau_pt":
#	total_sys_up_data.SetBinContent(13,0)
#	total_sys_dn_data.SetBinContent(13,0)

total_sys_up_data.Print("all")
total_sys_dn_data.Print("all")

nom_hists_file = ROOT.TFile('simple_outputnew.root')

graph_efficiency_simple_mc_nominal = nom_hists_file.Get('mc')
graph_efficiency_simple_subztt_nominal = nom_hists_file.Get('data')

print "********* MC"

graph_efficiency_simple_mc_nominal.Print("all")

print "******** data"

graph_efficiency_simple_subztt_nominal.Print("all")

# -------- MAKE STAT HISTS FROM ASYMM GRAPH

total_stat_up_data1 = ROOT.TH1F("total_stat_up_data", "total_stat_up_data", 100, 0, 1000.)
total_stat_dn_data1 = ROOT.TH1F("total_stat_dn_data", "total_stat_dn_data", 100, 0, 1000.)

total_stat_up_mc1 = ROOT.TH1F("total_stat_up_mc", "total_stat_up_mc", 100, 0, 1000.)
total_stat_dn_mc1 = ROOT.TH1F("total_stat_dn_mc", "total_stat_dn_mc", 100, 0, 1000.)

h_efficiency_simple_subztt_nominal1 = ROOT.TH1F("h_efficiency_simple_subztt_nominal", "h_efficiency_simple_subztt_nominal", 100, 0, 1000.)

h_efficiency_simple_mc_nominal1 = ROOT.TH1F("h_efficiency_simple_mc_nominal", "h_efficiency_simple_mc_nominal", 100, 0, 1000.)

if str(variable) == "tau_pt":

        xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
        if str(trig) == "160med":
            xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
	total_stat_up_data = total_stat_up_data1.Rebin(13,"total_stat_up_data",array.array('d',xlow))
	total_stat_dn_data = total_stat_dn_data1.Rebin(13,"total_stat_dn_data",array.array('d',xlow))

	total_stat_up_mc = total_stat_up_mc1.Rebin(13,"total_stat_up_mc",array.array('d',xlow))
	total_stat_dn_mc = total_stat_dn_mc1.Rebin(13,"total_stat_dn_mc",array.array('d',xlow))

	h_efficiency_simple_subztt_nominal = h_efficiency_simple_subztt_nominal1.Rebin(13,"h_efficiency_simple_subztt_nominal",array.array('d',xlow))

	h_efficiency_simple_mc_nominal = h_efficiency_simple_mc_nominal1.Rebin(13,"h_efficiency_simple_mc_nominal",array.array('d',xlow))

if str(variable) == "tau_eta":

        xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
	total_stat_up_data = total_stat_up_data1.Rebin(10,"total_stat_up_data",array.array('d',xlow))
	total_stat_dn_data = total_stat_dn_data1.Rebin(10,"total_stat_dn_data",array.array('d',xlow))

	total_stat_up_mc = total_stat_up_mc1.Rebin(10,"total_stat_up_mc",array.array('d',xlow))
	total_stat_dn_mc = total_stat_dn_mc1.Rebin(10,"total_stat_dn_mc",array.array('d',xlow))

	h_efficiency_simple_subztt_nominal = h_efficiency_simple_subztt_nominal1.Rebin(10,"h_efficiency_simple_subztt_nominal",array.array('d',xlow))

	h_efficiency_simple_mc_nominal = h_efficiency_simple_mc_nominal1.Rebin(10,"h_efficiency_simple_mc_nominal",array.array('d',xlow))

if str(variable) == "pileup":
	if str(trax) == "3Track":
		xlow = [0,12.,16.,18.,22.,24.,30.,50.]
		total_stat_up_data = total_stat_up_data1.Rebin(7,"total_stat_up_data",array.array('d',xlow))
		total_stat_dn_data = total_stat_dn_data1.Rebin(7,"total_stat_dn_data",array.array('d',xlow))

		total_stat_up_mc = total_stat_up_mc1.Rebin(7,"total_stat_up_mc",array.array('d',xlow))
		total_stat_dn_mc = total_stat_dn_mc1.Rebin(7,"total_stat_dn_mc",array.array('d',xlow))

		h_efficiency_simple_subztt_nominal = h_efficiency_simple_subztt_nominal1.Rebin(7,"h_efficiency_simple_subztt_nominal",array.array('d',xlow))

		h_efficiency_simple_mc_nominal = h_efficiency_simple_mc_nominal1.Rebin(7,"h_efficiency_simple_mc_nominal",array.array('d',xlow))
	else:
		xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
		total_stat_up_data = total_stat_up_data1.Rebin(8,"total_stat_up_data",array.array('d',xlow))
		total_stat_dn_data = total_stat_dn_data1.Rebin(8,"total_stat_dn_data",array.array('d',xlow))

		total_stat_up_mc = total_stat_up_mc1.Rebin(8,"total_stat_up_mc",array.array('d',xlow))
		total_stat_dn_mc = total_stat_dn_mc1.Rebin(8,"total_stat_dn_mc",array.array('d',xlow))

		h_efficiency_simple_subztt_nominal = h_efficiency_simple_subztt_nominal1.Rebin(8,"h_efficiency_simple_subztt_nominal",array.array('d',xlow))

		h_efficiency_simple_mc_nominal = h_efficiency_simple_mc_nominal1.Rebin(8,"h_efficiency_simple_mc_nominal",array.array('d',xlow))

uppp = 0
for l in range(0,total_stat_up_data.GetNbinsX()):

	n_bin = total_stat_up_data.GetBinCenter(l+1)
	print n_bin
	stat_up_data = graph_efficiency_simple_subztt_nominal.GetEYhigh()[l-uppp]
	stat_dn_data = graph_efficiency_simple_subztt_nominal.GetEYlow()[l-uppp]
	stat_up_mc = graph_efficiency_simple_mc_nominal.GetEYhigh()[l-uppp]
	stat_dn_mc = graph_efficiency_simple_mc_nominal.GetEYlow()[l-uppp]
	data_y_val = graph_efficiency_simple_subztt_nominal.GetY()[l-uppp]
	mc_y_val = graph_efficiency_simple_mc_nominal.GetY()[l-uppp ]

	#graph_efficiency_simple_subztt_nominal.SetPointEYhigh(l-uppp,0)
        #graph_efficiency_simple_subztt_nominal.SetPointEYlow(l-uppp,0)

	if str(variable) == "tau_eta":
		if n_bin == -1.445:

			total_stat_up_mc.SetBinContent(l+1, 0)
			total_stat_dn_mc.SetBinContent(l+1, 0)

			total_stat_up_data.SetBinContent(l+1, 0)
			total_stat_dn_data.SetBinContent(l+1, 0)

			h_efficiency_simple_subztt_nominal.SetBinContent(l+1, 0)
			h_efficiency_simple_mc_nominal.SetBinContent(l+1, 0)

			total_stat_up_mc.SetBinContent(l+1, 0)
			total_stat_dn_mc.SetBinContent(l+1, 0)
			uppp = 1
			continue


		elif n_bin == 1.445:
			total_stat_up_mc.SetBinContent(l+1, 0)
			total_stat_dn_mc.SetBinContent(l+1, 0)

			total_stat_up_data.SetBinContent(l+1, 0)
			total_stat_dn_data.SetBinContent(l+1, 0)

			h_efficiency_simple_subztt_nominal.SetBinContent(l+1, 0)
			h_efficiency_simple_mc_nominal.SetBinContent(l+1, 0)

			total_stat_up_mc.SetBinContent(l+1, 0)
			total_stat_dn_mc.SetBinContent(l+1, 0)
			uppp = 2
			continue

		else:
			total_stat_up_mc.SetBinContent(l+1, stat_up_mc)
			total_stat_dn_mc.SetBinContent(l+1, stat_dn_mc)

			total_stat_up_data.SetBinContent(l+1, stat_up_data)
			total_stat_dn_data.SetBinContent(l+1, stat_dn_data)

			h_efficiency_simple_subztt_nominal.SetBinContent(l+1, data_y_val)
			h_efficiency_simple_mc_nominal.SetBinContent(l+1, mc_y_val)

			total_stat_up_mc.SetBinContent(l+1, stat_up_mc)
			total_stat_dn_mc.SetBinContent(l+1, stat_dn_mc)

	if str(variable) == "pileup":
		total_stat_up_mc.SetBinContent(l+1, stat_up_mc)
		total_stat_dn_mc.SetBinContent(l+1, stat_dn_mc)

		total_stat_up_data.SetBinContent(l+1, stat_up_data)
		total_stat_dn_data.SetBinContent(l+1, stat_dn_data)

		h_efficiency_simple_subztt_nominal.SetBinContent(l+1, data_y_val)
		h_efficiency_simple_mc_nominal.SetBinContent(l+1, mc_y_val)


	if str(variable) == "tau_pt":
		total_stat_up_mc.SetBinContent(l+1, stat_up_mc)
		total_stat_dn_mc.SetBinContent(l+1, stat_dn_mc)

		total_stat_up_data.SetBinContent(l+1, stat_up_data)
		total_stat_dn_data.SetBinContent(l+1, stat_dn_data)

		h_efficiency_simple_subztt_nominal.SetBinContent(l+1, data_y_val)
		h_efficiency_simple_mc_nominal.SetBinContent(l+1, mc_y_val)

print "******** data"
h_efficiency_simple_subztt_nominal.Print("all")
print "******** mc"
h_efficiency_simple_mc_nominal.Print("all")

h_efficiency_simple_subztt_nominal.SetName('data_nom')
h_efficiency_simple_mc_nominal.SetName('mc_nom')


#----- Make sys plots ----#
#data sys efficiency plot
data_sys_error_plot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal, total_sys_dn_data, total_sys_up_data)
data_sys_error_plot.SetFillColor(ROOT.kAzure-3)
data_sys_error_plot.SetName("data_sys_error_plot")
data_sys_error_plot.SetLineColor(ROOT.kAzure-3)
# ----- Make total data sys + stat plots ----#

total_up_data1 = ROOT.TH1F("total_up_data", "total_sys_up_data", 100, 0, 1000.)
total_dn_data1 = ROOT.TH1F("total_dn_data", "total_sys_dn_data", 100, 0, 1000.)

total_err_up_ratio1 = ROOT.TH1F("total_err_up_ratio", "total_err_up_ratio", 100, 0, 1000.)
total_err_dn_ratio1 = ROOT.TH1F("total_err_dn_ratio", "total_err_dn_ratio", 100, 0, 1000.)

if str(variable) == "tau_pt":

	xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
        if str(trig) == "160med":
            xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]
	total_up_data = total_up_data1.Rebin(13,"total_up_data",array.array('d',xlow))
	total_dn_data = total_dn_data1.Rebin(13,"total_dn_data",array.array('d',xlow))

	total_err_up_ratio = total_err_up_ratio1.Rebin(13,"total_err_up_ratio",array.array('d',xlow))
	total_err_dn_ratio = total_err_dn_ratio1.Rebin(13,"total_err_dn_ratio",array.array('d',xlow))

if str(variable) == "tau_eta":

	xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2.,2.5]
	total_up_data = total_up_data1.Rebin(10,"total_up_data",array.array('d',xlow))
	total_dn_data = total_dn_data1.Rebin(10,"total_dn_data",array.array('d',xlow))

	total_err_up_ratio = total_err_up_ratio1.Rebin(10,"total_err_up_ratio",array.array('d',xlow))
	total_err_dn_ratio = total_err_dn_ratio1.Rebin(10,"total_err_dn_ratio",array.array('d',xlow))

if str(variable) == "pileup":
	if str(trax) == "3Track":
		xlow = [0,12.,16.,18.,22.,24.,30.,50.]
		total_up_data = total_up_data1.Rebin(7,"total_up_data",array.array('d',xlow))
		total_dn_data = total_dn_data1.Rebin(7,"total_dn_data",array.array('d',xlow))

		total_err_up_ratio = total_err_up_ratio1.Rebin(7,"total_err_up_ratio",array.array('d',xlow))
		total_err_dn_ratio = total_err_dn_ratio1.Rebin(7,"total_err_dn_ratio",array.array('d',xlow))
	else:
		xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]
		total_up_data = total_up_data1.Rebin(8,"total_up_data",array.array('d',xlow))
		total_dn_data = total_dn_data1.Rebin(8,"total_dn_data",array.array('d',xlow))

		total_err_up_ratio = total_err_up_ratio1.Rebin(8,"total_err_up_ratio",array.array('d',xlow))
		total_err_dn_ratio = total_err_dn_ratio1.Rebin(8,"total_err_dn_ratio",array.array('d',xlow))

for i in range(1,total_up_data.GetNbinsX()+1):

	tot_sys_up = total_sys_up_data.GetBinContent(i)
	tot_sys_dn = total_sys_dn_data.GetBinContent(i)

	dat_stat_err_up = total_stat_up_data.GetBinContent(i)
	dat_stat_err_dn = total_stat_dn_data.GetBinContent(i)

	mc_stat_err_up = total_stat_up_mc.GetBinContent(i)
	mc_stat_err_dn = total_stat_dn_mc.GetBinContent(i)

	tot_UP = math.sqrt(tot_sys_up**2 + dat_stat_err_up**2)
	tot_DN = math.sqrt(tot_sys_dn**2 + dat_stat_err_dn**2)

	tot_ratio_UP = math.sqrt(tot_sys_up**2 + dat_stat_err_up**2 + mc_stat_err_up**2)
	tot_ratio_DN = math.sqrt(tot_sys_dn**2 + dat_stat_err_dn**2 + mc_stat_err_dn**2)

	total_up_data.SetBinContent(i,tot_UP)
	total_dn_data.SetBinContent(i,tot_DN)

	total_err_up_ratio.SetBinContent(i,tot_ratio_UP)
	total_err_dn_ratio.SetBinContent(i,tot_ratio_DN)

total_up_data.Print("all")
total_dn_data.Print("all")

outfile = ROOT.TFile('hists_chain.root','recreate')
h_efficiency_simple_subztt_nominal.Write()
h_efficiency_simple_mc_nominal.Write()
total_stat_up_data.Write()
total_stat_dn_data.Write()
total_stat_up_mc.Write()
total_stat_dn_mc.Write()
total_sys_up_data.Write()
total_sys_dn_data.Write()
total_up_data.Write()
total_dn_data.Write()
outfile.Close()

# total uncertainty ratio plot
g_tot_error_plot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal,total_up_data,total_dn_data)
g_tot_error_plot.SetFillColor(ROOT.kCyan-9)
g_tot_error_plot.SetName("g_tot_error_plot")

data_stat_error_plot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal,total_stat_up_data,total_stat_dn_data)
data_stat_error_plot.SetFillColor(ROOT.kCyan-9)
data_stat_error_plot.SetName("data_stat_error_plot")
data_stat_error_plot.SetLineColor(ROOT.kCyan-9)
g_tot_error_plot.Print("all")

h_data = h_efficiency_simple_subztt_nominal.Clone()
h_ratio = h_data.Clone()
h_ratio.Divide(h_efficiency_simple_mc_nominal)
h_ratio.SetName("h_ratio")
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetLineWidth(2)

h_ratio_graph = funcs.make_graph_from_hist(h_ratio)
h_ratio_graph.SetMarkerStyle(20)
h_ratio_graph.SetMarkerColor(ROOT.kBlack)
h_ratio_graph.SetLineWidth(2)

# make "scatter" error bands for the ratio plot

mc_stat_ratio_error_plot = funcs.make_error_scatter_graph(h_ratio,total_stat_up_mc,total_stat_dn_mc)
data_sys_ratio_error_plot = funcs.make_error_scatter_graph(h_ratio, total_sys_up_data,total_sys_dn_data)
mc_data_tot_err_ratio = funcs.make_error_scatter_graph(h_ratio,total_err_up_ratio, total_err_dn_ratio)
data_stat_ratio_error_plot = funcs.make_error_scatter_graph(h_ratio,total_stat_up_data,total_stat_up_data)

mc_data_tot_err_ratio.SetName("mc_data_tot_err_ratio")
mc_stat_ratio_error_plot.SetName("mc_stat_ratio_error_plot")
data_stat_ratio_error_plot.SetName("data_stat_ratio_error_plot")

mc_data_tot_err_ratio.SetFillColor(ROOT.kSpring)
mc_stat_ratio_error_plot.SetFillColor(ROOT.kRed)
data_sys_ratio_error_plot.SetFillColor(ROOT.kAzure-3)
data_stat_ratio_error_plot.SetFillColor(ROOT.kCyan-9)

mc_stat_ratio_error_plot.SetLineColor(ROOT.kRed)
data_sys_ratio_error_plot.SetLineColor(ROOT.kAzure-3)
data_stat_ratio_error_plot.SetLineColor(ROOT.kCyan-9)

save_h_efficiency = h_efficiency_simple_subztt_nominal.Clone()
save_h_efficiency.SetName("nominal_eff_data_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

save_h_ratio = h_ratio.Clone()
save_h_ratio.SetName("SF_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

save_stats_mc_up = total_stat_up_mc.Clone()
save_stats_mc_dn = total_stat_dn_mc.Clone()
save_stats_mc_up.SetName("stats_mc_up_eff_mc_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))
save_stats_mc_dn.SetName("stats_mc_dn_eff_mc_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

save_stats_data_up = total_stat_up_data.Clone()
save_stats_data_dn = total_stat_dn_data.Clone()
save_stats_data_up.SetName("stats_data_up_eff_data_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))
save_stats_data_dn.SetName("stats_data_dn_eff_data_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

save_sys_data_up = total_sys_up_data.Clone()
save_sys_data_dn = total_sys_dn_data.Clone()
save_sys_data_up.SetName("sys_data_up_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))
save_sys_data_dn.SetName("sys_data_dn_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

save_tot_up = total_err_up_ratio.Clone()
save_tot_dn = total_err_dn_ratio.Clone()
save_tot_up.SetName("tot_up_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))
save_tot_dn.SetName("tot_dn_"+str(variable)+"_"+str(trig)+"_"+str(trax)+"_BDT_"+str(bdt))

all_effs_file = ROOT.TFile('all_efficiencies.root','update')
save_h_efficiency.Write()
save_h_ratio.Write()
save_stats_mc_up.Write()
save_stats_mc_dn.Write()
save_stats_data_up.Write()
save_stats_data_dn.Write()
save_sys_data_up.Write()
save_sys_data_dn.Write()
save_tot_up.Write()
save_tot_dn.Write()
all_effs_file.Close()

yaxistitle = ""

nLegend = 2
x_legend = 0.63
x_leg_shift = 0
y_leg_shift = 0.0
legYCompr = 8.0
#legYMax = 0.5
#legYMin = legYMax - (legYMax - (0.2 + y_leg_shift)) / legYCompr * nLegend
#legXMin = x_legend + x_leg_shift
#legXMax = legXMin + 0.4

graph_efficiency_simple_mc_nominal.SetMarkerStyle(22)
graph_efficiency_simple_mc_nominal.SetMarkerColor(ROOT.kRed)
graph_efficiency_simple_mc_nominal.SetLineColor(ROOT.kRed)
graph_efficiency_simple_mc_nominal.SetLineWidth(2)

graph_efficiency_simple_subztt_nominal.SetMarkerStyle(20)
graph_efficiency_simple_subztt_nominal.SetMarkerColor(ROOT.kBlack)

leg = ROOT.TLegend(0.45,0.15,0.87,0.33) #ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetNColumns(2)
leg.SetTextSize(0.038)
leg.AddEntry(graph_efficiency_simple_subztt_nominal,"Data 2016",'P')
leg.AddEntry(graph_efficiency_simple_mc_nominal,"MC Z#rightarrow#tau#tau",'P')
#leg.AddEntry(g_tot_error_plot, "Data Sys.+Stat.", 'F')
leg.AddEntry(data_sys_error_plot, "Data sys. error", 'f')
leg.AddEntry(mc_stat_ratio_error_plot, "MC stat. error", "L")
#leg.AddEntry(mc_data_tot_err_ratio, "Total Unc.", 'F')
leg.AddEntry(data_stat_error_plot, "Data stat. error",'f')

c = ROOT.TCanvas(str(variable)+"_"+str(trax)+"_"+str(trig)+"_"+str(bdt)+"_efficiency",str(variable)+"_"+str(trax)+"efficiency",600,600)
xmin = h_efficiency_simple_subztt_nominal.GetBinLowEdge(1)
if str(variable) == "tau_pt": xmax = 300
if str(variable) == "tau_eta": xmax = 3
if str(variable) == "pileup": xmax = 40

ymin = 0
ymax = 1.1 #h_total.GetMaximum()
#ymax *= 1.8
xtitle = ""

rsplit = 0.3
pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
pad1.SetLeftMargin(0.15)
pad1.SetTicky()
pad1.SetTickx()
pad1.SetBottomMargin(0.1)
if str(variable) == "tau_pt":
	pad1.SetLogx()
pad1.Draw()

pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
pad2.SetTopMargin(0.02)
pad2.SetBottomMargin(0.40)
pad2.SetLeftMargin(0.15)
pad2.SetTicky()
pad2.SetTickx()
#pad2.SetGridy()
if str(variable) == "tau_pt":
	pad2.SetLogx()
pad2.Draw()
pad1.cd()

ytitle = "Efficiency"
#ytitle = yaxistitle


fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
fr1.GetXaxis().SetTitleSize(0)
fr1.GetXaxis().SetLabelSize(0)
xaxis1 = fr1.GetXaxis()
xaxis1.SetRangeUser(25,300)
yaxis1 = fr1.GetYaxis()
scale = (1.3+rsplit)
yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
yaxis1.SetTitleOffset( 1 )
yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
xaxis1.SetNdivisions(510)
yaxis1.SetNdivisions(510)
yaxis1.SetTitle("Efficiency")

tot_eff = ROOT.TMultiGraph()
tot_eff.Add(data_stat_error_plot,"E2")#tot_eff.Add(g_tot_error_plot,"E2")
tot_eff.Add(data_sys_error_plot,"E2")
tot_eff.Add(graph_efficiency_simple_mc_nominal,"PZ")
tot_eff.Add(graph_efficiency_simple_subztt_nominal,"PZ")

tot_eff.Draw("a")
xaxis_top = tot_eff.GetXaxis()
yaxis_top = tot_eff.GetYaxis()
if str(variable) == "tau_pt":
	xaxis_top.SetMoreLogLabels()
	if "50" in str(trig):
                xaxis_top.SetRangeUser(50,300)
	elif "80" in str(trig):
	        xaxis_top.SetRangeUser(80,300)
	elif ("125" in str(trig)) or ("160" in str(trig)):
                xaxis_top.SetRangeUser(100,300)
	else:
		xaxis_top.SetRangeUser(25,300)
if str(variable) == "tau_eta":
     xaxis_top.SetRangeUser(-3,3)
if str(variable) == "pileup":
     xaxis_top.SetRangeUser(0,50)
yaxis_top.SetTitleSize( 0.045)#yaxis_top.GetTitleSize() * scale )
yaxis_top.SetTitleOffset( 1 )
yaxis_top.SetLabelSize(0.045)# 0.8 * yaxis_top.GetLabelSize() * scale )
yaxis_top.SetLabelOffset( 1. * yaxis_top.GetLabelOffset() / scale )
xaxis_top.SetNdivisions(510)
xaxis_top.SetNoExponent()
yaxis_top.SetNdivisions(510)
yaxis_top.SetTitle("Efficiency")
yaxis_top.SetRangeUser(0,1.05)

#xaxis_top.SetRangeUser(100,300)
xaxis_top.SetLabelSize(0.045)# 0.8 * yaxis_top.GetLabelSize() * scale )

leg.Draw()
pad1.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
#tlatex.SetTextSize(0.05)
lx = 0.5
ly = 0.845
tlatex.SetTextFont(42)

ty = 0.4
th = 0.1
tx = 0.5
latex_y = ty-2.*th
latex_yb = ty-4.*th

tlatex.SetTextSize(0.038)
tlatex.DrawLatex(0.45,0.55,"#bf{#it{ATLAS}} Internal")
tlatex.DrawLatex(0.45,0.42,'33.3 fb^{-1}, #sqrt{s} = 13 TeV') #)'#intL dt = 33.3 fb^{-1}, #sqrt{s} = 13 TeV' )
if str(trig) == "L1TAU12IMmed":
	tlatex.DrawLatex(0.45,0.5,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, L1TAU12IM trigger')
elif str(trig) == "tracktwo":
        tlatex.DrawLatex(0.45,0.5,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, HLT tau25 perf trigger')
elif str(trig) == "ptonly":
        tlatex.DrawLatex(0.45,0.5,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, HLT tau25 idperf trigger')
else:
	lab = str(trig).split("m")
	print lab[0]
	tlatex.DrawLatex(0.45,0.5,'HLT tau'+lab[0]+' medium trigger')
if trax:
	if str(trax) == '1Track':
		if str(bdt) == "medium":
			tlatex.DrawLatex(0.45,0.36,'1-prong')
		else:
			tlatex.DrawLatex(0.45,0.36,'1-prong, BDT '+str(bdt))
	elif str(trax) == '3Track':
		if str(bdt) == "medium":
			tlatex.DrawLatex(0.45,0.36,'3-prong')
		else:
			tlatex.DrawLatex(0.45,0.36,'3-prong, BDT '+str(bdt))

pad2.cd()
if str(variable) == "tau_pt":
	fr2 = pad2.DrawFrame(xmin,0.8,xmax,1.2,';%s;Data/exp.'%('Offline Tau P_{T} [GeV]'))
if str(variable) == "tau_eta":
	fr2 = pad2.DrawFrame(xmin,0.8,xmax,1.2,';%s;Data/exp.'%('\eta'))
if str(variable) == "pileup":
	fr2 = pad2.DrawFrame(xmin,0.8,xmax,1.2,';%s;Data/exp.'%('<#mu>'))
xaxis2 = fr2.GetXaxis()
yaxis2 = fr2.GetYaxis()

scale = (1. / rsplit)
yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
yaxis2.SetLabelSize( yaxis2.GetLabelSize() * scale )
yaxis2.SetTitleOffset( 2.1* yaxis2.GetTitleOffset() / scale  )
yaxis2.SetLabelOffset(0.2 * yaxis2.GetLabelOffset() * scale )
xaxis2.SetTitleSize( xaxis2.GetTitleSize() * scale )
xaxis2.SetLabelSize( 0.6 * xaxis2.GetLabelSize() * scale )
xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
xaxis2.SetTitleOffset(0.5)
xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
xaxis2.SetRangeUser(25,300)
yaxis2.SetRangeUser(0.6,1.4)
yaxis2.SetNdivisions(4)
xaxis2.SetNdivisions(510)
if str(variable) == "tau_pt":
	xaxis2.SetMoreLogLabels()
xaxis2.SetTitleOffset(1)
yaxis2.SetTitle("Data/exp.")
yaxis2.SetTitleOffset(0.5)

#ratio_line = ROOT.TLine(h_ratio.GetBinLowEdge(1),1,h_ratio.GetBinLowEdge(h_ratio.GetNbinsX()+1),1)
#ratio_line.SetLineColor(ROOT.kRed)
#ratio_line.SetLineStyle(7)
#ratio_line.Draw()

#ratio_line.Draw()
print "MC STAT"
mc_stat_ratio_error_plot.Print("all")
print "DATA STAT"
data_stat_ratio_error_plot.Print("all")
print "DATA SYS"
data_sys_ratio_error_plot.Print("all")
print "SF"
h_ratio_graph.Print("all")


tot_ratio = ROOT.TMultiGraph()
#tot_ratio.Add(mc_data_tot_err_ratio,"E2")
tot_ratio.Add(mc_stat_ratio_error_plot,"E2")
tot_ratio.Add(data_stat_ratio_error_plot,"E2")
tot_ratio.Add(data_sys_ratio_error_plot,"E2")
tot_ratio.Add(h_ratio_graph,"px")
tot_ratio.Draw("a same")

xaxis_bot = tot_ratio.GetXaxis()
yaxis_bot = tot_ratio.GetYaxis()
xaxis_bot.SetLabelFont(42)
yaxis_bot.SetLabelFont(42)

yaxis_bot.SetTitleSize(0.1)# yaxis_bot.GetTitleSize() * scale )
yaxis_bot.SetLabelSize(0.1)# yaxis_bot.GetLabelSize() * scale )
yaxis_bot.SetTitleOffset( 2.1* yaxis_bot.GetTitleOffset() / scale  )
yaxis_bot.SetLabelOffset(0.2 * yaxis_bot.GetLabelOffset() * scale )
xaxis_bot.SetTitleSize( 0.1)#xaxis_bot.GetTitleSize() * scale )
xaxis_bot.SetLabelSize( 0.1)# * xaxis_bot.GetLabelSize() * scale )
xaxis_bot.SetTickLength( xaxis_bot.GetTickLength() * scale )
xaxis_bot.SetTitleOffset(0.45)
xaxis_bot.SetLabelOffset( 2.5* xaxis_bot.GetLabelOffset() / scale )
if str(variable) == "tau_pt":
	if "50" in str(trig):
                xaxis_bot.SetRangeUser(50,300)
	elif "80" in str(trig):
	        xaxis_bot.SetRangeUser(80,300)
	elif ("125" in str(trig)) or ("160" in str(trig)):
                xaxis_bot.SetRangeUser(100,300)
	else:
     		xaxis_bot.SetRangeUser(25,300)
     	xaxis_bot.SetTitle('Offline Tau P_{T} [GeV]')
     	xaxis_bot.SetMoreLogLabels()
if str(variable) == "tau_eta":
     xaxis_bot.SetRangeUser(-3,3)
     xaxis_bot.SetTitle('Offline Tau #eta')
if str(variable) == "pileup":
     xaxis_bot.SetTitle('#mu')
     xaxis_bot.SetRangeUser(0,50)
yaxis_bot.SetRangeUser(0.6,1.4)
yaxis_bot.SetNdivisions(4)
xaxis_bot.SetNoExponent()
xaxis_bot.SetNdivisions(510)
xaxis_bot.SetTitleOffset(1)
yaxis_bot.SetTitle("Data/exp.")
yaxis_bot.SetTitleOffset(0.48)
yaxis_bot.SetLabelSize( 0.095)
yaxis_bot.SetTitleSize( 0.1)

#xaxis_bot.SetRangeUser(100,300)
pad2.RedrawAxis()
if trax:
	plotsfile = os.path.join("./","eff_"+str(variable)+"_"+str(trax)+"_"+str(trig)+"_"+str(bdt)+"_SYS.root")
else:
	plotsfile = os.path.join("./","eff_inclusive_"+str(trig)+"_SYS.root")


fout = ROOT.TFile.Open(plotsfile,'UPDATE')
fout.WriteTObject(c)
fout.Close()


if trig and chain:

	print "*********************************"
	print " 25med and chain!"
	print "*********************************"

	nom_hists_file = ROOT.TFile('simple_outputnew.root')

	graph_efficiency_simple_mc_nominal_chain = nom_hists_file.Get('mc_chain')
	graph_efficiency_simple_subztt_nominal_chain = nom_hists_file.Get('data_chain')
	ratio_plot = nom_hists_file.Get('chain_ratio')
	MC_ratio_plot = nom_hists_file.Get('MC_chain_ratio')
	eff_ratio_num = nom_hists_file.Get('eff_ratio_num')
	eff_ratio_den = nom_hists_file.Get('eff_ratio_den')
	MC_eff_ratio_num = nom_hists_file.Get('MC_eff_ratio_num')
	MC_eff_ratio_den = nom_hists_file.Get('MC_eff_ratio_den')

	print "********* MC"

	graph_efficiency_simple_mc_nominal_chain.Print("all")

	print "******** data"

	graph_efficiency_simple_subztt_nominal_chain.Print("all")

	# -------- MAKE STAT HISTS FROM ASYMM GRAPH

	total_stat_up_data1_chain = ROOT.TH1F("total_stat_up_data_chain", "total_stat_up_data_chain", 100, 0, 1000.)
	total_stat_dn_data1_chain = ROOT.TH1F("total_stat_dn_data_chain", "total_stat_dn_data_chain", 100, 0, 1000.)

	total_stat_up_mc1_chain = ROOT.TH1F("total_stat_up_mc_chain", "total_stat_up_mc_chain", 100, 0, 1000.)
	total_stat_dn_mc1_chain = ROOT.TH1F("total_stat_dn_mc_chain", "total_stat_dn_mc_chain", 100, 0, 1000.)

	total_stat_up_mc_data1_chain = ROOT.TH1F("total_stat_up_mc_data_chain", "total_stat_up_mc_data_chain", 100, 0, 1000.)
	total_stat_dn_mc_data1_chain = ROOT.TH1F("total_stat_dn_mc_data_chain", "total_stat_dn_mc_data_chain", 100, 0, 1000.)

	h_efficiency_simple_subztt_nominal1_chain = ROOT.TH1F("h_efficiency_simple_subztt_nominal_chain", "h_efficiency_simple_subztt_nominal_chain", 100, 0, 1000.)

	h_efficiency_simple_mc_nominal1_chain = ROOT.TH1F("h_efficiency_simple_mc_nominal_chain", "h_efficiency_simple_mc_nominal_chain", 100, 0, 1000.)

	if str(variable) == "tau_pt":

		xlow = [25.,28.,30.,32.,34.,36.,39.,43.,52.,64.,80.,100.,150.,300.]
                if str(trig) == "160med":
                    xlow = [25.,28.,30.,32.,52.,64.,80.,100.,150.,160.,165.,180.,200.,300.]

		total_stat_up_data_chain = total_stat_up_data1_chain.Rebin(13,"total_stat_up_data_chain",array.array('d',xlow))
		total_stat_dn_data_chain = total_stat_dn_data1_chain.Rebin(13,"total_stat_dn_data_chain",array.array('d',xlow))

		total_stat_up_mc_chain = total_stat_up_mc1_chain.Rebin(13,"total_stat_up_mc_chain",array.array('d',xlow))
		total_stat_dn_mc_chain = total_stat_dn_mc1_chain.Rebin(13,"total_stat_dn_mc_chain",array.array('d',xlow))

		total_stat_up_mc_data_chain = total_stat_up_mc_data1_chain.Rebin(13,"total_stat_up_mc_data_chain",array.array('d',xlow))
		total_stat_dn_mc_data_chain = total_stat_dn_mc_data1_chain.Rebin(13,"total_stat_dn_mc_data_chain",array.array('d',xlow))

		h_efficiency_simple_subztt_nominal_chain = h_efficiency_simple_subztt_nominal1_chain.Rebin(13,"h_efficiency_simple_subztt_nominal_chain",array.array('d',xlow))

		h_efficiency_simple_mc_nominal_chain = h_efficiency_simple_mc_nominal1_chain.Rebin(13,"h_efficiency_simple_mc_nominal_chain",array.array('d',xlow))

	if str(variable) == "tau_eta":

		xlow = [-2.5,-2.,-1.52,-1.37,-0.5,0,0.5,1.37,1.52,2,2.5]

		total_stat_up_data_chain = total_stat_up_data1_chain.Rebin(10,"total_stat_up_data_chain",array.array('d',xlow))
		total_stat_dn_data_chain = total_stat_dn_data1_chain.Rebin(10,"total_stat_dn_data_chain",array.array('d',xlow))

		total_stat_up_mc_chain = total_stat_up_mc1_chain.Rebin(10,"total_stat_up_mc_chain",array.array('d',xlow))
		total_stat_dn_mc_chain = total_stat_dn_mc1_chain.Rebin(10,"total_stat_dn_mc_chain",array.array('d',xlow))

		total_stat_up_mc_data_chain = total_stat_up_mc_data1_chain.Rebin(10,"total_stat_up_mc_data_chain",array.array('d',xlow))
		total_stat_dn_mc_data_chain = total_stat_dn_mc_data1_chain.Rebin(10,"total_stat_dn_mc_data_chain",array.array('d',xlow))

		h_efficiency_simple_subztt_nominal_chain = h_efficiency_simple_subztt_nominal1_chain.Rebin(10,"h_efficiency_simple_subztt_nominal_chain",array.array('d',xlow))

		h_efficiency_simple_mc_nominal_chain = h_efficiency_simple_mc_nominal1_chain.Rebin(10,"h_efficiency_simple_mc_nominal_chain",array.array('d',xlow))

	if str(variable) == "pileup":
		if str(trax) == "3Track":
			xlow = [0,12.,16.,18.,22.,24.,30.,50.]

			total_stat_up_data_chain = total_stat_up_data1_chain.Rebin(7,"total_stat_up_data_chain",array.array('d',xlow))
			total_stat_dn_data_chain = total_stat_dn_data1_chain.Rebin(7,"total_stat_dn_data_chain",array.array('d',xlow))

			total_stat_up_mc_chain = total_stat_up_mc1_chain.Rebin(7,"total_stat_up_mc_chain",array.array('d',xlow))
			total_stat_dn_mc_chain = total_stat_dn_mc1_chain.Rebin(7,"total_stat_dn_mc_chain",array.array('d',xlow))

			total_stat_up_mc_data_chain = total_stat_up_mc_data1_chain.Rebin(7,"total_stat_up_mc_data_chain",array.array('d',xlow))
			total_stat_dn_mc_data_chain = total_stat_dn_mc_data1_chain.Rebin(7,"total_stat_dn_mc_data_chain",array.array('d',xlow))

			h_efficiency_simple_subztt_nominal_chain = h_efficiency_simple_subztt_nominal1_chain.Rebin(7,"h_efficiency_simple_subztt_nominal_chain",array.array('d',xlow))

			h_efficiency_simple_mc_nominal_chain = h_efficiency_simple_mc_nominal1_chain.Rebin(7,"h_efficiency_simple_mc_nominal_chain",array.array('d',xlow))
		else:
			xlow = [0,12.,16.,18.,20.,22.,24.,30.,50.]

			total_stat_up_data_chain = total_stat_up_data1_chain.Rebin(8,"total_stat_up_data_chain",array.array('d',xlow))
			total_stat_dn_data_chain = total_stat_dn_data1_chain.Rebin(8,"total_stat_dn_data_chain",array.array('d',xlow))

			total_stat_up_mc_chain = total_stat_up_mc1_chain.Rebin(8,"total_stat_up_mc_chain",array.array('d',xlow))
			total_stat_dn_mc_chain = total_stat_dn_mc1_chain.Rebin(8,"total_stat_dn_mc_chain",array.array('d',xlow))

			total_stat_up_mc_data_chain = total_stat_up_mc_data1_chain.Rebin(8,"total_stat_up_mc_data_chain",array.array('d',xlow))
			total_stat_dn_mc_data_chain = total_stat_dn_mc_data1_chain.Rebin(8,"total_stat_dn_mc_data_chain",array.array('d',xlow))

			h_efficiency_simple_subztt_nominal_chain = h_efficiency_simple_subztt_nominal1_chain.Rebin(8,"h_efficiency_simple_subztt_nominal_chain",array.array('d',xlow))

			h_efficiency_simple_mc_nominal_chain = h_efficiency_simple_mc_nominal1_chain.Rebin(8,"h_efficiency_simple_mc_nominal_chain",array.array('d',xlow))

	uppp_chain = 0
	for l in range(0,total_stat_up_data_chain.GetNbinsX()):

		n_bin_chain = total_stat_up_data_chain.GetBinCenter(l+1)
		print n_bin_chain
		stat_up_data_chain = graph_efficiency_simple_subztt_nominal_chain.GetEYhigh()[l-uppp_chain]
		stat_dn_data_chain = graph_efficiency_simple_subztt_nominal_chain.GetEYlow()[l-uppp_chain]
		stat_up_mc_chain = graph_efficiency_simple_mc_nominal_chain.GetEYhigh()[l-uppp_chain]
		stat_dn_mc_chain = graph_efficiency_simple_mc_nominal_chain.GetEYlow()[l-uppp_chain]
		data_y_val_chain = graph_efficiency_simple_subztt_nominal_chain.GetY()[l-uppp_chain]
		mc_y_val_chain = graph_efficiency_simple_mc_nominal_chain.GetY()[l-uppp_chain]

		if str(variable) == "tau_eta":
			if n_bin_chain == -1.445:
				print "setting to 0"
				total_stat_up_mc_chain.SetBinContent(l+1, 0)
				total_stat_dn_mc_chain.SetBinContent(l+1, 0)

				total_stat_up_data_chain.SetBinContent(l+1, 0)
				total_stat_dn_data_chain.SetBinContent(l+1, 0)

				h_efficiency_simple_subztt_nominal_chain.SetBinContent(l+1, 0)
				h_efficiency_simple_mc_nominal_chain.SetBinContent(l+1, 0)

				total_stat_up_mc_chain.SetBinContent(l+1, 0)
				total_stat_dn_mc_chain.SetBinContent(l+1, 0)
				uppp_chain = 1



			elif n_bin_chain == 1.445:
				total_stat_up_mc_chain.SetBinContent(l+1, 0)
				total_stat_dn_mc_chain.SetBinContent(l+1, 0)

				total_stat_up_data_chain.SetBinContent(l+1, 0)
				total_stat_dn_data_chain.SetBinContent(l+1, 0)

				h_efficiency_simple_subztt_nominal_chain.SetBinContent(l+1, 0)
				h_efficiency_simple_mc_nominal_chain.SetBinContent(l+1, 0)

				total_stat_up_mc_chain.SetBinContent(l+1, 0)
				total_stat_dn_mc_chain.SetBinContent(l+1, 0)
				uppp_chain = 2
				continue

			else:
				total_stat_up_mc_chain.SetBinContent(l+1, stat_up_mc_chain)
				total_stat_dn_mc_chain.SetBinContent(l+1, stat_dn_mc_chain)

				total_stat_up_data_chain.SetBinContent(l+1, stat_up_data_chain)
				total_stat_dn_data_chain.SetBinContent(l+1, stat_dn_data_chain)

				h_efficiency_simple_subztt_nominal_chain.SetBinContent(l+1, data_y_val_chain)
				h_efficiency_simple_mc_nominal_chain.SetBinContent(l+1, mc_y_val_chain)

				total_stat_up_mc_chain.SetBinContent(l+1, stat_up_mc_chain)
				total_stat_dn_mc_chain.SetBinContent(l+1, stat_dn_mc_chain)

		elif str(variable) == "tau_pt":

			total_stat_up_mc_chain.SetBinContent(l+1, stat_up_mc_chain)
			total_stat_dn_mc_chain.SetBinContent(l+1, stat_dn_mc_chain)

			total_stat_up_data_chain.SetBinContent(l+1, stat_up_data_chain)
			total_stat_dn_data_chain.SetBinContent(l+1, stat_dn_data_chain)

			h_efficiency_simple_subztt_nominal_chain.SetBinContent(l+1, data_y_val_chain)
			h_efficiency_simple_mc_nominal_chain.SetBinContent(l+1, mc_y_val_chain)

		elif str(variable) == "pileup":

			total_stat_up_mc_chain.SetBinContent(l+1, stat_up_mc_chain)
			total_stat_dn_mc_chain.SetBinContent(l+1, stat_dn_mc_chain)

			total_stat_up_data_chain.SetBinContent(l+1, stat_up_data_chain)
			total_stat_dn_data_chain.SetBinContent(l+1, stat_dn_data_chain)

			h_efficiency_simple_subztt_nominal_chain.SetBinContent(l+1, data_y_val_chain)
			h_efficiency_simple_mc_nominal_chain.SetBinContent(l+1, mc_y_val_chain)

	print "******** data_chain"
	h_efficiency_simple_subztt_nominal_chain.Print("all")
	print "******** mc_chain"
	h_efficiency_simple_mc_nominal_chain.Print("all")

	hists_file = ROOT.TFile('hists_chain.root')
	h_efficiency_simple_subztt_nominal = hists_file.Get('data_nom')
	h_efficiency_simple_mc_nominal = hists_file.Get('mc_nom')
	total_stat_up_data = hists_file.Get('total_stat_up_data')
	total_stat_dn_data = hists_file.Get('total_stat_dn_data')
        total_stat_up_mc = hists_file.Get('total_stat_up_mc')
        total_stat_dn_mc = hists_file.Get('total_stat_dn_mc')
        total_up_data = hists_file.Get('total_up_data')
        total_dn_data = hists_file.Get('total_dn_data')

        print "******** data"
        h_efficiency_simple_subztt_nominal.Print("all")
        print "******** mc"
        h_efficiency_simple_mc_nominal.Print("all")

	data_stat_tot = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal,total_stat_up_data,total_stat_dn_data)
	data_stat_chain = funcs.make_error_scatter_graph(h_efficiency_simple_subztt_nominal_chain,total_stat_up_data_chain,total_stat_dn_data_chain)
	mc_stat_tot= funcs.make_error_scatter_graph(h_efficiency_simple_mc_nominal,total_stat_up_mc,total_stat_dn_mc)
	mc_stat_chain = funcs.make_error_scatter_graph(h_efficiency_simple_mc_nominal_chain,total_stat_up_mc_chain,total_stat_dn_mc_chain)
	if str(variable) == "tau_eta":
		for i in range(h_efficiency_simple_subztt_nominal.GetNbinsX()):
			val_trig = data_stat_tot.GetY()[i]
			val_chain = data_stat_chain.GetY()[i]
			if val_trig == 0:
				print "removing"
				data_stat_tot.RemovePoint(i)
			if val_chain == 0:
				print "removing"
				data_stat_chain.RemovePoint(i)
	mc_stat_tot.Print("all")

	data_stat_tot.SetMarkerColor(ROOT.kBlue)
	mc_stat_tot.SetMarkerColor(ROOT.kBlue)
	data_stat_chain.SetMarkerColor(ROOT.kRed)
	mc_stat_chain.SetMarkerColor(ROOT.kRed)

        data_stat_tot.SetLineColor(ROOT.kBlue)
        mc_stat_tot.SetLineColor(ROOT.kBlue)
        data_stat_chain.SetLineColor(ROOT.kRed)
        mc_stat_chain.SetLineColor(ROOT.kRed)

        data_stat_tot.SetMarkerStyle(20)
        data_stat_chain.SetMarkerStyle(20)
        mc_stat_tot.SetFillColor(ROOT.kBlue)
        mc_stat_chain.SetFillColor(ROOT.kRed)

        mc_stat_tot.SetFillStyle(3395)
        mc_stat_chain.SetFillStyle(3395)
	data_stat_tot.SetLineWidth(2)
	data_stat_chain.SetLineWidth(2)

        """
        for k in range(h_efficiency_simple_subztt_nominal.GetNbinsX()+1):
            tot_val = h_efficiency_simple_subztt_nominal_chain.GetBinContent(k)
            trig_val = h_efficiency_simple_subztt_nominal.GetBinContent(k)
            if trig_val<0:
                trig_val = 0
                data_post.SetBinContent(k,0)
            if trig_val>tot_val:
                h_efficiency_simple_subztt_nominal_chain.SetBinContent(k,trig_val)
                trig_err = h_efficiency_simple_subztt_nominal.GetBinError(k)
                h_efficiency_simple_subztt_nominal_chain.SetBinError(k,trig_err)


        h_ratio_chain = ROOT.TGraphAsymmErrors()
        h_ratio_chain.Divide(h_efficiency_simple_subztt_nominal,h_efficiency_simple_subztt_nominal_chain,"cl=0.683 b(1,1) mode")
        h_ratio_chain.SetName("h_ratio_chain")

        """
	h_data = h_efficiency_simple_subztt_nominal.Clone()
	h_ratio_chain = h_data.Clone()
	h_ratio_chain.Divide(h_efficiency_simple_subztt_nominal_chain)
	h_ratio_chain.SetName("h_ratio_chain")

        h_ratio_chain.SetMarkerColor(ROOT.kBlack)

	#ratio_plot.Print("all")

        print "*************************************************************** !!!!!!!!!!!!!!!!!!!!!!!!"
        if str(variable) == "tau_pt":
            for k in range(0,h_ratio_chain.GetNbinsX()+1):
                up_unc = math.sqrt(total_up_data.GetBinContent(k)**2 + total_stat_up_data_chain.GetBinContent(k)**2)
                print k, h_ratio_chain.GetBinContent(k), up_unc
                if h_ratio_chain.GetBinContent(k) > 1:
                        h_ratio_chain.SetBinContent(k,1)
                        total_up_data.SetBinContent(k,0)
                        total_stat_up_data_chain.SetBinContent(k,0)
                elif h_ratio_chain.GetBinContent(k) + math.sqrt(total_up_data.GetBinContent(k)**2 + total_stat_up_data_chain.GetBinContent(k)**2) > 1:
                        print "going over", k, h_ratio_chain.GetBinContent(k),math.sqrt(total_up_data.GetBinContent(k)**2 + total_stat_up_data_chain.GetBinContent(k)**2)
                        total_up_data.SetBinContent(k,0)
                        total_stat_up_data_chain.SetBinContent(k,1-h_ratio_chain.GetBinContent(k))
                        #print "going over", k, h_ratio_chain.GetBinContent(k), total_stat_up_data_chain
            for l in range(0,MC_ratio_plot.GetNbinsX()+1):
                if MC_ratio_plot.GetBinContent(l) > 1:
                        MC_ratio_plot.SetBinContent(l,1)
                        total_stat_up_mc.SetBinContent(l,0)
                        total_stat_up_mc_chain.SetBinContent(l,0)
                elif MC_ratio_plot.GetBinContent(l) + math.sqrt(total_stat_up_mc.GetBinContent(l)**2 + total_stat_up_mc_chain.GetBinContent(l)**2) > 1:
                        total_stat_up_mc.SetBinContent(l,0)
                        total_stat_up_mc_chain.SetBinContent(l,1-MC_ratio_plot.GetBinContent(l))


	#h_ratio_graph_chain = funcs.combination_ratio_stats(h_ratio_chain,eff_ratio_num,eff_ratio_den,total_stat_up_data,total_stat_dn_data,total_stat_up_data_chain,total_stat_dn_data_chain)

	h_ratio_graph_chain = funcs.combination_ratio_stats(h_ratio_chain,eff_ratio_num,eff_ratio_den,total_up_data,total_dn_data,total_stat_up_data_chain,total_stat_dn_data_chain)
        h_ratio_graph_chain.SetMarkerColor(ROOT.kBlack)

	h_ratio_graph_chain.SetMarkerStyle(20)
	h_ratio_graph_chain.SetLineWidth(2)

	h_ratio_MC_graph_chain = funcs.combination_ratio_stats(MC_ratio_plot,MC_eff_ratio_num,MC_eff_ratio_den,total_stat_up_mc,total_stat_dn_mc,total_stat_up_mc_chain,total_stat_dn_mc_chain)
	h_ratio_MC_graph_chain.SetFillColor(ROOT.kRed)
	h_ratio_MC_graph_chain.SetFillStyle(3001)

	h_ratio_MC_graph_chain.SetMarkerStyle(20)
	h_ratio_MC_graph_chain.SetLineWidth(2)
	h_ratio_MC_graph_chain.SetMarkerColor(ROOT.kRed)
	h_ratio_MC_graph_chain.SetLineColor(ROOT.kRed)
	if str(variable) == "tau_eta":
		for i in range(h_efficiency_simple_subztt_nominal.GetNbinsX()):
			val_data_c = h_ratio_graph_chain.GetY()[i]
			val_mc_c = h_ratio_MC_graph_chain.GetY()[i]
			if val_data_c== 0:
				print "removing"
				h_ratio_graph_chain.RemovePoint(i)
			if val_mc_c == 0:
				print "removing"
				h_ratio_MC_graph_chain.RemovePoint(i)

        nLegend = 2
	x_legend = 0.63
	x_leg_shift = 0
	y_leg_shift = 0.0
	legYCompr = 8.0
	#legYMax = 0.5
	#legYMin = legYMax - (legYMax - (0.2 + y_leg_shift)) / legYCompr * nLegend
	#legXMin = x_legend + x_leg_shift
	#legXMax = legXMin + 0.4
	leg = ROOT.TLegend(0.45,0.15,0.87,0.33)
	leg.SetBorderSize(0)
	leg.SetTextSize(0.038)
	leg.SetNColumns(2)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	if str(chain) == "tracktwo":
		leg.AddEntry(data_stat_chain,"Data w/o BDT",'PL')
		leg.AddEntry(mc_stat_chain, "MC w/o BDT","F")
		leg.AddEntry(data_stat_tot,"Data w BDT", 'PL')
		leg.AddEntry(mc_stat_tot,"MC w BDT","F")
		leg.AddEntry(h_ratio_graph_chain,"BDT eff. in data", 'PL')
		leg.AddEntry(h_ratio_MC_graph_chain,"BDT eff. in MC", 'F')
        if str(chain) == "ptonly":
                leg.AddEntry(data_stat_chain,"Data w/o trk",'PL')
                leg.AddEntry(mc_stat_chain, "MC w/o trk","F")
                leg.AddEntry(data_stat_tot,"Data w trk", 'PL')
                leg.AddEntry(mc_stat_tot,"MC w trk","F")
		leg.AddEntry(h_ratio_graph_chain,"Trk. eff. in data", 'PL')
		leg.AddEntry(h_ratio_MC_graph_chain,"Trk. eff. in MC", 'F')
        if str(chain) == "L1TAU12IMmed":
                leg.AddEntry(data_stat_chain,"Data w/o p_{T} cut",'PL')
                leg.AddEntry(mc_stat_chain, "MC w/o p_{T} cut","F")
                leg.AddEntry(data_stat_tot,"Data w p_{T} cut", 'PL')
                leg.AddEntry(mc_stat_tot,"MC w p_{T} cut","F")
		leg.AddEntry(h_ratio_graph_chain,"p_{T} eff. in data", 'PL')
		leg.AddEntry(h_ratio_MC_graph_chain,"p_{T} eff. in MC", 'F')

	c_chain = ROOT.TCanvas(str(variable)+"_"+str(trax)+"_trigchain_efficiency",str(variable)+"_"+str(trax)+"_trigchain_efficiency",600,600)
	xmin = h_efficiency_simple_subztt_nominal_chain.GetBinLowEdge(1)
	xmax = 300
	ymin = 0
	ymax = 1.1

	xtitle = ""

	rsplit = 0.3
	pad1_chain = ROOT.TPad("pad1_chain","top pad",0.,rsplit,1.,1.)
	pad1_chain.SetLeftMargin(0.15)
	pad1_chain.SetTicky()
	pad1_chain.SetTickx()
	pad1_chain.SetBottomMargin(0.1)
	if str(variable) == "tau_pt":
		pad1_chain.SetLogx()
	pad1_chain.Draw()

	pad2_chain = ROOT.TPad("pad2_chain","bottom pad",0,0,1,rsplit)
	pad2_chain.SetTopMargin(0.02)
	pad2_chain.SetBottomMargin(0.40)
	pad2_chain.SetLeftMargin(0.15)
	pad2_chain.SetTicky()
	pad2_chain.SetTickx()
	#pad2_chain.SetGridy()
	if str(variable) == "tau_pt":
		pad2_chain.SetLogx()
	pad2_chain.Draw()
	pad1_chain.cd()

	ytitle = "Efficiency"

	fr1_chain = pad1_chain.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
	fr1_chain.GetXaxis().SetTitleSize(0)
	fr1_chain.GetXaxis().SetLabelSize(0)
	xaxis1_chain = fr1_chain.GetXaxis()
	xaxis1_chain.SetRangeUser(25,300)
	yaxis1_chain = fr1_chain.GetYaxis()
	scale = (1.3+rsplit)
	yaxis1_chain.SetTitleSize( yaxis1_chain.GetTitleSize() * scale )
	yaxis1_chain.SetTitleOffset( 1 )
	yaxis1_chain.SetLabelSize( 0.8 * yaxis1_chain.GetLabelSize() * scale )
	yaxis1_chain.SetLabelOffset( 1. * yaxis1_chain.GetLabelOffset() / scale )
	xaxis1_chain.SetNdivisions(510)
	yaxis1_chain.SetNdivisions(510)
	yaxis1_chain.SetTitle("Efficiency")

	tot_eff_chain = ROOT.TMultiGraph()
        tot_eff_chain.Add(mc_stat_chain,"E2")
        tot_eff_chain.Add(mc_stat_tot,"E2")
        tot_eff_chain.Add(data_stat_chain,"APZ")
        tot_eff_chain.Add(data_stat_tot,"APZ")

	tot_eff_chain.Draw("a")
	xaxis_top_chain = tot_eff_chain.GetXaxis()
	yaxis_top_chain = tot_eff_chain.GetYaxis()

	if str(variable) == "tau_pt":
		if "50" in str(trig):
			xaxis_top_chain.SetRangeUser(50,300)
		elif "80" in str(trig):
			xaxis_top_chain.SetRangeUser(80,300)
		elif ("125" in str(trig)) or ("160" in str(trig)):
			xaxis_top_chain.SetRangeUser(100,300)
		else:
		     	xaxis_top_chain.SetRangeUser(25,300)
	        xaxis_top_chain.SetMoreLogLabels()
	if str(variable) == "tau_eta":
	     xaxis_top_chain.SetRangeUser(-3,3)
	if str(variable) == "pileup":
	     xaxis_top_chain.SetRangeUser(0,50)

	yaxis_top_chain.SetTitleSize(0.045)# yaxis_top_chain.GetTitleSize() * scale )
	yaxis_top_chain.SetTitleOffset( 1 )
	yaxis_top_chain.SetLabelSize(0.045)#( 0.8 * yaxis_top_chain.GetLabelSize() * scale )
	yaxis_top_chain.SetLabelOffset( 1. * yaxis_top_chain.GetLabelOffset() / scale )
	xaxis_top_chain.SetNdivisions(510)
	xaxis_top_chain.SetNoExponent()
	yaxis_top_chain.SetNdivisions(510)
	yaxis_top_chain.SetTitle("Trigger Efficiency")
	yaxis_top_chain.SetRangeUser(0,1.05)
        #xaxis_top_chain.SetMoreLogLabels()
        xaxis_top_chain.SetLabelSize(0.045)
	leg.Draw()
	pad1_chain.RedrawAxis()
	tlatex = ROOT.TLatex()
	tlatex.SetNDC()
	tlatex.SetTextSize(0.05)
	lx = 0.5
	ly = 0.845
	tlatex.SetTextFont(42)

	ty = 0.4
	th = 0.1
	tx = 0.5
	latex_y = ty-2.*th
	latex_yb = ty-4.*th

	tlatex.SetTextSize(0.038)
	tlatex.SetTextFont(42)
	tlatex.DrawLatex(0.45,0.55,"#bf{#it{ATLAS}} Internal")
	tlatex.DrawLatex(0.45,0.47,'33.3 fb^{-1}, #sqrt{s} = 13 TeV' )
	#tlatex.DrawLatex(0.5,0.20,'HLT_tau25_medium1_tracktwo')
	if trax:
		if str(trax) == '1Track':
			if str(bdt) == "medium":
				tlatex.DrawLatex(0.45,0.41,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, 1-prong')
			else:
				tlatex.DrawLatex(0.45,0.41,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, 1-prong, BDT '+str(bdt))
		elif str(trax) == '3Track':
			if str(bdt) == "medium":
				tlatex.DrawLatex(0.45,0.41,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, 3-prong')
			else:
				tlatex.DrawLatex(0.45,0.41,'Z#rightarrow#tau_{#mu}#tau_{had} T&P, 3-prong, BDT '+str(bdt))

	pad2_chain.cd()

	fr2_chain = pad2_chain.DrawFrame(xmin,0.8,xmax,1.2,';%s;Data/exp.'%('Offline Tau P_{T} [GeV]'))

	xaxis2_chain = fr2_chain.GetXaxis()
	yaxis2_chain = fr2_chain.GetYaxis()

	scale = (1. / rsplit)
	yaxis2_chain.SetTitleSize( yaxis2_chain.GetTitleSize() * scale )
	yaxis2_chain.SetLabelSize( yaxis2_chain.GetLabelSize() * scale )
	yaxis2_chain.SetTitleOffset( 2.1* yaxis2_chain.GetTitleOffset() / scale  )
	yaxis2_chain.SetLabelOffset(0.2 * yaxis2_chain.GetLabelOffset() * scale )
	xaxis2_chain.SetTitleSize( xaxis2_chain.GetTitleSize() * scale )
	xaxis2_chain.SetLabelSize( 0.8 * xaxis2_chain.GetLabelSize() * scale )
	xaxis2_chain.SetTickLength( xaxis2_chain.GetTickLength() * scale )
	xaxis2_chain.SetTitleOffset(0.5)
	xaxis2_chain.SetLabelOffset( 2.5* xaxis2_chain.GetLabelOffset() / scale )
	xaxis2_chain.SetRangeUser(25,300)
	yaxis2_chain.SetRangeUser(0.6,1.4)
	yaxis2_chain.SetNdivisions(4)
	xaxis2_chain.SetNdivisions(510)
	#xaxis2_chain.SetMoreLogLabels()
	xaxis2_chain.SetTitleOffset(1)
	#yaxis2_chain.SetTitle("Data/exp.")
	yaxis2_chain.SetTitleOffset(0.5)

	#ratio_line_chain = ROOT.TLine(h_ratio_chain.GetBinLowEdge(1),1,h_ratio_chain.GetBinLowEdge(h_ratio_chain.GetNbinsX()+1),1)
	#ratio_line_chain.SetLineColor(ROOT.kRed)
	#ratio_line_chain.SetLineStyle(7)

	#ratio_line_chain.Draw()

	tot_ratio_chain = ROOT.TMultiGraph()
	tot_ratio_chain.Add(h_ratio_MC_graph_chain,"E2")
	tot_ratio_chain.Add(h_ratio_MC_graph_chain,"APZ")
	tot_ratio_chain.Add(h_ratio_graph_chain,"APZ")
        tot_ratio_chain.Draw("a Same")


	xaxis_bot_chain = tot_ratio_chain.GetXaxis()
	yaxis_bot_chain = tot_ratio_chain.GetYaxis()
	#yaxis_bot_chain.SetTitleSize( yaxis_bot_chain.GetTitleSize() * scale )
	#yaxis_bot_chain.SetLabelSize( yaxis_bot_chain.GetLabelSize() * scale )
	yaxis_bot_chain.SetTitleOffset( 2.1* yaxis_bot_chain.GetTitleOffset() / scale  )
	yaxis_bot_chain.SetLabelOffset(0.2 * yaxis_bot_chain.GetLabelOffset() * scale )
	#xaxis_bot_chain.SetTitleSize( xaxis_bot_chain.GetTitleSize() * scale )
	#xaxis_bot_chain.SetLabelSize( 0.8 * xaxis_bot_chain.GetLabelSize() * scale )
	xaxis_bot_chain.SetTickLength( xaxis_bot_chain.GetTickLength() * scale )
	xaxis_bot_chain.SetNoExponent()
	xaxis_bot_chain.SetTitleOffset(0.5)
	xaxis_bot_chain.SetLabelOffset( 2.5* xaxis_bot_chain.GetLabelOffset() / scale )
	xaxis_bot_chain.SetTitleSize( 0.1)#xaxis_bot.GetTitleSize() * scale )
	xaxis_bot_chain.SetLabelSize( 0.1)# * xaxis_bot.GetLabelSize() * scale )
	if str(variable) == "tau_pt":
		if "50" in str(trig):
			xaxis_bot_chain.SetRangeUser(50,300)
		elif "80" in str(trig):
			xaxis_bot_chain.SetRangeUser(80,300)
		elif ("125" in str(trig)) or ("160" in str(trig)):
			xaxis_bot_chain.SetRangeUser(100,300)
		else:
	     		xaxis_bot_chain.SetRangeUser(25,300)
	     	xaxis_bot_chain.SetTitle('Offline Tau P_{T} [GeV]')
	    	xaxis_bot_chain.SetMoreLogLabels()
	if str(variable) == "tau_eta":
             xaxis_bot_chain.SetRangeUser(-3,3)
	     xaxis_bot_chain.SetTitle('Offline Tau #eta')
	if str(variable) == "pileup":
             xaxis_bot_chain.SetRangeUser(0,50)
	     xaxis_bot_chain.SetTitle('#mu')
	#yaxis_bot_chain.SetRangeUser(0.6,1.4)
	yaxis_bot_chain.SetNdivisions(4)
	yaxis_bot_chain.SetLabelSize( 0.1)
	yaxis_bot_chain.SetTitleSize( 0.1)
	xaxis_bot_chain.SetNdivisions(510)
	xaxis_bot_chain.SetTitleOffset(1)
	if str(trig) == "25med" and str(chain) == "tracktwo":
	     yaxis_bot_chain.SetTitle("BDT Eff.")
	elif str(trig) == "tracktwo" and str(chain) == "ptonly":
	     yaxis_bot_chain.SetTitle("Trk Eff.")
	elif str(trig) == "ptonly" and str(chain) == "L1TAU12IMmed":
	     yaxis_bot_chain.SetTitle("P_{T} Cut Eff.")
	yaxis_bot_chain.SetTitleOffset(0.5)


	pad2_chain.RedrawAxis()
	print str(trig), str(chain)
	if trax:
		if str(trig) == "25med" and str(chain) == "tracktwo":
			plotsfile = os.path.join("./","eff_"+str(variable)+"_BDT_tau25med_"+str(trax)+"_"+str(bdt)+"_SYS.root")
                        h_ratio_MC_graph_chain.SetName("BDT_mc_"+str(trax))
			h_ratio_graph_chain.SetName("BDT_data_"+str(trax))
                elif str(trig) == "tracktwo" and str(chain) == "ptonly":
                        plotsfile = os.path.join("./","eff_"+str(variable)+"_tracking_tau25med_"+str(trax)+"_"+str(bdt)+"_SYS.root")
                        h_ratio_MC_graph_chain.SetName("tracking_mc_"+str(trax))
			h_ratio_graph_chain.SetName("tracking_data_"+str(trax))

                elif str(trig) == "ptonly" and str(chain) == "L1TAU12IMmed":
                        plotsfile = os.path.join("./","eff_"+str(variable)+"_ptcut_tau25med_"+str(trax)+"_"+str(bdt)+"_SYS.root")
                        h_ratio_MC_graph_chain.SetName("ptcut_mc_"+str(trax))
			h_ratio_graph_chain.SetName("ptcut_data_"+str(trax))
	else:
		plotsfile = os.path.join("./","eff_inclusive_"+str(trig)+"_"+str(chain)+"_SYS.root")
	#c.SaveAs("Test")
	fout = ROOT.TFile.Open(plotsfile,'UPDATE')
	fout.WriteTObject(c_chain)
	fout.Close()

        #data_sys_ratio_error_plot_chain = funcs.make_error_scatter_graph(h_ratio_graph_chain, total_sys_up_data,total_sys_dn_data)
        #data_sys_ratio_error_plot_chain.SetName("sys_"+str(trig)+str(trax))
        #print "writing", data_sys_ratio_error_plot_chain.Name()

        trig_effs = ROOT.TFile("./trigger_chain_effiencies.root", "update")
	h_ratio_MC_graph_chain.Write()
	h_ratio_graph_chain.Write()
        #data_sys_ratio_error_plot_chain.Write()
        trig_effs.Close()

if str(trig) == "L1TAU12IMmed":
	trig_effs = ROOT.TFile("./trigger_chain_effiencies.root", "update")

	data_stat_error_plot.SetName("L1_data_stat_"+str(trax))
	data_sys_error_plot.SetName("L1_data_sys_"+str(trax))
	graph_efficiency_simple_mc_nominal.SetName("L1_eff_MC_"+str(trax))
	graph_efficiency_simple_subztt_nominal.SetName("L1_eff_data_"+str(trax))
        g_tot_error_plot.SetName("L1_tot_unc_"+str(trax))

        g_tot_error_plot.Write()
	data_stat_error_plot.Write()
	data_sys_error_plot.Write()
	graph_efficiency_simple_mc_nominal.Write()
	graph_efficiency_simple_subztt_nominal.Write()

	trig_effs.Close()

"""
if str(trig) == "ptonly":
        print "********************************** WRITING PT ONLY ****************************************"
        trig_effs = ROOT.TFile("./trigger_chain_effiencies.root", "update")
        data_sys_error_plot.SetName("ptonly"+str(trax))
        data_sys_error_plot.Write()
	trig_effs.Close()
if str(trig) == "tracktwo":
        trig_effs = ROOT.TFile("./trigger_chain_effiencies.root", "update")
        data_sys_error_plot.SetName("tracktwo"+str(trax))
        data_sys_error_plot.Write()
	trig_effs.Close()
if str(trig) == "25med":
	trig_effs = ROOT.TFile("./trigger_chain_effiencies.root", "update")
        data_sys_error_plot.SetName("25med"+str(trax))
        data_sys_error_plot.Write()
	trig_effs.Close()
"""




