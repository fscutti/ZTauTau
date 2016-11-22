# incl no trig

from math import *

print "INCLUSIVE"
print ""
print "*******************"
print ""

print "------------------------------"
print "        NO TRIGGER"
print "------------------------------"


kw_os_i_low_val = 1.409
kw_os_i_high_val = 1.486

kw_os_i_low = [1.405, 1.402, 1.399, 1.397]#, 1.391, 1.395, 1.383, 1.367, 1.337, 1.271]
kw_os_i_high = [1.474, 1.472, 1.467, 1.432]#, 1.413, 1.395, 1.334, 1.263, 1.191, 1.061]

diff_kw_os_i_low_val = 0
diff_kw_os_i_high_val = 0

min_kw_os_i_low = 20
max_kw_os_i_low = 0
min_kw_os_i_high = 20
max_kw_os_i_high = 0

for i in range(len(kw_os_i_low)):
	if kw_os_i_low[i]<min_kw_os_i_low:
		min_kw_os_i_low = kw_os_i_low[i]
	if kw_os_i_low[i]>max_kw_os_i_low:
		max_kw_os_i_low = kw_os_i_low[i]


for i in range(len(kw_os_i_high)):
        if kw_os_i_high[i]<min_kw_os_i_high:
                min_kw_os_i_high = kw_os_i_high[i]
        if kw_os_i_high[i]>max_kw_os_i_high:
                max_kw_os_i_high = kw_os_i_high[i]

print "no_trig: sys_i_low =", ((max_kw_os_i_low - min_kw_os_i_low)/2)
print "no_trig: sys_i_high =", ((max_kw_os_i_high - min_kw_os_i_high)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_os_i_low - min_kw_os_i_low)/2)/kw_os_i_low_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_os_i_high - min_kw_os_i_high)/2)/kw_os_i_high_val


print " ----------------------------------- "
print "     	   25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT
kw_os_i_low_25med_val = 1.366 
kw_os_i_high_25med_val = 1.377

kw_os_i_low_25med = [1.361, 1.358, 1.355, 1.346]#, 1.352, 1.346, 1.341, 1.309, 1.281, 1.182]
kw_os_i_high_25med = [1.369, 1.369, 1.367, 1.326]#, 1.300, 1.273, 1.207, 1.100, 1.008, 0.873]

min_kw_os_i_low_25med = 20
max_kw_os_i_low_25med = 0
min_kw_os_i_high_25med = 20
max_kw_os_i_high_25med = 0

for i in range(len(kw_os_i_low_25med)):
	if kw_os_i_low_25med[i]<min_kw_os_i_low_25med:
		min_kw_os_i_low_25med = kw_os_i_low_25med[i]
	if kw_os_i_low_25med[i]>max_kw_os_i_low_25med:
		max_kw_os_i_low_25med = kw_os_i_low_25med[i]


for i in range(len(kw_os_i_high_25med)):
        if kw_os_i_high_25med[i]<min_kw_os_i_high_25med:
                min_kw_os_i_high_25med = kw_os_i_high_25med[i]
        if kw_os_i_high_25med[i]>max_kw_os_i_high_25med:
                max_kw_os_i_high_25med = kw_os_i_high_25med[i]

print " 25med: sys_i_low =", ((max_kw_os_i_low_25med - min_kw_os_i_low_25med)/2)
print " 25med: sys_i_high =", ((max_kw_os_i_high_25med - min_kw_os_i_high_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_os_i_low_25med - min_kw_os_i_low_25med)/2)/kw_os_i_low_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_os_i_high_25med - min_kw_os_i_high_25med)/2)/kw_os_i_high_25med_val

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
kw_os_i_low_1track_val = 1.355 
kw_os_i_high_1track_val = 1.454

kw_os_i_low_1track = [1.369, 1.364, 1.357, 1.348]#, 1.351]#, 1.348, 1.345, 1.337, 1.289, 1.213]
kw_os_i_high_1track = [1.441, 1.441, 1.441, 1.413]#, 1.394]#, 1.374, 1.308, 1.241, 1.181, 1.058]

diff_kw_os_i_low_val_1track = 0
diff_kw_os_i_high_val_1track = 0

min_kw_os_i_low_1track = 20
max_kw_os_i_low_1track = 0
min_kw_os_i_high_1track = 20
max_kw_os_i_high_1track = 0

for i in range(len(kw_os_i_low_1track)):
	if kw_os_i_low_1track[i]<min_kw_os_i_low_1track:
		min_kw_os_i_low_1track = kw_os_i_low_1track[i]
	if kw_os_i_low_1track[i]>max_kw_os_i_low_1track:
		max_kw_os_i_low_1track = kw_os_i_low_1track[i]


for i in range(len(kw_os_i_high_1track)):
        if kw_os_i_high_1track[i]<min_kw_os_i_high_1track:
                min_kw_os_i_high_1track = kw_os_i_high_1track[i]
        if kw_os_i_high_1track[i]>max_kw_os_i_high_1track:
                max_kw_os_i_high_1track = kw_os_i_high_1track[i]

print "no_trig: sys_i_low =", ((max_kw_os_i_low_1track - min_kw_os_i_low_1track)/2)
print "no_trig: sys_i_high =", ((max_kw_os_i_high_1track - min_kw_os_i_high_1track)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_os_i_low_1track - min_kw_os_i_low_1track)/2)/kw_os_i_low_1track_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_os_i_high_1track - min_kw_os_i_high_1track)/2)/kw_os_i_high_1track_val

print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT

kw_os_i_low_1track_25med_val = 1.337
kw_os_i_high_1track_25med_val = 1.336

kw_os_i_low_1track_25med = [1.332, 1.331, 1.330, 1.322]#, 1.333]#, 1.326, 1.321, 1.293, 1.261, 1.184]
kw_os_i_high_1track_25med = [1.325, 1.331, 1.331, 1.298]#, 1.273]#, 1.255, 1.187, 1.091, 1.010, 0.882]

min_kw_os_i_low_1track_25med = 20
max_kw_os_i_low_1track_25med = 0
min_kw_os_i_high_1track_25med = 20
max_kw_os_i_high_1track_25med = 0

for i in range(len(kw_os_i_low_1track_25med)):
	if kw_os_i_low_1track_25med[i]<min_kw_os_i_low_1track_25med:
		min_kw_os_i_low_1track_25med = kw_os_i_low_1track_25med[i]
	if kw_os_i_low_1track_25med[i]>max_kw_os_i_low_1track_25med:
		max_kw_os_i_low_1track_25med = kw_os_i_low_1track_25med[i]


