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
    tu = randint(1, 6)
    mau = randint(2, 7)
    while math.gcd(tu, mau) != 1:
        mau = randint(2, 7)
    dau = random.choice([1, -1])
    ps_kq = Rational(dau * tu, mau)
    ps_de = ps_kq**3
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % latex(ps_kq)]
    da = random.choice(du)
    s = [
        '$%s$' % latex(-ps_kq),
        '$%s$' % latex(Rational(dau * tu**2, mau**2)),
        '$%s$' % latex(Rational(dau * tu, mau**3)),
        '$%s$' % latex(Rational(dau * tu**3, mau)),
        '$%s$' % latex(Rational(dau * mau, tu))
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Kết quả của phép tính $\\sqrt[3]{%s}$ là''' % latex(ps_de))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Vì $\\left(%s\\right)^3 = %s$ nên $\\sqrt[3]{%s} = \\sqrt[3]{\\left(%s\\right)^3} = %s$.'''
               % (latex(ps_kq), latex(ps_de), latex(ps_de), latex(ps_kq), latex(ps_kq)))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
