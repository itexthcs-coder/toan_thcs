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

def bt_dang6_p3_b1_c8_ds8(self):
    # Dạng 6: Biến cố hợp trên vòng quay số (nguyên lí bù trừ)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong = randint(40, 65)
        a, b = random.choice([(3, 4), (3, 5), (4, 5), (4, 6), (6, 8)])
        lcm_ab = (a * b) // math.gcd(a, b)
        n_a = tong // a
        n_b = tong // b
        n_ab = tong // lcm_ab
        ans = n_a + n_b - n_ab
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vòng quay may mắn có $%s$ ô được đánh số từ $1$ đến $%s$. Quay kim một lần và quan sát số ở ô kim dừng lại. Gọi $E$ là biến cố "Kim dừng ở ô ghi số chia hết cho $%s$ hoặc chia hết cho $%s$". Tìm số kết quả thuận lợi cho biến cố $E$.'''
                         % (tong, tong, a, b))

        # Nội dung lời giải
        loigiai = ('''Từ $1$ đến $%s$: \\
- Số các số chia hết cho $%s$ là $%s$ số. \\
- Số các số chia hết cho $%s$ là $%s$ số. \\
- Số các số chia hết cho cả $%s$ và $%s$ (tức chia hết cho $%s$) là $%s$ số. \\
Vậy số kết quả thuận lợi cho biến cố $E$ là $%s + %s - %s = %s$.'''
                   % (tong, a, n_a, b, n_b, a, b, lcm_ab, n_ab, n_a, n_b, n_ab, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
