#!/bin/bash

catalan() {

    i=$1 #this starts from 1

    if ((i==0)); then
        echo 1
    elif ((i==1)); then
        echo 1
    else

    output=0
    j=0
    # echo (($i-1))
    # why no $ before the outermost ((_)) below
    while ((j < i)); do
        ((output+=$(catalan $j)*$(catalan $((i-j-1)))))
        ((j++))
    done
    echo $output

    fi
}

catalan $1
#both work
# n=4
# echo $((5 < $(($n+2))))
# echo $((5 < (($n+2))))