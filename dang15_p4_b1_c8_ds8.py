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

def bt_dang15_p4_b1_c8_ds8(self):
    # Dạng 15: Kiểm định chất lượng sản phẩm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n1 = random.choice([5, 6, 7])
        n2 = 2
        n3 = random.choice([1, 2])
        tong = n1 + n2 + n3
        c1 = [f"A_{i}" for i in range(1, n1 + 1)]
        c2 = [f"B_{i}" for i in range(1, n2 + 1)]
        c3 = [f"L_{i}" for i in range(1, n3 + 1)]
        all_sp = c1 + c2 + c3
        tl = c1 + c2
        
        noidungcauhoi = ('''Một lô hàng linh kiện điện tử có $%s$ sản phẩm, trong đó có $%s$ sản phẩm đạt chuẩn loại I (kí hiệu $%s$), $%s$ sản phẩm đạt chuẩn loại II (kí hiệu $%s$) và $%s$ sản phẩm bị lỗi (kí hiệu $%s$). Nhân viên kiểm tra chất lượng lấy ngẫu nhiên $1$ sản phẩm từ lô hàng.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên.\\
b) Xác định các kết quả thuận lợi cho biến cố $Q$: ``Sản phẩm lấy ra đạt tiêu chuẩn xuất xưởng (không phải sản phẩm bị lỗi)''.'''
                         % (tong, n1, ', '.join(c1), n2, ', '.join(c2), n3, ', '.join(c3)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động lấy ngẫu nhiên $1$ sản phẩm là:\\
$%s$ (có tất cả $%s$ kết quả có thể).
\\item Sản phẩm đạt tiêu chuẩn xuất xưởng gồm các sản phẩm loại I và loại II.\\
Do đó, các kết quả thuận lợi cho biến cố $Q$ là: $%s$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % ('; '.join(all_sp), tong, '; '.join(tl), len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
