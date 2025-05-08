#!/bin/bash

git log --format="%cI" "$@" | 
    grep -o "Z$\|[+-][0-9][0-9]:[0-9][0-9]$" |
    sed 's/://' |
    sort | uniq -c | 
    awk '{print $2, $1}' |
    sort -n



