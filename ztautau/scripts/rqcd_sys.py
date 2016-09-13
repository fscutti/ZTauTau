# incl no trig

from math import *

print "INCLUSIVE"
print ""
print "*******************"
print ""

#------------------------------#
#        NO TRIGGER
#------------------------------#

rqcd_i_val = 1.171

rqcd_i_topo = [1.147, 1.144, 1.136, 1.132, 1.133, 1.133, 1.132, 1.127, 1.119, 1.112, 1.118, 1.114, 1.118, 1.113, 1.116, 1.116, 1.113, 1.101, 1.092, 1.088, 1.085, 1.081, 1.076, 1.077, 1.081, 1.069, 1.066, 1.057, 1.058, 1.062]

min_rqcd_i_topo = 2
max_rqcd_i_topo = 0

for i in range(len(rqcd_i_topo)):
	if rqcd_i_topo[i] < min_rqcd_i_topo:
		min_rqcd_i_topo = rqcd_i_topo[i]
	if rqcd_i_topo[i] > max_rqcd_i_topo:
		max_rqcd_i_topo = rqcd_i_topo[i]

rqcd_i_ptvar = [1.135, 1.135, 1.134, 1.134, 1.136, 1.135, 1.133, 1.134, 1.134, 1.131, 1.130, 1.125, 1.125, 1.124, 1.123, 1.125, 1.123, 1.125, 1.128, 1.128, 1.131, 1.131, 1.133, 1.133, 1.135, 1.137, 1.135, 1.139, 1.141]

min_rqcd_i_ptvar = 2
max_rqcd_i_ptvar = 0

for i in range(len(rqcd_i_ptvar)):
        if rqcd_i_ptvar[i] < min_rqcd_i_ptvar:
                min_rqcd_i_ptvar = rqcd_i_ptvar[i]
        if rqcd_i_ptvar[i] > max_rqcd_i_ptvar:
                max_rqcd_i_ptvar = rqcd_i_ptvar[i]

print "TOPO_no_trig: sys (percentage) =", ((max_rqcd_i_topo - min_rqcd_i_topo)/2)/rqcd_i_val
print "PTVAR_no_trig: sys (percentage) =", ((max_rqcd_i_ptvar - min_rqcd_i_ptvar)/2)/rqcd_i_val
print "TOPO_no_trig: sys =", ((max_rqcd_i_topo - min_rqcd_i_topo)/2)
print "PTVAR_no_trig: sys =", ((max_rqcd_i_ptvar - min_rqcd_i_ptvar)/2)
print ""
print "---> total sys no trig incl =", max( ((max_rqcd_i_topo - min_rqcd_i_topo)/2), ((max_rqcd_i_ptvar - min_rqcd_i_ptvar)/2) )
print "---> total sys no trig incl (percentage) =", max( ((max_rqcd_i_topo - min_rqcd_i_topo)/2)/rqcd_i_val, ((max_rqcd_i_ptvar - min_rqcd_i_ptvar)/2)/rqcd_i_val )
print ""


# LOW VS HIGH PT
rqcd_i_low_val = 1.141
rqcd_i_high_val = 1.224

rqcd_i_low_topo = [1.127, 1.121, 1.114, 1.108, 1.106, 1.099, 1.103, 1.098, 1.088, 1.080, 1.084, 1.079, 1.084, 1.080, 1.078, 1.072, 1.065, 1.057, 1.046, 1.039, 1.033, 1.027, 1.030, 1.022, 1.032, 1.028, 1.018, 1.019, 1.008, 1.016, 1.013]
rqcd_i_high_topo = [1.183, 1.183, 1.176, 1.176, 1.182, 1.190, 1.185, 1.098, 1.179, 1.175, 1.169, 1.181, 1.178, 1.180, 1.172, 1.185, 1.195, 1.202, 1.182, 1.176, 1.177, 1.181, 1.191, 1.173, 1.174, 1.159, 1.175, 1.159, 1.146, 1.140, 1.128, 1.143]

diff_rqcd_i_low_val_topo = 0
diff_rqcd_i_high_val_topo = 0

min_rqcd_i_low_topo = 2
max_rqcd_i_low_topo = 0
min_rqcd_i_high_topo = 2
max_rqcd_i_high_topo = 0

for i in range(len(rqcd_i_low_topo)):
	if rqcd_i_low_topo[i]<min_rqcd_i_low_topo:
		min_rqcd_i_low_topo = rqcd_i_low_topo[i]
	if rqcd_i_low_topo[i]>max_rqcd_i_low_topo:
		max_rqcd_i_low_topo = rqcd_i_low_topo[i]


for i in range(len(rqcd_i_high_topo)):
        if rqcd_i_high_topo[i]<min_rqcd_i_high_topo:
                min_rqcd_i_high_topo = rqcd_i_high_topo[i]
        if rqcd_i_high_topo[i]>max_rqcd_i_high_topo:
                max_rqcd_i_high_topo = rqcd_i_high_topo[i]

print "TOPO_no_trig: sys_i_low =", ((max_rqcd_i_low_topo - min_rqcd_i_low_topo)/2)
print "TOPO_no_trig: sys_i_high =", ((max_rqcd_i_high_topo - min_rqcd_i_high_topo)/2)
print "TOPO_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_topo - min_rqcd_i_low_topo)/2)/rqcd_i_low_val
print "TOPO_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_topo - min_rqcd_i_high_topo)/2)/rqcd_i_high_val

rqcd_i_low_ptvar = [1.103, 1.103, 1.102, 1.103, 1.104, 1.103, 1.100, 1.100, 1.103, 1.097, 1.097, 1.094, 1.094, 1.092, 1.090, 1.093, 1.093, 1.094,  1.096, 1.095, 1.100, 1.099, 1.101, 1.099, 1.103, 1.105, 1.105, 1.108, 1.106, 1.109, 1.108]
rqcd_i_high_ptvar = [1.187, 1.188, 1.188, 1.187, 1.187, 1.187, 1.189, 1.188, 1.185, 1.185, 1.183, 1.177, 1.177, 1.178, 1.176, 1.175, 1.171, 1.176, 1.181, 1.179, 1.182, 1.183, 1.184, 1.186, 1.186, 1.188, 1.183, 1.188, 1.187, 1.187, 1.193]

min_rqcd_i_low_ptvar = 2
max_rqcd_i_low_ptvar = 0
min_rqcd_i_high_ptvar = 2
max_rqcd_i_high_ptvar = 0

for i in range(len(rqcd_i_low_ptvar)):
        if rqcd_i_low_ptvar[i]<min_rqcd_i_low_ptvar:
                min_rqcd_i_low_ptvar = rqcd_i_low_ptvar[i]
        if rqcd_i_low_ptvar[i]>max_rqcd_i_low_ptvar:
                max_rqcd_i_low_ptvar = rqcd_i_low_ptvar[i]


