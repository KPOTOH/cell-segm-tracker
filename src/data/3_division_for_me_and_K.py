#!/usr/bin/env python
# coding: utf-8

# Import packages
import os
import numpy as np
import glob
from shutil import copyfile

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

PATH_TO_CLUSTERS = '/home/mr/cell_segmentation/data/interim/img_clusters_for_labeling/'
PATH_TO_MY = '/home/mr/cell_segmentation/data/interim/my_labeling/'
PATH_TO_K =  '/home/mr/cell_segmentation/data/interim/K_labeling/'

# get dirs of clusters
cl_dirs = glob.glob(PATH_TO_CLUSTERS + '*')

create_dir(PATH_TO_K)
create_dir(PATH_TO_MY)

for p in cl_dirs:
    create_dir(PATH_TO_MY + os.path.split(p)[-1])
    create_dir(PATH_TO_K + os.path.split(p)[-1])
    

for cl in cl_dirs:
    figs = glob.glob(cl + '/*')
    middle = len(figs) // 2
    np.random.shuffle(figs)
    
    my_figs = figs[:middle]
    for im in my_figs:
        src = im
        dst = im.replace('img_clusters_for_labeling','my_labeling')
        copyfile(src,dst)
        
    K_figs = figs[middle:]
    for im in K_figs:
        src = im
        dst = im.replace('img_clusters_for_labeling','K_labeling')
        copyfile(src,dst)