for i in range(len(kw_os_i_high_1track_25med)):
        if kw_os_i_high_1track_25med[i]<min_kw_os_i_high_1track_25med:
                min_kw_os_i_high_1track_25med = kw_os_i_high_1track_25med[i]
        if kw_os_i_high_1track_25med[i]>max_kw_os_i_high_1track_25med:
                max_kw_os_i_high_1track_25med = kw_os_i_high_1track_25med[i]

print " 25med: sys_i_low =", ((max_kw_os_i_low_1track_25med - min_kw_os_i_low_1track_25med)/2)
print " 25med: sys_i_high =", ((max_kw_os_i_high_1track_25med - min_kw_os_i_high_1track_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_25med - min_kw_os_i_low_1track_25med)/2)/kw_os_i_low_1track_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_25med - min_kw_os_i_high_1track_25med)/2)/kw_os_i_high_1track_25med_val

#######################################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

kw_os_i_low_1track_35med_val = 2.607 
kw_os_i_high_1track_35med_val = 1.269

kw_os_i_low_1track_35med = [2.483, 2.274, 2.227, 2.417]#, 2.574, 2.706, 2.485, 2.464, 2.952, 2.738]
kw_os_i_high_1track_35med = [1.261, 1.257, 1.256, 1.233]#, 1.190, 1.161, 1.079, 0.955, 0.854, 0.715]

min_kw_os_i_low_1track_35med = 20
max_kw_os_i_low_1track_35med = 0
min_kw_os_i_high_1track_35med = 20
max_kw_os_i_high_1track_35med = 0

for i in range(len(kw_os_i_low_1track_35med)):
	if kw_os_i_low_1track_35med[i]<min_kw_os_i_low_1track_35med:
		min_kw_os_i_low_1track_35med = kw_os_i_low_1track_35med[i]
	if kw_os_i_low_1track_35med[i]>max_kw_os_i_low_1track_35med:
		max_kw_os_i_low_1track_35med = kw_os_i_low_1track_35med[i]


for i in range(len(kw_os_i_high_1track_35med)):
        if kw_os_i_high_1track_35med[i]<min_kw_os_i_high_1track_35med:
                min_kw_os_i_high_1track_35med = kw_os_i_high_1track_35med[i]
        if kw_os_i_high_1track_35med[i]>max_kw_os_i_high_1track_35med:
                max_kw_os_i_high_1track_35med = kw_os_i_high_1track_35med[i]

print " 35med: sys_i_low =", ((max_kw_os_i_low_1track_35med - min_kw_os_i_low_1track_35med)/2)
print " 35med: sys_i_high =", ((max_kw_os_i_high_1track_35med - min_kw_os_i_high_1track_35med)/2)
print " 35med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_35med - min_kw_os_i_low_1track_35med)/2)/kw_os_i_low_1track_35med_val
print " 35med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_35med - min_kw_os_i_high_1track_35med)/2)/kw_os_i_high_1track_35med_val

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
kw_os_i_low_1track_50L1TAU12med_val = 2.168 
kw_os_i_high_1track_50L1TAU12med_val =  1.422

kw_os_i_low_1track_50L1TAU12med = [2.039, 1.649, 1.444, 0.989]#, 0.937, 1.156, 0.952, 1.229, 2.194, 1.000]
kw_os_i_high_1track_50L1TAU12med = [1.396, 1.390, 1.408, 1.401]#, 1.360, 1.325, 1.271, 1.160, 1.016, 0.925]

min_kw_os_i_low_1track_50L1TAU12med = 20
max_kw_os_i_low_1track_50L1TAU12med = 0
min_kw_os_i_high_1track_50L1TAU12med = 20
max_kw_os_i_high_1track_50L1TAU12med = 0

for i in range(len(kw_os_i_low_1track_50L1TAU12med)):
	if kw_os_i_low_1track_50L1TAU12med[i]<min_kw_os_i_low_1track_50L1TAU12med:
		min_kw_os_i_low_1track_50L1TAU12med = kw_os_i_low_1track_50L1TAU12med[i]
	if kw_os_i_low_1track_50L1TAU12med[i]>max_kw_os_i_low_1track_50L1TAU12med:
		max_kw_os_i_low_1track_50L1TAU12med = kw_os_i_low_1track_50L1TAU12med[i]


for i in range(len(kw_os_i_high_1track_50L1TAU12med)):
        if kw_os_i_high_1track_50L1TAU12med[i]<min_kw_os_i_high_1track_50L1TAU12med:
                min_kw_os_i_high_1track_50L1TAU12med = kw_os_i_high_1track_50L1TAU12med[i]
        if kw_os_i_high_1track_50L1TAU12med[i]>max_kw_os_i_high_1track_50L1TAU12med:
                max_kw_os_i_high_1track_50L1TAU12med = kw_os_i_high_1track_50L1TAU12med[i]

