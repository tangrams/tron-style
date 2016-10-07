#!/bin/sh

convert $1 -filter Jinc -resize 400% -threshold 30%  \( +clone -negate -morphology Distance Euclidean -level 50%,-50% \) -morphology Distance Euclidean -compose Plus -composite -level 0%,100% $2
convert $2 -resize 25% $2