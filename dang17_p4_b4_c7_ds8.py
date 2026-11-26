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

def bt_dang17_p4_b4_c7_ds8(self):
    # Dạng 17 (Thực tế 2): Chiều dài lò xo l = a*m + l0
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        l0 = random.choice([18, 20, 22, 24])
        # Độ giãn mỗi 100g là d_100 cm (ví dụ 2cm hoặc 3cm)
        d_100 = random.choice([2, 3, 4])
        a_val = round(d_100 / 100.0, 2)
        m1 = 100
        m2 = 250
        l1 = l0 + d_100
        l2 = round(l0 + 2.5 * d_100, 1)
        
        m3 = 400
        l3 = round(l0 + 4 * d_100, 1)
        
        bang_str = (
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|}\n'
            '\\hline\n'
            'Khối lượng vật nặng $m$ (gam) & $0$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n'
            'Chiều dài lò xo $l$ (cm) & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (m1, m2, m3, l0, fmt_num(l1), fmt_num(l2), fmt_num(l3))
        )
        
        noidungcauhoi = ('''Theo định luật Hooke trong vật lý, chiều dài $l$ (cm) của một lò xo treo thẳng đứng phụ thuộc bậc nhất vào khối lượng $m$ (gam) của vật nặng treo vào đầu dưới của nó. Thực nghiệm cho thấy khi treo vật nặng $%s\\text{ g}$ thì lò xo dài $%s\\text{ cm}$, còn khi treo vật nặng $%s\\text{ g}$ thì lò xo dài $%s\\text{ cm}$.\\
a) Lập công thức biểu thị chiều dài $l$ của lò xo theo khối lượng $m$ của vật nặng (trong giới hạn đàn hồi).\\
b) Cho biết chiều dài tự nhiên của lò xo khi chưa treo vật nặng là bao nhiêu? Nếu muốn lò xo dài $%s\\text{ cm}$ thì cần treo vật nặng có khối lượng bao nhiêu gam?'''
                         % (m1, fmt_num(l1), m2, fmt_num(l2), fmt_num(l3)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì chiều dài $l$ phụ thuộc bậc nhất vào khối lượng $m$ nên công thức có dạng $l = am + b$ ($a \\neq 0$).\\
Theo dữ kiện thực nghiệm, ta có:\\
- Khi $m = %s$ thì $l = %s$, suy ra $%sa + b = %s \\quad (1)$.\\
- Khi $m = %s$ thì $l = %s$, suy ra $%sa + b = %s \\quad (2)$.\\
Lấy $(2)$ trừ $(1)$ theo từng vế, ta được:\\
$%sa = %s \\Leftrightarrow a = \\frac{%s}{%s} = %s$.\\
Thay $a = %s$ vào $(1)$, ta có: $%s \\cdot %s + b = %s \\Leftrightarrow %s + b = %s \\Leftrightarrow b = %s$.\\
Vậy công thức biểu thị chiều dài $l$ theo khối lượng $m$ là $l = %sm + %s$.
\\item Khi chưa treo vật nặng ($m = 0$), chiều dài tự nhiên của lò xo là: $l = %s \\cdot 0 + %s = %s\\text{ (cm)}$.\\
Khi lò xo dài $l = %s\\text{ cm}$, ta có phương trình:\\
$%sm + %s = %s \\Leftrightarrow %sm = %s \\Leftrightarrow m = \\frac{%s}{%s} = %s\\text{ (gam)}$.\\
Bảng tổng hợp số liệu thực nghiệm:\\
%s\\
Vậy chiều dài tự nhiên của lò xo là $%s\\text{ cm}$ và để lò xo dài $%s\\text{ cm}$ cần treo vật nặng có khối lượng $%s\\text{ gam}$.
\\end{enumEX}'''
                   % (m1, fmt_num(l1), m1, fmt_num(l1),
                      m2, fmt_num(l2), m2, fmt_num(l2),
                      m2 - m1, fmt_num(round(l2 - l1, 1)), fmt_num(round(l2 - l1, 1)), m2 - m1, fmt_num(a_val),
                      fmt_num(a_val), m1, fmt_num(a_val), fmt_num(l1), fmt_num(round(a_val * m1, 1)), fmt_num(l1), l0,
                      fmt_num(a_val), l0,
                      fmt_num(a_val), l0, l0,
                      fmt_num(l3),
                      fmt_num(a_val), l0, fmt_num(l3), fmt_num(a_val), fmt_num(round(l3 - l0, 1)), fmt_num(round(l3 - l0, 1)), fmt_num(a_val), m3,
                      bang_str,
                      l0, fmt_num(l3), m3))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
