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

def bt_dang6_p4_b1_c8_ds8(self):
    # Dạng 6: Tọa độ điểm trên mặt phẳng tọa độ Oxy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, -2])
        pts = [
            ('A', 1, a * 1),
            ('B', -2, 4),
            ('C', 0, -3),
            ('D', 2, a * 2 + 1),
            ('E', -1, 3),
            ('F', 3, -2)
        ]
        str_pts = '; '.join([f"{name}({x0}; {y0})" for name, x0, y0 in pts])
        str_names = '; '.join([name for name, _, _ in pts])
        
        tl = [name for name, x0, y0 in pts if (y0 == a * x0) or (x0 < 0 and y0 > 0)]
        str_tl = '; '.join(tl)
        
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho $6$ điểm: $%s$. Chọn ngẫu nhiên một điểm trong $6$ điểm trên.\\
a) Liệt kê các kết quả có thể của hành động trên.\\
b) Xác định các kết quả thuận lợi cho biến cố $F$: ``Điểm được chọn nằm trên đồ thị hàm số $y = %sx$ hoặc nằm ở góc phần tư thứ II''.'''
                         % (str_pts, a))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động chọn ngẫu nhiên một điểm là: $%s$ (có $6$ kết quả có thể).
\\item Ta kiểm tra từng điều kiện của biến cố $F$:
\\begin{itemize}
\\item Điểm $A(1; %s)$ thỏa mãn $y = %s \\cdot 1 = %s$ nên điểm $A$ nằm trên đồ thị hàm số $y = %sx$.
\\item Các điểm có hoành độ âm và tung độ dương ($x < 0, y > 0$) nằm ở góc phần tư thứ II là: $B(-2; 4)$ và $E(-1; 3)$.
\\item Các điểm $C(0; -3)$, $D(2; %s)$, $F(3; -2)$ không thỏa mãn điều kiện nào của biến cố $F$.
\\end{itemize}
Vậy các kết quả thuận lợi cho biến cố $F$ là: $%s$.
\\end{enumEX}'''
                   % (str_names, a, a, a, a, a * 2 + 1, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
