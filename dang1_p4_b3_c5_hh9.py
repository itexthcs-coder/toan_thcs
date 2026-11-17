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


def bt_dang1_p4_b3_c5_hh9(self):
    # Dạng 1: Tính độ dài cung tròn và diện tích phần giới hạn bởi hai tiếp tuyến và cung nhỏ
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = randint(3, 10)
        OM = 2 * R
        MA_sym = R * sqrt(3)
        l_cung = Rational(120, 180) * sp.pi * R
        S_tu_giac = R * MA_sym
        S_quat = Rational(120, 360) * sp.pi * R**2
        S_hinh = S_tu_giac - S_quat

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$. Từ điểm $M$ nằm ngoài đường tròn sao cho $OM = %s\\text{ cm}$, kẻ hai tiếp tuyến $MA, MB$ tới $(O)$ ($A, B$ là các tiếp điểm).\\\\
a) Tính số đo góc ở tâm $\\widehat{AOB}$ và độ dài cung nhỏ $AB$.\\\\
b) Tính diện tích phần hình phẳng giới hạn bởi hai đoạn thẳng $MA, MB$ và cung nhỏ $AB$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[cyan!18] (60:1.6) -- (3.2,0) -- (-60:1.6) arc (-60:60:1.6) -- cycle;
\\draw[thick] (0,0) circle (1.6);
\\draw[thick] (3.2,0) -- (60:1.6) (3.2,0) -- (-60:1.6);
\\draw[dashed] (0,0) -- (60:1.6) (0,0) -- (-60:1.6) (0,0) -- (3.2,0);
\\fill (0,0) circle (1.5pt) node[left] {$O$};
\\fill (3.2,0) circle (1.5pt) node[right] {$M$};
\\fill (60:1.6) circle (1.5pt) node[above] {$A$};
\\fill (-60:1.6) circle (1.5pt) node[below] {$B$};
\\node at (0.7,0.4) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(OM), latex(R)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra $\\Delta OAM$ vuông tại $A$.\\\\
Ta có $\\cos \\widehat{AOM} = \\dfrac{OA}{OM} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{AOM} = 60^\\circ$.\\\\
Theo tính chất hai tiếp tuyến cắt nhau, $OM$ là tia phân giác của $\\widehat{AOB}$, do đó:
$$\\widehat{AOB} = 2\\widehat{AOM} = 2 \\cdot 60^\\circ = 120^\\circ.$$
Cung nhỏ $AB$ bị chắn bởi góc ở tâm $\\widehat{AOB} = 120^\\circ$ nên có độ dài là:
$$l = \\dfrac{120}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
\\item Áp dụng định lí Pythagore trong $\\Delta OAM$ vuông tại $A$, ta có:
$$MA = \\sqrt{OM^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Diện tích tứ giác $OAMB$ bằng hai lần diện tích $\\Delta OAM$:
$$S_{OAMB} = 2 \\cdot \\dfrac{1}{2} OA \\cdot MA = %s \\cdot %s = %s\\text{ (cm}^2\\text{)}.$$
Diện tích hình quạt tròn $OAB$ ứng với cung $120^\\circ$ là:
$$S_q = \\dfrac{120}{360}\\pi \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}.$$
Vậy diện tích phần hình phẳng cần tìm là:
$$S = S_{OAMB} - S_q = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R), latex(OM),
                      latex(R), latex(l_cung),
                      latex(OM), latex(R), latex(MA_sym),
                      latex(R), latex(MA_sym), latex(S_tu_giac),
                      latex(R), latex(S_quat),
                      latex(S_hinh)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
