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


def bt_dang12_p4_b3_c5_hh9(self):
    # Dạng 12: Ứng dụng tính chiều dài mép đường và diện tích mặt đường khúc cua cao tốc (hình vành khuyên)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        goc = random.choice([45, 60, 72, 90])
        R1 = random.choice([90, 120, 150, 180])
        w = random.choice([12, 15, 18])
        dongia = random.choice([400000, 450000, 500000])
        R2 = R1 + w
        l1_sym = Rational(goc, 180) * sp.pi * R1
        l2_sym = Rational(goc, 180) * sp.pi * R2
        l1_val = f"{float(l1_sym.evalf()):.2f}".replace('.', ',')
        l2_val = f"{float(l2_sym.evalf()):.2f}".replace('.', ',')
        S_heso = Rational(goc, 360) * (R2**2 - R1**2)
        S_approx = float(S_heso) * 3.14
        S_approx_str = f"{S_approx:.2f}".replace('.', ',')
        chiphi = int(round(S_approx * dongia))
        chiphi_str = f"{chiphi:,}".replace(',', '.')
        dongia_str = f"{dongia:,}".replace(',', '.')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khúc cua trên tuyến đường cao tốc có dạng một phần của hình vành khuyên ứng với góc ở tâm $%s^\\circ$. Bán kính mép đường phía trong là $R_1 = %s\\text{ m}$, bề rộng mặt đường là $%s\\text{ m}$.\\\\
a) Tính chiều dài mép đường phía trong và mép đường phía ngoài của khúc cua đó (làm tròn đến hàng phần trăm của mét).\\\\
b) Tính diện tích mặt đường của khúc cua và chi phí trải nhựa, biết đơn giá trải nhựa là $%s\\text{ đồng/m}^2$ (lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[gray!35] (15:2.2) -- (15:2.8) arc (15:75:2.8) -- (75:2.2) arc (75:15:2.2) -- cycle;
\\draw[thick] (15:2.2) arc (15:75:2.2);
\\draw[thick] (15:2.8) arc (15:75:2.8);
\\draw[dashed] (0,0) -- (15:2.8) (0,0) -- (75:2.8);
\\fill (0,0) circle (1.5pt) node[below left] {$O$};
\\node at (45:1.1) {$%s^\\circ$};
\\node[below right] at (15:1.3) {$R_1$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(goc), latex(R1), latex(w), dongia_str, latex(goc)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính mép đường phía ngoài của khúc cua là:
$$R_2 = R_1 + %s = %s + %s = %s\\text{ (m)}.$$
Chiều dài mép đường phía trong ứng với cung $%s^\\circ$ là:
$$l_1 = \\dfrac{%s}{180}\\pi \\cdot %s = %s \\approx %s\\text{ (m)}.$$
Chiều dài mép đường phía ngoài ứng với cung $%s^\\circ$ là:
$$l_2 = \\dfrac{%s}{180}\\pi \\cdot %s = %s \\approx %s\\text{ (m)}.$$
\\item Diện tích mặt đường của khúc cua (một phần hình vành khuyên ứng với góc ở tâm $%s^\\circ$) là:
$$S = \\dfrac{%s}{360}\\pi (R_2^2 - R_1^2) = \\dfrac{%s}{360}\\pi (%s^2 - %s^2) = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (m}^2\\text{)}.$$
Chi phí trải nhựa cho khúc cua là:
$$%s \\times %s = %s\\text{ (đồng)}.$$
\\end{enumEX}'''
                   % (latex(w), latex(R1), latex(w), latex(R2),
                      latex(goc), latex(goc), latex(R1), latex(l1_sym), l1_val,
                      latex(goc), latex(goc), latex(R2), latex(l2_sym), l2_val,
                      latex(goc), latex(goc), latex(goc), latex(R2), latex(R1), latex(S_heso), latex(S_heso), S_approx_str,
                      S_approx_str, dongia_str, chiphi_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
