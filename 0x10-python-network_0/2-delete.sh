#!/bin/bash
# Script that sends a delete req to URL passed as the first argument and display the body of response
curl -sX DELETE "$1"