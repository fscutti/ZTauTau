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

rqcd_i_low_topo = [1.184, 1.192, 1.192, 1.191, 1.194, 1.190, 1.188, 1.187, 1.188, 1.184, 1.183, 1.182, 1.179, 1.179, 1.181, 1.180, 1.181, 1.180, 1.180, 1.178, 1.178]
rqcd_i_high_topo = [1.257, 1.261, 1.262, 1.265, 1.263, 1.260, 1.253, 1.253, 1.249, 1.252, 1.251, 1.253, 1.251, 1.253, 1.254, 1.254, 1.252, 1.252, 1.251, 1.251, 1.249]

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

rqcd_i_low_ptvar = [1.222, 1.215, 1.213, 1.213, 1.208, 1.201]
rqcd_i_high_ptvar = [1.324, 1.315, 1.314, 1.310, 1.305, 1.303]

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

rqcd_i_low_topo_25med = [1.111, 1.128, 1.138, 1.141, 1.143, 1.138, 1.138, 1.142, 1.143, 1.137, 1.133, 1.134, 1.131, 1.136, 1.137, 1.134, 1.136, 1.135, 1.136, 1.135, 1.135]
rqcd_i_high_topo_25med = [1.284, 1.287, 1.291, 1.296, 1.297, 1.286, 1.276, 1.274, 1.274, 1.275, 1.275, 1.275, 1.273, 1.277, 1.276, 1.277, 1.274, 1.272, 1.272, 1.272, 1.269]

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

rqcd_i_low_ptvar_25med = [1.158, 1.164, 1.164, 1.153, 1.154, 1.148]
rqcd_i_high_ptvar_25med = [1.407, 1.393, 1.385, 1.376, 1.367, 1.365]

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

print " ----------------------------------- "
print "            no trigger"
print " ------------------------------------"

# LOW VS HIGH PT
rqcd_i_low_1track_val = 1.126  
rqcd_i_high_1track_val = 1.182

rqcd_i_low_topo_1track = [1.140, 1.153, 1.161, 1.160, 1.165, 1.161, 1.159, 1.158, 1.158, 1.151, 1.151, 1.151, 1.149, 1.148, 1.149, 1.148, 1.147, 1.146, 1.145, 1.142, 1.142]
rqcd_i_high_topo_1track = [1.191, 1.192, 1.194, 1.199, 1.198, 1.197, 1.190, 1.189, 1.188, 1.192, 1.193, 1.193, 1.191, 1.197, 1.197, 1.196, 1.192, 1.192, 1.192, 1.191, 1.190]

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

rqcd_i_low_ptvar_1track = [1.188, 1.184, 1.183, 1.181, 1.175, 1.169]
rqcd_i_high_ptvar_1track = [1.247, 1.237, 1.240, 1.238, 1.234, 1.229]

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

rqcd_i_low_topo_1track_25med = [1.086, 1.108, 1.123, 1.125, 1.127, 1.123, 1.123, 1.126, 1.127, 1.120, 1.116, 1.118, 1.114, 1.119, 1.120, 1.118, 1.118, 1.119, 1.117, 1.115, 1.116]
rqcd_i_high_topo_1track_25med = [1.209, 1.209, 1.211, 1.218, 1.222, 1.213, 1.203, 1.201, 1.203, 1.205, 1.206, 1.204, 1.203, 1.208, 1.209, 1.207, 1.203, 1.202, 1.202, 1.201, 1.199]

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

rqcd_i_low_ptvar_1track_25med = [1.146, 1.154, 1.156, 1.142, 1.142, 1.134]
rqcd_i_high_ptvar_1track_25med = [1.307, 1.296, 1.291, 1.284, 1.279, 1.275]

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

rqcd_i_low_topo_1track_35med = [1.131, 1.176, 1.177, 1.177, 1.190, 1.192, 1.193, 1.187, 1.119, 1.125, 1.121, 1.138, 1.114, 1.111, 1.113, 1.121, 1.116, 1.116, 1.114, 1.104, 1.094]
rqcd_i_high_topo_1track_35med = [1.221, 1.214, 1.216, 1.221, 1.227, 1.211, 1.200, 1.201, 1.205, 1.206, 1.207, 1.206, 1.204, 1.208, 1.209, 1.206, 1.204, 1.202, 1.203, 1.201, 1.200]

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

rqcd_i_low_ptvar_1track_35med = [1.068, 1.058, 1.068, 1.096, 1.071]
rqcd_i_high_ptvar_1track_35med = [1.292, 1.274, 1.261, 1.257, 1.255]

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

rqcd_i_low_topo_1track_50L1TAU12med = [0.748, 0.779, 0.798, 0.803, 0.838, 0.859, 0.878, 0.878, 0.856, 0.847, 0.864, 0.883, 0.869, 0.881, 0.885, 0.892, 0.904, 0.909, 0.903, 0.894, 0.895]
rqcd_i_high_topo_1track_50L1TAU12med = [1.315, 1.309, 1.306, 1.311, 1.313, 1.301, 1.287, 1.279, 1.283, 1.290, 1.290, 1.282, 1.283, 1.286, 1.289, 1.286, 1.286, 1.276, 1.274, 1.274, 1.273]

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

rqcd_i_low_ptvar_1track_50L1TAU12med = [0.726, 0.705, 0.709, 0.726, 0.757, 0.774]
rqcd_i_high_ptvar_1track_50L1TAU12med = [1.514, 1.485, 1.457, 1.456, 1.440, 1.414]

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

rqcd_i_low_topo_1track_80med = []
rqcd_i_high_topo_1track_80med = [1.303, 1.280, 1.291, 1.295, 1.282, 1.276, 1.265, 1.252, 1.264, 1.277, 1.283, 1.274, 1.274, 1.284, 1.291, 1.228, 1.232, 1.224, 1.223, 1.227, 1.232]

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

rqcd_i_low_ptvar_1track_80med = [1.654, 1.532, 1.667, 1.667, 1.667, 1.744]
rqcd_i_high_ptvar_1track_80med = [1.356, 1.359, 1.322, 1.325, 1.286, 1.242]

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

rqcd_i_low_topo_1track_80L1TAU60med = []
rqcd_i_high_topo_1track_80L1TAU60med = [1.310, 1.275, 1.284, 1.287, 1.276, 1.268, 1.262, 1.253, 1.260, 1.272, 1.276, 1.261, 1.264, 1.271, 1.279, 1.189, 1.194, 1.186, 1.182, 1.189, 1.195]

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

rqcd_i_low_ptvar_1track_80L1TAU60med = [0.544, 0.544, 0.572, 0.572, 0.572, 0.677]
rqcd_i_high_ptvar_1track_80L1TAU60med = [1.303, 1.311, 1.263, 1.257, 1.208, 1.159]

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

################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
rqcd_i_low_1track_125med_val = 0.722 
rqcd_i_high_1track_125med_val = 1.159

rqcd_i_low_topo_1track_125med = [0.634, 0.570, 0.570, 0.700, 0.700, 0.642, 0.572, 0.674, 0.629, 0.629, 0.652, 0.614, 0.580, 0.635, 0.746, 0.746, 0.746, 0.746, 0.746, 0.746, 0.746]
rqcd_i_high_topo_1track_125med = [1.301, 1.244, 1.258, 1.255, 1.235, 1.210, 1.190, 1.172, 1.185, 1.191, 1.195, 1.188, 1.198, 1.199, 1.205, 1.151, 1.158, 1.159, 1.158, 1.166, 1.163]

min_rqcd_i_low_topo_1track_125med = 2
max_rqcd_i_low_topo_1track_125med = 0
min_rqcd_i_high_topo_1track_125med = 2
max_rqcd_i_high_topo_1track_125med = 0

for i in range(len(rqcd_i_low_topo_1track_125med)):
	if rqcd_i_low_topo_1track_125med[i]<min_rqcd_i_low_topo_1track_125med:
		min_rqcd_i_low_topo_1track_125med = rqcd_i_low_topo_1track_125med[i]
	if rqcd_i_low_topo_1track_125med[i]>max_rqcd_i_low_topo_1track_125med:
		max_rqcd_i_low_topo_1track_125med = rqcd_i_low_topo_1track_125med[i]


for i in range(len(rqcd_i_high_topo_1track_125med)):
        if rqcd_i_high_topo_1track_125med[i]<min_rqcd_i_high_topo_1track_125med:
                min_rqcd_i_high_topo_1track_125med = rqcd_i_high_topo_1track_125med[i]
        if rqcd_i_high_topo_1track_125med[i]>max_rqcd_i_high_topo_1track_125med:
                max_rqcd_i_high_topo_1track_125med = rqcd_i_high_topo_1track_125med[i]

print "TOPO_125med: sys_i_low =", ((max_rqcd_i_low_topo_1track_125med - min_rqcd_i_low_topo_1track_125med)/2)
print "TOPO_125med: sys_i_high =", ((max_rqcd_i_high_topo_1track_125med - min_rqcd_i_high_topo_1track_125med)/2)
print "TOPO_125med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_125med - min_rqcd_i_low_topo_1track_125med)/2)/rqcd_i_low_1track_125med_val
print "TOPO_125med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_125med - min_rqcd_i_high_topo_1track_125med)/2)/rqcd_i_high_1track_125med_val

rqcd_i_low_ptvar_1track_125med = [2.705, 2.705, 2.705, 2.705]
rqcd_i_high_ptvar_1track_125med = [0.728, 0.738, 0.752, 0.810, 0.826, 0.816]

