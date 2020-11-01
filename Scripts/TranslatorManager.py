#!src/bin/python3
# -*- coding: utf-8 -*-

import re

class Create:
    def SetTranslator(self, translator):
        print('SetTranslator ', translator)
        self._translator = translator

    def SetSourceLanguage(self, source_language):
        print(source_language)

    def SetTargetLanguage(self, target_language):
        print(target_language)

    def Translate(self, text):
        if not bool(re.search('[a-zA-Z]', text)):
            return text
        result = self._translator.Translate(text)
        return result
    def Sleep(self):
        self._translator.Sleep()

Instance = Create()