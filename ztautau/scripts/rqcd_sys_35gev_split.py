# incl no trig

from math import *

print "INCLUSIVE"
print ""
print "*******************"
print ""

print "------------------------------"
print "        NO TRIGGER"
print "------------------------------"


rqcd_i_low_val = 1.157
rqcd_i_high_val = 1.229

rqcd_i_low_topo = [1.128, 1.112, 1.105, 1.100, 1.088, 1.087, 1.084, 1.078, 1.066, 1.070, 1.065, 1.060, 1.063, 1.055, 1.039, 1.035, 1.017, 1.011, 0.997, 0.999, 0.992, 0.978, 0.982, 0.976, 0.983, 0.999, 0.998, 0.997, 0.988, 1.002, 0.995]
rqcd_i_high_topo = [1.197, 1.187, 1.179, 1.168, 1.164, 1.163, 1.172, 1.167, 1.171, 1.156, 1.150, 1.135, 1.138, 1.119, 1.106, 1.095, 1.098, 1.084, 1.078, 1.069, 1.069, 1.065, 1.051, 1.039, 1.032, 1.027, 1.027, 0.996, 0.991, 0.997, 0.992]

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

rqcd_i_low_ptvar = [1.125, 1.126, 1.125, 1.123, 1.125, 1.127, 1.125, 1.124, 1.127, 1.125, 1.122, 1.120, 1.117, 1.117, 1.118, 1.120, 1.123, 1.122, 1.126, 1.123, 1.123, 1.119, 1.118, 1.118, 1.120, 1.122, 1.119, 1.119, 1.122, 1.121, 1.119]
rqcd_i_high_ptvar = [1.191, 1.192, 1.190, 1.189, 1.189, 1.188, 1.191, 1.194, 1.193, 1.195, 1.195, 1.192, 1.194, 1.193, 1.192, 1.194, 1.197, 1.196, 1.197, 1.196, 1.196, 1.199, 1.198, 1.200, 1.202, 1.202, 1.197, 1.200, 1.201, 1.201, 1.202]

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

print " ----------------------------------- "
print "     	   25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT
rqcd_i_low_25med_val = 1.128 
rqcd_i_high_25med_val = 1.251

rqcd_i_low_topo_25med = [1.142, 1.121, 1.105, 1.098, 1.089, 1.096, 1.092, 1.080, 1.072, 1.085, 1.094, 1.089, 1.096, 1.073, 1.063, 1.070, 1.057, 1.055, 1.043, 1.045, 1.037, 1.034, 1.033, 1.025, 1.040, 1.049, 1.039, 1.020, 1.012, 1.027, 1.045]
rqcd_i_high_topo_25med = [1.203, 1.192, 1.178, 1.162, 1.149, 1.161, 1.173, 1.173, 1.165, 1.153, 1.145, 1.132, 1.131, 1.104, 1.095, 1.081, 1.086, 1.080, 1.069, 1.056, 1.062, 1.063, 1.049, 1.037, 1.013, 1.009, 1.022, 0.999, 0.983, 0.990, 0.984]

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

rqcd_i_low_ptvar_25med = [1.108, 1.103, 1.102, 1.107, 1.105, 1.109, 1.107, 1.108, 1.115, 1.111, 1.108, 1.100, 1.096, 1.097, 1.098, 1.101, 1.107, 1.106, 1.109, 1.106, 1.101, 1.098, 1.096, 1.100, 1.103, 1.106, 1.109, 1.106, 1.110, 1.110, 1.106]
rqcd_i_high_ptvar_25med = [1.180, 1.181, 1.180, 1.180, 1.180, 1.177, 1.181, 1.184, 1.183, 1.181, 1.186, 1.184, 1.190, 1.187, 1.185, 1.189, 1.193, 1.190, 1.192, 1.196, 1.197, 1.198, 1.193, 1.198, 1.197, 1.198, 1.195, 1.202, 1.197, 1.199, 1.202]

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

print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT
rqcd_i_low_35med_val = 1.165 
rqcd_i_high_35med_val = 1.239

rqcd_i_low_topo_35med = [1.156, 1.126, 1.110, 1.095, 1.031, 1.030, 1.003, 1.011, 1.215, 1.207, 1.263, 1.206, 1.303, 1.334, 1.309, 1.317, 1.256, 1.328, 1.132, 1.104, 1.079, 1.093, 1.072, 1.068, 1.088, 1.061, 1.052, 1.059]
rqcd_i_high_topo_35med = [1.179, 1.175, 1.162, 1.148, 1.131, 1.153, 1.164, 1.158, 1.148, 1.136, 1.130, 1.114, 1.112, 1.092, 1.076, 1.067, 1.056, 1.185, 1.187, 1.189, 1.187, 1.189, 1.187, 1.192, 1.191, 1.193, 1.187, 1.196]

min_rqcd_i_low_topo_35med = 2
max_rqcd_i_low_topo_35med = 0
min_rqcd_i_high_topo_35med = 2
max_rqcd_i_high_topo_35med = 0

for i in range(len(rqcd_i_low_topo_35med)):
	if rqcd_i_low_topo_35med[i]<min_rqcd_i_low_topo_35med:
		min_rqcd_i_low_topo_35med = rqcd_i_low_topo_35med[i]
	if rqcd_i_low_topo_35med[i]>max_rqcd_i_low_topo_35med:
		max_rqcd_i_low_topo_35med = rqcd_i_low_topo_35med[i]


for i in range(len(rqcd_i_high_topo_35med)):
        if rqcd_i_high_topo_35med[i]<min_rqcd_i_high_topo_35med:
                min_rqcd_i_high_topo_35med = rqcd_i_high_topo_35med[i]
        if rqcd_i_high_topo_35med[i]>max_rqcd_i_high_topo_35med:
                max_rqcd_i_high_topo_35med = rqcd_i_high_topo_35med[i]

print "TOPO_35med: sys_i_low =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)
print "TOPO_35med: sys_i_high =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)
print "TOPO_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val
print "TOPO_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val

rqcd_i_low_ptvar_35med = [1.153, 1.173, 1.187, 1.167, 1.157, 1.171, 1.140, 1.153, 1.169, 1.151, 1.125, 1.147, 1.148, 1.148, 1.130, 1.152, 1.159, 1.138, 1.132, 1.104, 1.079, 1.093, 1.072, 1.068, 1.088, 1.061, 1.052, 1.059, 1.044, 1.015, 0.984]
rqcd_i_high_ptvar_35med = [1.181, 1.185, 1.186, 1.184, 1.185, 1.182, 1.186, 1.188, 1.186, 1.185, 1.189, 1.185, 1.190, 1.189, 1.185, 1.188, 1.188, 1.185, 1.187, 1.189, 1.187, 1.189, 1.187, 1.192, 1.191, 1.193, 1.187, 1.196, 1.193, 1.192, 1.197]

min_rqcd_i_low_ptvar_35med = 2
max_rqcd_i_low_ptvar_35med = 0
min_rqcd_i_high_ptvar_35med = 2
max_rqcd_i_high_ptvar_35med = 0

for i in range(len(rqcd_i_low_ptvar_35med)):
        if rqcd_i_low_ptvar_35med[i]<min_rqcd_i_low_ptvar_35med:
                min_rqcd_i_low_ptvar_35med = rqcd_i_low_ptvar_35med[i]
        if rqcd_i_low_ptvar_35med[i]>max_rqcd_i_low_ptvar_35med:
                max_rqcd_i_low_ptvar_35med = rqcd_i_low_ptvar_35med[i]


for i in range(len(rqcd_i_high_ptvar_35med)):
        if rqcd_i_high_ptvar_35med[i]<min_rqcd_i_high_ptvar_35med:
                min_rqcd_i_high_ptvar_35med = rqcd_i_high_ptvar_35med[i]
        if rqcd_i_high_ptvar_35med[i]>max_rqcd_i_high_ptvar_35med:
                max_rqcd_i_high_ptvar_35med = rqcd_i_high_ptvar_35med[i]

print "PTVAR_35med: sys_i_low =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)
print "PTVAR_35med: sys_i_high =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)
print "PTVAR_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val
print "PTVAR_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val
print ""
print "---> total sys 35med low pt =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2), ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2))
print "---> total sys 35med high pt =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2), ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2) )
print ""
print "---> total sys 35med low pt (percentage) =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val, ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val )
print "---> total sys 35med high pt (percentage) =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val, ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val )


################################################################################################################################################################################################################

print ""
print "ONE PRONG"
print ""
print "*******************"
print ""

print " ----------------------------------- "
print "            no trigger"
print " ------------------------------------"

# LOW VS HIGH PT
rqcd_i_low_1track_val = 1.126  
rqcd_i_high_1track_val = 1.182

rqcd_i_low_topo_1track = [1.106, 1.087, 1.070, 1.065, 1.048, 1.047, 1.044, 1.037, 1.029, 1.038, 1.029, 1.022, 1.021, 1.014, 1.002, 0.997, 0.990, 0.985, 0.982, 0.991, 0.980, 0.968, 0.972, 0.966, 0.980, 0.991, 0.994, 0.999, 0.984, 1.007, 1.008]
rqcd_i_high_topo_1track = [1.163, 1.160, 1.154, 1.142, 1.139, 1.137, 1.150, 1.150, 1.148, 1.133, 1.125, 1.122, 1.122, 1.093, 1.082, 1.084, 1.094, 1.090, 1.083, 1.078, 1.084, 1.084, 1.074, 1.072, 1.078, 1.078, 1.079, 1.048, 1.044, 1.052, 1.045]

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

rqcd_i_low_ptvar_1track = [1.093, 1.093, 1.091, 1.090, 1.092, 1.094, 1.092, 1.092, 1.097, 1.093, 1.092, 1.088, 1.085, 1.085, 1.087, 1.089, 1.094, 1.090, 1.095, 1.093, 1.096, 1.092, 1.091, 1.090, 1.090, 1.093, 1.090, 1.089, 1.092, 1.095, 1.089]
rqcd_i_high_ptvar_1track = [1.151, 1.153, 1.150, 1.149, 1.149, 1.150, 1.152, 1.155, 1.154, 1.156, 1.157, 1.152, 1.154, 1.153, 1.152, 1.154, 1.156, 1.154, 1.155, 1.154, 1.154, 1.156, 1.154, 1.156, 1.155, 1.157, 1.153, 1.153, 1.155, 1.153, 1.156]

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

print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT

rqcd_i_low_1track_25med_val = 1.107  
rqcd_i_high_1track_25med_val = 1.191

rqcd_i_low_topo_1track_25med = [1.126, 1.099, 1.076, 1.069, 1.060, 1.064, 1.059, 1.046, 1.037, 1.053, 1.059, 1.051, 1.058, 1.031, 1.019, 1.023, 1.017, 1.008, 1.009, 1.014, 1.006, 1.001, 0.997, 0.994, 1.014, 1.028, 1.027, 1.008, 0.998, 1.016, 1.042]
rqcd_i_high_topo_1track_25med = [1.160, 1.156, 1.147, 1.131, 1.116, 1.128, 1.145, 1.147, 1.134, 1.126, 1.115, 1.116, 1.113, 1.081, 1.070, 1.070, 1.084, 1.088, 1.077, 1.077, 1.085, 1.088, 1.073, 1.070, 1.056, 1.051, 1.069, 1.050, 1.036, 1.049, 1.046]

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

rqcd_i_low_ptvar_1track_25med = [1.083, 1.077, 1.074, 1.081, 1.079, 1.083, 1.080, 1.080, 1.087, 1.083, 1.084, 1.078, 1.074, 1.073, 1.074, 1.077, 1.083, 1.080, 1.084, 1.084, 1.082, 1.081, 1.081, 1.084, 1.086, 1.090, 1.094, 1.095, 1.098, 1.101, 1.096]
rqcd_i_high_ptvar_1track_25med = [1.136, 1.137, 1.136, 1.136, 1.135, 1.134, 1.135, 1.139, 1.139, 1.138, 1.145, 1.142, 1.147, 1.145, 1.142, 1.147, 1.150, 1.146, 1.149, 1.152, 1.152, 1.152, 1.148, 1.152, 1.151, 1.153, 1.149, 1.151, 1.145, 1.144, 1.151]

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
i
#######################################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

rqcd_i_low_1track_35med_val = 1.130 
rqcd_i_high_1track_35med_val = 1.191

rqcd_i_low_topo_1track_35med = [1.126, 1.063, 1.048, 1.027, 0.985, 0.972, 0.954, 0.949, 1.161, 1.143, 1.163, 1.087, 1.207, 1.233, 1.233, 1.185, 1.225, 1.236, 1.255, 1.379, 1.526, 1.570, 1.623, 1.581, 1.680, 1.722, 1.815, 1.648, 1.648, 1.855, 1.792]
rqcd_i_high_topo_1track_35med = [1.144, 1.146, 1.138, 1.124, 1.104, 1.129, 1.149, 1.142, 1.126, 1.116, 1.107, 1.102, 1.104, 1.080, 1.063, 1.072, 1.076, 1.077, 1.064, 1.066, 1.067, 1.071, 1.049, 1.050, 1.022, 1.050, 1.074, 1.051, 1.040, 1.057, 1.056]

