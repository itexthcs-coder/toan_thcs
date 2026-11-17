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


def bt_dang2_p4_b3_c5_hh9(self):
    # Dạng 2: Tính chu vi và diện tích hình "chiếc lá" tạo bởi hai cung tròn trong hình vuông
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(2, 10)
        P_la = 2 * Rational(90, 180) * sp.pi * a
        S_quat = Rational(90, 360) * sp.pi * a**2
        S_tamgiac = Rational(1, 2) * a**2
        S_nua = S_quat - S_tamgiac
        S_la = 2 * S_nua
        S_la_val = f"{float(S_la.evalf()):.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $ABCD$ có cạnh bằng $%s\\text{ cm}$. Vẽ hai cung tròn tâm $A$ và tâm $C$ cùng có bán kính $%s\\text{ cm}$ nằm bên trong hình vuông, cắt nhau tại $B$ và $D$ tạo thành một hình \\lq\\lq chiếc lá\\rq\\rq{} giới hạn bởi hai cung tròn $BD$.\\\\
a) Tính chu vi của hình \\lq\\lq chiếc lá\\rq\\rq{} đó.\\\\
b) Tính diện tích của hình \\lq\\lq chiếc lá\\rq\\rq{} đó (làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[green!22] (0,2.6) arc (90:0:2.6) arc (-90:-180:2.6) -- cycle;
\\draw[thick] (0,0) rectangle (2.6,2.6);
\\draw[thick, blue!70!black] (0,2.6) arc (90:0:2.6);
\\draw[thick, blue!70!black] (2.6,0) arc (-90:-180:2.6);
\\draw[dashed] (0,2.6) -- (2.6,0);
\\node[below left] at (0,0) {$A$};
\\node[below right] at (2.6,0) {$B$};
\\node[above right] at (2.6,2.6) {$C$};
\\node[above left] at (0,2.6) {$D$};
\\node[below] at (1.3,0) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(a), latex(a), latex(a)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Mỗi cung tròn $BD$ thuộc đường tròn bán kính $R = %s\\text{ cm}$ và bị chắn bởi góc ở tâm vuông ($90^\\circ$).\\\\
Độ dài một cung tròn $BD$ là:
$$l = \\dfrac{90}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Chu vi của hình \\lq\\lq chiếc lá\\rq\\rq{} bằng tổng độ dài hai cung tròn $BD$:
$$P = 2l = %s\\text{ (cm)}.$$
\\item Đường chéo $BD$ chia hình \\lq\\lq chiếc lá\\rq\\rq{} thành hai hình viên phân bằng nhau, mỗi hình ứng với cung $90^\\circ$ của đường tròn bán kính $R = %s\\text{ cm}$.\\\\
Diện tích hình quạt tròn $ABD$ là:
$$S_q = \\dfrac{90}{360}\\pi \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}.$$
Diện tích tam giác vuông $ABD$ là:
$$S_{\\Delta ABD} = \\dfrac{1}{2} AB \\cdot AD = \\dfrac{1}{2} \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}.$$
Diện tích cả hình \\lq\\lq chiếc lá\\rq\\rq{} là:
$$S = 2(S_q - S_{\\Delta ABD}) = %s \\approx %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(a), latex(a), latex(P_la / 2), latex(P_la),
                      latex(a), latex(a), latex(S_quat),
                      latex(a), latex(S_tamgiac),
                      latex(S_la), S_la_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
