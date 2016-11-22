# incl no trig

from math import *

print "INCLUSIVE"
print ""
print "*******************"
print ""

print "------------------------------"
print "        NO TRIGGER"
print "------------------------------"


kw_ss_i_low_val = 1.567 
kw_ss_i_high_val = 2.045

kw_ss_i_low = [1.571, 1.559, 1.529, 1.519]#, 1.500, 1.501, 1.483, 1.539, 1.563, 1.558]
kw_ss_i_high = [2.060, 2.044, 2.030, 2.060]#, 2.070, 2.080, 2.181, 2.150, 2.086, 2.120]

diff_kw_ss_i_low_val = 0
diff_kw_ss_i_high_val = 0

min_kw_ss_i_low = 20
max_kw_ss_i_low = 0
min_kw_ss_i_high = 20
max_kw_ss_i_high = 0

for i in range(len(kw_ss_i_low)):
	if kw_ss_i_low[i]<min_kw_ss_i_low:
		min_kw_ss_i_low = kw_ss_i_low[i]
	if kw_ss_i_low[i]>max_kw_ss_i_low:
		max_kw_ss_i_low = kw_ss_i_low[i]


for i in range(len(kw_ss_i_high)):
        if kw_ss_i_high[i]<min_kw_ss_i_high:
                min_kw_ss_i_high = kw_ss_i_high[i]
        if kw_ss_i_high[i]>max_kw_ss_i_high:
                max_kw_ss_i_high = kw_ss_i_high[i]

print "no_trig: sys_i_low =", ((max_kw_ss_i_low - min_kw_ss_i_low)/2)
print "no_trig: sys_i_high =", ((max_kw_ss_i_high - min_kw_ss_i_high)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_ss_i_low - min_kw_ss_i_low)/2)/kw_ss_i_low_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_ss_i_high - min_kw_ss_i_high)/2)/kw_ss_i_high_val


print " ----------------------------------- "
print "     	   25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT
kw_ss_i_low_25med_val = 1.531 
kw_ss_i_high_25med_val = 1.954

kw_ss_i_low_25med = [1.537, 1.520, 1.481, 1.436]#, 1.414, 1.401, 1.353, 1.365, 1.365, 1.333]
kw_ss_i_high_25med = [1.978, 1.958, 1.932, 1.939]#, 1.945, 1.957, 2.028, 2.005, 1.984, 2.047]

min_kw_ss_i_low_25med = 20
max_kw_ss_i_low_25med = 0
min_kw_ss_i_high_25med = 20
max_kw_ss_i_high_25med = 0

for i in range(len(kw_ss_i_low_25med)):
	if kw_ss_i_low_25med[i]<min_kw_ss_i_low_25med:
		min_kw_ss_i_low_25med = kw_ss_i_low_25med[i]
	if kw_ss_i_low_25med[i]>max_kw_ss_i_low_25med:
		max_kw_ss_i_low_25med = kw_ss_i_low_25med[i]


for i in range(len(kw_ss_i_high_25med)):
        if kw_ss_i_high_25med[i]<min_kw_ss_i_high_25med:
                min_kw_ss_i_high_25med = kw_ss_i_high_25med[i]
        if kw_ss_i_high_25med[i]>max_kw_ss_i_high_25med:
                max_kw_ss_i_high_25med = kw_ss_i_high_25med[i]

print " 25med: sys_i_low =", ((max_kw_ss_i_low_25med - min_kw_ss_i_low_25med)/2)
print " 25med: sys_i_high =", ((max_kw_ss_i_high_25med - min_kw_ss_i_high_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_ss_i_low_25med - min_kw_ss_i_low_25med)/2)/kw_ss_i_low_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_ss_i_high_25med - min_kw_ss_i_high_25med)/2)/kw_ss_i_high_25med_val



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
kw_ss_i_low_1track_val = 1.564 
kw_ss_i_high_1track_val = 2.009

kw_ss_i_low_1track = [1.569, 1.553, 1.522, 1.511]#, 1.485, 1.476, 1.433, 1.475, 1.531, 1.537]
kw_ss_i_high_1track = [2.031, 2.004, 1.972, 1.997]#, 2.002, 1.998, 2.127, 2.143, 2.036, 1.991]

diff_kw_ss_i_low_val_1track = 0
diff_kw_ss_i_high_val_1track = 0

min_kw_ss_i_low_1track = 20
max_kw_ss_i_low_1track = 0
min_kw_ss_i_high_1track = 20
max_kw_ss_i_high_1track = 0

for i in range(len(kw_ss_i_low_1track)):
	if kw_ss_i_low_1track[i]<min_kw_ss_i_low_1track:
		min_kw_ss_i_low_1track = kw_ss_i_low_1track[i]
	if kw_ss_i_low_1track[i]>max_kw_ss_i_low_1track:
		max_kw_ss_i_low_1track = kw_ss_i_low_1track[i]


for i in range(len(kw_ss_i_high_1track)):
        if kw_ss_i_high_1track[i]<min_kw_ss_i_high_1track:
                min_kw_ss_i_high_1track = kw_ss_i_high_1track[i]
        if kw_ss_i_high_1track[i]>max_kw_ss_i_high_1track:
                max_kw_ss_i_high_1track = kw_ss_i_high_1track[i]

print "no_trig: sys_i_low =", ((max_kw_ss_i_low_1track - min_kw_ss_i_low_1track)/2)
print "no_trig: sys_i_high =", ((max_kw_ss_i_high_1track - min_kw_ss_i_high_1track)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track - min_kw_ss_i_low_1track)/2)/kw_ss_i_low_1track_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track - min_kw_ss_i_high_1track)/2)/kw_ss_i_high_1track_val

print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT

kw_ss_i_low_1track_25med_val = 1.543
kw_ss_i_high_1track_25med_val = 1.948

kw_ss_i_low_1track_25med = [1.551, 1.531, 1.489, 1.446]#, 1.417, 1.425, 1.367, 1.383, 1.389, 1.359]
kw_ss_i_high_1track_25med = [1.975, 1.943, 1.873, 1.876]#, 1.868, 1.844, 1.949, 1.988, 1.917, 1.893]

min_kw_ss_i_low_1track_25med = 20
max_kw_ss_i_low_1track_25med = 0
min_kw_ss_i_high_1track_25med = 20
max_kw_ss_i_high_1track_25med = 0

for i in range(len(kw_ss_i_low_1track_25med)):
	if kw_ss_i_low_1track_25med[i]<min_kw_ss_i_low_1track_25med:
		min_kw_ss_i_low_1track_25med = kw_ss_i_low_1track_25med[i]
	if kw_ss_i_low_1track_25med[i]>max_kw_ss_i_low_1track_25med:
		max_kw_ss_i_low_1track_25med = kw_ss_i_low_1track_25med[i]


