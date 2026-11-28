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

def bt_dang13_p3_b1_c8_ds8(self):
    # Dạng 13: Bài toán hình học đếm tam giác tạo thành từ các điểm
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = randint(8, 12)
        m = randint(3, 5)
        tong_c3 = n * (n - 1) * (n - 2) // 6
        thang_c3 = m * (m - 1) * (m - 2) // 6
        ans = tong_c3 - thang_c3
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên mặt phẳng cho $%s$ điểm phân biệt, trong đó có đúng $%s$ điểm thẳng hàng, ngoài ra không có $3$ điểm nào khác thẳng hàng. Chọn ngẫu nhiên $3$ điểm trong $%s$ điểm đã cho. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $T$: "Ba điểm được chọn tạo thành một tam giác"?'''
                         % (n, m, n))

        # Nội dung lời giải
        loigiai = ('''Tổng số cách chọn $3$ điểm bất kì từ $%s$ điểm là $\\dfrac{%s \\cdot %s \\cdot %s}{6} = %s$. \\
Số cách chọn $3$ điểm thẳng hàng từ $%s$ điểm thẳng hàng là $\\dfrac{%s \\cdot %s \\cdot %s}{6} = %s$. \\
Ba điểm không thẳng hàng tạo thành một tam giác, nên số kết quả thuận lợi cho biến cố $T$ là $%s - %s = %s$.'''
                   % (n, n, n - 1, n - 2, tong_c3, m, m, m - 1, m - 2, thang_c3, tong_c3, thang_c3, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
