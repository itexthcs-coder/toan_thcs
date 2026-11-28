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

def bt_dang2_p4_b1_c8_ds8(self):
    # Dạng 2: Ước số của một số tự nhiên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        N = random.choice([36, 48, 60, 72, 84, 90])
        uoc = [i for i in range(1, N + 1) if N % i == 0]
        str_uoc = '; '.join(map(str, uoc))
        loai = random.choice(['le', 'chan'])
        if loai == 'le':
            dk_text = "là số lẻ"
            tl = [u for u in uoc if u % 2 == 1]
        else:
            dk_text = "là số chẵn và lớn hơn $10$"
            tl = [u for u in uoc if u % 2 == 0 and u > 10]
        str_tl = '; '.join(map(str, tl))
        
        noidungcauhoi = ('''Trên bàn có đặt các tấm thẻ giống nhau ghi tất cả các ước nguyên dương của số tự nhiên $%s$ (mỗi tấm thẻ ghi một ước khác nhau). Chọn ngẫu nhiên một tấm thẻ trên bàn.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên. Có tất cả bao nhiêu kết quả có thể?\\
b) Xác định các kết quả thuận lợi cho biến cố $B$: ``Số ghi trên tấm thẻ được chọn %s''.'''
                         % (N, dk_text))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tập hợp các ước nguyên dương của $%s$ là $\\{%s\\}$.\\
Do đó, các kết quả có thể của hành động chọn ngẫu nhiên một tấm thẻ là: $%s$.\\
Có tất cả $%s$ kết quả có thể.
\\item Trong các kết quả có thể ở trên, các số %s là: $%s$.\\
Vậy các kết quả thuận lợi cho biến cố $B$ là: $%s$ (gồm $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (N, str_uoc, str_uoc, len(uoc), dk_text, str_tl, str_tl, len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
