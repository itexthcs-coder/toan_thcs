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

def bt_dang11_p4_b4_c7_ds8(self):
    # Dạng 11: Tính độ dài AB và khoảng cách từ O đến đường thẳng (d) cắt Ox tại A, Oy tại B (bộ ba Pythagore)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Bộ ba Pythagore (3,4,5) hoặc (6,8,10)
        scale = random.choice([1, 2])
        oa_len, ob_len, ab_len = 3 * scale, 4 * scale, 5 * scale
        if random.choice([True, False]):
            oa_len, ob_len = ob_len, oa_len
            
        x_a = random.choice([-oa_len, oa_len])
        y_b = random.choice([-ob_len, ob_len])
        a_frac = frac(-y_b, x_a)
        b_val = y_b
        hs_str = fmt_linear(a_frac, b_val)
        oh_frac = frac(oa_len * ob_len, ab_len)
        
        x_min = min(-2, x_a - 1)
        x_max = max(2, x_a + 1)
        y_min = min(-2, y_b - 1)
        y_max = max(2, y_b + 1)
        
        # Chân đường cao H từ O xuống AB
        xh = round((x_a * ob_len**2) / (ab_len**2), 2)
        yh = round((y_b * oa_len**2) / (ab_len**2), 2)
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[below] {$x$};\n'
            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (%s,0) -- (0,%s);\n'
            '  \\draw[line width=1pt, dashed] (0,0) -- (%s,%s);\n'
            '  \\fill (%s,0) circle (1pt) node[below] {$A$};\n'
            '  \\fill (0,%s) circle (1pt) node[left] {$B$};\n'
            '  \\fill (%s,%s) circle (1pt) node[above right] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (x_min, x_max, y_min, y_max,
               x_a, y_b,
               xh, yh,
               x_a, y_b, xh, yh)
        )
        
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho đường thẳng $(d): y = %s$. Gọi $A$ và $B$ lần lượt là giao điểm của $(d)$ với trục $Ox$ và trục $Oy$. Tính độ dài đoạn thẳng $AB$ và khoảng cách từ gốc tọa độ $O$ đến đường thẳng $(d)$ (đơn vị đo trên các trục tọa độ là xentimét).'''
                         % hs_str)
        
        loigiai = ('''- Tìm tọa độ các giao điểm $A$ và $B$:\\
Cho $y = 0$ thì $%s = 0 \\Leftrightarrow x = %s$, suy ra $A(%s; 0)$ và $OA = |%s| = %s\\text{ (cm)}$.\\
Cho $x = 0$ thì $y = %s$, suy ra $B(0; %s)$ và $OB = |%s| = %s\\text{ (cm)}$.\\
%s\\
- Vì tam giác $OAB$ vuông tại $O$ nên áp dụng định lí Pythagore ta có:\\
$AB = \\sqrt{OA^2 + OB^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s\\text{ (cm)}$.\\
- Kẻ $OH \\perp AB$ tại $H$ ($H \\in AB$). Khi đó $OH$ là khoảng cách từ gốc tọa độ $O$ đến đường thẳng $(d)$.\\
Ta có $S_{\\triangle OAB} = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot OH \\cdot AB$.\\
Suy ra: $OH = \\frac{OA \\cdot OB}{AB} = \\frac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.'''
                   % (hs_str, x_a, x_a, x_a, oa_len,
                      b_val, y_b, y_b, ob_len,
                      tikz_code,
                      oa_len, ob_len, oa_len**2 + ob_len**2, ab_len,
                      oa_len, ob_len, ab_len, fmt_num(oh_frac)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
