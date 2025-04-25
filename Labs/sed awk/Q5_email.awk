BEGIN{
    FS= ","
    OFS = ","
}
NR == 1 {
    $5="Email-ID"
}
NR != 1 {
    $5 = $2$4"@surveycorps.com"
}
{
    print $0
}