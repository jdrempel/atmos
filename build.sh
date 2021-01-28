#!/bin/bash

if [ $# -ge 1 ]
then
    docker build --target $1 -t $1 .
else
    echo "Builds an ATMOS Docker image to a specific target (use atmos.sh to run it)."
    echo "Usage:"
    echo "        build.sh <target>"
    echo ""
    echo "Targets can be one of:"
    echo "  local_dev   (for doing development on local machine)"
    echo "  tests       (for running pytest)"
    echo "  atmos       (for running the current build)"
    echo ""
fi