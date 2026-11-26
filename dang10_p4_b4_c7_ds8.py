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

def bt_dang10_p4_b4_c7_ds8(self):
    # Dạng 10: Cho hàm số y = (|m| - k)x + m^2 - k^2. Tìm m để là hàm bậc nhất và đi qua gốc tọa độ O(0; 0)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4, 5])
        k2 = k * k
        
        noidungcauhoi = ('''Cho hàm số $y = (|m| - %s)x + m^2 - %s$. Tìm các giá trị của tham số $m$ để hàm số đã cho là hàm số bậc nhất và đồ thị của nó đi qua gốc tọa độ $O(0; 0)$.'''
                         % (k, k2))
        
        loigiai = ('''Để hàm số $y = (|m| - %s)x + m^2 - %s$ là hàm số bậc nhất thì hệ số của $x$ phải khác $0$:\\
$|m| - %s \\neq 0 \\Leftrightarrow |m| \\neq %s \\Leftrightarrow m \\neq %s$ và $m \\neq -%s$.\\
Để đồ thị của hàm số đi qua gốc tọa độ $O(0; 0)$ thì thay $x = 0$, $y = 0$ vào công thức hàm số ta được:\\
$(|m| - %s) \\cdot 0 + m^2 - %s = 0 \\Leftrightarrow m^2 - %s = 0 \\Leftrightarrow m^2 = %s \\Leftrightarrow m = %s$ hoặc $m = -%s$.\\
So sánh với điều kiện $m \\neq %s$ và $m \\neq -%s$, cả hai giá trị $m = %s$ và $m = -%s$ đều bị loại.\\
Vậy không có giá trị nào của tham số $m$ thỏa mãn yêu cầu đề bài.'''
                   % (k, k2,
                      k, k, k, k,
                      k, k2, k2, k2, k, k,
                      k, k, k, k))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
