#!/bin/bash

#make dir structure like in hdd
cat ../../data/raw/all_dirs.txt | xargs -I{} mkdir -p '{}'