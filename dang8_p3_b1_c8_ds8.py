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

def bt_dang8_p3_b1_c8_ds8(self):
    # Dạng 8: Phân công nhân sự trực theo nhóm giới tính
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nam = randint(11, 18)
        nu = randint(12, 20)
        ans = nam * nu
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Đội tình nguyện của trường gồm $%s$ nam và $%s$ nữ. Ban tổ chức chọn ngẫu nhiên $1$ bạn nam và $1$ bạn nữ để làm MC dẫn chương trình. Hỏi có tất cả bao nhiêu kết quả có thể cho việc chọn cặp MC này?'''
                         % (nam, nu))

        # Nội dung lời giải
        loigiai = ('''Kí hiệu $%s$ bạn nam và $%s$ bạn nữ bằng các mã số riêng biệt. \\
Có $%s$ cách chọn bạn nam làm MC; ứng với mỗi bạn nam được chọn, có $%s$ cách chọn bạn nữ đi kèm. \\
Vậy tổng số kết quả có thể là $%s \\cdot %s = %s$.'''
                   % (nam, nu, nam, nu, nam, nu, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
