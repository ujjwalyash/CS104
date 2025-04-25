#!/bin/bash

tr -d '\r' < $1 > temp
cat temp > $1
rm temp

cut -d "," -f6 $1 > scores

while read -r score; do
    if [[ $score = "total-marks" ]]; then
        grade="grades"
    elif [[ $score -gt 85 ]]; then
        grade="AA"
    elif [[ $score -gt 65 ]]; then
        grade="AB"
    elif [[ $score -gt 45 ]]; then
        grade="BB"
    elif [[ $score -gt 35 ]]; then
        grade="CC"
    else
        grade="F"
    fi
    echo $grade >> grades
    ((i++))
done < scores

paste -d "," $1 grades > temp
cat temp > $1
rm scores
rm grades

# awk 'BEGIN{
#     FS = ",";
# }

# {
#     if($6 == "total-marks") {print $0 ",grades"}
#     else if($6 > 85){print $0 ",AA"}
#     else if($6 > 65){print $0 ",AB"}
#     else if($6 > 45){print $0 ",BB"}
#     else if($6 > 35){print $0 ",CC"}
#     else {print $0 ",F"}
# }' $1 > temp
# cat temp > $1

rm temp

echo $(head -1 $1) > ug24.csv
echo $(head -1 $1) > ug23.csv

grep -e "^24" $1 | sort -t "," -k7 >> ug24.csv
grep -e "^23" $1 | sort -t "," -k7 >> ug23.csv