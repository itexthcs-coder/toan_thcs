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

def bt_dang5_p4_b4_c7_ds8(self):
    # Dạng 5: Vẽ đồ thị hai hàm số y = a1*x + b1 và y = a2*x + b2 và tìm giao điểm I
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([1, 2])
        a2 = random.choice([-1, -2])
        x_i = random.choice([1, 2, 3])
        y_i = random.choice([1, 2, 3])
        b1 = y_i - a1 * x_i
        b2 = y_i - a2 * x_i
        
        hs1 = fmt_linear(a1, b1)
        hs2 = fmt_linear(a2, b2)
        
        # Điểm phụ cho mỗi đường thẳng
        x1_aux = 0 if b1 != 0 else 1
        y1_aux = a1 * x1_aux + b1
        x2_aux = 0 if b2 != 0 else 1
        y2_aux = a2 * x2_aux + b2
        
        x_min, x_max = -2, 5
        y_min, y_max = -3, 5
        
        def clip_line(a, b):
            pts = []
            for xv in [x_min, x_max]:
                yv = a * xv + b
                if y_min <= yv <= y_max:
                    pts.append((xv, yv))
            for yv in [y_min, y_max]:
                xv = (yv - b) / a
                if x_min <= xv <= x_max:
                    pts.append((round(xv, 2), yv))
            pts = sorted(list(set(pts)))
            return pts[0], pts[-1]
            
        p1a, p1b = clip_line(a1, b1)
        p2a, p2b = clip_line(a2, b2)
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[below] {$x$};\n'
            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (%s,%s) -- (%s,%s);\n'
            '  \\draw[line width=1pt] (%s,%s) -- (%s,%s);\n'
            '  \\draw[line width=1pt, dashed] (%s,0) -- (%s,%s) -- (0,%s);\n'
            '  \\fill (%s,%s) circle (1pt) node[above] {$I(%s;%s)$};\n'
            '  \\fill (%s,0) circle (1pt) node[below] {$%s$};\n'
            '  \\fill (0,%s) circle (1pt) node[left] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (x_min, x_max, y_min, y_max,
               p1a[0], p1a[1], p1b[0], p1b[1],
               p2a[0], p2a[1], p2b[0], p2b[1],
               x_i, x_i, y_i, y_i,
               x_i, y_i, x_i, y_i,
               x_i, x_i, y_i, y_i)
        )
        
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, vẽ đồ thị của hai hàm số $y = %s$ và $y = %s$ trên cùng một hệ trục tọa độ. Tìm tọa độ giao điểm $I$ của hai đường thẳng đó bằng phép tính.'''
                         % (hs1, hs2))
        
        loigiai = ('''- Vẽ đồ thị hàm số $y = %s$:\\
Cho $x = %s$ thì $y = %s$, ta được điểm $A(%s; %s)$.\\
Cho $x = %s$ thì $y = %s$, ta được điểm $I(%s; %s)$.\\
Đồ thị hàm số $y = %s$ là đường thẳng đi qua hai điểm $A(%s; %s)$ và $I(%s; %s)$.\\
- Vẽ đồ thị hàm số $y = %s$:\\
Cho $x = %s$ thì $y = %s$, ta được điểm $B(%s; %s)$.\\
Cho $x = %s$ thì $y = %s$, ta được điểm $I(%s; %s)$.\\
Đồ thị hàm số $y = %s$ là đường thẳng đi qua hai điểm $B(%s; %s)$ và $I(%s; %s)$.\\
%s\\
- Tìm tọa độ giao điểm $I$ bằng phép tính:\\
Hoành độ giao điểm $I$ của hai đường thẳng là nghiệm của phương trình:\\
$%s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$.\\
Thay $x = %s$ vào hàm số $y = %s$, ta được $y = %s \\cdot %s + (%s) = %s$.\\
Vậy tọa độ giao điểm của hai đường thẳng là $I(%s; %s)$.'''
                   % (hs1, x1_aux, y1_aux, x1_aux, y1_aux, x_i, y_i, x_i, y_i, hs1, x1_aux, y1_aux, x_i, y_i,
                      hs2, x2_aux, y2_aux, x2_aux, y2_aux, x_i, y_i, x_i, y_i, hs2, x2_aux, y2_aux, x_i, y_i,
                      tikz_code,
                      hs1, hs2, a1 - a2, b2 - b1, x_i,
                      x_i, hs1, a1, x_i, b1, y_i,
                      x_i, y_i))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