min_rqcd_i_low_topo_1track_35med = 2
max_rqcd_i_low_topo_1track_35med = 0
min_rqcd_i_high_topo_1track_35med = 2
max_rqcd_i_high_topo_1track_35med = 0

for i in range(len(rqcd_i_low_topo_1track_35med)):
	if rqcd_i_low_topo_1track_35med[i]<min_rqcd_i_low_topo_1track_35med:
		min_rqcd_i_low_topo_1track_35med = rqcd_i_low_topo_1track_35med[i]
	if rqcd_i_low_topo_1track_35med[i]>max_rqcd_i_low_topo_1track_35med:
		max_rqcd_i_low_topo_1track_35med = rqcd_i_low_topo_1track_35med[i]


for i in range(len(rqcd_i_high_topo_1track_35med)):
        if rqcd_i_high_topo_1track_35med[i]<min_rqcd_i_high_topo_1track_35med:
                min_rqcd_i_high_topo_1track_35med = rqcd_i_high_topo_1track_35med[i]
        if rqcd_i_high_topo_1track_35med[i]>max_rqcd_i_high_topo_1track_35med:
                max_rqcd_i_high_topo_1track_35med = rqcd_i_high_topo_1track_35med[i]

print "TOPO_35med: sys_i_low =", ((max_rqcd_i_low_topo_1track_35med - min_rqcd_i_low_topo_1track_35med)/2)
print "TOPO_35med: sys_i_high =", ((max_rqcd_i_high_topo_1track_35med - min_rqcd_i_high_topo_1track_35med)/2)
print "TOPO_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_35med - min_rqcd_i_low_topo_1track_35med)/2)/rqcd_i_low_1track_35med_val
print "TOPO_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_35med - min_rqcd_i_high_topo_1track_35med)/2)/rqcd_i_high_1track_35med_val

rqcd_i_low_ptvar_1track_35med = [1.163, 1.172, 1.200, 1.172, 1.153, 1.176, 1.129, 1.129, 1.154, 1.168, 1.150, 1.132, 1.166, 1.173, 1.173, 1.155, 1.179, 1.193, 1.171, 1.161, 1.139, 1.135, 1.169, 1.149, 1.146, 1.156, 1.135, 1.132, 1.135, 1.123, 1.085, 1.045]
rqcd_i_high_ptvar_1track_35med = [1.142, 1.147, 1.148, 1.148, 1.147, 1.146, 1.147, 1.147, 1.151, 1.148, 1.149, 1.154, 1.149, 1.153, 1.153, 1.149, 1.152, 1.152, 1.148, 1.151, 1.153, 1.149, 1.151, 1.150, 1.156, 1.153, 1.157, 1.150, 1.153, 1.149, 1.146, 1.155]

min_rqcd_i_low_ptvar_1track_35med = 2
max_rqcd_i_low_ptvar_1track_35med = 0
min_rqcd_i_high_ptvar_1track_35med = 2
max_rqcd_i_high_ptvar_1track_35med = 0

for i in range(len(rqcd_i_low_ptvar_1track_35med)):
        if rqcd_i_low_ptvar_1track_35med[i]<min_rqcd_i_low_ptvar_1track_35med:
                min_rqcd_i_low_ptvar_1track_35med = rqcd_i_low_ptvar_1track_35med[i]
        if rqcd_i_low_ptvar_1track_35med[i]>max_rqcd_i_low_ptvar_1track_35med:
                max_rqcd_i_low_ptvar_1track_35med = rqcd_i_low_ptvar_1track_35med[i]


for i in range(len(rqcd_i_high_ptvar_1track_35med)):
        if rqcd_i_high_ptvar_1track_35med[i]<min_rqcd_i_high_ptvar_1track_35med:
                min_rqcd_i_high_ptvar_1track_35med = rqcd_i_high_ptvar_1track_35med[i]
        if rqcd_i_high_ptvar_1track_35med[i]>max_rqcd_i_high_ptvar_1track_35med:
                max_rqcd_i_high_ptvar_1track_35med = rqcd_i_high_ptvar_1track_35med[i]

print "PTVAR_35med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_35med - min_rqcd_i_low_ptvar_1track_35med)/2)
print "PTVAR_35med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_35med - min_rqcd_i_high_ptvar_1track_35med)/2)
print "PTVAR_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_35med - min_rqcd_i_low_ptvar_1track_35med)/2)/rqcd_i_low_1track_35med_val
print "PTVAR_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_35med - min_rqcd_i_high_ptvar_1track_35med)/2)/rqcd_i_high_1track_35med_val
print ""
print "---> total sys 35med low pt =", max( ((max_rqcd_i_low_topo_1track_35med - min_rqcd_i_low_topo_1track_35med)/2), ((max_rqcd_i_low_ptvar_1track_35med - min_rqcd_i_low_ptvar_1track_35med)/2))
print "---> total sys 35med high pt =", max( ((max_rqcd_i_high_topo_1track_35med - min_rqcd_i_high_topo_1track_35med)/2), ((max_rqcd_i_high_ptvar_1track_35med - min_rqcd_i_high_ptvar_1track_35med)/2) )
print ""
print "---> total sys 35med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_35med - min_rqcd_i_low_topo_1track_35med)/2)/rqcd_i_low_1track_35med_val, ((max_rqcd_i_low_ptvar_1track_35med - min_rqcd_i_low_ptvar_1track_35med)/2)/rqcd_i_low_1track_35med_val )
print "---> total sys 35med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_35med - min_rqcd_i_high_topo_1track_35med)/2)/rqcd_i_high_1track_35med_val, ((max_rqcd_i_high_ptvar_1track_35med - min_rqcd_i_high_ptvar_1track_35med)/2)/rqcd_i_high_1track_35med_val )

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
rqcd_i_low_1track_50L1TAU12med_val = 0.917 
rqcd_i_high_1track_50L1TAU12med_val = 1.262 

rqcd_i_low_topo_1track_50L1TAU12med = [1.144, 1.113, 1.106, 1.146, 1.092, 1.048, 1.007, 1.026, 1.116, 1.159, 1.131, 1.063, 1.153, 1.103, 1.101, 1.076, 1.006, 0.968, 1.019, 1.110, 1.115, 1.127, 1.084, 1.225, 1.216, 1.339, 1.366, 1.366, 1.366, 1.789, 1.789]
rqcd_i_high_topo_1track_50L1TAU12med = [1.197, 1.194, 1.190, 1.171, 1.158, 1.171, 1.193, 1.206, 1.190, 1.164, 1.154, 1.172, 1.159, 1.139, 1.113, 1.118, 1.113, 1.155, 1.160, 1.151, 1.153, 1.167, 1.143, 1.138, 1.114, 1.068, 1.091, 1.034, 1.024, 1.028, 1.062]

min_rqcd_i_low_topo_1track_50L1TAU12med = 2
max_rqcd_i_low_topo_1track_50L1TAU12med = 0
min_rqcd_i_high_topo_1track_50L1TAU12med = 2
max_rqcd_i_high_topo_1track_50L1TAU12med = 0

for i in range(len(rqcd_i_low_topo_1track_50L1TAU12med)):
	if rqcd_i_low_topo_1track_50L1TAU12med[i]<min_rqcd_i_low_topo_1track_50L1TAU12med:
		min_rqcd_i_low_topo_1track_50L1TAU12med = rqcd_i_low_topo_1track_50L1TAU12med[i]
	if rqcd_i_low_topo_1track_50L1TAU12med[i]>max_rqcd_i_low_topo_1track_50L1TAU12med:
		max_rqcd_i_low_topo_1track_50L1TAU12med = rqcd_i_low_topo_1track_50L1TAU12med[i]


for i in range(len(rqcd_i_high_topo_1track_50L1TAU12med)):
        if rqcd_i_high_topo_1track_50L1TAU12med[i]<min_rqcd_i_high_topo_1track_50L1TAU12med:
                min_rqcd_i_high_topo_1track_50L1TAU12med = rqcd_i_high_topo_1track_50L1TAU12med[i]
        if rqcd_i_high_topo_1track_50L1TAU12med[i]>max_rqcd_i_high_topo_1track_50L1TAU12med:
                max_rqcd_i_high_topo_1track_50L1TAU12med = rqcd_i_high_topo_1track_50L1TAU12med[i]

print "TOPO_50L1TAU12med: sys_i_low =", ((max_rqcd_i_low_topo_1track_50L1TAU12med - min_rqcd_i_low_topo_1track_50L1TAU12med)/2)
print "TOPO_50L1TAU12med: sys_i_high =", ((max_rqcd_i_high_topo_1track_50L1TAU12med - min_rqcd_i_high_topo_1track_50L1TAU12med)/2)
print "TOPO_50L1TAU12med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_50L1TAU12med - min_rqcd_i_low_topo_1track_50L1TAU12med)/2)/rqcd_i_low_1track_50L1TAU12med_val
print "TOPO_50L1TAU12med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_50L1TAU12med - min_rqcd_i_high_topo_1track_50L1TAU12med)/2)/rqcd_i_high_1track_50L1TAU12med_val

rqcd_i_low_ptvar_1track_50L1TAU12med = [1.037, 1.061, 1.076, 1.069, 1.045, 1.037, 1.038, 1.067, 1.068, 1.060, 1.031, 1.041, 1.067, 1.070, 1.070, 1.082, 1.071, 1.084, 1.077, 1.067, 1.069, 1.154, 1.114, 1.137, 1.155, 1.143, 1.159, 1.167, 1.175, 1.162, 1.084] 
rqcd_i_high_ptvar_1track_50L1TAU12med = [1.183, 1.186, 1.189, 1.185, 1.185, 1.190, 1.191, 1.197, 1.192, 1.196, 1.198, 1.193, 1.195, 1.197, 1.191, 1.194, 1.195, 1.191, 1.195, 1.192, 1.186, 1.190, 1.186, 1.192, 1.183, 1.185, 1.176, 1.179, 1.175, 1.172, 1.181]

min_rqcd_i_low_ptvar_1track_50L1TAU12med = 2
max_rqcd_i_low_ptvar_1track_50L1TAU12med = 0
min_rqcd_i_high_ptvar_1track_50L1TAU12med = 2
max_rqcd_i_high_ptvar_1track_50L1TAU12med = 0

for i in range(len(rqcd_i_low_ptvar_1track_50L1TAU12med)):
        if rqcd_i_low_ptvar_1track_50L1TAU12med[i]<min_rqcd_i_low_ptvar_1track_50L1TAU12med:
                min_rqcd_i_low_ptvar_1track_50L1TAU12med = rqcd_i_low_ptvar_1track_50L1TAU12med[i]
        if rqcd_i_low_ptvar_1track_50L1TAU12med[i]>max_rqcd_i_low_ptvar_1track_50L1TAU12med:
                max_rqcd_i_low_ptvar_1track_50L1TAU12med = rqcd_i_low_ptvar_1track_50L1TAU12med[i]


for i in range(len(rqcd_i_high_ptvar_1track_50L1TAU12med)):
        if rqcd_i_high_ptvar_1track_50L1TAU12med[i]<min_rqcd_i_high_ptvar_1track_50L1TAU12med:
                min_rqcd_i_high_ptvar_1track_50L1TAU12med = rqcd_i_high_ptvar_1track_50L1TAU12med[i]
        if rqcd_i_high_ptvar_1track_50L1TAU12med[i]>max_rqcd_i_high_ptvar_1track_50L1TAU12med:
                max_rqcd_i_high_ptvar_1track_50L1TAU12med = rqcd_i_high_ptvar_1track_50L1TAU12med[i]

print "PTVAR_50L1TAU12med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_50L1TAU12med - min_rqcd_i_low_ptvar_1track_50L1TAU12med)/2)
print "PTVAR_50L1TAU12med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_50L1TAU12med - min_rqcd_i_high_ptvar_1track_50L1TAU12med)/2)
print "PTVAR_50L1TAU12med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_50L1TAU12med - min_rqcd_i_low_ptvar_1track_50L1TAU12med)/2)/rqcd_i_low_1track_50L1TAU12med_val
print "PTVAR_50L1TAU12med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_50L1TAU12med - min_rqcd_i_high_ptvar_1track_50L1TAU12med)/2)/rqcd_i_high_1track_50L1TAU12med_val
print ""
print "---> total sys 50L1TAU12med low pt =", max( ((max_rqcd_i_low_topo_1track_50L1TAU12med - min_rqcd_i_low_topo_1track_50L1TAU12med)/2), ((max_rqcd_i_low_ptvar_1track_50L1TAU12med - min_rqcd_i_low_ptvar_1track_50L1TAU12med)/2))
print "---> total sys 50L1TAU12med high pt =", max( ((max_rqcd_i_high_topo_1track_50L1TAU12med - min_rqcd_i_high_topo_1track_50L1TAU12med)/2), ((max_rqcd_i_high_ptvar_1track_50L1TAU12med - min_rqcd_i_high_ptvar_1track_50L1TAU12med)/2) )
print ""
print "---> total sys 50L1TAU12med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_50L1TAU12med - min_rqcd_i_low_topo_1track_50L1TAU12med)/2)/rqcd_i_low_1track_50L1TAU12med_val, ((max_rqcd_i_low_ptvar_1track_50L1TAU12med - min_rqcd_i_low_ptvar_1track_50L1TAU12med)/2)/rqcd_i_low_1track_50L1TAU12med_val )
print "---> total sys 50L1TAU12med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_50L1TAU12med - min_rqcd_i_high_topo_1track_50L1TAU12med)/2)/rqcd_i_high_1track_50L1TAU12med_val, ((max_rqcd_i_high_ptvar_1track_50L1TAU12med - min_rqcd_i_high_ptvar_1track_50L1TAU12med)/2)/rqcd_i_high_1track_50L1TAU12med_val )


