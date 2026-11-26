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

def bt_dang16_p4_b4_c7_ds8(self):
    # Dạng 16 (Thực tế 1): Chi phí lắp điện mặt trời ban đầu B triệu, mỗi tháng tiết kiệm A triệu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([1.2, 1.5, 1.8, 2.0])
        thang_hv = random.choice([25, 30, 35, 40])
        b_val = round(a_val * thang_hv, 1)
        so_nam = random.choice([4, 5])
        so_thang_sau = so_nam * 12
        loi_ich = round(a_val * so_thang_sau - b_val, 1)
        
        # Bảng minh họa theo mốc thời gian
        t1 = 10
        t2 = 20
        t3 = thang_hv
        t4 = so_thang_sau
        y1 = round(a_val * t1 - b_val, 1)
        y2 = round(a_val * t2 - b_val, 1)
        
        bang_str = (
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|}\n'
            '\\hline\n'
            'Thời gian sử dụng $x$ (tháng) & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n'
            'Chênh lệch tài chính $y$ (triệu đồng) & $%s$ & $%s$ & $0$ & $%s$ \\\\ \\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (t1, t2, t3, t4, fmt_num(y1), fmt_num(y2), fmt_num(loi_ich))
        )
        
        noidungcauhoi = ('''Một hộ gia đình đầu tư hệ thống điện mặt trời áp mái với chi phí lắp đặt ban đầu là $%s$ triệu đồng. Trung bình mỗi tháng, hệ thống này giúp gia đình tiết kiệm được $%s$ triệu đồng tiền điện sinh hoạt.\\
a) Gọi $y$ (triệu đồng) là số tiền chênh lệch giữa tổng tiền điện tiết kiệm được sau $x$ tháng sử dụng và chi phí lắp đặt ban đầu. Hãy viết công thức biểu thị $y$ theo $x$. Công thức này có phải là hàm số bậc nhất không?\\
b) Sau bao nhiêu tháng sử dụng thì hộ gia đình này bắt đầu hoàn vốn (tức là $y = 0$)? Sau $%s$ năm, gia đình thu về khoản lợi ích ròng là bao nhiêu triệu đồng?'''
                         % (fmt_num(b_val), fmt_num(a_val), so_nam))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Sau $x$ tháng sử dụng, tổng số tiền điện gia đình tiết kiệm được là $%sx$ (triệu đồng).\\
Số tiền chênh lệch giữa tổng tiền điện tiết kiệm được và chi phí lắp đặt ban đầu là:\\
$y = %sx - %s$.\\
Vì công thức có dạng $y = ax + b$ với $a = %s \\neq 0$ và $b = -%s$ nên đây là một hàm số bậc nhất của $x$.
\\item Để bắt đầu hoàn vốn thì $y = 0$, ta có phương trình:\\
$%sx - %s = 0 \\Leftrightarrow %sx = %s \\Leftrightarrow x = \\frac{%s}{%s} = %s$ (tháng).\\
Đổi $%s$ năm $= %s \\cdot 12 = %s$ tháng. Thay $x = %s$ vào công thức hàm số, ta được:\\
$y = %s \\cdot %s - %s = %s - %s = %s$ (triệu đồng).\\
Bảng tổng hợp giá trị tài chính tại một số mốc thời gian:\\
%s\\
Vậy sau $%s$ tháng sử dụng thì gia đình bắt đầu hoàn vốn và sau $%s$ năm, gia đình thu về khoản lợi ích ròng là $%s$ triệu đồng.
\\end{enumEX}'''
                   % (fmt_num(a_val),
                      fmt_num(a_val), fmt_num(b_val),
                      fmt_num(a_val), fmt_num(b_val),
                      fmt_num(a_val), fmt_num(b_val), fmt_num(a_val), fmt_num(b_val), fmt_num(b_val), fmt_num(a_val), thang_hv,
                      so_nam, so_nam, so_thang_sau, so_thang_sau,
                      fmt_num(a_val), so_thang_sau, fmt_num(b_val), fmt_num(round(a_val * so_thang_sau, 1)), fmt_num(b_val), fmt_num(loi_ich),
                      bang_str,
                      thang_hv, so_nam, fmt_num(loi_ich)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