for i in range(len(rqcd_i_high_ptvar)):
        if rqcd_i_high_ptvar[i]<min_rqcd_i_high_ptvar:
                min_rqcd_i_high_ptvar = rqcd_i_high_ptvar[i]
        if rqcd_i_high_ptvar[i]>max_rqcd_i_high_ptvar:
                max_rqcd_i_high_ptvar = rqcd_i_high_ptvar[i]

print "PTVAR_no_trig: sys_i_low =", ((max_rqcd_i_low_ptvar - min_rqcd_i_low_ptvar)/2)
print "PTVAR_no_trig: sys_i_high =", ((max_rqcd_i_high_ptvar - min_rqcd_i_high_ptvar)/2)
print "PTVAR_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar - min_rqcd_i_low_ptvar)/2)/rqcd_i_low_val
print "PTVAR_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar - min_rqcd_i_high_ptvar)/2)/rqcd_i_high_val

print ""
print "---> total sys no trig low pt =", max( ((max_rqcd_i_low_ptvar - min_rqcd_i_low_ptvar)/2), ((max_rqcd_i_low_topo - min_rqcd_i_low_topo)/2))
print "---> total sys no trig high pt =", max( ((max_rqcd_i_high_ptvar - min_rqcd_i_high_ptvar)/2), ((max_rqcd_i_high_topo - min_rqcd_i_high_topo)/2))
print ""
print "---> total sys no trig low pt (percentage) =", max( ((max_rqcd_i_low_ptvar - min_rqcd_i_low_ptvar)/2)/rqcd_i_low_val, ((max_rqcd_i_low_topo - min_rqcd_i_low_topo)/2)/rqcd_i_low_val ) 
print "---> total sys no trig high pt (percentage) =", max( ((max_rqcd_i_high_ptvar - min_rqcd_i_high_ptvar)/2)/rqcd_i_high_val, ((max_rqcd_i_high_topo - min_rqcd_i_high_topo)/2)/rqcd_i_high_val )
print ""
print "***********"
print ""

# ----------------------------------- #
#     	   25 med trigger
# ------------------------------------#

rqcd_i_val_25med = 1.178 

rqcd_i_topo_25med = [1.154, 1.151, 1.142, 1.133, 1.132, 1.134, 1.133, 1.130, 1.115, 1.117, 1.115, 1.120, 1.108, 1.112, 1.108, 1.106, 1.090, 1.080, 1.070, 1.064, 1.066, 1.066, 1.074, 1.081, 1.071, 1.068, 1.052, 1.055, 1.065]

min_rqcd_i_topo_25med = 2
max_rqcd_i_topo_25med = 0

for i in range(len(rqcd_i_topo_25med)):
	if rqcd_i_topo_25med[i] < min_rqcd_i_topo_25med:
		min_rqcd_i_topo_25med = rqcd_i_topo_25med[i]
	if rqcd_i_topo_25med[i] > max_rqcd_i_topo_25med:
		max_rqcd_i_topo_25med = rqcd_i_topo_25med[i]

rqcd_i_ptvar_25med = [1.143, 1.141, 1.140, 1.142, 1.145, 1.143, 1.143, 1.139, 1.138, 1.132, 1.132, 1.130, 1.130, 1.132, 1.131, 1.132, 1.135, 1.134, 1.134, 1.137, 1.38, 1.37, 1.34, 1.138, 1.135, 1.136, 1.138]     

min_rqcd_i_ptvar_25med = 2
max_rqcd_i_ptvar_25med = 0

for i in range(len(rqcd_i_ptvar_25med)):
        if rqcd_i_ptvar_25med[i] < min_rqcd_i_ptvar_25med:
                min_rqcd_i_ptvar_25med = rqcd_i_ptvar_25med[i]
        if rqcd_i_ptvar_25med[i] > max_rqcd_i_ptvar_25med:
                max_rqcd_i_ptvar_25med = rqcd_i_ptvar_25med[i]

print "TOPO_25med: sys (percentage) =", ((max_rqcd_i_topo_25med - min_rqcd_i_topo_25med)/2)/rqcd_i_val_25med
print "PTVAR_25med: sys (percentage) =", ((max_rqcd_i_ptvar_25med - min_rqcd_i_ptvar_25med)/2)/rqcd_i_val_25med
print "TOPO_25med: sys =", ((max_rqcd_i_topo_25med - min_rqcd_i_topo_25med)/2)
print "PTVAR_25med: sys =", ((max_rqcd_i_ptvar_25med - min_rqcd_i_ptvar_25med)/2)
print ""
print "---> total sys 25med incl =", max( ((max_rqcd_i_topo_25med - min_rqcd_i_topo_25med)/2), ((max_rqcd_i_ptvar_25med - min_rqcd_i_ptvar_25med)/2))
print ""
print "---> total sys 25med incl (percentage) =", max( ((max_rqcd_i_topo_25med - min_rqcd_i_topo_25med)/2)/rqcd_i_val_25med, ((max_rqcd_i_ptvar_25med - min_rqcd_i_ptvar_25med)/2)/rqcd_i_val_25med )
print ""

# LOW VS HIGH PT
rqcd_i_low_25med_val = 1.131 
rqcd_i_high_25med_val = 1.228

rqcd_i_low_topo_25med = [1.125, 1.115, 1.110, 1.096, 1.091, 1.085, 1.086, 1.084, 1.073, 1.062, 1.062, 1.061, 1.065, 1.059, 1.055, 1.044, 1.040, 1.022, 1.007, 0.990, 0.979, 0.981, 0.986, 0.981, 1.001, 1.004, 0.995, 1.000, 0.987, 0.989, 1.000]
rqcd_i_high_topo_25med = [1.179, 1.184, 1.172, 1.171, 1.176, 1.186, 1.181, 1.180, 1.177, 1.175, 1.180, 1.176, 1.183, 1.161, 1.176, 1.180, 1.180, 1.167, 1.165, 1.164, 1.165, 1.167, 1.157, 1.164, 1.149, 1.157, 1.145, 1.130, 1.112, 1.114, 1.126]

min_rqcd_i_low_topo_25med = 2
max_rqcd_i_low_topo_25med = 0
min_rqcd_i_high_topo_25med = 2
max_rqcd_i_high_topo_25med = 0

for i in range(len(rqcd_i_low_topo_25med)):
	if rqcd_i_low_topo_25med[i]<min_rqcd_i_low_topo_25med:
		min_rqcd_i_low_topo_25med = rqcd_i_low_topo_25med[i]
	if rqcd_i_low_topo_25med[i]>max_rqcd_i_low_topo_25med:
		max_rqcd_i_low_topo_25med = rqcd_i_low_topo_25med[i]


for i in range(len(rqcd_i_high_topo_25med)):
        if rqcd_i_high_topo_25med[i]<min_rqcd_i_high_topo_25med:
                min_rqcd_i_high_topo_25med = rqcd_i_high_topo_25med[i]
        if rqcd_i_high_topo_25med[i]>max_rqcd_i_high_topo_25med:
                max_rqcd_i_high_topo_25med = rqcd_i_high_topo_25med[i]

