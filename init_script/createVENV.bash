#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath $0))
source "$SCRIPT_PATH/../util/bash/PythonChecker.bash"

if [ $(checkPython) = 'True' ]; then
    echo "Python 2.7 is installed."
else
    echo "Python 2.7 is not installed. Maybe you should do"\
        "'bash installDepencies.bash' first"
    return 0
fi

if [ $(checkPip) = 'True' ]; then
    echo "Python 2.7 pip is installed."
else
    echo "Python 2.7 pip is not installed. Maybe you should do"\
        "'bash installDepencies.bash' first"
    return 0
fi

if [ $(checkPythonModel virtualenv) = 'True' ]; then
    echo "Python 2.7 virtualenv is installed."
else
    echo "Trying to install virtualenv."
    python2 -m pip install virtualenv
    ret=$?
    [ $ret -ne 0 ] && {
        echo "virtual env install failed. Abort!"
        unset ret
        return 1
    }
    unset ret
fi

# arg 1: the path to install virtualenv
function installVirtualEnv() {
    venvPath=$1
    if [ -f $venvPath/bin/python ]; then
        echo "Virtual Env is installed already!"
        echo "if you hope to reinstall it, remove '$venvPath/bin/', "\
            "'$venvPath/include/', '$venvPath/lib/', "\
            "'$venvPath/local/' manually."
        return 0
    fi

    python2 -m virtualenv $venvPath
}
installVirtualEnv ../backend/venv/

