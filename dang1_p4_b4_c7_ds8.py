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

def bt_dang1_p4_b4_c7_ds8(self):
    # Dạng 1: Tìm tham số m để hàm số y = (m^2 - k^2)x^2 + (m - k)x + c*m + d là hàm số bậc nhất và đồ thị đi qua điểm A(x0; y0)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
        c = random.choice([2, 3, 4, 5])
        d = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        # Khi m = -k thì m^2 - k^2 = 0 và m - k = -2k != 0
        m_val = -k
        y0 = (-2 * k) * x0 + c * m_val + d
        
        k2 = k * k
        # Biểu diễn (m - k)x + c*m + d
        dau_d = '+' if d > 0 else '-'
        abs_d = abs(d)
        hs_m_sau = -k * x0 + c
        hs_tu_do_sau = -k * x0 + d
        
        noidungcauhoi = ('''Cho hàm số $y = (m^2 - %s)x^2 + (m - %s)x + %sm %s %s$ (với $m$ là tham số). Tìm tất cả các giá trị của $m$ để hàm số đã cho là hàm số bậc nhất và đồ thị của nó đi qua điểm $A(%s; %s)$.'''
                         % (k2, k, c, dau_d, abs_d, x0, y0))
        
        # Xử lý hiển thị phương trình tìm m
        if hs_m_sau == 1:
            ve_trai = 'm'
        elif hs_m_sau == -1:
            ve_trai = '-m'
        else:
            ve_trai = '%sm' % hs_m_sau
        if hs_tu_do_sau > 0:
            ve_trai += ' + %s' % hs_tu_do_sau
        elif hs_tu_do_sau < 0:
            ve_trai += ' - %s' % abs(hs_tu_do_sau)
            
        vp_sau = y0 - hs_tu_do_sau
        
        loigiai = ('''Để hàm số $y = (m^2 - %s)x^2 + (m - %s)x + %sm %s %s$ là hàm số bậc nhất thì hệ số của $x^2$ phải bằng $0$ và hệ số của $x$ phải khác $0$:\\
$\\begin{cases} m^2 - %s = 0 \\ m - %s \\neq 0 \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\text{ hoặc } m = %s \\ m \\neq %s \\end{cases} \\Leftrightarrow m = %s$.\\
Với $m = %s$, hàm số trở thành $y = %sx + (%s)$.\\
Vì đồ thị hàm số đi qua điểm $A(%s; %s)$ nên thay $x = %s$, $y = %s$ vào công thức hàm số ta được:\\
$%s \\cdot (%s) + (%s) = %s \\Leftrightarrow %s = %s$ (luôn đúng).\\
Vậy $m = %s$ là giá trị cần tìm.'''
                   % (k2, k, c, dau_d, abs_d,
                      k2, k, k, -k, k, m_val,
                      m_val, -2*k, c*m_val + d,
                      x0, y0, x0, y0,
                      -2*k, x0, c*m_val + d, y0, y0, y0,
                      m_val))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
