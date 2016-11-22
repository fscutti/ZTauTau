import ROOT

import array
#import histmgr
import funcs
import os
import math
from pyplot import histutils
from ztautau.samples import samples
from ztautau.plots   import vars
#from systematics     import *

sign = "os"
#sign = "ss"
#trax = "1"
#trax = "3"
trax = None
trig = "25med"
#trig = None
"""
a = ROOT.TFile('../../test/hists_tau_pt_SR.root')
a_my_est1 = a.Get('h_SR_nominal_Wjets')

b = ROOT.TFile('../../test/hists_tau_pt_SR_lowSCDP_lowMT.root')
b_mc1 = b.Get('h_SR_lowSCDP_lowMT_nominal_Wjets')

#a = ROOT.TFile('../../test/hists_tau_pt_SR_highSCDP_highMT.root')
#a_my_est1 = a.Get('h_SR_highSCDP_highMT_nominal_Wjets')

#b = ROOT.TFile('../../test/hists_tau_pt_SR_lowSCDP_highMT.root')
#b_mc1 = b.Get('h_SR_lowSCDP_highMT_nominal_Wjets')
"""
"""
c = ROOT.TFile('myest_incl_rqcd_hists_tau_pt_SR.root')
c_my_est1 = c.Get('h_SR_nominal_Wjets')

d = ROOT.TFile('mc_incl_rqcd_hists_tau_pt_SR.root')
d_mc1 = d.Get('h_SR_nominal_Wjets')

e = ROOT.TFile('mc_incl_rqcd_hists_tau_pt_Wjets_OS.root')
e_mc1 = e.Get('h_Wjets_OS_nominal_Wjets')

f = ROOT.TFile('myest_incl_rqcd_hists_tau_pt_Wjets_OS.root')
f_my_est1 = f.Get('h_Wjets_OS_nominal_Wjets')

g = ROOT.TFile('myest_hists_tau_pt_SR.root')
g_my_est1 = g.Get('h_SR_nominal_Wjets')

h = ROOT.TFile('mc_hists_tau_pt_SR.root')
h_mc1 = h.Get('h_SR_nominal_Wjets')
"""
#############
"""
a_my_est = a_my_est1.Clone()
b_mc = b_mc1.Clone()
"""
"""
c_my_est = c_my_est1.Clone()
d_mc = d_mc1.Clone()
e_mc = e_mc1.Clone()
f_my_est = f_my_est1.Clone()
g_my_est = g_my_est1.Clone()
h_mc = h_mc1.Clone()
"""
"""
a_my_est_int, a_err = histutils.full_integral_and_error(a_my_est)
b_mc_int, b_err = histutils.full_integral_and_error(b_mc)
print a_my_est_int/b_mc_int
c = a_my_est_int/b_mc_int
print a_my_est_int, a_err
print b_mc_int, b_err
print c
tot_err = c*math.sqrt((a_err/a_my_est_int)**2 + (b_err/b_mc_int)**2)
print tot_err/c

#a_my_est.Scale(1/a_my_est_int)
#b_mc.Scale(1/b_mc_int)

#a_my_est.SetName('my_est_WjetsOS')
#b_mc.SetName('mc_WjetsOS')
"""
"""
c_my_est_int = histutils.full_integral(c_my_est)
d_mc_int = histutils.full_integral(d_mc)

c_my_est.Scale(1/c_my_est_int)
d_mc.Scale(1/d_mc_int)

c_my_est.SetName('my_est_SR_inclrqcd')
d_mc.SetName('mc_SR_inclrqcd')
#######################
f_my_est_int = histutils.full_integral(f_my_est)
e_mc_int = histutils.full_integral(e_mc)

f_my_est.Scale(1/f_my_est_int)
e_mc.Scale(1/e_mc_int)

f_my_est.SetName('my_est_Wjets_incl')
e_mc.SetName('mc_Wjets_incl')

g_my_est_int = histutils.full_integral(g_my_est)
h_mc_int = histutils.full_integral(h_mc)

g_my_est.Scale(1/g_my_est_int)
h_mc.Scale(1/h_mc_int)

g_my_est.SetName('my_est_SR_ptbin')
h_mc.SetName('mc_SR_ptbin')
"""
"""
outfile = ROOT.TFile('scaled_hists.root','recreate')
a_my_est.Write()
b_mc.Write()
#c_my_est.Write()
#d_mc.Write()
#f_my_est.Write()
#e_mc.Write()
#g_my_est.Write()
#h_mc.Write()
outfile.Close()

"""

