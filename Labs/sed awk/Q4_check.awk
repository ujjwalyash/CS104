BEGIN{
    flag="YES"
    for(i=0; i < NUM_MAS; i++) {
        master_status[i]=1
    }
    for(i=0; i < NUM_WOR; i++) {
        worker_status[i]=1
    }
    for(i=0; i < TOTAL; i++) {
        item_status[i]=1
    }
    storage=0
}

/^Produced/ {
    if( item_status[$2] == 1 && master_status[$5] == 1 && storage < BUF_SIZE){
        Buffer_items[$2]=0
        item_status[$2] = 2
        storage++
    } else { flag="NO"}
}

/^Consumed/ {
    if( item_status[$2] == 2 && worker_status[$5] == 1){
        delete Buffer_items[$2]
        item_status[$2] = 3
        storage--
    } else { flag="NO"}
}

/^Master/ {
    master_status[$2] = 0
}

/^Worker/ {
    worker_status[$2] = 0
}
{
    for( indx in Buffer_items ){ printf "%s ", indx}
    printf "\n"
}
END{
    for(indx in item_status){
        if(item_status[indx] != 3){
            flag = "NO"
        }
    }
    print flag
}