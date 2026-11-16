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
    a = random.choice([-3, -2, -1, 1, 2, 3])
    c = randint(2, 8)
    nhi_thuc = x + a
    da_thuc = sp.expand(nhi_thuc**3)
    phan_ngoai = -x + c
    kq = sp.simplify(phan_ngoai + nhi_thuc)
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % latex(kq)]
    da = random.choice(du)
    s = [
        '$%s$' % latex(c - a),
        '$%s$' % latex(-2*x + c + a),
        '$%s$' % latex(2*x + c + a),
        '$%s$' % latex(c + a**3)
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Rút gọn biểu thức $A = %s + \\sqrt[3]{%s}$ ta được kết quả là'''
                     % (latex(phan_ngoai), latex(da_thuc)))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Ta có $%s = (%s)^3$.\\\\
Do đó:
\\begin{align*}
A &= %s + \\sqrt[3]{%s} \\\\
&= %s + \\sqrt[3]{(%s)^3} \\\\
&= %s + (%s) = %s.
\\end{align*}'''
               % (latex(da_thuc), latex(nhi_thuc), latex(phan_ngoai), latex(da_thuc), latex(phan_ngoai), latex(nhi_thuc), latex(phan_ngoai), latex(nhi_thuc), latex(kq)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
