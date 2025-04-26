#!/bin/bash

#indexing don't worl arr[0] gives whole $@, arr[1] gives nothing
# arr=$@

#bad subsitutuion
# i=0
# while ((i < $#)); do
#     arr[i]=${${i}}
#     ((i++))
# done

i=0
for arg in $@; do
    arr[i]=$arg
    ((i++))
done

while [[ "1" == "1" ]]; do
    i=0
    sorted="True"
    while ((i<$(($#-1)))); do
        if ((arr[i] > arr[i+1])); then
            temp=${arr[$i]}
            arr[$i]=${arr[$i+1]}
            arr[$((i+1))]=$temp
            sorted="False"
        fi
        ((i++))
    done
    if [[ $sorted == "True" ]]
    then
        # echo $arr
        echo ${arr[@]}
        exit
    fi
done