# encoding: utf-8
'''
systematics.py
description:
'''
## modules

# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------
class Systematic(object):
    '''
    class to hold info about systematics 
    '''
    #____________________________________________________________
    def __init__(self,
            name,
            title=None,
            var_up=None,
            var_dn=None,
            flat_err=None,
            ):
        self.name = name
        if not title: title = name
        self.title = title
        self.var_up=var_up
        self.var_dn=var_dn
        self.flat_err=flat_err 
        assert (self.var_up and self.var_dn) or self.flat_err!=None, 'Must provide either up and dn vars or a flat err!'


sys_dict = {}

# just an example

#['METResoPara', 'METResoPerp', 'MUID_DN', 'MUID_UP', 'MUMS_DN', 'MUMS_UP', 'MUSCALE_DN', 'MUSCALE_UP', 'TAUSF_SYS_DN', 'TAUSF_SYS_UP', 'TAUSF_STAT_UP', 'TAUSF_STAT_DN', 'MUSF_SYS_DN', 'MUSF_SYS_UP', 'MUSF_STAT_UP', 'MUSF_STAT_DN', 'METSCALE_DN', 'METSCALE_UP']


MUID = sys_dict['MUID'] = Systematic(
        'MUID',
        var_up='MUID_UP', #name of submit hist output
        var_dn='MUID_DN'
        )

MUMS = sys_dict['MUMS'] = Systematic(
        'MUMS',
        var_up='MUMS_UP', #name of submit hist output
        var_dn='MUMS_DN'
        )

MUSCALE = sys_dict['MUSCALE'] = Systematic(
        'MUSCALE',
        var_up='MUSCALE_UP', #name of submit hist output
        var_dn='MUSCALE_DN'
        )

METSCALE = sys_dict['METSCALE'] = Systematic(
        'METSCALE',
        var_up='METSCALE_UP', #name of submit hist output
        var_dn='METSCALE_DN'
        )

TAUSF_SYS = sys_dict['TAUSF_SYS'] = Systematic(
        'TAUSF_SYS',
        var_up='TAUSF_SYS_UP', #name of submit hist output
        var_dn='TAUSF_SYS_DN'
        )

TAUSF_STAT = sys_dict['TAUSF_STAT'] = Systematic(
        'TAUSF_STAT',
        var_up='TAUSF_STAT_UP', #name of submit hist output
        var_dn='TAUSF_STAT_DN'
        )

MUSF_SYS = sys_dict['MUSF_SYS'] = Systematic(
        'MUSF_SYS',
        var_up='MUSF_SYS_UP', #name of submit hist output
        var_dn='MUSF_SYS_DN'
        )

MUSF_STAT = sys_dict['MUSF_STAT'] = Systematic(
        'MUSF_STAT',
        var_up='MUSF_STAT_UP', #name of submit hist output
        var_dn='MUSF_STAT_DN'
        )

PILEUP = sys_dict['PILEUP'] = Systematic(
        'PILEUP',    
        var_up='PILEUP_UP',
	var_dn='PILEUP_DN',
        )

# -----------------------------------
# A whole bunch of RQCD uncertainties
# -----------------------------------

# track inclusive

RQCD_AntiIsoCR_lowPT = sys_dict['RQCD_AntiIsoCR_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0656871218669,
        )

RQCD_AntiIsoCR_highPT = sys_dict['RQCD_AntiIsoCR_highPT'] = Systematic(
        'RQCD_AntiIsoCR_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0838079739626,
        )

RQCD_AntiIsoCR_25med_lowPT = sys_dict['RQCD_AntiIsoCR_25med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0576241134752,
        )

RQCD_AntiIsoCR_25med_highPT = sys_dict['RQCD_AntiIsoCR_25med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.087929656275,
        )

RQCD_AntiIsoCR_35med_lowPT = sys_dict['RQCD_AntiIsoCR_35med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.142060085837,  
        )

RQCD_AntiIsoCR_35med_highPT = sys_dict['RQCD_AntiIsoCR_35med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0496368038741,  
        )

