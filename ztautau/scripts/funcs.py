# encoding: utf-8
'''
tools.py

description:

'''

## modules
import ROOT
from pyplot import histutils
from math import sqrt
from decimal import Decimal
#import sys_conv


# - - - - - - - - - - - class defs  - - - - - - - - - - - - #




# - - - - - - - - - - function defs - - - - - - - - - - - - #
#____________________________________________________________
def apply_blind(h,blind_range):
    for i in range(1,h.GetNbinsX()+1):
        elow  = h.GetBinLowEdge(i)
        ehigh = h.GetBinLowEdge(i) + h.GetBinWidth(i)
        if elow>=min(blind_range) and ehigh<max(blind_range): 
            h.SetBinContent(i,0.)
            h.SetBinError(i,0.)

#____________________________________________________________
def get_hists(
        region    = None,
        icut      = None,
        histname  = None,
        samples   = None,
        rebin     = None,
        sys_dict  = None,
        uo_flow   = False,
        ):
    '''
    if sys_dict is passed, hists for all systematics will be appended in a dict. 
    '''
    
    hists = {} 
    #print "grabbing syst"
    for s in samples:
      if not s.hist(region=region,icut=icut,histname=histname): continue
      h = s.hist(region=region,icut=icut,histname=histname).Clone()
      if rebin and h:
          print "Rebinning"
          if isinstance(h, ROOT.TH2):
              #h = h.RebinX(rebin['nbinsx'])
              #h = h.RebinY(rebin['nbinsy'])
              xmin     = h.GetXaxis().GetBinLowEdge(1)
              ymin     = h.GetYaxis().GetBinLowEdge(1)
              xmax     = h.GetXaxis().GetBinLowEdge(h.GetNbinsX()+1)
              ymax     = h.GetYaxis().GetBinLowEdge(h.GetNbinsY()+1)
              binsizex = (rebin['xmax'] - rebin['xmin']) / rebin['nbinsx']
              binsizey = (rebin['ymax'] - rebin['ymin']) / rebin['nbinsy']
              newbinx  = float(binsizex)
              newbiny  = float(binsizey)
              oldbinx  = float(h.GetXaxis().GetBinWidth(1))
              oldbiny  = float(h.GetYaxis().GetBinWidth(1))
              xratio, yratio = int(newbinx/oldbinx), int(newbiny/oldbiny)
              if oldbinx > newbinx:
                  print "Warning xbins: old %s > new %s" % (oldbinx, newbinx)
                  xratio = 1
              if oldbiny > newbiny:
                  print "Warning ybins: old %s > new %s setting ratio to 1" % (oldbiny, newbiny)
                  yratio = 1
              h = h.Rebin2D(xratio, yratio)
          elif isinstance(h, ROOT.TProfile) and not isinstance(h, ROOT.TH2):
              h = h.Rebin(len(rebin['rebin']['rebinx'])-1,h.GetName(),rebin['rebin']['rebinx'])
          elif isinstance(h, ROOT.TH1):                                                       
              h = h.Rebin(len(rebin['rebin'])-1,h.GetName(),rebin['rebin'])
          print "Rebinning done!"
      #####################
      bin_uf    = (h.GetBinContent(0), h.GetBinError(0))
      bin_first = (h.GetBinContent(1), h.GetBinError(1))
      last      = h.GetNbinsX()
      bin_of    = (h.GetBinContent(last  ), h.GetBinError(last  ))
      bin_last  = (h.GetBinContent(last+1), h.GetBinError(last+1))
      # Rebinning shit
      import math
      print "#################"
      h.Print("all")
      h.SetBinContent(1,bin_uf[0]+bin_first[0])
      h.SetBinError  (1,math.sqrt(bin_uf[1]*bin_uf[1]+bin_first[1]*bin_first[1]))
      h.SetBinContent(last,bin_of[0]+bin_last[0])
      h.SetBinError  (last,math.sqrt(bin_of[1]*bin_of[1]+bin_last[1]*bin_last[1]))
      print "#################"
      h.Print("all")
      hists[s] = h
      assert h, 'failed to gen hist for %s'%s.name
      h.SetName('h_%s_%s'%(region,s.name))
      if sys_dict: 
         h.sys_hists = get_sys_hists(region    = region,
                                     icut      = icut,
                                     histname  = histname,
                                     sample    = s,
                                     rebin     = rebin,
                                     sys_dict  = sys_dict,
                                     )

    for s in samples: s.estimator.flush_hists()
    return hists