min_rqcd_i_low_ptvar_1track_125med = 2
max_rqcd_i_low_ptvar_1track_125med = 0
min_rqcd_i_high_ptvar_1track_125med = 2
max_rqcd_i_high_ptvar_1track_125med = 0

for i in range(len(rqcd_i_low_ptvar_1track_125med)):
        if rqcd_i_low_ptvar_1track_125med[i]<min_rqcd_i_low_ptvar_1track_125med:
                min_rqcd_i_low_ptvar_1track_125med = rqcd_i_low_ptvar_1track_125med[i]
        if rqcd_i_low_ptvar_1track_125med[i]>max_rqcd_i_low_ptvar_1track_125med:
                max_rqcd_i_low_ptvar_1track_125med = rqcd_i_low_ptvar_1track_125med[i]


for i in range(len(rqcd_i_high_ptvar_1track_125med)):
        if rqcd_i_high_ptvar_1track_125med[i]<min_rqcd_i_high_ptvar_1track_125med:
                min_rqcd_i_high_ptvar_1track_125med = rqcd_i_high_ptvar_1track_125med[i]
        if rqcd_i_high_ptvar_1track_125med[i]>max_rqcd_i_high_ptvar_1track_125med:
                max_rqcd_i_high_ptvar_1track_125med = rqcd_i_high_ptvar_1track_125med[i]

print "PTVAR_125med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_125med - min_rqcd_i_low_ptvar_1track_125med)/2)
print "PTVAR_125med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_125med - min_rqcd_i_high_ptvar_1track_125med)/2)
print "PTVAR_125med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_125med - min_rqcd_i_low_ptvar_1track_125med)/2)/rqcd_i_low_1track_125med_val
print "PTVAR_125med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_125med - min_rqcd_i_high_ptvar_1track_125med)/2)/rqcd_i_high_1track_125med_val
print ""
print "---> total sys 125med low pt =", max( ((max_rqcd_i_low_topo_1track_125med - min_rqcd_i_low_topo_1track_125med)/2), ((max_rqcd_i_low_ptvar_1track_125med - min_rqcd_i_low_ptvar_1track_125med)/2))
print "---> total sys 125med high pt =", max( ((max_rqcd_i_high_topo_1track_125med - min_rqcd_i_high_topo_1track_125med)/2), ((max_rqcd_i_high_ptvar_1track_125med - min_rqcd_i_high_ptvar_1track_125med)/2) )
print ""
print "---> total sys 125med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_125med - min_rqcd_i_low_topo_1track_125med)/2)/rqcd_i_low_1track_125med_val, ((max_rqcd_i_low_ptvar_1track_125med - min_rqcd_i_low_ptvar_1track_125med)/2)/rqcd_i_low_1track_125med_val )
print "---> total sys 125med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_125med - min_rqcd_i_high_topo_1track_125med)/2)/rqcd_i_high_1track_125med_val, ((max_rqcd_i_high_ptvar_1track_125med - min_rqcd_i_high_ptvar_1track_125med)/2)/rqcd_i_high_1track_125med_val )

################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
rqcd_i_low_1track_160med_val = 1 
rqcd_i_high_1track_160med_val = 1.159

rqcd_i_low_topo_1track_160med = [0.667, 0.667, 0.667, 1.000, 0.571, 0.714, ]
rqcd_i_high_topo_1track_160med = [1.234, 1.207, 1.242, 1.234, 1.230, 1.230, 1.153, 1.143, 1.145, 1.150, 1.147, 1.172, 1.162, 1.215, 1.179, 1.182, 1.179, 1.158, 1.153, 1.177, 1.158]

min_rqcd_i_low_topo_1track_160med = 2
max_rqcd_i_low_topo_1track_160med = 0
min_rqcd_i_high_topo_1track_160med = 2
max_rqcd_i_high_topo_1track_160med = 0

for i in range(len(rqcd_i_low_topo_1track_160med)):
	if rqcd_i_low_topo_1track_160med[i]<min_rqcd_i_low_topo_1track_160med:
		min_rqcd_i_low_topo_1track_160med = rqcd_i_low_topo_1track_160med[i]
	if rqcd_i_low_topo_1track_160med[i]>max_rqcd_i_low_topo_1track_160med:
		max_rqcd_i_low_topo_1track_160med = rqcd_i_low_topo_1track_160med[i]


for i in range(len(rqcd_i_high_topo_1track_160med)):
        if rqcd_i_high_topo_1track_160med[i]<min_rqcd_i_high_topo_1track_160med:
                min_rqcd_i_high_topo_1track_160med = rqcd_i_high_topo_1track_160med[i]
        if rqcd_i_high_topo_1track_160med[i]>max_rqcd_i_high_topo_1track_160med:
                max_rqcd_i_high_topo_1track_160med = rqcd_i_high_topo_1track_160med[i]

print "TOPO_160med: sys_i_low =", ((max_rqcd_i_low_topo_1track_160med - min_rqcd_i_low_topo_1track_160med)/2)
print "TOPO_160med: sys_i_high =", ((max_rqcd_i_high_topo_1track_160med - min_rqcd_i_high_topo_1track_160med)/2)
print "TOPO_160med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_1track_160med - min_rqcd_i_low_topo_1track_160med)/2)/rqcd_i_low_1track_160med_val
print "TOPO_160med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_1track_160med - min_rqcd_i_high_topo_1track_160med)/2)/rqcd_i_high_1track_160med_val

rqcd_i_low_ptvar_1track_160med = []
rqcd_i_high_ptvar_1track_160med = []

min_rqcd_i_low_ptvar_1track_160med = 2
max_rqcd_i_low_ptvar_1track_160med = 0
min_rqcd_i_high_ptvar_1track_160med = 2
max_rqcd_i_high_ptvar_1track_160med = 0

for i in range(len(rqcd_i_low_ptvar_1track_160med)):
        if rqcd_i_low_ptvar_1track_160med[i]<min_rqcd_i_low_ptvar_1track_160med:
                min_rqcd_i_low_ptvar_1track_160med = rqcd_i_low_ptvar_1track_160med[i]
        if rqcd_i_low_ptvar_1track_160med[i]>max_rqcd_i_low_ptvar_1track_160med:
                max_rqcd_i_low_ptvar_1track_160med = rqcd_i_low_ptvar_1track_160med[i]


for i in range(len(rqcd_i_high_ptvar_1track_160med)):
        if rqcd_i_high_ptvar_1track_160med[i]<min_rqcd_i_high_ptvar_1track_160med:
                min_rqcd_i_high_ptvar_1track_160med = rqcd_i_high_ptvar_1track_160med[i]
        if rqcd_i_high_ptvar_1track_160med[i]>max_rqcd_i_high_ptvar_1track_160med:
                max_rqcd_i_high_ptvar_1track_160med = rqcd_i_high_ptvar_1track_160med[i]

print "PTVAR_160med: sys_i_low =", ((max_rqcd_i_low_ptvar_1track_160med - min_rqcd_i_low_ptvar_1track_160med)/2)
print "PTVAR_160med: sys_i_high =", ((max_rqcd_i_high_ptvar_1track_160med - min_rqcd_i_high_ptvar_1track_160med)/2)
print "PTVAR_160med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_1track_160med - min_rqcd_i_low_ptvar_1track_160med)/2)/rqcd_i_low_1track_160med_val
print "PTVAR_160med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_1track_160med - min_rqcd_i_high_ptvar_1track_160med)/2)/rqcd_i_high_1track_160med_val
print ""
print "---> total sys 160med low pt =", max( ((max_rqcd_i_low_topo_1track_160med - min_rqcd_i_low_topo_1track_160med)/2), ((max_rqcd_i_low_ptvar_1track_160med - min_rqcd_i_low_ptvar_1track_160med)/2))
print "---> total sys 160med high pt =", max( ((max_rqcd_i_high_topo_1track_160med - min_rqcd_i_high_topo_1track_160med)/2), ((max_rqcd_i_high_ptvar_1track_160med - min_rqcd_i_high_ptvar_1track_160med)/2) )
print ""
print "---> total sys 160med low pt (percentage) =", max( ((max_rqcd_i_low_topo_1track_160med - min_rqcd_i_low_topo_1track_160med)/2)/rqcd_i_low_1track_160med_val, ((max_rqcd_i_low_ptvar_1track_160med - min_rqcd_i_low_ptvar_1track_160med)/2)/rqcd_i_low_1track_160med_val )
print "---> total sys 160med high pt (percentage) =", max( ((max_rqcd_i_high_topo_1track_160med - min_rqcd_i_high_topo_1track_160med)/2)/rqcd_i_high_1track_160med_val, ((max_rqcd_i_high_ptvar_1track_160med - min_rqcd_i_high_ptvar_1track_160med)/2)/rqcd_i_high_1track_160med_val )



# ----------------------------------- #
#     	  ptonly1Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_ptonly1Track_val =  1.121
rqcd_i_high_ptonly1Track_val = 1.176

rqcd_i_low_topo_ptonly1Track = [1.121, 1.137, 1.147, 1.151, 1.156, 1.152, 1.153, 1.153, 1.151, 1.147, 1.144, 1.144, 1.141, 1.144, 1.143, 1.141, 1.142, 1.140, 1.140, 1.137, 1.137]
rqcd_i_high_topo_ptonly1Track = [1.186, 1.187, 1.189, 1.196, 1.196, 1.192, 1.185, 1.183, 1.183, 1.186, 1.188, 1.186, 1.185, 1.190, 1.191, 1.189, 1.186, 1.186, 1.186, 1.185, 1.183]

