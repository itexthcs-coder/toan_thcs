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
    a = random.choice([30, 35, 40, 45, 50, 55, 70, 80, 90, 100])
    val = a**(1/3)
    val_round2 = round(val, 2)
    
    def fmt_vn(num, dec=2):
        return f"{num:.{dec}f}".replace('.', ',')
    
    val_screen = f"{val:.9f}".replace('.', ',')
    kq_dung = fmt_vn(val_round2, 2)
    sai1 = f"{math.floor(val * 100) / 100:.2f}".replace('.', ',') if round(val, 2) > math.floor(val * 100) / 100 else fmt_vn(val_round2 + 0.01, 2)
    sai2 = f"{val:.3f}".replace('.', ',')
    sai3 = f"{val:.1f}".replace('.', ',')
    sai4 = fmt_vn(val_round2 - 0.01, 2)
    
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
    noidungcauhoi = ('''Dùng máy tính cầm tay tính $\\sqrt[3]{%s}$ (màn hình hiển thị $%s$). Làm tròn kết quả này với độ chính xác $0,005$ ta được'''
                     % (latex(a), val_screen))
    
    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    # Nội dung lời giải
    loigiai = ('''Để làm tròn với độ chính xác $0,005$, ta làm tròn số thập phân đến hàng phần trăm (chữ số thập phân thứ hai).\\\\
Từ kết quả $\\sqrt[3]{%s} \\approx %s$, làm tròn đến hàng phần trăm ta được $%s$.'''
               % (latex(a), val_screen, kq_dung))

# Xuất câu trắc nghiệm
content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

print(content)
