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
    tu = randint(1, 7)
    x0 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    mau = x - x0
    
    # Các đáp án trắc nghiệm
    du = ['$x \\ne %s$' % latex(x0)]
    da = random.choice(du)
    s = [
        '$x > %s$' % latex(x0),
        '$x \\ge %s$' % latex(x0),
        '$x < %s$' % latex(x0),
        'Với mọi $x \\in \\mathbb{R}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Căn thức bậc ba $\\sqrt[3]{\\frac{%s}{%s}}$ xác định khi nào?'''
                     % (latex(tu), latex(mau)))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Vì mọi số thực đều có căn bậc ba nên căn thức bậc ba $\\sqrt[3]{\\frac{%s}{%s}}$ xác định khi biểu thức $\\frac{%s}{%s}$ xác định, tức là $%s \\ne 0 \\Leftrightarrow x \\ne %s$.'''
               % (latex(tu), latex(mau), latex(tu), latex(mau), latex(mau), latex(x0)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
