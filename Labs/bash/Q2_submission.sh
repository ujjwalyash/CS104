#!/bin/bash

for file in $(find . -type f -name "*.out");do
	echo $* >> ${file}
done

---------------------------------------------------------------------------------------------

#!/bin/bash
touch files.txt
find ./ -regex ".*\.out$" > files.txt

cat files.txt
file=files.txt
if [ -f "$file" ]; then
  while read line; do
  echo "$*" >> "$line"
  done < $file 
fi
rm files.txt
