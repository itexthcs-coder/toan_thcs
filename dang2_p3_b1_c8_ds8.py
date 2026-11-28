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

def bt_dang2_p3_b1_c8_ds8(self):
    # Dạng 2: Tìm tham số giới hạn trên dựa vào số kết quả thuận lợi chia hết
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([3, 4, 5, 6, 7, 8])
        so_kq = randint(8, 18)
        ans = k * (so_kq + 1) - 1
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hộp chứa các tấm thẻ giống nhau được đánh số liên tiếp từ $1$ đến $n$ ($n \\in \\mathbb{N}^*$). Rút ngẫu nhiên một tấm thẻ từ hộp. Biết rằng có đúng $%s$ kết quả thuận lợi cho biến cố $E$: "Rút được tấm thẻ ghi số chia hết cho $%s$". Tìm giá trị lớn nhất của $n$.'''
                         % (so_kq, k))

        # Nội dung lời giải
        loigiai = ('''Các số nguyên dương đầu tiên chia hết cho $%s$ là $%s \\cdot 1; %s \\cdot 2; \\dots; %s \\cdot %s = %s$. \\
Số chia hết cho $%s$ thứ $%s$ là $%s \\cdot %s = %s$. \\
Để có đúng $%s$ kết quả thuận lợi cho biến cố $E$ thì $%s \\le n < %s$. Vậy giá trị lớn nhất của $n$ là $%s$.'''
                   % (k, k, k, k, so_kq, k * so_kq, k, so_kq + 1, k, so_kq + 1, k * (so_kq + 1), so_kq, k * so_kq, k * (so_kq + 1), kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
