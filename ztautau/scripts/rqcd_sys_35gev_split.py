# incl no trig

from math import *

print "INCLUSIVE"
print ""
print "*******************"
print ""

#------------------------------#
#        NO TRIGGER
#------------------------------#
"""
rqcd_i_val = 

rqcd_i_topo = 

min_rqcd_i_topo = 2
max_rqcd_i_topo = 0

for i in range(len(rqcd_i_topo)):
	if rqcd_i_topo[i] < min_rqcd_i_topo:
		min_rqcd_i_topo = rqcd_i_topo[i]
	if rqcd_i_topo[i] > max_rqcd_i_topo:
		max_rqcd_i_topo = rqcd_i_topo[i]

rqcd_i_ptvar =

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

"""
# LOW VS HIGH PT
rqcd_i_low_val = 1.137
rqcd_i_high_val = 1.207

rqcd_i_low_topo = [1.122, 1.115, 1.106, 1.103, 1.102, 1.095, 1.097, 1.096, 1.085, 1.081, 1.083, 1.077, 1.081, 1.076, 1.078, 1.069, 1.060, 1.044, 1.031, 1.030, 1.024, 1.024, 1.024, 1.019, 1.033, 1.029, 1.023, 1.026, 1.025, 1.033, 1.028]
rqcd_i_high_topo = [1.175, 1.175, 1.170, 1.164, 1.168, 1.169, 1.170, 1.160, 1.156, 1.144, 1.156, 1.155, 1.158, 1.153, 1.156, 1.166, 1.172, 1.164, 1.159, 1.151, 1.153, 1.150, 1.142, 1.137, 1.124, 1.136, 1.117, 1.107, 1.087, 1.080, 1.094]

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

rqcd_i_low_ptvar = [1.101, 1.102, 1.101, 1.101, 1.103, 1.102, 1.097, 1.098, 1.101, 1.097, 1.094, 1.091, 1.091, 1.089, 1.088, 1.092, 1.093, 1.094, 1.095, 1.093, 1.098, 1.096, 1.099, 1.096, 1.102, 1.102, 1.101, 1.104, 1.106, 1.110, 1.110]
rqcd_i_high_ptvar = [1.169, 1.169, 1.168, 1.168, 1.169, 1.169, 1.171, 1.171, 1.168, 1.165, 1.166, 1.161, 1.161, 1.160, 1.159, 1.158, 1.154, 1.157, 1.162, 1.161, 1.165, 1.167, 1.167, 1.169, 1.169, 1.173, 1.170, 1.173, 1.169, 1.168, 1.172]

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
"""
rqcd_i_val_25med =  

rqcd_i_topo_25med = 

min_rqcd_i_topo_25med = 2
max_rqcd_i_topo_25med = 0

for i in range(len(rqcd_i_topo_25med)):
	if rqcd_i_topo_25med[i] < min_rqcd_i_topo_25med:
		min_rqcd_i_topo_25med = rqcd_i_topo_25med[i]
	if rqcd_i_topo_25med[i] > max_rqcd_i_topo_25med:
		max_rqcd_i_topo_25med = rqcd_i_topo_25med[i]

rqcd_i_ptvar_25med =      

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
"""
# LOW VS HIGH PT
rqcd_i_low_25med_val = 1.120  
rqcd_i_high_25med_val = 1.211

rqcd_i_low_topo_25med = [1.117, 1.103, 1.101, 1.096, 1.093, 1.091, 1.090, 1.096, 1.088, 1.076, 1.075, 1.077, 1.088, 1.078, 1.079, 1.060, 1.051, 1.025, 1.000, 0.994, 0.982, 0.993, 0.992, 0.988, 1.014, 1.014, 1.006, 1.013, 1.015, 1.016, 1.030]
rqcd_i_high_topo_25med = [1.171, 1.175, 1.162, 1.152, 1.152, 1.155, 1.154, 1.146, 1.139, 1.136, 1.141, 1.134, 1.136, 1.121, 1.128, 1.133, 1.137, 1.128, 1.130, 1.116, 1.114, 1.109, 1.109, 1.112, 1.102, 1.112, 1.100, 1.088, 1.061, 1.063, 1.073]

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

rqcd_i_low_ptvar_25med = [1.089, 1.088, 1.085, 1.086, 1.091, 1.089, 1.084, 1.084, 1.092, 1.088, 1.084, 1.077, 1.075, 1.071, 1.072, 1.079, 1.082, 1.083, 1.082, 1.079, 1.083, 1.081, 1.083, 1.082, 1.088, 1.081, 1.078, 1.084, 1.084, 1.084]
rqcd_i_high_ptvar_25med = [1.166, 1.165, 1.165, 1.167, 1.169, 1.168, 1.169, 1.169, 1.164, 1.160, 1.160, 1.155, 1.157, 1.156, 1.154, 1.153, 1.148, 1.151, 1.155, 1.152, 1.155, 1.154, 1.152, 1.157, 1.155, 1.158, 1.156, 1.159, 1.152, 1.153]

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


