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
    a = randint(2, 6)
    kq = random.choice([-4, -3, -2, 2, 3, 4])
    x_val = random.choice([-5, -3, -2, -1, 1, 2, 3, 4, 5])
    b = kq**3 - a * x_val
    bt = a*x + b
    gt_trong_can = kq**3
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % latex(kq)]
    da = random.choice(du)
    s = [
        '$%s$' % latex(-kq),
        '$%s$' % latex(gt_trong_can),
        '$%s$' % latex(kq + 1),
        '$%s$' % latex(kq - 1),
        '$%s$' % latex(3*kq)
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Giá trị của căn thức $\\sqrt[3]{%s}$ tại $x = %s$ là'''
                     % (latex(bt), latex(x_val)))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Thay $x = %s$ vào căn thức $\\sqrt[3]{%s}$, ta được:
$$\\sqrt[3]{%s \\cdot (%s) + (%s)} = \\sqrt[3]{%s} = \\sqrt[3]{(%s)^3} = %s.$$'''
               % (latex(x_val), latex(bt), latex(a), latex(x_val), latex(b), latex(gt_trong_can), latex(kq), latex(kq)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
