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
    ds_so = [2, 3, 5, 6, 7, 10, 12, 15, 18, 20, -14, -18, -28]
    a = random.choice(ds_so)
    val = math.copysign(abs(a)**(1/3), a)
    val_round2 = round(val, 2)
    
    def fmt_vn(num, dec=2):
        return f"{num:.{dec}f}".replace('.', ',')
    
    val_full_str = f"{val:.9f}".replace('.', ',')
    kq_dung = fmt_vn(val_round2, 2)
    sai1 = fmt_vn(val_round2 + 0.01, 2)
    sai2 = fmt_vn(val_round2 - 0.01, 2)
    sai3 = f"{val:.3f}".replace('.', ',')
    sai4 = fmt_vn(-val_round2, 2)
    
    # Các đáp án trắc nghiệm
    du = ['$%s$' % kq_dung]
    da = random.choice(du)
    s = list(set([f'${sai1}$', f'${sai2}$', f'${sai3}$', f'${sai4}$']) - set(du))
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    # Câu hỏi
    noidungcauhoi = ('''Sử dụng máy tính cầm tay để tính $\\sqrt[3]{%s}$ và làm tròn kết quả đến chữ số thập phân thứ hai, ta được'''
                     % latex(a))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Sử dụng máy tính cầm tay, màn hình hiển thị kết quả $\\sqrt[3]{%s} \\approx %s$.\\\\
Làm tròn kết quả đến chữ số thập phân thứ hai ta được $\\sqrt[3]{%s} \\approx %s$.'''
               % (latex(a), val_full_str, latex(a), kq_dung))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