min_rqcd_i_low_topo_ptonly1Track = 2
max_rqcd_i_low_topo_ptonly1Track = 0
min_rqcd_i_high_topo_ptonly1Track = 2
max_rqcd_i_high_topo_ptonly1Track = 0

for i in range(len(rqcd_i_low_topo_ptonly1Track)):
	if rqcd_i_low_topo_ptonly1Track[i]<min_rqcd_i_low_topo_ptonly1Track:
		min_rqcd_i_low_topo_ptonly1Track = rqcd_i_low_topo_ptonly1Track[i]
	if rqcd_i_low_topo_ptonly1Track[i]>max_rqcd_i_low_topo_ptonly1Track:
		max_rqcd_i_low_topo_ptonly1Track = rqcd_i_low_topo_ptonly1Track[i]


for i in range(len(rqcd_i_high_topo_ptonly1Track)):
        if rqcd_i_high_topo_ptonly1Track[i]<min_rqcd_i_high_topo_ptonly1Track:
                min_rqcd_i_high_topo_ptonly1Track = rqcd_i_high_topo_ptonly1Track[i]
        if rqcd_i_high_topo_ptonly1Track[i]>max_rqcd_i_high_topo_ptonly1Track:
                max_rqcd_i_high_topo_ptonly1Track = rqcd_i_high_topo_ptonly1Track[i]

print "TOPO_ptonly1Track: sys_i_low =", ((max_rqcd_i_low_topo_ptonly1Track - min_rqcd_i_low_topo_ptonly1Track)/2)
print "TOPO_ptonly1Track: sys_i_high =", ((max_rqcd_i_high_topo_ptonly1Track - min_rqcd_i_high_topo_ptonly1Track)/2)
print "TOPO_ptonly1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_ptonly1Track - min_rqcd_i_low_topo_ptonly1Track)/2)/rqcd_i_low_ptonly1Track_val
print "TOPO_ptonly1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_ptonly1Track - min_rqcd_i_high_topo_ptonly1Track)/2)/rqcd_i_high_ptonly1Track_val

rqcd_i_low_ptvar_ptonly1Track = [1.194, 1.191, 1.190, 1.179, 1.173, 1.162]
rqcd_i_high_ptvar_ptonly1Track = [1.255, 1.244, 1.247, 1.241, 1.237, 1.232]

min_rqcd_i_low_ptvar_ptonly1Track = 2
max_rqcd_i_low_ptvar_ptonly1Track = 0
min_rqcd_i_high_ptvar_ptonly1Track = 2
max_rqcd_i_high_ptvar_ptonly1Track = 0

for i in range(len(rqcd_i_low_ptvar_ptonly1Track)):
        if rqcd_i_low_ptvar_ptonly1Track[i]<min_rqcd_i_low_ptvar_ptonly1Track:
                min_rqcd_i_low_ptvar_ptonly1Track = rqcd_i_low_ptvar_ptonly1Track[i]
        if rqcd_i_low_ptvar_ptonly1Track[i]>max_rqcd_i_low_ptvar_ptonly1Track:
                max_rqcd_i_low_ptvar_ptonly1Track = rqcd_i_low_ptvar_ptonly1Track[i]


for i in range(len(rqcd_i_high_ptvar_ptonly1Track)):
        if rqcd_i_high_ptvar_ptonly1Track[i]<min_rqcd_i_high_ptvar_ptonly1Track:
                min_rqcd_i_high_ptvar_ptonly1Track = rqcd_i_high_ptvar_ptonly1Track[i]
        if rqcd_i_high_ptvar_ptonly1Track[i]>max_rqcd_i_high_ptvar_ptonly1Track:
                max_rqcd_i_high_ptvar_ptonly1Track = rqcd_i_high_ptvar_ptonly1Track[i]

print "PTVAR_ptonly1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_ptonly1Track - min_rqcd_i_low_ptvar_ptonly1Track)/2)
print "PTVAR_ptonly1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_ptonly1Track - min_rqcd_i_high_ptvar_ptonly1Track)/2)
print "PTVAR_ptonly1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_ptonly1Track - min_rqcd_i_low_ptvar_ptonly1Track)/2)/rqcd_i_low_ptonly1Track_val
print "PTVAR_ptonly1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_ptonly1Track - min_rqcd_i_high_ptvar_ptonly1Track)/2)/rqcd_i_high_ptonly1Track_val
print ""
print "---> total sys ptonly1Track low pt =", max( ((max_rqcd_i_low_topo_ptonly1Track - min_rqcd_i_low_topo_ptonly1Track)/2), ((max_rqcd_i_low_ptvar_ptonly1Track - min_rqcd_i_low_ptvar_ptonly1Track)/2))
print "---> total sys ptonly1Track high pt =", max( ((max_rqcd_i_high_topo_ptonly1Track - min_rqcd_i_high_topo_ptonly1Track)/2), ((max_rqcd_i_high_ptvar_ptonly1Track - min_rqcd_i_high_ptvar_ptonly1Track)/2) )
print ""
print "---> total sys ptonly1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_ptonly1Track - min_rqcd_i_low_topo_ptonly1Track)/2)/rqcd_i_low_ptonly1Track_val, ((max_rqcd_i_low_ptvar_ptonly1Track - min_rqcd_i_low_ptvar_ptonly1Track)/2)/rqcd_i_low_ptonly1Track_val )
print "---> total sys ptonly1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_ptonly1Track - min_rqcd_i_high_topo_ptonly1Track)/2)/rqcd_i_high_ptonly1Track_val, ((max_rqcd_i_high_ptvar_ptonly1Track - min_rqcd_i_high_ptvar_ptonly1Track)/2)/rqcd_i_high_ptonly1Track_val )


# ----------------------------------- #
#     	   tracktwo1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_tracktwo1Track_val = 1.131 
rqcd_i_high_tracktwo1Track_val = 1.185

rqcd_i_low_topo_tracktwo1Track = [1.115, 1.137, 1.149, 1.149, 1.154, 1.152, 1.154, 1.155, 1.156, 1.151, 1.148, 1.149, 1.146, 1.149, 1.150, 1.148, 1.148, 1.148, 1.147, 1.145, 1.144]
rqcd_i_high_topo_tracktwo1Track = [1.202, 1.202, 1.203, 1.210, 1.210, 1.204, 1.194, 1.193, 1.195, 1.197, 1.198, 1.197, 1.196, 1.201, 1.202, 1.201, 1.198, 1.197, 1.197, 1.195, 1.193]

min_rqcd_i_low_topo_tracktwo1Track = 2
max_rqcd_i_low_topo_tracktwo1Track = 0
min_rqcd_i_high_topo_tracktwo1Track = 2
max_rqcd_i_high_topo_tracktwo1Track = 0

for i in range(len(rqcd_i_low_topo_tracktwo1Track)):
	if rqcd_i_low_topo_tracktwo1Track[i]<min_rqcd_i_low_topo_tracktwo1Track:
		min_rqcd_i_low_topo_tracktwo1Track = rqcd_i_low_topo_tracktwo1Track[i]
	if rqcd_i_low_topo_tracktwo1Track[i]>max_rqcd_i_low_topo_tracktwo1Track:
		max_rqcd_i_low_topo_tracktwo1Track = rqcd_i_low_topo_tracktwo1Track[i]


for i in range(len(rqcd_i_high_topo_tracktwo1Track)):
        if rqcd_i_high_topo_tracktwo1Track[i]<min_rqcd_i_high_topo_tracktwo1Track:
                min_rqcd_i_high_topo_tracktwo1Track = rqcd_i_high_topo_tracktwo1Track[i]
        if rqcd_i_high_topo_tracktwo1Track[i]>max_rqcd_i_high_topo_tracktwo1Track:
                max_rqcd_i_high_topo_tracktwo1Track = rqcd_i_high_topo_tracktwo1Track[i]

print "TOPO_tracktwo1Track: sys_i_low =", ((max_rqcd_i_low_topo_tracktwo1Track - min_rqcd_i_low_topo_tracktwo1Track)/2)
print "TOPO_tracktwo1Track: sys_i_high =", ((max_rqcd_i_high_topo_tracktwo1Track - min_rqcd_i_high_topo_tracktwo1Track)/2)
print "TOPO_tracktwo1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_tracktwo1Track - min_rqcd_i_low_topo_tracktwo1Track)/2)/rqcd_i_low_tracktwo1Track_val
print "TOPO_tracktwo1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_tracktwo1Track - min_rqcd_i_high_topo_tracktwo1Track)/2)/rqcd_i_high_tracktwo1Track_val

rqcd_i_low_ptvar_tracktwo1Track = [1.180, 1.181, 1.182, 1.168, 1.163, 1.156]
rqcd_i_high_ptvar_tracktwo1Track = [1.289, 1.278, 1.277, 1.266, 1.260, 1.251]

min_rqcd_i_low_ptvar_tracktwo1Track = 2
max_rqcd_i_low_ptvar_tracktwo1Track = 0
min_rqcd_i_high_ptvar_tracktwo1Track = 2
max_rqcd_i_high_ptvar_tracktwo1Track = 0

