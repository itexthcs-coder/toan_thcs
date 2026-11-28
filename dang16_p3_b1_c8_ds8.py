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

def bt_dang16_p3_b1_c8_ds8(self):
    # Dạng 16: Kết hợp phép thử ngẫu nhiên với điều kiện nghiệm nguyên của phương trình
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b_max = random.choice([10, 12, 14, 15, 18])
        counts = [b_max // a for a in range(1, 7)]
        ans = sum(counts)
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Bạn Hà gieo một con xúc xắc cân đối đồng chất để lấy số chấm xuất hiện làm giá trị cho $a$, sau đó rút ngẫu nhiên một tấm thẻ từ hộp đựng $%s$ tấm thẻ đánh số từ $1$ đến $%s$ để lấy số ghi trên thẻ làm giá trị cho $b$. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $P$: "Phương trình $ax - b = 0$ có nghiệm nguyên"?'''
                         % (b_max, b_max))

        # Nội dung lời giải
        loigiai = ('''Phương trình $ax - b = 0$ (với $a \\in \\{1; 2; 3; 4; 5; 6\\}$) có nghiệm duy nhất $x = \\dfrac{b}{a}$. \\
Nghiệm $x$ là số nguyên khi và chỉ khi $b$ chia hết cho $a$. Với $b \\in \\{1; 2; \\dots; %s\\}$: \\
- Với $a = 1$: có $%s$ giá trị của $b$; với $a = 2$: có $%s$ giá trị của $b$; \\
- Với $a = 3$: có $%s$ giá trị của $b$; với $a = 4$: có $%s$ giá trị của $b$; \\
- Với $a = 5$: có $%s$ giá trị của $b$; với $a = 6$: có $%s$ giá trị của $b$. \\
Tổng cộng có $%s + %s + %s + %s + %s + %s = %s$ kết quả thuận lợi.'''
                   % (b_max, counts[0], counts[1], counts[2], counts[3], counts[4], counts[5],
                      counts[0], counts[1], counts[2], counts[3], counts[4], counts[5], kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
