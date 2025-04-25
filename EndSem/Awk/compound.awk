BEGIN{
    FS=","
}
NR==1{
    printf "%s,%s\n", $0, "Amount"
}
NR!=1{
    amt = $3
    for(i=0; i" years" < $2; i++){amt *= $5}
    printf "%s,%s\n", $0, amt
}
