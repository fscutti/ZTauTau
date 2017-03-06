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

#trax = None
trax = "1Track"
#trax = "3Track"

f = ROOT.TFile('./mu_trigger_chain_effiencies.root')

L1_data_stat_1Track= f.Get("L1_data_stat_1Track")
L1_data_sys_1Track= f.Get("L1_data_sys_1Track")
L1_eff_MC_1Track= f.Get("L1_eff_MC_1Track")
L1_eff_data_1Track= f.Get("L1_eff_data_1Track")
L1_tot_unc_1Track = f.Get("L1_tot_unc_1Track")

L1_data_stat_3Track= f.Get("L1_data_stat_3Track")
L1_data_sys_3Track= f.Get("L1_data_sys_3Track")
L1_eff_MC_3Track= f.Get("L1_eff_MC_3Track")
L1_eff_data_3Track = f.Get("L1_eff_data_3Track")
L1_tot_unc_3Track = f.Get("L1_tot_unc_3Track")
L1_tot_unc_3Track.SetLineColor(ROOT.kBlack)

BDT_1p_MC = f.Get('BDT_mc_1Track')
BDT_1p_data = f.Get('BDT_data_1Track')
Trk_1p_MC = f.Get('tracking_mc_1Track')
Trk_1p_data = f.Get('tracking_data_1Track')
PTcut_1p_MC = f.Get('ptcut_mc_1Track')
PTcut_1p_data = f.Get('ptcut_data_1Track')

BDT_3p_MC = f.Get('BDT_mc_3Track')
BDT_3p_data = f.Get('BDT_data_3Track')
Trk_3p_MC = f.Get('tracking_mc_3Track')
Trk_3p_data = f.Get('tracking_data_3Track')
PTcut_3p_MC = f.Get('ptcut_mc_3Track')
PTcut_3p_data = f.Get('ptcut_data_3Track')

BDT_1p_sys = f.Get('sys_25med1Track')
Trk_1p_sys = f.Get('sys_tracktwo1Track')
PTcut_1p_sys = f.Get('sys_ptonly1Track')

BDT_3p_sys = f.Get('sys_25med3Track')
Trk_3p_sys = f.Get('sys_tracktwo3Track')
PTcut_3p_sys = f.Get('sys_ptonly3Track')

BDT_1p_MC.SetMarkerStyle(22)
BDT_3p_MC.SetMarkerStyle(22)
Trk_1p_MC.SetMarkerStyle(22)
Trk_3p_MC.SetMarkerStyle(22)
PTcut_1p_MC.SetMarkerStyle(22)
PTcut_3p_MC.SetMarkerStyle(22)

leg_eff = ROOT.TLegend(0.33,0.12,0.87,0.42) #ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg_eff.SetBorderSize(0)
leg_eff.SetFillColor(0)
leg_eff.SetFillStyle(0)
leg_eff.SetNColumns(2)
leg_eff.SetTextSize(0.09)
leg_eff.AddEntry(L1_eff_data_3Track,"Data 16",'P')
leg_eff.AddEntry(L1_eff_MC_3Track,"MC",'P')
#leg_eff.AddEntry(L1_data_sys_3Track, "Data sys.", 'f')
#leg_eff.AddEntry(L1_data_stat_3Track, "Data stat.",'f')
#leg_eff.AddEntry(L1_tot_unc_3Track, "Data Unc.",'f')

leg_chain = ROOT.TLegend(0.35,0.32,0.87,0.52) #ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
leg_chain.SetBorderSize(0)
leg_chain.SetFillColor(0)
leg_chain.SetFillStyle(0)
leg_chain.SetNColumns(2)
leg_chain.SetTextSize(0.1)
leg_chain.AddEntry(PTcut_3p_data,"Data",'P')
leg_chain.AddEntry(PTcut_3p_MC,"MC",'P')

c = ROOT.TCanvas("trig_effs","trig_effs",600,600)
#c.Divide(2,4)
padtitle1 = ROOT.TPad("padtitle","padtitle",0,0.95,0.5,1)
padtitle1.SetLeftMargin(0.14)
padtitle1.SetRightMargin(0.05)
padtitle1.Draw()

