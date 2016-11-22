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
import array
#import sys_conv


# - - - - - - - - - - - class defs  - - - - - - - - - - - - #




# - - - - - - - - - - function defs - - - - - - - - - - - - #
#____________________________________________________________
def apply_blind(h,blind_min):
    for i in range(1,h.GetNbinsX()+1):
        if h.GetBinLowEdge(i)>=blind_min: 
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
        ):
    '''
    if sys_dict is passed, hists for all systematics will be appended in a dict. 
    '''
    
    hists = {} 
    for s in samples:
      if not s.hist(region=region,icut=icut,histname=histname): continue
      h = s.hist(region=region,icut=icut,histname=histname).Clone()
      if rebin and h: h.Rebin(rebin)
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
    for name,sys in sys_dict.items():
        h_up = h_dn = None
        if sample.estimator.is_affected_by_systematic(sys):
          if not h_up:
            h_up = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone() 
          else:  h_up.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone())
          if not h_dn: h_dn = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone() 
          else:  h_dn.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone())
          h_up.SetName('h_%s_%s_up_%s'%(region,sys.name,sample.name))
          h_dn.SetName('h_%s_%s_dn_%s'%(region,sys.name,sample.name))
          
          if rebin:
           if h_up: h_up.Rebin(rebin)
           if h_dn: h_dn.Rebin(rebin)
             
        hist_dict[sys] = (h_up,h_dn)
    return hist_dict 

#____________________________________________________________
def make_normalised_stat_hist(h):
    '''
    makes histogram with fractional bin uncertainty as entries
    ie. new bin content = old bin error/old bin content
    (used for making stat. ratio bands)
    '''
    h_stat = h.Clone('%s_stat'%(h.GetName()))
    for i in range(1,h.GetNbinsX()+1): 

        n = h.GetBinContent(i)
        en = h.GetBinError(i)
	stat = en
        h_stat.SetBinContent(i,stat) 
    return h_stat



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
def make_stat_scatter(hist1, hist2):
    #make s stat error graph from hist 1, centered on hist 2 (for ratio plot)
    graph = ROOT.TGraphAsymmErrors()
    if hist1.GetNbinsX() == hist2.GetNbinsX():
	    for i in range(1,hist1.GetNbinsX()+1):	
		n = hist1.GetBinContent(i)
		en = hist1.GetBinError(i)
		stat = en / n if n else 0.0	
		ex = hist1.GetBinWidth(i)/2.
		graph.SetPoint(i-1,hist2.GetBinCenter(i),hist2.GetBinContent(i))
		graph.SetPointError(i-1,ex,ex,stat,stat)
	    return graph
#____________________________________________________________
def make_graph_from_hist(hist):
    graph = ROOT.TGraphAsymmErrors()
    for i in range(1,hist.GetNbinsX()+1):
		ex = hist.GetBinWidth(i)/2.
                graph.SetPoint(i-1,hist.GetBinCenter(i),hist.GetBinContent(i))
                graph.SetPointError(i-1,ex,ex,0,0)
    return graph
#____________________________________________________________
def make_error_graph_from_hist(hist):
    graph = ROOT.TGraphAsymmErrors()
    for i in range(1,hist.GetNbinsX()+1):
                ex = hist.GetBinWidth(i)/2.
                graph.SetPoint(i-1,hist.GetBinCenter(i),hist.GetBinContent(i))
		err0 = hist.GetBinError(i)
                n = hist.GetBinContent(i)
		err = err0# / n if n else 0.0
                graph.SetPointError(i-1,ex,ex,err,err)
    return graph


#____________________________________________________________
def make_band_scatter(hist1, h_UP,h_DN=None):
    graph = ROOT.TGraphAsymmErrors()
    if hist1.GetNbinsX() == h_UP.GetNbinsX():
            for i in range(1,hist1.GetNbinsX()+1):
        	eUP = abs(h_UP.GetBinContent(i))
	        eDN = abs(h_UP.GetBinContent(i))
	        if h_DN: eDN = abs(h_DN.GetBinContent(i))
                ex = hist1.GetBinWidth(i)/2.
                graph.SetPoint(i-1,hist1.GetBinCenter(i),hist1.GetBinContent(i))
                graph.SetPointError(i-1,ex,ex,eDN,eUP)
            return graph

