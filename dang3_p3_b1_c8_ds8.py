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

def bt_dang3_p3_b1_c8_ds8(self):
    # Dạng 3: Gieo đồng thời 2 con xúc xắc xét điều kiện tổng số chấm
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        s_min = random.choice([7, 8, 9, 10])
        pairs = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j >= s_min]
        ans = len(pairs)
        kq_str = str(ans)
        pairs_str = '; '.join(['(%s;%s)' % (i, j) for i, j in pairs])

        # Nội dung câu hỏi
        noidungcauhoi = ('''Gieo ngẫu nhiên đồng thời hai con xúc xắc cân đối và đồng chất (một con màu trắng, một con màu đen). Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $A$: "Tổng số chấm xuất hiện trên hai con xúc xắc lớn hơn hoặc bằng $%s$"?'''
                         % (s_min))

        # Nội dung lời giải
        loigiai = ('''Mỗi kết quả có thể là một cặp $(x; y)$, trong đó $x, y \\in \\{1; 2; 3; 4; 5; 6\\}$ lần lượt là số chấm trên xúc xắc trắng và xúc xắc đen. \\
Các cặp $(x; y)$ thỏa mãn $x + y \\ge %s$ là: $%s$. \\
Đếm tất cả các cặp trên, ta được $%s$ kết quả thuận lợi cho biến cố $A$.'''
                   % (s_min, pairs_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