print " 50L1TAU12med: sys_i_low =", ((max_kw_os_i_low_1track_50L1TAU12med - min_kw_os_i_low_1track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_high =", ((max_kw_os_i_high_1track_50L1TAU12med - min_kw_os_i_high_1track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_50L1TAU12med - min_kw_os_i_low_1track_50L1TAU12med)/2)/kw_os_i_low_1track_50L1TAU12med_val
print " 50L1TAU12med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_50L1TAU12med - min_kw_os_i_high_1track_50L1TAU12med)/2)/kw_os_i_high_1track_50L1TAU12med_val

################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
kw_os_i_low_1track_80med_val = -0.604 
kw_os_i_high_1track_80med_val = 1.505

kw_os_i_low_1track_80med = [-0.515, -0.586]
kw_os_i_high_1track_80med = [1.482, 1.507, 1.437, 1.413]#, 0.203, 1.113, 1.017, 0.864, 0.689, 0.412]

min_kw_os_i_low_1track_80med = 20
max_kw_os_i_low_1track_80med = 0
min_kw_os_i_high_1track_80med = 20
max_kw_os_i_high_1track_80med = 0

for i in range(len(kw_os_i_low_1track_80med)):
	if kw_os_i_low_1track_80med[i]<min_kw_os_i_low_1track_80med:
		min_kw_os_i_low_1track_80med = kw_os_i_low_1track_80med[i]
	if kw_os_i_low_1track_80med[i]>max_kw_os_i_low_1track_80med:
		max_kw_os_i_low_1track_80med = kw_os_i_low_1track_80med[i]


for i in range(len(kw_os_i_high_1track_80med)):
        if kw_os_i_high_1track_80med[i]<min_kw_os_i_high_1track_80med:
                min_kw_os_i_high_1track_80med = kw_os_i_high_1track_80med[i]
        if kw_os_i_high_1track_80med[i]>max_kw_os_i_high_1track_80med:
                max_kw_os_i_high_1track_80med = kw_os_i_high_1track_80med[i]

print " 80med: sys_i_low =", ((max_kw_os_i_low_1track_80med - min_kw_os_i_low_1track_80med)/2)
print " 80med: sys_i_high =", ((max_kw_os_i_high_1track_80med - min_kw_os_i_high_1track_80med)/2)
print " 80med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_80med - min_kw_os_i_low_1track_80med)/2)/kw_os_i_low_1track_80med_val
print " 80med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_80med - min_kw_os_i_high_1track_80med)/2)/kw_os_i_high_1track_80med_val


################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
kw_os_i_low_1track_80L1TAU60med_val = 0.475  
kw_os_i_high_1track_80L1TAU60med_val = 1.154

kw_os_i_low_1track_80L1TAU60med = [0.505, 0.399]
kw_os_i_high_1track_80L1TAU60med = [1.111, 1.097, 0.975, 0.941]#, 0.714, 0.650, 0.504, 0.277]

min_kw_os_i_low_1track_80L1TAU60med = 20
max_kw_os_i_low_1track_80L1TAU60med = 0
min_kw_os_i_high_1track_80L1TAU60med = 20
max_kw_os_i_high_1track_80L1TAU60med = 0

for i in range(len(kw_os_i_low_1track_80L1TAU60med)):
	if kw_os_i_low_1track_80L1TAU60med[i]<min_kw_os_i_low_1track_80L1TAU60med:
		min_kw_os_i_low_1track_80L1TAU60med = kw_os_i_low_1track_80L1TAU60med[i]
	if kw_os_i_low_1track_80L1TAU60med[i]>max_kw_os_i_low_1track_80L1TAU60med:
		max_kw_os_i_low_1track_80L1TAU60med = kw_os_i_low_1track_80L1TAU60med[i]


for i in range(len(kw_os_i_high_1track_80L1TAU60med)):
        if kw_os_i_high_1track_80L1TAU60med[i]<min_kw_os_i_high_1track_80L1TAU60med:
                min_kw_os_i_high_1track_80L1TAU60med = kw_os_i_high_1track_80L1TAU60med[i]
        if kw_os_i_high_1track_80L1TAU60med[i]>max_kw_os_i_high_1track_80L1TAU60med:
                max_kw_os_i_high_1track_80L1TAU60med = kw_os_i_high_1track_80L1TAU60med[i]

print " 80L1TAU60med: sys_i_low =", ((max_kw_os_i_low_1track_80L1TAU60med - min_kw_os_i_low_1track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_high =", ((max_kw_os_i_high_1track_80L1TAU60med - min_kw_os_i_high_1track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_80L1TAU60med - min_kw_os_i_low_1track_80L1TAU60med)/2)/kw_os_i_low_1track_80L1TAU60med_val
print " 80L1TAU60med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_80L1TAU60med - min_kw_os_i_high_1track_80L1TAU60med)/2)/kw_os_i_high_1track_80L1TAU60med_val


################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
kw_os_i_low_1track_125med_val = 1 
kw_os_i_high_1track_125med_val = 2.149

kw_os_i_low_1track_125med = [1]
kw_os_i_high_1track_125med = [2.003, 2.063, 1.739, 1.660]#, 1.719, 1.723, 2.426, 2.102, 6.627]

min_kw_os_i_low_1track_125med = 20
max_kw_os_i_low_1track_125med = 0
min_kw_os_i_high_1track_125med = 20
max_kw_os_i_high_1track_125med = 0

for i in range(len(kw_os_i_low_1track_125med)):
	if kw_os_i_low_1track_125med[i]<min_kw_os_i_low_1track_125med:
		min_kw_os_i_low_1track_125med = kw_os_i_low_1track_125med[i]
	if kw_os_i_low_1track_125med[i]>max_kw_os_i_low_1track_125med:
		max_kw_os_i_low_1track_125med = kw_os_i_low_1track_125med[i]


for i in range(len(kw_os_i_high_1track_125med)):
        if kw_os_i_high_1track_125med[i]<min_kw_os_i_high_1track_125med:
                min_kw_os_i_high_1track_125med = kw_os_i_high_1track_125med[i]
        if kw_os_i_high_1track_125med[i]>max_kw_os_i_high_1track_125med:
                max_kw_os_i_high_1track_125med = kw_os_i_high_1track_125med[i]

print " 125med: sys_i_low =", ((max_kw_os_i_low_1track_125med - min_kw_os_i_low_1track_125med)/2)
print " 125med: sys_i_high =", ((max_kw_os_i_high_1track_125med - min_kw_os_i_high_1track_125med)/2)
print " 125med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_125med - min_kw_os_i_low_1track_125med)/2)/kw_os_i_low_1track_125med_val
print " 125med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_125med - min_kw_os_i_high_1track_125med)/2)/kw_os_i_high_1track_125med_val


################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
kw_os_i_low_1track_160med_val = 1 
kw_os_i_high_1track_160med_val = 3.284

kw_os_i_low_1track_160med = [1]
kw_os_i_high_1track_160med = [3.064, 2.749, 2.327, 2.169]#, 1.862, 1.844, 5.016, 3.874]

min_kw_os_i_low_1track_160med = 20
max_kw_os_i_low_1track_160med = 0
min_kw_os_i_high_1track_160med = 20
max_kw_os_i_high_1track_160med = 0

for i in range(len(kw_os_i_low_1track_160med)):
	if kw_os_i_low_1track_160med[i]<min_kw_os_i_low_1track_160med:
		min_kw_os_i_low_1track_160med = kw_os_i_low_1track_160med[i]
	if kw_os_i_low_1track_160med[i]>max_kw_os_i_low_1track_160med:
		max_kw_os_i_low_1track_160med = kw_os_i_low_1track_160med[i]


for i in range(len(kw_os_i_high_1track_160med)):
        if kw_os_i_high_1track_160med[i]<min_kw_os_i_high_1track_160med:
                min_kw_os_i_high_1track_160med = kw_os_i_high_1track_160med[i]
        if kw_os_i_high_1track_160med[i]>max_kw_os_i_high_1track_160med:
                max_kw_os_i_high_1track_160med = kw_os_i_high_1track_160med[i]

print " 160med: sys_i_low =", ((max_kw_os_i_low_1track_160med - min_kw_os_i_low_1track_160med)/2)
print " 160med: sys_i_high =", ((max_kw_os_i_high_1track_160med - min_kw_os_i_high_1track_160med)/2)
print " 160med: sys_i_low (percentage) =", ((max_kw_os_i_low_1track_160med - min_kw_os_i_low_1track_160med)/2)/kw_os_i_low_1track_160med_val
print " 160med: sys_i_high (percentage) =", ((max_kw_os_i_high_1track_160med - min_kw_os_i_high_1track_160med)/2)/kw_os_i_high_1track_160med_val

# ----------------------------------- #
#     	  ptonly1Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_ptonly1Track_val = 1.460 
kw_os_i_high_ptonly1Track_val = 1.438

kw_os_i_low_ptonly1Track = [1.531, 1.526, 1.517, 1.515]
kw_os_i_high_ptonly1Track = [1.507, 1.505, 1.500, 1.473]

min_kw_os_i_low_ptonly1Track = 20
max_kw_os_i_low_ptonly1Track = 0
min_kw_os_i_high_ptonly1Track = 20
max_kw_os_i_high_ptonly1Track = 0

for i in range(len(kw_os_i_low_ptonly1Track)):
	if kw_os_i_low_ptonly1Track[i]<min_kw_os_i_low_ptonly1Track:
		min_kw_os_i_low_ptonly1Track = kw_os_i_low_ptonly1Track[i]
	if kw_os_i_low_ptonly1Track[i]>max_kw_os_i_low_ptonly1Track:
		max_kw_os_i_low_ptonly1Track = kw_os_i_low_ptonly1Track[i]


for i in range(len(kw_os_i_high_ptonly1Track)):
        if kw_os_i_high_ptonly1Track[i]<min_kw_os_i_high_ptonly1Track:
                min_kw_os_i_high_ptonly1Track = kw_os_i_high_ptonly1Track[i]
        if kw_os_i_high_ptonly1Track[i]>max_kw_os_i_high_ptonly1Track:
                max_kw_os_i_high_ptonly1Track = kw_os_i_high_ptonly1Track[i]

print " ptonly1Track: sys_i_low =", ((max_kw_os_i_low_ptonly1Track - min_kw_os_i_low_ptonly1Track)/2)
print " ptonly1Track: sys_i_high =", ((max_kw_os_i_high_ptonly1Track - min_kw_os_i_high_ptonly1Track)/2)
print " ptonly1Track: sys_i_low (percentage) =", ((max_kw_os_i_low_ptonly1Track - min_kw_os_i_low_ptonly1Track)/2)/kw_os_i_low_ptonly1Track_val
print " ptonly1Track: sys_i_high (percentage) =", ((max_kw_os_i_high_ptonly1Track - min_kw_os_i_high_ptonly1Track)/2)/kw_os_i_high_ptonly1Track_val
# ----------------------------------- #
#     	   tracktwo1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_tracktwo1Track_val = 1.414 
kw_os_i_high_tracktwo1Track_val = 1.367

kw_os_i_low_tracktwo1Track = [1.486, 1.483, 1.479, 1.471]
kw_os_i_high_tracktwo1Track = [1.439, 1.440, 1.440, 1.410]

min_kw_os_i_low_tracktwo1Track = 20
max_kw_os_i_low_tracktwo1Track = 0
min_kw_os_i_high_tracktwo1Track = 20
max_kw_os_i_high_tracktwo1Track = 0

for i in range(len(kw_os_i_low_tracktwo1Track)):
	if kw_os_i_low_tracktwo1Track[i]<min_kw_os_i_low_tracktwo1Track:
		min_kw_os_i_low_tracktwo1Track = kw_os_i_low_tracktwo1Track[i]
	if kw_os_i_low_tracktwo1Track[i]>max_kw_os_i_low_tracktwo1Track:
		max_kw_os_i_low_tracktwo1Track = kw_os_i_low_tracktwo1Track[i]


for i in range(len(kw_os_i_high_tracktwo1Track)):
        if kw_os_i_high_tracktwo1Track[i]<min_kw_os_i_high_tracktwo1Track:
                min_kw_os_i_high_tracktwo1Track = kw_os_i_high_tracktwo1Track[i]
        if kw_os_i_high_tracktwo1Track[i]>max_kw_os_i_high_tracktwo1Track:
                max_kw_os_i_high_tracktwo1Track = kw_os_i_high_tracktwo1Track[i]

print " tracktwo1Track: sys_i_low =", ((max_kw_os_i_low_tracktwo1Track - min_kw_os_i_low_tracktwo1Track)/2)
print " tracktwo1Track: sys_i_high =", ((max_kw_os_i_high_tracktwo1Track - min_kw_os_i_high_tracktwo1Track)/2)
print " tracktwo1Track: sys_i_low (percentage) =", ((max_kw_os_i_low_tracktwo1Track - min_kw_os_i_low_tracktwo1Track)/2)/kw_os_i_low_tracktwo1Track_val
print " tracktwo1Track: sys_i_high (percentage) =", ((max_kw_os_i_high_tracktwo1Track - min_kw_os_i_high_tracktwo1Track)/2)/kw_os_i_high_tracktwo1Track_val


# ----------------------------------- #
#     	   L1TAU12IM1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_L1TAU12IM1Track_val = 1.339 
kw_os_i_high_L1TAU12IM1Track_val = 1.439

kw_os_i_low_L1TAU12IM1Track = [1.334, 1.330, 1.326, 1.317]#, 1.322, 1.319, 1.316, 1.303, 1.250, 1.179]
kw_os_i_high_L1TAU12IM1Track = [1.426, 1.424, 1.418, 1.388]#, 1.364, 1.347, 1.279, 1.210, 1.150, 1.033]

min_kw_os_i_low_L1TAU12IM1Track = 20
max_kw_os_i_low_L1TAU12IM1Track = 0
min_kw_os_i_high_L1TAU12IM1Track = 20
max_kw_os_i_high_L1TAU12IM1Track = 0

for i in range(len(kw_os_i_low_L1TAU12IM1Track)):
	if kw_os_i_low_L1TAU12IM1Track[i]<min_kw_os_i_low_L1TAU12IM1Track:
		min_kw_os_i_low_L1TAU12IM1Track = kw_os_i_low_L1TAU12IM1Track[i]
	if kw_os_i_low_L1TAU12IM1Track[i]>max_kw_os_i_low_L1TAU12IM1Track:
		max_kw_os_i_low_L1TAU12IM1Track = kw_os_i_low_L1TAU12IM1Track[i]


for i in range(len(kw_os_i_high_L1TAU12IM1Track)):
        if kw_os_i_high_L1TAU12IM1Track[i]<min_kw_os_i_high_L1TAU12IM1Track:
                min_kw_os_i_high_L1TAU12IM1Track = kw_os_i_high_L1TAU12IM1Track[i]
        if kw_os_i_high_L1TAU12IM1Track[i]>max_kw_os_i_high_L1TAU12IM1Track:
                max_kw_os_i_high_L1TAU12IM1Track = kw_os_i_high_L1TAU12IM1Track[i]

print " L1TAU12IM1Track: sys_i_low =", ((max_kw_os_i_low_L1TAU12IM1Track - min_kw_os_i_low_L1TAU12IM1Track)/2)
print " L1TAU12IM1Track: sys_i_high =", ((max_kw_os_i_high_L1TAU12IM1Track - min_kw_os_i_high_L1TAU12IM1Track)/2)
print " L1TAU12IM1Track: sys_i_low (percentage) =", ((max_kw_os_i_low_L1TAU12IM1Track - min_kw_os_i_low_L1TAU12IM1Track)/2)/kw_os_i_low_L1TAU12IM1Track_val
print " L1TAU12IM1Track: sys_i_high (percentage) =", ((max_kw_os_i_high_L1TAU12IM1Track - min_kw_os_i_high_L1TAU12IM1Track)/2)/kw_os_i_high_L1TAU12IM1Track_val

print ""
print "THREE PRONG"
print ""
print "*******************"
print ""

print " ----------------------------------- "
print "            no trigger"
print " ------------------------------------"

# LOW VS HIGH PT
kw_os_i_low_3track_val = 1.599
kw_os_i_high_3track_val = 1.625

kw_os_i_low_3track = [1.369, 1.364, 1.357, 1.348]#, 1.351, 1.348, 1.345, 1.337, 1.289, 1.213]
kw_os_i_high_3track = [1.617, 1.600, 1.578, 1.508]#, 1.492, 1.482, 1.441, 1.354, 1.236, 1.073]

diff_kw_os_i_low_val_3track = 0
diff_kw_os_i_high_val_3track = 0

min_kw_os_i_low_3track = 20
max_kw_os_i_low_3track = 0
min_kw_os_i_high_3track = 20
max_kw_os_i_high_3track = 0

for i in range(len(kw_os_i_low_3track)):
	if kw_os_i_low_3track[i]<min_kw_os_i_low_3track:
		min_kw_os_i_low_3track = kw_os_i_low_3track[i]
	if kw_os_i_low_3track[i]>max_kw_os_i_low_3track:
		max_kw_os_i_low_3track = kw_os_i_low_3track[i]


for i in range(len(kw_os_i_high_3track)):
        if kw_os_i_high_3track[i]<min_kw_os_i_high_3track:
                min_kw_os_i_high_3track = kw_os_i_high_3track[i]
        if kw_os_i_high_3track[i]>max_kw_os_i_high_3track:
                max_kw_os_i_high_3track = kw_os_i_high_3track[i]

print "no_trig: sys_i_low =", ((max_kw_os_i_low_3track - min_kw_os_i_low_3track)/2)
print "no_trig: sys_i_high =", ((max_kw_os_i_high_3track - min_kw_os_i_high_3track)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_os_i_low_3track - min_kw_os_i_low_3track)/2)/kw_os_i_low_3track_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_os_i_high_3track - min_kw_os_i_high_3track)/2)/kw_os_i_high_3track_val

print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT

kw_os_i_low_3track_25med_val = 1.535
kw_os_i_high_3track_25med_val = 1.432

kw_os_i_low_3track_25med = [1.534, 1.506, 1.480, 1.436]#, 1.383, 1.354, 1.319, 1.219, 1.181, 0.942]
kw_os_i_high_3track_25med = [1.435, 1.404, 1.386, 1.287]#, 1.238, 1.148, 1.064, 0.868, 0.690, 0.494]

min_kw_os_i_low_3track_25med = 20
max_kw_os_i_low_3track_25med = 0
min_kw_os_i_high_3track_25med = 20
max_kw_os_i_high_3track_25med = 0

for i in range(len(kw_os_i_low_3track_25med)):
	if kw_os_i_low_3track_25med[i]<min_kw_os_i_low_3track_25med:
		min_kw_os_i_low_3track_25med = kw_os_i_low_3track_25med[i]
	if kw_os_i_low_3track_25med[i]>max_kw_os_i_low_3track_25med:
		max_kw_os_i_low_3track_25med = kw_os_i_low_3track_25med[i]


for i in range(len(kw_os_i_high_3track_25med)):
        if kw_os_i_high_3track_25med[i]<min_kw_os_i_high_3track_25med:
                min_kw_os_i_high_3track_25med = kw_os_i_high_3track_25med[i]
        if kw_os_i_high_3track_25med[i]>max_kw_os_i_high_3track_25med:
                max_kw_os_i_high_3track_25med = kw_os_i_high_3track_25med[i]

print " 25med: sys_i_low =", ((max_kw_os_i_low_3track_25med - min_kw_os_i_low_3track_25med)/2)
print " 25med: sys_i_high =", ((max_kw_os_i_high_3track_25med - min_kw_os_i_high_3track_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_25med - min_kw_os_i_low_3track_25med)/2)/kw_os_i_low_3track_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_25med - min_kw_os_i_high_3track_25med)/2)/kw_os_i_high_3track_25med_val