#____________________________________________________________
def combination_ratio_stats(hist1,h_num,h_den, h_num_UP,h_num_DN,h_den_UP,h_den_DN):
    graph = ROOT.TGraphAsymmErrors()
    if hist1.GetNbinsX() == h_num_UP.GetNbinsX():
            for i in range(1,hist1.GetNbinsX()+1):
		num = h_num.GetBinContent(i)
		den = h_den.GetBinContent(i)
		if num:
        		up1 = abs(h_num_UP.GetBinContent(i))/num
		else:
			up1 = 0
		if den:
			up2 = abs(h_den_UP.GetBinContent(i))/den
		else:
			up2 = 0
		up_tot = sqrt(up1**2 + up2**2)
                if num:
                	dn1 = abs(h_num_DN.GetBinContent(i))/num
		else:
			dn1 = 0
		if den:
                	dn2 = abs(h_den_DN.GetBinContent(i))/den
		else:
			dn2 = 0
                dn_tot = sqrt(dn1**2 + dn2**2)

                ex = hist1.GetBinWidth(i)/2.
                graph.SetPoint(i-1,hist1.GetBinCenter(i),hist1.GetBinContent(i))
                graph.SetPointError(i-1,ex,ex,dn_tot,up_tot)
            return graph

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
        graph.SetPointError(i-1,ex,ex,eDN,eUP)
    return graph


