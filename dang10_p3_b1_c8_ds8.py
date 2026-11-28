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

def bt_dang10_p3_b1_c8_ds8(self):
    # Dạng 10: Bốc thăm từ 2 hộp độc lập xét tính chẵn lẻ của tích
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n1 = randint(5, 9)
        n2 = randint(6, 10)
        le1 = (n1 + 1) // 2
        le2 = (n2 + 1) // 2
        tong_kq = n1 * n2
        tich_le = le1 * le2
        ans = tong_kq - tich_le
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Hộp I đựng $%s$ tấm thẻ đánh số từ $1$ đến $%s$. Hộp II đựng $%s$ tấm thẻ đánh số từ $1$ đến $%s$. Từ mỗi hộp rút ngẫu nhiên một tấm thẻ. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $K$: "Tích hai số ghi trên hai tấm thẻ là một số chẵn"?'''
                         % (n1, n1, n2, n2))

        # Nội dung lời giải
        loigiai = ('''Mỗi kết quả có thể là một cặp $(a; b)$, với $a$ là số trên thẻ ở hộp I và $b$ là số trên thẻ ở hộp II. Tổng số kết quả có thể là $%s \\cdot %s = %s$. \\
Tích hai số là số lẻ khi cả hai số đều lẻ: hộp I có $%s$ số lẻ, hộp II có $%s$ số lẻ nên có $%s \\cdot %s = %s$ kết quả cho tích lẻ. \\
Vậy số kết quả thuận lợi cho tích chẵn là $%s - %s = %s$.'''
                   % (n1, n2, tong_kq, le1, le2, le1, le2, tich_le, tong_kq, tich_le, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
