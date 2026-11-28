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
from decimal import Decimal, ROUND_HALF_UP

def bt_dang17_p3_b1_c8_ds8(self):
    # Dạng 17: Bài toán ngược tìm số lượng phần tử chưa biết trong hộp
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        do = randint(5, 10)
        vang = randint(4, 9)
        k = randint(3, 5)
        ans = k * vang - do - vang
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hộp có $%s$ viên bi đỏ, $%s$ viên bi vàng và $x$ viên bi xanh có cùng kích thước. Lấy ngẫu nhiên một viên bi từ hộp. Biết rằng số kết quả có thể của hành động này gấp $%s$ lần số kết quả thuận lợi cho biến cố "Lấy được viên bi màu vàng". Tìm giá trị của $x$.'''
                         % (do, vang, k))

        # Nội dung lời giải
        loigiai = ('''Số kết quả có thể của hành động lấy một viên bi từ hộp là $%s + %s + x = %s + x$. \\
Số kết quả thuận lợi cho biến cố lấy được viên bi màu vàng là $%s$. \\
Theo đề bài ta có: $%s + x = %s \\cdot %s = %s \\Rightarrow x = %s$.'''
                   % (do, vang, do + vang, vang, do + vang, k, vang, k * vang, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