################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
rqcd_i_low_1track_80med_val = 1.163 
rqcd_i_high_1track_80med_val = 1.204

rqcd_i_low_topo_1track_80med = [1.055, 1.017, 1.107, 1.213, 1.107, 1.169, 1.195, 1.409, 1.665, 1.574, 1.331, 1.257, 1.414, 1.164, 0.789, 1.052, 1.063, 0.863, 0.924, 0.924, 0.924, 0.924, 1.539, 1.539, 1.539, 2.309, 2.309, 2.309, 2.309, 2.309, 2.309]
rqcd_i_high_topo_1track_80med = [1.158, 1.176, 1.157, 1.141, 1.155, 1.158, 1.180, 1.214, 1.181, 1.142, 1.115, 1.134, 1.125, 1.086, 1.050, 1.084, 1.062, 1.149, 1.147, 1.123, 1.085, 1.076, 1.062, 1.072, 1.055, 1.079, 1.101, 1.047, 1.029, 1.037, 1.067]

min_rqcd_i_low_topo_1track_80med = 2
max_rqcd_i_low_topo_1track_80med = 0
min_rqcd_i_high_topo_1track_80med = 2
max_rqcd_i_high_topo_1track_80med = 0

for i in range(len(rqcd_i_low_topo_1track_80med)):
	if rqcd_i_low_topo_1track_80med[i]<min_rqcd_i_low_topo_1track_80med:
		min_rqcd_i_low_topo_1track_80med = rqcd_i_low_topo_1track_80med[i]
	if rqcd_i_low_topo_1track_80med[i]>max_rqcd_i_low_topo_1track_80med:
		max_rqcd_i_low_topo_1track_80med = rqcd_i_low_topo_1track_80med[i]


for i in range(len(rqcd_i_high_topo_1track_80med)):
        if rqcd_i_high_topo_1track_80med[i]<min_rqcd_i_high_topo_1track_80med:
                min_rqcd_i_high_topo_1track_80med = rqcd_i_high_topo_1track_80med[i]
        if rqcd_i_high_topo_1track_80med[i]>max_rqcd_i_high_topo_1track_80med:
                max_rqcd_i_high_topo_1track_80med = rqcd_i_high_topo_1track_80med[i]

print "TOPO_80med: sys_i_low =", ((max_rqcd_i_low_topo_1track_80med - min_rqcd_i_low_topo_1track_80med)/2)
print "TOPO_80med: sys_i_high =", ((max_rqcd_i_high_topo_1track_80med - min_rqcd_i_high_topo_1track_80med)/2)
print "TOPO_80med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_80med - min_rqcd_i_low_topo_1track_80med)/2)/rqcd_i_low_1track_80med_val
print "TOPO_80med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_80med - min_rqcd_i_high_topo_1track_80med)/2)/rqcd_i_high_1track_80med_val

rqcd_i_low_ptvar_1track_80med = [0.985, 1.014, 0.971, 0.971, 0.971, 0.941, 0.970, 1.000, 1.031, 1.031, 1.065, 1.078, 1.114, 1.153, 1.109, 1.112, 1.154, 1.154, 1.117, 1.079, 1.121, 1.167, 1.167, 1.098, 1.098, 1.098, 1.098, 1.145, 1.145, 1.102, 1.060]
rqcd_i_high_ptvar_1track_80med = [1.176, 1.173, 1.177, 1.175, 1.181, 1.191, 1.191, 1.193, 1.197, 1.208, 1.208, 1.213, 1.211, 1.205, 1.210, 1.214, 1.212, 1.212, 1.209, 1.207, 1.203, 1.210, 1.212, 1.221, 1.214, 1.207, 1.199, 1.204, 1.200, 1.194, 1.206]

min_rqcd_i_low_ptvar_1track_80med = 2
max_rqcd_i_low_ptvar_1track_80med = 0
min_rqcd_i_high_ptvar_1track_80med = 2
max_rqcd_i_high_ptvar_1track_80med = 0

for i in range(len(rqcd_i_low_ptvar_1track_80med)):
        if rqcd_i_low_ptvar_1track_80med[i]<min_rqcd_i_low_ptvar_1track_80med:
                min_rqcd_i_low_ptvar_1track_80med = rqcd_i_low_ptvar_1track_80med[i]
        if rqcd_i_low_ptvar_1track_80med[i]>max_rqcd_i_low_ptvar_1track_80med:
                max_rqcd_i_low_ptvar_1track_80med = rqcd_i_low_ptvar_1track_80med[i]


for i in range(len(rqcd_i_high_ptvar_1track_80med)):
        if rqcd_i_high_ptvar_1track_80med[i]<min_rqcd_i_high_ptvar_1track_80med:
                min_rqcd_i_high_ptvar_1track_80med = rqcd_i_high_ptvar_1track_80med[i]
        if rqcd_i_high_ptvar_1track_80med[i]>max_rqcd_i_high_ptvar_1track_80med:
                max_rqcd_i_high_ptvar_1track_80med = rqcd_i_high_ptvar_1track_80med[i]

print "PTVAR_80med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_80med - min_rqcd_i_low_ptvar_1track_80med)/2)
print "PTVAR_80med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_80med - min_rqcd_i_high_ptvar_1track_80med)/2)
print "PTVAR_80med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_80med - min_rqcd_i_low_ptvar_1track_80med)/2)/rqcd_i_low_1track_80med_val
print "PTVAR_80med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_80med - min_rqcd_i_high_ptvar_1track_80med)/2)/rqcd_i_high_1track_80med_val
print ""
print "---> total sys 80med low pt =", max( ((max_rqcd_i_low_topo_1track_80med - min_rqcd_i_low_topo_1track_80med)/2), ((max_rqcd_i_low_ptvar_1track_80med - min_rqcd_i_low_ptvar_1track_80med)/2))
print "---> total sys 80med high pt =", max( ((max_rqcd_i_high_topo_1track_80med - min_rqcd_i_high_topo_1track_80med)/2), ((max_rqcd_i_high_ptvar_1track_80med - min_rqcd_i_high_ptvar_1track_80med)/2) )
print ""
print "---> total sys 80med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_80med - min_rqcd_i_low_topo_1track_80med)/2)/rqcd_i_low_1track_80med_val, ((max_rqcd_i_low_ptvar_1track_80med - min_rqcd_i_low_ptvar_1track_80med)/2)/rqcd_i_low_1track_80med_val )
print "---> total sys 80med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_80med - min_rqcd_i_high_topo_1track_80med)/2)/rqcd_i_high_1track_80med_val, ((max_rqcd_i_high_ptvar_1track_80med - min_rqcd_i_high_ptvar_1track_80med)/2)/rqcd_i_high_1track_80med_val )

################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
rqcd_i_low_1track_80L1TAU60med_val = 0.763 
rqcd_i_high_1track_80L1TAU60med_val = 1.205

rqcd_i_low_topo_1track_80L1TAU60med = [0.778, 0.817, 0.908, 0.956, 0.890, 0.953, 0.971, 1.062, 1.327, 1.202, 1.088, 0.936, 1.124, 0.924, 0.524, 0.873, 0.809, 0.809, 0.809, 0.809, 0.809, 0.809, 1.618, 1.618, 1.618, 1.618, 1.618, 1.618, 1.618, 1.618, 1.618]
rqcd_i_high_topo_1track_80L1TAU60med = [1.134, 1.163, 1.149, 1.136, 1.148, 1.155, 1.167, 1.191, 1.173, 1.136, 1.117, 1.154, 1.141, 1.119, 1.081, 1.120, 1.096, 1.185, 1.206, 1.170, 1.131, 1.129, 1.134, 1.143, 1.129, 1.130, 1.162, 1.100, 1.074, 1.078, 1.128]

min_rqcd_i_low_topo_1track_80L1TAU60med = 2
max_rqcd_i_low_topo_1track_80L1TAU60med = 0
min_rqcd_i_high_topo_1track_80L1TAU60med = 2
max_rqcd_i_high_topo_1track_80L1TAU60med = 0

for i in range(len(rqcd_i_low_topo_1track_80L1TAU60med)):
	if rqcd_i_low_topo_1track_80L1TAU60med[i]<min_rqcd_i_low_topo_1track_80L1TAU60med:
		min_rqcd_i_low_topo_1track_80L1TAU60med = rqcd_i_low_topo_1track_80L1TAU60med[i]
	if rqcd_i_low_topo_1track_80L1TAU60med[i]>max_rqcd_i_low_topo_1track_80L1TAU60med:
		max_rqcd_i_low_topo_1track_80L1TAU60med = rqcd_i_low_topo_1track_80L1TAU60med[i]


for i in range(len(rqcd_i_high_topo_1track_80L1TAU60med)):
        if rqcd_i_high_topo_1track_80L1TAU60med[i]<min_rqcd_i_high_topo_1track_80L1TAU60med:
                min_rqcd_i_high_topo_1track_80L1TAU60med = rqcd_i_high_topo_1track_80L1TAU60med[i]
        if rqcd_i_high_topo_1track_80L1TAU60med[i]>max_rqcd_i_high_topo_1track_80L1TAU60med:
                max_rqcd_i_high_topo_1track_80L1TAU60med = rqcd_i_high_topo_1track_80L1TAU60med[i]

print "TOPO_80L1TAU60med: sys_i_low =", ((max_rqcd_i_low_topo_1track_80L1TAU60med - min_rqcd_i_low_topo_1track_80L1TAU60med)/2)
print "TOPO_80L1TAU60med: sys_i_high =", ((max_rqcd_i_high_topo_1track_80L1TAU60med - min_rqcd_i_high_topo_1track_80L1TAU60med)/2)
print "TOPO_80L1TAU60med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_80L1TAU60med - min_rqcd_i_low_topo_1track_80L1TAU60med)/2)/rqcd_i_low_1track_80L1TAU60med_val
print "TOPO_80L1TAU60med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_80L1TAU60med - min_rqcd_i_high_topo_1track_80L1TAU60med)/2)/rqcd_i_high_1track_80L1TAU60med_val

rqcd_i_low_ptvar_1track_80L1TAU60med = [0.843, 0.843, 0.828, 0.828, 0.828, 0.792, 0.822, 0.853, 0.888, 0.888, 0.888, 0.925, 0.941, 0.982, 0.982, 0.972, 0.970, 0.970, 0.925, 0.879, 0.921, 0.921, 0.921, 0.874, 0.874, 0.874, 0.874, 0.917, 0.917, 0.867, 0.817]
rqcd_i_high_ptvar_1track_80L1TAU60med = [1.188, 1.185, 1.192, 1.192, 1.201, 1.212, 1.214, 1.220, 1.225, 1.237, 1.238, 1.236, 1.238, 1.243, 1.235, 1.235, 1.240, 1.234, 1.233, 1.231, 1.226, 1.228, 1.230, 1.231, 1.226, 1.222, 1.218, 1.218, 1.211, 1.213, 1.221]

min_rqcd_i_low_ptvar_1track_80L1TAU60med = 2
max_rqcd_i_low_ptvar_1track_80L1TAU60med = 0
min_rqcd_i_high_ptvar_1track_80L1TAU60med = 2
max_rqcd_i_high_ptvar_1track_80L1TAU60med = 0

for i in range(len(rqcd_i_low_ptvar_1track_80L1TAU60med)):
        if rqcd_i_low_ptvar_1track_80L1TAU60med[i]<min_rqcd_i_low_ptvar_1track_80L1TAU60med:
                min_rqcd_i_low_ptvar_1track_80L1TAU60med = rqcd_i_low_ptvar_1track_80L1TAU60med[i]
        if rqcd_i_low_ptvar_1track_80L1TAU60med[i]>max_rqcd_i_low_ptvar_1track_80L1TAU60med:
                max_rqcd_i_low_ptvar_1track_80L1TAU60med = rqcd_i_low_ptvar_1track_80L1TAU60med[i]


for i in range(len(rqcd_i_high_ptvar_1track_80L1TAU60med)):
        if rqcd_i_high_ptvar_1track_80L1TAU60med[i]<min_rqcd_i_high_ptvar_1track_80L1TAU60med:
                min_rqcd_i_high_ptvar_1track_80L1TAU60med = rqcd_i_high_ptvar_1track_80L1TAU60med[i]
        if rqcd_i_high_ptvar_1track_80L1TAU60med[i]>max_rqcd_i_high_ptvar_1track_80L1TAU60med:
                max_rqcd_i_high_ptvar_1track_80L1TAU60med = rqcd_i_high_ptvar_1track_80L1TAU60med[i]

