#!/bin/bash
#this script takes in a url, send a GET request using curl, displays the body if the status code is 200
curl -sL "$1" -o /tmp/body.txt && grep -F 200 /tmp/body.txt > /dev/null && cat /tmp/body.txt
