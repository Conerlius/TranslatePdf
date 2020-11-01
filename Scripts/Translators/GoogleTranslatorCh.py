#!src/bin/python3
# -*- coding: utf-8 -*-

from googletrans import Translator


class Create:
    def __init__(self):
        self._allGoogleList = [
            # 'translate.google.com',
            # 'translate.google.co.kr',
            'translate.google.cn'
        ]
        self.server_index = 0
        self.Name = "translate.google.cn"
        self.Sleep()

    def Translate(self, text):
        result = self.translator.translate(text, dest='zh-CN')
        return result.text
    def Sleep(self):
        self.server_index = self.server_index % len(self._allGoogleList)
        serverr_name = self._allGoogleList[self.server_index]
        print(serverr_name)
        self.translator = Translator(service_urls=[
            serverr_name
        ])
        self.server_index += 1
