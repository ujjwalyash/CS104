#!/bin/bash

file='email.txt'

# if [[ -f $file ]];then

#     while read line;do

#     done < $file

sed -nE 's/^.*(^|:)([^@\.:]+@[^@\.:]*\.(org|com)):investor.*$/\2/p' $file | sed -E '/^micheal[^@\.:]*@/d' | sort -u