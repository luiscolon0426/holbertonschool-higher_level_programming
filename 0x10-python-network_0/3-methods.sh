#!/bin/bash
# Script thaat takes URL and display HTTP methods
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