print "PTVAR_80L1TAU60med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_80L1TAU60med - min_rqcd_i_low_ptvar_1track_80L1TAU60med)/2)
print "PTVAR_80L1TAU60med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_80L1TAU60med - min_rqcd_i_high_ptvar_1track_80L1TAU60med)/2)
print "PTVAR_80L1TAU60med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_80L1TAU60med - min_rqcd_i_low_ptvar_1track_80L1TAU60med)/2)/rqcd_i_low_1track_80L1TAU60med_val
print "PTVAR_80L1TAU60med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_80L1TAU60med - min_rqcd_i_high_ptvar_1track_80L1TAU60med)/2)/rqcd_i_high_1track_80L1TAU60med_val
print ""
print "---> total sys 80L1TAU60med low pt =", max( ((max_rqcd_i_low_topo_1track_80L1TAU60med - min_rqcd_i_low_topo_1track_80L1TAU60med)/2), ((max_rqcd_i_low_ptvar_1track_80L1TAU60med - min_rqcd_i_low_ptvar_1track_80L1TAU60med)/2))
print "---> total sys 80L1TAU60med high pt =", max( ((max_rqcd_i_high_topo_1track_80L1TAU60med - min_rqcd_i_high_topo_1track_80L1TAU60med)/2), ((max_rqcd_i_high_ptvar_1track_80L1TAU60med - min_rqcd_i_high_ptvar_1track_80L1TAU60med)/2) )
print ""
print "---> total sys 80L1TAU60med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_80L1TAU60med - min_rqcd_i_low_topo_1track_80L1TAU60med)/2)/rqcd_i_low_1track_80L1TAU60med_val, ((max_rqcd_i_low_ptvar_1track_80L1TAU60med - min_rqcd_i_low_ptvar_1track_80L1TAU60med)/2)/rqcd_i_low_1track_80L1TAU60med_val )
print "---> total sys 80L1TAU60med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_80L1TAU60med - min_rqcd_i_high_topo_1track_80L1TAU60med)/2)/rqcd_i_high_1track_80L1TAU60med_val, ((max_rqcd_i_high_ptvar_1track_80L1TAU60med - min_rqcd_i_high_ptvar_1track_80L1TAU60med)/2)/rqcd_i_high_1track_80L1TAU60med_val )


"""
# ----------------------------------- #
#     	  ptonly1Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_ptonly1Track_val =  
rqcd_i_high_ptonly1Track_val = 

rqcd_i_low_topo_ptonly1Track = [1.118, 1.097, 1.079, 1.067, 1.053, 1.054, 1.044, 1.037, 1.031, 1.034, 1.037, 1.037, 1.031, 1.033, 1.013, 1.006, 1.006, 0.994, 0.992, 0.985, 0.997, 0.987, 0.976, 0.978, 0.976, ]
rqcd_i_high_topo_ptonly1Track = [1.155, 1.152, 1.145, 1.130, 1.124, 1.128, 1.140, 1.142, 1.139, 1.125, 1.115, 1.115, 1.114, 1.113, 1.086, 1.074, 1.075, 1.086, 1.081, 1.076, 1.072, 1.078, 1.076, 1.063, 1.065, ]

min_rqcd_i_low_topo_ptonly1Track = 2
max_rqcd_i_low_topo_ptonly1Track = 0
min_rqcd_i_high_topo_ptonly1Track = 2
max_rqcd_i_high_topo_ptonly1Track = 0

for i in range(len(rqcd_i_low_topo_ptonly1Track)):
	if rqcd_i_low_topo_ptonly1Track[i]<min_rqcd_i_low_topo_ptonly:
		min_rqcd_i_low_topo_ptonly1Track = rqcd_i_low_topo_ptonly[i]
	if rqcd_i_low_topo_ptonly1Track[i]>max_rqcd_i_low_topo_ptonly:
		max_rqcd_i_low_topo_ptonly1Track = rqcd_i_low_topo_ptonly[i]


for i in range(len(rqcd_i_high_topo_ptonly1Track)):
        if rqcd_i_high_topo_ptonly1Track[i]<min_rqcd_i_high_topo_ptonly:
                min_rqcd_i_high_topo_ptonly1Track = rqcd_i_high_topo_ptonly[i]
        if rqcd_i_high_topo_ptonly1Track[i]>max_rqcd_i_high_topo_ptonly:
                max_rqcd_i_high_topo_ptonly1Track = rqcd_i_high_topo_ptonly[i]

print "TOPO_ptonly1Track: sys_i_low =", ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)
print "TOPO_ptonly1Track: sys_i_high =", ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)
print "TOPO_ptonly1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)/rqcd_i_low_ptonly_val
print "TOPO_ptonly1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)/rqcd_i_high_ptonly_val

rqcd_i_low_ptvar_ptonly1Track = [1.088, 1.087, 1.085, 1.089, 1.090, 1.095, 1.094, 1.094, 1.097, 1.091, 1.089, 1.086, 1.083, 1.084, 1.082, 1.086, 1.090, 1.086, 1.091, 1.090, 1.093, 1.090, 1.089, 1.089, 1.091, 1.094, 1.093, 1.092, 1.093, 1.092, 1.094, 1.095, 1.094]
rqcd_i_high_ptvar_ptonly1Track = [1.140, 1.142, 1.139, 1.139, 1.139, 1.140, 1.142, 1.145, 1.143, 1.144, 1.148, 1.143, 1.146, 1.147, 1.145, 1.147, 1.150, 1.149, 1.150, 1.150, 1.151, 1.152, 1.150, 1.150, 1.149, 1.149, 1.145, 1.146, 1.145, 1.146, 1.148, 1.148, 1.153]

min_rqcd_i_low_ptvar_ptonly1Track = 2
max_rqcd_i_low_ptvar_ptonly1Track = 0
min_rqcd_i_high_ptvar_ptonly1Track = 2
max_rqcd_i_high_ptvar_ptonly1Track = 0

for i in range(len(rqcd_i_low_ptvar_ptonly1Track)):
        if rqcd_i_low_ptvar_ptonly1Track[i]<min_rqcd_i_low_ptvar_ptonly:
                min_rqcd_i_low_ptvar_ptonly1Track = rqcd_i_low_ptvar_ptonly[i]
        if rqcd_i_low_ptvar_ptonly1Track[i]>max_rqcd_i_low_ptvar_ptonly:
                max_rqcd_i_low_ptvar_ptonly1Track = rqcd_i_low_ptvar_ptonly[i]


for i in range(len(rqcd_i_high_ptvar_ptonly1Track)):
        if rqcd_i_high_ptvar_ptonly1Track[i]<min_rqcd_i_high_ptvar_ptonly:
                min_rqcd_i_high_ptvar_ptonly1Track = rqcd_i_high_ptvar_ptonly[i]
        if rqcd_i_high_ptvar_ptonly1Track[i]>max_rqcd_i_high_ptvar_ptonly:
                max_rqcd_i_high_ptvar_ptonly1Track = rqcd_i_high_ptvar_ptonly[i]

print "PTVAR_ptonly1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)
print "PTVAR_ptonly1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)
print "PTVAR_ptonly1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)/rqcd_i_low_ptonly_val
print "PTVAR_ptonly1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)/rqcd_i_high_ptonly_val
print ""
print "---> total sys ptonly1Track low pt =", max( ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2), ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2))
print "---> total sys ptonly1Track high pt =", max( ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2), ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2) )
print ""
print "---> total sys ptonly1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)/rqcd_i_low_ptonly_val, ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)/rqcd_i_low_ptonly_val )
print "---> total sys ptonly1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)/rqcd_i_high_ptonly_val, ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)/rqcd_i_high_ptonly_val )


# ----------------------------------- #
#     	   tracktwo1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_tracktwo1Track_val =  
rqcd_i_high_tracktwo1Track_val = 

rqcd_i_low_topo_tracktwo1Track = [1.145, 1.119, 1.098, 1.093, 1.080, 1.078, 1.068, 1.059, 1.049, 1.056, 1.059, 1.050, 1.055, 1.031, 1.022, 1.023, 1.010, 1.005, 0.998, 1.006, 1.000, 0.987, 0.988, 0.993, 1.016, 1.032, 1.043, 1.033, 1.022, 1.046, 1.057]
rqcd_i_high_topo_tracktwo1Track = [1.156, 1.152, 1.146, 1.130, 1.123, 1.131, 1.148, 1.148, 1.139, 1.126, 1.118, 1.116, 1.116, 1.087, 1.072, 1.071, 1.083, 1.078, 1.069, 1.071, 1.080, 1.083, 1.071, 1.074, 1.066, 1.061, 1.068, 1.051, 1.040, 1.051, 1.038]

min_rqcd_i_low_topo_tracktwo1Track = 2
max_rqcd_i_low_topo_tracktwo1Track = 0
min_rqcd_i_high_topo_tracktwo1Track = 2
max_rqcd_i_high_topo_tracktwo1Track = 0

for i in range(len(rqcd_i_low_topo_tracktwo1Track)):
	if rqcd_i_low_topo_tracktwo1Track[i]<min_rqcd_i_low_topo_35med:
		min_rqcd_i_low_topo_tracktwo1Track = rqcd_i_low_topo_35med[i]
	if rqcd_i_low_topo_tracktwo1Track[i]>max_rqcd_i_low_topo_35med:
		max_rqcd_i_low_topo_tracktwo1Track = rqcd_i_low_topo_35med[i]


for i in range(len(rqcd_i_high_topo_tracktwo1Track)):
        if rqcd_i_high_topo_tracktwo1Track[i]<min_rqcd_i_high_topo_35med:
                min_rqcd_i_high_topo_tracktwo1Track = rqcd_i_high_topo_35med[i]
        if rqcd_i_high_topo_tracktwo1Track[i]>max_rqcd_i_high_topo_35med:
                max_rqcd_i_high_topo_tracktwo1Track = rqcd_i_high_topo_35med[i]

print "TOPO_tracktwo1Track: sys_i_low =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)
print "TOPO_tracktwo1Track: sys_i_high =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)
print "TOPO_tracktwo1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val
print "TOPO_tracktwo1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val

rqcd_i_low_ptvar_tracktwo1Track = [1.104, 1.101, 1.099, 1.105, 1.107, 1.110, 1.110, 1.109, 1.114, 1.109, 1.107, 1.101, 1.097, 1.097, 1.098, 1.102, 1.108, 1.105, 1.110, 1.109, 1.110, 1.107, 1.109, 1.111, 1.112, 1.115, 1.118, 1.121, 1.122, 1.122, 1.118]
rqcd_i_high_ptvar_tracktwo1Track = [1.137, 1.139, 1.137, 1.139, 1.139, 1.141, 1.142, 1.146, 1.144, 1.144, 1.149, 1.145, 1.150, 1.149, 1.147, 1.152, 1.155, 1.152, 1.154, 1.156, 1.158, 1.159, 1.157, 1.159, 1.158, 1.157, 1.152, 1.154, 1.152, 1.150, 1.157]

min_rqcd_i_low_ptvar_tracktwo1Track = 2
max_rqcd_i_low_ptvar_tracktwo1Track = 0
min_rqcd_i_high_ptvar_tracktwo1Track = 2
max_rqcd_i_high_ptvar_tracktwo1Track = 0

for i in range(len(rqcd_i_low_ptvar_tracktwo1Track)):
        if rqcd_i_low_ptvar_tracktwo1Track[i]<min_rqcd_i_low_ptvar_35med:
                min_rqcd_i_low_ptvar_tracktwo1Track = rqcd_i_low_ptvar_35med[i]
        if rqcd_i_low_ptvar_tracktwo1Track[i]>max_rqcd_i_low_ptvar_35med:
                max_rqcd_i_low_ptvar_tracktwo1Track = rqcd_i_low_ptvar_35med[i]


for i in range(len(rqcd_i_high_ptvar_tracktwo1Track)):
        if rqcd_i_high_ptvar_tracktwo1Track[i]<min_rqcd_i_high_ptvar_35med:
                min_rqcd_i_high_ptvar_tracktwo1Track = rqcd_i_high_ptvar_35med[i]
        if rqcd_i_high_ptvar_tracktwo1Track[i]>max_rqcd_i_high_ptvar_35med:
                max_rqcd_i_high_ptvar_tracktwo1Track = rqcd_i_high_ptvar_35med[i]

print "PTVAR_tracktwo1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)
print "PTVAR_tracktwo1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)
print "PTVAR_tracktwo1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val
print "PTVAR_tracktwo1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val
print ""
print "---> total sys tracktwo1Track low pt =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2), ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2))
print "---> total sys tracktwo1Track high pt =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2), ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2) )
print ""
print "---> total sys tracktwo1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val, ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val )
print "---> total sys tracktwo1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val, ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val )


# ----------------------------------- #
#     	   L1TAU12IM1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_L1TAU12IM1Track_val =  
rqcd_i_high_L1TAU12IM1Track_val = 

rqcd_i_low_topo_L1TAU12IM1Track = [1.114, 1.094, 1.077, 1.065, 1.049, 1.049, 1.045, 1.039, 1.032, 1.035, 1.034, 1.027, 1.029, 1.010, 1.001, 1.002, 1.002, 0.991, 0.988, 0.979, 0.990, 0.982, 0.970, 0.970, 0.966, 0.982, 0.996, 1.005, 1.009, 0.999, 1.023, 1.029]
rqcd_i_high_topo_L1TAU12IM1Track = [1.154, 1.151, 1.145, 1.129, 1.123, 1.127, 1.140, 1.141, 1.138, 1.124, 1.115, 1.113, 1.111, 1.084, 1.072, 1.073, 1.073, 1.084, 1.078, 1.073, 1.069, 1.075, 1.072, 1.059, 1.060, 1.063, 1.064, 1.060, 1.035, 1.032, 1.042, 1.034]

min_rqcd_i_low_topo_L1TAU12IM1Track = 2
max_rqcd_i_low_topo_L1TAU12IM1Track = 0
min_rqcd_i_high_topo_L1TAU12IM1Track = 2
max_rqcd_i_high_topo_L1TAU12IM1Track = 0

for i in range(len(rqcd_i_low_topo_L1TAU12IM1Track)):
	if rqcd_i_low_topo_L1TAU12IM1Track[i]<min_rqcd_i_low_topo_35med:
		min_rqcd_i_low_topo_L1TAU12IM1Track = rqcd_i_low_topo_35med[i]
	if rqcd_i_low_topo_L1TAU12IM1Track[i]>max_rqcd_i_low_topo_35med:
		max_rqcd_i_low_topo_L1TAU12IM1Track = rqcd_i_low_topo_35med[i]


for i in range(len(rqcd_i_high_topo_L1TAU12IM1Track)):
        if rqcd_i_high_topo_L1TAU12IM1Track[i]<min_rqcd_i_high_topo_35med:
                min_rqcd_i_high_topo_L1TAU12IM1Track = rqcd_i_high_topo_35med[i]
        if rqcd_i_high_topo_L1TAU12IM1Track[i]>max_rqcd_i_high_topo_35med:
                max_rqcd_i_high_topo_L1TAU12IM1Track = rqcd_i_high_topo_35med[i]

print "TOPO_L1TAU12IM1Track: sys_i_low =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)
print "TOPO_L1TAU12IM1Track: sys_i_high =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)
print "TOPO_L1TAU12IM1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val
print "TOPO_L1TAU12IM1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val

rqcd_i_low_ptvar_L1TAU12IM1Track = [1.087, 1.086, 1.085, 1.087, 1.089, 1.093, 1.092, 1.092, 1.095, 1.091, 1.088, 1.083, 1.081, 1.081, 1.080, 1.083, 1.088, 1.084, 1.088, 1.086, 1.089, 1.086, 1.086, 1.087, 1.089, 1.091, 1.090, 1.089, 1.091, 1.093, 1.089]
rqcd_i_high_ptvar_L1TAU12IM1Track = [1.140, 1.142, 1.139, 1.139, 1.139, 1.140, 1.142, 1.145, 1.143, 1.145, 1.148, 1.144, 1.147, 1.147, 1.146, 1.148, 1.150, 1.149, 1.150, 1.150, 1.151, 1.152, 1.150, 1.150, 1.149, 1.149, 1.145, 1.146, 1.148, 1.147, 1.152]

min_rqcd_i_low_ptvar_L1TAU12IM1Track = 2
max_rqcd_i_low_ptvar_L1TAU12IM1Track = 0
min_rqcd_i_high_ptvar_L1TAU12IM1Track = 2
max_rqcd_i_high_ptvar_L1TAU12IM1Track = 0

for i in range(len(rqcd_i_low_ptvar_L1TAU12IM1Track)):
        if rqcd_i_low_ptvar_L1TAU12IM1Track[i]<min_rqcd_i_low_ptvar_35med:
                min_rqcd_i_low_ptvar_L1TAU12IM1Track = rqcd_i_low_ptvar_35med[i]
        if rqcd_i_low_ptvar_L1TAU12IM1Track[i]>max_rqcd_i_low_ptvar_35med:
                max_rqcd_i_low_ptvar_L1TAU12IM1Track = rqcd_i_low_ptvar_35med[i]


for i in range(len(rqcd_i_high_ptvar_L1TAU12IM1Track)):
        if rqcd_i_high_ptvar_L1TAU12IM1Track[i]<min_rqcd_i_high_ptvar_35med:
                min_rqcd_i_high_ptvar_L1TAU12IM1Track = rqcd_i_high_ptvar_35med[i]
        if rqcd_i_high_ptvar_L1TAU12IM1Track[i]>max_rqcd_i_high_ptvar_35med:
                max_rqcd_i_high_ptvar_L1TAU12IM1Track = rqcd_i_high_ptvar_35med[i]

print "PTVAR_L1TAU12IM1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)
print "PTVAR_L1TAU12IM1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)
print "PTVAR_L1TAU12IM1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val
print "PTVAR_L1TAU12IM1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val
print ""
print "---> total sys L1TAU12IM1Track low pt =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2), ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2))
print "---> total sys L1TAU12IM1Track high pt =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2), ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2) )
print ""
print "---> total sys L1TAU12IM1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val, ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val )
print "---> total sys L1TAU12IM1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val, ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val )

"""

