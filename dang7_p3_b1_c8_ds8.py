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

def bt_dang7_p3_b1_c8_ds8(self):
    # Dạng 7: Chọn 2 thẻ sao cho tổng hai số là số lẻ
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = randint(8, 15)
        chan = n // 2
        le = n - chan
        ans = chan * le
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một hộp có $%s$ tấm thẻ giống nhau được đánh số từ $1$ đến $%s$. Lấy ngẫu nhiên đồng thời $2$ tấm thẻ từ hộp. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $C$: "Tổng hai số ghi trên hai tấm thẻ là một số lẻ"?'''
                         % (n, n))

        # Nội dung lời giải
        loigiai = ('''Từ $1$ đến $%s$ có $%s$ số lẻ và $%s$ số chẵn. \\
Tổng hai số là một số lẻ khi và chỉ khi chọn được $1$ tấm thẻ ghi số lẻ và $1$ tấm thẻ ghi số chẵn. \\
Do đó số kết quả thuận lợi cho biến cố $C$ là $%s \\cdot %s = %s$.'''
                   % (n, le, chan, le, chan, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
