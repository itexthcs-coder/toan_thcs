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


def bt_dang9_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('P', 'Q', 'R', 'S'),
        ('A', 'B', 'C', 'D'),
        ('M', 'N', 'P', 'Q')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4

    # Chọn k sao cho 5*k là tổng R + S (từ 140 đến 170)
    k = random.choice([28, 30, 32, 34])
    g3 = 2 * k
    g4 = 3 * k
    tong_34 = 5 * k
    tong_12 = 360 - tong_34
    g1 = random.randint(95, 115)
    g2 = tong_12 - g1

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.2,0);
    \\coordinate (C) at (2.7,2.1);
    \\coordinate (D) at (0.4,1.9);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\fill (A) circle (1pt) node[below left] {$%s$} node[above right] {$%s^\\circ$};
    \\fill (B) circle (1pt) node[below right] {$%s$} node[above left] {$%s^\\circ$};
    \\fill (C) circle (1pt) node[above right] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, g1, d2, g2, d3, d4)

    noidungcauhoi = ('''Cho tứ giác $%s$ có $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$ và $\\dfrac{\\widehat{%s}}{2} = \\dfrac{\\widehat{%s}}{3}$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_tg, d1, g1, d2, g2, d3, d4, hinh_ve))

    nb_da_1_d = '\\True Tổng số đo hai góc $\\widehat{%s} + \\widehat{%s}$ bằng $%s^\\circ$' % (d3, d4, tong_34)
    nb_da_1_s = 'Tổng số đo hai góc $\\widehat{%s} + \\widehat{%s}$ bằng $%s^\\circ$' % (d3, d4, tong_34 + 10)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong tứ giác $%s$, ta có $\\widehat{%s} + \\widehat{%s} = 360^\\circ - (\\widehat{%s} + \\widehat{%s}) = 360^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.'''
                    % (ten_tg, d3, d4, d1, d2, g1, g2, tong_34))

    th_da_1_d = '\\True Số đo của góc $%s$ bằng $%s^\\circ$' % (d3, g3)
    th_da_1_s = 'Số đo của góc $%s$ bằng $%s^\\circ$' % (d3, g4)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Áp dụng tính chất dãy tỉ số bằng nhau: $\\dfrac{\\widehat{%s}}{2} = \\dfrac{\\widehat{%s}}{3} = \\dfrac{\\widehat{%s} + \\widehat{%s}}{2 + 3} = \\dfrac{%s^\\circ}{5} = %s^\\circ$. Suy ra $\\widehat{%s} = 2 \\cdot %s^\\circ = %s^\\circ$.'''
                    % (d3, d4, d3, d4, tong_34, k, d3, k, g3))

    vd_da_1_d = '\\True Số đo của góc $%s$ bằng $%s^\\circ$' % (d4, g4)
    vd_da_1_s = 'Số đo của góc $%s$ bằng $%s^\\circ$' % (d4, g4 - 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Từ $\\dfrac{\\widehat{%s}}{3} = %s^\\circ$, suy ra $\\widehat{%s} = 3 \\cdot %s^\\circ = %s^\\circ$.'''
                    % (d4, k, d4, k, g4))

    vdc_da_1_d = '\\True Tứ giác $%s$ có một góc nhọn và ba góc tù' % (ten_tg)
    vdc_da_1_s = 'Tứ giác $%s$ có hai góc nhọn và hai góc tù' % (ten_tg)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Trong tứ giác $%s$, ta có $\\widehat{%s} = %s^\\circ > 90^\\circ$, $\\widehat{%s} = %s^\\circ > 90^\\circ$, $\\widehat{%s} = %s^\\circ > 90^\\circ$ (ba góc tù) và chỉ có $\\widehat{%s} = %s^\\circ < 90^\\circ$ (một góc nhọn).'''
                     % (ten_tg, d1, g1, d2, g2, d4, g4, d3, g3))

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
