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

# Khai báo biến
lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    a1 = randint(2, 5)
    a2 = randint(2, 5)
    c1 = a1**3
    c2 = -(a2**3)
    kq = a1 - (-a2)
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % latex(kq)]
    da = random.choice(du)
    s = [
        '$%s$' % latex(a1 - a2),
        '$%s$' % latex(-a1 - a2),
        '$%s$' % latex(a1 + a2 + 1),
        '$%s$' % latex(a1 + a2 - 1),
        '$%s$' % latex(c1 + c2)
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Giá trị của biểu thức $P = \\sqrt[3]{%s} - \\sqrt[3]{%s} + \\sqrt[3]{0}$ bằng'''
                     % (latex(c1), latex(c2)))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Ta có:
\\begin{align*}
P &= \\sqrt[3]{%s} - \\sqrt[3]{%s} + \\sqrt[3]{0} \\\\
&= \\sqrt[3]{%s^3} - \\sqrt[3]{(%s)^3} + 0 \\\\
&= %s - (%s) + 0 = %s.
\\end{align*}'''
               % (latex(c1), latex(c2), latex(a1), latex(-a2), latex(a1), latex(-a2), latex(kq)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