# REDO
RQCD_AntiIsoCR_50L1TAU12med_lowPT = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_highPT = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_80med_lowPT = sys_dict['RQCD_AntiIsoCR_80med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_80med_highPT = sys_dict['RQCD_AntiIsoCR_80med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_125med_lowPT = sys_dict['RQCD_AntiIsoCR_125med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_125med_highPT = sys_dict['RQCD_AntiIsoCR_125med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_160med_lowPT = sys_dict['RQCD_AntiIsoCR_160med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_160med_highPT = sys_dict['RQCD_AntiIsoCR_160med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_L1TAU12IMmed_lowPT = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_L1TAU12IMmed_highPT = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_highPT'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# 1-prong

RQCD_AntiIsoCR_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0621669626998,  
        )

RQCD_AntiIsoCR_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0503384094755,  
        )

RQCD_AntiIsoCR_25med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.059620596206,  
        )

RQCD_AntiIsoCR_25med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0520570948783,  
        )

RQCD_AntiIsoCR_35med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.400884955752,  
        )

RQCD_AntiIsoCR_35med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0533165407221,  
        )


RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.447655398037,  
        )

RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0721077654517,  
        )

RQCD_AntiIsoCR_80med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.653482373173,  
        )

RQCD_AntiIsoCR_80med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0768272425249,  
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_125med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_125med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_125med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_125med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_160med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_160med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_160med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_160med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0661896243292,  
        )

RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0518707482993,  
        )

RQCD_AntiIsoCR_tracktwo_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_tracktwo_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_tracktwo_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0698496905393,  
        )

RQCD_AntiIsoCR_tracktwo_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_tracktwo_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_tracktwo_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0497890295359,  
        )


RQCD_AntiIsoCR_ptonly_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_ptonly_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_ptonly_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0633363068689,  
        )

RQCD_AntiIsoCR_ptonly_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_ptonly_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_ptonly_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0391156462585,  
        )


# 3-prong

RQCD_AntiIsoCR_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0989541432019,  
        )

RQCD_AntiIsoCR_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.212100139082,  
        )

RQCD_AntiIsoCR_25med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.151671974522,  
        )

RQCD_AntiIsoCR_25med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.24857324033,  
        )

RQCD_AntiIsoCR_35med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.448942377826,  
        )
RQCD_AntiIsoCR_35med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.212546816479,  
        )


RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.215750915751,  
        )

RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.241066020594,  
        )


RQCD_AntiIsoCR_80med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.711574952562,  
        )

RQCD_AntiIsoCR_80med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.235807860262,  
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_125med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_125med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_125med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_125med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )

# REDO
RQCD_AntiIsoCR_160med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_160med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )
# REDO
RQCD_AntiIsoCR_160med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_160med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05,  
        )


RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0789049919485,  
        )

RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.216747070986,  
        )


RQCD_AntiIsoCR_ptonly_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_ptonly_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_ptonly_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0218270008084,  
        )

RQCD_AntiIsoCR_ptonly_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_ptonly_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_ptonly_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0382231404959,  
        )


RQCD_AntiIsoCR_tracktwo_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_tracktwo_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_tracktwo_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0691318327974,  
        )

RQCD_AntiIsoCR_tracktwo_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_tracktwo_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_tracktwo_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.223310810811,  
        )



fw_lowPT_incl = sys_dict['fw_lowPT_incl'] = Systematic(
	'fw_lowPT_incl','$\\sigma_{FW}$',
	flat_err=1.1101773016e-05,
	)

fw_highPT_incl = sys_dict['fw_highPT_incl'] = Systematic(
        'fw_highPT_incl','$\\sigma_{FW}$',
        flat_err=0.000106105027948,
        )

fw_lowPT_25med = sys_dict['fw_lowPT_25med'] = Systematic(
        'fw_lowPT_25med','$\\sigma_{FW}$',
        flat_err=1.1101773016e-05,
        )

fw_highPT_25med = sys_dict['fw_highPT_25med'] = Systematic(
        'fw_highPT_25med','$\\sigma_{FW}$',
        flat_err=0.000106105027948,
	)

# 1 Prong

