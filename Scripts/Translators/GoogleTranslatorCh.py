#!src/bin/python3
# -*- coding: utf-8 -*-

from google.cloud import translate_v2 as translate
import six


class Create:
    def __init__(self):
        self.Name = "translate.google.cn"
        self.translate_client = translate.Client()

    def Translate(self, text):
        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")
        result = self.translate_client.translate(text, target_language='zh-CN')
        return result