#____________________________________________________________
def get_sys_hists(
        region   = None,
        icut     = None,
        histname = None,
        sample   = None,
        rebin    = None,
        sys_dict = None,
        ):
    
    '''
    TODO: put description here
    '''

    hist_dict = {}
    #print "grabbing systs hists"
    for name,sys in sys_dict.items():
        #print name, sys
        h_up = h_dn = None
        if sample.estimator.is_affected_by_systematic(sys):
          #print "is allowed", sample
          if not h_up:
            #print "##############################################################################################"
            h_up = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone() 
          else:  h_up.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone())
          if not h_dn: h_dn = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone() 
          else:  h_dn.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone())
          h_up.SetName('h_%s_%s_up_%s'%(region,sys,sample.name))
          h_dn.SetName('h_%s_%s_dn_%s'%(region,sys,sample.name))
          
          if rebin:
           if isinstance(h_up, ROOT.TProfile) and not isinstance(h_up, ROOT.TH2):
               h_up = h_up.Rebin(len(rebin['rebin']['rebinx'])-1,h_up.GetName(),rebin['rebin']['rebinx'])
               h_dn = h_dn.Rebin(len(rebin['rebin']['rebinx'])-1,h_dn.GetName(),rebin['rebin']['rebinx'])
           elif isinstance(h_up, ROOT.TH1):                                                       
               h_up = h_up.Rebin(len(rebin['rebin'])-1,h_up.GetName(),rebin['rebin'])
               h_dn = h_dn.Rebin(len(rebin['rebin'])-1,h_dn.GetName(),rebin['rebin'])
             
        hist_dict[sys] = (h_up,h_dn)
    return hist_dict 


#____________________________________________________________
def make_stat_hist(h):
    '''
    makes histogram with fractional bin uncertainty as entries
    ie. new bin content = old bin error/old bin content
    (used for making stat. ratio bands)
    '''
    h_stat = h.Clone('%s_stat'%(h.GetName()))
    for i in range(1,h.GetNbinsX()+1): 
        n = h.GetBinContent(i)
        en = h.GetBinError(i)
        stat = en / n if n else 0.0
        h_stat.SetBinContent(i,stat) 
    return h_stat

#____________________________________________________________
def make_band_graph_from_hist(h_UP,h_DN=None):
    '''
    makes band graph from hist.
    anti-symmetric if h_DN supplied, otherwise symmetric
    '''
    graph = ROOT.TGraphAsymmErrors()
    # added following line
    #graph.GetXaxis().SetRangeUser(h_UP.GetXaxis().GetXmin(),h_UP.GetXaxis().GetXmax()) 
    for i in range(1,h_UP.GetNbinsX()+1):
        eUP = abs(h_UP.GetBinContent(i))
        eDN = abs(h_UP.GetBinContent(i))
        if h_DN: eDN = abs(h_DN.GetBinContent(i))
        ex = h_UP.GetBinWidth(i)/2.
        graph.SetPoint(i-1,h_UP.GetBinCenter(i),1.)
        graph.SetPointError(i-1,ex,ex,eUP,eDN)
    return graph

