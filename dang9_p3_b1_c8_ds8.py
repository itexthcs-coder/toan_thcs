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

def bt_dang9_p3_b1_c8_ds8(self):
    # Dạng 9: Tỉ số giữa số kết quả thuận lợi và số kết quả có thể
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong = random.choice([25, 30, 35, 40, 45, 50])
        k = random.choice([3, 4, 6, 7])
        m = tong // k
        h1 = Rational(m, tong)
        number = Decimal(float(h1))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một lô hàng gồm $%s$ sản phẩm được đánh số thứ tự từ $1$ đến $%s$. Kiểm tra ngẫu nhiên một sản phẩm. Gọi $m$ là số kết quả thuận lợi cho biến cố "Chọn được sản phẩm có số thứ tự là bội của $%s$" và $n$ là số kết quả có thể của phép thử. Tính tỉ số $\\dfrac{m}{n}$ (kết quả làm tròn đến hàng phần trăm).'''
                         % (tong, tong, k))

        # Nội dung lời giải
        loigiai = ('''Số kết quả có thể của phép thử kiểm tra một sản phẩm là $n = %s$. \\
Từ $1$ đến $%s$ có $%s$ số chia hết cho $%s$ (bội của $%s$) nên $m = %s$. \\
Do đó tỉ số $\\dfrac{m}{n} = \\dfrac{%s}{%s} \\approx %s$.'''
                   % (tong, tong, m, k, k, m, m, tong, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
