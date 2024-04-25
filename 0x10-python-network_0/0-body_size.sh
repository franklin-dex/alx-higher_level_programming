#!/bin/bash
#this script takes URL, send request using curl, display the size of body of response in byte
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
