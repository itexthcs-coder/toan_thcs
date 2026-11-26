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

def bt_dang20_p4_b4_c7_ds8(self):
    # Dạng 20 (Thực tế 5): Công thức chuyển đổi nhiệt độ F = 1,8*C + 32
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c_cho = random.choice([25, 30, 35, 37, 40])
        f_tinh = round(1.8 * c_cho + 32, 1)
        
        c_nguoc = random.choice([5, 10, 15, 20, 45])
        f_cho = int(round(1.8 * c_nguoc + 32))
        
        bang_str = (
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|}\n'
            '\\hline\n'
            'Nhiệt độ Celsius ($^\\circ\\text{C}$) & $0$ & $%s$ & $%s$ & $100$ \\\\ \\hline\n'
            'Nhiệt độ Fahrenheit ($^\\circ\\text{F}$) & $32$ & $%s$ & $%s$ & $212$ \\\\ \\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (c_nguoc, c_cho, f_cho, fmt_num(f_tinh))
        )
        
        noidungcauhoi = ('''Trong khoa học và đời sống quốc tế, ngoài thang đo độ Celsius ($^\\circ\\text{C}$) phổ biến ở Việt Nam, người ta còn dùng thang đo độ Fahrenheit ($^\\circ\\text{F}$). Mối liên hệ giữa nhiệt độ $F$ ($^\\circ\\text{F}$) và nhiệt độ $C$ ($^\\circ\\text{C}$) là một hàm số bậc nhất $F = aC + b$. Biết rằng nước tinh khiết đóng băng ở $0^\\circ\\text{C}$ tương ứng với $32^\\circ\\text{F}$, và sôi ở $100^\\circ\\text{C}$ tương ứng với $212^\\circ\\text{F}$.\\
a) Tìm các hệ số $a$, $b$ để thiết lập công thức chuyển đổi từ độ C sang độ F.\\
b) Nhiệt độ $%s^\\circ\\text{C}$ tương ứng với bao nhiêu độ F?\\
c) Một bản tin thời tiết quốc tế báo nhiệt độ ngoài trời là $%s^\\circ\\text{F}$, nhiệt độ này tương ứng với bao nhiêu độ C?'''
                         % (c_cho, f_cho))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thay các cặp giá trị tương ứng vào công thức $F = aC + b$, ta có:\\
- Khi $C = 0$ thì $F = 32$, suy ra: $a \\cdot 0 + b = 32 \\Leftrightarrow b = 32$.\\
- Khi $C = 100$ thì $F = 212$, suy ra: $100a + 32 = 212 \\Leftrightarrow 100a = 180 \\Leftrightarrow a = 1,8$ (hay $a = \\frac{9}{5}$).\\
Vậy công thức chuyển đổi từ độ C sang độ F là $F = 1,8C + 32$.
\\item Thay $C = %s$ vào công thức $F = 1,8C + 32$, ta được:\\
$F = 1,8 \\cdot %s + 32 = %s + 32 = %s\\text{ }(^\\circ\\text{F})$.\\
Vậy $%s^\\circ\\text{C}$ tương ứng với $%s^\\circ\\text{F}$.
\\item Thay $F = %s$ vào công thức $F = 1,8C + 32$, ta có phương trình:\\
$1,8C + 32 = %s \\Leftrightarrow 1,8C = %s \\Leftrightarrow C = \\frac{%s}{1,8} = %s\\text{ }(^\\circ\\text{C})$.\\
Bảng đối chiếu một số mức nhiệt độ:\\
%s\\
Vậy $%s^\\circ\\text{F}$ tương ứng với $%s^\\circ\\text{C}$.
\\end{enumEX}'''
                   % (c_cho, c_cho, fmt_num(round(1.8 * c_cho, 1)), fmt_num(f_tinh), c_cho, fmt_num(f_tinh),
                      f_cho, f_cho, f_cho - 32, f_cho - 32, c_nguoc,
                      bang_str,
                      f_cho, c_nguoc))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
