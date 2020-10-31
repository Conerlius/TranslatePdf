#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Scripts.UIFactory as UIFactory
import Scripts.PdfManager as PdfManager
import Scripts.TranslatorManager as TranslatorManager
import Scripts.TranslatorList as TranslatorList
import Scripts.SourceLanguage as SourceLanguage
import Scripts.TargetLanguage as TargetLanguage

class Create(UIFactory.TranslatePdf):
    def __init__(self, parent):
        UIFactory.TranslatePdf.__init__(self, parent)

    def OnActive( self, event ):
        try:
            self.Validate()
        except:
            return
        source_langs = []
        for index in range(len(SourceLanguage.All)):
            source_langs.append(SourceLanguage.All[index])
        self.source_Lan_Select.SetItems(source_langs)
        self.source_Lan_Select.SetSelection(0)

        target_langs = []
        for index in range(len(TargetLanguage.All)):
            target_langs.append(TargetLanguage.All[index])
        self.target_Lan_Select.SetItems(target_langs)
        self.target_Lan_Select.SetSelection(0)

        translator_list = []
        for index in range(len(TranslatorList.All)):
            translator_list.append(TranslatorList.All[index].Name)
        self.translator_select.SetItems(translator_list)
        self.translator_select.SetSelection(0)


    def ClickTranslate(self, event):
        print('translate')
        source_path = self.source_path_picker.GetPath()
        source_lan_index = self.source_Lan_Select.GetCurrentSelection()
        target_lan_index = self.target_Lan_Select.GetCurrentSelection()
        translator_index = self.translator_select.GetCurrentSelection()
        output_path = self.ouput_dir.GetPath()
        print(source_lan_index, source_path, translator_index, target_lan_index, output_path)
        TranslatorManager.Instance.SetTranslator(TranslatorList.All[translator_index])
        TranslatorManager.Instance.SetSourceLanguage(SourceLanguage.All[source_lan_index])
        TranslatorManager.Instance.SetTargetLanguage(TargetLanguage.All[source_lan_index])
        msg = PdfManager.Instance.Load(source_path)
        if msg != None:
            print(msg)
            return
