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

def bt_dang3_p4_b4_c7_ds8(self):
    # Dạng 3: Tìm hàm số bậc nhất y = ax + b đi qua hai điểm M(x1; y1) và N(x2; y2)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        b_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        x1 = random.choice([-3, -2, -1])
        x2 = random.choice([1, 2, 3])
        y1 = a_val * x1 + b_val
        y2 = a_val * x2 + b_val
        
        hs_str = fmt_linear(a_val, b_val)
        
        noidungcauhoi = ('''Tìm hàm số bậc nhất $y = ax + b$ ($a \\neq 0$), biết rằng đồ thị của hàm số đi qua hai điểm $M(%s; %s)$ và $N(%s; %s)$.'''
                         % (x1, y1, x2, y2))
        
        loigiai = ('''Vì đồ thị hàm số $y = ax + b$ đi qua điểm $M(%s; %s)$ nên thay $x = %s$, $y = %s$ vào công thức hàm số ta được:\\
$a \\cdot (%s) + b = %s \\Leftrightarrow %sa + b = %s \\quad (1)$.\\
Vì đồ thị hàm số $y = ax + b$ đi qua điểm $N(%s; %s)$ nên thay $x = %s$, $y = %s$ vào công thức hàm số ta được:\\
$a \\cdot (%s) + b = %s \\Leftrightarrow %sa + b = %s \\quad (2)$.\\
Lấy $(2)$ trừ $(1)$ theo từng vế, ta được:\\
$(%sa + b) - (%sa + b) = %s - (%s) \\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$ (thỏa mãn $a \\neq 0$).\\
Thay $a = %s$ vào $(2)$, ta có:\\
$%s \\cdot (%s) + b = %s \\Leftrightarrow b = %s - (%s) = %s$.\\
Vậy hàm số bậc nhất cần tìm là $y = %s$.'''
                   % (x1, y1, x1, y1, x1, y1, x1, y1,
                      x2, y2, x2, y2, x2, y2, x2, y2,
                      x2, x1, y2, y1, x2 - x1, y2 - y1, a_val,
                      a_val, x2, a_val, y2, y2, x2 * a_val, b_val,
                      hs_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
