#!/bin/bash
#this script takes a URL, sends a request to the URL using curl
#then displays the size of the body of the response in bytes

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
