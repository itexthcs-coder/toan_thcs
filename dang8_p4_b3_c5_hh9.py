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


def bt_dang8_p4_b3_c5_hh9(self):
    # Dạng 8: Chia hình tròn thành hai phần diện tích bằng nhau và tính diện tích hình quạt vành khuyên
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([6, 8, 10, 12, 14, 16])
        goc = random.choice([45, 60, 72, 90, 120])
        r_sym = Rational(R, 2) * sqrt(2)
        S_tron = sp.pi * R**2
        S_vanh = Rational(1, 2) * S_tron
        S_phan = Rational(goc, 360) * S_vanh

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình tròn $(O; R)$ với $R = %s\\text{ cm}$. Người ta vẽ một đường tròn đồng tâm $(O; r)$ ($0 < r < %s$) chia hình tròn $(O; R)$ thành hai phần có diện tích bằng nhau: một hình tròn nhỏ bên trong và một hình vành khuyên bên ngoài.\\\\
a) Tính bán kính $r$ của đường tròn đồng tâm đó.\\\\
b) Trên hình vành khuyên vừa tạo thành, xét phần giới hạn bởi hai bán kính $OA, OB$ của $(O; R)$ tạo với nhau góc $\\widehat{AOB} = %s^\\circ$. Tính diện tích phần hình vành khuyên bị giới hạn này.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[orange!25] (0:1.34) -- (0:1.9) arc (0:72:1.9) -- (72:1.34) arc (72:0:1.34) -- cycle;
\\draw[thick] (0,0) circle (1.9);
\\draw[thick] (0,0) circle (1.34);
\\draw[thick] (0,0) -- (0:1.9) (0,0) -- (72:1.9);
\\fill (0,0) circle (1.5pt) node[below left] {$O$};
\\fill (0:1.9) circle (1.5pt) node[right] {$A$};
\\fill (72:1.9) circle (1.5pt) node[above] {$B$};
\\node at (36:0.75) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(R), latex(goc), latex(goc)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích hình tròn $(O; R)$ là $S = \\pi R^2 = \\pi \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}$.\\\\
Vì đường tròn $(O; r)$ chia hình tròn $(O; R)$ thành hai phần có diện tích bằng nhau nên diện tích hình tròn $(O; r)$ bằng một nửa diện tích hình tròn $(O; R)$:
$$\\pi r^2 = \\dfrac{1}{2}\\pi R^2 \\Rightarrow r^2 = \\dfrac{%s^2}{2} \\Rightarrow r = \\dfrac{%s}{\\sqrt{2}} = %s\\text{ (cm)}.$$
\\item Diện tích của toàn bộ hình vành khuyên tạo bởi hai đường tròn $(O; R)$ và $(O; r)$ là:
$$S_v = \\dfrac{1}{2}S = %s\\text{ (cm}^2\\text{)}.$$
Phần hình vành khuyên giới hạn bởi hai bán kính $OA, OB$ ứng với góc ở tâm $\\widehat{AOB} = %s^\\circ$ chiếm tỉ số $\\dfrac{%s}{360}$ diện tích cả hình vành khuyên, do đó có diện tích là:
$$S_1 = \\dfrac{%s}{360} S_v = \\dfrac{%s}{360} \\cdot %s = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R), latex(S_tron),
                      latex(R), latex(R), latex(r_sym),
                      latex(S_vanh),
                      latex(goc), latex(goc),
                      latex(goc), latex(goc), latex(S_vanh), latex(S_phan)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