###########################################################################################################################################################################################################

print ""
print "THREE PRONG"
print ""
print "*******************"
print ""


print " ----------------------------------- "
print "            no trigger"
print " ------------------------------------"
# LOW VS HIGH PT
rqcd_i_low_3track_val = 1.243 
rqcd_i_high_3track_val = 1.438

rqcd_i_low_topo_3track = [1.184, 1.176, 1.203, 1.199, 1.204, 1.203, 1.202, 1.200, 1.176, 1.167, 1.173, 1.175, 1.189, 1.176, 1.147, 1.144, 1.094, 1.085, 1.039, 1.019, 1.028, 1.007, 1.009, 1.004, 0.987, 1.023, 1.010, 0.993, 1.000, 0.990, 0.958, ]
rqcd_i_high_topo_3track = [1.335, 1.294, 1.277, 1.271, 1.259, 1.268, 1.257, 1.230, 1.267, 1.250, 1.257, 1.183, 1.197, 1.224, 1.202, 1.131, 1.095, 1.038, 1.033, 1.005, 0.976, 0.952, 0.925, 0.871, 0.807, 0.784, 0.775, 0.740, 0.731, 0.727, 0.725]

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

rqcd_i_low_ptvar_3track = [1.215, 1.222, 1.223, 1.218, 1.219, 1.222, 1.219, 1.213, 1.214, 1.215, 1.207, 1.209, 1.209, 1.209, 1.207, 1.209, 1.206, 1.212, 1.213, 1.209, 1.199, 1.194, 1.195, 1.197, 1.206, 1.204, 1.201, 1.203, 1.205, 1.194, 1.201]
rqcd_i_high_ptvar_3track = [1.372, 1.369, 1.374, 1.372, 1.373, 1.360, 1.369, 1.373, 1.377, 1.376, 1.374, 1.373, 1.379, 1.377, 1.382, 1.382, 1.389, 1.391, 1.391, 1.394, 1.398, 1.408, 1.408, 1.411, 1.422, 1.416, 1.407, 1.425, 1.421, 1.434, 1.422]

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
print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"
# LOW VS HIGH PT
rqcd_i_low_3track_25med_val = 1.256 
rqcd_i_high_3track_25med_val = 1.577

rqcd_i_low_topo_3track_25med = [1.250, 1.274, 1.317, 1.310, 1.304, 1.339, 1.349, 1.345,1.351, 1.342, 1.370, 1.407, 1.402, 1.409, 1.413, 1.443, 1.369, 1.430, 1.299, 1.281, 1.274, 1.281, 1.308, 1.257, 1.229, 1.193, 1.120, 1.098, 1.105, 1.099, 1.062]
rqcd_i_high_topo_3track_25med = [1.432, 1.382, 1.334, 1.319, 1.314, 1.327, 1.317, 1.309, 1.328, 1.299, 1.304, 1.213, 1.217, 1.223, 1.221, 1.123, 1.077, 1.021, 1.004, 0.926, 0.915, 0.908, 0.898, 0.843, 0.775, 0.765, 0.755, 0.709, 0.687, 0.664, 0.648]

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

rqcd_i_low_ptvar_3track_25med = [1.296, 1.304, 1.314, 1.308, 1.308, 1.306, 1.313, 1.321, 1.332, 1.331, 1.300, 1.271, 1.268, 1.278, 1.280, 1.295, 1.298, 1.305, 1.303, 1.283, 1.249, 1.224, 1.214, 1.218, 1.227, 1.220, 1.226, 1.194, 1.202, 1.176, 1.181]
rqcd_i_high_ptvar_3track_25med = [1.428, 1.432, 1.437, 1.433, 1.440, 1.425, 1.448, 1.443, 1.437, 1.427, 1.423, 1.421, 1.440, 1.431, 1.430, 1.433, 1.444, 1.450, 1.444, 1.458, 1.464, 1.475, 1.464, 1.464, 1.468, 1.465, 1.467, 1.509, 1.508, 1.527, 1.507]

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

######################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"
# LOW VS HIGH PT
rqcd_i_low_3track_35med_val = 1.371 
rqcd_i_high_3track_35med_val = 1.602

rqcd_i_low_topo_3track_35med = [1.310, 1.474, 1.424, 1.418, 1.252, 1.324, 1.252, 1.308, 1.435, 1.474, 1.706, 1.852, 1.772, 1.772, 1.612, 1.452, 1.452, 1.633, 1.252, 1.157, 1.375, 1.551, 1.423, 1.631, 1.338, 1.338, 1.338, 1.893, 2.388, 2.388]
rqcd_i_high_topo_3track_35med = [1.443, 1.379, 1.328, 1.322, 1.325, 1.324, 1.264, 1.270, 1.310, 1.283, 1.301, 1.194, 1.166, 1.169, 1.163, 1.079, 1.033, 0.985, 0.980, 0.907, 0.919, 0.930, 0.954, 0.936, 0.837, 0.814, 0.842, 0.800, 0.762, 0.782]

min_rqcd_i_low_topo_3track_35med = 2
max_rqcd_i_low_topo_3track_35med = 0
min_rqcd_i_high_topo_3track_35med = 2
max_rqcd_i_high_topo_3track_35med = 0

for i in range(len(rqcd_i_low_topo_3track_35med)):
	if rqcd_i_low_topo_3track_35med[i]<min_rqcd_i_low_topo_3track_35med:
		min_rqcd_i_low_topo_3track_35med = rqcd_i_low_topo_3track_35med[i]
	if rqcd_i_low_topo_3track_35med[i]>max_rqcd_i_low_topo_3track_35med:
		max_rqcd_i_low_topo_3track_35med = rqcd_i_low_topo_3track_35med[i]


for i in range(len(rqcd_i_high_topo_3track_35med)):
        if rqcd_i_high_topo_3track_35med[i]<min_rqcd_i_high_topo_3track_35med:
                min_rqcd_i_high_topo_3track_35med = rqcd_i_high_topo_3track_35med[i]
        if rqcd_i_high_topo_3track_35med[i]>max_rqcd_i_high_topo_3track_35med:
                max_rqcd_i_high_topo_3track_35med = rqcd_i_high_topo_3track_35med[i]

print "TOPO_35med: sys_i_low =", ((max_rqcd_i_low_topo_3track_35med - min_rqcd_i_low_topo_3track_35med)/2)
print "TOPO_35med: sys_i_high =", ((max_rqcd_i_high_topo_3track_35med - min_rqcd_i_high_topo_3track_35med)/2)
print "TOPO_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_35med - min_rqcd_i_low_topo_3track_35med)/2)/rqcd_i_low_3track_35med_val
print "TOPO_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_35med - min_rqcd_i_high_topo_3track_35med)/2)/rqcd_i_high_3track_35med_val

rqcd_i_low_ptvar_3track_35med = [1.115, 1.172, 1.139, 1.144, 1.166, 1.152, 1.179, 1.147, 1.173, 1.156, 1.094, 1.074, 1.056, 1.057, 1.036, 1.058, 1.037, 1.023, 1.031, 0.987, 0.899, 0.855, 0.833, 0.833, 0.879, 0.833, 0.810, 0.829, 0.805, 0.795, 0.795]
rqcd_i_high_ptvar_3track_35med = [1.471, 1.476, 1.473, 1.461, 1.469, 1.452, 1.481, 1.476, 1.473, 1.464, 1.456, 1.461, 1.480, 1.463, 1.460, 1.468, 1.469, 1.470, 1.460, 1.472, 1.478, 1.486, 1.479, 1.476, 1.484, 1.476, 1.479, 1.541, 1.541, 1.550, 1.526]

min_rqcd_i_low_ptvar_3track_35med = 2
max_rqcd_i_low_ptvar_3track_35med = 0
min_rqcd_i_high_ptvar_3track_35med = 2
max_rqcd_i_high_ptvar_3track_35med = 0

for i in range(len(rqcd_i_low_ptvar_3track_35med)):
        if rqcd_i_low_ptvar_3track_35med[i]<min_rqcd_i_low_ptvar_3track_35med:
                min_rqcd_i_low_ptvar_3track_35med = rqcd_i_low_ptvar_3track_35med[i]
        if rqcd_i_low_ptvar_3track_35med[i]>max_rqcd_i_low_ptvar_3track_35med:
                max_rqcd_i_low_ptvar_3track_35med = rqcd_i_low_ptvar_3track_35med[i]


