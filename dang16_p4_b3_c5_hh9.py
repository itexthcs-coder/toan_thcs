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


def bt_dang16_p4_b3_c5_hh9(self):
    # Dạng 16: Ứng dụng tính diện tích bề mặt và chiều dài nẹp viền mặt bàn góc hình quạt vành khuyên
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([1.0, 1.2, 1.4, 1.5])
        r = random.choice([0.1, 0.2, 0.3])
        R_str = str(R).replace('.', ',')
        r_str = str(r).replace('.', ',')
        S_heso = round(0.25 * (R**2 - r**2), 4)
        S_heso_str = str(S_heso).replace('.', ',')
        S_val = f"{S_heso * math.pi:.2f}".replace('.', ',')
        P_cong_heso = round(0.5 * (R + r), 3)
        P_cong_heso_str = str(P_cong_heso).replace('.', ',')
        P_thang = round(2 * (R - r), 2)
        P_thang_str = str(P_thang).replace('.', ',')
        P_val = f"{P_cong_heso * math.pi + P_thang:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một xưởng mộc thiết kế một mặt bàn làm việc đặt tại góc phòng vuông có dạng một phần của hình vành khuyên ứng với góc ở tâm $90^\\circ$, bán kính mép ngoài là $R = %s\\text{ m}$ và bán kính mép trong (khoét tròn để luồn dây điện) là $r = %s\\text{ m}$.\\\\
a) Tính diện tích bề mặt của chiếc bàn đó (làm tròn đến hàng phần trăm của $\\text{m}^2$).\\\\
b) Người thợ cần dán nẹp nhựa bảo vệ xung quanh toàn bộ chu vi mặt bàn (gồm hai cung tròn và hai cạnh thẳng). Tính tổng chiều dài nẹp nhựa cần dùng (làm tròn đến hàng phần trăm của mét).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[brown!30] (0:0.5) -- (0:2.4) arc (0:90:2.4) -- (90:0.5) arc (90:0:0.5) -- cycle;
\\draw[very thick, brown!70!black] (0:0.5) -- (0:2.4) arc (0:90:2.4) -- (90:0.5) arc (90:0:0.5) -- cycle;
\\draw[dashed] (0,0) -- (0:0.5) (0,0) -- (90:0.5);
\\draw (0,0.25) -- (0.25,0.25) -- (0.25,0);
\\fill (0,0) circle (1.5pt) node[below left] {$O$};
\\end{tikzpicture}
\\end{center}'''
                         % (R_str, r_str))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Mặt bàn có dạng $\\dfrac{90}{360} = \\dfrac{1}{4}$ hình vành khuyên có bán kính ngoài $R = %s\\text{ m}$ và bán kính trong $r = %s\\text{ m}$.\\\\
Diện tích bề mặt của chiếc bàn là:
$$S = \\dfrac{90}{360}\\pi (R^2 - r^2) = \\dfrac{1}{4}\\pi (%s^2 - %s^2) = %s\\pi \\approx %s\\text{ (m}^2\\text{)}.$$
\\item Tổng độ dài hai cung tròn (mép ngoài và mép trong) là:
$$l_1 + l_2 = \\dfrac{90}{180}\\pi \\cdot %s + \\dfrac{90}{180}\\pi \\cdot %s = %s\\pi\\text{ (m)}.$$
Tổng độ dài hai cạnh thẳng áp sát tường là:
$$2(R - r) = 2(%s - %s) = %s\\text{ (m)}.$$
Vậy tổng chiều dài nẹp nhựa cần dùng là:
$$P = %s\\pi + %s \\approx %s\\text{ (m)}.$$
\\end{enumEX}'''
                   % (R_str, r_str, R_str, r_str, S_heso_str, S_val,
                      R_str, r_str, P_cong_heso_str,
                      R_str, r_str, P_thang_str,
                      P_cong_heso_str, P_thang_str, P_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
