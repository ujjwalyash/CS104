BEGIN	{
    FS=","
    ORS=","
}
{
    if (NR == 1){
        for(i=1; i <= NF; i++){
            print $i
        }
        printf "Amount"
        printf "\n"
    }
    else{
        for(i=1; i <= NF; i++){
            print $i
        }
        split($2, years, " ")
        time = years[1]
        amount = $3*($5)**time
        printf amount

        printf "\n"
    }
}