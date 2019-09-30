""" Anatomical exercise
"""
#: Compatibility with Python 3
from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0

#- Our usual imports
import numpy as np
import matplotlib.pyplot as plt


#- Read file into list of float values
file_path = 'E:\Qin_lab\class_fMRI\HW2-master\Anatomical.txt'
candidate_list = []
with open(file_path, 'r') as file_object:
    for line in file_object:
#        print("This is line: " + str(line))
        candidate_list.append(float(line))
print("This is list: ")
print(candidate_list)


#- How many pixel values?
print(len(candidate_list))


#- Find the size of a slice over the third dimension
num = len(candidate_list)
num_1 = num/32

#- Find candidates for I
group_x = []
group_y = []
group = []

for x in range(150, 250):
    if num_1 % x == 0:
        group_x.append(x)
        # - Find candidate pairs for I, J
        y = num_1/x
        group_y.append(y)
        group.append([x, y])

print(group)


#- Try reshaping using some candidate pairs
#print(candidate_list)
candidate_arr = np.asarray(candidate_list)
candidate_arr_reshape = np.reshape((candidate_arr), (170, -1, 32))
# print(candidate_arr_reshape)

plt.imshow(candidate_arr_reshape[:,:,15])
plt.show()