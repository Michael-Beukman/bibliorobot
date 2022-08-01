#!/bin/bash
# This is a script that downloads a collection of papers from Arxiv, adds their bib information to a bib file and saves the pdfs in a specific location.
source env.sh
mkdir -p $RESOURCES_FOLDER

F=$PATH_TO_BIB #`pwd`/doc/bib.bib
cd `dirname $0`
rm -rf bib_tmp
mkdir -p bib_tmp
j=0

# Download each paper in parallel
for i in `cat to_download`; do 
    echo $i 
    python download.py $i $j $RESOURCES_FOLDER &
    j=$((j+1))
done

wait; # Wait for all downloads to complete

# Then add all of the separate bib files to the main one
for j in `ls bib_tmp`; do
    cat bib_tmp/$j >> $F
done
rm -rf bib_tmp # rm the temp dir
cd -