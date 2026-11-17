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


def bt_dang4_p4_b3_c5_hh9(self):
    # Dạng 4: Tính độ dài cung tròn và lập công thức diện tích hình viên phân theo bán kính R
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)
    if dang == '1':
        day_str = "R"
        goc_nua = 30
        goc_tam = 60
        sin_str = "\\dfrac{1}{2}"
        OH_str = "\\dfrac{R\\sqrt{3}}{2}"
        S_tg_heso = Rational(1, 4) * sqrt(3)
    elif dang == '2':
        day_str = "R\\sqrt{2}"
        goc_nua = 45
        goc_tam = 90
        sin_str = "\\dfrac{\\sqrt{2}}{2}"
        OH_str = "\\dfrac{R\\sqrt{2}}{2}"
        S_tg_heso = Rational(1, 2)
    else:
        day_str = "R\\sqrt{3}"
        goc_nua = 60
        goc_tam = 120
        sin_str = "\\dfrac{\\sqrt{3}}{2}"
        OH_str = "\\dfrac{R}{2}"
        S_tg_heso = Rational(1, 4) * sqrt(3)

    goc_lon = 360 - goc_tam
    l_nho_heso = Rational(goc_tam, 180) * sp.pi
    l_lon_heso = Rational(goc_lon, 180) * sp.pi
    S_q_heso = Rational(goc_tam, 360) * sp.pi
    S_vp_heso = S_q_heso - S_tg_heso
    ang_A = -90 - goc_nua
    ang_B = -90 + goc_nua
    y_H = round(-1.8 * math.cos(math.radians(goc_nua)), 3)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho đường tròn $(O; R)$ và dây cung $AB = %s$.\\\\
a) Tính độ dài cung nhỏ $AB$ và cung lớn $AB$ theo $R$.\\\\
b) Lập công thức tính diện tích hình viên phân giới hạn bởi dây $AB$ và cung nhỏ $AB$ theo $R$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[purple!20] (%s:1.8) -- (%s:1.8) arc (%s:%s:1.8) -- cycle;
\\draw[thick] (0,0) circle (1.8);
\\draw[thick] (%s:1.8) -- (%s:1.8);
\\draw[dashed] (0,0) -- (%s:1.8) (0,0) -- (%s:1.8) (0,0) -- (0,%s);
\\fill (0,0) circle (1.5pt) node[above] {$O$};
\\fill (%s:1.8) circle (1.5pt) node[left] {$A$};
\\fill (%s:1.8) circle (1.5pt) node[right] {$B$};
\\fill (0,%s) circle (1.2pt) node[below right] {$H$};
\\end{tikzpicture}
\\end{center}'''
                     % (day_str,
                        ang_A, ang_B, ang_B, ang_A,
                        ang_A, ang_B,
                        ang_A, ang_B, y_H,
                        ang_A, ang_B, y_H))

    # Nội dung lời giải
    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Kẻ $OH \\perp AB$ tại $H$. Vì đường kính vuông góc với dây thì đi qua trung điểm của dây đó nên $AH = HB = \\dfrac{AB}{2} = \\dfrac{%s}{2}$.\\\\
Xét $\\Delta OAH$ vuông tại $H$, ta có:
$$\\sin \\widehat{AOH} = \\dfrac{AH}{OA} = %s \\Rightarrow \\widehat{AOH} = %s^\\circ.$$
Vì $\\Delta OAB$ cân tại $O$ có $OH$ là đường cao nên $OH$ đồng thời là tia phân giác của $\\widehat{AOB}$, suy ra:
$$\\widehat{AOB} = 2\\widehat{AOH} = %s^\\circ.$$
Vậy số đo cung nhỏ $AB$ là $%s^\\circ$ và số đo cung lớn $AB$ là $360^\\circ - %s^\\circ = %s^\\circ$.\\\\
Độ dài cung nhỏ $AB$ là:
$$l_1 = \\dfrac{%s}{180}\\pi R = %s R.$$
Độ dài cung lớn $AB$ là:
$$l_2 = \\dfrac{%s}{180}\\pi R = %s R.$$
\\item Áp dụng định lí Pythagore trong $\\Delta OAH$ vuông tại $H$, ta tính được $OH = %s$.\\\\
Diện tích $\\Delta OAB$ là:
$$S_{\\Delta OAB} = \\dfrac{1}{2} AB \\cdot OH = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s R^2.$$
Diện tích hình quạt tròn $OAB$ ứng với cung nhỏ $AB$ là:
$$S_q = \\dfrac{%s}{360}\\pi R^2 = %s R^2.$$
Vậy diện tích hình viên phân cần tìm là:
$$S = S_q - S_{\\Delta OAB} = R^2\\left(%s\\right).$$
\\end{enumEX}'''
               % (day_str, sin_str, latex(goc_nua), latex(goc_tam),
                  latex(goc_tam), latex(goc_tam), latex(goc_lon),
                  latex(goc_tam), latex(l_nho_heso),
                  latex(goc_lon), latex(l_lon_heso),
                  OH_str, day_str, OH_str, latex(S_tg_heso),
                  latex(goc_tam), latex(S_q_heso), latex(S_vp_heso)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
