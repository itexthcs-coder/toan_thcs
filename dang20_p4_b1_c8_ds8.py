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

def bt_dang20_p4_b1_c8_ds8(self):
    # Dạng 20: Quản lí chi tiêu - Phiếu khuyến mãi mua sắm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_phieu = random.choice([10, 12, 15])
        codes = [f"KM{i:02d}" for i in range(1, n_phieu + 1)]
        b_so = random.choice([3, 4])
        tl = [f"KM{i:02d}" for i in range(1, n_phieu + 1) if (i % b_so == 0) or (i % 2 == 1)]
        
        noidungcauhoi = ('''Nhân dịp khai trương, một siêu thị phát hành $%s$ phiếu giảm giá được đánh mã số lần lượt từ $\\text{KM01}$ đến $\\text{KM%02d}$. Quy định mức giảm giá như sau: các phiếu có số thứ tự chia hết cho $%s$ được giảm $50\\%%$, các phiếu có số thứ tự là số lẻ được giảm $20\\%%$, các phiếu còn lại giảm $10\\%%$ (nếu phiếu thỏa mãn cả hai điều kiện đầu thì áp dụng mức cao nhất là $50\\%%$). Một khách hàng bốc ngẫu nhiên $1$ phiếu từ hộp phiếu.\\
a) Có tất cả bao nhiêu kết quả có thể của hành động trên?\\
b) Liệt kê các kết quả thuận lợi cho biến cố $V$: ``Khách hàng nhận được mức giảm giá từ $20\\%%$ trở lên''.'''
                         % (n_phieu, n_phieu, b_so))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Có $%s$ phiếu giảm giá khác nhau nên khi bốc ngẫu nhiên $1$ phiếu thì có tất cả $%s$ kết quả có thể.
\\item Khách hàng nhận được mức giảm giá từ $20\\%%$ trở lên khi phiếu bốc được có số thứ tự chia hết cho $%s$ hoặc là số lẻ.\\
Trong các số từ $1$ đến $%s$, các số chia hết cho $%s$ hoặc là số lẻ gồm: $%s$.\\
Vậy các kết quả thuận lợi cho biến cố $V$ là: $\\text{%s}$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (n_phieu, n_phieu, b_so, n_phieu, b_so,
                      '; '.join([str(i) for i in range(1, n_phieu + 1) if (i % b_so == 0) or (i % 2 == 1)]),
                      '}$, $\\text{'.join(tl), len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
