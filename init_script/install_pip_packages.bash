#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath $0))
source "$SCRIPT_PATH/../util/bash/PythonChecker.bash"

venvPath="$SCRIPT_PATH/../backend/venv/"
requirementFile="$SCRIPT_PATH/pkg-config/backend_python_requirements.txt"

function checkVirtualEnv() {
    if [ ! -f $venvPath/bin/python ]; then
        echo "Virtual Env is not installed. Maybe you should do"\
            "'bash createVENV.bash' first"
        return 1
    fi
}
checkVirtualEnv $venvPath
[ $? -ne 0 ] && exit 1

function installRequirements() (
    source $venvPath/bin/activate
    pip install -r $requirementFile
)
installRequirements

