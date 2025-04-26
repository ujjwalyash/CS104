#!/bin/bash

current_seconds=$(date +%s)

files=$(ls)

for file in $files; do
            #no / \.jpg$ /
    if [[ $file =~ \.jpg$ ]]; then
        time_diff=$((${current_seconds}-$(date -r $file +%s)))
        if ((time_diff/(60*60*24) < 1)); then
            echo "renamng $file"
            name=$(echo $file | grep -Eo '^[^\.]*')
            #string concat
            $(mv $file $name"_today.jpg")
        fi
    fi
done