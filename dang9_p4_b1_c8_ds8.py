# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""

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

def bt_dang9_p4_b1_c8_ds8(self):
    # Dạng 9: Chọn cặp đối tượng không thứ tự từ một nhóm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nam = ['M_1', 'M_2', 'M_3']
        nu = ['N_1', 'N_2']
        all_p = nam + nu
        pairs = []
        for i in range(len(all_p)):
            for j in range(i + 1, len(all_p)):
                pairs.append((all_p[i], all_p[j]))
        str_pairs = '; '.join([f"({p1}, {p2})" for p1, p2 in pairs])
        
        loai = random.choice(['it_nhat_1_nu', 'ca_hai_nam'])
        if loai == 'it_nhat_1_nu':
            dk_text = "Trong $2$ bạn được chọn có ít nhất $1$ bạn nữ"
            tl = [f"({p1}, {p2})" for p1, p2 in pairs if (p1 in nu) or (p2 in nu)]
        else:
            dk_text = "Cả $2$ bạn được chọn đều là bạn nam"
            tl = [f"({p1}, {p2})" for p1, p2 in pairs if (p1 in nam) and (p2 in nam)]
        str_tl = '; '.join(tl)
        
        noidungcauhoi = ('''Trong một nhóm học tập có $3$ bạn nam (kí hiệu là $M_1, M_2, M_3$) và $2$ bạn nữ (kí hiệu là $N_1, N_2$). Giáo viên chọn ngẫu nhiên đồng thời $2$ bạn trong nhóm để lên bảng trực nhật.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên. Có tất cả bao nhiêu kết quả có thể?\\
b) Xác định các kết quả thuận lợi cho biến cố $I$: ``%s''.'''
                         % (dk_text))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì việc chọn $2$ bạn không phân biệt thứ tự nên tất cả các kết quả có thể của hành động trên là:\\
$%s$.\\
Có tất cả $%s$ kết quả có thể.
\\item Lọc từ danh sách các kết quả có thể ở câu a, các kết quả thuận lợi cho biến cố $I$ là:\\
$%s$ (có tất cả $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (str_pairs, len(pairs), str_tl, len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
