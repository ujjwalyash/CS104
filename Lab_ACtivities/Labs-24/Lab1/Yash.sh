mkdir outputs;
cp $(find ./inputs -name "*.txt") outputs/;
cat -n $(find outputs/ -name "*.txt") > cat.txt;
cat $(find outputs/ -name "*.txt") | grep -vc ^$ > lines.txt;
