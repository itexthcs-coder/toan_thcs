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

def bt_dang15_p4_b4_c7_ds8(self):
    # Dạng 15: Tìm điều kiện của m để giao điểm của (d1): y = a1*x - b1 và (d2): y = x + m nằm ở góc phần tư thứ I
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([2, 3])
        b1 = random.choice([1, 2, 3, 4])
        # Phương trình hoành độ: a1*x - b1 = x + m <=> (a1 - 1)x = m + b1 => x = (m + b1)/(a1 - 1)
        # y = x + m = (a1*m + b1)/(a1 - 1)
        # Góc phần tư thứ I: x > 0 và y > 0 <=> m > -b1 và m > -b1/a1 <=> m > -b1/a1
        nguong_y = frac(-b1, a1)
        
        noidungcauhoi = ('''Tìm điều kiện của tham số $m$ để giao điểm của hai đường thẳng $(d_1): y = %sx - %s$ và $(d_2): y = x + m$ nằm ở góc phần tư thứ nhất trên mặt phẳng tọa độ $Oxy$ (tức là giao điểm có hoành độ dương và tung độ dương).'''
                         % (a1, b1))
        
        loigiai = ('''Xét phương trình hoành độ giao điểm của $(d_1)$ và $(d_2)$:\\
$%sx - %s = x + m \\Leftrightarrow %sx = m + %s \\Leftrightarrow x = \\frac{m + %s}{%s}$.\\
Thay $x = \\frac{m + %s}{%s}$ vào phương trình đường thẳng $(d_2)$, ta được tung độ giao điểm là:\\
$y = \\frac{m + %s}{%s} + m = \\frac{%sm + %s}{%s}$.\\
Để giao điểm của $(d_1)$ và $(d_2)$ nằm ở góc phần tư thứ nhất thì hoành độ và tung độ của giao điểm đều phải dương:\\
$\\begin{cases} x > 0 \\ y > 0 \\end{cases} \\Leftrightarrow \\begin{cases} \\frac{m + %s}{%s} > 0 \\ \\frac{%sm + %s}{%s} > 0 \\end{cases} \\Leftrightarrow \\begin{cases} m + %s > 0 \\ %sm + %s > 0 \\end{cases} \\Leftrightarrow \\begin{cases} m > -%s \\ m > %s \\end{cases} \\Leftrightarrow m > %s$.\\
Vậy với $m > %s$ thì giao điểm của hai đường thẳng nằm ở góc phần tư thứ nhất.'''
                   % (a1, b1, a1 - 1, b1, b1, a1 - 1,
                      b1, a1 - 1,
                      b1, a1 - 1, a1, b1, a1 - 1,
                      b1, a1 - 1, a1, b1, a1 - 1, b1, a1, b1, b1, fmt_num(nguong_y), fmt_num(nguong_y),
                      fmt_num(nguong_y)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
