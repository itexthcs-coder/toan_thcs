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

def bt_dang18_p4_b4_c7_ds8(self):
    # Dạng 18 (Thực tế 3): Bơm thoát nước thể tích ban đầu V0, lưu lượng Q m3/h
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        q_val = random.choice([20, 24, 30])
        t_het = random.choice([6, 7.5, 8])
        v0 = int(q_val * t_het)
        gio = random.choice([3, 4])
        phut = random.choice([15, 30, 45])
        t_tinh = gio + phut / 60.0
        v_con = round(v0 - q_val * t_tinh, 1)
        
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '  \\draw[->, line width=1pt] (0,0) -- (9,0) node[below] {$t\\text{ (giờ)}$};\n'
            '  \\draw[->, line width=1pt] (0,0) -- (0,5.5) node[left] {$V\\text{ (m}^3\\text{)}$};\n'
            '  \\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '  \\draw[line width=1pt] (0,4.5) -- (7.5,0);\n'
            '  \\fill (0,4.5) circle (1pt) node[left] {$%s$};\n'
            '  \\fill (7.5,0) circle (1pt) node[below] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (v0, fmt_num(t_het))
        )
        
        noidungcauhoi = ('''Sau một trận mưa lớn, một tầng hầm chung cư bị ngập nước với tổng thể tích nước ước tính là $%s\\text{ m}^3$. Ban quản lý huy động máy bơm công suất lớn để hút nước ra ngoài với lưu lượng không đổi là $%s\\text{ m}^3/\\text{giờ}$.\\
a) Viết công thức tính thể tích nước $V$ ($\\text{m}^3$) còn lại trong tầng hầm sau $t$ giờ bơm ($0 \\le t \\le %s$).\\
b) Vẽ đồ thị biểu diễn hàm số $V$ theo $t$ trên mặt phẳng tọa độ (với $0 \\le t \\le %s$).\\
c) Sau $%s$ giờ $%s$ phút bơm liên tục, trong tầng hầm còn lại bao nhiêu mét khối nước?'''
                         % (v0, q_val, fmt_num(t_het), fmt_num(t_het), gio, phut))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Sau $t$ giờ bơm, lượng nước máy bơm hút được ra ngoài là $%st$ ($\\text{m}^3$).\\
Thể tích nước $V$ còn lại trong tầng hầm sau $t$ giờ bơm là:\\
$V = %s - %st$ (hay $V = -%st + %s$) với $0 \\le t \\le %s$.
\\item Đồ thị hàm số $V = -%st + %s$ với $0 \\le t \\le %s$ là đoạn thẳng nối hai điểm $A(0; %s)$ và $B(%s; 0)$ như hình vẽ minh họa:\\
%s
\\item Đổi $%s$ giờ $%s$ phút $= %s$ giờ.\\
Thay $t = %s$ vào công thức hàm số, ta được thể tích nước còn lại trong tầng hầm là:\\
$V = %s - %s \\cdot %s = %s - %s = %s\\text{ (m}^3\\text{)}$.
\\end{enumEX}'''
                   % (q_val, v0, q_val, q_val, v0, fmt_num(t_het),
                      q_val, v0, fmt_num(t_het), v0, fmt_num(t_het),
                      tikz_code,
                      gio, phut, fmt_num(t_tinh),
                      fmt_num(t_tinh),
                      v0, q_val, fmt_num(t_tinh), v0, fmt_num(round(q_val * t_tinh, 1)), fmt_num(v_con)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