for i in range(len(rqcd_i_low_ptvar_tracktwo1Track)):
        if rqcd_i_low_ptvar_tracktwo1Track[i]<min_rqcd_i_low_ptvar_tracktwo1Track:
                min_rqcd_i_low_ptvar_tracktwo1Track = rqcd_i_low_ptvar_tracktwo1Track[i]
        if rqcd_i_low_ptvar_tracktwo1Track[i]>max_rqcd_i_low_ptvar_tracktwo1Track:
                max_rqcd_i_low_ptvar_tracktwo1Track = rqcd_i_low_ptvar_tracktwo1Track[i]


for i in range(len(rqcd_i_high_ptvar_tracktwo1Track)):
        if rqcd_i_high_ptvar_tracktwo1Track[i]<min_rqcd_i_high_ptvar_tracktwo1Track:
                min_rqcd_i_high_ptvar_tracktwo1Track = rqcd_i_high_ptvar_tracktwo1Track[i]
        if rqcd_i_high_ptvar_tracktwo1Track[i]>max_rqcd_i_high_ptvar_tracktwo1Track:
                max_rqcd_i_high_ptvar_tracktwo1Track = rqcd_i_high_ptvar_tracktwo1Track[i]

print "PTVAR_tracktwo1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_tracktwo1Track - min_rqcd_i_low_ptvar_tracktwo1Track)/2)
print "PTVAR_tracktwo1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_tracktwo1Track - min_rqcd_i_high_ptvar_tracktwo1Track)/2)
print "PTVAR_tracktwo1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_tracktwo1Track - min_rqcd_i_low_ptvar_tracktwo1Track)/2)/rqcd_i_low_tracktwo1Track_val
print "PTVAR_tracktwo1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_tracktwo1Track - min_rqcd_i_high_ptvar_tracktwo1Track)/2)/rqcd_i_high_tracktwo1Track_val
print ""
print "---> total sys tracktwo1Track low pt =", max( ((max_rqcd_i_low_topo_tracktwo1Track - min_rqcd_i_low_topo_tracktwo1Track)/2), ((max_rqcd_i_low_ptvar_tracktwo1Track - min_rqcd_i_low_ptvar_tracktwo1Track)/2))
print "---> total sys tracktwo1Track high pt =", max( ((max_rqcd_i_high_topo_tracktwo1Track - min_rqcd_i_high_topo_tracktwo1Track)/2), ((max_rqcd_i_high_ptvar_tracktwo1Track - min_rqcd_i_high_ptvar_tracktwo1Track)/2) )
print ""
print "---> total sys tracktwo1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_tracktwo1Track - min_rqcd_i_low_topo_tracktwo1Track)/2)/rqcd_i_low_tracktwo1Track_val, ((max_rqcd_i_low_ptvar_tracktwo1Track - min_rqcd_i_low_ptvar_tracktwo1Track)/2)/rqcd_i_low_tracktwo1Track_val )
print "---> total sys tracktwo1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_tracktwo1Track - min_rqcd_i_high_topo_tracktwo1Track)/2)/rqcd_i_high_tracktwo1Track_val, ((max_rqcd_i_high_ptvar_tracktwo1Track - min_rqcd_i_high_ptvar_tracktwo1Track)/2)/rqcd_i_high_tracktwo1Track_val )


# ----------------------------------- #
#     	   L1TAU12IM1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_L1TAU12IM1Track_val = 1.118 
rqcd_i_high_L1TAU12IM1Track_val = 1.176

rqcd_i_low_topo_L1TAU12IM1Track = [1.117, 1.133, 1.142, 1.146, 1.152, 1.148, 1.146, 1.146, 1.146, 1.142, 1.140, 1.140, 1.137, 1.140, 1.139, 1.137, 1.138, 1.137, 1.136, 1.133, 1.133]
rqcd_i_high_topo_L1TAU12IM1Track = [1.188, 1.188, 1.191, 1.198, 1.198, 1.194, 1.186, 1.184, 1.184, 1.187, 1.189, 1.188, 1.187, 1.191, 1.193, 1.191, 1.188, 1.187, 1.187, 1.186, 1.185]

min_rqcd_i_low_topo_L1TAU12IM1Track = 2
max_rqcd_i_low_topo_L1TAU12IM1Track = 0
min_rqcd_i_high_topo_L1TAU12IM1Track = 2
max_rqcd_i_high_topo_L1TAU12IM1Track = 0

for i in range(len(rqcd_i_low_topo_L1TAU12IM1Track)):
	if rqcd_i_low_topo_L1TAU12IM1Track[i]<min_rqcd_i_low_topo_L1TAU12IM1Track:
		min_rqcd_i_low_topo_L1TAU12IM1Track = rqcd_i_low_topo_L1TAU12IM1Track[i]
	if rqcd_i_low_topo_L1TAU12IM1Track[i]>max_rqcd_i_low_topo_L1TAU12IM1Track:
		max_rqcd_i_low_topo_L1TAU12IM1Track = rqcd_i_low_topo_L1TAU12IM1Track[i]


for i in range(len(rqcd_i_high_topo_L1TAU12IM1Track)):
        if rqcd_i_high_topo_L1TAU12IM1Track[i]<min_rqcd_i_high_topo_L1TAU12IM1Track:
                min_rqcd_i_high_topo_L1TAU12IM1Track = rqcd_i_high_topo_L1TAU12IM1Track[i]
        if rqcd_i_high_topo_L1TAU12IM1Track[i]>max_rqcd_i_high_topo_L1TAU12IM1Track:
                max_rqcd_i_high_topo_L1TAU12IM1Track = rqcd_i_high_topo_L1TAU12IM1Track[i]

print "TOPO_L1TAU12IM1Track: sys_i_low =", ((max_rqcd_i_low_topo_L1TAU12IM1Track - min_rqcd_i_low_topo_L1TAU12IM1Track)/2)
print "TOPO_L1TAU12IM1Track: sys_i_high =", ((max_rqcd_i_high_topo_L1TAU12IM1Track - min_rqcd_i_high_topo_L1TAU12IM1Track)/2)
print "TOPO_L1TAU12IM1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_L1TAU12IM1Track - min_rqcd_i_low_topo_L1TAU12IM1Track)/2)/rqcd_i_low_L1TAU12IM1Track_val
print "TOPO_L1TAU12IM1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_L1TAU12IM1Track - min_rqcd_i_high_topo_L1TAU12IM1Track)/2)/rqcd_i_high_L1TAU12IM1Track_val

rqcd_i_low_ptvar_L1TAU12IM1Track = [1.181, 1.178, 1.177, 1.168, 1.162, 1.153]
rqcd_i_high_ptvar_L1TAU12IM1Track = [1.257, 1.246, 1.249, 1.243, 1.238, 1.233]

min_rqcd_i_low_ptvar_L1TAU12IM1Track = 2
max_rqcd_i_low_ptvar_L1TAU12IM1Track = 0
min_rqcd_i_high_ptvar_L1TAU12IM1Track = 2
max_rqcd_i_high_ptvar_L1TAU12IM1Track = 0

for i in range(len(rqcd_i_low_ptvar_L1TAU12IM1Track)):
        if rqcd_i_low_ptvar_L1TAU12IM1Track[i]<min_rqcd_i_low_ptvar_L1TAU12IM1Track:
                min_rqcd_i_low_ptvar_L1TAU12IM1Track = rqcd_i_low_ptvar_L1TAU12IM1Track[i]
        if rqcd_i_low_ptvar_L1TAU12IM1Track[i]>max_rqcd_i_low_ptvar_L1TAU12IM1Track:
                max_rqcd_i_low_ptvar_L1TAU12IM1Track = rqcd_i_low_ptvar_L1TAU12IM1Track[i]


for i in range(len(rqcd_i_high_ptvar_L1TAU12IM1Track)):
        if rqcd_i_high_ptvar_L1TAU12IM1Track[i]<min_rqcd_i_high_ptvar_L1TAU12IM1Track:
                min_rqcd_i_high_ptvar_L1TAU12IM1Track = rqcd_i_high_ptvar_L1TAU12IM1Track[i]
        if rqcd_i_high_ptvar_L1TAU12IM1Track[i]>max_rqcd_i_high_ptvar_L1TAU12IM1Track:
                max_rqcd_i_high_ptvar_L1TAU12IM1Track = rqcd_i_high_ptvar_L1TAU12IM1Track[i]

print "PTVAR_L1TAU12IM1Track: sys_i_low =", ((max_rqcd_i_low_ptvar_L1TAU12IM1Track - min_rqcd_i_low_ptvar_L1TAU12IM1Track)/2)
print "PTVAR_L1TAU12IM1Track: sys_i_high =", ((max_rqcd_i_high_ptvar_L1TAU12IM1Track - min_rqcd_i_high_ptvar_L1TAU12IM1Track)/2)
print "PTVAR_L1TAU12IM1Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_L1TAU12IM1Track - min_rqcd_i_low_ptvar_L1TAU12IM1Track)/2)/rqcd_i_low_L1TAU12IM1Track_val
print "PTVAR_L1TAU12IM1Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_L1TAU12IM1Track - min_rqcd_i_high_ptvar_L1TAU12IM1Track)/2)/rqcd_i_high_L1TAU12IM1Track_val
print ""
print "---> total sys L1TAU12IM1Track low pt =", max( ((max_rqcd_i_low_topo_L1TAU12IM1Track - min_rqcd_i_low_topo_L1TAU12IM1Track)/2), ((max_rqcd_i_low_ptvar_L1TAU12IM1Track - min_rqcd_i_low_ptvar_L1TAU12IM1Track)/2))
print "---> total sys L1TAU12IM1Track high pt =", max( ((max_rqcd_i_high_topo_L1TAU12IM1Track - min_rqcd_i_high_topo_L1TAU12IM1Track)/2), ((max_rqcd_i_high_ptvar_L1TAU12IM1Track - min_rqcd_i_high_ptvar_L1TAU12IM1Track)/2) )
print ""
print "---> total sys L1TAU12IM1Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_L1TAU12IM1Track - min_rqcd_i_low_topo_L1TAU12IM1Track)/2)/rqcd_i_low_L1TAU12IM1Track_val, ((max_rqcd_i_low_ptvar_L1TAU12IM1Track - min_rqcd_i_low_ptvar_L1TAU12IM1Track)/2)/rqcd_i_low_L1TAU12IM1Track_val )
print "---> total sys L1TAU12IM1Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_L1TAU12IM1Track - min_rqcd_i_high_topo_L1TAU12IM1Track)/2)/rqcd_i_high_L1TAU12IM1Track_val, ((max_rqcd_i_high_ptvar_L1TAU12IM1Track - min_rqcd_i_high_ptvar_L1TAU12IM1Track)/2)/rqcd_i_high_L1TAU12IM1Track_val )



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

