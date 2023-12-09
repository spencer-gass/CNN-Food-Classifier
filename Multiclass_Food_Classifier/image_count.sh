#!/bin/bash
for x in `ls Food_101/images`
do
    echo $x
    ls Food_101/images/$x | wc -l    
    echo
done
