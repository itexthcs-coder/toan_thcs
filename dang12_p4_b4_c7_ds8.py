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

def bt_dang12_p4_b4_c7_ds8(self):
    # Dạng 12: Tìm m để đồ thị hàm số y = (m - p)x + k*m + q cắt Ox, Oy tạo tam giác OPQ vuông cân
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([2, 3, 4])
        # Trường hợp 1: m - p = 1 => m = p + 1
        # Trường hợp 2: m - p = -1 => m = p - 1
        m1 = p + 1
        m2 = p - 1
        k = random.choice([2, 3])
        # Chọn q sao cho k*m1 + q != 0 và k*m2 + q != 0
        q = random.choice([1, 2, 4, 5])
        
        b1 = k * m1 + q
        b2 = k * m2 + q
        
        noidungcauhoi = ('''Cho hàm số bậc nhất $y = (m - %s)x + %sm + %s$ ($m \\neq %s$). Tìm $m$ để đồ thị hàm số cắt trục tung tại điểm $P$ và cắt trục hoành tại điểm $Q$ sao cho tam giác $OPQ$ là tam giác vuông cân.'''
                         % (p, k, q, p))
        
        loigiai = ('''Để đồ thị hàm số cắt hai trục tọa độ tạo thành tam giác $OPQ$ thì đồ thị không đi qua gốc tọa độ $O$, tức là hệ số tự do khác $0$:\\
$%sm + %s \\neq 0 \\Leftrightarrow m \\neq -\\frac{%s}{%s}$.\\
- Cho $x = 0$ thì $y = %sm + %s$, suy ra $P(0; %sm + %s)$ và $OP = |%sm + %s|$.\\
- Cho $y = 0$ thì $(m - %s)x + %sm + %s = 0 \\Leftrightarrow x = -\\frac{%sm + %s}{m - %s}$, suy ra $Q\\left(-\\frac{%sm + %s}{m - %s}; 0\\right)$ và $OQ = \\frac{|%sm + %s|}{|m - %s|}$.\\
Vì tam giác $OPQ$ vuông tại $O$ nên để tam giác $OPQ$ vuông cân thì $OP = OQ$:\\
$|%sm + %s| = \\frac{|%sm + %s|}{|m - %s|} \\Leftrightarrow |m - %s| = 1$ (do $|%sm + %s| > 0$).\\
Suy ra $m - %s = 1$ hoặc $m - %s = -1$, tức là $m = %s$ hoặc $m = %s$.\\
Cả hai giá trị này đều thỏa mãn $m \\neq %s$ và $m \\neq -\\frac{%s}{%s}$.\\
Vậy $m \\in \{%s; %s\}$ là các giá trị cần tìm.'''
                   % (k, q, q, k,
                      k, q, k, q, k, q,
                      p, k, q, k, q, p, k, q, p, k, q, p,
                      k, q, k, q, p, p, k, q,
                      p, p, m1, m2,
                      p, q, k,
                      m1, m2))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