#____________________________________________________________
def get_total_stat_sys_hists(hists,sys_dict):
    """
    first make total hist for each systematic. 
    then sum deviations in quadrature bin-by-bin to make band.
    """

    ## make total sys hists
    h_total = histutils.add_hists(hists)
    h_total_stat = make_stat_hist(h_total)
    sys_hists_total = {}
    for sys in sys_dict.values():
        hists_up = []
        hists_dn = []
        for h in hists: 
            ## if hist not found, take nominal
            if not h.sys_hists.has_key(sys):
                hists_up.append(h)
                hists_dn.append(h)
            else:
                hists_up.append(h.sys_hists[sys][0] or h)
                hists_dn.append(h.sys_hists[sys][0] or h)

        h_up = histutils.add_hists(hists_up)
        h_dn = histutils.add_hists(hists_dn)
        sys_hists_total[sys] = (h_up,h_dn)

    ## sum bin-by-bin deviations in quadrature
    h_sys_UP = h_total.Clone('%s_sys_UP'%(h_total.GetName()))
    h_sys_DN = h_total.Clone('%s_sys_DN'%(h_total.GetName()))
    h_total_UP = h_total.Clone('%s_total_UP'%(h_total.GetName()))
    h_total_DN = h_total.Clone('%s_total_DN'%(h_total.GetName()))
    for i in range(1,h_total.GetNbinsX()+1):
        n = h_total.GetBinContent(i)
        tot_sys_UP2 = 0.0
        tot_sys_DN2 = 0.0
        for sys in sys_dict.values():
            (h_UP,h_DN) = sys_hists_total[sys]
            n_UP = h_UP.GetBinContent(i)
            n_DN = h_DN.GetBinContent(i)
            v_UP = (n_UP-n)/n if (n_UP!=None and n) else 0.0
            v_DN = (n_DN-n)/n if (n_DN!=None and n) else 0.0

            tot_sys_UP2 += pow(v_UP,2)
            tot_sys_DN2 += pow(v_DN,2)
        tot_sys_UP = sqrt(tot_sys_UP2)            
        tot_sys_DN = sqrt(tot_sys_DN2)            
        h_sys_UP.SetBinContent(i,tot_sys_UP)
        h_sys_DN.SetBinContent(i,tot_sys_DN)
        
        stat = h_total_stat.GetBinContent(i)
        tot_UP = sqrt(pow(tot_sys_UP,2)+pow(stat,2))
        tot_DN = sqrt(pow(tot_sys_DN,2)+pow(stat,2))
        h_total_UP.SetBinContent(i,tot_UP)
        h_total_DN.SetBinContent(i,tot_DN)

    return (h_total_stat,h_sys_UP,h_sys_DN,h_total_UP,h_total_DN)



