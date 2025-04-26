BEGIN	{
    FS=","
    OFS=":"
    total=0
}
{
    if (NR != 1){
        arr[$4]+=$6
        total += $6 
    }
}
END	{
    print "Total",total
    for (key in arr){
        print key, int(arr[key]*100/total)
        # roudns up not truncate
        # printf "%s:%.0f\n", key, arr[key]*100/total
    }
}