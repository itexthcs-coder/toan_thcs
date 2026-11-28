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

def bt_dang18_p3_b1_c8_ds8(self):
    # Dạng 18: Bài toán cấp mã thẻ nhân viên theo quy tắc chữ số
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_first = randint(2, 6)
        ans = d_first * 10 * 9
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một công ty cấp mã nhân viên gồm $4$ chữ số: chữ số đầu tiên chọn từ tập $\\{1; 2; \\dots; %s\\}$, ba chữ số sau chọn tùy ý từ $\\{0; 1; 2; \\dots; 9\\}$. Chọn ngẫu nhiên một mã nhân viên. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố "Hai chữ số cuối cùng của mã nhân viên có tổng bằng $10$"?'''
                         % (d_first))

        # Nội dung lời giải
        loigiai = ('''Xét một mã nhân viên dạng $\\overline{abcd}$ thỏa mãn bài toán: \\
- Chữ số thứ nhất $a$ có $%s$ cách chọn từ $\\{1; 2; \\dots; %s\\}$. \\
- Chữ số thứ hai $b$ có $10$ cách chọn từ $\\{0; 1; 2; \\dots; 9\\}$. \\
- Hai chữ số cuối $(c; d)$ có tổng $c + d = 10$ gồm $9$ cặp là $(1;9), (2;8), (3;7), (4;6), (5;5), (6;4), (7;3), (8;2), (9;1)$. \\
Vậy số kết quả thuận lợi là $%s \\cdot 10 \\cdot 9 = %s$.'''
                   % (d_first, d_first, d_first, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
