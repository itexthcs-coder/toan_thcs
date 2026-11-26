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

def bt_dang14_p4_b4_c7_ds8(self):
    # Dạng 14: Rút gọn hàm số dạng tổng phân thức và tìm điểm M(x; y) thuộc đồ thị có x + y = 0
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chọn y = (p*x + q)/2 + (r*x + s)/4 = ((2p+r)/4)x + (2q+s)/4
        # Đảm bảo a = (2p+r)/4 nguyên khác 0 và khác -1, b = (2q+s)/4 chia hết cho (a + 1)
        while True:
            a_val = random.choice([-3, -2, 1, 2, 3])
            p = random.choice([1, 2, 3])
            r = 4 * a_val - 2 * p
            if r == 0:
                continue
            x_ans = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            b_val = -(a_val + 1) * x_ans
            q = random.choice([-3, -1, 1, 3])
            s = 4 * b_val - 2 * q
            if s != 0:
                break
                
        tu1 = fmt_linear(p, q)
        tu2 = fmt_linear(r, s)
        hs_str = fmt_linear(a_val, b_val)
        y_ans = -x_ans
        
        noidungcauhoi = ('''Cho hàm số $y = \\frac{%s}{2} + \\frac{%s}{4}$.\\
a) Chứng tỏ rằng hàm số đã cho là hàm số bậc nhất và xác định các hệ số $a$, $b$.\\
b) Tìm tọa độ điểm $M$ thuộc đồ thị hàm số đã cho sao cho hoành độ và tung độ của điểm $M$ là hai số đối nhau.'''
                         % (tu1, tu2))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Quy đồng và rút gọn biểu thức hàm số, ta có:\\
$y = \\frac{2(%s) + (%s)}{4} = \\frac{%s + (%s)}{4} = \\frac{%s}{4} = %s$.\\
Vì hàm số có dạng $y = ax + b$ với $a = %s \\neq 0$ và $b = %s$ nên hàm số đã cho là hàm số bậc nhất.
\\item Gọi tọa độ điểm cần tìm là $M(x_0; y_0)$.\\
Vì hoành độ và tung độ của điểm $M$ là hai số đối nhau nên $y_0 = -x_0$.\\
Lại vì $M(x_0; y_0)$ thuộc đồ thị hàm số $y = %s$ nên ta có:\\
$y_0 = %sx_0 + (%s) \\Leftrightarrow -x_0 = %sx_0 + (%s) \\Leftrightarrow %sx_0 = %s \\Leftrightarrow x_0 = %s$.\\
Suy ra $y_0 = -(%s) = %s$.\\
Vậy tọa độ điểm cần tìm là $M(%s; %s)$.
\\end{enumEX}'''
                   % (tu1, tu2, fmt_linear(2*p, 2*q), tu2, fmt_linear(4*a_val, 4*b_val), hs_str,
                      a_val, b_val,
                      hs_str,
                      a_val, b_val, a_val, b_val, -(a_val + 1), b_val, x_ans,
                      x_ans, y_ans,
                      x_ans, y_ans))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
