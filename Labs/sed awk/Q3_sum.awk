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

-------------------------------------------------------------------------

BEGIN {
	FS=","
}

{
	if (NR != 1){
	sums[$3] += $4;	
	print
	#print DOES NOT ADD EMPTY LINE PRINTS
	#      THE LINE BEING PROCESSED USE \n
	}
	else{
		print
	}
}
END{
	print "====="
	total = 0;
	for (name in sums){
    		total += sums[name]
	}
	printf "Net : %s\n", total #not $total

	n = asorti(sums, dest)
	#asort(sums)
	#for (name in sums){
	#	printf "%s : %s\n", name, sums[name] 
	#	
	#}
	for (it = 1; it <= n; it++){
		print dest[it], ":", sums[dest[it]] 
		# PRINT AUTOMATICALLY SEPRATES BY SPACE SO
		#NO " : " NEEDED
	}
}	
