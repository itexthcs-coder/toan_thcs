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
    bien_so = random.choice(['a', 'x', 'm', 'b'])
    
    # Các đáp án trắc nghiệm
    du = ['Mỗi số thực $%s$ đều có duy nhất một căn bậc ba.' % bien_so]
    da = random.choice(du)
    s = [
        'Chỉ các số thực không âm mới có căn bậc ba.',
        'Mỗi số thực dương có hai căn bậc ba là hai số đối nhau.',
        'Số thực âm không có căn bậc ba.',
        'Số $0$ không có căn bậc ba.',
        'Mỗi số thực âm có hai căn bậc ba phân biệt.'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Phát biểu nào sau đây là \\textbf{đúng} khi nói về căn bậc ba của một số thực?''')
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Theo tính chất của căn bậc ba: Mỗi số thực $%s$ đều có duy nhất một căn bậc ba (số dương có căn bậc ba là số dương, số âm có căn bậc ba là số âm, số $0$ có căn bậc ba là $0$).'''
               % bien_so)

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
