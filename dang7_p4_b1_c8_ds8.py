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

def bt_dang7_p4_b1_c8_ds8(self):
    # Dạng 7: Gieo đồng thời hai con xúc xắc cân đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        loai = random.choice(['chinh_phuong', 'chia_het_4'])
        pairs = [(i, j) for i in range(1, 7) for j in range(1, 7)]
        if loai == 'chinh_phuong':
            dk_str = "Tổng số chấm xuất hiện trên hai con xúc xắc là một số chính phương"
            tl = [f"({i}; {j})" for i, j in pairs if (i + j) in [4, 9]]
            giai_thich = "Tổng số chấm trên hai con xúc xắc nhận giá trị từ $2$ đến $12$. Các số chính phương trong khoảng này là $4$ và $9$."
        else:
            dk_str = "Tổng số chấm xuất hiện trên hai con xúc xắc chia hết cho $4$"
            tl = [f"({i}; {j})" for i, j in pairs if (i + j) % 4 == 0]
            giai_thich = "Tổng số chấm trên hai con xúc xắc nhận giá trị từ $2$ đến $12$. Các số chia hết cho $4$ trong khoảng này là $4; 8; 12$."
        str_tl = '; '.join(tl)
        
        noidungcauhoi = ('''Gieo đồng thời hai con xúc xắc cân đối và đồng chất (một con màu trắng và một con màu đỏ). Kí hiệu $(x; y)$ là kết quả của lần gieo, trong đó $x$ là số chấm xuất hiện trên con xúc xắc trắng và $y$ là số chấm xuất hiện trên con xúc xắc đỏ.\\
a) Hỏi có tất cả bao nhiêu kết quả có thể của thực nghiệm trên?\\
b) Liệt kê các kết quả thuận lợi cho biến cố $G$: ``%s''.'''
                         % (dk_str))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Con xúc xắc trắng có $6$ khả năng xuất hiện mặt ($x \\in \\{1; 2; 3; 4; 5; 6\\}$). Ứng với mỗi giá trị của $x$, con xúc xắc đỏ cũng có $6$ khả năng xuất hiện mặt ($y \\in \\{1; 2; 3; 4; 5; 6\\}$).\\
Vậy có tất cả $6 \\cdot 6 = 36$ kết quả có thể xảy ra.
\\item %s\\
Liệt kê các cặp $(x; y)$ thỏa mãn điều kiện trên, ta được các kết quả thuận lợi cho biến cố $G$ là:\\
$%s$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (giai_thich, str_tl, len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
