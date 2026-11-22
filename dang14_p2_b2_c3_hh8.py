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


def bt_dang14_p2_b2_c3_hh8(self):
    bo_dinh = [('A', 'B', 'C', 'D', 'I', 'J'), ('M', 'N', 'P', 'Q', 'E', 'F'), ('E', 'F', 'G', 'H', 'I', 'K')]
    d1, d2, d3, d4, p1, p2 = random.choice(bo_dinh)
    ten_ht = d1 + d2 + d3 + d4
    day1, day2 = d1 + d2, d3 + d4
    cb1, cb2 = d1 + d4, d2 + d3
    dc1, dc2 = d1 + d3, d2 + d4

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (3.6,0);
    \\coordinate (A) at (0.9,1.8);
    \\coordinate (B) at (2.7,1.8);
    \\coordinate (I) at (1.8,3.6);
    \\coordinate (J) at (intersection of A--C and B--D);
    \\draw[line width=1pt] (D)--(I)--(C) (A)--(B);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D) (I)--(J);
    \\fill (A) circle (1pt) node[left] {$%s$};
    \\fill (B) circle (1pt) node[right] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[below left] {$%s$};
    \\fill (I) circle (1pt) node[above] {$%s$};
    \\fill (J) circle (1pt) node[below] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4, p1, p2)

    noidungcauhoi = ('''Cho hình thang cân $%s$ ($%s // %s$, $%s < %s$) có các đường thẳng $%s, %s$ cắt nhau tại $%s$, các đường chéo $%s, %s$ cắt nhau tại $%s$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_ht, day1, day2, day1, day2, cb1, cb2, p1, dc1, dc2, p2, hinh_ve))

    nb_da_1_d = '\\True Tam giác $%s%s%s$ cân tại $%s$ nên $%s%s = %s%s$' % (p1, d1, d2, p1, p1, d1, p1, d2)
    nb_da_1_s = 'Tam giác $%s%s%s$ cân tại $%s$' % (p1, d1, d2, d1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $%s$ là hình thang cân nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, suy ra $\\triangle %s%s%s$ cân tại $%s$, do đó $%s%s = %s%s$.''' % (ten_ht, p1, d1, d2, p1, d2, d1, p1, d1, d2, p1, p1, d1, p1, d2))

    th_da_1_d = '\\True Điểm $%s$ cũng cách đều hai đầu mút $%s$ và $%s$ ($%s%s = %s%s$)' % (p2, d1, d2, p2, d1, p2, d2)
    th_da_1_s = 'Điểm $%s$ không cách đều hai điểm $%s$ và $%s$' % (p2, d1, d2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $\\triangle %s%s%s = \\triangle %s%s%s$ (c.c.c) nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, suy ra $\\triangle %s%s%s$ cân tại $%s$, do đó $%s%s = %s%s$.''' % (d1, d2, d3, d2, d1, d4, d2, d1, d3, d1, d2, d4, p2, d1, d2, p2, p2, d1, p2, d2))

    vd_da_1_d = '\\True Đường thẳng $%s%s$ là đường trung trực của đoạn thẳng $%s$' % (p1, p2, day1)
    vd_da_1_s = 'Đường thẳng $%s%s$ song song với đoạn thẳng $%s$' % (p1, p2, day1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $%s%s = %s%s$ và $%s%s = %s%s$ nên cả $%s$ và $%s$ đều thuộc đường trung trực của $%s$, vậy $%s%s$ là đường trung trực của $%s$.''' % (p1, d1, p1, d2, p2, d1, p2, d2, p1, p2, day1, p1, p2, day1))

    vdc_da_1_d = '\\True Đường thẳng $%s%s$ cũng là đường trung trực của đáy lớn $%s$' % (p1, p2, day2)
    vdc_da_1_s = 'Đường thẳng $%s%s$ không vuông góc với đáy lớn $%s$' % (p1, p2, day2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tương tự, ta chứng minh được $%s%s = %s%s$ và $%s%s = %s%s$ nên $%s%s$ cũng là đường trung trực của $%s$.''' % (p1, d3, p1, d4, p2, d3, p2, d4, p1, p2, day2))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
