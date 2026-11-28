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

def bt_dang10_p4_b1_c8_ds8(self):
    # Dạng 10: Lập số có ba chữ số khác nhau từ các chữ số cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        digits = sorted(random.sample([2, 3, 5, 6, 7, 8], 3))
        d1, d2, d3 = digits
        nums = sorted([100 * a + 10 * b + c for a in digits for b in digits for c in digits if len({a, b, c}) == 3])
        str_nums = '; '.join(map(str, nums))
        
        nguong = d2 * 100
        tl = [n for n in nums if n > nguong and n % 2 == 1]
        if not tl:
            digits = [2, 5, 8]
            d1, d2, d3 = digits
            nums = sorted([100 * a + 10 * b + c for a in digits for b in digits for c in digits if len({a, b, c}) == 3])
            str_nums = '; '.join(map(str, nums))
            nguong = 500
            tl = [n for n in nums if n > nguong and n % 2 == 1]
        str_tl = '; '.join(map(str, tl))
        
        noidungcauhoi = ('''Từ ba tấm thẻ ghi các chữ số $%s, %s, %s$, bạn Minh xếp ngẫu nhiên thành một số tự nhiên có ba chữ số khác nhau.\\
a) Liệt kê tất cả các số tự nhiên có thể tạo thành.\\
b) Xác định các kết quả thuận lợi cho biến cố $K$: ``Số tạo thành lớn hơn $%s$ và không chia hết cho $2$''.'''
                         % (d1, d2, d3, nguong))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Từ ba chữ số $%s, %s, %s$, ta xếp được tất cả $6$ số tự nhiên có ba chữ số khác nhau là: $%s$.
\\item Một số tự nhiên không chia hết cho $2$ khi số đó là số lẻ. Trong các số lập được ở câu a, các số lớn hơn $%s$ và là số lẻ gồm: $%s$.\\
Vậy các kết quả thuận lợi cho biến cố $K$ là: $%s$.
\\end{enumEX}'''
                   % (d1, d2, d3, str_nums, nguong, str_tl, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
