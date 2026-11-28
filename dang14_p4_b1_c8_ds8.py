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

def bt_dang14_p4_b1_c8_ds8(self):
    # Dạng 14: Thực đơn dinh dưỡng - Combo món ăn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mon_chinh = ["Phở bò (P)", "Bún chả (B)", "Bánh mì (M)"]
        do_uong = ["Sữa đậu nành (S)", "Nước cam (C)", "Trà đá (T)", "Cà phê (F)"]
        mc_code = ['P', 'B', 'M']
        du_code = ['S', 'C', 'T', 'F']
        
        all_combo = [f"({m}; {u})" for m in mc_code for u in du_code]
        tl = [f"({m}; {u})" for m in ['P', 'B'] for u in ['S', 'C']]
        
        noidungcauhoi = ('''Một quán ăn sáng phục vụ $3$ món chính: Phở bò (kí hiệu $P$), Bún chả (kí hiệu $B$), Bánh mì (kí hiệu $M$) và $4$ loại đồ uống: Sữa đậu nành (kí hiệu $S$), Nước cam (kí hiệu $C$), Trà đá (kí hiệu $T$), Cà phê (kí hiệu $F$). Một khách hàng chọn ngẫu nhiên một suất ăn sáng gồm $1$ món chính và $1$ đồ uống.\\
a) Liệt kê tất cả các thực đơn có thể chọn dưới dạng cặp (món chính; đồ uống). Có bao nhiêu kết quả có thể?\\
b) Tìm các kết quả thuận lợi cho biến cố $P$: ``Khách hàng không chọn Bánh mì và đồ uống được chọn không chứa caffeine (loại trừ Trà đá và Cà phê)''.'''
                         )
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Mỗi món chính có thể kết hợp với $4$ loại đồ uống nên có $3 \\cdot 4 = 12$ thực đơn có thể chọn là:\\
$%s$.
\\item Theo điều kiện biến cố $P$:
\\begin{itemize}
\\item Không chọn Bánh mì ($M$) nên món chính chỉ có thể là Phở bò ($P$) hoặc Bún chả ($B$).
\\item Đồ uống không chứa caffeine (loại trừ $T$ và $F$) nên đồ uống chỉ có thể là Sữa đậu nành ($S$) hoặc Nước cam ($C$).
\\end{itemize}
Vậy các kết quả thuận lợi cho biến cố $P$ là: $%s$ (có $4$ kết quả thuận lợi).
\\end{enumEX}'''
                   % ('; '.join(all_combo), '; '.join(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
