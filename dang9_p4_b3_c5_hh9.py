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


def bt_dang9_p4_b3_c5_hh9(self):
    # Dạng 9: Tính độ dài cung tròn và diện tích phần còn lại của hình thang vuông cắt bởi hai hình quạt tròn
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        h = randint(3, 6)
        AB = randint(4, 8)
        CD = AB + h
        BC_sym = h * sqrt(2)
        l_DM = Rational(90, 180) * sp.pi * h
        l_BN = Rational(45, 180) * sp.pi * BC_sym
        S_thang = Rational(1, 2) * (AB + CD) * h
        S_q1 = Rational(90, 360) * sp.pi * h**2
        S_q2 = Rational(45, 360) * sp.pi * (2 * h**2)
        S_conlai = S_thang - S_q1 - S_q2
        S_conlai_val = f"{float(S_conlai.evalf()):.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$, $AD = %s\\text{ cm}$. Vẽ cung tròn tâm $A$ bán kính $AD$ nằm trong hình thang cắt cạnh $AB$ tại $M$, đồng thời vẽ cung tròn tâm $C$ bán kính $CB$ nằm trong hình thang cắt cạnh $CD$ tại $N$.\\\\
a) Tính độ dài hai cung tròn $DM$ và $BN$.\\\\
b) Tính diện tích phần hình thang $ABCD$ nằm ngoài hai hình quạt tròn $ADM$ và $CBN$ (làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.75, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[cyan!20] (2,2) -- (2.4,2) arc (135:180:2.828) -- (0,0) arc (-90:0:2) -- cycle;
\\draw[thick] (0,0) -- (4.4,0) -- (2.4,2) -- (0,2) -- cycle;
\\draw[thick] (0,0) arc (-90:0:2);
\\draw[thick] (2.4,2) arc (135:180:2.828);
\\node[below left] at (0,0) {$D$};
\\node[below right] at (4.4,0) {$C$};
\\node[above right] at (2.4,2) {$B$};
\\node[above left] at (0,2) {$A$};
\\node[above] at (2,2) {$M$};
\\node[below] at (1.57,0) {$N$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(AB), latex(CD), latex(h)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Hạ $BH \\perp CD$ tại $H$, khi đó $ABHD$ là hình chữ nhật nên $BH = AD = %s\\text{ cm}$ và $DH = AB = %s\\text{ cm}$.\\\\
Suy ra $CH = CD - DH = %s - %s = %s\\text{ (cm)}$.\\\\
Xét $\\Delta BHC$ vuông tại $H$ có $BH = CH = %s\\text{ cm}$ nên $\\Delta BHC$ vuông cân tại $H$, suy ra $\\widehat{BCD} = 45^\\circ$ và:
$$BC = \\sqrt{BH^2 + CH^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}.$$
Cung $DM$ thuộc đường tròn tâm $A$, bán kính $AD = %s\\text{ cm}$, góc ở tâm $\\widehat{DAM} = 90^\\circ$ nên có độ dài:
$$l_{DM} = \\dfrac{90}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Cung $BN$ thuộc đường tròn tâm $C$, bán kính $CB = %s\\text{ cm}$, góc ở tâm $\\widehat{BCN} = 45^\\circ$ nên có độ dài:
$$l_{BN} = \\dfrac{45}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
\\item Diện tích hình thang vuông $ABCD$ là:
$$S_{ABCD} = \\dfrac{(AB + CD) \\cdot AD}{2} = \\dfrac{(%s + %s) \\cdot %s}{2} = %s\\text{ (cm}^2\\text{)}.$$
Diện tích hình quạt tròn $ADM$ là:
$$S_{q_1} = \\dfrac{90}{360}\\pi \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}.$$
Diện tích hình quạt tròn $CBN$ là:
$$S_{q_2} = \\dfrac{45}{360}\\pi \\cdot (%s)^2 = %s\\text{ (cm}^2\\text{)}.$$
Vậy diện tích phần hình thang nằm ngoài hai hình quạt tròn là:
$$S = S_{ABCD} - S_{q_1} - S_{q_2} = %s \\approx %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(h), latex(AB), latex(CD), latex(AB), latex(h),
                      latex(h), latex(h), latex(h), latex(BC_sym),
                      latex(h), latex(h), latex(l_DM),
                      latex(BC_sym), latex(BC_sym), latex(l_BN),
                      latex(AB), latex(CD), latex(h), latex(S_thang),
                      latex(h), latex(S_q1),
                      latex(BC_sym), latex(S_q2),
                      latex(S_conlai), S_conlai_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
