#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams,LTTextBoxHorizontal,LTImage,LTCurve,LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFDocument
from PyPDF2 import PdfFileWriter, PdfFileReader

import os
import time
import Scripts.TranslatorManager as TranslatorManager

class PdfManager:
    def Load(self, file_path):
        print("load pdf ", file_path)
        translator = TranslatorManager.Instance
        reader = open(file_path, 'rb')
        # parser = PDFParser(reader)
        rsrcmgr = PDFResourceManager(caching=False)
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0
        pauseCount = 0
        for page in PDFPage.get_pages(reader, pagenos=set(), maxpages=0, password='', caching=True, check_extractable=True):
            num_page += 1  # 页面增一
            interpreter.process_page(page)
            layout = device.get_result()
            fileNames = os.path.splitext(file_path)
            for x in layout:
                if hasattr(x, "get_text") or isinstance(x, LTTextBoxHorizontal):
                    with open(fileNames[0] + '.txt', mode='a+', encoding='utf-8') as f:
                        results = x.get_text().replace(u'\xa0', u' ')
                        ress = translator.Translate(results)
                        f.write(ress + '\n')
                # 如果x是水平文本对象的话
                if isinstance(x, LTTextBoxHorizontal):
                    num_TextBoxHorizontal += 1  # 水平文本框对象增一
                if isinstance(x, LTImage):  # 图片对象
                    num_image += 1
                if isinstance(x, LTCurve):  # 曲线对象
                    num_curve += 1
                if isinstance(x, LTFigure):  # figure对象
                    num_figure += 1
                if num_TextBoxHorizontal % 330 == 0 and num_TextBoxHorizontal != 0:
                    print('休息一会，防止google的检查')
                    # pauseCount = pauseCount + 1
                    translator.Sleep()
                    time.sleep(20)

            print('对象数量：%s,页面数：%s,图片数：%s,曲线数：%s,'
                  '水平文本框：%s,' % (num_figure, num_page, num_image, num_curve, num_TextBoxHorizontal))

        a = PDFDocument()
        a.


Instance = PdfManager()