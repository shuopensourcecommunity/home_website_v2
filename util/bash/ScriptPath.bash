#!/bin/bash

# Well, this function is for reference only, when you need script path,
# just copy it
function ScriptPath() {
    $(cd "$(dirname "$0")"; echo pwd)
}

