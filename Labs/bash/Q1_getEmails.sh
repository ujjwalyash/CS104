#!/bin/bash

if [[ $# -ne 1 ]];then
	echo "Usage: ./getEmails.sh <file>"
	exit 1
fi

if [[ ! -e $1 ]];then
	echo "Input File doesn't exist"
else
	grep -e "^[A-Za-z0-9]\+\@[A-Za-z]\+\.iitb\.ac\.in$" $1> emails.txt
	sort -fr emails.txt > sortedEmails.txt
	grep -e "^[A-Za-z0-9]\+\@cse\.iitb\.ac\.in$" sortedEmails.txt> cseEmails.txt
fi



