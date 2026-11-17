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


def bt_dang6_p4_b3_c5_hh9(self):
    # Dạng 6: Tính độ dài nửa đường tròn và tổng diện tích hai hình "trăng khuyết" (Hippocrates)
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)
    k = randint(1, 3)
    if dang == '1':
        AB, AC, BC = 3*k, 4*k, 5*k
    elif dang == '2':
        AB, AC, BC = 5*k, 12*k, 13*k
    else:
        AB, AC, BC = 8*k, 15*k, 17*k

    l1 = Rational(AB, 2) * sp.pi
    l2 = Rational(AC, 2) * sp.pi
    l_tong = l1 + l2
    l3 = Rational(BC, 2) * sp.pi
    hieu_l = l_tong - l3
    S_tg = Rational(1, 2) * AB * AC

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Vẽ hai nửa đường tròn đường kính $AB$ và $AC$ hướng ra phía ngoài tam giác $ABC$, đồng thời vẽ nửa đường tròn đường kính $BC$ đi qua đỉnh $A$.\\\\
a) Tính tổng độ dài của hai nửa đường tròn đường kính $AB$ và $AC$, so sánh với độ dài nửa đường tròn đường kính $BC$.\\\\
b) Tính tổng diện tích của hai hình \\lq\\lq trăng khuyết\\rq\\rq{} (phần nằm trong hai nửa đường tròn đường kính $AB, AC$ nhưng nằm ngoài nửa đường tròn đường kính $BC$).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\coordinate (B) at (-2,0);
\\coordinate (C) at (2,0);
\\coordinate (A) at (-0.56,1.92);
\\fill[yellow!35] (B) arc (180:106.26:2) arc (53.13:233.13:1.2) -- cycle;
\\fill[yellow!35] (A) arc (106.26:0:2) arc (-36.87:143.13:1.6) -- cycle;
\\draw[thick] (B) -- (C) -- (A) -- cycle;
\\draw[thick] (C) arc (0:180:2);
\\draw[thick] (A) arc (53.13:233.13:1.2);
\\draw[thick] (C) arc (-36.87:143.13:1.6);
\\node[left] at (B) {$B$};
\\node[right] at (C) {$C$};
\\node[above] at (A) {$A$};
\\end{tikzpicture}
\\end{center}'''
                     % (latex(AB), latex(AC)))

    # Nội dung lời giải
    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Áp dụng định lí Pythagore trong $\\Delta ABC$ vuông tại $A$, ta có:
$$BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}.$$
Tổng độ dài của hai nửa đường tròn đường kính $AB$ và $AC$ là:
$$l_1 + l_2 = \\dfrac{\\pi \\cdot AB}{2} + \\dfrac{\\pi \\cdot AC}{2} = \\dfrac{\\pi \\cdot %s}{2} + \\dfrac{\\pi \\cdot %s}{2} = %s\\text{ (cm)}.$$
Độ dài nửa đường tròn đường kính $BC$ là:
$$l_3 = \\dfrac{\\pi \\cdot BC}{2} = \\dfrac{\\pi \\cdot %s}{2} = %s\\text{ (cm)}.$$
Vì $%s > %s$ nên tổng độ dài hai nửa đường tròn nhỏ lớn hơn độ dài nửa đường tròn lớn một đoạn bằng $%s\\text{ cm}$.
\\item Gọi $S_1, S_2, S_3$ lần lượt là diện tích của các nửa hình tròn đường kính $AB, AC, BC$.\\\\
Tổng diện tích hai hình \\lq\\lq trăng khuyết\\rq\\rq{} bằng tổng diện tích hai nửa hình tròn nhỏ cộng với diện tích $\\Delta ABC$ rồi trừ đi diện tích nửa hình tròn lớn:
$$S = S_1 + S_2 + S_{\\Delta ABC} - S_3 = \\dfrac{\\pi}{8}(AB^2 + AC^2 - BC^2) + \\dfrac{1}{2}AB \\cdot AC.$$
Vì $\\Delta ABC$ vuông tại $A$ nên $AB^2 + AC^2 = BC^2$, suy ra $AB^2 + AC^2 - BC^2 = 0$. Do đó:
$$S = 0 + \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
               % (latex(AB), latex(AC), latex(BC),
                  latex(AB), latex(AC), latex(l_tong),
                  latex(BC), latex(l3),
                  latex(l_tong), latex(l3), latex(hieu_l),
                  latex(AB), latex(AC), latex(S_tg)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
