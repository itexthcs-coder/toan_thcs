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


def bt_dang14_p4_b3_c5_hh9(self):
    # Dạng 14: Ứng dụng tính quãng đường quét và diện tích làm sạch của cần gạt nước ô tô
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([45, 50, 55, 60])
        L_luoi = random.choice([35, 40])
        goc = random.choice([120, 135, 150])
        r = R - L_luoi
        l_sym = Rational(goc, 180) * sp.pi * R
        l_val = f"{float(l_sym.evalf()):.2f}".replace('.', ',')
        S_sym = Rational(goc, 360) * sp.pi * (R**2 - r**2)
        S_val = str(round(float(S_sym.evalf())))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cần gạt nước trên kính chắn gió ô tô có chiều dài toàn bộ tay gạt tính từ trục quay là $%s\\text{ cm}$, trong đó phần lưỡi cao su trực tiếp gạt nước dài $%s\\text{ cm}$ tính từ đầu mút ngoài cùng trở vào. Khi hoạt động, cần gạt quay qua lại một góc $%s^\\circ$.\\\\
a) Tính quãng đường đi được của đầu mút ngoài cùng lưỡi gạt sau một lượt gạt (làm tròn đến hàng phần trăm của cm).\\\\
b) Tính diện tích phần kính chắn gió được lưỡi cao su làm sạch sau một lượt gạt (làm tròn đến hàng đơn vị của $\\text{cm}^2$).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[cyan!22] (22.5:0.75) -- (22.5:2.6) arc (22.5:157.5:2.6) -- (157.5:0.75) arc (157.5:22.5:0.75) -- cycle;
\\draw[thick] (22.5:2.6) arc (22.5:157.5:2.6);
\\draw[thick] (22.5:0.75) arc (22.5:157.5:0.75);
\\draw[dashed] (0,0) -- (22.5:0.75) (0,0) -- (157.5:0.75);
\\draw[very thick] (22.5:0.75) -- (22.5:2.6);
\\draw[very thick] (157.5:0.75) -- (157.5:2.6);
\\fill (0,0) circle (1.8pt) node[below] {$O$};
\\node at (90:0.4) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(L_luoi), latex(goc), latex(goc)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đầu mút ngoài cùng của lưỡi gạt vạch nên một cung tròn bán kính $R = %s\\text{ cm}$, số đo $%s^\\circ$.\\\\
Quãng đường đi được của đầu mút ngoài cùng sau một lượt gạt là:
$$l = \\dfrac{%s}{180}\\pi \\cdot %s = %s \\approx %s\\text{ (cm)}.$$
\\item Bán kính đường tròn phía trong giới hạn phần lưỡi cao su là:
$$r = %s - %s = %s\\text{ (cm)}.$$
Phần kính chắn gió được lưỡi cao su làm sạch là một phần hình vành khuyên ứng với góc ở tâm $%s^\\circ$, có diện tích là:
$$S = \\dfrac{%s}{360}\\pi (R^2 - r^2) = \\dfrac{%s}{360}\\pi (%s^2 - %s^2) = %s \\approx %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R), latex(goc),
                      latex(goc), latex(R), latex(l_sym), l_val,
                      latex(R), latex(L_luoi), latex(r),
                      latex(goc), latex(goc), latex(goc), latex(R), latex(r), latex(S_sym), S_val))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