for i in range(len(rqcd_i_high_ptvar_3track_35med)):
        if rqcd_i_high_ptvar_3track_35med[i]<min_rqcd_i_high_ptvar_3track_35med:
                min_rqcd_i_high_ptvar_3track_35med = rqcd_i_high_ptvar_3track_35med[i]
        if rqcd_i_high_ptvar_3track_35med[i]>max_rqcd_i_high_ptvar_3track_35med:
                max_rqcd_i_high_ptvar_3track_35med = rqcd_i_high_ptvar_3track_35med[i]

print "PTVAR_35med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_35med - min_rqcd_i_low_ptvar_3track_35med)/2)
print "PTVAR_35med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_35med - min_rqcd_i_high_ptvar_3track_35med)/2)
print "PTVAR_35med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_35med - min_rqcd_i_low_ptvar_3track_35med)/2)/rqcd_i_low_3track_35med_val
print "PTVAR_35med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_35med - min_rqcd_i_high_ptvar_3track_35med)/2)/rqcd_i_high_3track_35med_val
print ""
print "---> total sys 35med low pt =", max( ((max_rqcd_i_low_topo_3track_35med - min_rqcd_i_low_topo_3track_35med)/2), ((max_rqcd_i_low_ptvar_3track_35med - min_rqcd_i_low_ptvar_3track_35med)/2))
print "---> total sys 35med high pt =", max( ((max_rqcd_i_high_topo_3track_35med - min_rqcd_i_high_topo_3track_35med)/2), ((max_rqcd_i_high_ptvar_3track_35med - min_rqcd_i_high_ptvar_3track_35med)/2) )
print ""
print "---> total sys 35med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_35med - min_rqcd_i_low_topo_3track_35med)/2)/rqcd_i_low_3track_35med_val, ((max_rqcd_i_low_ptvar_3track_35med - min_rqcd_i_low_ptvar_3track_35med)/2)/rqcd_i_low_3track_35med_val )
print "---> total sys 35med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_35med - min_rqcd_i_high_topo_3track_35med)/2)/rqcd_i_high_3track_35med_val, ((max_rqcd_i_high_ptvar_3track_35med - min_rqcd_i_high_ptvar_3track_35med)/2)/rqcd_i_high_3track_35med_val )

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
rqcd_i_low_3track_50L1TAU12med_val = 1.365 
rqcd_i_high_3track_50L1TAU12med_val = 1.651

rqcd_i_low_topo_3track_50L1TAU12med = [1.130, 1.184, 1.149, 1.154, 1.007, 1.094, 0.964, 1.056, 1.059, 1.026, 1.111, 1.145, 1.240, 1.351, 1.171, 1.044, 1.044, 1.159, 0.948, 1.060, 1.150, 1.319, 1.373, 1.030, 1.030, 0.858, 0.829, 0.829, 0.784, 0.784]
rqcd_i_high_topo_3track_50L1TAU12med = [1.522, 1.501, 1.429, 1.472, 1.478, 1.464, 1.427, 1.467, 1.456, 1.448, 1.500, 1.347, 1.334, 1.326, 1.342, 1.201, 1.131, 1.128, 1.074, 1.076, 1.034, 1.028, 1.102, 1.060, 1.011, 0.952, 0.849, 0.786, 0.726, 0.733]

min_rqcd_i_low_topo_3track_50L1TAU12med = 2
max_rqcd_i_low_topo_3track_50L1TAU12med = 0
min_rqcd_i_high_topo_3track_50L1TAU12med = 2
max_rqcd_i_high_topo_3track_50L1TAU12med = 0

for i in range(len(rqcd_i_low_topo_3track_50L1TAU12med)):
	if rqcd_i_low_topo_3track_50L1TAU12med[i]<min_rqcd_i_low_topo_3track_50L1TAU12med:
		min_rqcd_i_low_topo_3track_50L1TAU12med = rqcd_i_low_topo_3track_50L1TAU12med[i]
	if rqcd_i_low_topo_3track_50L1TAU12med[i]>max_rqcd_i_low_topo_3track_50L1TAU12med:
		max_rqcd_i_low_topo_3track_50L1TAU12med = rqcd_i_low_topo_3track_50L1TAU12med[i]


for i in range(len(rqcd_i_high_topo_3track_50L1TAU12med)):
        if rqcd_i_high_topo_3track_50L1TAU12med[i]<min_rqcd_i_high_topo_3track_50L1TAU12med:
                min_rqcd_i_high_topo_3track_50L1TAU12med = rqcd_i_high_topo_3track_50L1TAU12med[i]
        if rqcd_i_high_topo_3track_50L1TAU12med[i]>max_rqcd_i_high_topo_3track_50L1TAU12med:
                max_rqcd_i_high_topo_3track_50L1TAU12med = rqcd_i_high_topo_3track_50L1TAU12med[i]

print "TOPO_50L1TAU12med: sys_i_low =", ((max_rqcd_i_low_topo_3track_50L1TAU12med - min_rqcd_i_low_topo_3track_50L1TAU12med)/2)
print "TOPO_50L1TAU12med: sys_i_high =", ((max_rqcd_i_high_topo_3track_50L1TAU12med - min_rqcd_i_high_topo_3track_50L1TAU12med)/2)
print "TOPO_50L1TAU12med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_50L1TAU12med - min_rqcd_i_low_topo_3track_50L1TAU12med)/2)/rqcd_i_low_3track_50L1TAU12med_val
print "TOPO_50L1TAU12med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_50L1TAU12med - min_rqcd_i_high_topo_3track_50L1TAU12med)/2)/rqcd_i_high_3track_50L1TAU12med_val

rqcd_i_low_ptvar_3track_50L1TAU12med = [1.085, 1.149, 1.110, 1.092, 1.094, 1.053, 1.100, 1.057, 1.058, 1.036, 1.014, 0.991, 0.949, 0.949, 0.971, 0.971, 0.947, 0.921, 0.905, 0.905, 0.903, 0.828, 0.849, 0.824, 0.798, 0.801, 0.748, 0.722, 0.742, 0.715, 0.698, 0.719]
rqcd_i_high_ptvar_3track_50L1TAU12med = [1.561, 1.547, 1.562, 1.540, 1.544, 1.520, 1.561, 1.562, 1.558, 1.542, 1.530, 1.541, 1.564, 1.535, 1.514, 1.514, 1.511, 1.518, 1.512, 1.504, 1.527, 1.520, 1.527, 1.527, 1.519, 1.515, 1.482, 1.484, 1.536, 1.542, 1.568, 1.566]

min_rqcd_i_low_ptvar_3track_50L1TAU12med = 2
max_rqcd_i_low_ptvar_3track_50L1TAU12med = 0
min_rqcd_i_high_ptvar_3track_50L1TAU12med = 2
max_rqcd_i_high_ptvar_3track_50L1TAU12med = 0

for i in range(len(rqcd_i_low_ptvar_3track_50L1TAU12med)):
        if rqcd_i_low_ptvar_3track_50L1TAU12med[i]<min_rqcd_i_low_ptvar_3track_50L1TAU12med:
                min_rqcd_i_low_ptvar_3track_50L1TAU12med = rqcd_i_low_ptvar_3track_50L1TAU12med[i]
        if rqcd_i_low_ptvar_3track_50L1TAU12med[i]>max_rqcd_i_low_ptvar_3track_50L1TAU12med:
                max_rqcd_i_low_ptvar_3track_50L1TAU12med = rqcd_i_low_ptvar_3track_50L1TAU12med[i]


for i in range(len(rqcd_i_high_ptvar_3track_50L1TAU12med)):
        if rqcd_i_high_ptvar_3track_50L1TAU12med[i]<min_rqcd_i_high_ptvar_3track_50L1TAU12med:
                min_rqcd_i_high_ptvar_3track_50L1TAU12med = rqcd_i_high_ptvar_3track_50L1TAU12med[i]
        if rqcd_i_high_ptvar_3track_50L1TAU12med[i]>max_rqcd_i_high_ptvar_3track_50L1TAU12med:
                max_rqcd_i_high_ptvar_3track_50L1TAU12med = rqcd_i_high_ptvar_3track_50L1TAU12med[i]

print "PTVAR_50L1TAU12med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_50L1TAU12med - min_rqcd_i_low_ptvar_3track_50L1TAU12med)/2)
print "PTVAR_50L1TAU12med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_50L1TAU12med - min_rqcd_i_high_ptvar_3track_50L1TAU12med)/2)
print "PTVAR_50L1TAU12med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_50L1TAU12med - min_rqcd_i_low_ptvar_3track_50L1TAU12med)/2)/rqcd_i_low_3track_50L1TAU12med_val
print "PTVAR_50L1TAU12med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_50L1TAU12med - min_rqcd_i_high_ptvar_3track_50L1TAU12med)/2)/rqcd_i_high_3track_50L1TAU12med_val
print ""
print "---> total sys 50L1TAU12med low pt =", max( ((max_rqcd_i_low_topo_3track_50L1TAU12med - min_rqcd_i_low_topo_3track_50L1TAU12med)/2), ((max_rqcd_i_low_ptvar_3track_50L1TAU12med - min_rqcd_i_low_ptvar_3track_50L1TAU12med)/2))
print "---> total sys 50L1TAU12med high pt =", max( ((max_rqcd_i_high_topo_3track_50L1TAU12med - min_rqcd_i_high_topo_3track_50L1TAU12med)/2), ((max_rqcd_i_high_ptvar_3track_50L1TAU12med - min_rqcd_i_high_ptvar_3track_50L1TAU12med)/2) )
print ""
print "---> total sys 50L1TAU12med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_50L1TAU12med - min_rqcd_i_low_topo_3track_50L1TAU12med)/2)/rqcd_i_low_3track_50L1TAU12med_val, ((max_rqcd_i_low_ptvar_3track_50L1TAU12med - min_rqcd_i_low_ptvar_3track_50L1TAU12med)/2)/rqcd_i_low_3track_50L1TAU12med_val )
print "---> total sys 50L1TAU12med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_50L1TAU12med - min_rqcd_i_high_topo_3track_50L1TAU12med)/2)/rqcd_i_high_3track_50L1TAU12med_val, ((max_rqcd_i_high_ptvar_3track_50L1TAU12med - min_rqcd_i_high_ptvar_3track_50L1TAU12med)/2)/rqcd_i_high_3track_50L1TAU12med_val )


################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
rqcd_i_low_3track_80med_val = 1.054 
rqcd_i_high_3track_80med_val = 1.832

rqcd_i_low_topo_3track_80med = [1.384, 1.384, 1.384, 1.384, 1.241, 1.241, 0.955, 0.955, 0.955, 1.167, 1.200, 1.200, 1.200, 1.200, 1.200, 1.200, 2.000, 1.667, 1.667, 1.333, 1.000, 0.667, 0.667, 0.500]
rqcd_i_high_topo_3track_80med = [1.612, 1.601, 1.463, 1.461, 1.462, 1.430, 1.399, 1.376, 1.451, 1.508, 1.575, 1.537, 1.510, 1.542, 1.558, 1.393, 1.269, 1.224, 1.167, 1.137, 1.018, 0.748, 1.149, 1.077, 1.005, 0.932, 0.968, 0.990, 1.023, 0.997, 1.090]

min_rqcd_i_low_topo_3track_80med = 2
max_rqcd_i_low_topo_3track_80med = 0
min_rqcd_i_high_topo_3track_80med = 2
max_rqcd_i_high_topo_3track_80med = 0

for i in range(len(rqcd_i_low_topo_3track_80med)):
	if rqcd_i_low_topo_3track_80med[i]<min_rqcd_i_low_topo_3track_80med:
		min_rqcd_i_low_topo_3track_80med = rqcd_i_low_topo_3track_80med[i]
	if rqcd_i_low_topo_3track_80med[i]>max_rqcd_i_low_topo_3track_80med:
		max_rqcd_i_low_topo_3track_80med = rqcd_i_low_topo_3track_80med[i]


for i in range(len(rqcd_i_high_topo_3track_80med)):
        if rqcd_i_high_topo_3track_80med[i]<min_rqcd_i_high_topo_3track_80med:
                min_rqcd_i_high_topo_3track_80med = rqcd_i_high_topo_3track_80med[i]
        if rqcd_i_high_topo_3track_80med[i]>max_rqcd_i_high_topo_3track_80med:
                max_rqcd_i_high_topo_3track_80med = rqcd_i_high_topo_3track_80med[i]

print "TOPO_80med: sys_i_low =", ((max_rqcd_i_low_topo_3track_80med - min_rqcd_i_low_topo_3track_80med)/2)
print "TOPO_80med: sys_i_high =", ((max_rqcd_i_high_topo_3track_80med - min_rqcd_i_high_topo_3track_80med)/2)
print "TOPO_80med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_80med - min_rqcd_i_low_topo_3track_80med)/2)/rqcd_i_low_3track_80med_val
print "TOPO_80med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_80med - min_rqcd_i_high_topo_3track_80med)/2)/rqcd_i_high_3track_80med_val