fw_lowPT_1Track = sys_dict['fw_lowPT_1Track'] = Systematic(
        'fw_lowPT_1Track','$\\sigma_{FW}$',
        flat_err=1.4713734958e-05,
        )

fw_highPT_1Track = sys_dict['fw_highPT_1Track'] = Systematic(
        'fw_highPT_1Track','$\\sigma_{FW}$',
        flat_err=0.000158624487295,
	)

fw_lowPT_1Track_25med = sys_dict['fw_lowPT_1Track_25med'] = Systematic(
        'fw_lowPT_1Track_25med','$\\sigma_{FW}$',
        flat_err=2.74324927735e-05,
        )

fw_highPT_1Track_25med = sys_dict['fw_highPT_1Track_25med'] = Systematic(
        'fw_highPT_1Track_25med','$\\sigma_{FW}$',
        flat_err=0.000208131974528,
	)

fw_lowPT_1Track_35med = sys_dict['fw_lowPT_1Track_35med'] = Systematic(
        'fw_lowPT_1Track_35med','$\\sigma_{FW}$',
        flat_err=0.168196667677,
        )

fw_highPT_1Track_35med = sys_dict['fw_highPT_1Track_35med'] = Systematic(
        'fw_highPT_1Track_35med','$\\sigma_{FW}$',
        flat_err=0.000357164533668,
	)

fw_lowPT_1Track_50L1TAU12med = sys_dict['fw_lowPT_1Track_50L1TAU12med'] = Systematic(
        'fw_lowPT_1Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.12248656689,
        )

fw_highPT_1Track_50L1TAU12med = sys_dict['fw_highPT_1Track_50L1TAU12med'] = Systematic(
        'fw_highPT_1Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0159231651728,
	)

fw_highPT_1Track_80med = sys_dict['fw_highPT_1Track_80med'] = Systematic(
        'fw_highPT_1Track_80med','$\\sigma_{FW}$',
        flat_err=0.0,
	)


fw_lowPT_1Track_80med = sys_dict['fw_lowPT_1Track_80med'] = Systematic(
        'fw_lowPT_1Track_80med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_1Track_80L1TAU60med = sys_dict['fw_highPT_1Track_80L1TAU60med'] = Systematic(
        'fw_highPT_1Track_80L1TAU60med','$\\sigma_{FW}$',
        flat_err=0.0,
	)


fw_lowPT_1Track_80L1TAU60med = sys_dict['fw_lowPT_1Track_80L1TAU60med'] = Systematic(
        'fw_lowPT_1Track_80L1TAU60med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_1Track_125med = sys_dict['fw_highPT_1Track_125med'] = Systematic(
        'fw_highPT_1Track_125med','$\\sigma_{FW}$',
        flat_err=0.0,
	)


fw_lowPT_1Track_125med = sys_dict['fw_lowPT_1Track_125med'] = Systematic(
        'fw_lowPT_1Track_125med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_lowPT_1Track_160med = sys_dict['fw_lowPT_1Track_160med'] = Systematic(
        'fw_lowPT_1Track_160med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_1Track_160med = sys_dict['fw_highPT_1Track_160med'] = Systematic(
        'fw_highPT_1Track_160med','$\\sigma_{FW}$',
        flat_err=0.0,
	)

fw_lowPT_1Track_L1TAU12IMmed = sys_dict['fw_lowPT_1Track_L1TAU12IMmed'] = Systematic(
        'fw_lowPT_1Track_L1TAU12IMmed','$\\sigma_{FW}$',
        flat_err=.08744756736e-05,
        )

fw_highPT_1Track_L1TAU12IMmed = sys_dict['fw_highPT_1Track_L1TAU12IMmed'] = Systematic(
        'fw_highPT_1Track_L1TAU12IMmed','$\\sigma_{FW}$',
        flat_err=0.000186663913639,
	)

fw_lowPT_1Track_ptonly = sys_dict['fw_lowPT_1Track_ptonly'] = Systematic(
        'fw_lowPT_1Track_ptonly','$\\sigma_{FW}$',
        flat_err=2.50868646942e-05,
        )

