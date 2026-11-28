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
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational
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

def bt_dang17_p4_b1_c8_ds8(self):
    # Dạng 17: Thể thao và giải đấu - Bảng điểm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        names = ["An", "Bình", "Chi", "Dũng", "Giang", "Hà"]
        scores_sets = [
            [5, 4.5, 4, 3.5, 3, 1],
            [6, 5, 4.5, 3, 2.5, 3],
            [5.5, 4.5, 4, 3, 2, 2]
        ]
        scores = random.choice(scores_sets)
        tong_diem = sum(scores)
        tb = tong_diem / 6
        
        def fmt_vn(val):
            if val == int(val):
                return str(int(val))
            return str(val).replace('.', '{,}')
            
        info_str = ', '.join([f"{n} (${fmt_vn(s)}$ điểm)" for n, s in zip(names, scores)])
        tl = [n for n, s in zip(names, scores) if s > tb]
        
        noidungcauhoi = ('''Trong một giải cờ vua học sinh có $6$ kỳ thủ tham gia với số điểm hiện tại lần lượt là: %s. Ban tổ chức chọn ngẫu nhiên $1$ kỳ thủ để phỏng vấn.\\
a) Liệt kê các kết quả có thể của hành động trên.\\
b) Tìm các kết quả thuận lợi cho biến cố $S$: ``Kỳ thủ được chọn có số điểm cao hơn điểm trung bình của cả $6$ kỳ thủ''.'''
                         % (info_str))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động chọn ngẫu nhiên $1$ kỳ thủ là: %s (có $6$ kết quả có thể).
\\item Điểm trung bình của cả $6$ kỳ thủ là:\\
$\\dfrac{%s}{6} = %s$ (điểm).\\
Các kỳ thủ có số điểm cao hơn $%s$ điểm là: %s.\\
Vậy các kết quả thuận lợi cho biến cố $S$ là: %s (có $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (', '.join(names), ' + '.join([fmt_vn(s) for s in scores]), fmt_vn(tb), fmt_vn(tb), ', '.join(tl), ', '.join(tl), len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