########------------------ COMPARING LSCDP ESTIMATE -------------------

if trax == "1":
	sr_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_Tau1Track.root')
	sr1 = sr_file.Get('h_SR_Tau1Track_nominal_Wjets')

	lscdp_lowmt_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT_Tau1Track.root')
	lscdp_lowmt1 = lscdp_lowmt_file.Get('h_SR_lowSCDP_lowMT_Tau1Track_nominal_Wjets')

	sr_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_SS_Tau1Track.root')
	sr_ss1 = sr_ss_file.Get('h_SR_SS_Tau1Track_nominal_Wjets')

	lscdp_lowmt_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT_SS_Tau1Track.root')
	lscdp_lowmt_ss1 = lscdp_lowmt_ss_file.Get('h_SR_lowSCDP_lowMT_SS_Tau1Track_nominal_Wjets')

	sr2 = sr1.Clone()
	lscdp_lowmt2 = lscdp_lowmt1.Clone()

	sr_ss2 = sr_ss1.Clone()
	lscdp_lowmt_ss2 = lscdp_lowmt_ss1.Clone()

	sr_int = histutils.full_integral(sr2)
	lscdp_lowmt_int = histutils.full_integral(lscdp_lowmt2)

	sr_ss_int = histutils.full_integral(sr_ss2)
	lscdp_lowmt_ss_int = histutils.full_integral(lscdp_lowmt_ss2)

	sr2.Scale(1/sr_int)
	lscdp_lowmt2.Scale(1/lscdp_lowmt_int)

	sr_ss2.Scale(1/sr_ss_int)
	lscdp_lowmt_ss2.Scale(1/lscdp_lowmt_ss_int)

	outfile = ROOT.TFile('./Wjets_new_est_verification/Wjets_SR_LSCDP_comparison_1Track.root','recreate')
	sr2.Write()
	lscdp_lowmt2.Write()
	sr_ss2.Write()
	lscdp_lowmt_ss2.Write()
	outfile.Close()

elif trax == "3":
	sr_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_Tau3Track.root')
	sr1 = sr_file.Get('h_SR_Tau3Track_nominal_Wjets')

	lscdp_lowmt_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT_Tau3Track.root')
	lscdp_lowmt1 = lscdp_lowmt_file.Get('h_SR_lowSCDP_lowMT_Tau3Track_nominal_Wjets')

	sr_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_SS_Tau3Track.root')
	sr_ss1 = sr_ss_file.Get('h_SR_SS_Tau3Track_nominal_Wjets')

	lscdp_lowmt_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT_SS_Tau3Track.root')
	lscdp_lowmt_ss1 = lscdp_lowmt_ss_file.Get('h_SR_lowSCDP_lowMT_SS_Tau3Track_nominal_Wjets')

	sr2 = sr1.Clone()
	lscdp_lowmt2 = lscdp_lowmt1.Clone()

	sr_ss2 = sr_ss1.Clone()
	lscdp_lowmt_ss2 = lscdp_lowmt_ss1.Clone()

	sr_int = histutils.full_integral(sr2)
	lscdp_lowmt_int = histutils.full_integral(lscdp_lowmt2)

	sr_ss_int = histutils.full_integral(sr_ss2)
	lscdp_lowmt_ss_int = histutils.full_integral(lscdp_lowmt_ss2)

	sr2.Scale(1/sr_int)
	lscdp_lowmt2.Scale(1/lscdp_lowmt_int)

	sr_ss2.Scale(1/sr_ss_int)
	lscdp_lowmt_ss2.Scale(1/lscdp_lowmt_ss_int)

	outfile = ROOT.TFile('./Wjets_new_est_verification/Wjets_SR_LSCDP_comparison_3Track.root','recreate')
	sr2.Write()
	lscdp_lowmt2.Write()
	sr_ss2.Write()
	lscdp_lowmt_ss2.Write()
	outfile.Close()

