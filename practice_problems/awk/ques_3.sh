#!/bin/bash

n_lines=$(awk 'END{print NR}' $1)

awk 'BEGIN{FS=":"}{
        printf "s/student_name/%s/g; s/roll_no/%s/g\n", $1, $2
        }' $1 > commands.sed 

# cat commands.sed

i=0
while ((i < n_lines)); do
    sed -f commands.sed paragraph.txt
    sed -i '1d' commands.sed
    echo
    ((i += 1))
done

rm commands.sed