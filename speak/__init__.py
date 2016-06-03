#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" text to speech personal assistant using Google API. """

__version__ = "0.9.0"
__author__ = "jamalsenouci"
__license__ = "GPLv3"

_SUPPORTED_LANGUAGES = ("af", "ar", "az", "be", "bg", "bn", "ca", "cs",
                       "cy", "da", "de", "el", "en", "eo", "es", "et",
                       "eu", "fa", "fi", "fr", "ga", "gl", "gu", "hi",
                       "hr", "ht", "hu", "id", "is", "it", "iw", "ja",
                       "ka", "kn", "ko", "la", "lt", "lv", "mk", "ms",
                       "mt", "nl", "no", "pl", "pt", "ro", "ru", "sk",
                       "sl", "sq", "sr", "sv", "sw", "ta", "te", "th",
                       "tl", "tr", "uk", "ur", "vi", "yi", "zh-CN", "zh-TW")

# check deps
import sys
if sys.version_info[:2] >= (3, 3):
    import shutil
    if shutil.which('vlc') is None:
        if shutil.which('vlc.exe') is None:
            raise RuntimeError("vlc binary could not be found")
del sys


__all__=['speak']

class _Speech:

    """ Text segment to be read. """

    def __init__(self, text, lang):
        self.base_url = "http://api.voicerss.org/"
        self.text = text
        self.lang = lang

    def _clean(self):
        """Attempts to remove temp mp3 files. """
        import os
        import tempfile
        filelist = [f for f in os.listdir(tempfile.gettempdir())
                    if f.endswith(".mp3")]
        for file in filelist:
            try:
                os.remove(tempfile.gettempdir()+'\\'+file)
            except:
                pass

    def _download(self):
        """ Download a sound file and returns the file path. """
        import requests
        import tempfile
        params = {}
        params["key"] = "269fbb08fd884dfe9444bbf96bbef639"
        params["hl"] = self.lang
        params["src"] = self.text.lower()
        params["c"] = "MP3"
        temp = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
        req = requests.get(self.base_url, params=params)
        with open(temp.name, "wb") as file:
            file.write(req.content)
        return temp.name


    def play(self, audio):
        """ Play the segment. """
        from speak import vlc as vlc
        inst = vlc.Instance('--qt-start-minimized', '--play-and-exit');
        player = inst.media_player_new();
        media = inst.media_new(audio);
        player.set_media(media);
        player.play();


def speak(text, lang="en-gb"):
    """Converts Text to Speech. """
    speech = _Speech(text, lang)
    speech._clean()
    audio = speech._download()
    speech.play(audio)

#Not yet Implemented
'''
def weather(country='uk', forecast=False):
    """Reads the weather. """
    #Not yet Implemented
    text = get_weather()
    say(text, lang="en")

def news(country='uk', topic='general'):
    """Reads the latest news. """
    text = get_news()
    say(text, lang="en")
'''


def cl_main():
    """Command Line Handler, notifies when command is finished. """
    # parse args
    import argparse
    import subprocess
    import threading
    parser = argparse.ArgumentParser(description="Speak v%s.%s" % (__version__, __doc__))
    parser.add_argument("-l", "--lang", default="en", dest="lang", help="Language")
    parser.add_argument("command", help="command to run")
    args = parser.parse_args()

    # download speech file
    text = args.command +" Process Finished"
    lang = args.lang

    #run command and return speech notification
    def runInThread(Popenargs):
        proc = subprocess.Popen([Popenargs], shell=True)
        proc.wait()
        speech = _Speech(text, lang)
        speech._clean()
        audio = speech._download()
        subprocess.call(['vlc', audio,'--play-and-exit','--qt-start-minimized'])

        return
    thread = threading.Thread(target=runInThread(args.command))
    thread.start()


if __name__ == "__main__":
    cl_main()
