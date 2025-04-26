BEGIN	{
    ORS=";"
}
{
    if(NR==1){
        #start i from 1 not 0
        for(i=1; i <= NF; i++){
            print $i
        }
        printf "\n"
    }
    else if(NR==2){
        
        f1 = $2
        f2 = $3
        f3 = $4

        for(i=1; i <= NF; i++){
            print $i
        }
        printf "-"
        printf "\n"
    }
    else{
        for(i=1; i <= NF; i++){
            print $i
        }
        regex_1 = "^[a-zA-Z0-9]*\\"f1"$"
        regex_2 = "^[a-zA-Z0-9]*\\"f2"$"
        regex_3 = "^[a-zA-Z0-9]*\\"f3"$"
        # regex = "/^[a-zA-Z0-9]*\\"f1"$/" / / not need in dynamic regex
        # you need the 2 backslash but not in bash when writing constant regex but need then when using dynamic regex
        if ($2 ~ regex_1 && $3 ~ regex_2 && $4 ~ regex_3){
            printf "format correct"
        }
        else{
            printf "wrong format"
        }
        printf "\n"
    }
}