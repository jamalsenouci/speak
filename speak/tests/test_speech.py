from nose.tools import *
import unittest
import os
import speak

def is_internet_reachable():
  try:
    # open TCP socket to Google DNS server
    socket.create_connection(("8.8.8.8", 53))
  except OSError as e:
    if e.errno == 101:
      return False
    raise
  return True

class TestSpeech():
    def test_download(self):
      """ Download some reference speeches. """
      speeches = ("Hello", "Bonjour.")
      for lang, speech in zip(("en", "fr"), speeches):
          tempfile = speak._Speech(speech, lang)._download()
          assert(os.path.exists(tempfile))


