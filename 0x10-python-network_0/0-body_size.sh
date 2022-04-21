#!/bin/bash
#Script that takes the URL, sends req to URL, display size
curl -s "$1" | wc -c
