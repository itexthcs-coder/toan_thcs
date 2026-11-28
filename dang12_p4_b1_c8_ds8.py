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

def bt_dang12_p4_b1_c8_ds8(self):
    # Dạng 12: Bốc thăm ghép cặp thi đấu vòng bán kết
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        teams = random.choice([['A', 'B', 'C', 'D'], ['X', 'Y', 'Z', 'T']])
        t1, t2, t3, t4 = teams
        c1 = f"({t1}-{t2} \\text{{ và }} {t3}-{t4})"
        c2 = f"({t1}-{t3} \\text{{ và }} {t2}-{t4})"
        c3 = f"({t1}-{t4} \\text{{ và }} {t2}-{t3})"
        
        noidungcauhoi = ('''Bốn đội bóng $%s, %s, %s, %s$ bốc thăm ngẫu nhiên để chia thành $2$ cặp đấu ở vòng bán kết (không phân biệt thứ tự trận $1$ hay trận $2$).\\
a) Hãy liệt kê tất cả các cách chia cặp đấu có thể xảy ra.\\
b) Xác định các kết quả thuận lợi cho biến cố $M$: ``Hai đội $%s$ và $%s$ không gặp nhau ở vòng bán kết''.'''
                         % (t1, t2, t3, t4, t1, t2))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Chọn một đối thủ bất kì trong $3$ đội còn lại để ghép cặp với đội $%s$, hai đội còn lại tự động tạo thành cặp thứ hai. Vậy có tất cả $3$ cách chia cặp đấu có thể xảy ra là:\\
$%s$; $%s$; $%s$.
\\item Hai đội $%s$ và $%s$ không gặp nhau ở vòng bán kết khi chúng thuộc hai cặp đấu khác nhau.\\
Vậy các kết quả thuận lợi cho biến cố $M$ là: $%s$ và $%s$ (có $2$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (t1, c1, c2, c3, t1, t2, c2, c3))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
