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

def bt_dang1_p3_b1_c8_ds8(self):
    # Dạng 1: Chọn đồng thời 2 đối tượng từ tập hợp hỗn hợp
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n1 = randint(4, 9)
        n2 = randint(3, 8)
        tong = n1 + n2
        ans = tong * (tong - 1) // 2
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hộp kín đựng $%s$ chiếc bút bi màu xanh và $%s$ chiếc bút bi màu đen có hình dạng và kích thước giống hệt nhau. Lấy ngẫu nhiên đồng thời $2$ chiếc bút từ hộp. Hỏi có tất cả bao nhiêu kết quả có thể xảy ra của hành động trên?'''
                         % (n1, n2))

        # Nội dung lời giải
        loigiai = ('''Tổng số bút trong hộp là $%s + %s = %s$ (chiếc). \\
Kí hiệu các chiếc bút từ $1$ đến $%s$. Mỗi cách lấy đồng thời $2$ chiếc bút cho một cặp gồm $2$ chiếc bút khác nhau (không phân biệt thứ tự). \\
Với chiếc bút thứ nhất có $%s$ cách chọn, chiếc bút thứ hai có $%s$ cách chọn; do mỗi cặp bị lặp lại $2$ lần nên số kết quả có thể là $\\dfrac{%s \\cdot %s}{2} = %s$.'''
                   % (n1, n2, tong, tong, tong, tong - 1, tong, tong - 1, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