rqcd_i_low_ptvar_3track_80med = [0.803, 0.805, 0.805, 0.805, 0.855, 0.855, 0.912, 0.912, 0.912, 0.912, 0.912, 0.912, 0.846, 0.846, 0.846, 0.846, 0.835, 0.763, 0.763, 0.692, 0.621, 0.621, 0.621, 0.621, 0.692, 0.538, 0.538, 0.583, 0.500, 0.545, 0.545]
rqcd_i_high_ptvar_3track_80med = [1.677, 1.671, 1.695, 1.671, 1.656, 1.625, 1.657, 1.656, 1.630, 1.610, 1.596, 1.604, 1.606, 1.600, 1.607, 1.591, 1.601, 1.578, 1.580, 1.632, 1.626, 1.618, 1.628, 1.633, 1.655, 1.643, 1.696, 1.719, 1.723, 1.754, 1.788]

min_rqcd_i_low_ptvar_3track_80med = 2
max_rqcd_i_low_ptvar_3track_80med = 0
min_rqcd_i_high_ptvar_3track_80med = 2
max_rqcd_i_high_ptvar_3track_80med = 0

for i in range(len(rqcd_i_low_ptvar_3track_80med)):
        if rqcd_i_low_ptvar_3track_80med[i]<min_rqcd_i_low_ptvar_3track_80med:
                min_rqcd_i_low_ptvar_3track_80med = rqcd_i_low_ptvar_3track_80med[i]
        if rqcd_i_low_ptvar_3track_80med[i]>max_rqcd_i_low_ptvar_3track_80med:
                max_rqcd_i_low_ptvar_3track_80med = rqcd_i_low_ptvar_3track_80med[i]


for i in range(len(rqcd_i_high_ptvar_3track_80med)):
        if rqcd_i_high_ptvar_3track_80med[i]<min_rqcd_i_high_ptvar_3track_80med:
                min_rqcd_i_high_ptvar_3track_80med = rqcd_i_high_ptvar_3track_80med[i]
        if rqcd_i_high_ptvar_3track_80med[i]>max_rqcd_i_high_ptvar_3track_80med:
                max_rqcd_i_high_ptvar_3track_80med = rqcd_i_high_ptvar_3track_80med[i]

print "PTVAR_80med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_80med - min_rqcd_i_low_ptvar_3track_80med)/2)
print "PTVAR_80med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_80med - min_rqcd_i_high_ptvar_3track_80med)/2)
print "PTVAR_80med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_80med - min_rqcd_i_low_ptvar_3track_80med)/2)/rqcd_i_low_3track_80med_val
print "PTVAR_80med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_80med - min_rqcd_i_high_ptvar_3track_80med)/2)/rqcd_i_high_3track_80med_val
print ""
print "---> total sys 80med low pt =", max( ((max_rqcd_i_low_topo_3track_80med - min_rqcd_i_low_topo_3track_80med)/2), ((max_rqcd_i_low_ptvar_3track_80med - min_rqcd_i_low_ptvar_3track_80med)/2))
print "---> total sys 80med high pt =", max( ((max_rqcd_i_high_topo_3track_80med - min_rqcd_i_high_topo_3track_80med)/2), ((max_rqcd_i_high_ptvar_3track_80med - min_rqcd_i_high_ptvar_3track_80med)/2) )
print ""
print "---> total sys 80med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_80med - min_rqcd_i_low_topo_3track_80med)/2)/rqcd_i_low_3track_80med_val, ((max_rqcd_i_low_ptvar_3track_80med - min_rqcd_i_low_ptvar_3track_80med)/2)/rqcd_i_low_3track_80med_val )
print "---> total sys 80med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_80med - min_rqcd_i_high_topo_3track_80med)/2)/rqcd_i_high_3track_80med_val, ((max_rqcd_i_high_ptvar_3track_80med - min_rqcd_i_high_ptvar_3track_80med)/2)/rqcd_i_high_3track_80med_val )

################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
rqcd_i_low_3track_80L1TAU60med_val = 0.839 
rqcd_i_high_3track_80L1TAU60med_val = 1.747

rqcd_i_low_topo_3track_80L1TAU60med = [0.422, 0.422, 0.422, 0.422, 0.422, 0.422, 0.172, 0.172, 0.172, 0.250, 0.333, 0.333, 0.333, 0.333, 0.333, 0.333, 0.333, 1.000]
rqcd_i_high_topo_3track_80L1TAU60med = [1.367, 1.351, 1.199, 1.150, 1.145, 1.192, 1.118, 1.144, 1.202, 1.283, 1.361, 1.361, 1.308, 1.330, 1.294, 1.150, 1.071, 1.000, 0.852, 0.754, 0.795, 0.861, 0.861, 0.778, 0.694, 0.729, 0.775, 0.853]

min_rqcd_i_low_topo_3track_80L1TAU60med = 2
max_rqcd_i_low_topo_3track_80L1TAU60med = 0
min_rqcd_i_high_topo_3track_80L1TAU60med = 2
max_rqcd_i_high_topo_3track_80L1TAU60med = 0

for i in range(len(rqcd_i_low_topo_3track_80L1TAU60med)):
	if rqcd_i_low_topo_3track_80L1TAU60med[i]<min_rqcd_i_low_topo_3track_80L1TAU60med:
		min_rqcd_i_low_topo_3track_80L1TAU60med = rqcd_i_low_topo_3track_80L1TAU60med[i]
	if rqcd_i_low_topo_3track_80L1TAU60med[i]>max_rqcd_i_low_topo_3track_80L1TAU60med:
		max_rqcd_i_low_topo_3track_80L1TAU60med = rqcd_i_low_topo_3track_80L1TAU60med[i]


for i in range(len(rqcd_i_high_topo_3track_80L1TAU60med)):
        if rqcd_i_high_topo_3track_80L1TAU60med[i]<min_rqcd_i_high_topo_3track_80L1TAU60med:
                min_rqcd_i_high_topo_3track_80L1TAU60med = rqcd_i_high_topo_3track_80L1TAU60med[i]
        if rqcd_i_high_topo_3track_80L1TAU60med[i]>max_rqcd_i_high_topo_3track_80L1TAU60med:
                max_rqcd_i_high_topo_3track_80L1TAU60med = rqcd_i_high_topo_3track_80L1TAU60med[i]

print "TOPO_80L1TAU60med: sys_i_low =", ((max_rqcd_i_low_topo_3track_80L1TAU60med - min_rqcd_i_low_topo_3track_80L1TAU60med)/2)
print "TOPO_80L1TAU60med: sys_i_high =", ((max_rqcd_i_high_topo_3track_80L1TAU60med - min_rqcd_i_high_topo_3track_80L1TAU60med)/2)
print "TOPO_80L1TAU60med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_80L1TAU60med - min_rqcd_i_low_topo_3track_80L1TAU60med)/2)/rqcd_i_low_3track_80L1TAU60med_val
print "TOPO_80L1TAU60med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_80L1TAU60med - min_rqcd_i_high_topo_3track_80L1TAU60med)/2)/rqcd_i_high_3track_80L1TAU60med_val

rqcd_i_low_ptvar_3track_80L1TAU60med = [0.665, 0.668, 0.668, 0.668, 0.668, 1.610, 0.668, 0.668, 0.668, 0.668, 0.668, 0.668, 0.668, 0.668, 0.668, 0.668, 0.641, 0.557, 0.557, 0.474, 0.391, 0.391, 0.391, 0.391, 0.455, 0.364, 0.364, 0.400, 0.300, 0.333, 0.333]
rqcd_i_high_ptvar_3track_80L1TAU60med = [1.622, 1.593, 1.616, 1.604, 1.610, 1.585, 1.604, 1.614, 1.565, 1.533, 1.528, 1.523, 1.519, 1.510, 1.518, 1.513, 1.504, 1.481, 1.491, 1.526, 1.537, 1.545, 1.540, 1.540, 1.560, 1.538, 1.565, 1.519, 1.525, 1.580, 1.591]

min_rqcd_i_low_ptvar_3track_80L1TAU60med = 2
max_rqcd_i_low_ptvar_3track_80L1TAU60med = 0
min_rqcd_i_high_ptvar_3track_80L1TAU60med = 2
max_rqcd_i_high_ptvar_3track_80L1TAU60med = 0

for i in range(len(rqcd_i_low_ptvar_3track_80L1TAU60med)):
        if rqcd_i_low_ptvar_3track_80L1TAU60med[i]<min_rqcd_i_low_ptvar_3track_80L1TAU60med:
                min_rqcd_i_low_ptvar_3track_80L1TAU60med = rqcd_i_low_ptvar_3track_80L1TAU60med[i]
        if rqcd_i_low_ptvar_3track_80L1TAU60med[i]>max_rqcd_i_low_ptvar_3track_80L1TAU60med:
                max_rqcd_i_low_ptvar_3track_80L1TAU60med = rqcd_i_low_ptvar_3track_80L1TAU60med[i]


for i in range(len(rqcd_i_high_ptvar_3track_80L1TAU60med)):
        if rqcd_i_high_ptvar_3track_80L1TAU60med[i]<min_rqcd_i_high_ptvar_3track_80L1TAU60med:
                min_rqcd_i_high_ptvar_3track_80L1TAU60med = rqcd_i_high_ptvar_3track_80L1TAU60med[i]
        if rqcd_i_high_ptvar_3track_80L1TAU60med[i]>max_rqcd_i_high_ptvar_3track_80L1TAU60med:
                max_rqcd_i_high_ptvar_3track_80L1TAU60med = rqcd_i_high_ptvar_3track_80L1TAU60med[i]

print "PTVAR_80L1TAU60med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_80L1TAU60med - min_rqcd_i_low_ptvar_3track_80L1TAU60med)/2)
print "PTVAR_80L1TAU60med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_80L1TAU60med - min_rqcd_i_high_ptvar_3track_80L1TAU60med)/2)
print "PTVAR_80L1TAU60med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_80L1TAU60med - min_rqcd_i_low_ptvar_3track_80L1TAU60med)/2)/rqcd_i_low_3track_80L1TAU60med_val
print "PTVAR_80L1TAU60med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_80L1TAU60med - min_rqcd_i_high_ptvar_3track_80L1TAU60med)/2)/rqcd_i_high_3track_80L1TAU60med_val
print ""
print "---> total sys 80L1TAU60med low pt =", max( ((max_rqcd_i_low_topo_3track_80L1TAU60med - min_rqcd_i_low_topo_3track_80L1TAU60med)/2), ((max_rqcd_i_low_ptvar_3track_80L1TAU60med - min_rqcd_i_low_ptvar_3track_80L1TAU60med)/2))
print "---> total sys 80L1TAU60med high pt =", max( ((max_rqcd_i_high_topo_3track_80L1TAU60med - min_rqcd_i_high_topo_3track_80L1TAU60med)/2), ((max_rqcd_i_high_ptvar_3track_80L1TAU60med - min_rqcd_i_high_ptvar_3track_80L1TAU60med)/2) )
print ""
print "---> total sys 80L1TAU60med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_80L1TAU60med - min_rqcd_i_low_topo_3track_80L1TAU60med)/2)/rqcd_i_low_3track_80L1TAU60med_val, ((max_rqcd_i_low_ptvar_3track_80L1TAU60med - min_rqcd_i_low_ptvar_3track_80L1TAU60med)/2)/rqcd_i_low_3track_80L1TAU60med_val )
print "---> total sys 80L1TAU60med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_80L1TAU60med - min_rqcd_i_high_topo_3track_80L1TAU60med)/2)/rqcd_i_high_3track_80L1TAU60med_val, ((max_rqcd_i_high_ptvar_3track_80L1TAU60med - min_rqcd_i_high_ptvar_3track_80L1TAU60med)/2)/rqcd_i_high_3track_80L1TAU60med_val )