fw_highPT_1Track_ptonly = sys_dict['fw_highPT_1Track_ptonly'] = Systematic(
        'fw_highPT_1Track_ptonly','$\\sigma_{FW}$',
        flat_err=0.000186585595245,
	)

fw_lowPT_1Track_tracktwo = sys_dict['fw_lowPT_1Track_tracktwo'] = Systematic(
        'fw_lowPT_1Track_tracktwo','$\\sigma_{FW}$',
        flat_err=2.6386725894e-05,
        )

fw_highPT_1Track_tracktwo = sys_dict['fw_highPT_1Track_tracktwo'] = Systematic(
        'fw_highPT_1Track_tracktwo','$\\sigma_{FW}$',
        flat_err=0.000204666591424,
	)




#3 Prong

fw_lowPT_3Track = sys_dict['fw_lowPT_3Track'] = Systematic(
        'fw_lowPT_3Track','$\\sigma_{FW}$',
        flat_err=0.000163054411212,
        )

fw_highPT_3Track = sys_dict['fw_highPT_3Track'] = Systematic(
        'fw_highPT_3Track','$\\sigma_{FW}$',
        flat_err=0.00100907251131,
	)

fw_lowPT_3Track_25med = sys_dict['fw_lowPT_3Track_25med'] = Systematic(
        'fw_lowPT_3Track_25med','$\\sigma_{FW}$',
        flat_err=0.0013912018276,
        )

fw_highPT_3Track_25med = sys_dict['fw_highPT_3Track_25med'] = Systematic(
        'fw_highPT_3Track_25med','$\\sigma_{FW}$',
        flat_err=0.00217242336587,
        )

fw_lowPT_3Track_35med = sys_dict['fw_lowPT_3Track_35med'] = Systematic(
        'fw_lowPT_3Track_35med','$\\sigma_{FW}$',
        flat_err=0,
        )

fw_highPT_3Track_35med = sys_dict['fw_highPT_3Track_35med'] = Systematic(
        'fw_highPT_3Track_35med','$\\sigma_{FW}$',
        flat_err=0.0345997035183,
        )

fw_lowPT_3Track_50L1TAU12med = sys_dict['fw_lowPT_3Track_50L1TAU12med'] = Systematic(
        'fw_lowPT_3Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_50L1TAU12med = sys_dict['fw_highPT_3Track_50L1TAU12med'] = Systematic(
        'fw_highPT_3Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0963087604162,
        )


fw_lowPT_3Track_80med = sys_dict['fw_lowPT_3Track_80med'] = Systematic(
        'fw_lowPT_3Track_80med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_80med = sys_dict['fw_highPT_3Track_80med'] = Systematic(
        'fw_highPT_3Track_80med','$\\sigma_{FW}$',
        flat_err=0.0,
        )


fw_lowPT_3Track_80L1TAU60med = sys_dict['fw_lowPT_3Track_80L1TAU60med'] = Systematic(
        'fw_lowPT_3Track_80L1TAU60med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_80L1TAU60med = sys_dict['fw_highPT_3Track_80L1TAU60med'] = Systematic(
        'fw_highPT_3Track_80L1TAU60med','$\\sigma_{FW}$',
        flat_err=0.0,
        )


fw_lowPT_3Track_125med = sys_dict['fw_lowPT_3Track_125med'] = Systematic(
        'fw_lowPT_3Track_125med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_125med = sys_dict['fw_highPT_3Track_125med'] = Systematic(
        'fw_highPT_3Track_125med','$\\sigma_{FW}$',
        flat_err=0.0,
        )


fw_lowPT_3Track_160med = sys_dict['fw_lowPT_3Track_160med'] = Systematic(
        'fw_lowPT_3Track_160med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_160med = sys_dict['fw_highPT_3Track_160med'] = Systematic(
        'fw_highPT_3Track_160med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_lowPT_3Track_L1TAU12IMmed = sys_dict['fw_lowPT_3Track_L1TAU12IMmed'] = Systematic(
        'fw_lowPT_3Track_L1TAU12IMmed','$\\sigma_{FW}$',
        flat_err=0.000674088790834,
        )

