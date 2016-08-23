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
SYS1 = sys_dict['SYS1'] = Systematic(
        'SYS1',
        var_up='SYS1_UP',
        var_dn='SYS1_DN'
        )
SYS2 = sys_dict['SYS2'] = Systematic(
        'SYS2','$\\sigma_{\\rm Wtaunu}$',      
        flat_err=0.05,
        )

# -----------------------------------
# A whole bunch of RQCD uncertainties
# -----------------------------------

# track inclusive

RQCD_AntiIsoCR = sys_dict['RQCD_AntiIsoCR'] = Systematic(
        'RQCD_AntiIsoCR','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0384286934244,
        )

RQCD_AntiIsoCR_lowPT = sys_dict['RQCD_AntiIsoCR_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0521472392638,
        )

RQCD_AntiIsoCR_highPT = sys_dict['RQCD_AntiIsoCR_highPT'] = Systematic(
        'RQCD_AntiIsoCR_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.0424836601307,
        )

RQCD_AntiIsoCR_25med = sys_dict['RQCD_AntiIsoCR_25med'] = Systematic(
        'RQCD_AntiIsoCR_25med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_lowPT = sys_dict['RQCD_AntiIsoCR_25med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_highPT = sys_dict['RQCD_AntiIsoCR_25med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med = sys_dict['RQCD_AntiIsoCR_35med'] = Systematic(
        'RQCD_AntiIsoCR_35med','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_lowPT = sys_dict['RQCD_AntiIsoCR_35med_lowPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_highPT = sys_dict['RQCD_AntiIsoCR_35med_highPT'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

# 1-prong

RQCD_AntiIsoCR_1Track = sys_dict['RQCD_AntiIsoCR_1Track'] = Systematic(
        'RQCD_AntiIsoCR_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_lowPT_1Track = sys_dict['RQCD_AntiIsoCR_lowPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_highPT_1Track = sys_dict['RQCD_AntiIsoCR_highPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_1Track = sys_dict['RQCD_AntiIsoCR_25med_1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_lowPT_1Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_highPT_1Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_1Track = sys_dict['RQCD_AntiIsoCR_35med_1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_lowPT_1Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_highPT_1Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_1Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_1Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )


# 3-prong

RQCD_AntiIsoCR_3Track = sys_dict['RQCD_AntiIsoCR_3Track'] = Systematic(
        'RQCD_AntiIsoCR_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_lowPT_3Track = sys_dict['RQCD_AntiIsoCR_lowPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_lowPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_highPT_3Track = sys_dict['RQCD_AntiIsoCR_highPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_highPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_3Track = sys_dict['RQCD_AntiIsoCR_25med_3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_lowPT_3Track = sys_dict['RQCD_AntiIsoCR_25med_lowPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_lowPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_25med_highPT_3Track = sys_dict['RQCD_AntiIsoCR_25med_highPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_25med_highPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_3Track = sys_dict['RQCD_AntiIsoCR_35med_3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_lowPT_3Track = sys_dict['RQCD_AntiIsoCR_35med_lowPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_lowPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )

RQCD_AntiIsoCR_35med_highPT_3Track = sys_dict['RQCD_AntiIsoCR_35med_highPT_3Track'] = Systematic(
        'RQCD_AntiIsoCR_35med_highPT_3Track','$\\sigma_{R_{\\rm QCD}}$',      
        flat_err=0.05, # some 5% unc.
        )



## EOF
