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

def bt_dang19_p4_b4_c7_ds8(self):
    # Dạng 19 (Thực tế 4): Lương cứng L0 + hoa hồng h * n sản phẩm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        luong_cung = random.choice([6000000, 6500000, 7000000])
        hoa_hong = random.choice([300000, 350000, 400000])
        n_thang10 = random.choice([20, 22, 24, 25])
        thu_nhap_10 = luong_cung + hoa_hong * n_thang10
        
        # Mục tiêu tháng 11 không chia hết để học sinh phải làm tròn lên số sản phẩm nguyên
        n_muctieu_min = n_thang10 + random.choice([8, 9, 10])
        thu_nhap_muctieu = luong_cung + hoa_hong * (n_muctieu_min - 1) + 150000
        
        def fmt_vnd(val):
            return '{:,}'.format(val).replace(',', '.')
            
        n_le = frac(thu_nhap_muctieu - luong_cung, hoa_hong)
        n_le_dec = fmt_dec(float(n_le), '0.01')
        
        noidungcauhoi = ('''Một công ty phân phối thiết bị gia dụng trả lương hằng tháng cho nhân viên kinh doanh gồm hai phần: lương cứng cố định là $%s$ đồng/tháng và tiền hoa hồng là $%s$ đồng cho mỗi sản phẩm bán được trong tháng.\\
a) Lập công thức tính tổng thu nhập $T$ (đồng) trong một tháng của nhân viên đó khi bán được $n$ sản phẩm ($n \\in \\mathbb{N}$).\\
b) Trong tháng $10$, nhân viên Nam nhận được tổng thu nhập là $%s$ đồng. Hỏi trong tháng đó anh Nam đã bán được bao nhiêu sản phẩm?\\
c) Nếu mục tiêu của anh Nam trong tháng $11$ là đạt thu nhập tối thiểu $%s$ đồng thì anh cần bán được ít nhất bao nhiêu sản phẩm?'''
                         % (fmt_vnd(luong_cung), fmt_vnd(hoa_hong), fmt_vnd(thu_nhap_10), fmt_vnd(thu_nhap_muctieu)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khi bán được $n$ sản phẩm ($n \\in \\mathbb{N}$), số tiền hoa hồng nhân viên nhận được là $%sn$ (đồng).\\
Công thức tính tổng thu nhập $T$ trong một tháng của nhân viên đó là:\\
$T = %sn + %s$ (đồng).
\\item Trong tháng $10$, anh Nam nhận được $T = %s$ đồng nên ta có phương trình:\\
$%sn + %s = %s \\Leftrightarrow %sn = %s \\Leftrightarrow n = \\frac{%s}{%s} = %s$ (sản phẩm).\\
Vậy trong tháng $10$, anh Nam đã bán được $%s$ sản phẩm.
\\item Để đạt thu nhập tối thiểu $%s$ đồng trong tháng $11$ thì $T \\ge %s$, suy ra:\\
$%sn + %s \\ge %s \\Leftrightarrow %sn \\ge %s \\Leftrightarrow n \\ge \\frac{%s}{%s} \\approx %s$.\\
Vì số sản phẩm $n$ là số tự nhiên nên anh Nam cần bán được ít nhất $%s$ sản phẩm.
\\end{enumEX}'''
                   % (fmt_vnd(hoa_hong),
                      fmt_vnd(hoa_hong), fmt_vnd(luong_cung),
                      fmt_vnd(thu_nhap_10),
                      fmt_vnd(hoa_hong), fmt_vnd(luong_cung), fmt_vnd(thu_nhap_10),
                      fmt_vnd(hoa_hong), fmt_vnd(thu_nhap_10 - luong_cung),
                      fmt_vnd(thu_nhap_10 - luong_cung), fmt_vnd(hoa_hong), n_thang10,
                      n_thang10,
                      fmt_vnd(thu_nhap_muctieu), fmt_vnd(thu_nhap_muctieu),
                      fmt_vnd(hoa_hong), fmt_vnd(luong_cung), fmt_vnd(thu_nhap_muctieu),
                      fmt_vnd(hoa_hong), fmt_vnd(thu_nhap_muctieu - luong_cung),
                      fmt_vnd(thu_nhap_muctieu - luong_cung), fmt_vnd(hoa_hong), n_le_dec,
                      n_muctieu_min))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
