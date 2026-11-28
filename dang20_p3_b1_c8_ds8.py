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

def bt_dang20_p3_b1_c8_ds8(self):
    # Dạng 20: Chọn 2 quyển sách khác thể loại từ tủ sách nhiều ngăn
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        s1 = randint(4, 8)
        s2 = randint(5, 9)
        s3 = randint(3, 7)
        ans = s1 * s2 + s2 * s3 + s3 * s1
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên giá sách có $%s$ quyển sách Toán, $%s$ quyển sách Ngữ văn và $%s$ quyển sách Tiếng Anh (các quyển sách đều khác nhau). Bạn Mai lấy ngẫu nhiên đồng thời $2$ quyển sách trên giá. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $Q$: "Hai quyển sách lấy được thuộc hai môn học khác nhau"?'''
                         % (s1, s2, s3))

        # Nội dung lời giải
        loigiai = ('''Để lấy được $2$ quyển sách thuộc hai môn học khác nhau, ta chia làm $3$ trường hợp: \\
- $1$ quyển Toán và $1$ quyển Ngữ văn: có $%s \\cdot %s = %s$ cách. \\
- $1$ quyển Ngữ văn và $1$ quyển Tiếng Anh: có $%s \\cdot %s = %s$ cách. \\
- $1$ quyển Tiếng Anh và $1$ quyển Toán: có $%s \\cdot %s = %s$ cách. \\
Vậy số kết quả thuận lợi cho biến cố $Q$ là $%s + %s + %s = %s$.'''
                   % (s1, s2, s1 * s2, s2, s3, s2 * s3, s3, s1, s3 * s1, s1 * s2, s2 * s3, s3 * s1, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
