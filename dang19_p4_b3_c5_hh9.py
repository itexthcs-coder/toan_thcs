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


def bt_dang19_p4_b3_c5_hh9(self):
    # Dạng 19: Ứng dụng tính chiều dài cung chiếu sáng và diện tích vùng biển an toàn quanh ngọn hải đăng
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([15, 18, 20, 24, 25])
        r = random.choice([2, 3, 4])
        goc = random.choice([180, 210, 216, 240])
        l_sym = Rational(goc, 180) * sp.pi * R
        l_val = f"{float(l_sym.evalf()):.2f}".replace('.', ',')
        S_heso = Rational(goc, 360) * (R**2 - r**2)
        S_heso_str = f"{float(S_heso):.2f}".rstrip('0').rstrip('.').replace('.', ',')
        S_val = f"{float(S_heso) * 3.14:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ngọn hải đăng đặt tại vị trí $O$ trên mũi đất có tầm chiếu sáng tối đa $%s\\text{ km}$. Do vách núi phía sau che khuất nên chùm sáng của hải đăng chỉ quét trên mặt biển một góc ở tâm là $%s^\\circ$. Ngoài ra, vùng biển trong bán kính $%s\\text{ km}$ quanh chân hải đăng có bãi đá ngầm nguy hiểm không cho phép tàu thuyền đi vào.\\\\
a) Tính chiều dài cung tròn giới hạn ranh giới ngoài cùng của vùng chiếu sáng trên mặt biển (làm tròn đến hàng phần trăm của km).\\\\
b) Tính diện tích vùng biển an toàn (nằm ngoài bãi đá ngầm) nhận được tín hiệu ánh sáng từ ngọn hải đăng (lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[yellow!30] (-18:0.45) -- (-18:2.1) arc (-18:198:2.1) -- (198:0.45) arc (198:-18:0.45) -- cycle;
\\fill[red!25] (0,0) circle (0.45);
\\draw[thick] (-18:2.1) arc (-18:198:2.1);
\\draw[thick, red!75!black] (0,0) circle (0.45);
\\draw[thick] (0,0) -- (-18:2.1) (0,0) -- (198:2.1);
\\fill (0,0) circle (1.8pt) node[below] {$O$};
\\node at (90:1.3) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(goc), latex(r), latex(goc)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Ranh giới ngoài cùng của vùng chiếu sáng trên mặt biển là một cung tròn bán kính $R = %s\\text{ km}$, số đo $%s^\\circ$.\\\\
Chiều dài cung tròn giới hạn này là:
$$l = \\dfrac{%s}{180}\\pi \\cdot %s = %s \\approx %s\\text{ (km)}.$$
\\item Vùng biển an toàn nhận được ánh sáng từ ngọn hải đăng là một phần của hình vành khuyên ứng với góc ở tâm $%s^\\circ$, có bán kính ngoài $R = %s\\text{ km}$ và bán kính trong $r = %s\\text{ km}$.\\\\
Diện tích vùng biển an toàn đó là:
$$S = \\dfrac{%s}{360}\\pi (R^2 - r^2) = \\dfrac{%s}{360}\\pi (%s^2 - %s^2) = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (km}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R), latex(goc),
                      latex(goc), latex(R), latex(l_sym), l_val,
                      latex(goc), latex(R), latex(r),
                      latex(goc), latex(goc), latex(R), latex(r), S_heso_str, S_heso_str, S_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