print "TOPO_25med: sys_i_low =", ((max_rqcd_i_low_topo_25med - min_rqcd_i_low_topo_25med)/2)
print "TOPO_25med: sys_i_high =", ((max_rqcd_i_high_topo_25med - min_rqcd_i_high_topo_25med)/2)
print "TOPO_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_25med - min_rqcd_i_low_topo_25med)/2)/rqcd_i_low_25med_val
print "TOPO_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_25med - min_rqcd_i_high_topo_25med)/2)/rqcd_i_high_25med_val

rqcd_i_low_ptvar_25med = [1.096, 1.095, 1.091, 1.093, 1.098, 1.096, 1.093, 1.098, 1.098, 1.090, 1.085, 1.084, 1.080, 1.079, 1.083, 1.085, 1.085, 1.085, 1.082, 1.087, 1.085, 1.088, 1.087, 1.090, 1.089, 1.088, 1.090, 1.085, 1.087, 1.086]
rqcd_i_high_ptvar_25med = [1.181, 1.180, 1.181, 1.183, 1.184, 1.183, 1.185, 1.183, 1.178, 1.176, 1.168, 1.170, 1.170, 1.170, 1.169, 1.164, 1.168, 1.174, 1.170, 1.171, 1.170 ,1.167, 1.174, 1.171, 1.170, 1.168, 1.173, 1.170, 1.170, 1.177]

min_rqcd_i_low_ptvar_25med = 2
max_rqcd_i_low_ptvar_25med = 0
min_rqcd_i_high_ptvar_25med = 2
max_rqcd_i_high_ptvar_25med = 0

for i in range(len(rqcd_i_low_ptvar_25med)):
        if rqcd_i_low_ptvar_25med[i]<min_rqcd_i_low_ptvar_25med:
                min_rqcd_i_low_ptvar_25med = rqcd_i_low_ptvar_25med[i]
        if rqcd_i_low_ptvar_25med[i]>max_rqcd_i_low_ptvar_25med:
                max_rqcd_i_low_ptvar_25med = rqcd_i_low_ptvar_25med[i]


for i in range(len(rqcd_i_high_ptvar_25med)):
        if rqcd_i_high_ptvar_25med[i]<min_rqcd_i_high_ptvar_25med:
                min_rqcd_i_high_ptvar_25med = rqcd_i_high_ptvar_25med[i]
        if rqcd_i_high_ptvar_25med[i]>max_rqcd_i_high_ptvar_25med:
                max_rqcd_i_high_ptvar_25med = rqcd_i_high_ptvar_25med[i]

print "PTVAR_25med: sys_i_low =", ((max_rqcd_i_low_ptvar_25med - min_rqcd_i_low_ptvar_25med)/2)
print "PTVAR_25med: sys_i_high =", ((max_rqcd_i_high_ptvar_25med - min_rqcd_i_high_ptvar_25med)/2)
print "PTVAR_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_25med - min_rqcd_i_low_ptvar_25med)/2)/rqcd_i_low_25med_val
print "PTVAR_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_25med - min_rqcd_i_high_ptvar_25med)/2)/rqcd_i_high_25med_val
print ""
print "---> total sys 25med low pt =", max( ((max_rqcd_i_low_topo_25med - min_rqcd_i_low_topo_25med)/2), ((max_rqcd_i_low_ptvar_25med - min_rqcd_i_low_ptvar_25med)/2))
print "---> total sys 25med high pt =", max( ((max_rqcd_i_high_topo_25med - min_rqcd_i_high_topo_25med)/2), ((max_rqcd_i_high_ptvar_25med - min_rqcd_i_high_ptvar_25med)/2) )
print ""
print "---> total sys 25med low pt (percentage) =", max( ((max_rqcd_i_low_topo_25med - min_rqcd_i_low_topo_25med)/2)/rqcd_i_low_25med_val, ((max_rqcd_i_low_ptvar_25med - min_rqcd_i_low_ptvar_25med)/2)/rqcd_i_low_25med_val )
print "---> total sys 25med high pt (percentage) =", max( ((max_rqcd_i_high_topo_25med - min_rqcd_i_high_topo_25med)/2)/rqcd_i_high_25med_val, ((max_rqcd_i_high_ptvar_25med - min_rqcd_i_high_ptvar_25med)/2)/rqcd_i_high_25med_val )

################################################################################################################################################################################################################

print ""
print "ONE PRONG"
print ""
print "*******************"
print ""

"""
#------------------------------#
#        NO TRIGGER
#------------------------------#

rqcd_i_val_1track = 

rqcd_i_topo_1track = []

min_rqcd_i_topo_1track = 2
max_rqcd_i_topo_1track = 0

for i in range(len(rqcd_i_topo_1track)):
	if rqcd_i_topo_1track[i] < min_rqcd_i_topo_1track:
		min_rqcd_i_topo_1track = rqcd_i_topo_1track[i]
	if rqcd_i_topo_1track[i] > max_rqcd_i_topo_1track:
		max_rqcd_i_topo_1track = rqcd_i_topo_1track[i]

rqcd_i_ptvar_1track = []

min_rqcd_i_ptvar_1track = 2
max_rqcd_i_ptvar_1track = 0

for i in range(len(rqcd_i_ptvar_1track)):
        if rqcd_i_ptvar_1track[i] < min_rqcd_i_ptvar_1track:
                min_rqcd_i_ptvar_1track = rqcd_i_ptvar_1track[i]
        if rqcd_i_ptvar_1track[i] > max_rqcd_i_ptvar_1track:
                max_rqcd_i_ptvar_1track = rqcd_i_ptvar_1track[i]

print "TOPO_no_trig: sys (percentage) =", ((max_rqcd_i_topo_1track - min_rqcd_i_topo_1track)/2)/rqcd_i_val_1track
print "PTVAR_no_trig: sys (percentage) =", ((max_rqcd_i_ptvar_1track - min_rqcd_i_ptvar_1track)/2)/rqcd_i_val_1track
print "TOPO_no_trig: sys =", ((max_rqcd_i_topo_1track - min_rqcd_i_topo_1track)/2)
print "PTVAR_no_trig: sys =", ((max_rqcd_i_ptvar_1track - min_rqcd_i_ptvar_1track)/2)
print ""
print "---> total sys no trig incl =", max( ((max_rqcd_i_topo_1track - min_rqcd_i_topo_1track)/2), ((max_rqcd_i_ptvar_1track - min_rqcd_i_ptvar_1track)/2) )
print "---> total sys no trig incl (percentage) =", max( ((max_rqcd_i_topo_1track - min_rqcd_i_topo_1track)/2)/rqcd_i_val_1track, ((max_rqcd_i_ptvar_1track - min_rqcd_i_ptvar_1track)/2)/rqcd_i_val_1track )
print ""

"""
# LOW VS HIGH PT
rqcd_i_low_1track_val = 1.127 
rqcd_i_high_1track_val = 1.183

