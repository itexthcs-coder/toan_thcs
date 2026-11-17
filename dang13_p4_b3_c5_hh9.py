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


def bt_dang13_p4_b3_c5_hh9(self):
    # Dạng 13: Ứng dụng tính chu vi biên tưới và diện tích phần cỏ không được tưới bởi vòi phun tự động
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(4, 10)
        dai = 2 * r
        l_bien = 2 * Rational(90, 180) * sp.pi * r
        l_bien_val = f"{float(Rational(90, 180) * r) * 3.14 * 2:.2f}".replace('.', ',')
        S_bai = dai * r
        S_tuoi_heso = 2 * Rational(90, 360) * r**2
        S_tuoi_val = f"{float(S_tuoi_heso) * 3.14:.2f}".replace('.', ',')
        S_khong = S_bai - float(S_tuoi_heso) * 3.14
        S_khong_val = f"{S_khong:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bãi cỏ hình chữ nhật $ABCD$ có chiều dài $AB = %s\\text{ m}$, chiều rộng $AD = %s\\text{ m}$. Người ta lắp hai vòi phun nước tự động cố định tại hai góc $A$ và $B$, mỗi vòi có tầm phun xa tối đa $%s\\text{ m}$ và chỉ quay trong phạm vi góc $90^\\circ$ hướng vào bên trong bãi cỏ.\\\\
a) Tính tổng chiều dài đường biên dạng cung tròn của vùng cỏ được tưới nước.\\\\
b) Tính diện tích phần cỏ trong bãi không nhận được nước trực tiếp từ hai vòi phun này (lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[green!15] (0,0) rectangle (3.6,1.8);
\\fill[cyan!25] (0,0) -- (1.8,0) arc (0:90:1.8) -- cycle;
\\fill[cyan!25] (3.6,0) -- (3.6,1.8) arc (90:180:1.8) -- cycle;
\\draw[thick] (0,0) rectangle (3.6,1.8);
\\draw[thick, blue!75!black] (1.8,0) arc (0:90:1.8);
\\draw[thick, blue!75!black] (3.6,1.8) arc (90:180:1.8);
\\node[below left] at (0,0) {$A$};
\\node[below right] at (3.6,0) {$B$};
\\node[above right] at (3.6,1.8) {$C$};
\\node[above left] at (0,1.8) {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(dai), latex(r), latex(r)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $AB = %s\\text{ m} = 2 \\cdot %s\\text{ m}$ nên hai vùng cỏ được tưới nước là hai hình quạt tròn bằng nhau (mỗi hình có bán kính $R = %s\\text{ m}$, góc ở tâm $90^\\circ$) và tiếp xúc nhau tại trung điểm của $AB$.\\\\
Tổng chiều dài đường biên dạng cung tròn của vùng cỏ được tưới nước là:
$$l = 2 \\cdot \\dfrac{90}{180}\\pi \\cdot %s = %s \\approx %s\\text{ (m)}.$$
\\item Diện tích bãi cỏ hình chữ nhật $ABCD$ là:
$$S_{ABCD} = AB \\cdot AD = %s \\cdot %s = %s\\text{ (m}^2\\text{)}.$$
Tổng diện tích vùng cỏ được hai vòi phun tưới nước là:
$$S_{\\text{tưới}} = 2 \\cdot \\dfrac{90}{360}\\pi \\cdot %s^2 = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (m}^2\\text{)}.$$
Vậy diện tích phần cỏ không nhận được nước trực tiếp từ hai vòi phun là:
$$S = S_{ABCD} - S_{\\text{tưới}} \\approx %s - %s = %s\\text{ (m}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(dai), latex(r), latex(r),
                      latex(r), latex(l_bien), l_bien_val,
                      latex(dai), latex(r), latex(S_bai),
                      latex(r), latex(S_tuoi_heso), latex(S_tuoi_heso), S_tuoi_val,
                      latex(S_bai), S_tuoi_val, S_khong_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
