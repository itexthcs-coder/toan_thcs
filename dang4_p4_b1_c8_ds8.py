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

def bt_dang4_p4_b1_c8_ds8(self):
    # Dạng 4: Nghiệm của phương trình và bất phương trình
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        S = list(range(-4, 6))
        str_S = '; '.join(map(str, S))
        a = random.choice([2, 3])
        b = random.randint(1, 3)
        c = random.randint(2, 5)
        k = random.choice([1, 2, 3])
        tl = [x_val for x_val in S if (a * x_val - b > c) or (abs(x_val) == k)]
        str_tl = '; '.join(map(str, tl))
        
        noidungcauhoi = ('''Cho tập hợp $S = \\{%s\\}$. Chọn ngẫu nhiên một số $x$ từ tập hợp $S$.\\
a) Có bao nhiêu kết quả có thể của hành động trên?\\
b) Xác định các kết quả thuận lợi cho biến cố $D$: ``Số $x$ được chọn thỏa mãn bất phương trình $%sx - %s > %s$ hoặc $|x| = %s$''.'''
                         % (str_S, a, b, c, k))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tập hợp $S$ có $10$ phần tử nên khi chọn ngẫu nhiên một số $x$ từ $S$ thì có tất cả $10$ kết quả có thể.
\\item Ta có:
\\begin{itemize}
\\item Bất phương trình $%sx - %s > %s \\Leftrightarrow %sx > %s \\Leftrightarrow x > \\dfrac{%s}{%s}$. Trong tập hợp $S$, các giá trị thỏa mãn là: $%s$.
\\item Phương trình $|x| = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$ (đều thuộc $S$).
\\end{itemize}
Kết hợp cả hai điều kiện, các kết quả thuận lợi cho biến cố $D$ là: $%s$.
\\end{enumEX}'''
                   % (a, b, c, a, b + c, b + c, a,
                      '; '.join(map(str, [v for v in S if a * v - b > c])),
                      k, k, k, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