rqcd_i_low_topo_3track = [1.296, 1.294, 1.268, 1.267, 1.262, 1.259, 1.258, 1.257, 1.263, 1.264, 1.260, 1.258, 1.254, 1.255, 1.260, 1.259, 1.266, 1.266] 
rqcd_i_high_topo_3track = [1.525, 1.548, 1.545, 1.535, 1.530, 1.515, 1.511, 1.512, 1.491, 1.491, 1.484, 1.498, 1.489, 1.478, 1.479, 1.490, 1.493, 1.497]

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

rqcd_i_low_ptvar_3track = [1.293, 1.279, 1.274, 1.280, 1.277, 1.271]
rqcd_i_high_ptvar_3track = [1.578, 1.573, 1.555, 1.551, 1.542, 1.558]

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

rqcd_i_low_topo_3track_25med = [1.257, 1.257, 1.240, 1.217, 1.225, 1.231, 1.220, 1.222, 1.225, 1.227, 1.232, 1.228, 1.224, 1.227, 1.227, 1.229, 1.226, 1.238, 1.232, 1.248, 1.251, 1.252]
rqcd_i_high_topo_3track_25med = [1.706, 1.706, 1.736, 1.752, 1.739, 1.724, 1.699, 1.688, 1.678, 1.660, 1.660, 1.649, 1.667, 1.657, 1.648, 1.643, 1.659, 1.663, 1.667, 1.664, 1.670, 1.662]

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

rqcd_i_low_ptvar_3track_25med = [1.191, 1.184, 1.177, 1.188, 1.192, 1.198]
rqcd_i_high_ptvar_3track_25med = [1.941, 1.900, 1.865, 1.854, 1.820, 1.833]

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

rqcd_i_low_topo_3track_35med = [1.413, 1.320, 1.346, 1.351, 1.420, 1.387, 1.410, 1.391, 1.353, 1.344, 1.301, 1.298, 1.310, 1.310, 1.335, 1.359, 1.359, 1.338, 1.386, 1.398, 1.371]
rqcd_i_high_topo_3track_35med = [1.737, 1.780, 1.797, 1.773, 1.750, 1.736, 1.749, 1.727, 1.698, 1.697, 1.682, 1.705, 1.703, 1.693, 1.690, 1.703, 1.709, 1.707, 1.701, 1.705, 1.695]

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

rqcd_i_low_ptvar_3track_35med = [1.939, 1.736, 1.796, 1.751, 1.685, 1.693]
rqcd_i_high_ptvar_3track_35med = [1.955, 1.911, 1.901, 1.913, 1.868, 1.885]

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

rqcd_i_low_topo_3track_50L1TAU12med = [1.579, 1.494, 1.519, 1.506, 1.577, 1.506, 1.574, 1.506, 1.495, 1.499, 1.451, 1.417, 1.392, 1.367, 1.403, 1.430, 1.430, 1.398, 1.433, 1.408, 1.393]
rqcd_i_high_topo_3track_50L1TAU12med = [1.757, 1.758, 1.798, 1.750, 1.734, 1.732, 1.737, 1.710, 1.708, 1.703, 1.685, 1.717, 1.715, 1.712, 1.705, 1.731, 1.740, 1.731, 1.736, 1.731, 1.734]

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

rqcd_i_low_ptvar_3track_50L1TAU12med = [2.524, 2.049, 2.174, 2.164, 2.099, 2.210]
rqcd_i_high_ptvar_3track_50L1TAU12med = [1.949, 1.967, 1.892, 1.934, 1.904, 1.946]

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

rqcd_i_low_topo_3track_80med = [0.818, 0.818, 0.818, ]
rqcd_i_high_topo_3track_80med = [2.302, 2.300, 2.398, 2.342, 2.315, 2.325, 2.305, 2.279, 2.234, 2.192, 2.168, 2.164, 2.156, 2.141, 2.134, 2.172, 2.197, 2.195, 2.200, 2.199, 2.224]

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

rqcd_i_low_ptvar_3track_80med = [7.276, 7.213, 7.213, 7.213, 2.938, 2.938]
rqcd_i_high_ptvar_3track_80med = [3.180, 3.062, 2.663, 2.774, 2.815, 2.995]

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

rqcd_i_low_topo_3track_80L1TAU60med = []
rqcd_i_high_topo_3track_80L1TAU60med = [2.324, 2.329, 2.453, 2.400, 2.361, 2.318, 2.318, 2.261, 2.221, 2.152, 2.109, 2.087, 2.086, 2.065, 2.075, 2.112, 2.131, 2.150, 2.157, 2.176, 2.204]

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

rqcd_i_low_ptvar_3track_80L1TAU60med = [6.394, 6.256, 6.256, 6.256, 6.256, 6.256]
rqcd_i_high_ptvar_3track_80L1TAU60med = [3.445, 3.771, 3.004, 3.004, 2.856, 3.068]

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

################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
rqcd_i_low_3track_125med_val = 0.569 
rqcd_i_high_3track_125med_val = 0.923

rqcd_i_low_topo_3track_125med = [0.571, 0.571, 0.571, 0.571, 0.571, 0.571, 0.714, 0.714, 0.714, 0.670, 0.586, 0.586, 0.586, 0.586, 0.586, 0.586, 0.586, 0.521, 0.521, 0.521, 0.521]
rqcd_i_high_topo_3track_125med = [2.039, 2.030, 2.052, 2.002, 2.050, 1.986, 2.008, 1.966, 1.861, 1.795, 1.732, 1.683, 1.683, 1.627, 1.644, 1.710, 1.743, 1.743, 1.747, 1.747, 1.758]

min_rqcd_i_low_topo_3track_125med = 2
max_rqcd_i_low_topo_3track_125med = 0
min_rqcd_i_high_topo_3track_125med = 2
max_rqcd_i_high_topo_3track_125med = 0

for i in range(len(rqcd_i_low_topo_3track_125med)):
	if rqcd_i_low_topo_3track_125med[i]<min_rqcd_i_low_topo_3track_125med:
		min_rqcd_i_low_topo_3track_125med = rqcd_i_low_topo_3track_125med[i]
	if rqcd_i_low_topo_3track_125med[i]>max_rqcd_i_low_topo_3track_125med:
		max_rqcd_i_low_topo_3track_125med = rqcd_i_low_topo_3track_125med[i]


for i in range(len(rqcd_i_high_topo_3track_125med)):
        if rqcd_i_high_topo_3track_125med[i]<min_rqcd_i_high_topo_3track_125med:
                min_rqcd_i_high_topo_3track_125med = rqcd_i_high_topo_3track_125med[i]
        if rqcd_i_high_topo_3track_125med[i]>max_rqcd_i_high_topo_3track_125med:
                max_rqcd_i_high_topo_3track_125med = rqcd_i_high_topo_3track_125med[i]

print "TOPO_125med: sys_i_low =", ((max_rqcd_i_low_topo_3track_125med - min_rqcd_i_low_topo_3track_125med)/2)
print "TOPO_125med: sys_i_high =", ((max_rqcd_i_high_topo_3track_125med - min_rqcd_i_high_topo_3track_125med)/2)
print "TOPO_125med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_125med - min_rqcd_i_low_topo_3track_125med)/2)/rqcd_i_low_3track_125med_val
print "TOPO_125med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_125med - min_rqcd_i_high_topo_3track_125med)/2)/rqcd_i_high_3track_125med_val

rqcd_i_low_ptvar_3track_125med = []
rqcd_i_high_ptvar_3track_125med = []

min_rqcd_i_low_ptvar_3track_125med = 2
max_rqcd_i_low_ptvar_3track_125med = 0
min_rqcd_i_high_ptvar_3track_125med = 2
max_rqcd_i_high_ptvar_3track_125med = 0

for i in range(len(rqcd_i_low_ptvar_3track_125med)):
        if rqcd_i_low_ptvar_3track_125med[i]<min_rqcd_i_low_ptvar_3track_125med:
                min_rqcd_i_low_ptvar_3track_125med = rqcd_i_low_ptvar_3track_125med[i]
        if rqcd_i_low_ptvar_3track_125med[i]>max_rqcd_i_low_ptvar_3track_125med:
                max_rqcd_i_low_ptvar_3track_125med = rqcd_i_low_ptvar_3track_125med[i]


