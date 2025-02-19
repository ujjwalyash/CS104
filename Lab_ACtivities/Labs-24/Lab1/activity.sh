mkdir outputs;
cp $(find inputs -name "*.txt") -n outputs;
cat -n outputs/{.*.txt,*.txt} >> cat.txt;
grep ^[^\n] outputs/{.*.txt,*.txt} | wc -l > lines.txt;