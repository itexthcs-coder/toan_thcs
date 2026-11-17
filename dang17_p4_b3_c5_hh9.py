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


def bt_dang17_p4_b3_c5_hh9(self):
    # Dạng 17: Ứng dụng tính diện tích vùng ghi âm và quãng đường đầu kim trượt trên đĩa than (vinyl)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([14.0, 14.5])
        r = random.choice([5.0, 5.5, 6.0])
        tocdo, thoigian = random.choice([(33, 20), (33, 40), (45, 20), (45, 40)])
        R_str = str(R).replace('.', ',')
        r_str = str(r).replace('.', ',')
        S_heso = round(R**2 - r**2, 2)
        S_heso_str = str(S_heso).replace('.', ',')
        S_val = f"{S_heso * 3.14:.2f}".replace('.', ',')
        so_vong = (tocdo * thoigian) // 60
        s_cm_heso = round(so_vong * 2 * R, 1)
        s_cm_heso_str = str(s_cm_heso).replace('.', ',')
        s_cm_val = f"{s_cm_heso * math.pi:.1f}".replace('.', ',')
        s_m_val = f"{(s_cm_heso * math.pi) / 100.0:.1f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc đĩa than (vinyl) có đường kính $30\\text{ cm}$. Vùng chứa các rãnh ghi âm trên một mặt đĩa là một hình vành khuyên có bán kính ngoài $R = %s\\text{ cm}$ và bán kính trong $r = %s\\text{ cm}$.\\\\
a) Tính diện tích vùng chứa rãnh ghi âm trên một mặt đĩa (lấy $\\pi \\approx 3,14$).\\\\
b) Khi phát nhạc, đĩa quay đều với tốc độ $%s\\text{ vòng/phút}$. Trong khoảng thời gian $%s\\text{ giây}$ đầu tiên khi đầu kim đặt ở rãnh ngoài cùng (cách tâm $%s\\text{ cm}$), đầu kim đã trượt trên rãnh đĩa một quãng đường dài bao nhiêu mét (làm tròn đến hàng phần chục)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[black!80, even odd rule] (0,0) circle (1.8) (0,0) circle (0.68);
\\fill[red!70!black, even odd rule] (0,0) circle (0.68) (0,0) circle (0.12);
\\draw[white!40] (0,0) circle (1.45) (0,0) circle (1.1);
\\draw[dashed, white] (0,0) -- (30:1.8) (0,0) -- (-30:0.68);
\\fill[white] (0,0) circle (1.2pt);
\\end{tikzpicture}
\\end{center}'''
                         % (R_str, r_str, latex(tocdo), latex(thoigian), R_str))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích vùng chứa rãnh ghi âm trên một mặt đĩa (hình vành khuyên bán kính ngoài $R = %s\\text{ cm}$ và bán kính trong $r = %s\\text{ cm}$) là:
$$S_v = \\pi (R^2 - r^2) = \\pi (%s^2 - %s^2) = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (cm}^2\\text{)}.$$
\\item Đổi $%s\\text{ giây} = \\dfrac{%s}{60}\\text{ phút}$.\\\\
Số vòng đĩa quay được trong $%s\\text{ giây}$ là:
$$%s \\cdot \\dfrac{%s}{60} = %s\\text{ (vòng)}.$$
Chu vi của rãnh ngoài cùng bán kính $R = %s\\text{ cm}$ là:
$$C = 2\\pi R = 2\\pi \\cdot %s = %s\\pi\\text{ (cm)}.$$
Quãng đường đầu kim trượt được trên rãnh đĩa là:
$$s = %s \\cdot %s\\pi = %s\\pi \\approx %s\\text{ (cm)} \\approx %s\\text{ (m)}.$$
\\end{enumEX}'''
                   % (R_str, r_str, R_str, r_str, S_heso_str, S_heso_str, S_val,
                      latex(thoigian), latex(thoigian), latex(thoigian),
                      latex(tocdo), latex(thoigian), latex(so_vong),
                      R_str, R_str, str(round(2*R, 1)).replace('.', ','),
                      latex(so_vong), str(round(2*R, 1)).replace('.', ','), s_cm_heso_str, s_cm_val, s_m_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
