# Speak 

[![Build Status](https://travis-ci.org/jamalsenouci/speak.svg?branch=master)](https://travis-ci.org/jamalsenouci/speak)

A Python package for creating voice notifications

Influenced by Desmba/GoogleSpeech but intended for voice notifications on completion of long running tasks.

##Installation

####From PyPI (with PIP)
1. Ensure vlc is in your path
2. run `pip install git+https://github.com/jamalsenouci/speak.git`

####From source
1. Ensure vlc is in your path
2. Clone this repository: `git clone https://github.com/jamalsenouci/speak`
3. navigate to the root speak directory and run `python setup.py install`

##Usage
####Examples
#####Interactive Usage
`import speak`
`speak.say('Processing has finished')`

#####Command line usage
speak [command]

##Dependencies: 
* [Vlc media player](http://www.videolan.org/vlc/), (vlc executable directory must be in path)
* Internet connection (to access Google text-to-speech api)

##License
[GPLv3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
