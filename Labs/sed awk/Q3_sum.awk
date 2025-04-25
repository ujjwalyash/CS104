BEGIN{
    FS=","
    n = 1
    data["Net"] = 0
}
NR != 1 {
    if ($3 in data){
        data[$3] += $4
    }else{
        fields[n] = $3
        data[$3] = $4
        n++
    }
    data["Net"] += $4
}
{
    print $0
}
END{
    print "====="
    n = asort(fields)
    printf "Net : %d\n", data["Net"]
    for(i=1; i<=n; i++){
        printf "%s : %d\n", fields[i], data[fields[i]]
    }
}