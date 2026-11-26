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

def bt_dang13_p4_b4_c7_ds8(self):
    # Dạng 13: Hai đường thẳng (d1), (d2) cắt nhau tại C và cắt Ox tại A, B. Tính diện tích và chu vi tam giác ABC
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chọn tam giác cân hoặc vuông đẹp với đỉnh C(xc; yc) trên Ox (yc > 0)
        # Ví dụ A(xc - h; 0), B(xc + h; 0), C(xc; h) -> tam giác vuông cân tại C!
        xc = random.choice([0, 1, 2])
        h = random.choice([2, 3, 4])
        xa = xc - h
        xb = xc + h
        yc = h
        
        # (d1) qua A(xa; 0) và C(xc; yc): hệ số góc a1 = 1, b1 = -xa
        a1 = 1
        b1 = -xa
        # (d2) qua B(xb; 0) và C(xc; yc): hệ số góc a2 = -1, b2 = xb
        a2 = -1
        b2 = xb
        
        hs1 = fmt_linear(a1, b1)
        hs2 = fmt_linear(a2, b2)
        
        ab_len = 2 * h
        s_abc = h * h
        
        x_min = xa - 1
        x_max = xb + 1
        y_min = -1
        y_max = yc + 2
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[below] {$x$};\n'
            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (%s,0) -- (%s,%s);\n'
            '  \\draw[line width=1pt] (%s,0) -- (%s,%s);\n'
            '  \\draw[line width=1pt, dashed] (%s,0) -- (%s,%s);\n'
            '  \\fill (%s,0) circle (1pt) node[below] {$A(%s;0)$};\n'
            '  \\fill (%s,0) circle (1pt) node[below] {$B(%s;0)$};\n'
            '  \\fill (%s,%s) circle (1pt) node[above] {$C(%s;%s)$};\n'
            '  \\fill (%s,0) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (x_min, x_max, y_min, y_max,
               xa, xc, yc,
               xb, xc, yc,
               xc, xc, yc,
               xa, xa, xb, xb, xc, yc, xc, yc, xc)
        )
        
        noidungcauhoi = ('''Cho hai hàm số bậc nhất $y = %s$ có đồ thị $(d_1)$ và $y = %s$ có đồ thị $(d_2)$. Gọi $C$ là giao điểm của $(d_1)$ và $(d_2)$; $A$ và $B$ lần lượt là giao điểm của $(d_1)$ và $(d_2)$ với trục hoành $Ox$. Tính chu vi và diện tích của tam giác $ABC$ (đơn vị đo trên các trục tọa độ là xentimét).'''
                         % (hs1, hs2))
        
        loigiai = ('''- Tìm tọa độ các điểm $A$, $B$, $C$:\\
+ Giao điểm $A$ của $(d_1)$ với $Ox$: cho $y = 0 \\Rightarrow %s = 0 \\Leftrightarrow x = %s$, suy ra $A(%s; 0)$.\\
+ Giao điểm $B$ của $(d_2)$ với $Ox$: cho $y = 0 \\Rightarrow %s = 0 \\Leftrightarrow x = %s$, suy ra $B(%s; 0)$.\\
+ Hoành độ giao điểm $C$ của $(d_1)$ và $(d_2)$ là nghiệm phương trình:\\
$%s = %s \\Leftrightarrow 2x = %s \\Leftrightarrow x = %s$.\\
Thay $x = %s$ vào $(d_1)$ ta được $y = %s + (%s) = %s$, suy ra $C(%s; %s)$.\\
%s\\
- Tính độ dài các cạnh và diện tích tam giác $ABC$:\\
Kẻ $CH \\perp Ox$ tại $H(%s; 0)$, ta có $CH = |%s| = %s\\text{ (cm)}$, $AB = |%s - (%s)| = %s\\text{ (cm)}$.\\
Ta có $AH = |%s - (%s)| = %s\\text{ (cm)}$ và $BH = |%s - %s| = %s\\text{ (cm)}$.\\
Áp dụng định lí Pythagore trong các tam giác vuông $AHC$ và $BHC$, ta được:\\
$AC = BC = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s\\sqrt{2}\\text{ (cm)}$.\\
- Chu vi tam giác $ABC$ là: $C_{\\triangle ABC} = AB + AC + BC = %s + %s\\sqrt{2}\\text{ (cm)}$.\\
- Diện tích tam giác $ABC$ là: $S_{\\triangle ABC} = \\frac{1}{2} \\cdot CH \\cdot AB = \\frac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.'''
                   % (hs1, xa, xa,
                      hs2, xb, xb,
                      hs1, hs2, xb - xa, xc,
                      xc, xc, b1, yc, xc, yc,
                      tikz_code,
                      xc, yc, yc, xb, xa, ab_len,
                      xc, xa, h, xb, xc, h,
                      h, h, 2 * h * h, h,
                      ab_len, 2 * h,
                      yc, ab_len, s_abc))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
