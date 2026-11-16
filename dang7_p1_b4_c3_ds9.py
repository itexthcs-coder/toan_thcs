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
    cap_so = random.choice([
        ('-0,001', '-0,1', '0,1', '-0,01', '-0,0001'),
        ('0,008', '0,2', '-0,2', '0,02', '0,002'),
        ('-0,027', '-0,3', '0,3', '-0,03', '-0,003'),
        ('0,064', '0,4', '-0,4', '0,04', '0,8'),
        ('-0,125', '-0,5', '0,5', '-0,05', '-0,25'),
        ('1,331', '1,1', '-1,1', '0,11', '1,21')
    ])
    so_de, kq_dung, sai1, sai2, sai3 = cap_so
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % kq_dung]
    da = random.choice(du)
    s = [
        '$%s$' % sai1,
        '$%s$' % sai2,
        '$%s$' % sai3,
        '$0$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Giá trị của $\\sqrt[3]{%s}$ là''' % so_de)
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Vì $(%s)^3 = %s$ nên $\\sqrt[3]{%s} = \\sqrt[3]{(%s)^3} = %s$.'''
               % (kq_dung, so_de, so_de, kq_dung, kq_dung))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
