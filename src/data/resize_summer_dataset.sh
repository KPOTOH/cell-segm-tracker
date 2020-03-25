#!/bin/bash

for f in ../../data/raw/summer_project/*;
	do  echo "Converting $f";
	convert -resize 1392x1040 "$f"  "../../data/raw/coco/$(basename "$f")"; 
done;