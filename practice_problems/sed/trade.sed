# for 11CDEJUN05 the [0-9]+ will match only 1 not 11 since latter leads to complete match
# thus added that 4 CCCC must start with no digit
s/^[0-9]+[^0-9].{3}([a-zA-Z]{3})([0-9]{2})$/\2 \1/