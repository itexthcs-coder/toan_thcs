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

def bt_dang15_p3_b1_c8_ds8(self):
    # Dạng 15: Biến cố phủ định trên tập hợp kí tự
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        phrases = [
            ("VIET NAM VO DICH", "V", "I"),
            ("KET NOI TRI THUC", "T", "I"),
            ("CHINH PHUC TRI THUC", "H", "C"),
            ("TOAN HOC VA DOI SONG", "O", "A")
        ]
        phrase, c1, c2 = random.choice(phrases)
        letters = [ch for ch in phrase if ch != ' ']
        tong = len(letters)
        n1 = letters.count(c1)
        n2 = letters.count(c2)
        ans = tong - n1 - n2
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Viết mỗi chữ cái trong cụm từ "%s" (không tính dấu cách) lên một tấm thẻ giống nhau rồi cho vào hộp. Rút ngẫu nhiên một tấm thẻ từ hộp. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố "Rút được thẻ không phải chữ cái %s và cũng không phải chữ cái %s"?'''
                         % (phrase, c1, c2))

        # Nội dung lời giải
        loigiai = ('''Cụm từ "%s" có tất cả $%s$ chữ cái (tương ứng $%s$ tấm thẻ, tức $%s$ kết quả có thể). \\
Trong đó có $%s$ tấm thẻ ghi chữ cái %s và $%s$ tấm thẻ ghi chữ cái %s. \\
Vậy số kết quả thuận lợi cho biến cố đã cho là $%s - %s - %s = %s$.'''
                   % (phrase, tong, tong, tong, n1, c1, n2, c2, tong, n1, n2, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