#____________________________________________________________
def plot_hist( 
    backgrounds   = None,
    signal        = None,   
    data          = None,
    region        = None,
    label         = None,
    icut          = None,
    histname      = None,
    log           = False,
    logx          = False,
    blind         = None,
    xmin          = None,
    xmax          = None,
    rebin         = None,
    sys_dict      = None,
    do_ratio_plot = False,
    do_profile    = False,
    do_2d         = False,
    profile_2d    = False,
    plotsfile     = None,
    sig_rescale   = None,
    ):
    
    '''
    TODO: 
        * move this to a new module when finished
        * write description for this function

    '''
    print 'making plot: ', histname, ' in region', region
    
    #assert signal, "ERROR: no signal provided for plot_hist"
    #assert backgrounds, "ERROR: no background provided for plot_hist"
    if not signal and not backgrounds and not data:
        assert data, "ERROR: No signal, backgrounds or data... What are you doing???"
    
    samples = []
    if backgrounds: samples += backgrounds

    if signal: samples+= signal
    
    if data: samples += [data] 

    ## generate nominal hists
    hists = get_hists(
        region=region,
        icut=icut,
        histname=histname,
        samples=samples,
        rebin=rebin,
        sys_dict=sys_dict,
        uo_flow=True,
        )
    ## sum nominal background
    h_samp_list = []
    #for s in backgrounds+signal:
    if backgrounds:
        for s in backgrounds:
          if not s in hists.keys(): continue
          h_samp_list.append(hists[s])
    
    h_total = histutils.add_hists(h_samp_list)
    #if do_profile: h_total = None

    ## get stat / sys bands
    #g_tot = None
    if not do_profile and not do_2d and not profile_2d:
        if sys_dict: 
            total_hists = get_total_stat_sys_hists(h_samp_list,sys_dict)
            
            g_stat = make_band_graph_from_hist(total_hists[0])
            g_stat.SetFillColor(ROOT.kGray+1)
            g_stat.SetFillStyle(3325)
            g_tot  = make_band_graph_from_hist(total_hists[3],total_hists[4])
            g_tot.SetFillColor(ROOT.kRed)

        else:
            h_total_stat = make_stat_hist(h_total)
            g_stat = make_band_graph_from_hist(h_total_stat)
            g_stat.SetFillColor(ROOT.kGray+1)
            g_stat.SetFillStyle(3352)
            g_tot = None

    ## blind data and create ratio 
    h_data  = None
    h_ratio = None
    if data:
        h_data = hists[data]
        #if do_profile:
            #if blind: apply_blind(h_data,blind)
            #h_data = h_data.ProfileX('data', 0, int(h_data.GetYaxis().GetNbins()), 'g')
        #else:
        if blind and not (do_profile or do_2d): apply_blind(h_data,blind)
        if do_ratio_plot:
            h_ratio = h_data.Clone('%s_ratio'%(h_data.GetName()))
            h_ratio.Divide(h_total)
    
    yaxistitle = None
    if backgrounds:
        for b in reversed(backgrounds):
          if not b in hists.keys(): continue
          else : 
            yaxistitle = hists[b].GetYaxis().GetTitle()
            break
    elif h_total and data:
        yaxistitle = hists[data].GetYaxis().GetTitle()

    ## create stack
    ytitle = h_data.GetYaxis().GetTitle()
    if profile_2d:
        h_data  = h_data .ProfileX().Clone()
        h_total = h_total.ProfileX().Clone()
    if profile_2d or do_profile:
        h_total.SetMarkerStyle(26)
        h_total.SetLineColor(ROOT.kRed)
        h_total.SetMarkerColor(ROOT.kRed)
        h_data.SetMarkerStyle(24)
        h_data.SetLineColor(ROOT.kBlue)
        h_data.SetMarkerColor(ROOT.kBlue)

    #if do_profile:
    #    #print "running over bkgd"
    #    #for i,b in enumerate(backgrounds):
    #    #  if not b in hists.keys(): continue
    #    #  if i == 0: h_bkgd =hists[b]
    #    #  else: h_bkgd.Add(hists[b])
    #    #h_bkgd = h_bkgd.ProfileX('expected', 0, int(h_bkgd.GetYaxis().GetNbins()), 'g')
    #    h_total.SetMarkerStyle(26)
    #    h_total.SetLineColor(ROOT.kRed)
    #    h_total.SetMarkerColor(ROOT.kRed)
    if not profile_2d:
        h_stack = ROOT.THStack()
        for b in reversed(backgrounds):
          if not b in hists.keys(): continue
          h_stack.Add(hists[b])
    
    h_sig = None 
    if signal and not do_profile and not do_2d and not profile_2d:
        h_sig = []
        for b in reversed(signal):
          if not b in hists.keys(): continue
          h_sig.append(hists[b])

    leg = None
    if not (do_2d and not profile_2d):
        if do_profile or profile_2d: nLegend = 2
        elif signal: nLegend = len(signal+backgrounds) + 1
        else: nLegend = len(backgrounds) + 1
        x_legend = 0.63
        x_leg_shift = -0.055
        y_leg_shift = 0.0 
        legYCompr = 8.0
        legYMax = 0.85
        legYMin = legYMax - (legYMax - (0.55 + y_leg_shift)) / legYCompr * nLegend
        legXMin = x_legend + x_leg_shift
        legXMax = legXMin + 0.4
      
        ## create legend (could use metaroot functionality?)
        if not do_ratio_plot:
          legXMin -= 0.005
          legXMax -= 0.058
        leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        if data:
            leg.AddEntry(h_data,data.tlatex,'PL')
        if signal and not do_profile and not profile_2d:
            for s in signal:
              sig_tag = s.tlatex
              if sig_rescale: sig_tag = "%d #times "%int(sig_rescale) + sig_tag
              if not s in hists.keys(): continue
              leg.AddEntry(hists[s],sig_tag,'F')
        if do_profile or profile_2d:
            leg.AddEntry(h_total, 'Estimate', 'PL')
        else:
            for b in backgrounds: 
              if not b in hists.keys(): continue
              leg.AddEntry(hists[b],b.tlatex,'F')


    ## create canvas
    reg = region
    if not reg: reg = ""
    name = '_'.join([reg,histname]).replace('/','_') 
    cname = "c_final_%s"%name
    if do_ratio_plot: c = ROOT.TCanvas(cname,cname,750,800)
    elif do_2d and not profile_2d: c = ROOT.TCanvas(cname,cname,1600,700)
    else: c = ROOT.TCanvas(cname,cname,800,700)
    ## set Min and Max
    ymin = 1.e-3
    ymax = 100
    h_check = h_data if h_data else h_total
    if isinstance(h_check, ROOT.TH2):
        xmin = min(rebin['rebin']['rebinx'])
        xmax = max(rebin['rebin']['rebinx'])
        ymax = max(rebin['rebin']['rebiny'])
    elif isinstance(h_check, ROOT.TProfile):
        xmin = min(rebin['rebin']['rebinx'])
        xmax = max(rebin['rebin']['rebinx'])
        ymax = max(rebin['rebin']['rebiny'])
        ymin = min(rebin['rebin']['rebiny'])
    elif isinstance(h_check, ROOT.TH1):
        xmin = min(rebin['rebin'])
        xmax = max(rebin['rebin'])
        profile_2d = False
    else:
        if xmin==None: xmin = h_check.GetBinLowEdge(1)
        if xmax==None: xmax = h_check.GetBinLowEdge(h_total.GetNbinsX()+1)
    if signal:
        for s in signal:
          if not s in hists.keys(): continue
          ymax = max([ymax,hists[s].GetMaximum()])
    #if h_data and not do_2d:
    #    ymax = max([ymax,h_data.GetMaximum()])
    
    if h_total and not do_2d:
        ymax = max([ymax,h_total.GetMaximum()])
    ymax = float(ymax)
    if not (do_2d and not profile_2d):
        if log: ymax *= 100000.
        else:   ymax *= 1.8

    if h_data:
        xtitle = h_data.GetXaxis().GetTitle()
    else:
        xtitle = h_total.GetXaxis().GetTitle()

    ## Making the pads
    if do_ratio_plot: rsplit = 0.3
    else: rsplit = 0.
    if do_2d and not profile_2d: pad1 = ROOT.TPad("pad1", "Data", 0., 0., 0.5, 1.)
    else: pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
    pad1.SetLeftMargin(0.15)
    pad1.SetTicky()
    pad1.SetTickx()
    if do_ratio_plot: pad1.SetBottomMargin(0.04)
    else: pad1.SetBottomMargin(0.15)

    pad1.Draw()
    if do_ratio_plot:
      pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
      pad2.SetTopMargin(0.04)
      pad2.SetBottomMargin(0.40)
      pad2.SetLeftMargin(0.15)
      pad2.SetTicky()
      pad2.SetTickx()
      pad2.SetGridy()
      pad2.Draw()
    if do_2d and not profile_2d:
        pad2 = ROOT.TPad("pad2", "Background", 0.5, 0., 1., 1. )
        pad2.SetLeftMargin(0.15)
        pad2.SetTicky()
        pad2.SetTickx()
        pad2.SetBottomMargin(0.15)
        pad2.Draw()
    pad1.cd()

    ## ytitle
    skip = False
    if not ytitle == "Events":
        skip = True
    if not skip:
        ytitle = "Events" 
        if not rebin: ytitle = yaxistitle
        if isinstance(h_data, ROOT.TH2) or isinstance(h_data, ROOT.TProfile):
            ytitle = h_data.GetYaxis().GetTitle()
        else:
          if not (do_profile or do_2d or profile_2d):
              print rebin['rebin']
              if not isinstance(rebin['rebin'], dict):
                  bw = (float(max(rebin['rebin'])) - float(min(rebin['rebin']))) / (len(rebin['rebin']) - 1)
                  ytitle += " / %s" % bw
          if ("eta" in xtitle) or ("phi" in xtitle) or ("trk" in xtitle): pass
          elif not do_2d: ytitle += " GeV"

    #print xmin, ymin, xmax, ymax, ytitle
    if do_2d and not profile_2d:
        fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle + ' (Data)'))
    else:
        fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
    if do_ratio_plot:
      fr1.GetXaxis().SetTitleSize(0)
      fr1.GetXaxis().SetLabelSize(0)
    xaxis1 = fr1.GetXaxis()
    yaxis1 = fr1.GetYaxis()
    scale = (1.3+rsplit)

    if not do_ratio_plot:
      xaxis1.SetTitleSize( xaxis1.GetTitleSize() * scale )
      xaxis1.SetLabelSize( 0.9 * xaxis1.GetLabelSize() * scale )
      xaxis1.SetTickLength( xaxis1.GetTickLength() * scale )
      xaxis1.SetTitleOffset( 1.3* xaxis1.GetTitleOffset() / scale  )
      xaxis1.SetLabelOffset( 1.* xaxis1.GetLabelOffset() / scale )

    yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
    yaxis1.SetTitleOffset( 2.1 * yaxis1.GetTitleOffset() / scale )
    yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
    yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
    xaxis1.SetNdivisions(510)
    yaxis1.SetNdivisions(510)

    if do_2d:
        ROOT.gStyle.SetOptTitle(1)
        ROOT.gStyle.SetTitleFontSize(10)
    ## All the drawing
    if do_profile or profile_2d:
        h_total.Draw("SAME")
    elif not do_2d:
        h_stack.Draw("SAME,HIST")
    
    if signal and not (do_profile or do_2d):
      for sig in h_sig:
          if sig_rescale: sig.Scale(sig_rescale)
          sig.Draw("SAME,HIST") 

    if h_total and not do_2d and not profile_2d:
        h_stat = h_total.Clone('h_total_stat_upper')
        h_stat.SetFillColor(ROOT.kGray+1)
        h_stat.SetFillStyle(3352)
        h_stat.Draw("SAME,E2")
    if h_data and (do_2d and not profile_2d):
        h_data.Draw("SAME,COLZ")
    elif h_data:
        h_data.Draw("SAME")

    pad1.SetLogy(log)
    pad1.SetLogx(logx)
    if leg: leg.Draw()
    pad1.RedrawAxis()

    if not (do_2d and not profile_2d):
        tlatex = ROOT.TLatex()
        tlatex.SetNDC()
        tlatex.SetTextSize(0.05)
        lx = 0.6 # for ATLAS internal
        ly = 0.845
        tlatex.SetTextFont(42)
        
        ty = 0.96
        th = 0.07
        tx = 0.18
        lumi = backgrounds[0].estimator.hm.target_lumi/1000.
        textsize = 0.8
        if not do_ratio_plot: textsize = 0.6
        latex_y = ty-2.*th
        ks = h_total.KolmogorovTest(h_data)
        tlatex.DrawLatex(tx,latex_y,'#scale[%lf]{#scale[%lf]{#int}L dt = %2.1f fb^{-1}, #sqrt{s} = 13 TeV}'%(textsize,0.8*textsize,lumi) )
        if label:
          latex_y -= 0.06
          #for i,line in enumerate(label):
          #  tlatex.DrawLatex(tx,latex_y-i*0.06,"#scale[%lf]{%s}"%(textsize,line))
          tlatex.DrawLatex(tx,latex_y - 0.06,"#scale[%lf]{%s, KS = %2.2f}"%(textsize,label,ks))
        #if blind:
            #line = ROOT.TLine()
            #line.SetLineColor(ROOT.kBlack)
            #line.SetLineStyle(2)
            #line.DrawLine(blind,ymin,blind,ymax)