for i in range(len(rqcd_i_high_ptvar_3track_125med)):
        if rqcd_i_high_ptvar_3track_125med[i]<min_rqcd_i_high_ptvar_3track_125med:
                min_rqcd_i_high_ptvar_3track_125med = rqcd_i_high_ptvar_3track_125med[i]
        if rqcd_i_high_ptvar_3track_125med[i]>max_rqcd_i_high_ptvar_3track_125med:
                max_rqcd_i_high_ptvar_3track_125med = rqcd_i_high_ptvar_3track_125med[i]

print "PTVAR_125med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_125med - min_rqcd_i_low_ptvar_3track_125med)/2)
print "PTVAR_125med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_125med - min_rqcd_i_high_ptvar_3track_125med)/2)
print "PTVAR_125med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_125med - min_rqcd_i_low_ptvar_3track_125med)/2)/rqcd_i_low_3track_125med_val
print "PTVAR_125med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_125med - min_rqcd_i_high_ptvar_3track_125med)/2)/rqcd_i_high_3track_125med_val
print ""
print "---> total sys 125med low pt =", max( ((max_rqcd_i_low_topo_3track_125med - min_rqcd_i_low_topo_3track_125med)/2), ((max_rqcd_i_low_ptvar_3track_125med - min_rqcd_i_low_ptvar_3track_125med)/2))
print "---> total sys 125med high pt =", max( ((max_rqcd_i_high_topo_3track_125med - min_rqcd_i_high_topo_3track_125med)/2), ((max_rqcd_i_high_ptvar_3track_125med - min_rqcd_i_high_ptvar_3track_125med)/2) )
print ""
print "---> total sys 125med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_125med - min_rqcd_i_low_topo_3track_125med)/2)/rqcd_i_low_3track_125med_val, ((max_rqcd_i_low_ptvar_3track_125med - min_rqcd_i_low_ptvar_3track_125med)/2)/rqcd_i_low_3track_125med_val )
print "---> total sys 125med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_125med - min_rqcd_i_high_topo_3track_125med)/2)/rqcd_i_high_3track_125med_val, ((max_rqcd_i_high_ptvar_3track_125med - min_rqcd_i_high_ptvar_3track_125med)/2)/rqcd_i_high_3track_125med_val )

################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
rqcd_i_low_3track_160med_val = 0.672 
rqcd_i_high_3track_160med_val = 1.482

rqcd_i_low_topo_3track_160med = [1.000, 0.844, 0.562, 0.562, 0.422]
rqcd_i_high_topo_3track_160med = [2.356, 2.189, 1.764, 1.764, 1.718, 1.808, 1.808, 1.847, 1.651, 1.690, 1.729, 1.768, 2.409, 2.193, 2.257, 2.120, 2.114, 2.102, 1.843]

min_rqcd_i_low_topo_3track_160med = 2
max_rqcd_i_low_topo_3track_160med = 0
min_rqcd_i_high_topo_3track_160med = 2
max_rqcd_i_high_topo_3track_160med = 0

for i in range(len(rqcd_i_low_topo_3track_160med)):
	if rqcd_i_low_topo_3track_160med[i]<min_rqcd_i_low_topo_3track_160med:
		min_rqcd_i_low_topo_3track_160med = rqcd_i_low_topo_3track_160med[i]
	if rqcd_i_low_topo_3track_160med[i]>max_rqcd_i_low_topo_3track_160med:
		max_rqcd_i_low_topo_3track_160med = rqcd_i_low_topo_3track_160med[i]


for i in range(len(rqcd_i_high_topo_3track_160med)):
        if rqcd_i_high_topo_3track_160med[i]<min_rqcd_i_high_topo_3track_160med:
                min_rqcd_i_high_topo_3track_160med = rqcd_i_high_topo_3track_160med[i]
        if rqcd_i_high_topo_3track_160med[i]>max_rqcd_i_high_topo_3track_160med:
                max_rqcd_i_high_topo_3track_160med = rqcd_i_high_topo_3track_160med[i]

print "TOPO_160med: sys_i_low =", ((max_rqcd_i_low_topo_3track_160med - min_rqcd_i_low_topo_3track_160med)/2)
print "TOPO_160med: sys_i_high =", ((max_rqcd_i_high_topo_3track_160med - min_rqcd_i_high_topo_3track_160med)/2)
print "TOPO_160med: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_3track_160med - min_rqcd_i_low_topo_3track_160med)/2)/rqcd_i_low_3track_160med_val
print "TOPO_160med: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_3track_160med - min_rqcd_i_high_topo_3track_160med)/2)/rqcd_i_high_3track_160med_val

rqcd_i_low_ptvar_3track_160med = []
rqcd_i_high_ptvar_3track_160med = []

min_rqcd_i_low_ptvar_3track_160med = 2
max_rqcd_i_low_ptvar_3track_160med = 0
min_rqcd_i_high_ptvar_3track_160med = 2
max_rqcd_i_high_ptvar_3track_160med = 0

for i in range(len(rqcd_i_low_ptvar_3track_160med)):
        if rqcd_i_low_ptvar_3track_160med[i]<min_rqcd_i_low_ptvar_3track_160med:
                min_rqcd_i_low_ptvar_3track_160med = rqcd_i_low_ptvar_3track_160med[i]
        if rqcd_i_low_ptvar_3track_160med[i]>max_rqcd_i_low_ptvar_3track_160med:
                max_rqcd_i_low_ptvar_3track_160med = rqcd_i_low_ptvar_3track_160med[i]


for i in range(len(rqcd_i_high_ptvar_3track_160med)):
        if rqcd_i_high_ptvar_3track_160med[i]<min_rqcd_i_high_ptvar_3track_160med:
                min_rqcd_i_high_ptvar_3track_160med = rqcd_i_high_ptvar_3track_160med[i]
        if rqcd_i_high_ptvar_3track_160med[i]>max_rqcd_i_high_ptvar_3track_160med:
                max_rqcd_i_high_ptvar_3track_160med = rqcd_i_high_ptvar_3track_160med[i]

print "PTVAR_160med: sys_i_low =", ((max_rqcd_i_low_ptvar_3track_160med - min_rqcd_i_low_ptvar_3track_160med)/2)
print "PTVAR_160med: sys_i_high =", ((max_rqcd_i_high_ptvar_3track_160med - min_rqcd_i_high_ptvar_3track_160med)/2)
print "PTVAR_160med: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_3track_160med - min_rqcd_i_low_ptvar_3track_160med)/2)/rqcd_i_low_3track_160med_val
print "PTVAR_160med: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_3track_160med - min_rqcd_i_high_ptvar_3track_160med)/2)/rqcd_i_high_3track_160med_val
print ""
print "---> total sys 160med low pt =", max( ((max_rqcd_i_low_topo_3track_160med - min_rqcd_i_low_topo_3track_160med)/2), ((max_rqcd_i_low_ptvar_3track_160med - min_rqcd_i_low_ptvar_3track_160med)/2))
print "---> total sys 160med high pt =", max( ((max_rqcd_i_high_topo_3track_160med - min_rqcd_i_high_topo_3track_160med)/2), ((max_rqcd_i_high_ptvar_3track_160med - min_rqcd_i_high_ptvar_3track_160med)/2) )
print ""
print "---> total sys 160med low pt (percentage) =", max( ((max_rqcd_i_low_topo_3track_160med - min_rqcd_i_low_topo_3track_160med)/2)/rqcd_i_low_3track_160med_val, ((max_rqcd_i_low_ptvar_3track_160med - min_rqcd_i_low_ptvar_3track_160med)/2)/rqcd_i_low_3track_160med_val )
print "---> total sys 160med high pt (percentage) =", max( ((max_rqcd_i_high_topo_3track_160med - min_rqcd_i_high_topo_3track_160med)/2)/rqcd_i_high_3track_160med_val, ((max_rqcd_i_high_ptvar_3track_160med - min_rqcd_i_high_ptvar_3track_160med)/2)/rqcd_i_high_3track_160med_val )




# ----------------------------------- #
#     	  ptonly3Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_ptonly3Track_val =  1.237
rqcd_i_high_ptonly3Track_val = 1.452

rqcd_i_low_topo_ptonly3Track = [1.329, 1.318, 1.293, 1.282, 1.279, 1.274, 1.275, 1.274, 1.280, 1.274, 1.269, 1.267, 1.261, 1.263, 1.260, 1.261, 1.274, 1.274, 1.280, 1.280, 1.278]
rqcd_i_high_topo_ptonly3Track = [1.556, 1.582, 1.579, 1.573, 1.564, 1.546, 1.535, 1.537, 1.520, 1.519, 1.511, 1.526, 1.519, 1.509, 1.510, 1.519, 1.521, 1.524, 1.521, 1.521, 1.520]

min_rqcd_i_low_topo_ptonly3Track = 2
max_rqcd_i_low_topo_ptonly3Track = 0
min_rqcd_i_high_topo_ptonly3Track = 2
max_rqcd_i_high_topo_ptonly3Track = 0

for i in range(len(rqcd_i_low_topo_ptonly3Track)):
	if rqcd_i_low_topo_ptonly3Track[i]<min_rqcd_i_low_topo_ptonly3Track:
		min_rqcd_i_low_topo_ptonly3Track = rqcd_i_low_topo_ptonly3Track[i]
	if rqcd_i_low_topo_ptonly3Track[i]>max_rqcd_i_low_topo_ptonly3Track:
		max_rqcd_i_low_topo_ptonly3Track = rqcd_i_low_topo_ptonly3Track[i]


