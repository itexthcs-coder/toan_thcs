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

def bt_dang8_p4_b1_c8_ds8(self):
    # Dạng 8: Thực nghiệm 2 giai đoạn - Quay vòng quay và tung đồng xu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        letters = random.choice([['A', 'B', 'C'], ['E', 'M', 'N'], ['I', 'K', 'L'], ['O', 'P', 'Q']])
        vowels = {'A', 'E', 'I', 'O', 'U'}
        kq_cothe = [f"({ch}; {coin})" for ch in letters for coin in ['S', 'N']]
        str_cothe = '; '.join(kq_cothe)
        
        tl = [f"({ch}; N)" for ch in letters if ch in vowels]
        str_tl = '; '.join(tl)
        vowel_found = [ch for ch in letters if ch in vowels][0]
        
        noidungcauhoi = ('''Một trò chơi gồm hai bước liên tiếp: Bước 1 quay một bánh xe chia làm $3$ phần bằng nhau ghi các chữ cái $%s, %s, %s$; Bước 2 tung một đồng xu cân đối có hai mặt Sấp (kí hiệu $S$) và Ngửa (kí hiệu $N$).\\
a) Liệt kê tất cả các kết quả có thể của trò chơi trên dưới dạng cặp (chữ cái; mặt đồng xu).\\
b) Tìm các kết quả thuận lợi cho biến cố $H$: ``Kim chỉ vào chữ cái nguyên âm và đồng xu xuất hiện mặt Ngửa''.'''
                         % (letters[0], letters[1], letters[2]))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tất cả các kết quả có thể của trò chơi gồm $6$ cặp là: $%s$.
\\item Trong ba chữ cái $%s, %s, %s$, chữ cái nguyên âm là $%s$. Đồng xu xuất hiện mặt Ngửa được kí hiệu là $N$.\\
Vậy kết quả thuận lợi cho biến cố $H$ là: $%s$ (có $1$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (str_cothe, letters[0], letters[1], letters[2], vowel_found, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
