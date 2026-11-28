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

def bt_dang11_p3_b1_c8_ds8(self):
    # Dạng 11: So sánh hiệu số kết quả thuận lợi của hai biến cố (giá trị âm)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = randint(30, 55)
        sq = [i * i for i in range(1, 10) if i * i <= n]
        a = len(sq)
        b = n // 3
        ans = a - b
        kq_str = str(ans)
        sq_str = '; '.join(map(str, sq))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một túi đựng $%s$ viên bi được đánh số từ $1$ đến $%s$. Lấy ngẫu nhiên một viên bi từ túi. Gọi $a$ là số kết quả thuận lợi cho biến cố "Lấy được viên bi ghi số chính phương" và $b$ là số kết quả thuận lợi cho biến cố "Lấy được viên bi ghi số chia hết cho $3$". Tính giá trị của $a - b$.'''
                         % (n, n))

        # Nội dung lời giải
        loigiai = ('''Từ $1$ đến $%s$: \\
- Các số chính phương là $%s$ nên có $a = %s$ kết quả thuận lợi. \\
- Các số chia hết cho $3$ gồm $%s$ số nên có $b = %s$ kết quả thuận lợi. \\
Vậy $a - b = %s - %s = %s$.'''
                   % (n, sq_str, a, b, b, a, b, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