rqcd_i_low_topo_1track = [1.107, 1.103, 1.096, 1.091, 1.088, 1.082, 1.090, 1.081, 1.070, 1.062, 1.060, 1.062, 1.068, 1.064, 1.057, 1.050, 1.049, 1.044, 1.038, 1.032, 1.028, 1.035, 1.025, 1.037, 1.026, 1.026, 1.039, 1.021, 1.025, 1.033]
rqcd_i_high_topo_1track = [1.152, 1.158, 1.149, 1.160, 1.166, 1.175, 1.178, 1.175, 1.171, 1.172, 1.185, 1.189, 1.189, 1.178, 1.201, 1.208, 1.189, 1.186, 1.180, 1.189, 1.197, 1.180, 1.186, 1.172, 1.186, 1.158, 1.146, 1.148, 1.145, 1.154]

diff_rqcd_i_low_val_topo_1track = 0
diff_rqcd_i_high_val_topo_1track = 0

min_rqcd_i_low_topo_1track = 2
max_rqcd_i_low_topo_1track = 0
min_rqcd_i_high_topo_1track = 2
max_rqcd_i_high_topo_1track = 0

for i in range(len(rqcd_i_low_topo_1track)):
	if rqcd_i_low_topo_1track[i]<min_rqcd_i_low_topo_1track:
		min_rqcd_i_low_topo_1track = rqcd_i_low_topo_1track[i]
	if rqcd_i_low_topo_1track[i]>max_rqcd_i_low_topo_1track:
		max_rqcd_i_low_topo_1track = rqcd_i_low_topo_1track[i]


for i in range(len(rqcd_i_high_topo_1track)):
        if rqcd_i_high_topo_1track[i]<min_rqcd_i_high_topo_1track:
                min_rqcd_i_high_topo_1track = rqcd_i_high_topo_1track[i]
        if rqcd_i_high_topo_1track[i]>max_rqcd_i_high_topo_1track:
                max_rqcd_i_high_topo_1track = rqcd_i_high_topo_1track[i]

print "TOPO_no_trig: sys_i_low =", ((max_rqcd_i_low_topo_1track - min_rqcd_i_low_topo_1track)/2)
print "TOPO_no_trig: sys_i_high =", ((max_rqcd_i_high_topo_1track - min_rqcd_i_high_topo_1track)/2)
print "TOPO_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track - min_rqcd_i_low_topo_1track)/2)/rqcd_i_low_1track_val
print "TOPO_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track - min_rqcd_i_high_topo_1track)/2)/rqcd_i_high_1track_val

rqcd_i_low_ptvar_1track = [1.089, 1.088, 1.084, 1.087, 1.087, 1.085, 1.082, 1.083, 1.087, 1.082, 1.081, 1.077, 1.074, 1.070, 1.069, 1.071, 1.072, 1.073, 1.075, 1.072, 1.081, 1.077, 1.080, 1.079, 1.083, 1.084, 1.085, 1.085, 1.081, 1.086, 1.085]
rqcd_i_high_ptvar_1track = [1.165, 1.165, 1.168, 1.166, 1.167, 1.169, 1.168, 1.167, 1.162, 1.161, 1.160, 1.154, 1.152, 1.154, 1.154, 1.155, 1.152, 1.154, 1.159, 1.157, 1.161, 1.162, 1.161, 1.163, 1.161, 1.166, 1.162, 1.166, 1.168, 1.166, 1.173]

min_rqcd_i_low_ptvar_1track = 2
max_rqcd_i_low_ptvar_1track = 0
min_rqcd_i_high_ptvar_1track = 2
max_rqcd_i_high_ptvar_1track = 0

for i in range(len(rqcd_i_low_ptvar_1track)):
        if rqcd_i_low_ptvar_1track[i]<min_rqcd_i_low_ptvar_1track:
                min_rqcd_i_low_ptvar_1track = rqcd_i_low_ptvar_1track[i]
        if rqcd_i_low_ptvar_1track[i]>max_rqcd_i_low_ptvar_1track:
                max_rqcd_i_low_ptvar_1track = rqcd_i_low_ptvar_1track[i]


for i in range(len(rqcd_i_high_ptvar_1track)):
        if rqcd_i_high_ptvar_1track[i]<min_rqcd_i_high_ptvar_1track:
                min_rqcd_i_high_ptvar_1track = rqcd_i_high_ptvar_1track[i]
        if rqcd_i_high_ptvar_1track[i]>max_rqcd_i_high_ptvar_1track:
                max_rqcd_i_high_ptvar_1track = rqcd_i_high_ptvar_1track[i]

print "PTVAR_no_trig: sys_i_low =", ((max_rqcd_i_low_ptvar_1track - min_rqcd_i_low_ptvar_1track)/2)
print "PTVAR_no_trig: sys_i_high =", ((max_rqcd_i_high_ptvar_1track - min_rqcd_i_high_ptvar_1track)/2)
print "PTVAR_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track - min_rqcd_i_low_ptvar_1track)/2)/rqcd_i_low_1track_val
print "PTVAR_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track - min_rqcd_i_high_ptvar_1track)/2)/rqcd_i_high_1track_val

print ""
print "---> total sys no trig low pt =", max( ((max_rqcd_i_low_ptvar_1track - min_rqcd_i_low_ptvar_1track)/2), ((max_rqcd_i_low_topo_1track - min_rqcd_i_low_topo_1track)/2))
print "---> total sys no trig high pt =", max( ((max_rqcd_i_high_ptvar_1track - min_rqcd_i_high_ptvar_1track)/2), ((max_rqcd_i_high_topo_1track - min_rqcd_i_high_topo_1track)/2))
print ""
print "---> total sys no trig low pt (percentage) =", max( ((max_rqcd_i_low_ptvar_1track - min_rqcd_i_low_ptvar_1track)/2)/rqcd_i_low_1track_val, ((max_rqcd_i_low_topo_1track - min_rqcd_i_low_topo_1track)/2)/rqcd_i_low_1track_val ) 
print "---> total sys no trig high pt (percentage) =", max( ((max_rqcd_i_high_ptvar_1track - min_rqcd_i_high_ptvar_1track)/2)/rqcd_i_high_1track_val, ((max_rqcd_i_high_topo_1track - min_rqcd_i_high_topo_1track)/2)/rqcd_i_high_1track_val )
print ""
print "***********"
print ""

# ----------------------------------- #
#     	   25 med trigger
# ------------------------------------#

rqcd_i_val_1track_25med = 1.148 

