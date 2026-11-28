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

def bt_dang14_p3_b1_c8_ds8(self):
    # Dạng 14: Bài toán thực tế chọn thực đơn có điều kiện ràng buộc
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        kv = randint(3, 6)
        mc = randint(4, 7)
        tm = randint(2, 5)
        tong = kv * mc * tm
        ans = tong - tm
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Thực đơn của một quán ăn gồm $%s$ món khai vị, $%s$ món chính và $%s$ món tráng miệng. Một khách hàng chọn ngẫu nhiên một suất ăn gồm đủ $3$ món (mỗi loại $1$ món). Biết rằng món khai vị súp cua không dùng chung với món chính lẩu hải sản. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố "Khách hàng chọn được suất ăn không đồng thời có cả súp cua và lẩu hải sản"?'''
                         % (kv, mc, tm))

        # Nội dung lời giải
        loigiai = ('''Tổng số cách chọn một suất ăn bất kì gồm $3$ món là $%s \\cdot %s \\cdot %s = %s$. \\
Số cách chọn suất ăn có đồng thời súp cua và lẩu hải sản (kèm $1$ trong $%s$ món tráng miệng) là $1 \\cdot 1 \\cdot %s = %s$. \\
Vậy số kết quả thuận lợi cho biến cố đã cho là $%s - %s = %s$.'''
                   % (kv, mc, tm, tong, tm, tm, tm, tong, tm, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