#------------------------------#
#        NO TRIGGER
#------------------------------#
"""
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
rqcd_i_low_1track_val = 1.121  
rqcd_i_high_1track_val = 1.170

rqcd_i_low_topo_1track = [1.096, 1.090, 1.080, 1.079, 1.076, 1.074, 1.079, 1.074, 1.064, 1.059, 1.052, 1.052, 1.056, 1.050, 1.058, 1.045, 1.037, 1.027, 1.019, 1.022, 1.013, 1.016, 1.017, 1.012, 1.026, 1.016, 1.019, 1.030, 1.023, 1.027, 1.036]
rqcd_i_high_topo_1track = [1.149, 1.157, 1.152, 1.150, 1.157, 1.156, 1.163, 1.155, 1.150, 1.145, 1.160, 1.165, 1.168, 1.161, 1.164, 1.178, 1.184, 1.179, 1.177, 1.162, 1.171, 1.167, 1.163, 1.161, 1.149, 1.159, 1.134, 1.129, 1.115, 1.115, 1.122]

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

rqcd_i_low_ptvar_1track = [1.092, 1.092, 1.089, 1.091, 1.091, 1.089, 1.084, 1.085, 1.090, 1.086, 1.083, 1.078, 1.075, 1.072, 1.071, 1.074, 1.077, 1.078, 1.081, 1.078, 1.086, 1.082, 1.085, 1.084, 1.089, 1.087, 1.086, 1.087, 1.086, 1.093, 1.093]
rqcd_i_high_ptvar_1track = [1.145, 1.144, 1.145, 1.145, 1.146, 1.147, 1.148, 1.148, 1.144, 1.141, 1.142, 1.137, 1.135, 1.135, 1.135, 1.135, 1.130, 1.132, 1.137, 1.135, 1.140, 1.140, 1.139, 1.141, 1.140, 1.146, 1.145, 1.148, 1.145, 1.143, 1.148]

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
"""
rqcd_i_val_1track_25med =  

rqcd_i_topo_1track_25med = 

min_rqcd_i_topo_1track_25med = 2
max_rqcd_i_topo_1track_25med = 0

for i in range(len(rqcd_i_topo_1track_25med)):
	if rqcd_i_topo_1track_25med[i] < min_rqcd_i_topo_1track_25med:
		min_rqcd_i_topo_1track_25med = rqcd_i_topo_1track_25med[i]
	if rqcd_i_topo_1track_25med[i] > max_rqcd_i_topo_1track_25med:
		max_rqcd_i_topo_1track_25med = rqcd_i_topo_1track_25med[i]

rqcd_i_ptvar_1track_25med =      

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
"""
# LOW VS HIGH PT

rqcd_i_low_1track_25med_val = 1.116  
rqcd_i_high_1track_25med_val = 1.172

rqcd_i_low_topo_1track_25med = [1.115, 1.103, 1.098, 1.094, 1.090, 1.089, 1.092, 1.093, 1.082, 1.075, 1.067, 1.070, 1.081, 1.069, 1.077, 1.062, 1.063, 1.037, 1.014, 1.011, 0.998, 1.009, 1.011, 1.011, 1.021, 1.019, 1.022, 1.031, 1.032, 1.028, 1.057]
rqcd_i_high_topo_1track_25med = [1.142, 1.150, 1.139, 1.132, 1.135, 1.136, 1.143, 1.139, 1.131, 1.133, 1.140, 1.140, 1.142, 1.130, 1.133, 1.145, 1.144, 1.140, 1.144, 1.130, 1.134, 1.128, 1.127, 1.134, 1.130, 1.129, 1.120, 1.117, 1.101, 1.106, 1.113]

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

rqcd_i_low_ptvar_1track_25med = [1.096, 1.094, 1.090, 1.094, 1.099, 1.098, 1.092, 1.092, 1.098, 1.095, 1.091, 1.084, 1.080, 1.077, 1.080, 1.084, 1.086, 1.086, 1.088, 1.085, 1.091, 1.091, 1.094, 1.093, 1.095, 1.088, 1.085, 1.093, 1.089, 1.092, 1.092]
rqcd_i_high_ptvar_1track_25med = [1.137, 1.134, 1.135, 1.137, 1.139, 1.139, 1.139, 1.138, 1.136, 1.131, 1.133, 1.126, 1.125, 1.125, 1.124, 1.124, 1.119, 1.119, 1.125, 1.120, 1.125, 1.122, 1.119, 1.124, 1.122, 1.128, 1.127, 1.127, 1.122, 1.122, 1.129]

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
"""

