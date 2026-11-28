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

def bt_dang12_p3_b1_c8_ds8(self):
    # Dạng 12: Tung đồng xu liên tiếp nhiều lần
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([4, 5, 6])
        ans = k + 1
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tung một đồng xu cân đối và đồng chất liên tiếp $%s$ lần. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $M$: "Mặt sấp xuất hiện ít nhất $%s$ lần"?'''
                         % (k, k - 1))

        # Nội dung lời giải
        loigiai = ('''Mỗi kết quả có thể là một dãy gồm $%s$ kí tự $S$ (sấp) hoặc $N$ (ngửa), có tất cả $2^{%s} = %s$ kết quả. \\
Mặt sấp xuất hiện ít nhất $%s$ lần gồm $2$ trường hợp: \\
- Xuất hiện đúng $%s$ lần: mặt ngửa nằm ở $1$ trong $%s$ vị trí nên có $%s$ kết quả. \\
- Xuất hiện cả $%s$ lần: có $1$ kết quả duy nhất (tất cả đều là $S$). \\
Tổng cộng có $%s + 1 = %s$ kết quả thuận lợi cho biến cố $M$.'''
                   % (k, k, 2**k, k - 1, k - 1, k, k, k, k, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
