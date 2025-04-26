#!/bin/bash

file=$1 #args starts from 0
declare -A arr

if [[ -f $file ]]; then
    while read line; do
        for word in $line; do # default FS used?
            # for arthmetic use ((__))
            ((arr[$word] += 1))
        done
    done < $file
fi

for key in ${!arr[@]}; do
    echo "$key: ${arr[$key]}"
done