padtitle3 = ROOT.TPad("padtitle","padtitle",0.5,0.95,1,1)
padtitle3.SetLeftMargin(0.14)
padtitle3.SetRightMargin(0.05)
padtitle3.Draw()

pad1 = ROOT.TPad("pad1","pad1",0.,0.72,0.5,0.95)
pad1.SetTicky()
pad1.SetTickx()
pad1.SetLeftMargin(0.14)
pad1.SetRightMargin(0.05)
pad1.Draw()

pad2 = ROOT.TPad("pad2","pad2",0.,0.5,0.5,0.72)
pad2.SetTicky()
pad2.SetTickx()
pad2.SetLeftMargin(0.14)
pad2.SetRightMargin(0.05)
pad2.Draw()

pad3 = ROOT.TPad("pad3","pad3",0.,0.28,0.5,0.5)
pad3.SetTicky()
pad3.SetTickx()
pad3.SetLeftMargin(0.14)
pad3.SetRightMargin(0.05)
pad3.Draw()

pad4 = ROOT.TPad("pad4","pad4",0.,0,0.5,0.28)
pad4.SetTicky()
pad4.SetTickx()
pad4.SetBottomMargin(0.27)
pad4.SetRightMargin(0.05)
pad4.SetLeftMargin(0.14)
pad4.Draw()

pad5 = ROOT.TPad("pad5","pad5",0.5,0.72,1,0.95)
pad5.SetTicky()
pad5.SetTickx()
#pad5.SetLeftMargin(0.14)
pad5.Draw()

pad6 = ROOT.TPad("pad6","pad6",0.5,0.5,1,0.72)
pad6.SetTicky()
pad6.SetTickx()
#pad6.SetLeftMargin(0.14)
pad6.Draw()

pad7 = ROOT.TPad("pad7","pad7",0.5,0.28,1,0.5)
pad7.SetTicky()
pad7.SetTickx()
#pad7.SetLeftMargin(0.14)
pad7.Draw()

pad8 = ROOT.TPad("pad8","pad8",0.5,0.,1,0.28)
pad8.SetTicky()
pad8.SetTickx()
pad8.SetBottomMargin(0.25)
#pad8.SetLeftMargin(0.14)
pad8.Draw()

padtitle1.cd()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.5)

padtitle3.cd()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.55)
#tlatex.DrawLatex(0.11,0.07,'HLT tau25 medium1 trigger')
#tlatex.DrawLatex(0.05,0.58,"#bf{#it{ATLAS}} Internal, 33.3 fb^{-1}")

pad1.cd()
fr1 = pad1.DrawFrame(0,0,300,1,';%s;Data/exp.'%('#mu'))
eff_L1 = ROOT.TMultiGraph()
#eff_L1.Add(L1_data_stat_1Track,"E2")
#eff_L1.Add(L1_data_sys_1Track,"E2")
eff_L1.Add(L1_tot_unc_1Track,"APZ")
eff_L1.Add(L1_eff_MC_1Track,"APZ")
eff_L1.Add(L1_eff_data_1Track,"APZ")
eff_L1.Draw("a Same")

