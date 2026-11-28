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

def bt_dang19_p4_b1_c8_ds8(self):
    # Dạng 19: Hình học trực quan - Tính chất đường chéo và đối xứng của đa giác
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        shapes = [
            "Tam giác đều",
            "Hình vuông",
            "Hình chữ nhật (không phải hình vuông)",
            "Hình thoi (không phải hình vuông)",
            "Hình bình hành",
            "Hình thang cân"
        ]
        loai = random.choice(['cheo_bang_nhau_tam_dx', 'cheo_vuong_goc'])
        if loai == 'cheo_bang_nhau_tam_dx':
            dk_text = "Hình được chọn là tứ giác có hai đường chéo bằng nhau đồng thời có tâm đối xứng"
            tl = ["Hình vuông", "Hình chữ nhật (không phải hình vuông)"]
            giai_thich = "Các tứ giác có hai đường chéo bằng nhau gồm: hình vuông, hình chữ nhật và hình thang cân. Tuy nhiên, hình thang cân không có tâm đối xứng; chỉ có hình vuông và hình chữ nhật có tâm đối xứng (giao điểm hai đường chéo)."
        else:
            dk_text = "Hình được chọn là tứ giác có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường"
            tl = ["Hình vuông", "Hình thoi (không phải hình vuông)"]
            giai_thich = "Trong các tứ giác đã cho, chỉ có hình vuông và hình thoi có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường."
            
        noidungcauhoi = ('''Cho một hộp đựng $6$ tấm bìa có dạng các hình học sau: %s. Lấy ngẫu nhiên một tấm bìa từ trong hộp.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên.\\
b) Xác định các kết quả thuận lợi cho biến cố $U$: ``%s''.'''
                         % (', '.join(shapes), dk_text))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động lấy ngẫu nhiên một tấm bìa là: %s (có $6$ kết quả có thể).
\\item %s\\
Vậy các kết quả thuận lợi cho biến cố $U$ là: %s (có $2$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (', '.join(shapes), giai_thich, '; '.join(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
