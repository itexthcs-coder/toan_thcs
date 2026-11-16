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
    bien_so = random.choice(['a', 'm', 'p', 'k'])
    bien_can = random.choice(['x', 'y', 't', 'u'])
    
    # Các đáp án trắc nghiệm
    du = ['$%s^3 = %s$' % (bien_can, bien_so)]
    da = random.choice(du)
    s = [
        '$%s^2 = %s$' % (bien_can, bien_so),
        '$%s^3 = %s$' % (bien_so, bien_can),
        '$3%s = %s$' % (bien_can, bien_so),
        '$%s^3 = -%s$' % (bien_can, bien_so),
        '$%s^2 = -%s$' % (bien_can, bien_so)
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Căn bậc ba của một số thực $%s$ là số thực $%s$ thỏa mãn điều kiện nào sau đây?'''
                     % (bien_so, bien_can))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Theo định nghĩa, căn bậc ba của số thực $%s$ là số thực $%s$ thỏa mãn $%s^3 = %s$.'''
               % (bien_so, bien_can, bien_can, bien_so))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
