BEGIN{
    FS=","
    tot=0
}
NR != 1{
    share[$4] += $6
    tot+=$6
}
END{
    printf "Total:%d\n", tot
    j=0
    for(i in share){
        arr[j] = i
        pct[i] = (100*share[i])/tot
        j++
    }
    for(i=0; i < j; i++){
        for(k=0; k < i; k++){
            if(pct[arr[k]] > pct[arr[k+1]]){
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
            }
        }
    }
    for(i=j-1; i >= 0; i--){
        printf "%s:%d\n", arr[i], pct[arr[i]]
    }
}