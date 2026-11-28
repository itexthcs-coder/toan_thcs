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

def bt_dang11_p4_b1_c8_ds8(self):
    # Dạng 11: Rút có hoàn lại (rút liên tiếp 2 lần)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_dau = random.choice([2, 3])
        n_cam = 2
        dau = [f"D_{i}" for i in range(1, n_dau + 1)]
        cam = [f"C_{i}" for i in range(1, n_cam + 1)]
        items = dau + cam
        tong_item = len(items)
        
        pairs = [(x0, y0) for x0 in items for y0 in items]
        tl = [f"({x0}; {y0})" for x0, y0 in pairs if (x0 in dau and y0 in cam) or (x0 in cam and y0 in dau)]
        str_tl = '; '.join(tl)
        
        noidungcauhoi = ('''Một túi đựng $%s$ viên kẹo vị dâu (kí hiệu $%s$) và $%s$ viên kẹo vị cam (kí hiệu $%s$). An lấy ngẫu nhiên $1$ viên kẹo, xem vị rồi bỏ lại vào túi, sau đó tiếp tục lấy ngẫu nhiên $1$ viên kẹo nữa.\\
a) Hỏi có tất cả bao nhiêu kết quả có thể của hành động trên?\\
b) Liệt kê các kết quả thuận lợi cho biến cố $L$: ``Hai lần lấy được hai viên kẹo khác vị nhau''.'''
                         % (n_dau, ', '.join(dau), n_cam, ', '.join(cam)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong túi có tất cả $%s + %s = %s$ viên kẹo. Vì viên kẹo lấy ra lần đầu được bỏ lại vào túi nên lần lấy thứ nhất có $%s$ khả năng và lần lấy thứ hai cũng có $%s$ khả năng.\\
Vậy có tất cả $%s \\cdot %s = %s$ kết quả có thể.
\\item Hai viên kẹo khác vị nhau khi một viên vị dâu và một viên vị cam. Các kết quả thuận lợi cho biến cố $L$ là:\\
$%s$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (n_dau, n_cam, tong_item, tong_item, tong_item, tong_item, tong_item, len(pairs), str_tl, len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