#____________________________________________________________
def make_error_scatter_graph(hist,h_UP,h_DN):

    graph = ROOT.TGraphAsymmErrors()
    for i in range(1,hist.GetNbinsX()+1):
        eUP = abs(h_UP.GetBinContent(i))
        eDN = abs(h_DN.GetBinContent(i))
	
	ex = h_UP.GetBinWidth(i)/2.
	graph.SetPoint(i-1,hist.GetBinCenter(i),hist.GetBinContent(i))
	graph.SetPointError(i-1,ex,ex,eDN,eUP)
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
    xmin2 	  = None,
    xmax2 	  = None,
    rebin         = None,
    sys_dict      = None,
    do_ratio_plot = False,
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
    assert backgrounds, "ERROR: no background provided for plot_hist"
 
    if signal:samples = backgrounds + signal    
    else: samples = backgrounds
    
    if data: samples += [data] 
    if data: print len(data.daughters)	
    ## generate nominal hists
    hists = get_hists(
	region=region,
	icut=icut,
	histname=histname,
	samples=samples,
	rebin=rebin,
	sys_dict=sys_dict,
	)
    ## sum nominal background
    h_samp_list = []
    for s in backgrounds+signal:
      if not s in hists.keys(): continue
      #print hists[s]
      h_samp_list.append(hists[s])
      if s.name == "Wjets":
	h_wjets = hists[s]
	print "got the", s.name, "hist"
  
    h_total = histutils.add_hists(h_samp_list)

    if xmin2:
        reg = region
        if not reg: reg = ""
        name = '_'.join([reg,histname]).replace('/','_')
        cname = "c_final_%s"%name
        c = ROOT.TCanvas(cname,cname,800,700)

	center_pad = ROOT.TPad("center_pad", "center_pad", 0.0, 0.0, 0.6, 0.6)
 	center_pad.Draw()
	right_pad = ROOT.TPad("right_pad", "right_pad", 0.55, 0.0, 1.0, 0.6)
	right_pad.Draw()
	top_pad = ROOT.TPad("top_pad", "top_pad", 0.0, 0.55, 0.6, 1.0)
	top_pad.Draw()

	projh2X = h_wjets.ProjectionX()
	projh2Y = h_wjets.ProjectionY()

	center_pad.cd()
	h_wjets.Draw("CONT1Z")		
	c_factor = h_wjets.GetCorrelationFactor(1,2)

	print "***********************************************"
	print "correlation factor for", histname, "is", c_factor
	print "***********************************************"

	top_pad.cd()
	projh2X.SetFillColor(ROOT.kYellow-3)
	projh2X.Draw("bar")

	right_pad.cd()
	projh2Y.SetFillColor(ROOT.kYellow-3)
	projh2Y.Draw("hbar")

	c.cd()

        print 'saving plot...'
        c.SaveAs("%s.eps"%c.GetName())
        fout = ROOT.TFile.Open(plotsfile,'UPDATE')
        fout.WriteTObject(c)
        fout.Close()

    else:
	    print "making a 1D plot for you!"

	    ## get stat / sys bands
	    if sys_dict: 
		total_hists = get_total_stat_sys_hists(h_samp_list,sys_dict)
		
		g_stat = make_band_graph_from_hist(total_hists[0])
		g_stat.SetFillColor(ROOT.kGray+3)
		g_stat.SetFillStyle(3001)
		g_tot  = make_band_graph_from_hist(total_hists[3],total_hists[4])
		g_tot.SetFillColor(ROOT.kRed)
		g_tot.SetFillStyle(3001)
	    else:
		h_total_stat = make_stat_hist(h_total)
		g_stat = make_band_graph_from_hist(h_total_stat)
		g_stat.SetFillColor(ROOT.kGray+3)
		g_stat.SetFillStyle(3001)
		
		g_tot = None

	    

            mc_total_stat = make_stat_hist(h_total)
            mc_stat_scatter = make_error_graph_from_hist(h_total)#make_error_scatter_graph(h_total,mc_total_stat,mc_total_stat)
            mc_stat_scatter.SetFillStyle(3001)
            mc_stat_scatter.SetFillColor(ROOT.kGray+3)
            mc_stat_scatter.SetLineStyle(1)
 
	    ROOT.gStyle.SetHatchesLineWidth(3)
            ROOT.gStyle.SetHatchesSpacing(0.05)
	    ## blind data and create ratio 
	    h_data  = None
	    h_ratio = None
	    if data: 
		h_data = hists[data]
		if blind: apply_blind(h_data,blind)
		h_ratio = h_data.Clone('%s_ratio'%(h_data.GetName()))
		h_ratio.Divide(h_total)
		h_ratio.SetMarkerStyle(20)
	    
	    yaxistitle = None
	    for b in reversed(backgrounds):
	      if not b in hists.keys(): continue
	      else : 
		yaxistitle = hists[b].GetYaxis().GetTitle()
		break

	    ## create stack
	    h_stack = ROOT.THStack()
	    for b in reversed(signal+backgrounds):
	      if not b in hists.keys(): continue
	      h_stack.Add(hists[b])
	   
	    nLegend = len(signal+backgrounds) + 1
	    x_legend = 0.63
	    x_leg_shift = -0.055
	    y_leg_shift = 0.0 
	    legYCompr = 8.0
	    legYMax = 0.85
	    legYMin = legYMax - (legYMax - (0.55 + y_leg_shift)) / legYCompr * nLegend
	    legXMin = 0.5#x_legend + x_leg_shift
	    legXMax = 0.87#legXMin + 0.4
	     
	    ## create legend (could use metaroot functionality?)
	    if not do_ratio_plot:
	      legXMin -= 0.005
	      legXMax -= 0.058
	    leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
	    leg.SetBorderSize(0)
	    leg.SetFillColor(0)
	    leg.SetFillStyle(0)
            leg.SetNColumns(2)
            leg.SetTextSize(0.03)
	    if data: leg.AddEntry(h_data,data.tlatex,'PL')
	    for s in signal:
	      sig_tag = s.tlatex
	      if sig_rescale: sig_tag = "%d #times "%int(sig_rescale) + sig_tag
	      if not s in hists.keys(): continue
	      leg.AddEntry(hists[s],sig_tag,'F')
	    for b in backgrounds: 
	      if not b in hists.keys(): continue
	      leg.AddEntry(hists[b],b.tlatex,'F')
	    #leg.AddEntry(mc_stat_scatter, "MC Stat. Unc.","F")
	    if sys_dict:
		leg.AddEntry(g_tot, "Sys + Stat Unc.", 'F')
	    leg.AddEntry(g_stat, "MC Stat.", 'F')

	    ## create canvas
	    reg = region
	    if not reg: reg = ""
	    name = '_'.join([reg,histname]).replace('/','_') 
	    cname = "c_final_%s"%name
	    if do_ratio_plot: c = ROOT.TCanvas(cname,cname,600,600)
	    else: c = ROOT.TCanvas(cname,cname,800,600)	
	    if xmin==None: xmin = h_total.GetBinLowEdge(1)
	    if xmax==None: xmax = h_total.GetBinLowEdge(h_total.GetNbinsX()+1)
	    ymin = 1.e-3
	    ymax = h_total.GetMaximum()
	    for s in signal:
	      if not s in hists.keys(): continue
	      ymax = max([ymax,hists[s].GetMaximum()])
	    if data: ymax = max([ymax,h_data.GetMaximum()])
	    if log: ymax *= 100000.
	    else:   ymax *= 1.8
	    xtitle = h_total.GetXaxis().GetTitle()

	    ratio_line = ROOT.TLine(xmin,1,xmax,1)
	    ratio_line.SetLineColor(ROOT.kRed)
            ratio_line.SetLineStyle(7)

	    if do_ratio_plot: rsplit = 0.3
	    else: rsplit = 0.
	    pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
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
	      #pad2.SetGridy()
	    #if do_ratio_plot: pad2.Draw()
	      pad2.Draw()
	    pad1.cd()

	    ytitle = "Events" 
	    if not rebin: ytitle = yaxistitle
            #ytitle = yaxistitle
	    elif rebin!=1:
	      if not "BDT" in xtitle:
		if ("f" in xtitle) or ("track" in xtitle) or ("S" in xtitle) or ("R" in xtitle) or ("eta" in xtitle) or ("phi" in xtitle) or ("trk" in xtitle): pass
		ytitle += " / %s"%rebin
		ytitle += " GeV"
	      #else: ytitle += " / %s"%(0.05)

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

	    yaxis1.SetTitleSize(0.045)# yaxis1.GetTitleSize() * scale )
	    yaxis1.SetTitleOffset( 2.1 * yaxis1.GetTitleOffset() / scale )
	    yaxis1.SetLabelSize(0.04)# 0.8 * yaxis1.GetLabelSize() * scale )
	    yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
	    xaxis1.SetNdivisions(510)
	    yaxis1.SetNdivisions(510)
            xaxis1.SetLabelSize(0.04)

	    h_stack.Draw("SAME,HIST")
	    mc_stat_scatter.Draw("E2 SAME") 
	    """
	    for s in reversed(signal):
	      if not s in hists.keys(): continue
	      if sig_rescale: hists[s].Scale(sig_rescale)
	      hists[s].Draw("SAME,HIST")
	    """
	    
	    if data: h_data.Draw("SAME")
	    pad1.SetLogy(log)
	    pad1.SetLogx(logx)
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
	    lumi = backgrounds[0].estimator.hm.target_lumi/1000.
	    textsize = 0.7
	    if not do_ratio_plot: textsize = 0.8
	    latex_y = ty-2.*th
	    tlatex.DrawLatex(tx,latex_y,"#scale[0.7]{#bf{#it{ATLAS}} Internal}")
	    tlatex.DrawLatex(tx,latex_y-0.07,'#scale[%lf]{#scale[%lf]{#int}L dt = %2.1f fb^{-1}}'%(textsize,0.8*textsize,lumi) )
	    tlatex.DrawLatex(tx,latex_y-0.14,'#scale[%lf]{#sqrt{s} = 13 TeV}'%(textsize))
	    tlatex.DrawLatex(tx, latex_y-0.21,'#scale[%lf]{Z#rightarrow#tau#tau#rightarrow#mu#tau_{had} T&P}'%(textsize))
	    if label:
              if "_" in label:
		list_labels = label.split("_")
		fin_lab = ""
		for j in range(len(list_labels)):
			fin_lab += list_labels[j]
			fin_lab += " "

	        tlatex.DrawLatex(tx,latex_y - 0.28,"#scale[0.7]{%s}"%(str(fin_lab)))
	      #latex_y -= 0.1
	      #for i,line in enumerate(label):
	      #  tlatex.DrawLatex(tx,latex_y-i*0.06,"#scale[%lf]{%s}"%(textsize,line))
	    if blind:
		line = ROOT.TLine()
		line.SetLineColor(ROOT.kBlack)
		line.SetLineStyle(2)
		line.DrawLine(blind,ymin,blind,ymax)
		bltext = ROOT.TLatex()
		bltext.SetTextFont(42)
		bltext.SetTextSize(0.04)
		bltext.SetTextAngle(90.)
		bltext.SetTextAlign(31)
		bltext.DrawLatex(blind,ymax, 'Blind   ')

	    if do_ratio_plot:
	      pad2.cd()
	      fr2 = pad2.DrawFrame(xmin,0.49,xmax,1.51,';%s;Data/exp.'%(xtitle))
	      xaxis2 = fr2.GetXaxis()
	      yaxis2 = fr2.GetYaxis()
	      scale = (1. / rsplit)
	      yaxis2.SetTitleSize( 0.095)#yaxis2.GetTitleSize() * scale )
	      yaxis2.SetLabelSize( 0.095)#yaxis2.GetLabelSize() * scale )
	      yaxis2.SetTitleOffset(0.4)# 2.1* yaxis2.GetTitleOffset() / scale  )
	      yaxis2.SetLabelOffset(0.4 * yaxis2.GetLabelOffset() * scale )
	      xaxis2.SetTitleSize( 0.095)#xaxis2.GetTitleSize() * scale )
	      xaxis2.SetLabelSize( 0.095)#0.8 * xaxis2.GetLabelSize() * scale )
	      xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
	      xaxis2.SetTitleOffset( 3.2* xaxis2.GetTitleOffset() / scale  )
	      xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
	      yaxis2.SetNdivisions(510)
	      xaxis2.SetNdivisions(510)

	      if logx: 
		pad2.SetLogx(logx) 
		xaxis2.SetMoreLogLabels()
	      else: 
		pass
              ratio_line.Draw()
	      if g_tot: 
                 g_tot.Draw("E2 Same")
		 g_stat.Draw("E2 Same")

	      else: g_stat.Draw("E2")

	      if data: h_ratio.Draw("SAME") 
	      pad2.RedrawAxis()

	    print 'saving plot...'
	    if not log: c.SaveAs("%s.eps"%c.GetName())
	    else:   c.SaveAs("%s_LOG.eps"%c.GetName())
	    fout = ROOT.TFile.Open(plotsfile,'UPDATE')
	    fout.WriteTObject(c)
	    fout.Close()

#____________________________________________________________
def write_hist(
        backgrounds = None,
        signal     = None,
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
    samples = backgrounds + signal
    if data: samples += [data]
    ## generate nominal hists
    hists = get_hists(
        region=region,
        icut=icut,
        histname=histname,
        samples=samples, 
        rebin=rebin,
        sys_dict=sys_dict,
        )

    #histnamestr = histname.replace('/','_')
    fname = outname
    fout = ROOT.TFile.Open(fname,'RECREATE')
    for s,h in hists.items():
        hname = 'h_%s_nominal_%s' % (region,s.name)
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

    ## create total background hists
    #h_total = histutils.add_hists([ hists[s] for s in backgrounds ])
    #fout.WriteTObject(h_total,'h_%s_nominal_smtot'%region)
    
    fout.Close()


def list_open_files():
    l = ROOT.gROOT.GetListOfFiles()
    itr = l.MakeIterator()
    obj = itr.Next()
    while obj:
        print obj.GetName()
        obj = itr.Next()

def ratiounc(a,b,sigmaa,sigmab):
  unc = 0 
  unc += pow(1./b,2) * sigmaa * sigmaa
  unc += (pow(a,2) / pow(b,4)) * sigmab * sigmab
  return sqrt(unc)

## EOF
