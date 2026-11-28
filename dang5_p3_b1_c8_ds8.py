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

def bt_dang5_p3_b1_c8_ds8(self):
    # Dạng 5: Thiết lập mã khóa mật khẩu gồm chữ và số
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        letters = random.sample(['M', 'N', 'P', 'Q', 'K'], random.randint(2, 4))
        digits = sorted(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], random.randint(3, 5)))
        n_l = len(letters)
        n_d = len(digits)
        ans = n_l * n_d * (n_d - 1)
        kq_str = str(ans)
        l_str = '; '.join(letters)
        d_str = '; '.join(map(str, digits))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ổ khóa vali dùng mật mã gồm $3$ kí tự: kí tự đầu tiên là một chữ cái lấy từ tập $\\{%s\\}$, hai kí tự sau là hai chữ số khác nhau lấy từ tập $\\{%s\\}$. Một người thử ngẫu nhiên một mật mã. Hỏi có tất cả bao nhiêu kết quả có thể của hành động thử mật mã này?'''
                         % (l_str, d_str))

        # Nội dung lời giải
        loigiai = ('''Mỗi kết quả có thể là một bộ $3$ kí tự hợp lệ của mật mã: \\
- Kí tự thứ nhất có $%s$ cách chọn từ tập $\\{%s\\}$. \\
- Kí tự thứ hai có $%s$ cách chọn từ tập $\\{%s\\}$. \\
- Kí tự thứ ba khác kí tự thứ hai nên có $%s$ cách chọn. \\
Vậy số kết quả có thể là $%s \\cdot %s \\cdot %s = %s$.'''
                   % (n_l, l_str, n_d, d_str, n_d - 1, n_l, n_d, n_d - 1, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
