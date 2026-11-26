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
from sympy import symbols, sqrt, evaluate, Subs, latex, Rational
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

def fmt_num(val):
    if isinstance(val, frac):
        if val.denominator == 1:
            return str(val.numerator)
        if val.numerator < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dec(val, places='0.1'):
    d = Decimal(str(val)).quantize(Decimal(places), rounding=ROUND_HALF_UP)
    s = format(d, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')

def fmt_linear(a, b, var='x'):
    # Định dạng ax + b với a, b là int hoặc frac
    if a == 1:
        sa = var
    elif a == -1:
        sa = '-' + var
    else:
        sa = '%s%s' % (fmt_num(a), var)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_num(b))
    else:
        return '%s - %s' % (sa, fmt_num(abs(b)))

def bt_dang9_p4_b4_c7_ds8(self):
    # Dạng 9: Khi tăng x thêm dx đơn vị thì y tăng/giảm dy đơn vị, và tại x0 thì y = y0. Tìm a, b
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        dx = random.choice([2, 3, 4])
        a_val = random.choice([-4, -3, -2, 2, 3, 4])
        dy = a_val * dx
        x0 = random.choice([-2, -1, 1, 2])
        b_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        y0 = a_val * x0 + b_val
        
        tang_giam = 'tăng thêm' if dy > 0 else 'giảm đi'
        abs_dy = abs(dy)
        
        noidungcauhoi = ('''Cho hàm số bậc nhất $y = ax + b$ ($a \\neq 0$). Biết rằng khi tăng giá trị của biến $x$ thêm $%s$ đơn vị thì giá trị tương ứng của $y$ %s $%s$ đơn vị, và khi $x = %s$ thì $y = %s$. Hãy xác định các hệ số $a$, $b$ của hàm số.'''
                         % (dx, tang_giam, abs_dy, x0, y0))
        
        loigiai = ('''Gọi $y_1 = ax_1 + b$ là giá trị của hàm số tại $x = x_1$.\\
Khi tăng giá trị của biến $x$ thêm $%s$ đơn vị, tức là $x_2 = x_1 + %s$, thì giá trị tương ứng của hàm số là:\\
$y_2 = a(x_1 + %s) + b = (ax_1 + b) + %sa = y_1 + %sa$.\\
Theo giả thiết, khi tăng $x$ thêm $%s$ đơn vị thì $y$ %s $%s$ đơn vị, nghĩa là $y_2 - y_1 = %s$.\\
Do đó: $%sa = %s \\Leftrightarrow a = %s$ (thỏa mãn $a \\neq 0$).\\
Lại có khi $x = %s$ thì $y = %s$, thay vào công thức hàm số $y = %sx + b$ ta được:\\
$%s \\cdot (%s) + b = %s \\Leftrightarrow %s + b = %s \\Leftrightarrow b = %s$.\\
Vậy các hệ số cần tìm là $a = %s$ và $b = %s$.'''
                   % (dx, dx,
                      dx, dx, dx,
                      dx, tang_giam, abs_dy, dy,
                      dx, dy, a_val,
                      x0, y0, a_val,
                      a_val, x0, y0, a_val * x0, y0, b_val,
                      a_val, b_val))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
