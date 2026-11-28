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

def bt_dang18_p4_b1_c8_ds8(self):
    # Dạng 18: Khoa học tự nhiên - Phân loại hóa chất
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        substances = [
            "Nước cất ($\\mathrm{H_2O}$)",
            "Dung dịch axit sunfuric ($\\mathrm{H_2SO_4}$)",
            "Dung dịch natri hiđroxit ($\\mathrm{NaOH}$)",
            "Muối ăn rắn ($\\mathrm{NaCl}$)",
            "Rượu etylic ($\\mathrm{C_2H_5OH}$)",
            "Khí oxi ($\\mathrm{O_2}$)"
        ]
        loai = random.choice(['doi_mau_quy', 'khong_doi_mau'])
        if loai == 'doi_mau_quy':
            dk_text = "Chất trong lọ ở thể lỏng ở điều kiện thường và làm đổi màu giấy quỳ tím"
            tl = ["Dung dịch axit sunfuric ($\\mathrm{H_2SO_4}$)", "Dung dịch natri hiđroxit ($\\mathrm{NaOH}$)"]
            giai_thich = "Ở điều kiện thường, các chất ở thể lỏng gồm: nước cất, dung dịch $\\mathrm{H_2SO_4}$, dung dịch $\\mathrm{NaOH}$ và rượu etylic. Trong đó, dung dịch axit $\\mathrm{H_2SO_4}$ làm quỳ tím hóa đỏ và dung dịch bazơ $\\mathrm{NaOH}$ làm quỳ tím hóa xanh."
        else:
            dk_text = "Chất trong lọ ở thể lỏng ở điều kiện thường nhưng không làm đổi màu giấy quỳ tím"
            tl = ["Nước cất ($\\mathrm{H_2O}$)", "Rượu etylic ($\\mathrm{C_2H_5OH}$)"]
            giai_thich = "Ở điều kiện thường, các chất ở thể lỏng gồm: nước cất, dung dịch $\\mathrm{H_2SO_4}$, dung dịch $\\mathrm{NaOH}$ và rượu etylic. Trong đó, nước cất và rượu etylic có môi trường trung tính nên không làm đổi màu giấy quỳ tím."
            
        noidungcauhoi = ('''Trên bàn thí nghiệm có $6$ lọ hóa chất mất nhãn đựng $6$ chất riêng biệt: %s. Giáo viên chọn ngẫu nhiên $1$ lọ để kiểm tra.\\
a) Hỏi có tất cả bao nhiêu kết quả có thể của hành động trên?\\
b) Xác định các kết quả thuận lợi cho biến cố $T$: ``%s''.'''
                         % (', '.join(substances), dk_text))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Có $6$ lọ hóa chất riêng biệt nên khi chọn ngẫu nhiên $1$ lọ thì có tất cả $6$ kết quả có thể.
\\item %s\\
Vậy các kết quả thuận lợi cho biến cố $T$ là: %s (có $2$ kết quả thuận lợi).
\\end{enumEX}'''
                   % (giai_thich, '; '.join(tl)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