for i in range(len(rqcd_i_high_topo_ptonly3Track)):
        if rqcd_i_high_topo_ptonly3Track[i]<min_rqcd_i_high_topo_ptonly3Track:
                min_rqcd_i_high_topo_ptonly3Track = rqcd_i_high_topo_ptonly3Track[i]
        if rqcd_i_high_topo_ptonly3Track[i]>max_rqcd_i_high_topo_ptonly3Track:
                max_rqcd_i_high_topo_ptonly3Track = rqcd_i_high_topo_ptonly3Track[i]

print "TOPO_ptonly3Track: sys_i_low =", ((max_rqcd_i_low_topo_ptonly3Track - min_rqcd_i_low_topo_ptonly3Track)/2)
print "TOPO_ptonly3Track: sys_i_high =", ((max_rqcd_i_high_topo_ptonly3Track - min_rqcd_i_high_topo_ptonly3Track)/2)
print "TOPO_ptonly3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_ptonly3Track - min_rqcd_i_low_topo_ptonly3Track)/2)/rqcd_i_low_ptonly3Track_val
print "TOPO_ptonly3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_ptonly3Track - min_rqcd_i_high_topo_ptonly3Track)/2)/rqcd_i_high_ptonly3Track_val

rqcd_i_low_ptvar_ptonly3Track = [1.250, 1.250, 1.234, 1.252, 1.242, 1.236]
rqcd_i_high_ptvar_ptonly3Track = [1.674, 1.664, 1.637, 1.636, 1.617, 1.632]

min_rqcd_i_low_ptvar_ptonly3Track = 2
max_rqcd_i_low_ptvar_ptonly3Track = 0
min_rqcd_i_high_ptvar_ptonly3Track = 2
max_rqcd_i_high_ptvar_ptonly3Track = 0

for i in range(len(rqcd_i_low_ptvar_ptonly3Track)):
        if rqcd_i_low_ptvar_ptonly3Track[i]<min_rqcd_i_low_ptvar_ptonly3Track:
                min_rqcd_i_low_ptvar_ptonly3Track = rqcd_i_low_ptvar_ptonly3Track[i]
        if rqcd_i_low_ptvar_ptonly3Track[i]>max_rqcd_i_low_ptvar_ptonly3Track:
                max_rqcd_i_low_ptvar_ptonly3Track3Track = rqcd_i_low_ptvar_ptonly3Track[i]


for i in range(len(rqcd_i_high_ptvar_ptonly3Track)):
        if rqcd_i_high_ptvar_ptonly3Track[i]<min_rqcd_i_low_ptvar_ptonly3Track:
                min_rqcd_i_low_ptvar_ptonly3Track3Track = rqcd_i_high_ptvar_ptonly3Track[i]
        if rqcd_i_high_ptvar_ptonly3Track[i]>max_rqcd_i_high_ptvar_ptonly3Track:
                max_rqcd_i_high_ptvar_ptonly3Track = rqcd_i_high_ptvar_ptonly3Track[i]

