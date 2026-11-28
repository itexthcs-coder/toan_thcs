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

def bt_dang5_p4_b1_c8_ds8(self):
    # Dạng 5: Phân số tối giản và số thập phân hữu hạn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        N_max = random.choice([12, 15, 16])
        mau = random.choice([12, 15, 18])
        kq_cothe = list(range(1, N_max + 1))
        str_cothe = '; '.join(map(str, kq_cothe))
        
        def is_finite_decimal(num, den):
            g = math.gcd(num, den)
            d = den // g
            while d % 2 == 0:
                d //= 2
            while d % 5 == 0:
                d //= 5
            return d == 1
            
        tl = [n for n in kq_cothe if is_finite_decimal(n, mau)]
        str_tl = '; '.join(map(str, tl))
        
        noidungcauhoi = ('''Viết các số tự nhiên từ $1$ đến $%s$ lên $%s$ mảnh giấy giống nhau (mỗi mảnh giấy ghi một số) rồi bỏ vào hộp. Rút ngẫu nhiên một mảnh giấy có ghi số $n$.\\
a) Liệt kê các kết quả có thể của hành động trên.\\
b) Tìm các kết quả thuận lợi cho biến cố $E$: ``Phân số $\\dfrac{n}{%s}$ viết được dưới dạng số thập phân hữu hạn''.'''
                         % (N_max, N_max, mau))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động rút ngẫu nhiên một mảnh giấy là: $%s$ (có tất cả $%s$ kết quả có thể).
\\item Một phân số tối giản với mẫu dương viết được dưới dạng số thập phân hữu hạn khi và chỉ khi mẫu số không có ước nguyên tố nào khác $2$ và $5$.\\
Kiểm tra lần lượt các giá trị $n \\in \\{1; 2; \\dots; %s\\}$, ta thấy phân số $\\dfrac{n}{%s}$ sau khi rút gọn có mẫu chỉ chứa ước nguyên tố $2$ hoặc $5$ khi $n \\in \\{%s\\}$.\\
Vậy các kết quả thuận lợi cho biến cố $E$ là: $%s$.
\\end{enumEX}'''
                   % (str_cothe, N_max, N_max, mau, str_tl, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
