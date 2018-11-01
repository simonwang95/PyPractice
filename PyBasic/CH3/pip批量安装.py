# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:47:26 2018

@author: 10696
"""

import os
libs = {'send2trash','requests','beautifulsoup4','selenium','openpyxl','PyPDF2','python-docx','imapclient','pyzmail','twilio',
        'pillow','pyautogui'}
try:
    for lib in libs:
        os.system('pip install ' + lib)
    print('sucessful')
except:
    print('failes somehow')