fw_highPT_3Track_L1TAU12IMmed = sys_dict['fw_highPT_3Track_L1TAU12IMmed'] = Systematic(
        'fw_highPT_3Track_L1TAU12IMmed','$\\sigma_{FW}$',
        flat_err=0.00127147460984,
        )

fw_lowPT_3Track_ptonly = sys_dict['fw_lowPT_3Track_ptonly'] = Systematic(
        'fw_lowPT_3Track_ptonly','$\\sigma_{FW}$',
        flat_err=0.000659630651756,
        )

fw_highPT_3Track_ptonly = sys_dict['fw_highPT_3Track_ptonly'] = Systematic(
        'fw_highPT_3Track_ptonly','$\\sigma_{FW}$',
        flat_err=0.00127250351758,
	)

fw_lowPT_3Track_tracktwo = sys_dict['fw_lowPT_3Track_tracktwo'] = Systematic(
        'fw_lowPT_3Track_tracktwo','$\\sigma_{FW}$',
        flat_err=0.000774386773868,
        )

fw_highPT_3Track_tracktwo = sys_dict['fw_highPT_3Track_tracktwo'] = Systematic(
        'fw_highPT_3Track_tracktwo','$\\sigma_{FW}$',
        flat_err=0.00179730544749,
	)


# ------------------#
#	kW
#-------------------#

# 1-prong