#######################################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

kw_os_i_low_3track_35med_val = 4.433
kw_os_i_high_3track_35med_val = 1.266

kw_os_i_low_3track_35med = [4.087, 5.530, 5.092, 9.214, ]
kw_os_i_high_3track_35med = [1.241, 1.184, 1.127, 1.027]#, 2.595, 2.268, 4.727, 3.715, 3.519, 3.444]

min_kw_os_i_low_3track_35med = 20
max_kw_os_i_low_3track_35med = 0
min_kw_os_i_high_3track_35med = 20
max_kw_os_i_high_3track_35med = 0

for i in range(len(kw_os_i_low_3track_35med)):
	if kw_os_i_low_3track_35med[i]<min_kw_os_i_low_3track_35med:
		min_kw_os_i_low_3track_35med = kw_os_i_low_3track_35med[i]
	if kw_os_i_low_3track_35med[i]>max_kw_os_i_low_3track_35med:
		max_kw_os_i_low_3track_35med = kw_os_i_low_3track_35med[i]


for i in range(len(kw_os_i_high_3track_35med)):
        if kw_os_i_high_3track_35med[i]<min_kw_os_i_high_3track_35med:
                min_kw_os_i_high_3track_35med = kw_os_i_high_3track_35med[i]
        if kw_os_i_high_3track_35med[i]>max_kw_os_i_high_3track_35med:
                max_kw_os_i_high_3track_35med = kw_os_i_high_3track_35med[i]

