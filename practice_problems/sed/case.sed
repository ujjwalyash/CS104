s/^([a-zA-Z])([a-zA-Z]*)/\U\1\L\2/
s/ ([a-zA-Z])([a-zA-Z]*)/ \U\1\L\2/g
s/\.([a-zA-Z])([a-zA-Z]*)/.\U\1\L\2/g
s/\. ([a-zA-Z])([a-zA-Z]*)/. (\U\1)\L\2/g