# REDO
kW_Tau1Track = sys_dict['kW_Tau1Track'] = Systematic(
        'kW_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_lowPT_Tau1Track = sys_dict['kW_lowPT_Tau1Track'] = Systematic(
        'kW_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_highPT_Tau1Track = sys_dict['kW_highPT_Tau1Track'] = Systematic(
        'kW_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_25med_Tau1Track = sys_dict['kW_25med_Tau1Track'] = Systematic(
        'kW_25med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_25med_lowPT_Tau1Track = sys_dict['kW_25med_lowPT_Tau1Track'] = Systematic(
        'kW_25med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_25med_highPT_Tau1Track = sys_dict['kW_25med_highPT_Tau1Track'] = Systematic(
        'kW_25med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_35med_Tau1Track = sys_dict['kW_35med_Tau1Track'] = Systematic(
        'kW_35med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_35med_lowPT_Tau1Track = sys_dict['kW_35med_lowPT_Tau1Track'] = Systematic(
        'kW_35med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_35med_highPT_Tau1Track = sys_dict['kW_35med_highPT_Tau1Track'] = Systematic(
        'kW_35med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_50L1TAU12med_Tau1Track = sys_dict['kW_50L1TAU12med_Tau1Track'] = Systematic(
        'kW_50L1TAU12med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_50L1TAU12med_lowPT_Tau1Track = sys_dict['kW_50L1TAU12med_lowPT_Tau1Track'] = Systematic(
        'kW_50L1TAU12med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_50L1TAU12med_highPT_Tau1Track = sys_dict['kW_50L1TAU12med_highPT_Tau1Track'] = Systematic(
        'kW_50L1TAU12med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_80med_Tau1Track = sys_dict['kW_80med_Tau1Track'] = Systematic(
        'kW_80med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80med_lowPT_Tau1Track = sys_dict['kW_80med_lowPT_Tau1Track'] = Systematic(
        'kW_80med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80med_highPT_Tau1Track = sys_dict['kW_80med_highPT_Tau1Track'] = Systematic(
        'kW_80med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_80L1TAU60med_Tau1Track = sys_dict['kW_80L1TAU60med_Tau1Track'] = Systematic(
        'kW_80L1TAU60med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80L1TAU60med_lowPT_Tau1Track = sys_dict['kW_80L1TAU60med_lowPT_Tau1Track'] = Systematic(
        'kW_80L1TAU60med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80L1TAU60med_highPT_Tau1Track = sys_dict['kW_80L1TAU60med_highPT_Tau1Track'] = Systematic(
        'kW_80L1TAU60med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_125med_Tau1Track = sys_dict['kW_125med_Tau1Track'] = Systematic(
        'kW_125med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_125med_lowPT_Tau1Track = sys_dict['kW_125med_lowPT_Tau1Track'] = Systematic(
        'kW_125med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_125med_highPT_Tau1Track = sys_dict['kW_125med_highPT_Tau1Track'] = Systematic(
        'kW_125med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_160med_Tau1Track = sys_dict['kW_160med_Tau1Track'] = Systematic(
        'kW_160med_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_160med_lowPT_Tau1Track = sys_dict['kW_160med_lowPT_Tau1Track'] = Systematic(
        'kW_160med_lowPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_160med_highPT_Tau1Track = sys_dict['kW_160med_highPT_Tau1Track'] = Systematic(
        'kW_160med_highPT_Tau1Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# 3-prong

# REDO
kW_Tau3Track = sys_dict['kW_Tau3Track'] = Systematic(
        'kW_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_lowPT_Tau3Track = sys_dict['kW_lowPT_Tau3Track'] = Systematic(
        'kW_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_highPT_Tau3Track = sys_dict['kW_highPT_Tau3Track'] = Systematic(
        'kW_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_25med_Tau3Track = sys_dict['kW_25med_Tau3Track'] = Systematic(
        'kW_25med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_25med_lowPT_Tau3Track = sys_dict['kW_25med_lowPT_Tau3Track'] = Systematic(
        'kW_25med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

kW_25med_highPT_Tau3Track = sys_dict['kW_25med_highPT_Tau3Track'] = Systematic(
        'kW_25med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_35med_Tau3Track = sys_dict['kW_35med_Tau3Track'] = Systematic(
        'kW_35med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_35med_lowPT_Tau3Track = sys_dict['kW_35med_lowPT_Tau3Track'] = Systematic(
        'kW_35med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_35med_highPT_Tau3Track = sys_dict['kW_35med_highPT_Tau3Track'] = Systematic(
        'kW_35med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_50L1TAU12med_Tau3Track = sys_dict['kW_50L1TAU12med_Tau3Track'] = Systematic(
        'kW_50L1TAU12med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_50L1TAU12med_lowPT_Tau3Track = sys_dict['kW_50L1TAU12med_lowPT_Tau3Track'] = Systematic(
        'kW_50L1TAU12med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_50L1TAU12med_highPT_Tau3Track = sys_dict['kW_50L1TAU12med_highPT_Tau3Track'] = Systematic(
        'kW_50L1TAU12med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_80med_Tau3Track = sys_dict['kW_80med_Tau3Track'] = Systematic(
        'kW_80med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80med_lowPT_Tau3Track = sys_dict['kW_80med_lowPT_Tau3Track'] = Systematic(
        'kW_80med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80med_highPT_Tau3Track = sys_dict['kW_80med_highPT_Tau3Track'] = Systematic(
        'kW_80med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_80L1TAU60med_Tau3Track = sys_dict['kW_80L1TAU60med_Tau3Track'] = Systematic(
        'kW_80L1TAU60med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80L1TAU60med_lowPT_Tau3Track = sys_dict['kW_80L1TAU60med_lowPT_Tau3Track'] = Systematic(
        'kW_80L1TAU60med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_80L1TAU60med_highPT_Tau3Track = sys_dict['kW_80L1TAU60med_highPT_Tau3Track'] = Systematic(
        'kW_80L1TAU60med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_125med_Tau3Track = sys_dict['kW_125med_Tau3Track'] = Systematic(
        'kW_125med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_125med_lowPT_Tau3Track = sys_dict['kW_125med_lowPT_Tau3Track'] = Systematic(
        'kW_125med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_125med_highPT_Tau3Track = sys_dict['kW_125med_highPT_Tau3Track'] = Systematic(
        'kW_125med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )

# REDO
kW_160med_Tau3Track = sys_dict['kW_160med_Tau3Track'] = Systematic(
        'kW_160med_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_160med_lowPT_Tau3Track = sys_dict['kW_160med_lowPT_Tau3Track'] = Systematic(
        'kW_160med_lowPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )
# REDO
kW_160med_highPT_Tau3Track = sys_dict['kW_160med_highPT_Tau3Track'] = Systematic(
        'kW_160med_highPT_Tau3Track','$\\sigma_{kW}}$',      
        flat_err=0.0,  
        )



## EOF
