# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from decimal import Decimal, ROUND_HALF_UP

def bt_dang16_p4_b1_c8_ds8(self):
    # Dạng 16: Lịch sử - Địa lí Việt Nam
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        places = ["Hà Nội", "Hải Phòng", "Đà Nẵng", "Huế", "Cần Thơ", "TP. Hồ Chí Minh", "Quảng Ninh", "Nghệ An"]
        loai = random.choice(['trung_nam', 'bac'])
        if loai == 'trung_nam':
            dk_text = "Địa danh được chọn là thành phố trực thuộc Trung ương và nằm ở khu vực miền Trung hoặc miền Nam"
            tl = ["Đà Nẵng", "Huế", "Cần Thơ", "TP. Hồ Chí Minh"]
            giai_thich = "Trong danh sách trên, các thành phố trực thuộc Trung ương gồm: Hà Nội, Hải Phòng, Đà Nẵng, Huế, Cần Thơ, TP. Hồ Chí Minh (Quảng Ninh và Nghệ An là tỉnh). Trong đó, các thành phố thuộc miền Trung hoặc miền Nam là: Đà Nẵng, Huế, Cần Thơ, TP. Hồ Chí Minh."
        else:
            dk_text = "Địa danh được chọn là thành phố trực thuộc Trung ương và nằm ở khu vực miền Bắc"
            tl = ["Hà Nội", "Hải Phòng"]
            giai_thich = "Trong danh sách trên, các thành phố trực thuộc Trung ương nằm ở miền Bắc là Hà Nội và Hải Phòng (Quảng Ninh là tỉnh)."
            
        noidungcauhoi = ('''Trong một trò chơi đố vui Địa lí, ban tổ chức chuẩn bị $8$ tấm thẻ giống nhau, mỗi tấm thẻ ghi tên một địa danh trong danh sách sau: \\textit{%s}. Người chơi rút ngẫu nhiên một tấm thẻ.\\
a) Có tất cả bao nhiêu kết quả có thể của hành động trên?\\
b) Liệt kê các kết quả thuận lợi cho biến cố $R$: ``%s''.'''
                         % (', '.join(places), dk_text))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Có $8$ tấm thẻ ghi $8$ địa danh khác nhau nên khi rút ngẫu nhiên một tấm thẻ thì có tất cả $8$ kết quả có thể.
\\item %s\\
Vậy các kết quả thuận lợi cho biến cố $R$ là: %s (có $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (giai_thich, ', '.join(tl), len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
