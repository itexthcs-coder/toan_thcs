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

def bt_dang2_p4_b4_c7_ds8(self):
    # Dạng 2: Tìm tham số k để đồ thị cắt trục tung tại điểm cho trước và vẽ đồ thị
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chọn k nguyên sao cho a = 2k - 1 != 0 và b = k + d chia hết cho a để giao điểm Ox đẹp
        while True:
            k_val = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            a_val = 2 * k_val - 1
            if a_val == 0:
                continue
            # Chọn giao điểm trục Ox là x_ox nguyên khác 0 trong [-4, 4]
            x_ox = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            y_oy = -a_val * x_ox
            if abs(y_oy) <= 5 and y_oy != 0:
                d = y_oy - k_val
                break
        
        dau_d = '+' if d >= 0 else '-'
        abs_d = abs(d)
        hs_str = fmt_linear(a_val, y_oy)
        
        # Tọa độ vẽ TikZ (giới hạn khung nhìn vừa vặn)
        x_min = min(-4, x_ox - 1)
        x_max = max(4, x_ox + 1)
        y_min = min(-4, y_oy - 1)
        y_max = max(4, y_oy + 1)
        
        # Tính 2 điểm đầu mút đoạn thẳng trong khung hình
        pts = []
        for xv in [x_min, x_max]:
            yv = a_val * xv + y_oy
            if y_min <= yv <= y_max:
                pts.append((xv, yv))
        for yv in [y_min, y_max]:
            xv = (yv - y_oy) / a_val
            if x_min <= xv <= x_max:
                pts.append((round(xv, 2), yv))
        pts = sorted(list(set(pts)))
        p1, p2 = pts[0], pts[-1]
        
        pos_P = 'left' if x_ox > 0 else 'right'
        pos_Q = 'below' if y_oy > 0 else 'above'
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[below] {$x$};\n'
            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (%s,%s) -- (%s,%s);\n'
            '  \\fill (0,%s) circle (1pt) node[%s] {$P(0;%s)$};\n'
            '  \\fill (%s,0) circle (1pt) node[%s] {$Q(%s;0)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (x_min, x_max, y_min, y_max,
               p1[0], p1[1], p2[0], p2[1],
               y_oy, pos_P, y_oy,
               x_ox, pos_Q, x_ox)
        )
        
        noidungcauhoi = ('''Cho hàm số bậc nhất $y = (2k - 1)x + k %s %s$ ($k \\neq \\frac{1}{2}$). Tìm giá trị của $k$ sao cho đồ thị hàm số cắt trục tung tại điểm có tung độ bằng $%s$, sau đó vẽ đồ thị của hàm số với giá trị $k$ vừa tìm được.'''
                         % (dau_d, abs_d, y_oy))
        
        loigiai = ('''Vì đồ thị hàm số $y = (2k - 1)x + k %s %s$ cắt trục tung tại điểm có tung độ bằng $%s$ nên điểm $P(0; %s)$ thuộc đồ thị hàm số.\\
Thay $x = 0$, $y = %s$ vào công thức hàm số, ta được:\\
$(2k - 1) \\cdot 0 + k %s %s = %s \\Leftrightarrow k %s %s = %s \\Leftrightarrow k = %s$ (thỏa mãn điều kiện $k \\neq \\frac{1}{2}$).\\
Với $k = %s$, hàm số có dạng $y = %s$.\\
Vẽ đồ thị hàm số $y = %s$:\\
- Cho $x = 0$ thì $y = %s$, ta được giao điểm của đồ thị với trục $Oy$ là $P(0; %s)$.\\
- Cho $y = 0$ thì $%s = 0 \\Leftrightarrow x = %s$, ta được giao điểm của đồ thị với trục $Ox$ là $Q(%s; 0)$.\\
Đồ thị của hàm số $y = %s$ là đường thẳng đi qua hai điểm $P(0; %s)$ và $Q(%s; 0)$ như hình vẽ sau:\\
%s'''
                   % (dau_d, abs_d, y_oy, y_oy,
                      y_oy, dau_d, abs_d, y_oy, dau_d, abs_d, y_oy, k_val,
                      k_val, hs_str,
                      hs_str,
                      y_oy, y_oy,
                      hs_str, x_ox, x_ox,
                      hs_str, y_oy, x_ox,
                      tikz_code))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