else:
	if trig:
		sr_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_25med.root')
		sr1 = sr_file.Get('h_SR_25med_nominal_Wjets')

		lscdp_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_25med.root')
		lscdp1 = lscdp_file.Get('h_SR_lowSCDP_25med_nominal_Wjets')

		lscdp_lowmt_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT.root')
		lscdp_lowmt1 = lscdp_lowmt_file.Get('h_SR_lowSCDP_lowMT_nominal_Wjets')


		sr_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_SS25med.root')
		sr_ss1 = sr_ss_file.Get('h_SR_SS25med_nominal_Wjets')

		lscdp_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_SS25med.root')
		lscdp_ss1 = lscdp_ss_file.Get('h_SR_lowSCDP_SS25med_nominal_Wjets')

		lscdp_lowmt_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP_lowMT_SS.root')
		lscdp_lowmt_ss1 = lscdp_lowmt_ss_file.Get('h_SR_lowSCDP_lowMT_SS_nominal_Wjets')

	else:
		sr_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR.root')
		sr1 = sr_file.Get('h_SR_nominal_Wjets')
		lscdp_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_lowSCDP.root')
		lscdp1 = lscdp_file.Get('h_SR_lowSCDP_nominal_Wjets')

		sr_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_SS.root')
		sr_ss1 = sr_ss_file.Get('h_SR_SS_nominal_Wjets')
		lscdp_ss_file = ROOT.TFile('./Wjets_new_est_verification/hists_tau_pt_SR_SS_lowSCDP.root')
		lscdp_ss1 = lscdp_ss_file.Get('h_SR_SS_lowSCDP_nominal_Wjets')


	sr2 = sr1.Clone()
	#lscdp_lowmt2 = lscdp_lowmt1.Clone()
        lscdp2 = lscdp1.Clone()

	sr_ss2 = sr_ss1.Clone()
	#lscdp_lowmt_ss2 = lscdp_lowmt_ss1.Clone()
	lscdp_ss2 = lscdp_ss1.Clone()

	sr_int = histutils.full_integral(sr2)
	#lscdp_lowmt_int = histutils.full_integral(lscdp_lowmt2)
	lscdp_int = histutils.full_integral(lscdp2)

	sr_ss_int = histutils.full_integral(sr_ss2)
	#lscdp_lowmt_ss_int = histutils.full_integral(lscdp_lowmt_ss2)
	lscdp_ss_int = histutils.full_integral(lscdp_ss2)

	sr2.Scale(1/sr_int)
	#lscdp_lowmt2.Scale(1/lscdp_lowmt_int)
	lscdp2.Scale(1/lscdp_int)

	sr_ss2.Scale(1/sr_ss_int)
	#lscdp_lowmt_ss2.Scale(1/lscdp_lowmt_ss_int)
	lscdp_ss2.Scale(1/lscdp_ss_int)

	outfile = ROOT.TFile('./Wjets_new_est_verification/Wjets_SR_LSCDP_comparison_incl.root','recreate')
	sr2.Write()
	#lscdp_lowmt2.Write()
	lscdp2.Write()
	sr_ss2.Write()
	#lscdp_lowmt_ss2.Write()
	lscdp_ss2.Write()
	outfile.Close()

#xlow = [20,25,30,35,40,45,50,55,60,65,70,75,80]
xlow = [20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80]
sr = sr2.Rebin(15,"sr",array.array('d',xlow))
sr_ss = sr_ss2.Rebin(15,"sr_ss",array.array('d',xlow))
#lscdp_lowmt = lscdp_lowmt2.Rebin(15,"lscdp_lowmt",array.array('d',xlow))
#lscdp_lowmt_ss = lscdp_lowmt_ss2.Rebin(15,"lscdp_lowmt_ss",array.array('d',xlow))
lscdp = lscdp2.Rebin(15,"lscdp",array.array('d',xlow))
lscdp_ss = lscdp_ss2.Rebin(15,"lscdp_ss",array.array('d',xlow))