for i in range(len(kw_ss_i_high_1track_25med)):
        if kw_ss_i_high_1track_25med[i]<min_kw_ss_i_high_1track_25med:
                min_kw_ss_i_high_1track_25med = kw_ss_i_high_1track_25med[i]
        if kw_ss_i_high_1track_25med[i]>max_kw_ss_i_high_1track_25med:
                max_kw_ss_i_high_1track_25med = kw_ss_i_high_1track_25med[i]

print " 25med: sys_i_low =", ((max_kw_ss_i_low_1track_25med - min_kw_ss_i_low_1track_25med)/2)
print " 25med: sys_i_high =", ((max_kw_ss_i_high_1track_25med - min_kw_ss_i_high_1track_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_25med - min_kw_ss_i_low_1track_25med)/2)/kw_ss_i_low_1track_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_25med - min_kw_ss_i_high_1track_25med)/2)/kw_ss_i_high_1track_25med_val

#######################################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

kw_ss_i_low_1track_35med_val = 4.404 
kw_ss_i_high_1track_35med_val = 1.878

kw_ss_i_low_1track_35med = [4.755, 4.326, 4.212, 3.824]#, 3.187, 5.120, 4.324, 6.836, 10.002, 7.013]
kw_ss_i_high_1track_35med = [1.911, 1.869, 1.800, 1.770]#, 1.777, 1.763, 1.847, 1.883, 1.814, 1.837]

min_kw_ss_i_low_1track_35med = 20
max_kw_ss_i_low_1track_35med = 0
min_kw_ss_i_high_1track_35med = 20
max_kw_ss_i_high_1track_35med = 0

for i in range(len(kw_ss_i_low_1track_35med)):
	if kw_ss_i_low_1track_35med[i]<min_kw_ss_i_low_1track_35med:
		min_kw_ss_i_low_1track_35med = kw_ss_i_low_1track_35med[i]
	if kw_ss_i_low_1track_35med[i]>max_kw_ss_i_low_1track_35med:
		max_kw_ss_i_low_1track_35med = kw_ss_i_low_1track_35med[i]


for i in range(len(kw_ss_i_high_1track_35med)):
        if kw_ss_i_high_1track_35med[i]<min_kw_ss_i_high_1track_35med:
                min_kw_ss_i_high_1track_35med = kw_ss_i_high_1track_35med[i]
        if kw_ss_i_high_1track_35med[i]>max_kw_ss_i_high_1track_35med:
                max_kw_ss_i_high_1track_35med = kw_ss_i_high_1track_35med[i]

print " 35med: sys_i_low =", ((max_kw_ss_i_low_1track_35med - min_kw_ss_i_low_1track_35med)/2)
print " 35med: sys_i_high =", ((max_kw_ss_i_high_1track_35med - min_kw_ss_i_high_1track_35med)/2)
print " 35med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_35med - min_kw_ss_i_low_1track_35med)/2)/kw_ss_i_low_1track_35med_val
print " 35med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_35med - min_kw_ss_i_high_1track_35med)/2)/kw_ss_i_high_1track_35med_val

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
kw_ss_i_low_1track_50L1TAU12med_val = 2.806 
kw_ss_i_high_1track_50L1TAU12med_val =  2.810

kw_ss_i_low_1track_50L1TAU12med = [2.680, 2.449, 2.267, 2.154]#, 1.661, 1.766, 1.629, 1.291, 1.476, 1.195]
kw_ss_i_high_1track_50L1TAU12med = [2.934, 2.804, 2.808, 2.963]#, 3.130, 3.039, 3.523, 3.314, 2.876, 2.930]

min_kw_ss_i_low_1track_50L1TAU12med = 20
max_kw_ss_i_low_1track_50L1TAU12med = 0
min_kw_ss_i_high_1track_50L1TAU12med = 20
max_kw_ss_i_high_1track_50L1TAU12med = 0

for i in range(len(kw_ss_i_low_1track_50L1TAU12med)):
	if kw_ss_i_low_1track_50L1TAU12med[i]<min_kw_ss_i_low_1track_50L1TAU12med:
		min_kw_ss_i_low_1track_50L1TAU12med = kw_ss_i_low_1track_50L1TAU12med[i]
	if kw_ss_i_low_1track_50L1TAU12med[i]>max_kw_ss_i_low_1track_50L1TAU12med:
		max_kw_ss_i_low_1track_50L1TAU12med = kw_ss_i_low_1track_50L1TAU12med[i]


for i in range(len(kw_ss_i_high_1track_50L1TAU12med)):
        if kw_ss_i_high_1track_50L1TAU12med[i]<min_kw_ss_i_high_1track_50L1TAU12med:
                min_kw_ss_i_high_1track_50L1TAU12med = kw_ss_i_high_1track_50L1TAU12med[i]
        if kw_ss_i_high_1track_50L1TAU12med[i]>max_kw_ss_i_high_1track_50L1TAU12med:
                max_kw_ss_i_high_1track_50L1TAU12med = kw_ss_i_high_1track_50L1TAU12med[i]

