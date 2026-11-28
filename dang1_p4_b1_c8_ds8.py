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

def bt_dang1_p4_b1_c8_ds8(self):
    # Dạng 1: Chia hết và Bội chung
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.randint(10, 20)
        b = random.randint(35, 50)
        p, q = random.choice([(3, 5), (4, 6), (3, 4), (4, 5)])
        kq_cothe = list(range(a, b + 1))
        so_kq_cothe = len(kq_cothe)
        kq_thuanloi = [k for k in kq_cothe if (k % p == 0) or (k % q == 0)]
        str_thuanloi = '; '.join(map(str, kq_thuanloi))
        
        noidungcauhoi = ('''Một hộp đựng các quả bóng bàn giống nhau được đánh số liên tiếp từ $%s$ đến $%s$. Lấy ngẫu nhiên một quả bóng trong hộp.\\
a) Hỏi có tất cả bao nhiêu kết quả có thể của hành động trên?\\
b) Liệt kê các kết quả thuận lợi cho biến cố $A$: ``Số ghi trên quả bóng lấy ra chia hết cho $%s$ hoặc chia hết cho $%s$''.'''
                         % (a, b, p, q))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động lấy ngẫu nhiên một quả bóng là các số tự nhiên từ $%s$ đến $%s$.\\
Số kết quả có thể xảy ra là: $%s - %s + 1 = %s$ (kết quả).
\\item Trong các số tự nhiên từ $%s$ đến $%s$, các số chia hết cho $%s$ hoặc chia hết cho $%s$ là: $%s$.\\
Vậy các kết quả thuận lợi cho biến cố $A$ là: $%s$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (a, b, b, a, so_kq_cothe, a, b, p, q, str_thuanloi, str_thuanloi, len(kq_thuanloi)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
