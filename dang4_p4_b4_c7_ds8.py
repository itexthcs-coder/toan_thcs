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

def bt_dang4_p4_b4_c7_ds8(self):
    # Dạng 4: Đường thẳng (d): y = (m + p)x - k*m + q. Tìm m để cắt Ox tại điểm cho trước và tìm điểm cố định
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([1, 2, 3])
        k = random.choice([2, 3, 4])
        # Điểm cố định I(k; p*k + q)
        q = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        y_fix = p * k + q
        
        # Chọn m_ans != -p sao cho hoành độ giao điểm trục Ox là số nguyên
        while True:
            m_ans = random.choice([-4, -3, -2, 0, 1, 2, 3, 4])
            if m_ans == -p:
                continue
            tu = k * m_ans - q
            mau = m_ans + p
            if tu % mau == 0 and tu != 0:
                x_ox = tu // mau
                break
        
        dau_q = '+' if q > 0 else '-'
        abs_q = abs(q)
        
        noidungcauhoi = ('''Cho đường thẳng $(d): y = (m + %s)x - %sm %s %s$ ($m \\neq -%s$).\\
a) Tìm $m$ để đường thẳng $(d)$ cắt trục hoành tại điểm có hoành độ bằng $%s$.\\
b) Chứng minh rằng với mọi giá trị của $m \\neq -%s$, đường thẳng $(d)$ luôn đi qua một điểm cố định. Hãy xác định tọa độ điểm cố định đó.'''
                         % (p, k, dau_q, abs_q, p,
                            x_ox,
                            p))
        
        hs_m_pt = x_ox - k
        vp_pt = -p * x_ox - q
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì đường thẳng $(d)$ cắt trục hoành tại điểm có hoành độ bằng $%s$ nên điểm $A(%s; 0)$ thuộc $(d)$.\\
Thay $x = %s$, $y = 0$ vào phương trình đường thẳng $(d)$, ta được:\\
$(m + %s) \\cdot (%s) - %sm %s %s = 0 \\Leftrightarrow %sm + (%s) - %sm %s %s = 0 \\Leftrightarrow %sm = %s \\Leftrightarrow m = %s$ (thỏa mãn $m \\neq -%s$).\\
Vậy $m = %s$ là giá trị cần tìm.
\\item Gọi $I(x_0; y_0)$ là điểm cố định mà đường thẳng $(d)$ luôn đi qua với mọi $m \\neq -%s$.\\
Khi đó, phương trình sau luôn nghiệm đúng với mọi $m \\neq -%s$:\\
$y_0 = (m + %s)x_0 - %sm %s %s \\Leftrightarrow (x_0 - %s)m + (%sx_0 %s %s - y_0) = 0$.\\
Điều này xảy ra khi và chỉ khi:\\
$\\begin{cases} x_0 - %s = 0 \\ %sx_0 %s %s - y_0 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x_0 = %s \\ y_0 = %s \\cdot %s %s %s = %s \\end{cases}$.\\
Vậy với mọi $m \\neq -%s$, đường thẳng $(d)$ luôn đi qua điểm cố định $I(%s; %s)$.
\\end{enumEX}'''
                   % (x_ox, x_ox,
                      x_ox,
                      p, x_ox, k, dau_q, abs_q, x_ox, p * x_ox, k, dau_q, abs_q, hs_m_pt, vp_pt, m_ans, p,
                      m_ans,
                      p,
                      p,
                      p, k, dau_q, abs_q, k, p, dau_q, abs_q,
                      k, p, dau_q, abs_q, k, p, k, dau_q, abs_q, y_fix,
                      p, k, y_fix))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