print "PTVAR_ptonly3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)
print "PTVAR_ptonly3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)
print "PTVAR_ptonly3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)/rqcd_i_low_ptonly3Track_val
print "PTVAR_ptonly3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)/rqcd_i_high_ptonly3Track_val
print ""
print "---> total sys ptonly3Track low pt =", max( ((max_rqcd_i_low_topo_ptonly3Track - min_rqcd_i_low_topo_ptonly3Track)/2), ((max_rqcd_i_low_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2))
print "---> total sys ptonly3Track high pt =", max( ((max_rqcd_i_high_topo_ptonly3Track - min_rqcd_i_high_topo_ptonly3Track)/2), ((max_rqcd_i_high_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2) )
print ""
print "---> total sys ptonly3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_ptonly3Track - min_rqcd_i_low_topo_ptonly3Track)/2)/rqcd_i_low_ptonly3Track_val, ((max_rqcd_i_low_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)/rqcd_i_low_ptonly3Track_val )
print "---> total sys ptonly3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_ptonly3Track - min_rqcd_i_high_topo_ptonly3Track)/2)/rqcd_i_high_ptonly3Track_val, ((max_rqcd_i_high_ptvar_ptonly3Track - min_rqcd_i_low_ptvar_ptonly3Track)/2)/rqcd_i_high_ptonly3Track_val )


# ----------------------------------- #
#     	   tracktwo3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_tracktwo3Track_val =  1.244
rqcd_i_high_tracktwo3Track_val = 1.480

rqcd_i_low_topo_tracktwo3Track = [1.291, 1.263, 1.235, 1.228, 1.228, 1.231, 1.234, 1.234, 1.236, 1.241, 1.235, 1.234, 1.229, 1.229, 1.229, 1.232, 1.243, 1.241, 1.249, 1.248, 1.247]
rqcd_i_high_topo_tracktwo3Track = [1.603, 1.628, 1.632, 1.626, 1.612, 1.592, 1.578, 1.568, 1.548, 1.545, 1.536, 1.551, 1.543, 1.535, 1.532, 1.543, 1.546, 1.550, 1.551, 1.554, 1.551]

min_rqcd_i_low_topo_tracktwo3Track = 2
max_rqcd_i_low_topo_tracktwo3Track = 0
min_rqcd_i_high_topo_tracktwo3Track = 2
max_rqcd_i_high_topo_tracktwo3Track = 0

for i in range(len(rqcd_i_low_topo_tracktwo3Track)):
	if rqcd_i_low_topo_tracktwo3Track[i]<min_rqcd_i_low_topo_tracktwo3Track:
		min_rqcd_i_low_topo_tracktwo3Track = rqcd_i_low_topo_tracktwo3Track[i]
	if rqcd_i_low_topo_tracktwo3Track[i]>max_rqcd_i_low_topo_tracktwo3Track:
		max_rqcd_i_low_topo_tracktwo3Track = rqcd_i_low_topo_tracktwo3Track[i]


for i in range(len(rqcd_i_high_topo_tracktwo3Track)):
        if rqcd_i_high_topo_tracktwo3Track[i]<min_rqcd_i_high_topo_tracktwo3Track:
                min_rqcd_i_high_topo_tracktwo3Track = rqcd_i_high_topo_tracktwo3Track[i]
        if rqcd_i_high_topo_tracktwo3Track[i]>max_rqcd_i_high_topo_tracktwo3Track:
                max_rqcd_i_high_topo_tracktwo3Track = rqcd_i_high_topo_tracktwo3Track[i]

print "TOPO_tracktwo3Track: sys_i_low =", ((max_rqcd_i_low_topo_tracktwo3Track - min_rqcd_i_low_topo_tracktwo3Track)/2)
print "TOPO_tracktwo3Track: sys_i_high =", ((max_rqcd_i_high_topo_tracktwo3Track - min_rqcd_i_high_topo_tracktwo3Track)/2)
print "TOPO_tracktwo3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_tracktwo3Track - min_rqcd_i_low_topo_tracktwo3Track)/2)/rqcd_i_low_tracktwo3Track_val
print "TOPO_tracktwo3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_tracktwo3Track - min_rqcd_i_high_topo_tracktwo3Track)/2)/rqcd_i_high_tracktwo3Track_val

rqcd_i_low_ptvar_tracktwo3Track = [1.202, 1.207, 1.208, 1.220, 1.217, 1.214]
rqcd_i_high_ptvar_tracktwo3Track = [1.799, 1.769, 1.737, 1.725, 1.696, 1.708]

min_rqcd_i_low_ptvar_tracktwo3Track = 2
max_rqcd_i_low_ptvar_tracktwo3Track = 0
min_rqcd_i_high_ptvar_tracktwo3Track = 2
max_rqcd_i_high_ptvar_tracktwo3Track = 0

for i in range(len(rqcd_i_low_ptvar_tracktwo3Track)):
        if rqcd_i_low_ptvar_tracktwo3Track[i]<min_rqcd_i_low_ptvar_tracktwo3Track:
                min_rqcd_i_low_ptvar_tracktwo3Track = rqcd_i_low_ptvar_tracktwo3Track[i]
        if rqcd_i_low_ptvar_tracktwo3Track[i]>max_rqcd_i_low_ptvar_tracktwo3Track:
                max_rqcd_i_low_ptvar_tracktwo3Track = rqcd_i_low_ptvar_tracktwo3Track[i]


for i in range(len(rqcd_i_high_ptvar_tracktwo3Track)):
        if rqcd_i_high_ptvar_tracktwo3Track[i]<min_rqcd_i_high_ptvar_tracktwo3Track:
                min_rqcd_i_high_ptvar_tracktwo3Track = rqcd_i_high_ptvar_tracktwo3Track[i]
        if rqcd_i_high_ptvar_tracktwo3Track[i]>max_rqcd_i_high_ptvar_tracktwo3Track:
                max_rqcd_i_high_ptvar_tracktwo3Track = rqcd_i_high_ptvar_tracktwo3Track[i]

print "PTVAR_tracktwo3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_tracktwo3Track - min_rqcd_i_low_ptvar_tracktwo3Track)/2)
print "PTVAR_tracktwo3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_tracktwo3Track - min_rqcd_i_high_ptvar_tracktwo3Track)/2)
print "PTVAR_tracktwo3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_tracktwo3Track - min_rqcd_i_low_ptvar_tracktwo3Track)/2)/rqcd_i_low_tracktwo3Track_val
print "PTVAR_tracktwo3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_tracktwo3Track - min_rqcd_i_high_ptvar_tracktwo3Track)/2)/rqcd_i_high_tracktwo3Track_val
print ""
print "---> total sys tracktwo3Track low pt =", max( ((max_rqcd_i_low_topo_tracktwo3Track - min_rqcd_i_low_topo_tracktwo3Track)/2), ((max_rqcd_i_low_ptvar_tracktwo3Track - min_rqcd_i_low_ptvar_tracktwo3Track)/2))
print "---> total sys tracktwo3Track high pt =", max( ((max_rqcd_i_high_topo_tracktwo3Track - min_rqcd_i_high_topo_tracktwo3Track)/2), ((max_rqcd_i_high_ptvar_tracktwo3Track - min_rqcd_i_high_ptvar_tracktwo3Track)/2) )
print ""
print "---> total sys tracktwo3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_tracktwo3Track - min_rqcd_i_low_topo_tracktwo3Track)/2)/rqcd_i_low_tracktwo3Track_val, ((max_rqcd_i_low_ptvar_tracktwo3Track - min_rqcd_i_low_ptvar_tracktwo3Track)/2)/rqcd_i_low_tracktwo3Track_val )
print "---> total sys tracktwo3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_tracktwo3Track - min_rqcd_i_high_topo_tracktwo3Track)/2)/rqcd_i_high_tracktwo3Track_val, ((max_rqcd_i_high_ptvar_tracktwo3Track - min_rqcd_i_high_ptvar_tracktwo3Track)/2)/rqcd_i_high_tracktwo3Track_val )

# ----------------------------------- #
#     	   L1TAU12IM3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
rqcd_i_low_L1TAU12IM3Track_val = 1.242 
rqcd_i_high_L1TAU12IM3Track_val = 1.451

rqcd_i_low_topo_L1TAU12IM3Track = [1.327, 1.315, 1.294, 1.286, 1.283, 1.279, 1.281, 1.275, 1.281, 1.274, 1.269, 1.266, 1.261, 1.263, 1.262, 1.260, 1.272, 1.272, 1.277, 1.278, 1.276]
rqcd_i_high_topo_L1TAU12IM3Track = [1.554, 1.580, 1.578, 1.571, 1.563, 1.544, 1.533, 1.535, 1.516, 1.516, 1.508, 1.524, 1.516, 1.507, 1.507, 1.516, 1.519, 1.521, 1.519, 1.519, 1.518]

min_rqcd_i_low_topo_L1TAU12IM3Track = 2
max_rqcd_i_low_topo_L1TAU12IM3Track = 0
min_rqcd_i_high_topo_L1TAU12IM3Track = 2
max_rqcd_i_high_topo_L1TAU12IM3Track = 0

for i in range(len(rqcd_i_low_topo_L1TAU12IM3Track)):
	if rqcd_i_low_topo_L1TAU12IM3Track[i]<min_rqcd_i_low_topo_L1TAU12IM3Track:
		min_rqcd_i_low_topo_L1TAU12IM3Track = rqcd_i_low_topo_L1TAU12IM3Track[i]
	if rqcd_i_low_topo_L1TAU12IM3Track[i]>max_rqcd_i_low_topo_L1TAU12IM3Track:
		max_rqcd_i_low_topo_L1TAU12IM3Track = rqcd_i_low_topo_L1TAU12IM3Track[i]


for i in range(len(rqcd_i_high_topo_L1TAU12IM3Track)):
        if rqcd_i_high_topo_L1TAU12IM3Track[i]<min_rqcd_i_high_topo_L1TAU12IM3Track:
                min_rqcd_i_high_topo_L1TAU12IM3Track = rqcd_i_high_topo_L1TAU12IM3Track[i]
        if rqcd_i_high_topo_L1TAU12IM3Track[i]>max_rqcd_i_high_topo_L1TAU12IM3Track:
                max_rqcd_i_high_topo_L1TAU12IM3Track = rqcd_i_high_topo_L1TAU12IM3Track[i]

print "TOPO_L1TAU12IM3Track: sys_i_low =", ((max_rqcd_i_low_topo_L1TAU12IM3Track - min_rqcd_i_low_topo_L1TAU12IM3Track)/2)
print "TOPO_L1TAU12IM3Track: sys_i_high =", ((max_rqcd_i_high_topo_L1TAU12IM3Track - min_rqcd_i_high_topo_L1TAU12IM3Track)/2)
print "TOPO_L1TAU12IM3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_topo_L1TAU12IM3Track - min_rqcd_i_low_topo_L1TAU12IM3Track)/2)/rqcd_i_low_L1TAU12IM3Track_val
print "TOPO_L1TAU12IM3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_topo_L1TAU12IM3Track - min_rqcd_i_high_topo_L1TAU12IM3Track)/2)/rqcd_i_high_L1TAU12IM3Track_val

rqcd_i_low_ptvar_L1TAU12IM3Track = [1.243, 1.248, 1.235, 1.253, 1.241, 1.237]
rqcd_i_high_ptvar_L1TAU12IM3Track = [1.671, 1.664, 1.637, 1.634, 1.615, 1.630]

min_rqcd_i_low_ptvar_L1TAU12IM3Track = 2
max_rqcd_i_low_ptvar_L1TAU12IM3Track = 0
min_rqcd_i_high_ptvar_L1TAU12IM3Track = 2
max_rqcd_i_high_ptvar_L1TAU12IM3Track = 0

for i in range(len(rqcd_i_low_ptvar_L1TAU12IM3Track)):
        if rqcd_i_low_ptvar_L1TAU12IM3Track[i]<min_rqcd_i_low_ptvar_L1TAU12IM3Track:
                min_rqcd_i_low_ptvar_L1TAU12IM3Track = rqcd_i_low_ptvar_L1TAU12IM3Track[i]
        if rqcd_i_low_ptvar_L1TAU12IM3Track[i]>max_rqcd_i_low_ptvar_L1TAU12IM3Track:
                max_rqcd_i_low_ptvar_L1TAU12IM3Track = rqcd_i_low_ptvar_L1TAU12IM3Track[i]


for i in range(len(rqcd_i_high_ptvar_L1TAU12IM3Track)):
        if rqcd_i_high_ptvar_L1TAU12IM3Track[i]<min_rqcd_i_high_ptvar_L1TAU12IM3Track:
                min_rqcd_i_high_ptvar_L1TAU12IM3Track = rqcd_i_high_ptvar_L1TAU12IM3Track[i]
        if rqcd_i_high_ptvar_L1TAU12IM3Track[i]>max_rqcd_i_high_ptvar_L1TAU12IM3Track:
                max_rqcd_i_high_ptvar_L1TAU12IM3Track = rqcd_i_high_ptvar_L1TAU12IM3Track[i]

print "PTVAR_L1TAU12IM3Track: sys_i_low =", ((max_rqcd_i_low_ptvar_L1TAU12IM3Track - min_rqcd_i_low_ptvar_L1TAU12IM3Track)/2)
print "PTVAR_L1TAU12IM3Track: sys_i_high =", ((max_rqcd_i_high_ptvar_L1TAU12IM3Track - min_rqcd_i_high_ptvar_L1TAU12IM3Track)/2)
print "PTVAR_L1TAU12IM3Track: sys_i_low (percentage) =", ((max_rqcd_i_low_ptvar_L1TAU12IM3Track - min_rqcd_i_low_ptvar_L1TAU12IM3Track)/2)/rqcd_i_low_L1TAU12IM3Track_val
print "PTVAR_L1TAU12IM3Track: sys_i_high (percentage) =", ((max_rqcd_i_high_ptvar_L1TAU12IM3Track - min_rqcd_i_high_ptvar_L1TAU12IM3Track)/2)/rqcd_i_high_L1TAU12IM3Track_val
print ""
print "---> total sys L1TAU12IM3Track low pt =", max( ((max_rqcd_i_low_topo_L1TAU12IM3Track - min_rqcd_i_low_topo_L1TAU12IM3Track)/2), ((max_rqcd_i_low_ptvar_L1TAU12IM3Track - min_rqcd_i_low_ptvar_L1TAU12IM3Track)/2))
print "---> total sys L1TAU12IM3Track high pt =", max( ((max_rqcd_i_high_topo_L1TAU12IM3Track - min_rqcd_i_high_topo_L1TAU12IM3Track)/2), ((max_rqcd_i_high_ptvar_L1TAU12IM3Track - min_rqcd_i_high_ptvar_L1TAU12IM3Track)/2) )
print ""
print "---> total sys L1TAU12IM3Track low pt (percentage) =", max( ((max_rqcd_i_low_topo_L1TAU12IM3Track - min_rqcd_i_low_topo_L1TAU12IM3Track)/2)/rqcd_i_low_L1TAU12IM3Track_val, ((max_rqcd_i_low_ptvar_L1TAU12IM3Track - min_rqcd_i_low_ptvar_L1TAU12IM3Track)/2)/rqcd_i_low_L1TAU12IM3Track_val )
print "---> total sys L1TAU12IM3Track high pt (percentage) =", max( ((max_rqcd_i_high_topo_L1TAU12IM3Track - min_rqcd_i_high_topo_L1TAU12IM3Track)/2)/rqcd_i_high_L1TAU12IM3Track_val, ((max_rqcd_i_high_ptvar_L1TAU12IM3Track - min_rqcd_i_high_ptvar_L1TAU12IM3Track)/2)/rqcd_i_high_L1TAU12IM3Track_val )


