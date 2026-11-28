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

def bt_dang3_p4_b1_c8_ds8(self):
    # Dạng 3: Tổng các chữ số và tính chất số học
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        digits = sorted(random.sample([1, 2, 3, 4, 5, 6, 7], 3))
        d1, d2, d3 = digits
        nums = [10 * a + b for a in digits for b in digits if a != b]
        str_nums = '; '.join(map(str, nums))
        
        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0: return False
            return True
            
        tl = [n for n in nums if is_prime((n // 10) + (n % 10))]
        if not tl:
            digits = [1, 2, 4]
            d1, d2, d3 = digits
            nums = [10 * a + b for a in digits for b in digits if a != b]
            str_nums = '; '.join(map(str, nums))
            tl = [n for n in nums if is_prime((n // 10) + (n % 10))]
        str_tl = '; '.join(map(str, tl))
        
        noidungcauhoi = ('''Từ ba chữ số $%s; %s; %s$, người ta lập tất cả các số tự nhiên có hai chữ số khác nhau và viết mỗi số lên một mảnh giấy giống nhau rồi bỏ vào hộp. Rút ngẫu nhiên một mảnh giấy từ trong hộp.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên.\\
b) Tìm các kết quả thuận lợi cho biến cố $C$: ``Số ghi trên mảnh giấy rút được có tổng hai chữ số là một số nguyên tố''.'''
                         % (d1, d2, d3))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Từ ba chữ số $%s; %s; %s$, ta lập được $6$ số tự nhiên có hai chữ số khác nhau là: $%s$.\\
Vậy các kết quả có thể của hành động rút mảnh giấy là: $%s$ (có $6$ kết quả có thể).
\\item Xét tổng hai chữ số của từng số trên, các số có tổng hai chữ số là số nguyên tố gồm: $%s$.\\
Vậy các kết quả thuận lợi cho biến cố $C$ là: $%s$.
\\end{enumEX}'''
                   % (d1, d2, d3, str_nums, str_nums, str_tl, str_tl))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
