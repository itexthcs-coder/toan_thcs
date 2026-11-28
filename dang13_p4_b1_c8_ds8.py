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

def bt_dang13_p4_b1_c8_ds8(self):
    # Dạng 13: Lịch trình giao thông và thời gian trong tuần
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        days_vn = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
        loai = random.choice(['T', 'S'])
        if loai == 'T':
            dk_str = "Ngày Hùng chọn không phải là ngày cuối tuần (Thứ Bảy, Chủ Nhật) và tên gọi trong tiếng Anh bắt đầu bằng chữ cái ``T''"
            tl = ["Thứ Ba", "Thứ Năm"]
            giai_thich = "Các ngày trong tuần không phải cuối tuần là từ Thứ Hai đến Thứ Sáu. Trong tiếng Anh, Thứ Ba là \\textit{Tuesday} và Thứ Năm là \\textit{Thursday} đều bắt đầu bằng chữ cái ``T''."
        else:
            dk_str = "Ngày Hùng chọn là ngày cuối tuần hoặc tên gọi trong tiếng Anh bắt đầu bằng chữ cái ``W''"
            tl = ["Thứ Tư", "Thứ Bảy", "Chủ Nhật"]
            giai_thich = "Các ngày cuối tuần là Thứ Bảy và Chủ Nhật; ngày có tên tiếng Anh bắt đầu bằng chữ ``W'' là Thứ Tư (\\textit{Wednesday})."
            
        noidungcauhoi = ('''Một tuyến xe buýt chạy tất cả các ngày trong tuần từ Thứ Hai đến Chủ Nhật. Bạn Hùng chọn ngẫu nhiên một ngày trong tuần để đi thăm bảo tàng.\\
a) Liệt kê tất cả các kết quả có thể của hành động trên. Có tất cả bao nhiêu kết quả có thể?\\
b) Xác định các kết quả thuận lợi cho biến cố $N$: ``%s''.'''
                         % (dk_str))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các kết quả có thể của hành động chọn một ngày trong tuần là: %s.\\
Có tất cả $7$ kết quả có thể.
\\item %s\\
Vậy các kết quả thuận lợi cho biến cố $N$ là: %s (có $%s$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (', '.join(days_vn), giai_thich, ', '.join(tl), len(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
