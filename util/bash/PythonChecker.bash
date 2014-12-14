#!/bin/bash

# Return 'True' if python is satisfied, 'False' otherwise
function checkPython() {
    python2 --version > /dev/null 2>&1
    local ret=$?

    [ $ret -ne 0 ] && { echo False; return 0; }

    ver=$(python2 --version 2>&1 \
        | awk '{ print $2 }' \
        | awk 'BEGIN { FS="."; } { print $1"."$2; }')
    [ $ver = '2.7' ] && { echo True; return 0; }
    echo False
}

# Return 'True' if python-pip is satisfied, 'False' otherwise
function checkPip() {
    python2 -m pip > /dev/null 2>&1
    local ret=$?

    [ $ret -eq 0 ] && { echo True; return 0; }

    echo False
}

# arg 1: the model to check
# arg 2: the version to check, 'ANY' to check any version
# return True if the model is satisfied, False otherwise
# assume that python-pip is installed
function checkPythonModel() {
    local model=$1
    local version=$2
    [ -z "$version" ] && version='ANY'

    local ret=$(python2 -m pip show $model | awk '/Version/{print $2;}')

    if [ $version = 'ANY' ]; then
        [ $ret != '' ] && { echo True; return 0; }
    else
        [ $ret = $version ] && { echo True; return 0; }
    fi
    echo False
}

