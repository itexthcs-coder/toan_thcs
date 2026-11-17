# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
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
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import qrcode
import glob
import base64
from datetime import datetime, timedelta
from sympy import symbols, solve, Lt
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sympy.abc import x, y, z, t
from math import degrees
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps


def bt_dang15_p4_b3_c5_hh9(self):
    # Dạng 15: Ứng dụng tính độ dài vòng chạy, khoảng cách xuất phát so le và diện tích làn chạy điền kinh
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        L_thang = random.choice([80, 85, 90, 100])
        R1 = random.choice([34, 35, 36, 38])
        w = 1.2
        lan_k = random.choice([3, 4, 5])
        Rk = R1 + (lan_k - 1) * w
        R1_ngoai = R1 + w
        C1_cong = 2 * R1
        C1_val = f"{2 * L_thang + 2 * math.pi * R1:.2f}".replace('.', ',')
        Ck_cong = round(2 * Rk, 1)
        Ck_cong_str = str(Ck_cong).replace('.', ',')
        Ck_val = f"{2 * L_thang + 2 * math.pi * Rk:.2f}".replace('.', ',')
        delta_cong = round(2 * (Rk - R1), 1)
        delta_cong_str = str(delta_cong).replace('.', ',')
        delta_val = f"{2 * math.pi * (Rk - R1):.2f}".replace('.', ',')
        S_thang = round(2 * L_thang * w, 1)
        S_vanh_heso = round(R1_ngoai**2 - R1**2, 2)
        S_vanh_heso_str = str(S_vanh_heso).replace('.', ',')
        S_tong_val = f"{S_thang + S_vanh_heso * 3.14:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một sân vận động có đường chạy gồm hai đoạn thẳng song song dài $%s\\text{ m}$ và hai đầu là hai nửa đường tròn đồng tâm. Làn chạy số $1$ (trong cùng) có bán kính mép trong là $R_1 = %s\\text{ m}$, mỗi làn chạy rộng $1,2\\text{ m}$.\\\\
a) Tính độ dài một vòng chạy dọc theo mép trong của làn số $1$ và làn số $%s$ (làm tròn đến hàng phần trăm của mét).\\\\
b) Để hai vận động viên ở làn $1$ và làn $%s$ cùng chạy đúng một quãng đường bằng độ dài một vòng làn $1$ và về đích tại cùng một vạch thẳng, vận động viên ở làn $%s$ phải xuất phát đứng trước (so le) vận động viên ở làn $1$ bao nhiêu mét? Tính diện tích bề mặt của riêng làn chạy số $1$ (lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.65, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[orange!25] (-1.6,-1.1) -- (1.6,-1.1) arc (-90:90:1.1) -- (-1.6,1.1) arc (90:270:1.1) -- cycle;
\\fill[green!20] (-1.6,-0.8) -- (1.6,-0.8) arc (-90:90:0.8) -- (-1.6,0.8) arc (90:270:0.8) -- cycle;
\\draw[thick] (-1.6,-0.8) -- (1.6,-0.8) arc (-90:90:0.8) -- (-1.6,0.8) arc (90:270:0.8) -- cycle;
\\draw[thick] (-1.6,-1.1) -- (1.6,-1.1) arc (-90:90:1.1) -- (-1.6,1.1) arc (90:270:1.1) -- cycle;
\\draw[thick] (-1.6,-1.4) -- (1.6,-1.4) arc (-90:90:1.4) -- (-1.6,1.4) arc (90:270:1.4) -- cycle;
\\draw[dashed] (-1.6,-0.8) -- (-1.6,0.8) (1.6,-0.8) -- (1.6,0.8);
\\node at (0,0) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(L_thang), latex(R1), latex(lan_k), latex(lan_k), latex(lan_k), latex(L_thang)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Độ dài một vòng chạy dọc theo mép trong của làn số $1$ gồm hai đoạn thẳng và một đường tròn bán kính $R_1 = %s\\text{ m}$:
$$C_1 = 2 \\cdot %s + 2\\pi \\cdot %s = %s + %s\\pi \\approx %s\\text{ (m)}.$$
Bán kính mép trong của làn số $%s$ là:
$$R_{%s} = %s + %s \\cdot 1,2 = %s\\text{ (m)}.$$
Độ dài một vòng chạy dọc theo mép trong của làn số $%s$ là:
$$C_{%s} = 2 \\cdot %s + 2\\pi \\cdot %s = %s + %s\\pi \\approx %s\\text{ (m)}.$$
\\item Khoảng cách vận động viên ở làn $%s$ phải xuất phát đứng trước vận động viên ở làn $1$ đúng bằng hiệu độ dài hai vòng chạy:
$$\\Delta C = C_{%s} - C_1 = %s\\pi \\approx %s\\text{ (m)}.$$
Bề mặt của riêng làn chạy số $1$ gồm hai hình chữ nhật kích thước $%s\\text{ m} \\times 1,2\\text{ m}$ và một hình vành khuyên có bán kính ngoài $R_2 = %s + 1,2 = %s\\text{ (m)}$ và bán kính trong $R_1 = %s\\text{ m}$.\\\\
Diện tích bề mặt của riêng làn chạy số $1$ là:
$$S = 2 \\cdot (%s \\cdot 1,2) + \\pi (%s^2 - %s^2) = %s + %s\\pi \\approx %s + %s \\cdot 3,14 = %s\\text{ (m}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R1), latex(L_thang), latex(R1), latex(2*L_thang), latex(C1_cong), C1_val,
                      latex(lan_k), latex(lan_k), latex(R1), latex(lan_k - 1), str(round(Rk, 1)).replace('.', ','),
                      latex(lan_k), latex(lan_k), latex(L_thang), str(round(Rk, 1)).replace('.', ','), latex(2*L_thang), Ck_cong_str, Ck_val,
                      latex(lan_k), latex(lan_k), delta_cong_str, delta_val,
                      latex(L_thang), latex(R1), str(round(R1_ngoai, 1)).replace('.', ','), latex(R1),
                      latex(L_thang), str(round(R1_ngoai, 1)).replace('.', ','), latex(R1), str(S_thang).replace('.', ','), S_vanh_heso_str, str(S_thang).replace('.', ','), S_vanh_heso_str, S_tong_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
