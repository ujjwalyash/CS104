#!/bin/bash

for file in $(find . -type f -name "*.out");do
	echo $* >> ${file}
done


