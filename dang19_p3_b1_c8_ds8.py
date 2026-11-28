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

def bt_dang19_p3_b1_c8_ds8(self):
    # Dạng 19: Biến cố chia hết cho A hoặc B nhưng không chia hết cho cả hai
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = randint(36, 72)
        n2 = n // 2
        n3 = n // 3
        n6 = n // 6
        ans = n2 + n3 - 2 * n6
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Viết các số tự nhiên từ $1$ đến $%s$ lên $%s$ tấm thẻ giống nhau rồi trộn đều. Rút ngẫu nhiên một tấm thẻ. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $H$: "Rút được thẻ ghi số chia hết cho $2$ hoặc chia hết cho $3$, nhưng không chia hết cho $6$"?'''
                         % (n, n))

        # Nội dung lời giải
        loigiai = ('''Từ $1$ đến $%s$: \\
- Có $%s$ số chia hết cho $2$. \\
- Có $%s$ số chia hết cho $3$. \\
- Có $%s$ số chia hết cho cả $2$ và $3$ (tức chia hết cho $6$). \\
Số kết quả thuận lợi cho biến cố $H$ là $(%s - %s) + (%s - %s) = %s$.'''
                   % (n, n2, n3, n6, n2, n6, n3, n6, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
