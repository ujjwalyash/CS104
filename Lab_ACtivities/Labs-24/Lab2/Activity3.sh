tar -xf files.tar.gz;

find -type f -name "file_[0-9][0-9][0-9][0-9].txt" > 1.txt
find -type f -name "*.log" > 2.txt
find bigDirectory/ -type f -perm 777 > 3.txt
find bigDirectory/ -type f -mtime -1 > 4.txt
find -type f -size +100c -mtime +7 > 5.txt