xaxis_bot1 = eff_L1.GetXaxis()
yaxis_bot1 = eff_L1.GetYaxis()
xaxis_bot1.SetLabelFont(42)
xaxis_bot1.SetTitleFont(42)
yaxis_bot1.SetTitleFont(42)
yaxis_bot1.SetLabelFont(42)
xaxis_bot1.SetRangeUser(0,50)
yaxis_bot1.SetRangeUser(0,1.02)
yaxis_bot1.SetRangeUser(0,1.02)
#xaxis_bot1.SetTitle('#mu')
xaxis_bot1.SetNoExponent()
xaxis_bot1.SetTitleOffset(1)
yaxis_bot1.SetTitle("L1 Trigger Efficiency")
yaxis_bot1.SetTitleOffset(0.72)
yaxis_bot1.SetLabelSize( 0.088)
xaxis_bot1.SetLabelSize( 0.087)
yaxis_bot1.SetTitleSize( 0.09)
xaxis_bot1.SetTitleSize( 0.1)
leg_eff.Draw()
pad1.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.1)
tlatex.DrawLatex(0.2,0.6,'#bf{#it{ATLAS}} Internal, 33.3 fb^{-1}, #sqrt{s} = 13 TeV')
tlatex.DrawLatex(0.2,0.4,'HLT tau25 medium trigger, 1-prong')#, #sqrt{s} = 13 TeV')
#tlatex.DrawLatex(0.35,0.58,"#bf{#it{ATLAS}} Internal, 33.3 fb^{-1}")

pad2.cd()
fr2 = pad2.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_pt_1p = ROOT.TMultiGraph()
#tot_ratio_pt_1p.Add(PTcut_1p_MC,"E2")
tot_ratio_pt_1p.Add(PTcut_1p_MC,"APZ")
tot_ratio_pt_1p.Add(PTcut_1p_data,"APZ")
#tot_ratio_pt_1p.Add(PTcut_1p_sys,"APZ")
tot_ratio_pt_1p.Draw("a Same")

xaxis_bot2 = tot_ratio_pt_1p.GetXaxis()
yaxis_bot2 = tot_ratio_pt_1p.GetYaxis()
xaxis_bot2.SetLabelFont(42)
yaxis_bot2.SetLabelFont(42)
xaxis_bot2.SetRangeUser(0,50)
yaxis_bot2.SetRangeUser(0.86,1.02)
#xaxis_bot2.SetTitle('#mu')
xaxis_bot2.SetNoExponent()
xaxis_bot2.SetTitleOffset(1)
yaxis_bot2.SetTitle("Pt Cut Eff.")
yaxis_bot2.SetTitleOffset(0.72)
yaxis_bot2.SetNdivisions(8)
yaxis_bot2.SetLabelSize( 0.088)
xaxis_bot2.SetLabelSize( 0.087)
yaxis_bot2.SetTitleSize( 0.09)
xaxis_bot2.SetTitleSize( 0.1)
#leg_chain.Draw()
pad2.RedrawAxis()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.1)
tlatex.DrawLatex(0.35,0.2,'1-prong')

pad3.cd()
fr3 = pad3.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_trk_1p = ROOT.TMultiGraph()
#tot_ratio_trk_1p.Add(Trk_1p_MC,"E2")
tot_ratio_trk_1p.Add(Trk_1p_MC,"APZ")
tot_ratio_trk_1p.Add(Trk_1p_data,"APZ")
#tot_ratio_trk_1p.Add(Trk_1p_sys,"APZ")
tot_ratio_trk_1p.Draw("a Same")

xaxis_bot3 = tot_ratio_trk_1p.GetXaxis()
yaxis_bot3 = tot_ratio_trk_1p.GetYaxis()
xaxis_bot3.SetLabelFont(42)
yaxis_bot3.SetLabelFont(42)
xaxis_bot3.SetRangeUser(0,50)
yaxis_bot3.SetRangeUser(0.86,1.02)
#xaxis_bot3.SetTitle('#mu')
xaxis_bot3.SetNoExponent()
xaxis_bot3.SetTitleOffset(1)
yaxis_bot3.SetTitle("Trk. Counting Eff.")
yaxis_bot3.SetTitleOffset(0.72)
yaxis_bot3.SetLabelSize( 0.088)
xaxis_bot3.SetLabelSize( 0.087)
yaxis_bot3.SetTitleSize( 0.09)
xaxis_bot3.SetTitleSize( 0.1)
pad3.RedrawAxis()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.1)
tlatex.DrawLatex(0.35,0.2,'1-prong')