#        bltext = ROOT.TLatex()
#        bltext.SetTextFont(42)
#        bltext.SetTextSize(0.04)
#        bltext.SetTextAngle(90.)
#        bltext.SetTextAlign(31)
#        bltext.DrawLatex(blind,ymax, 'Blind   ')

    if do_ratio_plot:
      pad2.cd()
      fr2 = pad2.DrawFrame(xmin,0.49,xmax,1.51,';%s;Data / Bkg_{SM}'%(xtitle))
      xaxis2 = fr2.GetXaxis()
      yaxis2 = fr2.GetYaxis()
      scale = (1. / rsplit)
      yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
      yaxis2.SetLabelSize( yaxis2.GetLabelSize() * scale )
      yaxis2.SetTitleOffset( 2.1* yaxis2.GetTitleOffset() / scale  )
      yaxis2.SetLabelOffset(0.4 * yaxis2.GetLabelOffset() * scale )
      xaxis2.SetTitleSize( xaxis2.GetTitleSize() * scale )
      xaxis2.SetLabelSize( 0.8 * xaxis2.GetLabelSize() * scale )
      xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
      xaxis2.SetTitleOffset( 3.2* xaxis2.GetTitleOffset() / scale  )
      xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
      yaxis2.SetNdivisions(510)
      xaxis2.SetNdivisions(510)

    elif do_2d and not profile_2d:
        pad2.cd()
        fr2 = pad2.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle + ' (Background)'))
        xaxis2 = fr2.GetXaxis()
        yaxis2 = fr2.GetYaxis()
        yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
        yaxis2.SetTitleOffset( 2.1 * yaxis2.GetTitleOffset() / scale )
        yaxis2.SetLabelSize( 0.8 * yaxis2.GetLabelSize() * scale )
        yaxis2.SetLabelOffset( 1. * yaxis2.GetLabelOffset() / scale )
        xaxis2.SetNdivisions(510)
        yaxis2.SetNdivisions(510)
        if h_total and do_2d:
            h_total.Draw("SAME,COLZ")
        pad2.RedrawAxis()


    if do_ratio_plot:
      if logx: 
        pad2.SetLogx(logx) 
        xaxis2.SetMoreLogLabels()
      else: 
        pass

      if do_ratio_plot:
          if g_tot: 
             g_tot.Draw("E2")
             g_stat.Draw("SAME,E2")

          else: g_stat.Draw("E2")

          if data and do_ratio_plot:
              h_ratio.Draw("SAME") 
      pad2.RedrawAxis()

    print 'saving plot...'
    if not log:
        c.SaveAs("%s.eps" %c.GetName())
        c.SaveAs("%s.png" %c.GetName())
        c.SaveAs("%s.root"%c.GetName())
    else:
        c.SaveAs("%s_LOG.eps" %c.GetName())
        c.SaveAs("%s_LOG.png" %c.GetName())
        c.SaveAs("%s_LOG.root"%c.GetName())
    fout = ROOT.TFile.Open(plotsfile,'UPDATE')
    fout.WriteTObject(c)
    fout.Close()

