import ROOT
import array
import histmgr
import funcs
import os

from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *

#--------- one and three prong ------------#
"""
f = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_data.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_nominal_sub_ztt')

g = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_data.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_nominal_sub_ztt_25med')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_nominal_sub_ztt_35med')

h = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_MC.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_nominal_Zttjets')

i = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_MC.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_25med_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_35med_nominal_Zttjets')

hist_SR_subztt_pretrig1.Print("all")
"""
"""
#    ONE PRONG

f = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau1Track_data.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau1Track_nominal_sub_ztt_1Track')

g = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau1Track_data.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_Tau1Track_nominal_sub_ztt_25med_1Track')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau1Track_data.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_Tau1Track_nominal_sub_ztt_35med_1Track')

h = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau1Track_MC.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau1Track_nominal_Zttjets')

i = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau1Track_MC.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_25med_Tau1Track_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau1Track_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_35med_Tau1Track_nominal_Zttjets')

"""
#    THREE PRONG

f = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau3Track_data.root')
hist_SR_subztt_pretrig1 = f.Get('h_SR_Tau3Track_nominal_sub_ztt_3Track')

g = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau3Track_data.root')
hist_SR_subztt_posttrig1 = g.Get('h_SR_25med_Tau3Track_nominal_sub_ztt_25med_3Track')

#g = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau3Track_data.root')
#hist_SR_subztt_posttrig1 = g.Get('h_SR_35med_Tau3Track_nominal_sub_ztt_35med_3Track')

h = ROOT.TFile('../../test/2016/efficiency_calculations/no_trig/hists_tau_pt_SR_Tau3Track_MC.root')
hist_SR_MC_pretrig1 = h.Get('h_SR_Tau3Track_nominal_Zttjets')

i = ROOT.TFile('../../test/2016/efficiency_calculations/25med/hists_tau_pt_SR_25med_Tau3Track_MC.root')
hist_SR_MC_posttrig1 = i.Get('h_SR_25med_Tau3Track_nominal_Zttjets')

#i = ROOT.TFile('../../test/2016/efficiency_calculations/35med/hists_tau_pt_SR_35med_Tau3Track_MC.root')
#hist_SR_MC_posttrig1 = i.Get('h_SR_35med_Tau3Track_nominal_Zttjets')


print hist_SR_subztt_pretrig1, hist_SR_subztt_posttrig1, hist_SR_MC_pretrig1, hist_SR_MC_posttrig1 

#xlow = [20.,25.,27.,30.,34.,38.,43.,52.,70.,100.]
xlow = [25.,28.,30.,32.,34.,36.,39.,40.,52.,64.,80.,100.,150.,300.]
hist_SR_subztt_pretrig = hist_SR_subztt_pretrig1.Rebin(13,"hist_SR_subztt_pretrig",array.array('d',xlow))
hist_SR_subztt_posttrig = hist_SR_subztt_posttrig1.Rebin(13,"hist_SR_subztt_posttrig",array.array('d',xlow))
hist_SR_MC_pretrig = hist_SR_MC_pretrig1.Rebin(13,"hist_SR_MC_pretrig",array.array('d',xlow))
hist_SR_MC_posttrig = hist_SR_MC_posttrig1.Rebin(13,"hist_SR_MC_posttrig",array.array('d',xlow))
'''
h_efficiency_subztt = hist_SR_subztt_posttrig
h_efficiency_subztt.Divide(hist_SR_subztt_posttrig, hist_SR_subztt_pretrig, 1.0, 1.0, "B")

h_efficiency_mc = hist_SR_MC_posttrig
h_efficiency_mc.Divide(hist_SR_MC_posttrig,hist_SR_MC_pretrig, 1.0, 1.0, "B")
'''
h_efficiency_simple_subztt = hist_SR_subztt_posttrig.Clone()
#h_efficiency_simple_subztt.Divide(hist_SR_subztt_pretrig)
h_efficiency_simple_subztt.Divide(hist_SR_subztt_posttrig, hist_SR_subztt_pretrig, 1.0, 1.0, "B")
print "*********** DATA"
print "numerator"
hist_SR_subztt_posttrig.Print("all")
print "denominator"
hist_SR_subztt_pretrig.Print("all")

print "*********** MC"
print "numerator"
hist_SR_MC_posttrig.Print("all")
print "denominator"
hist_SR_MC_pretrig.Print("all")

h_efficiency_simple_mc = hist_SR_MC_posttrig.Clone()
#h_efficiency_simple_mc.Divide(hist_SR_MC_pretrig)
h_efficiency_simple_mc.Divide(hist_SR_MC_posttrig, hist_SR_MC_pretrig, 1.0, 1.0, "B")

print "**************** RESULT"
h_efficiency_simple_subztt.Print("all")
h_efficiency_simple_mc.Print("all")
outfile = ROOT.TFile('simple_outputnew.root','recreate')
'''
h_efficiency_subztt.Write()
h_efficiency_mc.Write()
'''
h_efficiency_simple_subztt.Write()
h_efficiency_simple_mc.Write()
outfile.Close()

h_samp_list = []
h_samp_list.append(h_efficiency_simple_mc)
h_total = funcs.histutils.add_hists(h_samp_list)
h_total_stat = funcs.make_stat_hist(h_total)
g_stat = funcs.make_band_graph_from_hist(h_total_stat)
g_stat.SetFillColor(ROOT.kGray+1)
g_tot = None

h_data = h_efficiency_simple_subztt.Clone()
h_ratio = h_data.Clone()
h_ratio.Divide(h_efficiency_simple_mc)

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

leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.AddEntry(h_efficiency_simple_subztt,"Data",'PL')
leg.AddEntry(h_efficiency_simple_mc,"Z#rightarrow#tau#tau",'F')

c = ROOT.TCanvas("efficiency","efficiency",750,800)
xmin = h_total.GetBinLowEdge(1)
xmax = 100 
ymin = 1.e-3
ymax = h_total.GetMaximum()
ymax *= 1.8
xtitle = ""

rsplit = 0.3
pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
pad1.SetLeftMargin(0.15)
pad1.SetTicky()
pad1.SetTickx()
pad1.SetBottomMargin(0.04)

pad1.Draw()

pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
pad2.SetTopMargin(0.04)
pad2.SetBottomMargin(0.40)
pad2.SetLeftMargin(0.15)
pad2.SetTicky()
pad2.SetTickx()
pad2.SetGridy()
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
tlatex.SetTextSize=0.001
tlatex.DrawLatex(tx,latex_y,'#intL dt = 3.2 fb^{-1}, #sqrt{s} = 13 TeV}' )
tlatex.DrawLatex(tx,latex_yb,'HLT_tau25_medium1_tracktwo')
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
h_ratio.Draw("Same")
pad2.RedrawAxis()
plotsfile = os.path.join("./","eff.root")
#c.SaveAs("Test")
fout = ROOT.TFile.Open(plotsfile,'UPDATE')
fout.WriteTObject(c)
fout.Close()