rqcd_i_topo_1track_25med = [1.131, 1.122, 1.116, 1.117, 1.117, 1.122, 1.120, 1.111, 1.109, 1.109, 1.111, 1.117, 1.105, 1.110, 1.110, 1.111, 1.097, 1.089, 1.080, 1.076, 1.078, 1.078, 1.082, 1.085, 1.084, 1.081, 1.083, 1.075, 1.076, 1.092]

min_rqcd_i_topo_1track_25med = 2
max_rqcd_i_topo_1track_25med = 0

for i in range(len(rqcd_i_topo_1track_25med)):
	if rqcd_i_topo_1track_25med[i] < min_rqcd_i_topo_1track_25med:
		min_rqcd_i_topo_1track_25med = rqcd_i_topo_1track_25med[i]
	if rqcd_i_topo_1track_25med[i] > max_rqcd_i_topo_1track_25med:
		max_rqcd_i_topo_1track_25med = rqcd_i_topo_1track_25med[i]

rqcd_i_ptvar_1track_25med = [1.120, 1.118, 1.117, 1.120, 1.123, 1.122, 1.120, 1.119, 1.120, 1.116, 1.116, 1.109, 1.107, 1.105, 1.106, 1.108, 1.105, 1.106, 1.110, 1.106, 1.111, 1.110, 1.109, 1.112, 1.111, 1.110, 1.113, 1.108, 1.108, 1.110, 1.114]     

min_rqcd_i_ptvar_1track_25med = 2
max_rqcd_i_ptvar_1track_25med = 0

for i in range(len(rqcd_i_ptvar_1track_25med)):
        if rqcd_i_ptvar_1track_25med[i] < min_rqcd_i_ptvar_1track_25med:
                min_rqcd_i_ptvar_1track_25med = rqcd_i_ptvar_1track_25med[i]
        if rqcd_i_ptvar_1track_25med[i] > max_rqcd_i_ptvar_1track_25med:
                max_rqcd_i_ptvar_1track_25med = rqcd_i_ptvar_1track_25med[i]

print "TOPO_25med: sys (percentage) =", ((max_rqcd_i_topo_1track_25med - min_rqcd_i_topo_1track_25med)/2)/rqcd_i_val_1track_25med
print "PTVAR_25med: sys (percentage) =", ((max_rqcd_i_ptvar_1track_25med - min_rqcd_i_ptvar_1track_25med)/2)/rqcd_i_val_1track_25med
print "TOPO_25med: sys =", ((max_rqcd_i_topo_1track_25med - min_rqcd_i_topo_1track_25med)/2)
print "PTVAR_25med: sys =", ((max_rqcd_i_ptvar_1track_25med - min_rqcd_i_ptvar_1track_25med)/2)
print ""
print "---> total sys 25med incl =", max( ((max_rqcd_i_topo_1track_25med - min_rqcd_i_topo_1track_25med)/2), ((max_rqcd_i_ptvar_1track_25med - min_rqcd_i_ptvar_1track_25med)/2))
print ""
print "---> total sys 25med incl (percentage) =", max( ((max_rqcd_i_topo_1track_25med - min_rqcd_i_topo_1track_25med)/2)/rqcd_i_val_1track_25med, ((max_rqcd_i_ptvar_1track_25med - min_rqcd_i_ptvar_1track_25med)/2)/rqcd_i_val_1track_25med )
print ""

# LOW VS HIGH PT

rqcd_i_low_1track_25med_val = 1.122 
rqcd_i_high_1track_25med_val = 1.183

rqcd_i_low_topo_1track_25med = [1.122, 1.114, 1.109, 1.095, 1.091, 1.083, 1.089, 1.084, 1.070, 1.064, 1.060, 1.061, 1.067, 1.059, 1.059, 1.052, 1.056, 1.042, 1.027, 1.011, 1.003, 1.005, 1.015, 1.014, 1.025, 1.020, 1.025, 1.039, 1.027]
rqcd_i_high_topo_1track_25med = [1.141, 1.150, 1.137, 1.141, 1.147, 1.158, 1.164, 1.165, 1.162, 1.167, 1.173, 1.176, 1.181, 1.164, 1.176, 1.184, 1.182, 1.169, 1.170, 1.170, 1.173, 1.174, 1.161, 1.173, 1.163, 1.162, 1.148, 1.135, 1.131]

min_rqcd_i_low_topo_1track_25med = 2
max_rqcd_i_low_topo_1track_25med = 0
min_rqcd_i_high_topo_1track_25med = 2
max_rqcd_i_high_topo_1track_25med = 0

for i in range(len(rqcd_i_low_topo_1track_25med)):
	if rqcd_i_low_topo_1track_25med[i]<min_rqcd_i_low_topo_1track_25med:
		min_rqcd_i_low_topo_1track_25med = rqcd_i_low_topo_1track_25med[i]
	if rqcd_i_low_topo_1track_25med[i]>max_rqcd_i_low_topo_1track_25med:
		max_rqcd_i_low_topo_1track_25med = rqcd_i_low_topo_1track_25med[i]


for i in range(len(rqcd_i_high_topo_1track_25med)):
        if rqcd_i_high_topo_1track_25med[i]<min_rqcd_i_high_topo_1track_25med:
                min_rqcd_i_high_topo_1track_25med = rqcd_i_high_topo_1track_25med[i]
        if rqcd_i_high_topo_1track_25med[i]>max_rqcd_i_high_topo_1track_25med:
                max_rqcd_i_high_topo_1track_25med = rqcd_i_high_topo_1track_25med[i]

print "TOPO_25med: sys_i_low =", ((max_rqcd_i_low_topo_1track_25med - min_rqcd_i_low_topo_1track_25med)/2)
print "TOPO_25med: sys_i_high =", ((max_rqcd_i_high_topo_1track_25med - min_rqcd_i_high_topo_1track_25med)/2)
print "TOPO_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_25med - min_rqcd_i_low_topo_1track_25med)/2)/rqcd_i_low_1track_25med_val
print "TOPO_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_25med - min_rqcd_i_high_topo_1track_25med)/2)/rqcd_i_high_1track_25med_val

rqcd_i_low_ptvar_1track_25med = [1.093, 1.090, 1.086, 1.090, 1.094, 1.093, 1.089, 1.090, 1.095, 1.087, 1.086, 1.081, 1.077, 1.073, 1.073, 1.076, 1.076, 1.075, 1.076, 1.073, 1.080, 1.078, 1.080, 1.079, 1.081, 1.079, 1.078, 1.081, 1.073, 1.075, 1.076]
rqcd_i_high_ptvar_1track_25med = [1.152, 1.149, 1.153, 1.153, 1.156, 1.156, 1.155, 1.152, 1.150, 1.150, 1.149, 1.141, 1.141, 1.143, 1.143, 1.144, 1.139, 1.141, 1.148, 1.144, 1.146, 1.146, 1.142, 1.148, 1.146, 1.148, 1.146, 1.150, 1.148, 1.149, 1.158]

