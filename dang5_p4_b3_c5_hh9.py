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


def bt_dang5_p4_b3_c5_hh9(self):
    # Dạng 5: Tính diện tích hình vành khuyên khi biết dây cung của đường tròn lớn tiếp xúc với đường tròn nhỏ
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(3, 10)
        MN = 2 * k
        S_vanh = sp.pi * k**2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn đồng tâm $(O; R)$ và $(O; r)$ với $R > r$. Một dây cung $MN$ của đường tròn lớn $(O; R)$ tiếp xúc với đường tròn nhỏ $(O; r)$ tại điểm $H$. Biết độ dài dây $MN = %s\\text{ cm}$.\\\\
a) Chứng minh rằng diện tích của hình vành khuyên tạo bởi hai đường tròn trên chỉ phụ thuộc vào độ dài dây $MN$ mà không phụ thuộc vào giá trị cụ thể của $R$ và $r$.\\\\
b) Tính diện tích hình vành khuyên đó.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[teal!18, even odd rule] (0,0) circle (1.9) (0,0) circle (1.1);
\\draw[thick] (0,0) circle (1.9);
\\draw[thick] (0,0) circle (1.1);
\\draw[thick] (-1.549,-1.1) -- (1.549,-1.1);
\\draw[dashed] (0,0) -- (0,-1.1) (0,0) -- (-1.549,-1.1);
\\fill (0,0) circle (1.5pt) node[above] {$O$};
\\fill (-1.549,-1.1) circle (1.5pt) node[left] {$M$};
\\fill (1.549,-1.1) circle (1.5pt) node[right] {$N$};
\\fill (0,-1.1) circle (1.5pt) node[below] {$H$};
\\node[left] at (-0.8,-0.55) {$R$};
\\node[right] at (0,-0.55) {$r$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(MN)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì dây cung $MN$ tiếp xúc với đường tròn $(O; r)$ tại $H$ nên $OH \\perp MN$ và $OH = r$.\\\\
Xét đường tròn $(O; R)$, đường kính vuông góc với dây $MN$ tại $H$ nên đi qua trung điểm của $MN$, suy ra:
$$MH = \\dfrac{MN}{2}.$$
Áp dụng định lí Pythagore trong $\\Delta OMH$ vuông tại $H$, ta có:
$$OM^2 - OH^2 = MH^2 \\Rightarrow R^2 - r^2 = \\left(\\dfrac{MN}{2}\\right)^2 = \\dfrac{MN^2}{4}.$$
Do đó, diện tích hình vành khuyên tạo bởi hai đường tròn $(O; R)$ và $(O; r)$ là:
$$S_v = \\pi(R^2 - r^2) = \\dfrac{\\pi \\cdot MN^2}{4}.$$
Biểu thức này chỉ phụ thuộc vào độ dài dây $MN$ mà không phụ thuộc vào giá trị riêng lẻ của $R$ và $r$.
\\item Thay $MN = %s\\text{ cm}$ vào công thức trên, ta được diện tích hình vành khuyên là:
$$S_v = \\dfrac{\\pi \\cdot %s^2}{4} = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(MN), latex(MN), latex(S_vanh)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
