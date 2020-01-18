#!/bin/bash

#To convert pdf files to text, to parse for as dataset

echo "Converting pdf files to text"

non_text_format_folder="books/non_text_format/"
text_format_folder="books/text_format/"
T=".txt"
for files in "$non_text_format_folder$1"/*.pdf
do
    name=${files%".pdf"}
    name=${name#"$non_text_format_folder$1"}
    ebook-convert "$files" "$text_format_folder$1$name$T"
done

echo "Converted pdfs and Moved text files to text folder"
