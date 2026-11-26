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

def bt_dang6_p4_b4_c7_ds8(self):
    # Dạng 6: Cho hàm số y = ax + b. Tìm giao điểm A với Ox, B với Oy và tính diện tích tam giác OAB
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chọn giao điểm A(x_a; 0) và B(0; y_b) nguyên khác 0
        x_a = random.choice([-4, -3, -2, 2, 3, 4])
        y_b = random.choice([-4, -3, -2, 2, 3, 4])
        a_frac = frac(-y_b, x_a)
        b_val = y_b
        
        hs_str = fmt_linear(a_frac, b_val)
        oa = abs(x_a)
        ob = abs(y_b)
        s_oab = frac(oa * ob, 2)
        
        x_min = min(-2, x_a - 1)
        x_max = max(2, x_a + 1)
        y_min = min(-2, y_b - 1)
        y_max = max(2, y_b + 1)
        
        pos_A = 'below' if y_b > 0 else 'above'
        pos_B = 'left' if x_a > 0 else 'right'
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[below] {$x$};\n'
            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (%s,0) -- (0,%s);\n'
            '  \\fill (%s,0) circle (1pt) node[%s] {$A(%s;0)$};\n'
            '  \\fill (0,%s) circle (1pt) node[%s] {$B(0;%s)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (x_min, x_max, y_min, y_max,
               x_a, y_b,
               x_a, pos_A, x_a,
               y_b, pos_B, y_b)
        )
        
        noidungcauhoi = ('''Cho hàm số bậc nhất $y = %s$ có đồ thị là đường thẳng $(d)$.\\
a) Xác định tọa độ các giao điểm $A$, $B$ của $(d)$ lần lượt với trục hoành $Ox$ và trục tung $Oy$.\\
b) Tính diện tích của tam giác $OAB$ (đơn vị đo trên các trục tọa độ là xentimét).'''
                         % hs_str)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tìm tọa độ các giao điểm $A$ và $B$:\\
- Cho $y = 0$ thì $%s = 0 \\Leftrightarrow x = %s$, suy ra tọa độ giao điểm của $(d)$ với trục hoành $Ox$ là $A(%s; 0)$.\\
- Cho $x = 0$ thì $y = %s$, suy ra tọa độ giao điểm của $(d)$ với trục tung $Oy$ là $B(0; %s)$.
\\item Minh họa trên mặt phẳng tọa độ $Oxy$:\\
%s\\
Ta có $OA = |%s| = %s\\text{ (cm)}$ và $OB = |%s| = %s\\text{ (cm)}$.\\
Vì tam giác $OAB$ vuông tại $O$ nên diện tích tam giác $OAB$ là:\\
$S_{\\triangle OAB} = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.
\\end{enumEX}'''
                   % (hs_str, x_a, x_a,
                      b_val, y_b,
                      tikz_code,
                      x_a, oa, y_b, ob,
                      oa, ob, fmt_num(s_oab)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
