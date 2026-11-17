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


def bt_dang11_p4_b3_c5_hh9(self):
    # Dạng 11: Ứng dụng tính bán kính cung tròn và chiều dài vòm cổng trong kiến trúc
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b, h = random.choice([(3, 1), (4, 2), (6, 2), (8, 4), (12, 4), (5, 1)])
        AB = 2 * b
        R = (b**2 + h**2) // (2 * h)
        goc_nua_deg = math.degrees(math.asin(b / R))
        goc_tam_deg = round(2 * goc_nua_deg)
        l_vom = (goc_tam_deg / 180.0) * math.pi * R
        goc_nua_str = f"{goc_nua_deg:.2f}".replace('.', ',')
        l_vom_str = f"{l_vom:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cổng chào có phần vòm phía trên là một cung tròn $AB$ căng bởi dây cung ngang $AB = %s\\text{ m}$, chiều cao từ trung điểm $H$ của $AB$ lên đến đỉnh cao nhất $C$ của vòm là $CH = %s\\text{ m}$.\\\\
a) Tính bán kính $R$ của cung tròn tạo nên vòm cổng.\\\\
b) Tính số đo góc ở tâm $\\widehat{AOB}$ (làm tròn đến độ) và chiều dài thanh thép uốn theo cung vòm $AB$ (làm tròn kết quả đến hàng phần trăm của mét).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\draw[very thick, brown!80!black] (-2.1,1.4) arc (146.3:33.7:2.52);
\\draw[thick] (-2.1,1.4) -- (2.1,1.4);
\\draw[dashed] (0,0) -- (-2.1,1.4) (0,0) -- (2.1,1.4) (0,0) -- (0,2.52);
\\fill (0,0) circle (1.5pt) node[below] {$O$};
\\fill (-2.1,1.4) circle (1.5pt) node[left] {$A$};
\\fill (2.1,1.4) circle (1.5pt) node[right] {$B$};
\\fill (0,1.4) circle (1.5pt) node[below right] {$H$};
\\fill (0,2.52) circle (1.5pt) node[above] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(AB), latex(h)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O$ là tâm của đường tròn chứa cung $AB$. Vì $C$ là điểm chính giữa cung $AB$ và $H$ là trung điểm của $AB$ nên $O, H, C$ thẳng hàng, $OC \\perp AB$ tại $H$ và $AH = \\dfrac{AB}{2} = %s\\text{ (m)}$.\\\\
Ta có $OA = OC = R$, suy ra $OH = OC - CH = R - %s\\text{ (m)}$.\\\\
Áp dụng định lí Pythagore trong $\\Delta OAH$ vuông tại $H$, ta có:
$$OA^2 = AH^2 + OH^2 \\Rightarrow R^2 = %s^2 + (R - %s)^2$$
$$\\Leftrightarrow R^2 = %s + R^2 - %sR + %s \\Leftrightarrow %sR = %s \\Leftrightarrow R = %s\\text{ (m)}.$$
\\item Trong $\\Delta OAH$ vuông tại $H$, ta có:
$$\\sin \\widehat{AOH} = \\dfrac{AH}{OA} = \\dfrac{%s}{%s} \\Rightarrow \\widehat{AOH} \\approx %s^\\circ.$$
Do đó số đo góc ở tâm $\\widehat{AOB} = 2\\widehat{AOH} \\approx %s^\\circ$.\\\\
Chiều dài thanh thép uốn theo cung vòm $AB$ là:
$$l = \\dfrac{%s}{180}\\pi \\cdot %s \\approx %s\\text{ (m)}.$$
\\end{enumEX}'''
                   % (latex(b), latex(h),
                      latex(b), latex(h),
                      latex(b**2), latex(2*h), latex(h**2), latex(2*h), latex(b**2 + h**2), latex(R),
                      latex(b), latex(R), goc_nua_str, latex(goc_tam_deg),
                      latex(goc_tam_deg), latex(R), l_vom_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
