# encoding: utf-8
'''
samples.py

'''
## modules
from sample import Sample
from colours import *
import ROOT


# -----------------------------------------
# data
# -----------------------------------------

GRL = []

GRL += [ 
         "00309640","00279764","00307732","00308047","00301918","00309759","00302380",
         "00306419","00300287","00281074","00306655","00276778","00301932","00307124",
         "00279259","00280368","00306247","00309516","00304178","00280500","00283429",
         "00299584","00303201","00304198","00298773","00304128","00303846","00300784",
         "00303499","00303007","00304308","00299184","00302391","00299340","00305777",
         "00305380","00300279","00283074","00303943","00301912","00280673","00280231",
         "00307935","00299147","00301973","00279813","00281385","00310341","00303291",
         "00284473","00304243","00306278","00279984","00305293","00303421","00282784",
         "00282712","00302300","00305727","00305291","00283608","00305674","00310863",
         "00310691","00276511","00309674","00307656","00302137","00299315","00302829",
         "00305543","00299243","00310405","00278880","00306269","00300418",
         ]
#GRL = ['00300418']
GRL.sort()

ds_name = '%s'

for run in GRL:
    name = ds_name % run
    globals()[name] = Sample(
            name = name,
            type = "data"
            )

list_runs =[globals()[ds_name%(run)] for run in GRL]

data = Sample(name         = "data",
              tlatex       = "Data 2015",
              fill_color   = ROOT.kWhite,
              fill_style   = 0,
              line_color   = ROOT.kBlack,
              line_style   = 1,
              marker_color = ROOT.kBlack,
              marker_style = 20,
              daughters    = list_runs,
              )

