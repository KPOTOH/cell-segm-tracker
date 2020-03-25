#!/usr/bin/env python3
# coding: utf-8

import glob
from shutil import copyfile, move
import os
import random
import argparse


parser = argparse.ArgumentParser(description="split all im-json set to train and val", )

parser.add_argument('-d', "--data", default='./', help='path to data dir, default=./', metavar='')
parser.add_argument('-p', "--proportion", default=.2, type=float, help='proportion of test set, default=.2', metavar='')


args = parser.parse_args()

PATH_TO_DATA = args.data
PROPORTION = args.proportion


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


images = glob.glob(os.path.join(PATH_TO_DATA, '*.jpg'))
random.shuffle(images)

N = int(len(images) * PROPORTION)
test, train = images[:N], images[N:]
im_heap = dict(test=test, train=train)

create_dir(os.path.join(PATH_TO_DATA, 'test'))
create_dir(os.path.join(PATH_TO_DATA, 'train'))


for part in im_heap:
    for src_im in im_heap[part]:
        src_jsn = src_im.replace('jpg', 'json')
        
        dst_im = os.path.join(PATH_TO_DATA, part, src_im.split('/')[-1])
        dst_jsn = dst_im.replace('jpg','json')
        
        move(src_im, dst_im)
        move(src_jsn, dst_jsn)

