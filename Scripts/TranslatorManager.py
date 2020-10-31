#!src/bin/python3
# -*- coding: utf-8 -*-

class Create:
    def SetTranslator(self, translator):
        print('SetTranslator ', translator)
        self._translator = translator

    def SetSourceLanguage(self, source_language):
        print(source_language)

    def SetTargetLanguage(self, target_language):
        print(target_language)

    def Translate(self, text):
        return self._translator.Translate(text)

Instance = Create()