# LOW VS HIGH PT
rqcd_i_low_3track_val = 1.178 
rqcd_i_high_3track_val = 1.364

rqcd_i_low_topo_3track = [1.186, 1.178, 1.173, 1.168, 1.170, 1.154, 1.148, 1.155, 1.144, 1.142, 1.171, 1.146, 1.151, 1.148, 1.133, 1.134, 1.124, 1.091, 1.064, 1.053, 1.052, 1.045, 1.042, 1.039, 1.054, 1.065, 1.032, 1.013, 1.030, 1.051, 1.005]
rqcd_i_high_topo_3track = [1.281, 1.249, 1.241, 1.217, 1.208, 1.224, 1.196, 1.178, 1.179, 1.137, 1.135, 1.106, 1.107, 1.114, 1.115, 1.109, 1.110, 1.090, 1.073, 1.089, 1.064, 1.063, 1.041, 1.023, 1.002, 1.026, 1.031, 0.997, 0.953, 0.915, 0.956]

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

rqcd_i_low_ptvar_3track = [1.126, 1.127, 1.132, 1.128, 1.133, 1.133, 1.130, 1.130, 1.128, 1.125, 1.124, 1.121, 1.132, 1.136, 1.132, 1.138, 1.134, 1.135, 1.132, 1.134, 1.130, 1.132, 1.133, 1.128, 1.135, 1.141, 1.140, 1.151, 1.158, 1.155, 1.154]
rqcd_i_high_ptvar_3track = [1.273, 1.278, 1.270, 1.271, 1.274, 1.267, 1.275, 1.274, 1.275, 1.274, 1.275, 1.272, 1.282, 1.278, 1.268, 1.264, 1.260, 1.269, 1.278, 1.282, 1.281, 1.291, 1.295, 1.299, 1.302, 1.292, 1.283, 1.289, 1.277, 1.280, 1.279]

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

rqcd_i_val_3track_25med =   

rqcd_i_topo_3track_25med = 

min_rqcd_i_topo_3track_25med = 2
max_rqcd_i_topo_3track_25med = 0

for i in range(len(rqcd_i_topo_3track_25med)):
	if rqcd_i_topo_3track_25med[i] < min_rqcd_i_topo_3track_25med:
		min_rqcd_i_topo_3track_25med = rqcd_i_topo_3track_25med[i]
	if rqcd_i_topo_3track_25med[i] > max_rqcd_i_topo_3track_25med:
		max_rqcd_i_topo_3track_25med = rqcd_i_topo_3track_25med[i]

rqcd_i_ptvar_3track_25med =      

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
"""
# LOW VS HIGH PT
rqcd_i_low_3track_25med_val = 1.139  
rqcd_i_high_3track_25med_val = 1.411

rqcd_i_low_topo_3track_25med = [1.120, 1.099, 1.116, 1.103, 1.109, 1.101, 1.077, 1.113, 1.125, 1.078, 1.127, 1.127, 1.121, 1.130, 1.144, 1.090, 1.049, 0.968, 0.948, 0.898, 0.876, 0.878, 0.886, 0.871, 0.836, 0.964, 0.985, 0.903, 0.896, 0.903, 0.936, 0.861]
rqcd_i_high_topo_3track_25med = [1.324, 1.300, 1.279, 1.253, 1.236, 1.254, 1.207, 1.183, 1.179, 1.145, 1.139, 1.139, 1.101, 1.102, 1.066, 1.092, 1.069, 1.083, 1.053, 1.047, 1.037, 1.006, 1.002, 1.006, 0.989, 0.952, 1.011, 0.986, 0.934, 0.857, 0.845, 0.868]

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

rqcd_i_low_ptvar_3track_25med = [1.046, 1.047, 1.049, 1.032, 1.035, 1.028, 1.031, 1.036, 1.048, 1.044, 1.039, 1.030, 1.035, 1.028, 1.019, 1.042, 1.051, 1.053, 1.038, 1.032, 1.025, 1.014, 1.014, 1.010, 1.037, 1.032, 1.028, 1.023, 1.051, 1.035, 1.027]
rqcd_i_high_ptvar_3track_25med = [1.328, 1.338, 1.331, 1.337, 1.338, 1.330, 1.344, 1.346, 1.329, 1.327, 1.320, 1.341, 1.320, 1.339, 1.328, 1.322, 1.321, 1.334, 1.330, 1.340, 1.329, 1.340, 1.340, 1.348, 1.341, 1.329, 1.321, 1.337, 1.320, 1.326, 1.319]

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