print " 35med: sys_i_low =", ((max_kw_os_i_low_3track_35med - min_kw_os_i_low_3track_35med)/2)
print " 35med: sys_i_high =", ((max_kw_os_i_high_3track_35med - min_kw_os_i_high_3track_35med)/2)
print " 35med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_35med - min_kw_os_i_low_3track_35med)/2)/kw_os_i_low_3track_35med_val
print " 35med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_35med - min_kw_os_i_high_3track_35med)/2)/kw_os_i_high_3track_35med_val

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
kw_os_i_low_3track_50L1TAU12med_val = 6.245  
kw_os_i_high_3track_50L1TAU12med_val =  1.398

kw_os_i_low_3track_50L1TAU12med = [5.567, 4.881, 4.751, 4.049]#, 4.049, 4.049, ]
kw_os_i_high_3track_50L1TAU12med = [1.356, 1.229, 1.168]#, 0.994]#, 0.878, 0.771, 2.826, 2.232, 2.413, 2.067]

min_kw_os_i_low_3track_50L1TAU12med = 20
max_kw_os_i_low_3track_50L1TAU12med = 0
min_kw_os_i_high_3track_50L1TAU12med = 20
max_kw_os_i_high_3track_50L1TAU12med = 0

for i in range(len(kw_os_i_low_3track_50L1TAU12med)):
	if kw_os_i_low_3track_50L1TAU12med[i]<min_kw_os_i_low_3track_50L1TAU12med:
		min_kw_os_i_low_3track_50L1TAU12med = kw_os_i_low_3track_50L1TAU12med[i]
	if kw_os_i_low_3track_50L1TAU12med[i]>max_kw_os_i_low_3track_50L1TAU12med:
		max_kw_os_i_low_3track_50L1TAU12med = kw_os_i_low_3track_50L1TAU12med[i]


