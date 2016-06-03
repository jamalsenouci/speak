#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    brew update
    brew install vlc
    alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'
else
    sudo apt-get update -qq
    sudo apt-get install vlc
    export PATH=$PATH:usr/bin/vlc/
fi