pad4.cd()
fr4 = pad4.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_bdt_1p = ROOT.TMultiGraph()
#tot_ratio_bdt_1p.Add(BDT_1p_MC,"E2")
tot_ratio_bdt_1p.Add(BDT_1p_MC,"APZ")
tot_ratio_bdt_1p.Add(BDT_1p_data,"APZ")
#tot_ratio_bdt_1p.Add(BDT_1p_sys,"APZ")
tot_ratio_bdt_1p.Draw("a Same")

xaxis_bot4 = tot_ratio_bdt_1p.GetXaxis()
yaxis_bot4 = tot_ratio_bdt_1p.GetYaxis()
xaxis_bot4.SetLabelFont(42)
yaxis_bot4.SetLabelFont(42)
xaxis_bot4.SetRangeUser(0,50)
yaxis_bot4.SetRangeUser(0.9,1.02)
xaxis_bot4.SetTitle('#mu')
xaxis_bot4.SetNoExponent()
xaxis_bot4.SetTitleOffset(1)
yaxis_bot4.SetTitle("BDT Eff.")
yaxis_bot4.SetTitleOffset(0.74)
yaxis_bot4.SetLabelSize( 0.068)
xaxis_bot4.SetLabelSize( 0.087)
yaxis_bot4.SetTitleSize( 0.08)
xaxis_bot4.SetTitleSize( 0.08)
pad4.RedrawAxis()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.08)
tlatex.DrawLatex(0.35,0.33,'1-prong')

pad5.cd()
fr5 = pad5.DrawFrame(0,0,300,1,';%s;Data/exp.'%('#mu'))
eff_L1_3p = ROOT.TMultiGraph()
#eff_L1_3p.Add(L1_data_stat_3Track,"E2")
#eff_L1_3p.Add(L1_data_sys_3Track,"E2")
eff_L1_3p.Add(L1_tot_unc_3Track,"APZ")
eff_L1_3p.Add(L1_eff_MC_3Track,"APZ")
eff_L1_3p.Add(L1_eff_data_3Track,"APZ")
eff_L1_3p.Draw("a Same")

xaxis_bot5 = eff_L1_3p.GetXaxis()
yaxis_bot5 = eff_L1_3p.GetYaxis()
xaxis_bot5.SetLabelFont(42)
yaxis_bot5.SetLabelFont(42)
xaxis_bot5.SetRangeUser(0,50)
#yaxis_bot5.SetRangeUser(0,1.02)
#xaxis_bot5.SetTitle('#mu')
xaxis_bot5.SetNoExponent()
xaxis_bot5.SetTitleOffset(1)
#yaxis_bot5.SetTitle("L1 Trigger Efficiency")
#yaxis_bot5.SetTitleOffset(0.7)
yaxis_bot5.SetLabelSize( 0.088)
xaxis_bot5.SetLabelSize( 0.087)
yaxis_bot5.SetTitleSize( 0.088)
xaxis_bot5.SetTitleSize( 0.1)
yaxis_bot5.SetRangeUser(0,1.02)
#leg_eff.Draw()
pad5.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.09)
tlatex.DrawLatex(0.33,0.45,'3-prong')
#tlatex.DrawLatex(0.33,0.58,"#bf{#it{ATLAS}} Internal, 33.3 fb^{-1}")

pad6.cd()
fr6 = pad6.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_pt_3p = ROOT.TMultiGraph()
#tot_ratio_pt_3p.Add(PTcut_3p_MC,"E2")
tot_ratio_pt_3p.Add(PTcut_3p_MC,"APZ")
tot_ratio_pt_3p.Add(PTcut_3p_data,"APZ")
#tot_ratio_pt_3p.Add(PTcut_3p_sys,"APZ")
tot_ratio_pt_3p.Draw("a Same")