for i in range(len(kw_os_i_high_3track_50L1TAU12med)):
        if kw_os_i_high_3track_50L1TAU12med[i]<min_kw_os_i_high_3track_50L1TAU12med:
                min_kw_os_i_high_3track_50L1TAU12med = kw_os_i_high_3track_50L1TAU12med[i]
        if kw_os_i_high_3track_50L1TAU12med[i]>max_kw_os_i_high_3track_50L1TAU12med:
                max_kw_os_i_high_3track_50L1TAU12med = kw_os_i_high_3track_50L1TAU12med[i]

print " 50L1TAU12med: sys_i_low =", ((max_kw_os_i_low_3track_50L1TAU12med - min_kw_os_i_low_3track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_high =", ((max_kw_os_i_high_3track_50L1TAU12med - min_kw_os_i_high_3track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_50L1TAU12med - min_kw_os_i_low_3track_50L1TAU12med)/2)/kw_os_i_low_3track_50L1TAU12med_val
print " 50L1TAU12med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_50L1TAU12med - min_kw_os_i_high_3track_50L1TAU12med)/2)/kw_os_i_high_3track_50L1TAU12med_val

################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
kw_os_i_low_3track_80med_val = 1 
kw_os_i_high_3track_80med_val = 0.392

kw_os_i_low_3track_80med = [1]
kw_os_i_high_3track_80med = [0.417, 0.350, 0.290, 0.150]#, -0.099, -0.210, -0.393, -0.646, -0.928, -1.059]

min_kw_os_i_low_3track_80med = 20
max_kw_os_i_low_3track_80med = 0
min_kw_os_i_high_3track_80med = 20
max_kw_os_i_high_3track_80med = 0

for i in range(len(kw_os_i_low_3track_80med)):
	if kw_os_i_low_3track_80med[i]<min_kw_os_i_low_3track_80med:
		min_kw_os_i_low_3track_80med = kw_os_i_low_3track_80med[i]
	if kw_os_i_low_3track_80med[i]>max_kw_os_i_low_3track_80med:
		max_kw_os_i_low_3track_80med = kw_os_i_low_3track_80med[i]


for i in range(len(kw_os_i_high_3track_80med)):
        if kw_os_i_high_3track_80med[i]<min_kw_os_i_high_3track_80med:
                min_kw_os_i_high_3track_80med = kw_os_i_high_3track_80med[i]
        if kw_os_i_high_3track_80med[i]>max_kw_os_i_high_3track_80med:
                max_kw_os_i_high_3track_80med = kw_os_i_high_3track_80med[i]

print " 80med: sys_i_low =", ((max_kw_os_i_low_3track_80med - min_kw_os_i_low_3track_80med)/2)
print " 80med: sys_i_high =", ((max_kw_os_i_high_3track_80med - min_kw_os_i_high_3track_80med)/2)
print " 80med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_80med - min_kw_os_i_low_3track_80med)/2)/kw_os_i_low_3track_80med_val
print " 80med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_80med - min_kw_os_i_high_3track_80med)/2)/kw_os_i_high_3track_80med_val


################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
kw_os_i_low_3track_80L1TAU60med_val = 1 
kw_os_i_high_3track_80L1TAU60med_val = 5.318 

kw_os_i_low_3track_80L1TAU60med = [1]
kw_os_i_high_3track_80L1TAU60med = [5.221, 6.099, 5.647]#, 6.128], -0.871, -0.861]#, -1.002, -1.284, -2.136, -2.085]

min_kw_os_i_low_3track_80L1TAU60med = 20
max_kw_os_i_low_3track_80L1TAU60med = 0
min_kw_os_i_high_3track_80L1TAU60med = 20
max_kw_os_i_high_3track_80L1TAU60med = 0

for i in range(len(kw_os_i_low_3track_80L1TAU60med)):
	if kw_os_i_low_3track_80L1TAU60med[i]<min_kw_os_i_low_3track_80L1TAU60med:
		min_kw_os_i_low_3track_80L1TAU60med = kw_os_i_low_3track_80L1TAU60med[i]
	if kw_os_i_low_3track_80L1TAU60med[i]>max_kw_os_i_low_3track_80L1TAU60med:
		max_kw_os_i_low_3track_80L1TAU60med = kw_os_i_low_3track_80L1TAU60med[i]


for i in range(len(kw_os_i_high_3track_80L1TAU60med)):
        if kw_os_i_high_3track_80L1TAU60med[i]<min_kw_os_i_high_3track_80L1TAU60med:
                min_kw_os_i_high_3track_80L1TAU60med = kw_os_i_high_3track_80L1TAU60med[i]
        if kw_os_i_high_3track_80L1TAU60med[i]>max_kw_os_i_high_3track_80L1TAU60med:
                max_kw_os_i_high_3track_80L1TAU60med = kw_os_i_high_3track_80L1TAU60med[i]

print " 80L1TAU60med: sys_i_low =", ((max_kw_os_i_low_3track_80L1TAU60med - min_kw_os_i_low_3track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_high =", ((max_kw_os_i_high_3track_80L1TAU60med - min_kw_os_i_high_3track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_80L1TAU60med - min_kw_os_i_low_3track_80L1TAU60med)/2)/kw_os_i_low_3track_80L1TAU60med_val
print " 80L1TAU60med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_80L1TAU60med - min_kw_os_i_high_3track_80L1TAU60med)/2)/kw_os_i_high_3track_80L1TAU60med_val


################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
kw_os_i_low_3track_125med_val =  1
kw_os_i_high_3track_125med_val = 0.162

kw_os_i_low_3track_125med = [1]
kw_os_i_high_3track_125med = [0.169, 0.224, 0.155, 0.028]

min_kw_os_i_low_3track_125med = 20
max_kw_os_i_low_3track_125med = 0
min_kw_os_i_high_3track_125med = 20
max_kw_os_i_high_3track_125med = 0

for i in range(len(kw_os_i_low_3track_125med)):
	if kw_os_i_low_3track_125med[i]<min_kw_os_i_low_3track_125med:
		min_kw_os_i_low_3track_125med = kw_os_i_low_3track_125med[i]
	if kw_os_i_low_3track_125med[i]>max_kw_os_i_low_3track_125med:
		max_kw_os_i_low_3track_125med = kw_os_i_low_3track_125med[i]


for i in range(len(kw_os_i_high_3track_125med)):
        if kw_os_i_high_3track_125med[i]<min_kw_os_i_high_3track_125med:
                min_kw_os_i_high_3track_125med = kw_os_i_high_3track_125med[i]
        if kw_os_i_high_3track_125med[i]>max_kw_os_i_high_3track_125med:
                max_kw_os_i_high_3track_125med = kw_os_i_high_3track_125med[i]

print " 125med: sys_i_low =", ((max_kw_os_i_low_3track_125med - min_kw_os_i_low_3track_125med)/2)
print " 125med: sys_i_high =", ((max_kw_os_i_high_3track_125med - min_kw_os_i_high_3track_125med)/2)
print " 125med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_125med - min_kw_os_i_low_3track_125med)/2)/kw_os_i_low_3track_125med_val
print " 125med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_125med - min_kw_os_i_high_3track_125med)/2)/kw_os_i_high_3track_125med_val


################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
kw_os_i_low_3track_160med_val = 1
kw_os_i_high_3track_160med_val = 0.250

kw_os_i_low_3track_160med = [1]
kw_os_i_high_3track_160med = [0.280, 0.299, 0.166, 0.204]#, -0.350, -0.457, -0.414, -0.813, -0.444, -0.886]

min_kw_os_i_low_3track_160med = 20
max_kw_os_i_low_3track_160med = 0
min_kw_os_i_high_3track_160med = 20
max_kw_os_i_high_3track_160med = 0

for i in range(len(kw_os_i_low_3track_160med)):
	if kw_os_i_low_3track_160med[i]<min_kw_os_i_low_3track_160med:
		min_kw_os_i_low_3track_160med = kw_os_i_low_3track_160med[i]
	if kw_os_i_low_3track_160med[i]>max_kw_os_i_low_3track_160med:
		max_kw_os_i_low_3track_160med = kw_os_i_low_3track_160med[i]


for i in range(len(kw_os_i_high_3track_160med)):
        if kw_os_i_high_3track_160med[i]<min_kw_os_i_high_3track_160med:
                min_kw_os_i_high_3track_160med = kw_os_i_high_3track_160med[i]
        if kw_os_i_high_3track_160med[i]>max_kw_os_i_high_3track_160med:
                max_kw_os_i_high_3track_160med = kw_os_i_high_3track_160med[i]

print " 160med: sys_i_low =", ((max_kw_os_i_low_3track_160med - min_kw_os_i_low_3track_160med)/2)
print " 160med: sys_i_high =", ((max_kw_os_i_high_3track_160med - min_kw_os_i_high_3track_160med)/2)
print " 160med: sys_i_low (percentage) =", ((max_kw_os_i_low_3track_160med - min_kw_os_i_low_3track_160med)/2)/kw_os_i_low_3track_160med_val
print " 160med: sys_i_high (percentage) =", ((max_kw_os_i_high_3track_160med - min_kw_os_i_high_3track_160med)/2)/kw_os_i_high_3track_160med_val

# ----------------------------------- #
#     	  ptonly3Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_ptonly3Track_val = 1.868 
kw_os_i_high_ptonly3Track_val = 1.635

kw_os_i_low_ptonly3Track = [1.899, 1.867, 1.839, 1.794]
kw_os_i_high_ptonly3Track = [1.692, 1.671, 1.650, 1.573]

min_kw_os_i_low_ptonly3Track = 20
max_kw_os_i_low_ptonly3Track = 0
min_kw_os_i_high_ptonly3Track = 20
max_kw_os_i_high_ptonly3Track = 0

for i in range(len(kw_os_i_low_ptonly3Track)):
	if kw_os_i_low_ptonly3Track[i]<min_kw_os_i_low_ptonly3Track:
		min_kw_os_i_low_ptonly3Track = kw_os_i_low_ptonly3Track[i]
	if kw_os_i_low_ptonly3Track[i]>max_kw_os_i_low_ptonly3Track:
		max_kw_os_i_low_ptonly3Track = kw_os_i_low_ptonly3Track[i]


for i in range(len(kw_os_i_high_ptonly3Track)):
        if kw_os_i_high_ptonly3Track[i]<min_kw_os_i_high_ptonly3Track:
                min_kw_os_i_high_ptonly3Track = kw_os_i_high_ptonly3Track[i]
        if kw_os_i_high_ptonly3Track[i]>max_kw_os_i_high_ptonly3Track:
                max_kw_os_i_high_ptonly3Track = kw_os_i_high_ptonly3Track[i]

print " ptonly3Track: sys_i_low =", ((max_kw_os_i_low_ptonly3Track - min_kw_os_i_low_ptonly3Track)/2)
print " ptonly3Track: sys_i_high =", ((max_kw_os_i_high_ptonly3Track - min_kw_os_i_high_ptonly3Track)/2)
print " ptonly3Track: sys_i_low (percentage) =", ((max_kw_os_i_low_ptonly3Track - min_kw_os_i_low_ptonly3Track)/2)/kw_os_i_low_ptonly3Track_val
print " ptonly3Track: sys_i_high (percentage) =", ((max_kw_os_i_high_ptonly3Track - min_kw_os_i_high_ptonly3Track)/2)/kw_os_i_high_ptonly3Track_val
# ----------------------------------- #
#     	   tracktwo3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_tracktwo3Track_val = 1.792 
kw_os_i_high_tracktwo3Track_val = 1.552

kw_os_i_low_tracktwo3Track = [1.825, 1.798, 1.749, 1.704]
kw_os_i_high_tracktwo3Track = [1.620, 1.591, 1.568, 1.487]

min_kw_os_i_low_tracktwo3Track = 20
max_kw_os_i_low_tracktwo3Track = 0
min_kw_os_i_high_tracktwo3Track = 20
max_kw_os_i_high_tracktwo3Track = 0

for i in range(len(kw_os_i_low_tracktwo3Track)):
	if kw_os_i_low_tracktwo3Track[i]<min_kw_os_i_low_tracktwo3Track:
		min_kw_os_i_low_tracktwo3Track = kw_os_i_low_tracktwo3Track[i]
	if kw_os_i_low_tracktwo3Track[i]>max_kw_os_i_low_tracktwo3Track:
		max_kw_os_i_low_tracktwo3Track = kw_os_i_low_tracktwo3Track[i]


for i in range(len(kw_os_i_high_tracktwo3Track)):
        if kw_os_i_high_tracktwo3Track[i]<min_kw_os_i_high_tracktwo3Track:
                min_kw_os_i_high_tracktwo3Track = kw_os_i_high_tracktwo3Track[i]
        if kw_os_i_high_tracktwo3Track[i]>max_kw_os_i_high_tracktwo3Track:
                max_kw_os_i_high_tracktwo3Track = kw_os_i_high_tracktwo3Track[i]

print " tracktwo3Track: sys_i_low =", ((max_kw_os_i_low_tracktwo3Track - min_kw_os_i_low_tracktwo3Track)/2)
print " tracktwo3Track: sys_i_high =", ((max_kw_os_i_high_tracktwo3Track - min_kw_os_i_high_tracktwo3Track)/2)
print " tracktwo3Track: sys_i_low (percentage) =", ((max_kw_os_i_low_tracktwo3Track - min_kw_os_i_low_tracktwo3Track)/2)/kw_os_i_low_tracktwo3Track_val
print " tracktwo3Track: sys_i_high (percentage) =", ((max_kw_os_i_high_tracktwo3Track - min_kw_os_i_high_tracktwo3Track)/2)/kw_os_i_high_tracktwo3Track_val


# ----------------------------------- #
#     	   L1TAU12IM3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_os_i_low_L1TAU12IM3Track_val = 1.503 
kw_os_i_high_L1TAU12IM3Track_val = 1.633

kw_os_i_low_L1TAU12IM3Track = [1.499, 1.484, 1.455, 1.438]#, 1.415, 1.397, 1.379, 1.375, 1.319, 1.203]
kw_os_i_high_L1TAU12IM3Track = [1.627, 1.603, 1.577, 1.497]#, 1.472, 1.451, 1.376, 1.242, 1.123, 0.947]

min_kw_os_i_low_L1TAU12IM3Track = 20
max_kw_os_i_low_L1TAU12IM3Track = 0
min_kw_os_i_high_L1TAU12IM3Track = 20
max_kw_os_i_high_L1TAU12IM3Track = 0

for i in range(len(kw_os_i_low_L1TAU12IM3Track)):
	if kw_os_i_low_L1TAU12IM3Track[i]<min_kw_os_i_low_L1TAU12IM3Track:
		min_kw_os_i_low_L1TAU12IM3Track = kw_os_i_low_L1TAU12IM3Track[i]
	if kw_os_i_low_L1TAU12IM3Track[i]>max_kw_os_i_low_L1TAU12IM3Track:
		max_kw_os_i_low_L1TAU12IM3Track = kw_os_i_low_L1TAU12IM3Track[i]


for i in range(len(kw_os_i_high_L1TAU12IM3Track)):
        if kw_os_i_high_L1TAU12IM3Track[i]<min_kw_os_i_high_L1TAU12IM3Track:
                min_kw_os_i_high_L1TAU12IM3Track = kw_os_i_high_L1TAU12IM3Track[i]
        if kw_os_i_high_L1TAU12IM3Track[i]>max_kw_os_i_high_L1TAU12IM3Track:
                max_kw_os_i_high_L1TAU12IM3Track = kw_os_i_high_L1TAU12IM3Track[i]

print " L1TAU12IM3Track: sys_i_low =", ((max_kw_os_i_low_L1TAU12IM3Track - min_kw_os_i_low_L1TAU12IM3Track)/2)
print " L1TAU12IM3Track: sys_i_high =", ((max_kw_os_i_high_L1TAU12IM3Track - min_kw_os_i_high_L1TAU12IM3Track)/2)
print " L1TAU12IM3Track: sys_i_low (percentage) =", ((max_kw_os_i_low_L1TAU12IM3Track - min_kw_os_i_low_L1TAU12IM3Track)/2)/kw_os_i_low_L1TAU12IM3Track_val
print " L1TAU12IM3Track: sys_i_high (percentage) =", ((max_kw_os_i_high_L1TAU12IM3Track - min_kw_os_i_high_L1TAU12IM3Track)/2)/kw_os_i_high_L1TAU12IM3Track_val

