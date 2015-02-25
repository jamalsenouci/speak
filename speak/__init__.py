#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" text to speech personal assistant using Google API. """

__version__ = "0.1.0"
__author__ = "jamalsenouci"
__license__ = "GPLv3"

import argparse
import os
import subprocess
import requests
import tempfile
import threading

import bin_dep
import vlc


SUPPORTED_LANGUAGES = ("af", "ar", "az", "be", "bg", "bn", "ca", "cs",
                       "cy", "da", "de", "el", "en", "eo", "es", "et",
                       "eu", "fa", "fi", "fr", "ga", "gl", "gu", "hi",
                       "hr", "ht", "hu", "id", "is", "it", "iw", "ja",
                       "ka", "kn", "ko", "la", "lt", "lv", "mk", "ms",
                       "mt", "nl", "no", "pl", "pt", "ro", "ru", "sk",
                       "sl", "sq", "sr", "sv", "sw", "ta", "te", "th",
                       "tl", "tr", "uk", "ur", "vi", "yi", "zh-CN", "zh-TW")


class Speech:

    """ Text segment to be read. """

    def __init__(self, text, lang):
        self.base_url = "http://translate.google.com/translate_tts"
        self.text = text
        self.lang = lang
        self.play()

    def _clean(self):
        """Attempts to remove temp mp3 files. """
        filelist = [f for f in os.listdir(tempfile.gettempdir())
                    if f.endswith(".mp3")]
        for file in filelist:
            try:
                os.remove(tempfile.gettempdir()+'\\'+file)
            except:
                pass

    def play(self):
        """ Play the segment. """
        self._clean()
        audio = self._download()
        inst = vlc.Instance('--qt-start-minimized', '--play-and-exit')
        player = inst.media_player_new()
        media = inst.media_new(audio)
        player.set_media(media)
        player.play()


    def _download(self):
        """ Download a sound file and returns the file path. """
        params = {}
        params["ie"] = "UTF-8"
        params["textlen"] = str(len(self.text))
        params["tl"] = self.lang
        params["q"] = self.text.lower()
        temp = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
        req = requests.get(self.base_url, params=params)
        with open(temp.name, "wb") as file:
            file.write(req.content)
        return temp.name


def speak(text, lang="en"):
    """Converts Text to Speech. """
    Speech(text, lang)

def weather(country='uk', forecast=False):
    """Reads the weather. """
    #Not yet Implemented
    text = get_weather()
    Speech(text, lang="en")

def news(country='uk'):
    """Reads the news. """
    #Not yet Implemented
    text = get_news()
    Speech(text, lang="en")


def cl_main():
    """Command Line Handler, notifies when command is finished. """
    # parse args
    parser = argparse.ArgumentParser(description="Speak v%s.%s" % (__version__, __doc__))
    parser.add_argument("-l", "--lang", default="en", dest="lang", help="Language")
    parser.add_argument("command", help="command to run")
    args = parser.parse_args()

    # download speech file
    text = args.command +" Process Finished"
    lang = args.lang
    #speech = Speech(text, lang)
    #speech._clean()
    #audio = speech._download()

    #run command and return speech notification
    def runInThread(Popenargs):
        proc = subprocess.Popen([Popenargs], shell=True)
        proc.wait()
        #run the speech function
        return
    thread = threading.Thread(target=runInThread(args.command))
    thread.start()


# check deps
bin_dep.check_bin_dependency(("vlc",))


if __name__ == "__main__":
    cl_main()
