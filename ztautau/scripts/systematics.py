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

# REDO
RQCD_AntiIsoCR = sys_dict['RQCD_AntiIsoCR'] = Systematic(
        'RQCD_AntiIsoCR','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0384286934244,
        )

RQCD_AntiIsoCR_lowPT = sys_dict['RQCD_AntiIsoCR_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0452946350044,
        )

RQCD_AntiIsoCR_highPT = sys_dict['RQCD_AntiIsoCR_highPT'] = Systematic(
        'RQCD_AntiIsoCR_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0393537696769,
        )

# REDO
RQCD_AntiIsoCR_25med = sys_dict['RQCD_AntiIsoCR_25med'] = Systematic(
        'RQCD_AntiIsoCR_25med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.106746370623,
        )

RQCD_AntiIsoCR_25med_lowPT = sys_dict['RQCD_AntiIsoCR_25med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0602678571429,
        )

RQCD_AntiIsoCR_25med_highPT = sys_dict['RQCD_AntiIsoCR_25med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.047068538398,
        )

# REDO
RQCD_AntiIsoCR_35med = sys_dict['RQCD_AntiIsoCR_35med'] = Systematic(
        'RQCD_AntiIsoCR_35med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_lowPT = sys_dict['RQCD_AntiIsoCR_35med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_highPT = sys_dict['RQCD_AntiIsoCR_35med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_50L1TAU12med = sys_dict['RQCD_AntiIsoCR_50L1TAU12med'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_lowPT = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_highPT = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80med = sys_dict['RQCD_AntiIsoCR_80med'] = Systematic(
        'RQCD_AntiIsoCR_80med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_lowPT = sys_dict['RQCD_AntiIsoCR_80med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_highPT = sys_dict['RQCD_AntiIsoCR_80med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med = sys_dict['RQCD_AntiIsoCR_80L1TAU60med'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_125med = sys_dict['RQCD_AntiIsoCR_125med'] = Systematic(
        'RQCD_AntiIsoCR_125med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_lowPT = sys_dict['RQCD_AntiIsoCR_125med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_highPT = sys_dict['RQCD_AntiIsoCR_125med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_160med = sys_dict['RQCD_AntiIsoCR_160med'] = Systematic(
        'RQCD_AntiIsoCR_160med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_lowPT = sys_dict['RQCD_AntiIsoCR_160med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_highPT = sys_dict['RQCD_AntiIsoCR_160med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# 1-prong

# REDO
RQCD_AntiIsoCR_Tau1Track = sys_dict['RQCD_AntiIsoCR_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0374665477252, # some 5% unc.
        )

RQCD_AntiIsoCR_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0294871794872, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_25med_Tau1Track = sys_dict['RQCD_AntiIsoCR_25med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0524193548387, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0524193548387, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0209044368601, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_35med_Tau1Track = sys_dict['RQCD_AntiIsoCR_35med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_50L1TAU12med_Tau1Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80med_Tau1Track = sys_dict['RQCD_AntiIsoCR_80med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med_Tau1Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_125med_Tau1Track = sys_dict['RQCD_AntiIsoCR_125med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_125med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_125med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_160med_Tau1Track = sys_dict['RQCD_AntiIsoCR_160med_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_lowPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_160med_lowPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_highPT_Tau1Track = sys_dict['RQCD_AntiIsoCR_160med_highPT_Tau1Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT_Tau1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# 3-prong

# REDO
RQCD_AntiIsoCR_Tau3Track = sys_dict['RQCD_AntiIsoCR_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0768251273345, # some 5% unc.
        )

RQCD_AntiIsoCR_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.134164222874, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_25med_Tau3Track = sys_dict['RQCD_AntiIsoCR_25med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.135206321335, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.169737774628, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_Tau3Track = sys_dict['RQCD_AntiIsoCR_35med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_35med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_50L1TAU12med_Tau3Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80med_Tau3Track = sys_dict['RQCD_AntiIsoCR_80med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_80L1TAU60med_Tau3Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_125med_Tau3Track = sys_dict['RQCD_AntiIsoCR_125med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_125med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_125med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_125med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_125med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# REDO
RQCD_AntiIsoCR_160med_Tau3Track = sys_dict['RQCD_AntiIsoCR_160med_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_lowPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_160med_lowPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_lowPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )
# REDO
RQCD_AntiIsoCR_160med_highPT_Tau3Track = sys_dict['RQCD_AntiIsoCR_160med_highPT_Tau3Track'] = Systematic(
        'RQCD_AntiIsoCR_160med_highPT_Tau3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )


#INCL
fw_incl = sys_dict['fw_incl'] = Systematic(
        'fw_incl','$\\sigma_{FW}$',
        flat_err=0.15,
        )

fw_lowPT_incl = sys_dict['fw_lowPT_incl'] = Systematic(
	'fw_lowPT_incl','$\\sigma_{FW}$',
	flat_err=0.15,
	)

fw_highPT_incl = sys_dict['fw_highPT_incl'] = Systematic(
        'fw_highPT_incl','$\\sigma_{FW}$',
        flat_err=0.15,
        )

fw_lowPT_25med = sys_dict['fw_lowPT_25med'] = Systematic(
        'fw_lowPT_25med','$\\sigma_{FW}$',
        flat_err=0.15,
        )

fw_highPT_25med = sys_dict['fw_highPT_25med'] = Systematic(
        'fw_highPT_25med','$\\sigma_{FW}$',
        flat_err=0.15,
	)

# 1 Prong

fw_lowPT_1Track = sys_dict['fw_lowPT_1Track'] = Systematic(
        'fw_lowPT_1Track','$\\sigma_{FW}$',
        flat_err=0.0572,
        )

fw_highPT_1Track = sys_dict['fw_highPT_1Track'] = Systematic(
        'fw_highPT_1Track','$\\sigma_{FW}$',
        flat_err=0.074,
	)

fw_lowPT_1Track_25med = sys_dict['fw_lowPT_1Track_25med'] = Systematic(
        'fw_lowPT_1Track_25med','$\\sigma_{FW}$',
        flat_err=0.058,
        )

fw_highPT_1Track_25med = sys_dict['fw_highPT_1Track_25med'] = Systematic(
        'fw_highPT_1Track_25med','$\\sigma_{FW}$',
        flat_err=0.076,
	)

fw_lowPT_1Track_35med = sys_dict['fw_lowPT_1Track_35med'] = Systematic(
        'fw_lowPT_1Track_35med','$\\sigma_{FW}$',
        flat_err=0.097,
        )

fw_highPT_1Track_35med = sys_dict['fw_highPT_1Track_35med'] = Systematic(
        'fw_highPT_1Track_35med','$\\sigma_{FW}$',
        flat_err=0.097,
	)

fw_lowPT_1Track_50L1TAU12med = sys_dict['fw_lowPT_1Track_50L1TAU12med'] = Systematic(
        'fw_lowPT_1Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0,
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

fw_highPT_1Track_50L1TAU12med = sys_dict['fw_highPT_1Track_50L1TAU12med'] = Systematic(
        'fw_highPT_1Track_50L1TAU12med','$\\sigma_{FW}$',
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



#3 Prong

fw_lowPT_3Track = sys_dict['fw_lowPT_3Track'] = Systematic(
        'fw_lowPT_3Track','$\\sigma_{FW}$',
        flat_err=0.190,
        )

fw_highPT_3Track = sys_dict['fw_highPT_3Track'] = Systematic(
        'fw_highPT_3Track','$\\sigma_{FW}$',
        flat_err=0.213,
	)

fw_lowPT_3Track_25med = sys_dict['fw_lowPT_3Track_25med'] = Systematic(
        'fw_lowPT_3Track_25med','$\\sigma_{FW}$',
        flat_err=0.289,
        )

fw_highPT_3Track_25med = sys_dict['fw_highPT_3Track_25med'] = Systematic(
        'fw_highPT_3Track_25med','$\\sigma_{FW}$',
        flat_err=0.21,
        )

fw_lowPT_3Track_35med = sys_dict['fw_lowPT_3Track_35med'] = Systematic(
        'fw_lowPT_3Track_35med','$\\sigma_{FW}$',
        flat_err=0.15,
        )

fw_highPT_3Track_35med = sys_dict['fw_highPT_3Track_35med'] = Systematic(
        'fw_highPT_3Track_35med','$\\sigma_{FW}$',
        flat_err=0.15,
        )

fw_lowPT_3Track_50L1TAU12med = sys_dict['fw_lowPT_3Track_50L1TAU12med'] = Systematic(
        'fw_lowPT_3Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0,
        )

fw_highPT_3Track_50L1TAU12med = sys_dict['fw_highPT_3Track_50L1TAU12med'] = Systematic(
        'fw_highPT_3Track_50L1TAU12med','$\\sigma_{FW}$',
        flat_err=0.0,
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



## EOF
