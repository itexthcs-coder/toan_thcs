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

def bt_dang7_p4_b4_c7_ds8(self):
    # Dạng 7: Tìm m (m != 0) để đồ thị hàm số y = mx + b tạo với hai trục tọa độ tam giác có diện tích S
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b_val = random.choice([2, 4, 6])
        m_abs = random.choice([1, 2, 3])
        # S = b^2 / (2 * |m|)
        s_val = frac(b_val * b_val, 2 * m_abs)
        
        noidungcauhoi = ('''Tìm giá trị của tham số $m$ ($m \\neq 0$) để đồ thị của hàm số bậc nhất $y = mx + %s$ tạo với hai trục tọa độ $Ox$, $Oy$ một tam giác vuông có diện tích bằng $%s$ (đơn vị diện tích).'''
                         % (b_val, fmt_num(s_val)))
        
        loigiai = ('''Gọi $A$ và $B$ lần lượt là giao điểm của đồ thị hàm số $y = mx + %s$ ($m \\neq 0$) với trục hoành $Ox$ và trục tung $Oy$.\\
- Cho $x = 0$ thì $y = %s$, suy ra $B(0; %s)$ và độ dài $OB = |%s| = %s$.\\
- Cho $y = 0$ thì $mx + %s = 0 \\Leftrightarrow x = -\\frac{%s}{m}$, suy ra $A\\left(-\\frac{%s}{m}; 0\\right)$ và độ dài $OA = \\left|-\\frac{%s}{m}\\right| = \\frac{%s}{|m|}$.\\
Vì tam giác $OAB$ vuông tại $O$ nên diện tích tam giác $OAB$ là:\\
$S_{\\triangle OAB} = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot \\frac{%s}{|m|} \\cdot %s = \\frac{%s}{|m|}$.\\
Theo đề bài, $S_{\\triangle OAB} = %s$ nên ta có:\\
$\\frac{%s}{|m|} = %s \\Leftrightarrow |m| = %s \\Leftrightarrow m = %s$ hoặc $m = -%s$ (thỏa mãn $m \\neq 0$).\\
Vậy $m \\in \{%s; -%s\}$ là các giá trị cần tìm.'''
                   % (b_val,
                      b_val, b_val, b_val, b_val,
                      b_val, b_val, b_val, b_val, b_val,
                      b_val, b_val, frac(b_val * b_val, 2),
                      fmt_num(s_val),
                      frac(b_val * b_val, 2), fmt_num(s_val), m_abs, m_abs, m_abs,
                      m_abs, m_abs))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