min_rqcd_i_low_ptvar_1track_25med = 2
max_rqcd_i_low_ptvar_1track_25med = 0
min_rqcd_i_high_ptvar_1track_25med = 2
max_rqcd_i_high_ptvar_1track_25med = 0

for i in range(len(rqcd_i_low_ptvar_1track_25med)):
        if rqcd_i_low_ptvar_1track_25med[i]<min_rqcd_i_low_ptvar_1track_25med:
                min_rqcd_i_low_ptvar_1track_25med = rqcd_i_low_ptvar_1track_25med[i]
        if rqcd_i_low_ptvar_1track_25med[i]>max_rqcd_i_low_ptvar_1track_25med:
                max_rqcd_i_low_ptvar_1track_25med = rqcd_i_low_ptvar_1track_25med[i]


for i in range(len(rqcd_i_high_ptvar_1track_25med)):
        if rqcd_i_high_ptvar_1track_25med[i]<min_rqcd_i_high_ptvar_1track_25med:
                min_rqcd_i_high_ptvar_1track_25med = rqcd_i_high_ptvar_1track_25med[i]
        if rqcd_i_high_ptvar_1track_25med[i]>max_rqcd_i_high_ptvar_1track_25med:
                max_rqcd_i_high_ptvar_1track_25med = rqcd_i_high_ptvar_1track_25med[i]

print "PTVAR_25med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_25med - min_rqcd_i_low_ptvar_1track_25med)/2)
print "PTVAR_25med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_25med - min_rqcd_i_high_ptvar_1track_25med)/2)
print "PTVAR_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_25med - min_rqcd_i_low_ptvar_1track_25med)/2)/rqcd_i_low_1track_25med_val
print "PTVAR_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_25med - min_rqcd_i_high_ptvar_1track_25med)/2)/rqcd_i_high_1track_25med_val
print ""
print "---> total sys 25med low pt =", max( ((max_rqcd_i_low_topo_1track_25med - min_rqcd_i_low_topo_1track_25med)/2), ((max_rqcd_i_low_ptvar_1track_25med - min_rqcd_i_low_ptvar_1track_25med)/2))
print "---> total sys 25med high pt =", max( ((max_rqcd_i_high_topo_1track_25med - min_rqcd_i_high_topo_1track_25med)/2), ((max_rqcd_i_high_ptvar_1track_25med - min_rqcd_i_high_ptvar_1track_25med)/2) )
print ""
print "---> total sys 25med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_25med - min_rqcd_i_low_topo_1track_25med)/2)/rqcd_i_low_1track_25med_val, ((max_rqcd_i_low_ptvar_1track_25med - min_rqcd_i_low_ptvar_1track_25med)/2)/rqcd_i_low_1track_25med_val )
print "---> total sys 25med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_25med - min_rqcd_i_high_topo_1track_25med)/2)/rqcd_i_high_1track_25med_val, ((max_rqcd_i_high_ptvar_1track_25med - min_rqcd_i_high_ptvar_1track_25med)/2)/rqcd_i_high_1track_25med_val )


################################################################################################################################################################################################################

print ""
print "THREE PRONG"
print ""
print "*******************"
print ""


#------------------------------#
#        NO TRIGGER
#------------------------------#
"""
rqcd_i_val_3track = 

rqcd_i_topo_3track = []

min_rqcd_i_topo_3track = 2
max_rqcd_i_topo_3track = 0

for i in range(len(rqcd_i_topo_3track)):
	if rqcd_i_topo_3track[i] < min_rqcd_i_topo_3track:
		min_rqcd_i_topo_3track = rqcd_i_topo_3track[i]
	if rqcd_i_topo_3track[i] > max_rqcd_i_topo_3track:
		max_rqcd_i_topo_3track = rqcd_i_topo_3track[i]

rqcd_i_ptvar_3track = []

min_rqcd_i_ptvar_3track = 2
max_rqcd_i_ptvar_3track = 0

for i in range(len(rqcd_i_ptvar_3track)):
        if rqcd_i_ptvar_3track[i] < min_rqcd_i_ptvar_3track:
                min_rqcd_i_ptvar_3track = rqcd_i_ptvar_3track[i]
        if rqcd_i_ptvar_3track[i] > max_rqcd_i_ptvar_3track:
                max_rqcd_i_ptvar_3track = rqcd_i_ptvar_3track[i]

print "TOPO_no_trig: sys (percentage) =", ((max_rqcd_i_topo_3track - min_rqcd_i_topo_3track)/2)/rqcd_i_val_3track
print "PTVAR_no_trig: sys (percentage) =", ((max_rqcd_i_ptvar_3track - min_rqcd_i_ptvar_3track)/2)/rqcd_i_val_3track
print "TOPO_no_trig: sys =", ((max_rqcd_i_topo_3track - min_rqcd_i_topo_3track)/2)
print "PTVAR_no_trig: sys =", ((max_rqcd_i_ptvar_3track - min_rqcd_i_ptvar_3track)/2)
print ""
print "---> total sys no trig incl =", max( ((max_rqcd_i_topo_3track - min_rqcd_i_topo_3track)/2), ((max_rqcd_i_ptvar_3track - min_rqcd_i_ptvar_3track)/2) )
print "---> total sys no trig incl (percentage) =", max( ((max_rqcd_i_topo_3track - min_rqcd_i_topo_3track)/2)/rqcd_i_val_3track, ((max_rqcd_i_ptvar_3track - min_rqcd_i_ptvar_3track)/2)/rqcd_i_val_3track )
print ""


# LOW VS HIGH PT
rqcd_i_low_3track_val = 
rqcd_i_high_3track_val = 

rqcd_i_low_topo_3track = []
rqcd_i_high_topo_3track = []

diff_rqcd_i_low_val_topo_3track = 0
diff_rqcd_i_high_val_topo_3track = 0

min_rqcd_i_low_topo_3track = 2
max_rqcd_i_low_topo_3track = 0
min_rqcd_i_high_topo_3track = 2
max_rqcd_i_high_topo_3track = 0

for i in range(len(rqcd_i_low_topo_3track)):
	if rqcd_i_low_topo_3track[i]<min_rqcd_i_low_topo_3track:
		min_rqcd_i_low_topo_3track = rqcd_i_low_topo_3track[i]
	if rqcd_i_low_topo_3track[i]>max_rqcd_i_low_topo_3track:
		max_rqcd_i_low_topo_3track = rqcd_i_low_topo_3track[i]


for i in range(len(rqcd_i_high_topo_3track)):
        if rqcd_i_high_topo_3track[i]<min_rqcd_i_high_topo_3track:
                min_rqcd_i_high_topo_3track = rqcd_i_high_topo_3track[i]
        if rqcd_i_high_topo_3track[i]>max_rqcd_i_high_topo_3track:
                max_rqcd_i_high_topo_3track = rqcd_i_high_topo_3track[i]

print "TOPO_no_trig: sys_i_low =", ((max_rqcd_i_low_topo_3track - min_rqcd_i_low_topo_3track)/2)
print "TOPO_no_trig: sys_i_high =", ((max_rqcd_i_high_topo_3track - min_rqcd_i_high_topo_3track)/2)
print "TOPO_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track - min_rqcd_i_low_topo_3track)/2)/rqcd_i_low_3track_val
print "TOPO_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track - min_rqcd_i_high_topo_3track)/2)/rqcd_i_high_3track_val

rqcd_i_low_ptvar_3track = []
rqcd_i_high_ptvar_3track = []

min_rqcd_i_low_ptvar_3track = 2
max_rqcd_i_low_ptvar_3track = 0
min_rqcd_i_high_ptvar_3track = 2
max_rqcd_i_high_ptvar_3track = 0

for i in range(len(rqcd_i_low_ptvar_3track)):
        if rqcd_i_low_ptvar_3track[i]<min_rqcd_i_low_ptvar_3track:
                min_rqcd_i_low_ptvar_3track = rqcd_i_low_ptvar_3track[i]
        if rqcd_i_low_ptvar_3track[i]>max_rqcd_i_low_ptvar_3track:
                max_rqcd_i_low_ptvar_3track = rqcd_i_low_ptvar_3track[i]


for i in range(len(rqcd_i_high_ptvar_3track)):
        if rqcd_i_high_ptvar_3track[i]<min_rqcd_i_high_ptvar_3track:
                min_rqcd_i_high_ptvar_3track = rqcd_i_high_ptvar_3track[i]
        if rqcd_i_high_ptvar_3track[i]>max_rqcd_i_high_ptvar_3track:
                max_rqcd_i_high_ptvar_3track = rqcd_i_high_ptvar_3track[i]

print "PTVAR_no_trig: sys_i_low =", ((max_rqcd_i_low_ptvar_3track - min_rqcd_i_low_ptvar_3track)/2)
print "PTVAR_no_trig: sys_i_high =", ((max_rqcd_i_high_ptvar_3track - min_rqcd_i_high_ptvar_3track)/2)
print "PTVAR_no_trig: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track - min_rqcd_i_low_ptvar_3track)/2)/rqcd_i_low_3track_val
print "PTVAR_no_trig: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track - min_rqcd_i_high_ptvar_3track)/2)/rqcd_i_high_3track_val

print ""
print "---> total sys no trig low pt =", max( ((max_rqcd_i_low_ptvar_3track - min_rqcd_i_low_ptvar_3track)/2), ((max_rqcd_i_low_topo_3track - min_rqcd_i_low_topo_3track)/2))
print "---> total sys no trig high pt =", max( ((max_rqcd_i_high_ptvar_3track - min_rqcd_i_high_ptvar_3track)/2), ((max_rqcd_i_high_topo_3track - min_rqcd_i_high_topo_3track)/2))
print ""
print "---> total sys no trig low pt (percentage) =", max( ((max_rqcd_i_low_ptvar_3track - min_rqcd_i_low_ptvar_3track)/2)/rqcd_i_low_3track_val, ((max_rqcd_i_low_topo_3track - min_rqcd_i_low_topo_3track)/2)/rqcd_i_low_3track_val ) 
print "---> total sys no trig high pt (percentage) =", max( ((max_rqcd_i_high_ptvar_3track - min_rqcd_i_high_ptvar_3track)/2)/rqcd_i_high_3track_val, ((max_rqcd_i_high_topo_3track - min_rqcd_i_high_topo_3track)/2)/rqcd_i_high_3track_val )
print ""
print "***********"
print ""
"""
# ----------------------------------- #
#     	   25 med trigger
# ------------------------------------#