#____________________________________________________________
def write_hist(
        backgrounds = None,
        signal      = None,
        data        = None,
        region      = None,
        icut        = None,
        histname    = None,
        rebin       = None,
        sys_dict    = None,
        outname     = None,
        ):
    """
    write hists for backgrounds, signals and data to file.
    will also write sys hists if sys_dict is passed. 
    also write smtot hists for summed background.
    No folder structure is provided
    """
    if signal: samples = backgrounds + signal
    else: samples = backgrounds
    if data: samples += [data]
    ## generate nominal hists
    print 'grabbing hist'
    hists = get_hists(
        region=region,
        icut=icut,
        histname=histname,
        samples=samples, 
        rebin=rebin,
        sys_dict=sys_dict,
        uo_flow=True,
        )
    
    #histnamestr = histname.replace('/','_')
    fname = outname
    fout = ROOT.TFile.Open(fname,'RECREATE')
    for s,h in hists.items():
        print s.name
        if s.name == 'data':
            print h.GetEntries()
        hname = 'h_%s_nominal_%s' % (region,s.name)
        h.SetNameTitle(hname,hname)
        fout.WriteTObject(h,hname)
        ## systematics
        if hasattr(h,'sys_hists'):
         if sys_dict:
            for sys,hsys in h.sys_hists.items():
                
                s_name = sys#.name
                
                hname_sys_up = hname.replace('nominal','%s_%s' % (s_name,'UP'))
                hname_sys_dn = hname.replace('nominal','%s_%s' % (s_name,'DN'))

                if hsys[0]: hsys[0].SetNameTitle(hname_sys_up,hname_sys_up)
                if hsys[1]: hsys[1].SetNameTitle(hname_sys_dn,hname_sys_dn)
                fout.WriteTObject(hsys[0],hname_sys_up)
                fout.WriteTObject(hsys[1],hname_sys_dn)

    ## create total background hists
    #h_total = histutils.add_hists([ hists[s] for s in backgrounds ])
    #fout.WriteTObject(h_total,'h_%s_nominal_smtot'%region)
    
    fout.Close()


