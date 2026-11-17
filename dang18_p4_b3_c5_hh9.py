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


def bt_dang18_p4_b3_c5_hh9(self):
    # Dạng 18: Ứng dụng tính diện tích mảnh vải và đường kính hai đáy khi uốn hình quạt vành khuyên thành chao đèn nón cụt
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        goc, R, r = random.choice([(120, 36, 15), (120, 42, 18), (150, 36, 12), (150, 48, 18), (180, 30, 12), (180, 36, 14)])
        S_sym = Rational(goc, 360) * sp.pi * (R**2 - r**2)
        S_val = str(round(float(S_sym.evalf())))
        C1_sym = Rational(goc, 180) * sp.pi * r
        C2_sym = Rational(goc, 180) * sp.pi * R
        d1 = Rational(goc, 180) * r
        d2 = Rational(goc, 180) * R

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để làm một chiếc chao đèn trang trí có dạng hình nón cụt, người thợ cắt một mảnh vải phẳng có dạng một phần của hình vành khuyên ứng với cung $%s^\\circ$, bán kính ngoài $R = %s\\text{ cm}$ và bán kính trong $r = %s\\text{ cm}$ (bỏ qua phần mép dán).\\\\
a) Tính diện tích mảnh vải dùng để làm chiếc chao đèn đó (làm tròn đến hàng đơn vị của $\\text{cm}^2$).\\\\
b) Khi uốn cong mảnh vải và ghép hai cạnh thẳng lại với nhau để tạo thành chao đèn, hai cung tròn sẽ tạo thành hai đường tròn miệng trên và đáy dưới của chao đèn. Tính đường kính của miệng trên và đáy dưới chiếc chao đèn.
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[orange!20] (15:0.75) -- (15:2.2) arc (15:165:2.2) -- (165:0.75) arc (165:15:0.75) -- cycle;
\\draw[thick] (15:0.75) -- (15:2.2) arc (15:165:2.2) -- (165:0.75) arc (165:15:0.75) -- cycle;
\\draw[dashed] (0,0) -- (15:0.75) (0,0) -- (165:0.75);
\\fill (0,0) circle (1.5pt) node[below] {$O$};
\\node at (90:0.4) {$%s^\\circ$};
\\draw[->, very thick] (2.6,1.1) -- (3.5,1.1);
\\fill[orange!20] (4.3,1.8) -- (5.5,1.8) -- (6.1,0.3) -- (3.7,0.3) -- cycle;
\\draw[thick] (4.9,1.8) ellipse (0.6 and 0.16);
\\draw[thick] (3.7,0.3) arc (180:360:1.2 and 0.28);
\\draw[dashed] (3.7,0.3) arc (180:0:1.2 and 0.28);
\\draw[thick] (4.3,1.8) -- (3.7,0.3) (5.5,1.8) -- (6.1,0.3);
\\end{tikzpicture}
\\end{center}'''
                         % (latex(goc), latex(R), latex(r), latex(goc)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích mảnh vải dùng để làm chao đèn (một phần hình vành khuyên ứng với cung $%s^\\circ$) là:
$$S = \\dfrac{%s}{360}\\pi (R^2 - r^2) = \\dfrac{%s}{360}\\pi (%s^2 - %s^2) = %s \\approx %s\\text{ (cm}^2\\text{)}.$$
\\item Chu vi đường tròn miệng trên của chao đèn bằng độ dài cung trong (bán kính $r = %s\\text{ cm}$, số đo $%s^\\circ$):
$$C_1 = \\dfrac{%s}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Suy ra đường kính của miệng trên chiếc chao đèn là:
$$d_1 = \\dfrac{C_1}{\\pi} = %s\\text{ (cm)}.$$
Chu vi đường tròn đáy dưới của chao đèn bằng độ dài cung ngoài (bán kính $R = %s\\text{ cm}$, số đo $%s^\\circ$):
$$C_2 = \\dfrac{%s}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Suy ra đường kính của đáy dưới chiếc chao đèn là:
$$d_2 = \\dfrac{C_2}{\\pi} = %s\\text{ (cm)}.$$
\\end{enumEX}'''
                   % (latex(goc), latex(goc), latex(goc), latex(R), latex(r), latex(S_sym), S_val,
                      latex(r), latex(goc), latex(goc), latex(r), latex(C1_sym), latex(d1),
                      latex(R), latex(goc), latex(goc), latex(R), latex(C2_sym), latex(d2)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
