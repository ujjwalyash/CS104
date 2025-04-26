BEGIN	{
    FS=","
    OFS="\t"
    ORS="\t"
}
{   

    if (NR == 1){
        for(i=1; i <= NF; i++){
            print $i
        }
        #OFS, ORS dont act on printf
        printf "Average"
        printf "\n"
    }
    else{
        sum = 0
        for(i=1; i <= NF; i++){
            print $i
            sum += $i
        }
        printf sum/(NF-1)
        printf "\n"
    }
}