#sr = sr2.Clone()
#lscdp_lowmt = lscdp_lowmt2.Clone()
#sr_ss = sr_ss2.Clone()
#lscdp_lowmt_ss = lscdp_lowmt_ss2.Clone()

if sign == "ss":
	h_ratio = sr_ss.Clone()
	h_ratio.Divide(lscdp_ss)
	sr_stats = funcs.make_normalised_stat_hist(sr_ss)
	sr_stats_graph = funcs.make_error_scatter_graph(sr_ss,sr_stats,sr_stats)

elif sign == "os":
	h_ratio = sr.Clone()
	h_ratio.Divide(lscdp)
	sr_stats = funcs.make_normalised_stat_hist(sr)
	sr_stats_graph = funcs.make_error_scatter_graph(sr,sr_stats,sr_stats)

sr_stats_graph.SetFillStyle(3004)
sr_stats_graph.SetFillStyle(3004)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerColor(ROOT.kBlack)

yaxistitle = ""

nLegend = 2
x_legend = 0.63
x_leg_shift = 0
y_leg_shift = 0.0
legYCompr = 8.0
legYMax = 0.85
legYMin = legYMax - (legYMax - (0.2 + y_leg_shift)) / legYCompr * nLegend
legXMin = 0.5 
legXMax = 0.87 

#lscdp_lowmt.SetMarkerStyle(20)
#lscdp_lowmt.SetMarkerColor(ROOT.kBlack)
#lscdp_lowmt_ss.SetMarkerStyle(20)
#lscdp_lowmt_ss.SetMarkerColor(ROOT.kBlack)

lscdp.SetMarkerStyle(20)
lscdp.SetMarkerColor(ROOT.kRed)
lscdp_ss.SetMarkerStyle(20)
lscdp_ss.SetMarkerColor(ROOT.kRed)

leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextSize(0.03)

if sign == "os":
	leg.AddEntry(sr, "Wjets (signal region)",'F')
	#leg.AddEntry(lscdp_lowmt,"Wjets (LSCDP LowMT region)",'PL')
	leg.AddEntry(lscdp,"Wjets (LSCDP region)",'P')


elif sign == "ss":
	leg.AddEntry(sr_ss, "Wjets (signal SS region)",'F')
	#leg.AddEntry(lscdp_lowmt_ss,"Wjets (LSCDP LowMT SS region)",'PL')
	leg.AddEntry(lscdp_ss,"Wjets (LSCDP SS region)",'P')	

if sign == "os":
	c = ROOT.TCanvas("wjets_OS","wjets_OS",800,600)
if sign == "ss":
        c = ROOT.TCanvas("wjets_SS","wjets_SS",800,600)

xmin = sr.GetBinLowEdge(1)
xmax = 100
ymin = 0
ymax = 0.8 
#ymax *= 1.8
xtitle = ""

ratio_line = ROOT.TLine(xmin,1,xmax,1)
ratio_line.SetLineColor(ROOT.kRed)
ratio_line.SetLineStyle(10)

rsplit = 0
pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
pad1.SetLeftMargin(0.15)
pad1.SetTicky()
pad1.SetTickx()
pad1.SetBottomMargin(0.15)
pad1.Draw()

#pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
#pad2.SetTopMargin(0.04)
#pad2.SetBottomMargin(0.40)
#pad2.SetLeftMargin(0.15)
#pad2.SetTicky()
#pad2.SetTickx()
#pad2.SetGridy()
#pad2.Draw()
pad1.cd()

ytitle = "Events"
#ytitle = yaxistitle

