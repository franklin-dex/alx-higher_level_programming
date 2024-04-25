#!/bin/bash
#this script takes in a url, send a GET request using curl, displays the body if status code is 200
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1; curl -sL "$1" -o /tmp/body.txt; grep -q "200 OK" /tmp/body.txt && cat /tmp/body.txt; rm -f /tmp/body.txt