#____________________________________________________________
def print_cutflows(
        backgrounds = None,
        signal      = None,
        data        = None,
        region      = None,
        histname    = None,
        outname     = None,
        sys_dict    = None,
        ):
    """
    write hists for backgrounds, signals and data to file.
    will also write sys hists if sys_dict is passed. 
    also write smtot hists for summed background.
    No folder structure is provided
    """
    if signal: samples = backgrounds + signal
    else: samples = backgrounds
    if data: samples += [data]
    ## generate nominal hists
    #print "Retrieving hists"
    hists = get_hists(
        region=region,
        icut=0,
        histname=histname,
        samples=samples, 
        rebin=None,
        sys_dict=None,
        )
    #print "got hist", hists
    
    #histnamestr = histname.replace('/','_')
    fname = outname
    fout = ROOT.TFile.Open(fname,'RECREATE')
    for s,h in hists.items():
        hname = 'h_%s_nominal_%s' % (histname,s.name)
        h.SetNameTitle(hname,hname)
        fout.WriteTObject(h,hname)
        ## systematics
        if hasattr(h,'sys_hists'):
         if sys_dict:
            for sys,hsys in h.sys_hists.items():
                
                s_name = sys.name
                
                hname_sys_up = hname.replace('nominal','%s_%s' % (s_name,'UP'))
                hname_sys_dn = hname.replace('nominal','%s_%s' % (s_name,'DN'))

                if hsys[0]: hsys[0].SetNameTitle(hname_sys_up,hname_sys_up)
                if hsys[1]: hsys[1].SetNameTitle(hname_sys_dn,hname_sys_dn)
                fout.WriteTObject(hsys[0],hname_sys_up)
                fout.WriteTObject(hsys[1],hname_sys_dn)

    fout.Close()




def list_open_files():
    l = ROOT.gROOT.GetListOfFiles()
    itr = l.MakeIterator()
    obj = itr.Next()
    while obj:
        print obj.GetName()
        obj = itr.Next()


## EOF