rqcd_i_val_3track_25med = 1.301  

rqcd_i_topo_3track_25med = [1.244, 1.222, 1.217, 1.195, 1.187, 1.195, 1.161, 1.158, 1.161, 1.122, 1.136, 1.108, 1.112, 1.094, 1.092, 1.062, 1.042, 1.015, 0.993, 0.979, 0.959, 0.960, 0.957, 0.934, 0.957, 1.003, 1.957, 0.922, 0.874, 0.878, 0.867]

min_rqcd_i_topo_3track_25med = 2
max_rqcd_i_topo_3track_25med = 0

for i in range(len(rqcd_i_topo_3track_25med)):
	if rqcd_i_topo_3track_25med[i] < min_rqcd_i_topo_3track_25med:
		min_rqcd_i_topo_3track_25med = rqcd_i_topo_3track_25med[i]
	if rqcd_i_topo_3track_25med[i] > max_rqcd_i_topo_3track_25med:
		max_rqcd_i_topo_3track_25med = rqcd_i_topo_3track_25med[i]

rqcd_i_ptvar_3track_25med = [1.222, 1.229, 1.226, 1.223, 1.225, 1.218, 1.227, 1.230, 1.225, 1.222, 1.215, 1.213, 1.227, 1.223, 1.213, 1.219, 1.222, 1.232, 1.224, 1.227, 1.218, 1.220, 1.220, 1.223, 1.231, 1.231, 1.216, 1.224, 1.225, 1.214]     

min_rqcd_i_ptvar_3track_25med = 2
max_rqcd_i_ptvar_3track_25med = 0

for i in range(len(rqcd_i_ptvar_3track_25med)):
        if rqcd_i_ptvar_3track_25med[i] < min_rqcd_i_ptvar_3track_25med:
                min_rqcd_i_ptvar_3track_25med = rqcd_i_ptvar_3track_25med[i]
        if rqcd_i_ptvar_3track_25med[i] > max_rqcd_i_ptvar_3track_25med:
                max_rqcd_i_ptvar_3track_25med = rqcd_i_ptvar_3track_25med[i]

print "TOPO_25med: sys (percentage) =", ((max_rqcd_i_topo_3track_25med - min_rqcd_i_topo_3track_25med)/2)/rqcd_i_val_3track_25med
print "PTVAR_25med: sys (percentage) =", ((max_rqcd_i_ptvar_3track_25med - min_rqcd_i_ptvar_3track_25med)/2)/rqcd_i_val_3track_25med
print "TOPO_25med: sys =", ((max_rqcd_i_topo_3track_25med - min_rqcd_i_topo_3track_25med)/2)
print "PTVAR_25med: sys =", ((max_rqcd_i_ptvar_3track_25med - min_rqcd_i_ptvar_3track_25med)/2)
print ""
print "---> total sys 25med incl =", max( ((max_rqcd_i_topo_3track_25med - min_rqcd_i_topo_3track_25med)/2), ((max_rqcd_i_ptvar_3track_25med - min_rqcd_i_ptvar_3track_25med)/2))
print ""
print "---> total sys 25med incl (percentage) =", max( ((max_rqcd_i_topo_3track_25med - min_rqcd_i_topo_3track_25med)/2)/rqcd_i_val_3track_25med, ((max_rqcd_i_ptvar_3track_25med - min_rqcd_i_ptvar_3track_25med)/2)/rqcd_i_val_3track_25med )
print ""

