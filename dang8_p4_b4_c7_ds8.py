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

def bt_dang8_p4_b4_c7_ds8(self):
    # Dạng 8: Cho ba điểm A(x1; y1), B(x2; y2) và C(m + p; k*m + q). Tìm m để A, B, C thẳng hàng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([-3, -2, 2, 3])
        b_val = random.choice([-3, -2, -1, 1, 2, 3])
        x1 = random.choice([-2, -1])
        x2 = random.choice([1, 2])
        y1 = a_val * x1 + b_val
        y2 = a_val * x2 + b_val
        
        m_ans = random.choice([-2, -1, 1, 2, 3])
        p = random.choice([-2, -1, 1, 2])
        k = -a_val if a_val != 1 else 2
        xc_val = m_ans + p
        yc_val = a_val * xc_val + b_val
        q = yc_val - k * m_ans
        
        xc_str = fmt_linear(1, p, 'm')
        yc_str = fmt_linear(k, q, 'm')
        hs_str = fmt_linear(a_val, b_val)
        
        noidungcauhoi = ('''Cho ba điểm $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$. Tìm giá trị của $m$ để ba điểm $A$, $B$, $C$ thẳng hàng.'''
                         % (x1, y1, x2, y2, xc_str, yc_str))
        
        loigiai = ('''Vì $x_A = %s \\neq x_B = %s$ nên đường thẳng $AB$ là đồ thị của hàm số bậc nhất có dạng $y = ax + b$ ($a \\neq 0$).\\
Vì đường thẳng $AB$ đi qua $A(%s; %s)$ và $B(%s; %s)$ nên ta có:\\
$\\begin{cases} a \\cdot (%s) + b = %s \\ a \\cdot (%s) + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\ b = %s \\end{cases}$.\\
Suy ra phương trình đường thẳng $AB$ là $y = %s$.\\
Để ba điểm $A$, $B$, $C$ thẳng hàng thì điểm $C(%s; %s)$ phải thuộc đường thẳng $AB$.\\
Thay $x = %s$ và $y = %s$ vào phương trình đường thẳng $AB$, ta được:\\
$%s = %s(%s) + (%s) \\Leftrightarrow %s = %s \\Leftrightarrow %sm = %s \\Leftrightarrow m = %s$.\\
Vậy $m = %s$ thì ba điểm $A$, $B$, $C$ thẳng hàng.'''
                   % (x1, x2,
                      x1, y1, x2, y2,
                      x1, y1, x2, y2, a_val, b_val,
                      hs_str,
                      xc_str, yc_str,
                      xc_str, yc_str,
                      yc_str, a_val, xc_str, b_val,
                      yc_str, fmt_linear(a_val, a_val * p + b_val, 'm'),
                      k - a_val, a_val * p + b_val - q, m_ans,
                      m_ans))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
