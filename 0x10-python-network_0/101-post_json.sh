#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <file>"
    exit 1
fi

# Assign arguments to variables
url=$1
file=$2

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "Error: File '$file' not found."
    exit 1
fi

# Send POST request with file contents in the body using curl
curl -X POST -H "Content-Type: application/json" -d "@$file" "$url"