# LOW VS HIGH PT
rqcd_i_low_3track_25med_val = 1.170 
rqcd_i_high_3track_25med_val = 1.493

rqcd_i_low_topo_3track_25med = [1.136, 1.113, 1.111, 1.094, 1.083, 1.089, 1.067, 1.076, 1.080, 1.047, 1.071, 1.056, 1.050, 1.052, 1.024, 0.989, 0.943, 0.908, 0.884, 0.864, 0.841, 0.837, 0.823, 0.794, 0.864, 0.907, 0.827, 0.783, 0.769, 0.794, 0.746]
rqcd_i_high_topo_3track_25med = [1.410, 1.384, 1.372, 1.342, 1.335, 1.348, 1.277, 1.262, 1.261, 1.214, 1.215, 1.172, 1.189, 1.145, 1.177, 1.156, 1.169, 1.158, 1.133, 1.126, 1.114, 1.123, 1.135, 1.113, 1.075, 1.127, 1.126, 1.098, 1.006, 0.982, 1.019]

min_rqcd_i_low_topo_3track_25med = 2
max_rqcd_i_low_topo_3track_25med = 0
min_rqcd_i_high_topo_3track_25med = 2
max_rqcd_i_high_topo_3track_25med = 0

for i in range(len(rqcd_i_low_topo_3track_25med)):
	if rqcd_i_low_topo_3track_25med[i]<min_rqcd_i_low_topo_3track_25med:
		min_rqcd_i_low_topo_3track_25med = rqcd_i_low_topo_3track_25med[i]
	if rqcd_i_low_topo_3track_25med[i]>max_rqcd_i_low_topo_3track_25med:
		max_rqcd_i_low_topo_3track_25med = rqcd_i_low_topo_3track_25med[i]


for i in range(len(rqcd_i_high_topo_3track_25med)):
        if rqcd_i_high_topo_3track_25med[i]<min_rqcd_i_high_topo_3track_25med:
                min_rqcd_i_high_topo_3track_25med = rqcd_i_high_topo_3track_25med[i]
        if rqcd_i_high_topo_3track_25med[i]>max_rqcd_i_high_topo_3track_25med:
                max_rqcd_i_high_topo_3track_25med = rqcd_i_high_topo_3track_25med[i]

print "TOPO_25med: sys_i_low =", ((max_rqcd_i_low_topo_3track_25med - min_rqcd_i_low_topo_3track_25med)/2)
print "TOPO_25med: sys_i_high =", ((max_rqcd_i_high_topo_3track_25med - min_rqcd_i_high_topo_3track_25med)/2)
print "TOPO_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_25med - min_rqcd_i_low_topo_3track_25med)/2)/rqcd_i_low_3track_25med_val
print "TOPO_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_25med - min_rqcd_i_high_topo_3track_25med)/2)/rqcd_i_high_3track_25med_val

rqcd_i_low_ptvar_3track_25med = [1.113, 1.117, 1.122, 1.110, 1.117, 1.111, 1.113, 1.115, 1.117, 1.111, 1.114, 1.112, 1.127, 1.125, 1.116, 1.131, 1.141, 1.146, 1.136, 1.138, 1.134, 1.135, 1.137, 1.133, 1.149, 1.153, 1.148, 1.149, 1.164, 1.164, 1.154]
rqcd_i_high_ptvar_3track_25med = [1.360, 1.369, 1.355, 1.364, 1.359, 1.349, 1.370, 1.373, 1.358, 1.359, 1.362, 1.357, 1.371, 1.364, 1.354, 1.347, 1.342, 1.356, 1.350, 1.356, 1.342, 1.345, 1.343, 1.353, 1.347, 1.323, 1.316, 1.341, 1.329, 1.325, 1.321]

min_rqcd_i_low_ptvar_3track_25med = 2
max_rqcd_i_low_ptvar_3track_25med = 0
min_rqcd_i_high_ptvar_3track_25med = 2
max_rqcd_i_high_ptvar_3track_25med = 0

for i in range(len(rqcd_i_low_ptvar_3track_25med)):
        if rqcd_i_low_ptvar_3track_25med[i]<min_rqcd_i_low_ptvar_3track_25med:
                min_rqcd_i_low_ptvar_3track_25med = rqcd_i_low_ptvar_3track_25med[i]
        if rqcd_i_low_ptvar_3track_25med[i]>max_rqcd_i_low_ptvar_3track_25med:
                max_rqcd_i_low_ptvar_3track_25med = rqcd_i_low_ptvar_3track_25med[i]


for i in range(len(rqcd_i_high_ptvar_3track_25med)):
        if rqcd_i_high_ptvar_3track_25med[i]<min_rqcd_i_high_ptvar_3track_25med:
                min_rqcd_i_high_ptvar_3track_25med = rqcd_i_high_ptvar_3track_25med[i]
        if rqcd_i_high_ptvar_3track_25med[i]>max_rqcd_i_high_ptvar_3track_25med:
                max_rqcd_i_high_ptvar_3track_25med = rqcd_i_high_ptvar_3track_25med[i]

print "PTVAR_25med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_25med - min_rqcd_i_low_ptvar_3track_25med)/2)
print "PTVAR_25med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_25med - min_rqcd_i_high_ptvar_3track_25med)/2)
print "PTVAR_25med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_25med - min_rqcd_i_low_ptvar_3track_25med)/2)/rqcd_i_low_3track_25med_val
print "PTVAR_25med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_25med - min_rqcd_i_high_ptvar_3track_25med)/2)/rqcd_i_high_3track_25med_val
print ""
print "---> total sys 25med low pt =", max( ((max_rqcd_i_low_topo_3track_25med - min_rqcd_i_low_topo_3track_25med)/2), ((max_rqcd_i_low_ptvar_3track_25med - min_rqcd_i_low_ptvar_3track_25med)/2))
print "---> total sys 25med high pt =", max( ((max_rqcd_i_high_topo_3track_25med - min_rqcd_i_high_topo_3track_25med)/2), ((max_rqcd_i_high_ptvar_3track_25med - min_rqcd_i_high_ptvar_3track_25med)/2) )
print ""
print "---> total sys 25med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_25med - min_rqcd_i_low_topo_3track_25med)/2)/rqcd_i_low_3track_25med_val, ((max_rqcd_i_low_ptvar_3track_25med - min_rqcd_i_low_ptvar_3track_25med)/2)/rqcd_i_low_3track_25med_val )
print "---> total sys 25med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_25med - min_rqcd_i_high_topo_3track_25med)/2)/rqcd_i_high_3track_25med_val, ((max_rqcd_i_high_ptvar_3track_25med - min_rqcd_i_high_ptvar_3track_25med)/2)/rqcd_i_high_3track_25med_val )