print " 50L1TAU12med: sys_i_low =", ((max_kw_ss_i_low_1track_50L1TAU12med - min_kw_ss_i_low_1track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_high =", ((max_kw_ss_i_high_1track_50L1TAU12med - min_kw_ss_i_high_1track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_50L1TAU12med - min_kw_ss_i_low_1track_50L1TAU12med)/2)/kw_ss_i_low_1track_50L1TAU12med_val
print " 50L1TAU12med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_50L1TAU12med - min_kw_ss_i_high_1track_50L1TAU12med)/2)/kw_ss_i_high_1track_50L1TAU12med_val

################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
kw_ss_i_low_1track_80med_val = 1.629 
kw_ss_i_high_1track_80med_val = 3.055

kw_ss_i_low_1track_80med = [1.568, 1.388, 1.351, 1.155]#, 0.809]
kw_ss_i_high_1track_80med = [3.296, 3.070, 3.902, 3.859]#, 1.617, 4.111, 4.449, 4.353, 3.473, 2.931]

min_kw_ss_i_low_1track_80med = 20
max_kw_ss_i_low_1track_80med = 0
min_kw_ss_i_high_1track_80med = 20
max_kw_ss_i_high_1track_80med = 0

for i in range(len(kw_ss_i_low_1track_80med)):
	if kw_ss_i_low_1track_80med[i]<min_kw_ss_i_low_1track_80med:
		min_kw_ss_i_low_1track_80med = kw_ss_i_low_1track_80med[i]
	if kw_ss_i_low_1track_80med[i]>max_kw_ss_i_low_1track_80med:
		max_kw_ss_i_low_1track_80med = kw_ss_i_low_1track_80med[i]


for i in range(len(kw_ss_i_high_1track_80med)):
        if kw_ss_i_high_1track_80med[i]<min_kw_ss_i_high_1track_80med:
                min_kw_ss_i_high_1track_80med = kw_ss_i_high_1track_80med[i]
        if kw_ss_i_high_1track_80med[i]>max_kw_ss_i_high_1track_80med:
                max_kw_ss_i_high_1track_80med = kw_ss_i_high_1track_80med[i]

print " 80med: sys_i_low =", ((max_kw_ss_i_low_1track_80med - min_kw_ss_i_low_1track_80med)/2)
print " 80med: sys_i_high =", ((max_kw_ss_i_high_1track_80med - min_kw_ss_i_high_1track_80med)/2)
print " 80med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_80med - min_kw_ss_i_low_1track_80med)/2)/kw_ss_i_low_1track_80med_val
print " 80med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_80med - min_kw_ss_i_high_1track_80med)/2)/kw_ss_i_high_1track_80med_val


################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
kw_ss_i_low_1track_80L1TAU60med_val = 0.609 
kw_ss_i_high_1track_80L1TAU60med_val = 2.687

kw_ss_i_low_1track_80L1TAU60med = [0.609]#, 0.550]
kw_ss_i_high_1track_80L1TAU60med = [2.530, 2.216, 3.862, 3.577]#, 3.412, 3.424, 3.764, 3.871, 3.202, 2.473]

min_kw_ss_i_low_1track_80L1TAU60med = 20
max_kw_ss_i_low_1track_80L1TAU60med = 0
min_kw_ss_i_high_1track_80L1TAU60med = 20
max_kw_ss_i_high_1track_80L1TAU60med = 0

for i in range(len(kw_ss_i_low_1track_80L1TAU60med)):
	if kw_ss_i_low_1track_80L1TAU60med[i]<min_kw_ss_i_low_1track_80L1TAU60med:
		min_kw_ss_i_low_1track_80L1TAU60med = kw_ss_i_low_1track_80L1TAU60med[i]
	if kw_ss_i_low_1track_80L1TAU60med[i]>max_kw_ss_i_low_1track_80L1TAU60med:
		max_kw_ss_i_low_1track_80L1TAU60med = kw_ss_i_low_1track_80L1TAU60med[i]


for i in range(len(kw_ss_i_high_1track_80L1TAU60med)):
        if kw_ss_i_high_1track_80L1TAU60med[i]<min_kw_ss_i_high_1track_80L1TAU60med:
                min_kw_ss_i_high_1track_80L1TAU60med = kw_ss_i_high_1track_80L1TAU60med[i]
        if kw_ss_i_high_1track_80L1TAU60med[i]>max_kw_ss_i_high_1track_80L1TAU60med:
                max_kw_ss_i_high_1track_80L1TAU60med = kw_ss_i_high_1track_80L1TAU60med[i]

print " 80L1TAU60med: sys_i_low =", ((max_kw_ss_i_low_1track_80L1TAU60med - min_kw_ss_i_low_1track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_high =", ((max_kw_ss_i_high_1track_80L1TAU60med - min_kw_ss_i_high_1track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_80L1TAU60med - min_kw_ss_i_low_1track_80L1TAU60med)/2)/kw_ss_i_low_1track_80L1TAU60med_val
print " 80L1TAU60med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_80L1TAU60med - min_kw_ss_i_high_1track_80L1TAU60med)/2)/kw_ss_i_high_1track_80L1TAU60med_val


################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
kw_ss_i_low_1track_125med_val = 1
kw_ss_i_high_1track_125med_val = 3.608

kw_ss_i_low_1track_125med = [1]
kw_ss_i_high_1track_125med = [3.560, 3.864, 5.122, 4.101]#, 3.956, 6.852, 5.792, 4.719, 3.232, 2.470]

min_kw_ss_i_low_1track_125med = 20
max_kw_ss_i_low_1track_125med = 0
min_kw_ss_i_high_1track_125med = 20
max_kw_ss_i_high_1track_125med = 0

for i in range(len(kw_ss_i_low_1track_125med)):
	if kw_ss_i_low_1track_125med[i]<min_kw_ss_i_low_1track_125med:
		min_kw_ss_i_low_1track_125med = kw_ss_i_low_1track_125med[i]
	if kw_ss_i_low_1track_125med[i]>max_kw_ss_i_low_1track_125med:
		max_kw_ss_i_low_1track_125med = kw_ss_i_low_1track_125med[i]


for i in range(len(kw_ss_i_high_1track_125med)):
        if kw_ss_i_high_1track_125med[i]<min_kw_ss_i_high_1track_125med:
                min_kw_ss_i_high_1track_125med = kw_ss_i_high_1track_125med[i]
        if kw_ss_i_high_1track_125med[i]>max_kw_ss_i_high_1track_125med:
                max_kw_ss_i_high_1track_125med = kw_ss_i_high_1track_125med[i]

print " 125med: sys_i_low =", ((max_kw_ss_i_low_1track_125med - min_kw_ss_i_low_1track_125med)/2)
print " 125med: sys_i_high =", ((max_kw_ss_i_high_1track_125med - min_kw_ss_i_high_1track_125med)/2)
print " 125med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_125med - min_kw_ss_i_low_1track_125med)/2)/kw_ss_i_low_1track_125med_val
print " 125med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_125med - min_kw_ss_i_high_1track_125med)/2)/kw_ss_i_high_1track_125med_val


################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
kw_ss_i_low_1track_160med_val = 1 
kw_ss_i_high_1track_160med_val = 12.180 

kw_ss_i_low_1track_160med = [1]
kw_ss_i_high_1track_160med = [11.860]

min_kw_ss_i_low_1track_160med = 20
max_kw_ss_i_low_1track_160med = 0
min_kw_ss_i_high_1track_160med = 20
max_kw_ss_i_high_1track_160med = 0

for i in range(len(kw_ss_i_low_1track_160med)):
	if kw_ss_i_low_1track_160med[i]<min_kw_ss_i_low_1track_160med:
		min_kw_ss_i_low_1track_160med = kw_ss_i_low_1track_160med[i]
	if kw_ss_i_low_1track_160med[i]>max_kw_ss_i_low_1track_160med:
		max_kw_ss_i_low_1track_160med = kw_ss_i_low_1track_160med[i]


for i in range(len(kw_ss_i_high_1track_160med)):
        if kw_ss_i_high_1track_160med[i]<min_kw_ss_i_high_1track_160med:
                min_kw_ss_i_high_1track_160med = kw_ss_i_high_1track_160med[i]
        if kw_ss_i_high_1track_160med[i]>max_kw_ss_i_high_1track_160med:
                max_kw_ss_i_high_1track_160med = kw_ss_i_high_1track_160med[i]

print " 160med: sys_i_low =", ((max_kw_ss_i_low_1track_160med - min_kw_ss_i_low_1track_160med)/2)
print " 160med: sys_i_high =", ((max_kw_ss_i_high_1track_160med - min_kw_ss_i_high_1track_160med)/2)
print " 160med: sys_i_low (percentage) =", ((max_kw_ss_i_low_1track_160med - min_kw_ss_i_low_1track_160med)/2)/kw_ss_i_low_1track_160med_val
print " 160med: sys_i_high (percentage) =", ((max_kw_ss_i_high_1track_160med - min_kw_ss_i_high_1track_160med)/2)/kw_ss_i_high_1track_160med_val

# ----------------------------------- #
#     	  ptonly1Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_ptonly1Track_val = 1.701 
kw_ss_i_high_ptonly1Track_val = 2.043

kw_ss_i_low_ptonly1Track = [1.786, 1.762, 1.716, 1.682]
kw_ss_i_high_ptonly1Track = [2.191, 2.152, 2.103, 2.131]

min_kw_ss_i_low_ptonly1Track = 20
max_kw_ss_i_low_ptonly1Track = 0
min_kw_ss_i_high_ptonly1Track = 20
max_kw_ss_i_high_ptonly1Track = 0

for i in range(len(kw_ss_i_low_ptonly1Track)):
	if kw_ss_i_low_ptonly1Track[i]<min_kw_ss_i_low_ptonly1Track:
		min_kw_ss_i_low_ptonly1Track = kw_ss_i_low_ptonly1Track[i]
	if kw_ss_i_low_ptonly1Track[i]>max_kw_ss_i_low_ptonly1Track:
		max_kw_ss_i_low_ptonly1Track = kw_ss_i_low_ptonly1Track[i]


for i in range(len(kw_ss_i_high_ptonly1Track)):
        if kw_ss_i_high_ptonly1Track[i]<min_kw_ss_i_high_ptonly1Track:
                min_kw_ss_i_high_ptonly1Track = kw_ss_i_high_ptonly1Track[i]
        if kw_ss_i_high_ptonly1Track[i]>max_kw_ss_i_high_ptonly1Track:
                max_kw_ss_i_high_ptonly1Track = kw_ss_i_high_ptonly1Track[i]

print " ptonly1Track: sys_i_low =", ((max_kw_ss_i_low_ptonly1Track - min_kw_ss_i_low_ptonly1Track)/2)
print " ptonly1Track: sys_i_high =", ((max_kw_ss_i_high_ptonly1Track - min_kw_ss_i_high_ptonly1Track)/2)
print " ptonly1Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_ptonly1Track - min_kw_ss_i_low_ptonly1Track)/2)/kw_ss_i_low_ptonly1Track_val
print " ptonly1Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_ptonly1Track - min_kw_ss_i_high_ptonly1Track)/2)/kw_ss_i_high_ptonly1Track_val
# ----------------------------------- #
#     	   tracktwo1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_tracktwo1Track_val = 1.629 
kw_ss_i_high_tracktwo1Track_val = 1.999

kw_ss_i_low_tracktwo1Track = [1.721, 1.701, 1.658, 1.617]
kw_ss_i_high_tracktwo1Track = [2.161, 2.120, 2.060, 2.076]

min_kw_ss_i_low_tracktwo1Track = 20
max_kw_ss_i_low_tracktwo1Track = 0
min_kw_ss_i_high_tracktwo1Track = 20
max_kw_ss_i_high_tracktwo1Track = 0

for i in range(len(kw_ss_i_low_tracktwo1Track)):
	if kw_ss_i_low_tracktwo1Track[i]<min_kw_ss_i_low_tracktwo1Track:
		min_kw_ss_i_low_tracktwo1Track = kw_ss_i_low_tracktwo1Track[i]
	if kw_ss_i_low_tracktwo1Track[i]>max_kw_ss_i_low_tracktwo1Track:
		max_kw_ss_i_low_tracktwo1Track = kw_ss_i_low_tracktwo1Track[i]


for i in range(len(kw_ss_i_high_tracktwo1Track)):
        if kw_ss_i_high_tracktwo1Track[i]<min_kw_ss_i_high_tracktwo1Track:
                min_kw_ss_i_high_tracktwo1Track = kw_ss_i_high_tracktwo1Track[i]
        if kw_ss_i_high_tracktwo1Track[i]>max_kw_ss_i_high_tracktwo1Track:
                max_kw_ss_i_high_tracktwo1Track = kw_ss_i_high_tracktwo1Track[i]

print " tracktwo1Track: sys_i_low =", ((max_kw_ss_i_low_tracktwo1Track - min_kw_ss_i_low_tracktwo1Track)/2)
print " tracktwo1Track: sys_i_high =", ((max_kw_ss_i_high_tracktwo1Track - min_kw_ss_i_high_tracktwo1Track)/2)
print " tracktwo1Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_tracktwo1Track - min_kw_ss_i_low_tracktwo1Track)/2)/kw_ss_i_low_tracktwo1Track_val
print " tracktwo1Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_tracktwo1Track - min_kw_ss_i_high_tracktwo1Track)/2)/kw_ss_i_high_tracktwo1Track_val


# ----------------------------------- #
#     	   L1TAU12IM1Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_L1TAU12IM1Track_val = 1.569 
kw_ss_i_high_L1TAU12IM1Track_val = 2.038

kw_ss_i_low_L1TAU12IM1Track = [1.568, 1.559, 1.524, 1.502]#, 1.457, 1.456, 1.414, 1.446, 1.468, 1.443]
kw_ss_i_high_L1TAU12IM1Track = [2.051, 2.012, 1.962, 1.981]#, 1.960, 1.969, 2.090, 2.126, 2.021, 2.010]

min_kw_ss_i_low_L1TAU12IM1Track = 20
max_kw_ss_i_low_L1TAU12IM1Track = 0
min_kw_ss_i_high_L1TAU12IM1Track = 20
max_kw_ss_i_high_L1TAU12IM1Track = 0

for i in range(len(kw_ss_i_low_L1TAU12IM1Track)):
	if kw_ss_i_low_L1TAU12IM1Track[i]<min_kw_ss_i_low_L1TAU12IM1Track:
		min_kw_ss_i_low_L1TAU12IM1Track = kw_ss_i_low_L1TAU12IM1Track[i]
	if kw_ss_i_low_L1TAU12IM1Track[i]>max_kw_ss_i_low_L1TAU12IM1Track:
		max_kw_ss_i_low_L1TAU12IM1Track = kw_ss_i_low_L1TAU12IM1Track[i]


for i in range(len(kw_ss_i_high_L1TAU12IM1Track)):
        if kw_ss_i_high_L1TAU12IM1Track[i]<min_kw_ss_i_high_L1TAU12IM1Track:
                min_kw_ss_i_high_L1TAU12IM1Track = kw_ss_i_high_L1TAU12IM1Track[i]
        if kw_ss_i_high_L1TAU12IM1Track[i]>max_kw_ss_i_high_L1TAU12IM1Track:
                max_kw_ss_i_high_L1TAU12IM1Track = kw_ss_i_high_L1TAU12IM1Track[i]

print " L1TAU12IM1Track: sys_i_low =", ((max_kw_ss_i_low_L1TAU12IM1Track - min_kw_ss_i_low_L1TAU12IM1Track)/2)
print " L1TAU12IM1Track: sys_i_high =", ((max_kw_ss_i_high_L1TAU12IM1Track - min_kw_ss_i_high_L1TAU12IM1Track)/2)
print " L1TAU12IM1Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_L1TAU12IM1Track - min_kw_ss_i_low_L1TAU12IM1Track)/2)/kw_ss_i_low_L1TAU12IM1Track_val
print " L1TAU12IM1Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_L1TAU12IM1Track - min_kw_ss_i_high_L1TAU12IM1Track)/2)/kw_ss_i_high_L1TAU12IM1Track_val

print ""
print "THREE PRONG"
print ""
print "*******************"
print ""

print " ----------------------------------- "
print "            no trigger"
print " ------------------------------------"

# LOW VS HIGH PT
kw_ss_i_low_3track_val = 1.575 
kw_ss_i_high_3track_val = 2.082

kw_ss_i_low_3track = [1.578, 1.577, 1.549, 1.543]#, 1.545, 1.575, 1.646, 1.754, 1.661, 1.619]
kw_ss_i_high_3track = [2.072, 2.086, 2.138, 2.189]#, 2.226, 2.291, 2.272, 2.066, 2.137, 2.496]

diff_kw_ss_i_low_val_3track = 0
diff_kw_ss_i_high_val_3track = 0

min_kw_ss_i_low_3track = 20
max_kw_ss_i_low_3track = 0
min_kw_ss_i_high_3track = 20
max_kw_ss_i_high_3track = 0

for i in range(len(kw_ss_i_low_3track)):
	if kw_ss_i_low_3track[i]<min_kw_ss_i_low_3track:
		min_kw_ss_i_low_3track = kw_ss_i_low_3track[i]
	if kw_ss_i_low_3track[i]>max_kw_ss_i_low_3track:
		max_kw_ss_i_low_3track = kw_ss_i_low_3track[i]


for i in range(len(kw_ss_i_high_3track)):
        if kw_ss_i_high_3track[i]<min_kw_ss_i_high_3track:
                min_kw_ss_i_high_3track = kw_ss_i_high_3track[i]
        if kw_ss_i_high_3track[i]>max_kw_ss_i_high_3track:
                max_kw_ss_i_high_3track = kw_ss_i_high_3track[i]

print "no_trig: sys_i_low =", ((max_kw_ss_i_low_3track - min_kw_ss_i_low_3track)/2)
print "no_trig: sys_i_high =", ((max_kw_ss_i_high_3track - min_kw_ss_i_high_3track)/2)
print "no_trig: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track - min_kw_ss_i_low_3track)/2)/kw_ss_i_low_3track_val
print "no_trig: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track - min_kw_ss_i_high_3track)/2)/kw_ss_i_high_3track_val

print " ----------------------------------- "
print "            25 med trigger"
print " ------------------------------------"

# LOW VS HIGH PT

kw_ss_i_low_3track_25med_val = 1.396
kw_ss_i_high_3track_25med_val = 1.893

kw_ss_i_low_3track_25med = [1.389, 1.386, 1.373, 1.314]#, 1.334, 1.210, 1.221, 1.204, 1.187, 1.161]
kw_ss_i_high_3track_25med = [1.904, 1.926, 2.102, 2.123]#, 2.229, 2.468, 2.306, 1.958, 2.155, 2.787]

min_kw_ss_i_low_3track_25med = 20
max_kw_ss_i_low_3track_25med = 0
min_kw_ss_i_high_3track_25med = 20
max_kw_ss_i_high_3track_25med = 0

for i in range(len(kw_ss_i_low_3track_25med)):
	if kw_ss_i_low_3track_25med[i]<min_kw_ss_i_low_3track_25med:
		min_kw_ss_i_low_3track_25med = kw_ss_i_low_3track_25med[i]
	if kw_ss_i_low_3track_25med[i]>max_kw_ss_i_low_3track_25med:
		max_kw_ss_i_low_3track_25med = kw_ss_i_low_3track_25med[i]


for i in range(len(kw_ss_i_high_3track_25med)):
        if kw_ss_i_high_3track_25med[i]<min_kw_ss_i_high_3track_25med:
                min_kw_ss_i_high_3track_25med = kw_ss_i_high_3track_25med[i]
        if kw_ss_i_high_3track_25med[i]>max_kw_ss_i_high_3track_25med:
                max_kw_ss_i_high_3track_25med = kw_ss_i_high_3track_25med[i]

print " 25med: sys_i_low =", ((max_kw_ss_i_low_3track_25med - min_kw_ss_i_low_3track_25med)/2)
print " 25med: sys_i_high =", ((max_kw_ss_i_high_3track_25med - min_kw_ss_i_high_3track_25med)/2)
print " 25med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_25med - min_kw_ss_i_low_3track_25med)/2)/kw_ss_i_low_3track_25med_val
print " 25med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_25med - min_kw_ss_i_high_3track_25med)/2)/kw_ss_i_high_3track_25med_val

#######################################
print " ----------------------------------- "
print "            35 med trigger"
print " ------------------------------------"

kw_ss_i_low_3track_35med_val = 2.674
kw_ss_i_high_3track_35med_val = 1.940

kw_ss_i_low_3track_35med = [2.540, 2.347, 2.263, 2.116]#, 0.923, 0.864, 0.735, 0.490, 0.364, 0.135]
kw_ss_i_high_3track_35med = [1.962, 2.073, 2.505, 2.760]#, 2.889, 3.042, 2.973, 2.321, 2.998, 3.613]

min_kw_ss_i_low_3track_35med = 20
max_kw_ss_i_low_3track_35med = 0
min_kw_ss_i_high_3track_35med = 20
max_kw_ss_i_high_3track_35med = 0

for i in range(len(kw_ss_i_low_3track_35med)):
	if kw_ss_i_low_3track_35med[i]<min_kw_ss_i_low_3track_35med:
		min_kw_ss_i_low_3track_35med = kw_ss_i_low_3track_35med[i]
	if kw_ss_i_low_3track_35med[i]>max_kw_ss_i_low_3track_35med:
		max_kw_ss_i_low_3track_35med = kw_ss_i_low_3track_35med[i]


for i in range(len(kw_ss_i_high_3track_35med)):
        if kw_ss_i_high_3track_35med[i]<min_kw_ss_i_high_3track_35med:
                min_kw_ss_i_high_3track_35med = kw_ss_i_high_3track_35med[i]
        if kw_ss_i_high_3track_35med[i]>max_kw_ss_i_high_3track_35med:
                max_kw_ss_i_high_3track_35med = kw_ss_i_high_3track_35med[i]

print " 35med: sys_i_low =", ((max_kw_ss_i_low_3track_35med - min_kw_ss_i_low_3track_35med)/2)
print " 35med: sys_i_high =", ((max_kw_ss_i_high_3track_35med - min_kw_ss_i_high_3track_35med)/2)
print " 35med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_35med - min_kw_ss_i_low_3track_35med)/2)/kw_ss_i_low_3track_35med_val
print " 35med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_35med - min_kw_ss_i_high_3track_35med)/2)/kw_ss_i_high_3track_35med_val

################################################################################################
print " ----------------------------------- "
print "            50l1tau12med trigger"
print " ------------------------------------"
kw_ss_i_low_3track_50L1TAU12med_val = 3.730  
kw_ss_i_high_3track_50L1TAU12med_val = 3.619

kw_ss_i_low_3track_50L1TAU12med = [3.730, 3.600, 3.543, 3.530]#, 3.231, 2.972, 0.595, 0.431, 0.266, 0.022]
kw_ss_i_high_3track_50L1TAU12med = [4.440, 5.018, 4.981]#, 3.917, 4.168, 3.925, 5.444, 4.221, 3.499, 4.290]

min_kw_ss_i_low_3track_50L1TAU12med = 20
max_kw_ss_i_low_3track_50L1TAU12med = 0
min_kw_ss_i_high_3track_50L1TAU12med = 20
max_kw_ss_i_high_3track_50L1TAU12med = 0

for i in range(len(kw_ss_i_low_3track_50L1TAU12med)):
	if kw_ss_i_low_3track_50L1TAU12med[i]<min_kw_ss_i_low_3track_50L1TAU12med:
		min_kw_ss_i_low_3track_50L1TAU12med = kw_ss_i_low_3track_50L1TAU12med[i]
	if kw_ss_i_low_3track_50L1TAU12med[i]>max_kw_ss_i_low_3track_50L1TAU12med:
		max_kw_ss_i_low_3track_50L1TAU12med = kw_ss_i_low_3track_50L1TAU12med[i]


for i in range(len(kw_ss_i_high_3track_50L1TAU12med)):
        if kw_ss_i_high_3track_50L1TAU12med[i]<min_kw_ss_i_high_3track_50L1TAU12med:
                min_kw_ss_i_high_3track_50L1TAU12med = kw_ss_i_high_3track_50L1TAU12med[i]
        if kw_ss_i_high_3track_50L1TAU12med[i]>max_kw_ss_i_high_3track_50L1TAU12med:
                max_kw_ss_i_high_3track_50L1TAU12med = kw_ss_i_high_3track_50L1TAU12med[i]

print " 50L1TAU12med: sys_i_low =", ((max_kw_ss_i_low_3track_50L1TAU12med - min_kw_ss_i_low_3track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_high =", ((max_kw_ss_i_high_3track_50L1TAU12med - min_kw_ss_i_high_3track_50L1TAU12med)/2)
print " 50L1TAU12med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_50L1TAU12med - min_kw_ss_i_low_3track_50L1TAU12med)/2)/kw_ss_i_low_3track_50L1TAU12med_val
print " 50L1TAU12med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_50L1TAU12med - min_kw_ss_i_high_3track_50L1TAU12med)/2)/kw_ss_i_high_3track_50L1TAU12med_val

################################################################################################
print " ----------------------------------- "
print "            80 med trigger"
print " ------------------------------------"
kw_ss_i_low_3track_80med_val = 0.502
kw_ss_i_high_3track_80med_val = 3.324

kw_ss_i_low_3track_80med = [0.502, 0.502, 0.564, 0.619]#, 0.474, 0.474, 0.399, 0.159, 0.191, 0.231]
kw_ss_i_high_3track_80med = [3.198, 2.784, 4.532, 4.157]#, 3.853, 3.041, 2.433, 2.098, 1.758, 1.386]

min_kw_ss_i_low_3track_80med = 20
max_kw_ss_i_low_3track_80med = 0
min_kw_ss_i_high_3track_80med = 20
max_kw_ss_i_high_3track_80med = 0

for i in range(len(kw_ss_i_low_3track_80med)):
	if kw_ss_i_low_3track_80med[i]<min_kw_ss_i_low_3track_80med:
		min_kw_ss_i_low_3track_80med = kw_ss_i_low_3track_80med[i]
	if kw_ss_i_low_3track_80med[i]>max_kw_ss_i_low_3track_80med:
		max_kw_ss_i_low_3track_80med = kw_ss_i_low_3track_80med[i]


for i in range(len(kw_ss_i_high_3track_80med)):
        if kw_ss_i_high_3track_80med[i]<min_kw_ss_i_high_3track_80med:
                min_kw_ss_i_high_3track_80med = kw_ss_i_high_3track_80med[i]
        if kw_ss_i_high_3track_80med[i]>max_kw_ss_i_high_3track_80med:
                max_kw_ss_i_high_3track_80med = kw_ss_i_high_3track_80med[i]

print " 80med: sys_i_low =", ((max_kw_ss_i_low_3track_80med - min_kw_ss_i_low_3track_80med)/2)
print " 80med: sys_i_high =", ((max_kw_ss_i_high_3track_80med - min_kw_ss_i_high_3track_80med)/2)
print " 80med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_80med - min_kw_ss_i_low_3track_80med)/2)/kw_ss_i_low_3track_80med_val
print " 80med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_80med - min_kw_ss_i_high_3track_80med)/2)/kw_ss_i_high_3track_80med_val


################################################################################################
print " ----------------------------------- "
print "            80L1TAU60 med trigger"
print " ------------------------------------"
kw_ss_i_low_3track_80L1TAU60med_val = 0.351  
kw_ss_i_high_3track_80L1TAU60med_val = 1.870

kw_ss_i_low_3track_80L1TAU60med = [0.351, 0.351, 0.375, 0.416]#, 0.375, 0.375, 0.403, 0.196, 0.228, 0.268]
kw_ss_i_high_3track_80L1TAU60med = [1.728, 1.481, 2.615, 2.471]#, 2.457, 2.187, 1.864, 1.645, 1.400, 1.178]

min_kw_ss_i_low_3track_80L1TAU60med = 20
max_kw_ss_i_low_3track_80L1TAU60med = 0
min_kw_ss_i_high_3track_80L1TAU60med = 20
max_kw_ss_i_high_3track_80L1TAU60med = 0

for i in range(len(kw_ss_i_low_3track_80L1TAU60med)):
	if kw_ss_i_low_3track_80L1TAU60med[i]<min_kw_ss_i_low_3track_80L1TAU60med:
		min_kw_ss_i_low_3track_80L1TAU60med = kw_ss_i_low_3track_80L1TAU60med[i]
	if kw_ss_i_low_3track_80L1TAU60med[i]>max_kw_ss_i_low_3track_80L1TAU60med:
		max_kw_ss_i_low_3track_80L1TAU60med = kw_ss_i_low_3track_80L1TAU60med[i]


for i in range(len(kw_ss_i_high_3track_80L1TAU60med)):
        if kw_ss_i_high_3track_80L1TAU60med[i]<min_kw_ss_i_high_3track_80L1TAU60med:
                min_kw_ss_i_high_3track_80L1TAU60med = kw_ss_i_high_3track_80L1TAU60med[i]
        if kw_ss_i_high_3track_80L1TAU60med[i]>max_kw_ss_i_high_3track_80L1TAU60med:
                max_kw_ss_i_high_3track_80L1TAU60med = kw_ss_i_high_3track_80L1TAU60med[i]

print " 80L1TAU60med: sys_i_low =", ((max_kw_ss_i_low_3track_80L1TAU60med - min_kw_ss_i_low_3track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_high =", ((max_kw_ss_i_high_3track_80L1TAU60med - min_kw_ss_i_high_3track_80L1TAU60med)/2)
print " 80L1TAU60med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_80L1TAU60med - min_kw_ss_i_low_3track_80L1TAU60med)/2)/kw_ss_i_low_3track_80L1TAU60med_val
print " 80L1TAU60med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_80L1TAU60med - min_kw_ss_i_high_3track_80L1TAU60med)/2)/kw_ss_i_high_3track_80L1TAU60med_val


################################################################################################
print " ----------------------------------- "
print "            125 med trigger"
print " ------------------------------------"
kw_ss_i_low_3track_125med_val = 1 
kw_ss_i_high_3track_125med_val = 1

kw_ss_i_low_3track_125med = [1]
kw_ss_i_high_3track_125med = [1]

min_kw_ss_i_low_3track_125med = 20
max_kw_ss_i_low_3track_125med = 0
min_kw_ss_i_high_3track_125med = 20
max_kw_ss_i_high_3track_125med = 0

for i in range(len(kw_ss_i_low_3track_125med)):
	if kw_ss_i_low_3track_125med[i]<min_kw_ss_i_low_3track_125med:
		min_kw_ss_i_low_3track_125med = kw_ss_i_low_3track_125med[i]
	if kw_ss_i_low_3track_125med[i]>max_kw_ss_i_low_3track_125med:
		max_kw_ss_i_low_3track_125med = kw_ss_i_low_3track_125med[i]


for i in range(len(kw_ss_i_high_3track_125med)):
        if kw_ss_i_high_3track_125med[i]<min_kw_ss_i_high_3track_125med:
                min_kw_ss_i_high_3track_125med = kw_ss_i_high_3track_125med[i]
        if kw_ss_i_high_3track_125med[i]>max_kw_ss_i_high_3track_125med:
                max_kw_ss_i_high_3track_125med = kw_ss_i_high_3track_125med[i]

print " 125med: sys_i_low =", ((max_kw_ss_i_low_3track_125med - min_kw_ss_i_low_3track_125med)/2)
print " 125med: sys_i_high =", ((max_kw_ss_i_high_3track_125med - min_kw_ss_i_high_3track_125med)/2)
print " 125med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_125med - min_kw_ss_i_low_3track_125med)/2)/kw_ss_i_low_3track_125med_val
print " 125med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_125med - min_kw_ss_i_high_3track_125med)/2)/kw_ss_i_high_3track_125med_val


################################################################################################
print " ----------------------------------- "
print "            160 med trigger"
print " ------------------------------------"
kw_ss_i_low_3track_160med_val = 1
kw_ss_i_high_3track_160med_val = 1

kw_ss_i_low_3track_160med = [1]
kw_ss_i_high_3track_160med = [1]

min_kw_ss_i_low_3track_160med = 20
max_kw_ss_i_low_3track_160med = 0
min_kw_ss_i_high_3track_160med = 20
max_kw_ss_i_high_3track_160med = 0

for i in range(len(kw_ss_i_low_3track_160med)):
	if kw_ss_i_low_3track_160med[i]<min_kw_ss_i_low_3track_160med:
		min_kw_ss_i_low_3track_160med = kw_ss_i_low_3track_160med[i]
	if kw_ss_i_low_3track_160med[i]>max_kw_ss_i_low_3track_160med:
		max_kw_ss_i_low_3track_160med = kw_ss_i_low_3track_160med[i]


for i in range(len(kw_ss_i_high_3track_160med)):
        if kw_ss_i_high_3track_160med[i]<min_kw_ss_i_high_3track_160med:
                min_kw_ss_i_high_3track_160med = kw_ss_i_high_3track_160med[i]
        if kw_ss_i_high_3track_160med[i]>max_kw_ss_i_high_3track_160med:
                max_kw_ss_i_high_3track_160med = kw_ss_i_high_3track_160med[i]

print " 160med: sys_i_low =", ((max_kw_ss_i_low_3track_160med - min_kw_ss_i_low_3track_160med)/2)
print " 160med: sys_i_high =", ((max_kw_ss_i_high_3track_160med - min_kw_ss_i_high_3track_160med)/2)
print " 160med: sys_i_low (percentage) =", ((max_kw_ss_i_low_3track_160med - min_kw_ss_i_low_3track_160med)/2)/kw_ss_i_low_3track_160med_val
print " 160med: sys_i_high (percentage) =", ((max_kw_ss_i_high_3track_160med - min_kw_ss_i_high_3track_160med)/2)/kw_ss_i_high_3track_160med_val

# ----------------------------------- #
#     	  ptonly3Track  trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_ptonly3Track_val = 1.924
kw_ss_i_high_ptonly3Track_val = 2.043

kw_ss_i_low_ptonly3Track = [1.991, 2.002, 2.068, 2.008]
kw_ss_i_high_ptonly3Track = [2.121, 2.162, 2.268, 2.366]

min_kw_ss_i_low_ptonly3Track = 20
max_kw_ss_i_low_ptonly3Track = 0
min_kw_ss_i_high_ptonly3Track = 20
max_kw_ss_i_high_ptonly3Track = 0

for i in range(len(kw_ss_i_low_ptonly3Track)):
	if kw_ss_i_low_ptonly3Track[i]<min_kw_ss_i_low_ptonly3Track:
		min_kw_ss_i_low_ptonly3Track = kw_ss_i_low_ptonly3Track[i]
	if kw_ss_i_low_ptonly3Track[i]>max_kw_ss_i_low_ptonly3Track:
		max_kw_ss_i_low_ptonly3Track = kw_ss_i_low_ptonly3Track[i]


for i in range(len(kw_ss_i_high_ptonly3Track)):
        if kw_ss_i_high_ptonly3Track[i]<min_kw_ss_i_high_ptonly3Track:
                min_kw_ss_i_high_ptonly3Track = kw_ss_i_high_ptonly3Track[i]
        if kw_ss_i_high_ptonly3Track[i]>max_kw_ss_i_high_ptonly3Track:
                max_kw_ss_i_high_ptonly3Track = kw_ss_i_high_ptonly3Track[i]

print " ptonly3Track: sys_i_low =", ((max_kw_ss_i_low_ptonly3Track - min_kw_ss_i_low_ptonly3Track)/2)
print " ptonly3Track: sys_i_high =", ((max_kw_ss_i_high_ptonly3Track - min_kw_ss_i_high_ptonly3Track)/2)
print " ptonly3Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_ptonly3Track - min_kw_ss_i_low_ptonly3Track)/2)/kw_ss_i_low_ptonly3Track_val
print " ptonly3Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_ptonly3Track - min_kw_ss_i_high_ptonly3Track)/2)/kw_ss_i_high_ptonly3Track_val
# ----------------------------------- #
#     	   tracktwo3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_tracktwo3Track_val =  1.668
kw_ss_i_high_tracktwo3Track_val = 1.986

kw_ss_i_low_tracktwo3Track = [1.723, 1.717, 1.744, 1.716]
kw_ss_i_high_tracktwo3Track = [2.068, 2.053, 2.232, 2.350]

min_kw_ss_i_low_tracktwo3Track = 20
max_kw_ss_i_low_tracktwo3Track = 0
min_kw_ss_i_high_tracktwo3Track = 20
max_kw_ss_i_high_tracktwo3Track = 0

for i in range(len(kw_ss_i_low_tracktwo3Track)):
	if kw_ss_i_low_tracktwo3Track[i]<min_kw_ss_i_low_tracktwo3Track:
		min_kw_ss_i_low_tracktwo3Track = kw_ss_i_low_tracktwo3Track[i]
	if kw_ss_i_low_tracktwo3Track[i]>max_kw_ss_i_low_tracktwo3Track:
		max_kw_ss_i_low_tracktwo3Track = kw_ss_i_low_tracktwo3Track[i]


for i in range(len(kw_ss_i_high_tracktwo3Track)):
        if kw_ss_i_high_tracktwo3Track[i]<min_kw_ss_i_high_tracktwo3Track:
                min_kw_ss_i_high_tracktwo3Track = kw_ss_i_high_tracktwo3Track[i]
        if kw_ss_i_high_tracktwo3Track[i]>max_kw_ss_i_high_tracktwo3Track:
                max_kw_ss_i_high_tracktwo3Track = kw_ss_i_high_tracktwo3Track[i]

print " tracktwo3Track: sys_i_low =", ((max_kw_ss_i_low_tracktwo3Track - min_kw_ss_i_low_tracktwo3Track)/2)
print " tracktwo3Track: sys_i_high =", ((max_kw_ss_i_high_tracktwo3Track - min_kw_ss_i_high_tracktwo3Track)/2)
print " tracktwo3Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_tracktwo3Track - min_kw_ss_i_low_tracktwo3Track)/2)/kw_ss_i_low_tracktwo3Track_val
print " tracktwo3Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_tracktwo3Track - min_kw_ss_i_high_tracktwo3Track)/2)/kw_ss_i_high_tracktwo3Track_val


# ----------------------------------- #
#     	   L1TAU12IM3Track trigger
# ------------------------------------#

# LOW VS HIGH PT
kw_ss_i_low_L1TAU12IM3Track_val = 1.460 
kw_ss_i_high_L1TAU12IM3Track_val = 2.031

kw_ss_i_low_L1TAU12IM3Track = [1.462, 1.451, 1.444, 1.419]#, 1.415, 1.418, 1.465, 1.437, 1.377, 1.259]
kw_ss_i_high_L1TAU12IM3Track = [2.026, 2.065, 2.154, 2.234]#, 2.290, 2.417, 2.284, 2.007, 2.286, 2.732]

min_kw_ss_i_low_L1TAU12IM3Track = 20
max_kw_ss_i_low_L1TAU12IM3Track = 0
min_kw_ss_i_high_L1TAU12IM3Track = 20
max_kw_ss_i_high_L1TAU12IM3Track = 0

for i in range(len(kw_ss_i_low_L1TAU12IM3Track)):
	if kw_ss_i_low_L1TAU12IM3Track[i]<min_kw_ss_i_low_L1TAU12IM3Track:
		min_kw_ss_i_low_L1TAU12IM3Track = kw_ss_i_low_L1TAU12IM3Track[i]
	if kw_ss_i_low_L1TAU12IM3Track[i]>max_kw_ss_i_low_L1TAU12IM3Track:
		max_kw_ss_i_low_L1TAU12IM3Track = kw_ss_i_low_L1TAU12IM3Track[i]


for i in range(len(kw_ss_i_high_L1TAU12IM3Track)):
        if kw_ss_i_high_L1TAU12IM3Track[i]<min_kw_ss_i_high_L1TAU12IM3Track:
                min_kw_ss_i_high_L1TAU12IM3Track = kw_ss_i_high_L1TAU12IM3Track[i]
        if kw_ss_i_high_L1TAU12IM3Track[i]>max_kw_ss_i_high_L1TAU12IM3Track:
                max_kw_ss_i_high_L1TAU12IM3Track = kw_ss_i_high_L1TAU12IM3Track[i]

print " L1TAU12IM3Track: sys_i_low =", ((max_kw_ss_i_low_L1TAU12IM3Track - min_kw_ss_i_low_L1TAU12IM3Track)/2)
print " L1TAU12IM3Track: sys_i_high =", ((max_kw_ss_i_high_L1TAU12IM3Track - min_kw_ss_i_high_L1TAU12IM3Track)/2)
print " L1TAU12IM3Track: sys_i_low (percentage) =", ((max_kw_ss_i_low_L1TAU12IM3Track - min_kw_ss_i_low_L1TAU12IM3Track)/2)/kw_ss_i_low_L1TAU12IM3Track_val
print " L1TAU12IM3Track: sys_i_high (percentage) =", ((max_kw_ss_i_high_L1TAU12IM3Track - min_kw_ss_i_high_L1TAU12IM3Track)/2)/kw_ss_i_high_L1TAU12IM3Track_val