fr1 = pad1.DrawFrame(20,ymin,100,ymax,';%s;%s'%(xtitle,ytitle))
fr1.GetXaxis().SetTitleSize(0)
fr1.GetXaxis().SetLabelSize(0)
xaxis1 = fr1.GetXaxis()
xaxis1.SetRangeUser(20,100)
yaxis1 = fr1.GetYaxis()
scale = (1.3+rsplit)
yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
yaxis1.SetTitleOffset( 1 )
#yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
#yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
xaxis1.SetNdivisions(510)
yaxis1.SetNdivisions(510)
yaxis1.SetTitleSize(0.045)
yaxis1.SetLabelSize(0.04)
xaxis1.SetLabelSize(0.04)

yaxis1.SetTitle("Events")

if sign == "os":
	sr.Draw("hist")
	#lscdp_lowmt.Draw("SAME")
	lscdp.Draw("SAME")

elif sign == "ss":
	sr_ss.Draw("hist")
	#lscdp_lowmt_ss.Draw("SAME")
        lscdp_ss.Draw("SAME")

sr_stats_graph.Draw("E2 SAME")

leg.Draw()
pad1.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextSize(0.05)
lx = 0.6 # for ATLAS internal
ly = 0.845
tlatex.SetTextFont(42)

ty = 0.96
th = 0.07
tx = 0.18
latex_y = ty-2.*th
latex_yb = ty-4.*th
#tlatex.SetTextAlign(10)
tlatex.SetTextSize(0.035)
textsize = 0.7
latex_y = ty-2.*th
tlatex.DrawLatex(tx,latex_y,"#scale[0.7]{#bf{#it{ATLAS}} Internal}")
tlatex.DrawLatex(tx,latex_y-0.07,'#scale[%lf]{#scale[%lf]{#int}L dt = 24.8 fb^{-1}}'%(textsize,0.8*textsize) )
tlatex.DrawLatex(tx,latex_y-0.14,'#scale[%lf]{#sqrt{s} = 13 TeV}'%(textsize))
if trig:
	tlatex.DrawLatex(tx,latex_y-0.21,'#scale[%lf]{tau 25 medium trigger}'%(textsize))
#pad2.cd()
#
#fr2 = pad2.DrawFrame(20,0.8,100,1.2,';%s;SF'%('Offline Tau P_{T} [GeV]'))

#xaxis2 = fr2.GetXaxis()
#yaxis2 = fr2.GetYaxis()

#scale = (1. / rsplit)
#yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
#yaxis2.SetLabelSize( yaxis2.GetLabelSize() * scale )
#yaxis2.SetTitleOffset( 2.1* yaxis2.GetTitleOffset() / scale  )
#yaxis2.SetLabelOffset(0.2 * yaxis2.GetLabelOffset() * scale )
#xaxis2.SetTitleSize( xaxis2.GetTitleSize() * scale )
#xaxis2.SetLabelSize( 0.8 * xaxis2.GetLabelSize() * scale )
#xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
#xaxis2.SetTitleOffset(0.5)
#xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
#xaxis2.SetRangeUser(20,100)
#yaxis2.SetRangeUser(0.6,1.4)
#yaxis2.SetNdivisions(4)
#xaxis2.SetNdivisions(510)
#xaxis2.SetMoreLogLabels()
#xaxis2.SetTitleOffset(1)
#yaxis2.SetTitle("Ratio")
#yaxis2.SetTitleOffset(0.5)

#h_ratio.Draw("Same")

#pad2.RedrawAxis()

if trax == "1":
	plotsfile = os.path.join("./",str(trax)+"wjets_new_method_val_"+str(sign)+".root")
elif trax == "3":
	plotsfile = os.path.join("./",str(trax)+"wjets_new_method_val_"+str(sign)+".root")
else:
	if trig:
        	plotsfile = os.path.join("./","wjets_new_method_val_"+str(trig)+"_"+str(sign)+".root")
        else:
		plotsfile = os.path.join("./","wjets_new_method_val_"+str(sign)+".root")
fout = ROOT.TFile.Open(plotsfile,'UPDATE')
fout.WriteTObject(c)
fout.Close()



