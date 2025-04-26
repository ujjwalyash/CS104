#!/bin/bash
#error is not used bash: bash.sh: No such file or directory
#specifing the interpreter

i=1
found=False
all_args=$*
# "$@", $@, ${all_args(=$@)}, $*, ${all_args(=$*)} WORK
# "${all_args(=$@)}", "$*", "${all_args(=$*)}" does not work arg takes all arguments at once
for arg in ${all_args}; do
    echo "on ${i}th loop"
    # and gives errors && works
    if ((arg == $1 && i != 1)); then
        found=True
        # break works as expected
        break
    fi
    ((i++))
done

# echo ${all_args}
# echo $*
# echo $(("1 1 2 3" == 3))    


#bad gives errors bad subsituion but works
# while ((i < $#))
# do
#     # $$ is the pid itself of the script
#     if ((${${i}} == $1)); then
#     found=True
#     break
#     exit
#     fi
# done

# if ((found)); then does not work

#if ((found=="True")); then
#wrong arithmetic expression convert both strings to 0 so it always return true
if [[ $found == "True" ]]; then #no -eq
    echo "Yes"
else
    echo "No"
fi