xaxis_bot6 = tot_ratio_pt_3p.GetXaxis()
yaxis_bot6 = tot_ratio_pt_3p.GetYaxis()
xaxis_bot6.SetLabelFont(42)
yaxis_bot6.SetLabelFont(42)
xaxis_bot6.SetRangeUser(0,50)
yaxis_bot6.SetRangeUser(0.86,1.02)
#xaxis_bot6.SetTitle('#mu')
xaxis_bot6.SetNoExponent()
xaxis_bot6.SetTitleOffset(1)
#yaxis_bot6.SetTitle("Pt Cut Eff.")
#yaxis_bot6.SetTitleOffset(0.7)
yaxis_bot6.SetLabelSize( 0.088)
xaxis_bot6.SetLabelSize( 0.087)
yaxis_bot6.SetTitleSize( 0.088)
xaxis_bot6.SetTitleSize( 0.1)
#leg_chain.Draw()
pad6.RedrawAxis()
tlatex = ROOT.TLatex()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.1)
tlatex.DrawLatex(0.35,0.22,'3-prong')

pad7.cd()
fr7 = pad7.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_trk_3p = ROOT.TMultiGraph()
#tot_ratio_trk_3p.Add(Trk_3p_MC,"E2")
tot_ratio_trk_3p.Add(Trk_3p_MC,"APZ")
tot_ratio_trk_3p.Add(Trk_3p_data,"APZ")
#tot_ratio_trk_3p.Add(Trk_3p_sys,"APZ")
tot_ratio_trk_3p.Draw("a Same")

xaxis_bot7 = tot_ratio_trk_3p.GetXaxis()
yaxis_bot7 = tot_ratio_trk_3p.GetYaxis()
xaxis_bot7.SetLabelFont(42)
yaxis_bot7.SetLabelFont(42)
xaxis_bot7.SetRangeUser(0,50)
yaxis_bot7.SetRangeUser(0.86,1.02)
#xaxis_bot7.SetTitle('#mu')
xaxis_bot7.SetNoExponent()
xaxis_bot7.SetTitleOffset(1)
#yaxis_bot7.SetTitle("Trk. Eff.")
#yaxis_bot7.SetTitleOffset(0.7)
yaxis_bot7.SetLabelSize( 0.088)
xaxis_bot7.SetLabelSize( 0.087)
yaxis_bot7.SetTitleSize( 0.088)
xaxis_bot7.SetTitleSize( 0.1)
pad7.RedrawAxis()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.1)
tlatex.DrawLatex(0.35,0.22,'3-prong')

pad8.cd()
fr8 = pad8.DrawFrame(0,0.8,300,1.2,';%s;Data/exp.'%('#mu'))
tot_ratio_bdt_3p = ROOT.TMultiGraph()
#tot_ratio_bdt_3p.Add(BDT_3p_MC,"E2")
tot_ratio_bdt_3p.Add(BDT_3p_MC,"PZ")
tot_ratio_bdt_3p.Add(BDT_3p_data,"APZ")
#tot_ratio_bdt_3p.Add(BDT_3p_sys,"APZ")
tot_ratio_bdt_3p.Draw("a Same")

xaxis_bot8 = tot_ratio_bdt_3p.GetXaxis()
yaxis_bot8 = tot_ratio_bdt_3p.GetYaxis()
xaxis_bot8.SetLabelFont(42)
yaxis_bot8.SetLabelFont(42)
xaxis_bot8.SetRangeUser(0,50)
yaxis_bot8.SetRangeUser(0.9,1.02)
xaxis_bot8.SetTitle('#mu')
xaxis_bot8.SetNoExponent()
xaxis_bot8.SetTitleOffset(1)
#yaxis_bot8.SetTitle("BDT Eff.")
#yaxis_bot8.SetTitleOffset(0.7)
yaxis_bot8.SetLabelSize( 0.068)
xaxis_bot8.SetLabelSize( 0.087)
yaxis_bot8.SetTitleSize( 0.088)
xaxis_bot8.SetTitleSize( 0.08)
pad8.RedrawAxis()
tlatex.SetNDC()
tlatex.SetTextFont(42)
tlatex.SetTextSize(0.08)
tlatex.DrawLatex(0.35,0.33,'3-prong')

g = ROOT.TFile('./mu_multipadeffs.root', 'recreate')
c.Write()
g.Close()
c.Draw()
