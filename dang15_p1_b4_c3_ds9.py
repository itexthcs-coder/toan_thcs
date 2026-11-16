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
    a = randint(1, 3)
    b = random.choice([2, 3, 5, 6, 7])
    while a >= math.sqrt(b):
        b = random.choice([2, 3, 5, 6, 7, 10, 11])
    bt = a - sqrt(b)
    bt_doi = sqrt(b) - a
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % latex(bt)]
    da = random.choice(du)
    s = [
        '$%s$' % latex(bt_doi),
        '$%s$' % latex(a + sqrt(b)),
        '$%s$' % latex(-a - sqrt(b)),
        '$%s$' % latex(a**3 - b)
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Rút gọn biểu thức $\\sqrt[3]{(%s)^3}$ ta được kết quả là''' % latex(bt))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Áp dụng hằng đẳng thức $\\sqrt[3]{A^3} = A$ với mọi số thực $A$, ta có:
$$\\sqrt[3]{(%s)^3} = %s.$$'''
               % (latex(bt), latex(bt)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