"""
# ----------------------------------- #
#     	  ptonly3Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_ptonly3Track_val =  
rqcd_i_high_ptonly3Track_val = 

rqcd_i_low_topo_ptonly3Track = []
rqcd_i_high_topo_ptonly3Track = []

min_rqcd_i_low_topo_ptonly3Track = 2
max_rqcd_i_low_topo_ptonly3Track = 0
min_rqcd_i_high_topo_ptonly3Track = 2
max_rqcd_i_high_topo_ptonly3Track = 0

for i in range(len(rqcd_i_low_topo_ptonly3Track)):
	if rqcd_i_low_topo_ptonly3Track[i]<min_rqcd_i_low_topo_ptonly:
		min_rqcd_i_low_topo_ptonly3Track = rqcd_i_low_topo_ptonly[i]
	if rqcd_i_low_topo_ptonly3Track[i]>max_rqcd_i_low_topo_ptonly:
		max_rqcd_i_low_topo_ptonly3Track = rqcd_i_low_topo_ptonly[i]


for i in range(len(rqcd_i_high_topo_ptonly3Track)):
        if rqcd_i_high_topo_ptonly3Track[i]<min_rqcd_i_high_topo_ptonly:
                min_rqcd_i_high_topo_ptonly3Track = rqcd_i_high_topo_ptonly[i]
        if rqcd_i_high_topo_ptonly3Track[i]>max_rqcd_i_high_topo_ptonly:
                max_rqcd_i_high_topo_ptonly3Track = rqcd_i_high_topo_ptonly[i]

print "TOPO_ptonly3Track: sys_i_low =", ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)
print "TOPO_ptonly3Track: sys_i_high =", ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)
print "TOPO_ptonly3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)/rqcd_i_low_ptonly_val
print "TOPO_ptonly3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)/rqcd_i_high_ptonly_val

rqcd_i_low_ptvar_ptonly3Track = [1.231, 1.231, 1.237, 1.229, 1.233, 1.236, 1.236, 1.232, 1.231, 1.232, 1.214, 1.210, 1.210, 1.206, 1.199, 1.194, 1.196, 1.196, 1.205, 1.204, 1.196, 1.185, 1.183, 1.189, 1.191, 1.198, 1.197, 1.192, 1.190, 1.199, 1.189, 1.192]
rqcd_i_high_ptvar_ptonly3Track = [1.361, 1.358, 1.363, 1.358, 1.362, 1.350, 1.358, 1.361, 1.359, 1.357, 1.356, 1.353, 1.353, 1.362, 1.360, 1.366, 1.366, 1.370, 1.373, 1.374, 1.380, 1.385, 1.392, 1.391, 1.390, 1.402, 1.395, 1.388, 1.410, 1.405, 1.418, 1.407]

min_rqcd_i_low_ptvar_ptonly3Track = 2
max_rqcd_i_low_ptvar_ptonly3Track = 0
min_rqcd_i_high_ptvar_ptonly3Track = 2
max_rqcd_i_high_ptvar_ptonly3Track = 0

for i in range(len(rqcd_i_low_ptvar_ptonly3Track)):
        if rqcd_i_low_ptvar_ptonly3Track[i]<min_rqcd_i_low_ptvar_ptonly:
                min_rqcd_i_low_ptvar_ptonly3Track = rqcd_i_low_ptvar_ptonly[i]
        if rqcd_i_low_ptvar_ptonly3Track[i]>max_rqcd_i_low_ptvar_ptonly:
                max_rqcd_i_low_ptvar_ptonly3Track = rqcd_i_low_ptvar_ptonly[i]


for i in range(len(rqcd_i_high_ptvar_ptonly3Track)):
        if rqcd_i_high_ptvar_ptonly3Track[i]<min_rqcd_i_high_ptvar_ptonly:
                min_rqcd_i_high_ptvar_ptonly3Track = rqcd_i_high_ptvar_ptonly[i]
        if rqcd_i_high_ptvar_ptonly3Track[i]>max_rqcd_i_high_ptvar_ptonly:
                max_rqcd_i_high_ptvar_ptonly3Track = rqcd_i_high_ptvar_ptonly[i]

print "PTVAR_ptonly3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)
print "PTVAR_ptonly3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)
print "PTVAR_ptonly3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)/rqcd_i_low_ptonly_val
print "PTVAR_ptonly3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)/rqcd_i_high_ptonly_val
print ""
print "---> total sys ptonly3Track low pt =", max( ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2), ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2))
print "---> total sys ptonly3Track high pt =", max( ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2), ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2) )
print ""
print "---> total sys ptonly3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_ptonly - min_rqcd_i_low_topo_ptonly)/2)/rqcd_i_low_ptonly_val, ((max_rqcd_i_low_ptvar_ptonly - min_rqcd_i_low_ptvar_ptonly)/2)/rqcd_i_low_ptonly_val )
print "---> total sys ptonly3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_ptonly - min_rqcd_i_high_topo_ptonly)/2)/rqcd_i_high_ptonly_val, ((max_rqcd_i_high_ptvar_ptonly - min_rqcd_i_high_ptvar_ptonly)/2)/rqcd_i_high_ptonly_val )


# ----------------------------------- #
#     	   tracktwo3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_tracktwo3Track_val =  
rqcd_i_high_tracktwo3Track_val = 

rqcd_i_low_topo_tracktwo3Track = [1.185, 1.214, 1.257, 1.272, 1.274, 1.273, 1.268, 1.271, 1.266, 1.251, 1.276, 1.287, 1.314, 1.323, 1.331, 1.316, 1.241, 1.254, 1.199, 1.205, 1.207, 1.204, 1.237, 1.227, 1.201, 1.221, 1.162, 1.159, 1.181, 1.192, 1.161]
rqcd_i_high_topo_tracktwo3Track = [1.341, 1.295, 1.264, 1.243, 1.238, 1.249, 1.248, 1.241, 1.270, 1.257, 1.262, 1.184, 1.187, 1.196, 1.193, 1.118, 1.084, 1.026, 0.997, 0.939, 0.912, 0.896, 0.891, 0.832, 0.760, 0.750, 0.743, 0.701, 0.696, 0.691, 0.680]

min_rqcd_i_low_topo_tracktwo3Track = 2
max_rqcd_i_low_topo_tracktwo3Track = 0
min_rqcd_i_high_topo_tracktwo3Track = 2
max_rqcd_i_high_topo_tracktwo3Track = 0

for i in range(len(rqcd_i_low_topo_tracktwo3Track)):
	if rqcd_i_low_topo_tracktwo3Track[i]<min_rqcd_i_low_topo_35med:
		min_rqcd_i_low_topo_tracktwo3Track = rqcd_i_low_topo_35med[i]
	if rqcd_i_low_topo_tracktwo3Track[i]>max_rqcd_i_low_topo_35med:
		max_rqcd_i_low_topo_tracktwo3Track = rqcd_i_low_topo_35med[i]


for i in range(len(rqcd_i_high_topo_tracktwo3Track)):
        if rqcd_i_high_topo_tracktwo3Track[i]<min_rqcd_i_high_topo_35med:
                min_rqcd_i_high_topo_tracktwo3Track = rqcd_i_high_topo_35med[i]
        if rqcd_i_high_topo_tracktwo3Track[i]>max_rqcd_i_high_topo_35med:
                max_rqcd_i_high_topo_tracktwo3Track = rqcd_i_high_topo_35med[i]

print "TOPO_tracktwo3Track: sys_i_low =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)
print "TOPO_tracktwo3Track: sys_i_high =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)
print "TOPO_tracktwo3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val
print "TOPO_tracktwo3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val

rqcd_i_low_ptvar_tracktwo3Track = []
rqcd_i_high_ptvar_tracktwo3Track = []

min_rqcd_i_low_ptvar_tracktwo3Track = 2
max_rqcd_i_low_ptvar_tracktwo3Track = 0
min_rqcd_i_high_ptvar_tracktwo3Track = 2
max_rqcd_i_high_ptvar_tracktwo3Track = 0

for i in range(len(rqcd_i_low_ptvar_tracktwo3Track)):
        if rqcd_i_low_ptvar_tracktwo3Track[i]<min_rqcd_i_low_ptvar_35med:
                min_rqcd_i_low_ptvar_tracktwo3Track = rqcd_i_low_ptvar_35med[i]
        if rqcd_i_low_ptvar_tracktwo3Track[i]>max_rqcd_i_low_ptvar_35med:
                max_rqcd_i_low_ptvar_tracktwo3Track = rqcd_i_low_ptvar_35med[i]


for i in range(len(rqcd_i_high_ptvar_tracktwo3Track)):
        if rqcd_i_high_ptvar_tracktwo3Track[i]<min_rqcd_i_high_ptvar_35med:
                min_rqcd_i_high_ptvar_tracktwo3Track = rqcd_i_high_ptvar_35med[i]
        if rqcd_i_high_ptvar_tracktwo3Track[i]>max_rqcd_i_high_ptvar_35med:
                max_rqcd_i_high_ptvar_tracktwo3Track = rqcd_i_high_ptvar_35med[i]

print "PTVAR_tracktwo3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)
print "PTVAR_tracktwo3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)
print "PTVAR_tracktwo3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val
print "PTVAR_tracktwo3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val
print ""
print "---> total sys tracktwo3Track low pt =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2), ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2))
print "---> total sys tracktwo3Track high pt =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2), ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2) )
print ""
print "---> total sys tracktwo3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val, ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val )
print "---> total sys tracktwo3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val, ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val )

# ----------------------------------- #
#     	   L1TAU12IM3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_L1TAU12IM3Track_val =  
rqcd_i_high_L1TAU12IM3Track_val = 

rqcd_i_low_topo_L1TAU12IM3Track = [1.150, 1.150, 1.164, 1.168, 1.164, 1.162, 1.150, 1.154, 1.130, 1.139, 1.149, 1.148, 1.161, 1.146, 1.144, 1.146, 1.078, 1.066, 1.023, 1.005, 0.998, 0.995, 1.016, 1.002, 0.993, 1.041, 1.023, 1.008, 1.018, 1.009, 0.972]
rqcd_i_high_topo_L1TAU12IM3Track = [1.333, 1.288, 1.268, 1.254, 1.244, 1.254, 1.253, 1.225, 1.250, 1.231, 1.236, 1.157, 1.158, 1.172, 1.148, 1.085, 1.050, 1.005, 0.991, 0.951, 0.921, 0.911, 0.897, 0.843, 0.776, 0.759, 0.753, 0.717, 0.713, 0.704, 0.704]

min_rqcd_i_low_topo_L1TAU12IM3Track = 2
max_rqcd_i_low_topo_L1TAU12IM3Track = 0
min_rqcd_i_high_topo_L1TAU12IM3Track = 2
max_rqcd_i_high_topo_L1TAU12IM3Track = 0

for i in range(len(rqcd_i_low_topo_L1TAU12IM3Track)):
	if rqcd_i_low_topo_L1TAU12IM3Track[i]<min_rqcd_i_low_topo_35med:
		min_rqcd_i_low_topo_L1TAU12IM3Track = rqcd_i_low_topo_35med[i]
	if rqcd_i_low_topo_L1TAU12IM3Track[i]>max_rqcd_i_low_topo_35med:
		max_rqcd_i_low_topo_L1TAU12IM3Track = rqcd_i_low_topo_35med[i]


for i in range(len(rqcd_i_high_topo_L1TAU12IM3Track)):
        if rqcd_i_high_topo_L1TAU12IM3Track[i]<min_rqcd_i_high_topo_35med:
                min_rqcd_i_high_topo_L1TAU12IM3Track = rqcd_i_high_topo_35med[i]
        if rqcd_i_high_topo_L1TAU12IM3Track[i]>max_rqcd_i_high_topo_35med:
                max_rqcd_i_high_topo_L1TAU12IM3Track = rqcd_i_high_topo_35med[i]

print "TOPO_L1TAU12IM3Track: sys_i_low =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)
print "TOPO_L1TAU12IM3Track: sys_i_high =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)
print "TOPO_L1TAU12IM3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val
print "TOPO_L1TAU12IM3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val

rqcd_i_low_ptvar_L1TAU12IM3Track = [1.241, 1.239, 1.245, 1.236, 1.242, 1.244, 1.246, 1.242, 1.240, 1.241, 1.230, 1.227, 1.220, 1.216, 1.213, 1.214, 1.205, 1.213, 1.213, 1.207, 1.196, ]
rqcd_i_high_ptvar_L1TAU12IM3Track = [1.360, 1.356, 1.362, 1.357, 1.361, 1.348, 1.357, 1.360, 1.358, 1.355, 1.354, 1.351, 1.361, 1.360, 1.366, 1.364, 1.369, 1.372, 1.373, 1.379, 1.383, ]

min_rqcd_i_low_ptvar_L1TAU12IM3Track = 2
max_rqcd_i_low_ptvar_L1TAU12IM3Track = 0
min_rqcd_i_high_ptvar_L1TAU12IM3Track = 2
max_rqcd_i_high_ptvar_L1TAU12IM3Track = 0

for i in range(len(rqcd_i_low_ptvar_L1TAU12IM3Track)):
        if rqcd_i_low_ptvar_L1TAU12IM3Track[i]<min_rqcd_i_low_ptvar_35med:
                min_rqcd_i_low_ptvar_L1TAU12IM3Track = rqcd_i_low_ptvar_35med[i]
        if rqcd_i_low_ptvar_L1TAU12IM3Track[i]>max_rqcd_i_low_ptvar_35med:
                max_rqcd_i_low_ptvar_L1TAU12IM3Track = rqcd_i_low_ptvar_35med[i]


for i in range(len(rqcd_i_high_ptvar_L1TAU12IM3Track)):
        if rqcd_i_high_ptvar_L1TAU12IM3Track[i]<min_rqcd_i_high_ptvar_35med:
                min_rqcd_i_high_ptvar_L1TAU12IM3Track = rqcd_i_high_ptvar_35med[i]
        if rqcd_i_high_ptvar_L1TAU12IM3Track[i]>max_rqcd_i_high_ptvar_35med:
                max_rqcd_i_high_ptvar_L1TAU12IM3Track = rqcd_i_high_ptvar_35med[i]

print "PTVAR_L1TAU12IM3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)
print "PTVAR_L1TAU12IM3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)
print "PTVAR_L1TAU12IM3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val
print "PTVAR_L1TAU12IM3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val
print ""
print "---> total sys L1TAU12IM3Track low pt =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2), ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2))
print "---> total sys L1TAU12IM3Track high pt =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2), ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2) )
print ""
print "---> total sys L1TAU12IM3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_35med - min_rqcd_i_low_topo_35med)/2)/rqcd_i_low_35med_val, ((max_rqcd_i_low_ptvar_35med - min_rqcd_i_low_ptvar_35med)/2)/rqcd_i_low_35med_val )
print "---> total sys L1TAU12IM3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_35med - min_rqcd_i_high_topo_35med)/2)/rqcd_i_high_35med_val, ((max_rqcd_i_high_ptvar_35med - min_rqcd_i_high_ptvar_35med)/2)/rqcd_i_high_35med_val )

"""
