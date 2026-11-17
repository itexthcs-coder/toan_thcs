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


def bt_dang20_p4_b3_c5_hh9(self):
    # Dạng 20: Ứng dụng tính góc ôm cung tròn và tổng chiều dài dây đai truyền động hai bánh ròng rọc
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = random.choice([6, 8, 10, 12])
        k = random.choice([6, 8, 10, 12])
        R = r + k
        O1O2 = 2 * k
        AB_sym = k * sqrt(3)
        l_lon = Rational(240, 180) * sp.pi * R
        l_nho = Rational(120, 180) * sp.pi * r
        L_tong_sym = 2 * AB_sym + l_lon + l_nho
        L_tong_val = f"{float(L_tong_sym.evalf()):.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai bánh ròng rọc tròn tâm $O_1$ (bán kính $R_1 = %s\\text{ cm}$) và tâm $O_2$ (bán kính $R_2 = %s\\text{ cm}$) có khoảng cách hai tâm $O_1O_2 = %s\\text{ cm}$ được nối với nhau bằng một dây đai (dây curoa) không co dãn mắc căng theo hai tiếp tuyến chung ngoài $AB$ và $CD$ ($A, C \\in (O_1)$; $B, D \\in (O_2)$).\\\\
a) Tính số đo góc ở tâm của cung lớn $AC$ trên bánh ròng rọc lớn và cung nhỏ $BD$ trên bánh ròng rọc nhỏ mà dây đai ôm sát.\\\\
b) Tính tổng chiều dài của sợi dây đai đó (làm tròn đến hàng phần trăm của cm).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\draw[thick] (0,0) circle (1.5);
\\draw[thick] (3.0,0) circle (0.75);
\\draw[very thick, blue!75!black] (60:1.5) -- (3.375,0.65) arc (60:-60:0.75) -- (-60:1.5) arc (-60:-300:1.5);
\\draw[dashed] (0,0) -- (3.0,0) (0,0) -- (60:1.5) (0,0) -- (-60:1.5) (3.0,0) -- (3.375,0.65) (3.0,0) -- (3.375,-0.65);
\\fill (0,0) circle (1.5pt) node[left] {$O_1$};
\\fill (3.0,0) circle (1.5pt) node[right] {$O_2$};
\\fill (60:1.5) circle (1.5pt) node[above] {$A$};
\\fill (-60:1.5) circle (1.5pt) node[below] {$C$};
\\fill (3.375,0.65) circle (1.5pt) node[above] {$B$};
\\fill (3.375,-0.65) circle (1.5pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(r), latex(O1O2)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $AB$ là tiếp tuyến chung ngoài nên $O_1A \\perp AB$ và $O_2B \\perp AB$, suy ra $O_1A \\parallel O_2B$.\\\\
Kẻ $O_2H \\perp O_1A$ tại $H$, khi đó $O_2HBA$ là hình chữ nhật nên $AH = O_2B = %s\\text{ cm}$ và $O_1H = O_1A - AH = %s - %s = %s\\text{ (cm)}$.\\\\
Trong $\\Delta O_1HO_2$ vuông tại $H$, ta có:
$$\\cos \\widehat{HO_1O_2} = \\dfrac{O_1H}{O_1O_2} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{AO_1O_2} = 60^\\circ.$$
Do tính chất đối xứng qua đường nối tâm $O_1O_2$, góc ở tâm chắn cung nhỏ $AC$ là $\\widehat{AO_1C} = 2 \\cdot 60^\\circ = 120^\\circ$, suy ra số đo góc ở tâm của cung lớn $AC$ mà dây đai ôm sát trên ròng rọc lớn là:
$$360^\\circ - 120^\\circ = 240^\\circ.$$
Vì $O_1A \\parallel O_2B$ nên $\\widehat{BO_2O_1} = 180^\\circ - 60^\\circ = 120^\\circ$. Tương tự $\\widehat{DO_2O_1} = 120^\\circ$, suy ra góc ở tâm của cung nhỏ $BD$ mà dây đai ôm sát trên ròng rọc nhỏ là:
$$\\widehat{BO_2D} = 360^\\circ - 2 \\cdot 120^\\circ = 120^\\circ.$$
\\item Áp dụng định lí Pythagore trong $\\Delta O_1HO_2$ vuông tại $H$, ta có:
$$AB = CD = O_2H = \\sqrt{O_1O_2^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Độ dài cung lớn $AC$ trên bánh ròng rọc lớn là:
$$l_1 = \\dfrac{240}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Độ dài cung nhỏ $BD$ trên bánh ròng rọc nhỏ là:
$$l_2 = \\dfrac{120}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Vậy tổng chiều dài của sợi dây đai là:
$$L = 2AB + l_1 + l_2 = 2 \\cdot %s + %s + %s = %s \\approx %s\\text{ (cm)}.$$
\\end{enumEX}'''
                   % (latex(r), latex(R), latex(r), latex(k),
                      latex(k), latex(O1O2),
                      latex(O1O2), latex(k), latex(AB_sym),
                      latex(R), latex(l_lon),
                      latex(r), latex(l_nho),
                      latex(AB_sym), latex(l_lon), latex(l_nho), latex(L_tong_sym), L_tong_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