# -----------------------------------------
# Ztautau
# -----------------------------------------
Sh221_PDF30_Ztt_MHPT0_70_l13l7                    = Sample(  name="Sh221_PDF30_Ztt_MHPT0_70_l13l7"          , dsid="344772" , xsec=50.1405  , kfactor=0.9751 ) 
Sh221_PDF30_Ztt_MHPT0_70_l15h20                   = Sample(  name="Sh221_PDF30_Ztt_MHPT0_70_l15h20"         , dsid="344774" , xsec=105.6425 , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT70_140_l13l7                  = Sample(  name="Sh221_PDF30_Ztt_MHPT70_140_l13l7"        , dsid="344776" , xsec=3.8705   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT70_140_l15h20                 = Sample(  name="Sh221_PDF30_Ztt_MHPT70_140_l15h20"       , dsid="344778" , xsec=7.945    , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT140_280_l13l7                 = Sample(  name="Sh221_PDF30_Ztt_MHPT140_280_l13l7"       , dsid="344780" , xsec=1.68222  , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT140_280_l15h20                = Sample(  name="Sh221_PDF30_Ztt_MHPT140_280_l15h20"      , dsid="344781" , xsec=3.8047   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT280_500_CVetoBVeto            = Sample(  name="Sh221_PDF30_Ztt_MHPT280_500_CVetoBVeto"  , dsid="364137" , xsec=4.7911   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT280_500_CFiltBVet             = Sample(  name="Sh221_PDF30_Ztt_MHPT280_500_CFiltBVet"   , dsid="364138" , xsec=2.2756   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT280_500_BFilter               = Sample(  name="Sh221_PDF30_Ztt_MHPT280_500_BFilter"     , dsid="364139" , xsec=1.5028   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT500_1000                      = Sample(  name="Sh221_PDF30_Ztt_MHPT500_1000"            , dsid="364140" , xsec=1.8096   , kfactor=0.9751 )
Sh221_PDF30_Ztt_MHPT1000_E_CMS                    = Sample(  name="Sh221_PDF30_Ztt_MHPT1000_E_CMS"          , dsid="364141" , xsec=0.14834  , kfactor=0.9751 )

Ztautau =  Sample( name =   'Ztautau',
                   tlatex = 'Z#rightarrow#tau#tau',
                   fill_color   =  1041,
                   line_color   =  1041,
                   marker_color =  1041,
                   daughters    = [
                                   Sh221_PDF30_Ztt_MHPT0_70_l13l7,
                                   Sh221_PDF30_Ztt_MHPT0_70_l15h20,       
                                   Sh221_PDF30_Ztt_MHPT70_140_l13l7,      
                                   Sh221_PDF30_Ztt_MHPT70_140_l15h20,     
                                   Sh221_PDF30_Ztt_MHPT140_280_l13l7,    
                                   Sh221_PDF30_Ztt_MHPT140_280_l15h20,    
                                   Sh221_PDF30_Ztt_MHPT280_500_CVetoBVeto,
                                   Sh221_PDF30_Ztt_MHPT280_500_CFiltBVet, 
                                   Sh221_PDF30_Ztt_MHPT280_500_BFilter,   
                                   Sh221_PDF30_Ztt_MHPT500_1000,          
                                   Sh221_PDF30_Ztt_MHPT1000_E_CMS,        
                                ]
                )


# -----------------------------------------
# Zleplep
# -----------------------------------------
Sh221_PDF30_Zmumu_MHPT0_70_CVetoBVeto             = Sample(  name="Sh221_PDF30_Zmumu_MHPT0_70_CVetoBVeto"      , dsid="364100" , xsec=1630.2243  , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT0_70_CFiltBVet              = Sample(  name="Sh221_PDF30_Zmumu_MHPT0_70_CFiltBVet"       , dsid="364101" , xsec=223.72     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT0_70_BFilter                = Sample(  name="Sh221_PDF30_Zmumu_MHPT0_70_BFilter"         , dsid="364102" , xsec=127.180    , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT70_140_CVetoBVeto           = Sample(  name="Sh221_PDF30_Zmumu_MHPT70_140_CVetoBVeto"    , dsid="364103" , xsec=75.016     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT70_140_CFiltBVet            = Sample(  name="Sh221_PDF30_Zmumu_MHPT70_140_CFiltBVet"     , dsid="364104" , xsec=20.348     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT70_140_BFilter              = Sample(  name="Sh221_PDF30_Zmumu_MHPT70_140_BFilter"       , dsid="364105" , xsec=12.388     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT140_280_CVetoBVeto          = Sample(  name="Sh221_PDF30_Zmumu_MHPT140_280_CVetoBVeto"   , dsid="364106" , xsec=24.285     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT140_280_CFiltBVet           = Sample(  name="Sh221_PDF30_Zmumu_MHPT140_280_CFiltBVet"    , dsid="364107" , xsec=9.275      , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT140_280_BFilter             = Sample(  name="Sh221_PDF30_Zmumu_MHPT140_280_BFilter"      , dsid="364108" , xsec=5.833      , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT280_500_CVetoBVeto          = Sample(  name="Sh221_PDF30_Zmumu_MHPT280_500_CVetoBVeto"   , dsid="364109" , xsec=4.7729     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT280_500_CFiltBVet           = Sample(  name="Sh221_PDF30_Zmumu_MHPT280_500_CFiltBVet"    , dsid="364110" , xsec=2.2655     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT280_500_BFilter             = Sample(  name="Sh221_PDF30_Zmumu_MHPT280_500_BFilter"      , dsid="364111" , xsec=1.4913     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT500_1000                    = Sample(  name="Sh221_PDF30_Zmumu_MHPT500_1000"             , dsid="364112" , xsec=1.7881     , kfactor=0.9751  )
Sh221_PDF30_Zmumu_MHPT1000_E_CMS                  = Sample(  name="Sh221_PDF30_Zmumu_MHPT1000_E_CMS"           , dsid="364113" , xsec=0.14769    , kfactor=0.9751  )
Sh221__Zmm_Mll10_40_MHPT70_280_BVeto              = Sample(  name="Sh221__Zmm_Mll10_40_MHPT70_280_BVeto"       , dsid="364200" , xsec=44.8791    , kfactor=0.9751  )
Sh221__Zmm_Mll10_40_MHPT70_280_BFilter            = Sample(  name="Sh221__Zmm_Mll10_40_MHPT70_280_BFilter"     , dsid="364201" , xsec=5.115      , kfactor=0.9751  )
Sh221__Zmm_Mll10_40_MHPT280_BVeto                 = Sample(  name="Sh221__Zmm_Mll10_40_MHPT280_BVeto"          , dsid="364202" , xsec=2.760      , kfactor=0.9751  )
Sh221__Zmm_Mll10_40_MHPT280_BFilter               = Sample(  name="Sh221__Zmm_Mll10_40_MHPT280_BFilter"        , dsid="364203" , xsec=0.4721     , kfactor=0.9751  )

Sh221_PDF30_Zee_MHPT0_70_CVetoBVeto               = Sample(  name="Sh221_PDF30_Zee_MHPT0_70_CVetoBVeto"        , dsid="364114" , xsec=1627.1767  , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT0_70_CFiltBVet                = Sample(  name="Sh221_PDF30_Zee_MHPT0_70_CFiltBVet"         , dsid="364115" , xsec=223.731    , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT0_70_BFilter                  = Sample(  name="Sh221_PDF30_Zee_MHPT0_70_BFilter"           , dsid="364116" , xsec=126.45     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT70_140_CVetoBVeto             = Sample(  name="Sh221_PDF30_Zee_MHPT70_140_CVetoBVeto"      , dsid="364117" , xsec=76.292     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT70_140_CFiltBVet              = Sample(  name="Sh221_PDF30_Zee_MHPT70_140_CFiltBVet"       , dsid="364118" , xsec=20.336     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT70_140_BFilter                = Sample(  name="Sh221_PDF30_Zee_MHPT70_140_BFilter"         , dsid="364119" , xsec=12.623     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT140_280_CVetoBVeto            = Sample(  name="Sh221_PDF30_Zee_MHPT140_280_CVetoBVeto"     , dsid="364120" , xsec=25.0300    , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT140_280_CFiltBVet             = Sample(  name="Sh221_PDF30_Zee_MHPT140_280_CFiltBVet"      , dsid="364121" , xsec=9.372      , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT140_280_BFilter               = Sample(  name="Sh221_PDF30_Zee_MHPT140_280_BFilter"        , dsid="364122" , xsec=6.0826     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT280_500_CVetoBVeto            = Sample(  name="Sh221_PDF30_Zee_MHPT280_500_CVetoBVeto"     , dsid="364123" , xsec=4.8692     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT280_500_CFiltBVet             = Sample(  name="Sh221_PDF30_Zee_MHPT280_500_CFiltBVet"      , dsid="364124" , xsec=2.2799     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT280_500_BFilter               = Sample(  name="Sh221_PDF30_Zee_MHPT280_500_BFilter"        , dsid="364125" , xsec=1.49437    , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT500_1000                      = Sample(  name="Sh221_PDF30_Zee_MHPT500_1000"               , dsid="364126" , xsec=1.8081     , kfactor=0.9751  )
Sh221_PDF30_Zee_MHPT1000_E_CMS                    = Sample(  name="Sh221_PDF30_Zee_MHPT1000_E_CMS"             , dsid="364127" , xsec=0.14857    , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT0_70_BVeto                = Sample(  name="Sh221__Zee_Mll10_40_MHPT0_70_BVeto"         , dsid="364204" , xsec=2331.22    , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT0_70_BFilter              = Sample(  name="Sh221__Zee_Mll10_40_MHPT0_70_BFilter"       , dsid="364205" , xsec=81.357     , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT70_280_BVeto              = Sample(  name="Sh221__Zee_Mll10_40_MHPT70_280_BVeto"       , dsid="364206" , xsec=44.97      , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT70_280_BFilter            = Sample(  name="Sh221__Zee_Mll10_40_MHPT70_280_BFilter"     , dsid="364207" , xsec=5.4814     , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT280_BVeto                 = Sample(  name="Sh221__Zee_Mll10_40_MHPT280_BVeto"          , dsid="364208" , xsec=2.777      , kfactor=0.9751  )
Sh221__Zee_Mll10_40_MHPT280_BFilter               = Sample(  name="Sh221__Zee_Mll10_40_MHPT280_BFilter"        , dsid="364209" , xsec=0.4730     , kfactor=0.9751  )

Zleplep =  Sample( name =   'Zleplep',
                   tlatex = 'Z#rightarrowll',
                   fill_color   =  1053,
                   line_color   =  1053,
                   marker_color =  1053,
                   daughters    = [
                                    Sh221_PDF30_Zmumu_MHPT0_70_CVetoBVeto,                                     
                                    Sh221_PDF30_Zmumu_MHPT0_70_CFiltBVet,   
                                    Sh221_PDF30_Zmumu_MHPT0_70_BFilter,     
                                    Sh221_PDF30_Zmumu_MHPT70_140_CVetoBVeto,
                                    Sh221_PDF30_Zmumu_MHPT70_140_CFiltBVet, 
                                    Sh221_PDF30_Zmumu_MHPT70_140_BFilter,   
                                    Sh221_PDF30_Zmumu_MHPT140_280_CVetoBVeto,
                                    Sh221_PDF30_Zmumu_MHPT140_280_CFiltBVet,
                                    Sh221_PDF30_Zmumu_MHPT140_280_BFilter,  
                                    Sh221_PDF30_Zmumu_MHPT280_500_CVetoBVeto,
                                    Sh221_PDF30_Zmumu_MHPT280_500_CFiltBVet,
                                    Sh221_PDF30_Zmumu_MHPT280_500_BFilter,  
                                    Sh221_PDF30_Zmumu_MHPT500_1000,         
                                    Sh221_PDF30_Zmumu_MHPT1000_E_CMS,       
                                    Sh221__Zmm_Mll10_40_MHPT70_280_BVeto,   
                                    Sh221__Zmm_Mll10_40_MHPT70_280_BFilter, 
                                    Sh221__Zmm_Mll10_40_MHPT280_BVeto,      
                                    Sh221__Zmm_Mll10_40_MHPT280_BFilter,    
                                    Sh221_PDF30_Zee_MHPT0_70_CVetoBVeto,    
                                    Sh221_PDF30_Zee_MHPT0_70_CFiltBVet,     
                                    Sh221_PDF30_Zee_MHPT0_70_BFilter,       
                                    Sh221_PDF30_Zee_MHPT70_140_CVetoBVeto,  
                                    Sh221_PDF30_Zee_MHPT70_140_CFiltBVet,   
                                    Sh221_PDF30_Zee_MHPT70_140_BFilter,     
                                    Sh221_PDF30_Zee_MHPT140_280_CVetoBVeto,
                                    Sh221_PDF30_Zee_MHPT140_280_CFiltBVet,  
                                    Sh221_PDF30_Zee_MHPT140_280_BFilter,    
                                    Sh221_PDF30_Zee_MHPT280_500_CVetoBVeto, 
                                    Sh221_PDF30_Zee_MHPT280_500_CFiltBVet,  
                                    Sh221_PDF30_Zee_MHPT280_500_BFilter,    
                                    Sh221_PDF30_Zee_MHPT500_1000,           
                                    Sh221_PDF30_Zee_MHPT1000_E_CMS,         
                                    Sh221__Zee_Mll10_40_MHPT0_70_BVeto,     
                                    Sh221__Zee_Mll10_40_MHPT0_70_BFilter,   
                                    Sh221__Zee_Mll10_40_MHPT70_280_BVeto,   
                                    Sh221__Zee_Mll10_40_MHPT70_280_BFilter, 
                                    Sh221__Zee_Mll10_40_MHPT280_BVeto,      
                                    Sh221__Zee_Mll10_40_MHPT280_BFilter,    
                                 ]
                )



# -----------------------------------------
# Wlepnu
# -----------------------------------------
Sh221_PDF30_Wmunu_MHPT0_70_CVetoBVeto             = Sample(  name="Sh221_PDF30_Wmunu_MHPT0_70_CVetoBVeto"      , dsid="364156" , xsec=19143     , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT0_70_CFiltBVet              = Sample(  name="Sh221_PDF30_Wmunu_MHPT0_70_CFiltBVet"       , dsid="364157" , xsec=2493.38   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT0_70_BFilter                = Sample(  name="Sh221_PDF30_Wmunu_MHPT0_70_BFilter"         , dsid="364158" , xsec=853.97    , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT70_140_CVetoBVeto           = Sample(  name="Sh221_PDF30_Wmunu_MHPT70_140_CVetoBVeto"    , dsid="364159" , xsec=637.42    , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT70_140_CFiltBVet            = Sample(  name="Sh221_PDF30_Wmunu_MHPT70_140_CFiltBVet"     , dsid="364160" , xsec=219.965   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT70_140_BFilter              = Sample(  name="Sh221_PDF30_Wmunu_MHPT70_140_BFilter"       , dsid="364161" , xsec=73.191    , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT140_280_CVetoBVeto          = Sample(  name="Sh221_PDF30_Wmunu_MHPT140_280_CVetoBVeto"   , dsid="364162" , xsec=207.554   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT140_280_CFiltBVet           = Sample(  name="Sh221_PDF30_Wmunu_MHPT140_280_CFiltBVet"    , dsid="364163" , xsec=98.437    , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT140_280_BFilter             = Sample(  name="Sh221_PDF30_Wmunu_MHPT140_280_BFilter"      , dsid="364164" , xsec=37.4744   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT280_500_CVetoBVeto          = Sample(  name="Sh221_PDF30_Wmunu_MHPT280_500_CVetoBVeto"   , dsid="364165" , xsec=39.3824   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT280_500_CFiltBVet           = Sample(  name="Sh221_PDF30_Wmunu_MHPT280_500_CFiltBVet"    , dsid="364166" , xsec=22.9178   , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT280_500_BFilter             = Sample(  name="Sh221_PDF30_Wmunu_MHPT280_500_BFilter"      , dsid="364167" , xsec=9.6086    , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT500_1000                    = Sample(  name="Sh221_PDF30_Wmunu_MHPT500_1000"             , dsid="364168" , xsec=15.01     , kfactor=0.9702  )
Sh221_PDF30_Wmunu_MHPT1000_E_CMS                  = Sample(  name="Sh221_PDF30_Wmunu_MHPT1000_E_CMS"           , dsid="364169" , xsec=1.2344    , kfactor=0.9702  )

Sh221_PDF30_Wenu_MHPT0_70_CVetoBVeto              = Sample(  name="Sh221_PDF30_Wenu_MHPT0_70_CVetoBVeto"       , dsid="364170" , xsec=15769.63  , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT0_70_CFiltBVet               = Sample(  name="Sh221_PDF30_Wenu_MHPT0_70_CFiltBVet"        , dsid="364171" , xsec=2492.639  , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT0_70_BFilter                 = Sample(  name="Sh221_PDF30_Wenu_MHPT0_70_BFilter"          , dsid="364172" , xsec=844.6380  , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT70_140_CVetoBVeto            = Sample(  name="Sh221_PDF30_Wenu_MHPT70_140_CVetoBVeto"     , dsid="364173" , xsec=630.322   , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT70_140_CFiltBVet             = Sample(  name="Sh221_PDF30_Wenu_MHPT70_140_CFiltBVet"      , dsid="364174" , xsec=215.49    , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT70_140_BFilter               = Sample(  name="Sh221_PDF30_Wenu_MHPT70_140_BFilter"        , dsid="364175" , xsec=97.74     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT140_280_CVetoBVeto           = Sample(  name="Sh221_PDF30_Wenu_MHPT140_280_CVetoBVeto"    , dsid="364176" , xsec=202.8359  , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT140_280_CFiltBVet            = Sample(  name="Sh221_PDF30_Wenu_MHPT140_280_CFiltBVet"     , dsid="364177" , xsec=98.44     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT140_280_BFilter              = Sample(  name="Sh221_PDF30_Wenu_MHPT140_280_BFilter"       , dsid="364178" , xsec=33.996    , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT280_500_CVetoBVeto           = Sample(  name="Sh221_PDF30_Wenu_MHPT280_500_CVetoBVeto"    , dsid="364179" , xsec=39.24     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT280_500_CFiltBVet            = Sample(  name="Sh221_PDF30_Wenu_MHPT280_500_CFiltBVet"     , dsid="364180" , xsec=22.84     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT280_500_BFilter              = Sample(  name="Sh221_PDF30_Wenu_MHPT280_500_BFilter"       , dsid="364181" , xsec=9.656     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT500_1000                     = Sample(  name="Sh221_PDF30_Wenu_MHPT500_1000"              , dsid="364182" , xsec=15.04     , kfactor=0.9702  )
Sh221_PDF30_Wenu_MHPT1000_E_CMS                   = Sample(  name="Sh221_PDF30_Wenu_MHPT1000_E_CMS"            , dsid="364183" , xsec=1.2334    , kfactor=0.9702  )

Wlepnu =  Sample( name =   'Wlepnu',
                   tlatex = 'W+Jets',
                   fill_color   =  1055,
                   line_color   =  1055,
                   marker_color =  1055,
                   daughters    = [
                                     Sh221_PDF30_Wmunu_MHPT0_70_CVetoBVeto,                                      
                                     Sh221_PDF30_Wmunu_MHPT0_70_CFiltBVet,      
                                     Sh221_PDF30_Wmunu_MHPT0_70_BFilter,        
                                     Sh221_PDF30_Wmunu_MHPT70_140_CVetoBVeto,   
                                     Sh221_PDF30_Wmunu_MHPT70_140_CFiltBVet,    
                                     Sh221_PDF30_Wmunu_MHPT70_140_BFilter,      
                                     Sh221_PDF30_Wmunu_MHPT140_280_CVetoBVeto,  
                                     Sh221_PDF30_Wmunu_MHPT140_280_CFiltBVet,   
                                     Sh221_PDF30_Wmunu_MHPT140_280_BFilter,     
                                     Sh221_PDF30_Wmunu_MHPT280_500_CVetoBVeto,  
                                     Sh221_PDF30_Wmunu_MHPT280_500_CFiltBVet,   
                                     Sh221_PDF30_Wmunu_MHPT280_500_BFilter,     
                                     Sh221_PDF30_Wmunu_MHPT500_1000,            
                                     Sh221_PDF30_Wmunu_MHPT1000_E_CMS,          
                                     Sh221_PDF30_Wenu_MHPT0_70_CVetoBVeto,      
                                     Sh221_PDF30_Wenu_MHPT0_70_CFiltBVet,       
                                     Sh221_PDF30_Wenu_MHPT0_70_BFilter,         
                                     Sh221_PDF30_Wenu_MHPT70_140_CVetoBVeto,    
                                     Sh221_PDF30_Wenu_MHPT70_140_CFiltBVet,     
                                     Sh221_PDF30_Wenu_MHPT70_140_BFilter,       
                                     Sh221_PDF30_Wenu_MHPT140_280_CVetoBVeto,   
                                     Sh221_PDF30_Wenu_MHPT140_280_CFiltBVet,    
                                     Sh221_PDF30_Wenu_MHPT140_280_BFilter,      
                                     Sh221_PDF30_Wenu_MHPT280_500_CVetoBVeto,   
                                     Sh221_PDF30_Wenu_MHPT280_500_CFiltBVet,    
                                     Sh221_PDF30_Wenu_MHPT280_500_BFilter,      
                                     Sh221_PDF30_Wenu_MHPT500_1000,             
                                     Sh221_PDF30_Wenu_MHPT1000_E_CMS,           
                                  ]
                )
                     
# -----------------------------------------
# Wtaunu
# -----------------------------------------
Sh221_PDF30_Wtaunu_MHPT0_70_CVetoBVeto            = Sample(  name="Sh221_PDF30_Wtaunu_MHPT0_70_CVetoBVeto"     , dsid="364184" , xsec=15799.44   , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT0_70_CFiltBVet             = Sample(  name="Sh221_PDF30_Wtaunu_MHPT0_70_CFiltBVet"      , dsid="364185" , xsec=2477.249   , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT0_70_BFilter               = Sample(  name="Sh221_PDF30_Wtaunu_MHPT0_70_BFilter"        , dsid="364186" , xsec=854.55     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT70_140_CVetoBVeto          = Sample(  name="Sh221_PDF30_Wtaunu_MHPT70_140_CVetoBVeto"   , dsid="364187" , xsec=638.54     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT70_140_CFiltBVet           = Sample(  name="Sh221_PDF30_Wtaunu_MHPT70_140_CFiltBVet"    , dsid="364188" , xsec=210.3823   , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT70_140_BFilter             = Sample(  name="Sh221_PDF30_Wtaunu_MHPT70_140_BFilter"      , dsid="364189" , xsec=98.065     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT140_280_CVetoBVeto         = Sample(  name="Sh221_PDF30_Wtaunu_MHPT140_280_CVetoBVeto"  , dsid="364190" , xsec=202.33     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT140_280_CFiltBVet          = Sample(  name="Sh221_PDF30_Wtaunu_MHPT140_280_CFiltBVet"   , dsid="364191" , xsec=98.577     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT140_280_BFilter            = Sample(  name="Sh221_PDF30_Wtaunu_MHPT140_280_BFilter"     , dsid="364192" , xsec=38.128     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT280_500_CVetoBVeto         = Sample(  name="Sh221_PDF30_Wtaunu_MHPT280_500_CVetoBVeto"  , dsid="364193" , xsec=39.316     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT280_500_CFiltBVet          = Sample(  name="Sh221_PDF30_Wtaunu_MHPT280_500_CFiltBVet"   , dsid="364194" , xsec=22.7789    , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT280_500_BFilter            = Sample(  name="Sh221_PDF30_Wtaunu_MHPT280_500_BFilter"     , dsid="364195" , xsec=9.6702     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT500_1000                   = Sample(  name="Sh221_PDF30_Wtaunu_MHPT500_1000"            , dsid="364196" , xsec=15.046     , kfactor=0.9702  )
Sh221_PDF30_Wtaunu_MHPT1000_E_CMS                 = Sample(  name="Sh221_PDF30_Wtaunu_MHPT1000_E_CMS"          , dsid="364197" , xsec=1.2339     , kfactor=0.9702  )

Wtaunu =  Sample( name =   'Wtaunu',
                   tlatex = 'W#rightarrow #tau#nu+Jets',
                   fill_color   =  1052,
                   line_color   =  1052,
                   marker_color =  1052,
                   daughters    = [
                                    Sh221_PDF30_Wtaunu_MHPT0_70_CVetoBVeto,
                                    Sh221_PDF30_Wtaunu_MHPT0_70_CFiltBVet,    
                                    Sh221_PDF30_Wtaunu_MHPT0_70_BFilter,      
                                    Sh221_PDF30_Wtaunu_MHPT70_140_CVetoBVeto, 
                                    Sh221_PDF30_Wtaunu_MHPT70_140_CFiltBVet,  
                                    Sh221_PDF30_Wtaunu_MHPT70_140_BFilter,    
                                    Sh221_PDF30_Wtaunu_MHPT140_280_CVetoBVeto,
                                    Sh221_PDF30_Wtaunu_MHPT140_280_CFiltBVet, 
                                    Sh221_PDF30_Wtaunu_MHPT140_280_BFilter,   
                                    Sh221_PDF30_Wtaunu_MHPT280_500_CVetoBVeto,
                                    Sh221_PDF30_Wtaunu_MHPT280_500_CFiltBVet, 
                                    Sh221_PDF30_Wtaunu_MHPT280_500_BFilter,   
                                    Sh221_PDF30_Wtaunu_MHPT500_1000,          
                                    Sh221_PDF30_Wtaunu_MHPT1000_E_CMS,        
                                  ]
                )

# -----------------------------------------
# Top
# -----------------------------------------
PoPy_P2012_ttb_nonallh                            = Sample(  name="PoPy_P2012_ttb_nonallh"           , dsid="410000" , xsec=831.78   , kfactor=0.543   )
PoPy_P2012_ttb_allh                               = Sample(  name="PoPy_P2012_ttb_allh"              , dsid="410007" , xsec=831.77   , kfactor=0.4562  )
PoPy_P2012_st_tchan_lept_top                      = Sample(  name="PoPy_P2012_st_tchan_lept_top"     , dsid="410011" , xsec=44.1501  , kfactor=1.0000  )
PoPy_P2012_st_tchan_lept_atop                     = Sample(  name="PoPy_P2012_st_tchan_lept_atop"    , dsid="410012" , xsec=25.778   , kfactor=1.0193  )
PoPy_P2012_Wt_incl_top                            = Sample(  name="PoPy_P2012_Wt_incl_top"           , dsid="410013" , xsec=34.009   , kfactor=1.054   )
PoPy_P2012_Wt_incl_atop                           = Sample(  name="PoPy_P2012_Wt_incl_atop"          , dsid="410014" , xsec=33.989   , kfactor=1.054   )
PoPy_P2012_STSchan_noAllHad_top                   = Sample(  name="PoPy_P2012_STSchan_noAllHad_top"  , dsid="410025" , xsec=2.0517   , kfactor=1.0046  )
PoPy_P2012_STSchan_noAllHad_atop                  = Sample(  name="PoPy_P2012_STSchan_noAllHad_atop" , dsid="410026" , xsec=1.2615   , kfactor=1.0215  )


top =  Sample( name =   'top',
               tlatex = 'Top',
               fill_color   =  1022,
               line_color   =  1022,
               marker_color =  1022,
               daughters    = [
                                PoPy_P2012_ttb_nonallh,
                                PoPy_P2012_ttb_allh,             
                                PoPy_P2012_st_tchan_lept_top,    
                                PoPy_P2012_st_tchan_lept_atop,   
                                PoPy_P2012_Wt_incl_top,          
                                PoPy_P2012_Wt_incl_atop,         
                                PoPy_P2012_STSchan_noAllHad_top, 
                                PoPy_P2012_STSchan_noAllHad_atop,
                              ]
             )


# -----------------------------------------
# LFVH
# -----------------------------------------
PoPy8_ggH125_taumu                                = Sample(  name="PoPy8_ggH125_taumu"     , dsid="344084" , xsec=30.1089 )
PoPy8_VBFH125_taumu                               = Sample(  name="PoPy8_VBFH125_taumu"    , dsid="344085" , xsec=3.8155  )
PoPy8_ggH125_taue                                 = Sample(  name="PoPy8_ggH125_taue"      , dsid="344088" , xsec=30.189  )
PoPy8_VBFH125_taue                                = Sample(  name="PoPy8_VBFH125_taue"     , dsid="344089" , xsec=3.8155  )

lfvh =  Sample( name =   'lfvh',
                tlatex = 'H#rightarrow#tau#tau (LFV)',
                fill_color   =  1020,
                line_color   =  1020,
                marker_color =  1020,
                daughters    = [
                                 PoPy8_ggH125_taumu, 
                                 PoPy8_VBFH125_taumu,
                                 PoPy8_ggH125_taue,  
                                 PoPy8_VBFH125_taue,
                                ]
                )

PoPy8_ggH125_tautau                               = Sample(  name="PoPy8_ggH125_tautau"    , dsid="341123" , xsec=1.262409959 )
PoPy8_VBFH125_tautau                              = Sample(  name="PoPy8_VBFH125_tautau"   , dsid="341156" , xsec=0.107869976 )

smh  =  Sample( name =   'smh',
                tlatex = 'H#rightarrow#tau#tau (SM)',
                fill_color   =  1031,
                line_color   =  1031,
                marker_color =  1031,
                daughters    = [
                                 PoPy8_ggH125_tautau, 
                                 PoPy8_VBFH125_tautau,
                                ]
                )

# the following samples we have locally but they are not included in the xml
"""
PoPy8_ggH125_WWlvlv_EF_15_5                       = Sample(  name="PoPy8_ggH125_WWlvlv_EF_15_5"      , dsid="341079" , xsec=     )      
PoPy8_VBFH125_WWlvlv_EF_15_5                      = Sample(  name="PoPy8_VBFH125_WWlvlv_EF_15_5"     , dsid="341080" , xsec=     )
PoPy8_ggH125_ttlh_CPodd                           = Sample(  name="PoPy8_ggH125_ttlh_CPodd"          , dsid="341902" , xsec=     )
PoPy8_ggH125_ttlh_mix50                           = Sample(  name="PoPy8_ggH125_ttlh_mix50"          , dsid="341903" , xsec=     )
PoPy8_ggH125_ttlh_unpol                           = Sample(  name="PoPy8_ggH125_ttlh_unpol"          , dsid="341904" , xsec=     )
PoPy8_VBFH125_ttlh_CPodd                          = Sample(  name="PoPy8_VBFH125_ttlh_CPodd"         , dsid="341908" , xsec=     )
PoPy8_VBFH125_ttlh_mix50                          = Sample(  name="PoPy8_VBFH125_ttlh_mix50"         , dsid="341909" , xsec=     )
PoPy8_VBFH125_ttlh_unpol                          = Sample(  name="PoPy8_VBFH125_ttlh_unpol"         , dsid="341910" , xsec=     )
"""

"""
Sh221_PDF30_Zmumu_MHPT0_70_VBF                    = Sample(  name="Sh221_PDF30_Zmumu_MHPT0_70_VBF"      , dsid="345099" , xsec=   , kfactor=  )
Sh221_PDF30_Zmumu_MHPT70_140_VBF                  = Sample(  name="Sh221_PDF30_Zmumu_MHPT70_140_VBF"    , dsid="345100" , xsec=   , kfactor=  )
Sh221_PDF30_Zee_MHPT0_70_VBF                      = Sample(  name="Sh221_PDF30_Zee_MHPT0_70_VBF"        , dsid="345101" , xsec=   , kfactor=  )
Sh221_PDF30_Zee_MHPT70_140_VBF                    = Sample(  name="Sh221_PDF30_Zee_MHPT70_140_VBF"      , dsid="345102" , xsec=   , kfactor=  )

Sh_llll                                           = Sample(  name="Sh_llll"                   , dsid="361063" , xsec=   , kfactor=  )
Sh_lllvSFMinus                                    = Sample(  name="Sh_lllvSFMinus"            , dsid="361064" , xsec=   , kfactor=  )
Sh_lllvOFMinus                                    = Sample(  name="Sh_lllvOFMinus"            , dsid="361065" , xsec=   , kfactor=  ) 
Sh_lllvSFPlus                                     = Sample(  name="Sh_lllvSFPlus"             , dsid="361066" , xsec=   , kfactor=  )
Sh_lllvOFPlus                                     = Sample(  name="Sh_lllvOFPlus"             , dsid="361067" , xsec=   , kfactor=  )
Sh_llvv                                           = Sample(  name="Sh_llvv"                   , dsid="361068" , xsec=   , kfactor=  )
Sh_WplvWmqq                                       = Sample(  name="Sh_WplvWmqq"               , dsid="361081" , xsec=   , kfactor=  )
Sh_WpqqWmlv                                       = Sample(  name="Sh_WpqqWmlv"               , dsid="361082" , xsec=   , kfactor=  )
Sh_WlvZqq                                         = Sample(  name="Sh_WlvZqq"                 , dsid="361083" , xsec=   , kfactor=  )
Sh_WqqZll                                         = Sample(  name="Sh_WqqZll"                 , dsid="361084" , xsec=   , kfactor=  )
Sh_ZqqZll                                         = Sample(  name="Sh_ZqqZll"                 , dsid="361086" , xsec=   , kfactor=  )
Sh_lvvv                                           = Sample(  name="Sh_lvvv"                   , dsid="361088" , xsec=   , kfactor=  )
Sh_vvvv                                           = Sample(  name="Sh_vvvv"                   , dsid="361089" , xsec=   , kfactor=  )
Sh_WqqZvv_SHv21_improved                          = Sample(  name="Sh_WqqZvv_SHv21_improved"  , dsid="361095" , xsec=   , kfactor=  )
Sh_ZqqZvv_SHv21_improved                          = Sample(  name="Sh_ZqqZvv_SHv21_improved"  , dsid="361097" , xsec=   , kfactor=  )
"""

"""
Sh221_PDF30_Ztt_MHPT0_70_CVetoBVeto               = Sample(  name="Sh221_PDF30_Ztt_MHPT0_70_CVetoBVeto"     , dsid="364128" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT0_70_CFiltBVet                = Sample(  name="Sh221_PDF30_Ztt_MHPT0_70_CFiltBVet"      , dsid="364129" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT0_70_BFilter                  = Sample(  name="Sh221_PDF30_Ztt_MHPT0_70_BFilter"        , dsid="364130" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT70_140_CVetoBVeto             = Sample(  name="Sh221_PDF30_Ztt_MHPT70_140_CVetoBVeto"   , dsid="364131" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT70_140_CFiltBVet              = Sample(  name="Sh221_PDF30_Ztt_MHPT70_140_CFiltBVet"    , dsid="364132" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT70_140_BFilter                = Sample(  name="Sh221_PDF30_Ztt_MHPT70_140_BFilter"      , dsid="364133" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT140_280_CVetoBVeto            = Sample(  name="Sh221_PDF30_Ztt_MHPT140_280_CVetoBVeto"  , dsid="364134" , xsec=   , kfactor=  )
Sh221_PDF30_Ztt_MHPT140_280_CFiltBVet             = Sample(  name="Sh221_PDF30_Ztt_MHPT140_280_CFiltBVet"   , dsid="364135" , xsec=   , kfactor=  ) 
Sh221_PDF30_Ztt_MHPT140_280_BFilter               = Sample(  name="Sh221_PDF30_Ztt_MHPT140_280_BFilter"     , dsid="364136" , xsec=   , kfactor=  )
"""

"""
PoPy8_A14_ttb_nonallh                             = Sample(  name="PoPy8_A14_ttb_nonallh"                  , dsid="410500" , xsec=   , kfactor=  )
PoPy_P2012radHi_ttb_down_nonallh                  = Sample(  name="PoPy_P2012radHi_ttb_down_nonallh"       , dsid="410001" , xsec=   , kfactor=  )
PoPy_P2012radLo_ttb_up_nonallh                    = Sample(  name="PoPy_P2012radLo_ttb_up_nonallh"         , dsid="410002" , xsec=   , kfactor=  )
PowhegHerwigppEvtGen_UEEE5_ttb_nonallh            = Sample(  name="PowhegHerwigppEvtGen_UEEE5_ttb_nonallh" , dsid="410004" , xsec=   , kfactor=  )
"""

all_data = data.daughters

all_mc = []
#all_mc += Wtaunu.daughters
#all_mc += Wlepnu.daughters
#all_mc += Zleplep.daughters
#all_mc += Ztautau.daughters
#all_mc += top.daughters
all_mc += lfvh.daughters

# EOF
