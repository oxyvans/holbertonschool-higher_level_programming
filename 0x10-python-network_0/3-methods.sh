#!/bin/bash
#task 3
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
