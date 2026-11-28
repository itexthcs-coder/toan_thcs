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

def bt_dang4_p3_b1_c8_ds8(self):
    # Dạng 4: Lập số tự nhiên có hai chữ số từ tập chữ số cho trước
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        digits = sorted(random.sample([1, 2, 3, 4, 5, 6, 7, 8], 5))
        nums = [10 * a + b for a in digits for b in digits if a != b]
        fav = [num for num in nums if num % 3 == 0]
        ans = len(fav)
        kq_str = str(ans)
        digits_str = '; '.join(map(str, digits))
        fav_str = '; '.join(map(str, fav))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Từ các chữ số $\\{%s\\}$, bạn Khoa lập tất cả các số tự nhiên có hai chữ số khác nhau rồi viết mỗi số lên một mảnh giấy giống nhau. Bốc ngẫu nhiên một mảnh giấy. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $B$: "Số trên mảnh giấy chia hết cho $3$"?'''
                         % (digits_str))

        # Nội dung lời giải
        loigiai = ('''Các số có hai chữ số khác nhau lập từ tập $\\{%s\\}$ gồm $5 \\cdot 4 = 20$ số (tương ứng $20$ kết quả có thể). \\
Trong các số đó, những số có tổng các chữ số chia hết cho $3$ là: $%s$. \\
Vậy có $%s$ kết quả thuận lợi cho biến cố $B$.'''
                   % (digits_str, fav_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
