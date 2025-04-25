if [[ $# -eq 0 ]]; then
    echo "ERROR: No arguments provided"
    exit 1
elif [[ $# -eq 1 ]]; then
    echo "ERROR: No query type provided"
    exit 1
elif [[ ! -f $1 ]]; then
    echo "ERROR: File does not exist"
    exit 1
elif [[ $2 -ne 1 && $2 -ne 2 ]]; then
    echo "ERROR: Invalid query type"
    exit 1
fi

# Process Query
IFS=","
declare -A quant=( ["NRF"]=-1 )
declare -A enum=( ["type"]=0 ["price"]=1 ["year"]=2 ["color"]=3 ["quantity"]=4 )

if [[ $2 -eq 1 ]]; then

    while read line; do
        data=($line)
        if [[ -z $4  || "${data[${enum[$3]}]}" = "$4" ]]; then
            (( quant[${data[3]}]+=data[4] ))
        fi
    done < $1

    maxcolor="NRF"
    for i in "${!quant[@]}"; do
        if [[ ${quant[${maxcolor}]} -lt ${quant[$i]} ]]; then
            maxcolor=$i
        fi
    done
    echo $maxcolor
fi

if [[ $2 -eq 2 ]]; then
    found=0
    sum=0

    while read line; do
        data=($line)
        if [[ -z $3  || ( ${data[1]} -gt $3 && (-z $4 || ${data[3]} = $4 )) ]]; then
            (( sum+=data[4]*data[1] ))
            (( found = 1))
        fi
    done < $1

    if [[ $found -eq 0 ]]; then
        echo "NRF"
    else
        echo $sum
    fi
fi
