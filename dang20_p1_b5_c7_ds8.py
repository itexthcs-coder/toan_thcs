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
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang20_p1_b5_c7_ds8(self):
    def fmt_num(val):
        if isinstance(val, Fraction):
            if val.denominator == 1:
                return str(val.numerator)
            if val.numerator < 0:
                return '-\\dfrac{%s}{%s}' % (abs(val.numerator), val.denominator)
            return '\\dfrac{%s}{%s}' % (val.numerator, val.denominator)
        if isinstance(val, float):
            s_val = ('%g' % val).replace('.', ',')
            return s_val
        return str(val)

    def fmt_line(a_val, b_val):
        # Định dạng y = ax + b với a_val, b_val là int hoặc Fraction
        if isinstance(a_val, Fraction) and a_val.denominator != 1:
            if a_val.numerator < 0:
                str_a = '-\\dfrac{%s}{%s}x' % (abs(a_val.numerator), a_val.denominator)
            else:
                str_a = '\\dfrac{%s}{%s}x' % (a_val.numerator, a_val.denominator)
        else:
            ai = int(a_val)
            if ai == 1:
                str_a = 'x'
            elif ai == -1:
                str_a = '-x'
            else:
                str_a = '%sx' % ai

        if b_val == 0:
            return 'y = %s' % str_a
        if isinstance(b_val, Fraction) and b_val.denominator != 1:
            if b_val.numerator < 0:
                str_b = '- \\dfrac{%s}{%s}' % (abs(b_val.numerator), b_val.denominator)
            else:
                str_b = '+ \\dfrac{%s}{%s}' % (b_val.numerator, b_val.denominator)
        else:
            bi = int(b_val)
            if bi > 0:
                str_b = '+ %s' % bi
            else:
                str_b = '- %s' % abs(bi)
        return 'y = %s %s' % (str_a, str_b)

    # Dạng 20: So sánh độ lớn của hai hệ số góc dương thông qua góc tạo bởi đường thẳng với trục Ox
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_goc = (
            '\\begin{center}'
            '\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
            '\\draw[->, line width=1pt] (-1.5,0)--(3.5,0) node[below] {$x$};'
            '\\draw[->, line width=1pt] (0,-0.8)--(0,3.2) node[left] {$y$};'
            '\\draw[line width=1pt] (-1.0,-0.5)--(3.0,1.5) node[right] {$(d_1)$};'
            '\\draw[line width=1pt] (0.5,-0.5)--(2.3,3.1) node[right] {$(d_2)$};'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};'
            '\\draw[line width=1pt] (0.6,0) arc (0:26.5:0.6);'
            '\\node at (1.05,0.22) {$\\alpha_1$};'
            '\\draw[line width=1pt] (1.25,0) arc (0:63.4:0.5);'
            '\\node at (1.55,0.32) {$\\alpha_2$};'
            '\\end{tikzpicture}'
            '\\end{center}'
        )
        noidungcauhoi = ('Cho hai đường thẳng $(d_1): y = ax + b$ ($a > 0$) và $(d_2): y = a\'x + b\'$ ($a\' > 0$) lần lượt tạo với trục $Ox$ các góc nhọn $\\alpha_1$ và $\\alpha_2$. Biết $\\alpha_1 < \\alpha_2 < 90^\\circ$, khẳng định nào sau đây là đúng?' + tikz_goc)
        da_d = '\\True $a < a\'$'
        da_s1 = '$a > a\'$'
        da_s2 = '$a = a\'$'
        da_s3 = '$a + a\' = 0$'
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('Khi hệ số góc dương ($a > 0$), góc tạo bởi đường thẳng $y = ax + b$ và trục $Ox$ là góc nhọn và góc này càng lớn thì đường thẳng càng dốc, tức là hệ số góc $a$ càng lớn.\\\\'
                   'Vì $0^\\circ < \\alpha_1 < \\alpha_2 < 90^\\circ$ nên $a < a\'$.')

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
