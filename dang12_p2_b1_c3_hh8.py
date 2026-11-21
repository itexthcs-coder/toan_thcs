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


def bt_dang12_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('A', 'B', 'C', 'D'),
        ('M', 'N', 'P', 'Q'),
        ('E', 'F', 'G', 'H')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4

    # Các bộ 4 số tỉ lệ có tổng là ước của 360 (10, 12, 15, 18)
    bo_ti_le = [
        (1, 2, 3, 4),   # tổng = 10 -> k = 36
        (1, 2, 4, 5),   # tổng = 12 -> k = 30
        (2, 3, 4, 6),   # tổng = 15 -> k = 24
        (3, 4, 5, 6)    # tổng = 18 -> k = 20
    ]
    r1, r2, r3, r4 = random.choice(bo_ti_le)
    tong_r = r1 + r2 + r3 + r4
    k = 360 // tong_r
    g1, g2, g3, g4 = r1 * k, r2 * k, r3 * k, r4 * k

    noidungcauhoi = ('''Cho tứ giác $%s$ có số đo các góc $\\widehat{%s}$, $\\widehat{%s}$, $\\widehat{%s}$, $\\widehat{%s}$ lần lượt tỉ lệ với $%s$; $%s$; $%s$; $%s$. Xét tính đúng, sai của các khẳng định sau:'''
                     % (ten_tg, d1, d2, d3, d4, r1, r2, r3, r4))

    nb_da_1_d = '\\True Ta có dãy tỉ số bằng nhau $\\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = %s^\\circ$' % (d1, r1, d2, r2, d3, r3, d4, r4, k)
    nb_da_1_s = 'Ta có dãy tỉ số bằng nhau $\\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = %s^\\circ$' % (d1, r1, d2, r2, d3, r3, d4, r4, k + 6)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Áp dụng tính chất dãy tỉ số bằng nhau: $\\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s}}{%s} = \\dfrac{\\widehat{%s} + \\widehat{%s} + \\widehat{%s} + \\widehat{%s}}{%s + %s + %s + %s} = \\dfrac{360^\\circ}{%s} = %s^\\circ$.'''
                    % (d1, r1, d2, r2, d3, r3, d4, r4, d1, d2, d3, d4, r1, r2, r3, r4, tong_r, k))

    th_da_1_d = '\\True Số đo của góc $%s$ bằng $%s^\\circ$ và số đo của góc $%s$ bằng $%s^\\circ$' % (d1, g1, d2, g2)
    th_da_1_s = 'Số đo của góc $%s$ bằng $%s^\\circ$ và số đo của góc $%s$ bằng $%s^\\circ$' % (d1, g1 + 10, d2, g2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $\\widehat{%s} = %s \\cdot %s^\\circ = %s^\\circ$ và $\\widehat{%s} = %s \\cdot %s^\\circ = %s^\\circ$.'''
                    % (d1, r1, k, g1, d2, r2, k, g2))

    vd_da_1_d = '\\True Góc $%s$ là góc tù' % (d3)
    vd_da_1_s = 'Góc $%s$ là góc vuông' % (d3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\widehat{%s} = %s \\cdot %s^\\circ = %s^\\circ > 90^\\circ$ nên góc $%s$ là góc tù.'''
                    % (d3, r3, k, g3, d3))

    vdc_da_1_d = '\\True Tổng số đo hai góc đối $\\widehat{%s} + \\widehat{%s}$ bằng tổng số đo hai góc đối $\\widehat{%s} + \\widehat{%s}$' % (d1, d4, d2, d3)
    vdc_da_1_s = 'Tổng số đo hai góc đối $\\widehat{%s} + \\widehat{%s}$ lớn hơn tổng số đo hai góc đối $\\widehat{%s} + \\widehat{%s}$' % (d1, d4, d2, d3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $\\widehat{%s} + \\widehat{%s} = %s^\\circ + %s^\\circ = %s^\\circ$ và $\\widehat{%s} + \\widehat{%s} = %s^\\circ + %s^\\circ = %s^\\circ$, do đó $\\widehat{%s} + \\widehat{%s} = \\widehat{%s} + \\widehat{%s}$.'''
                     % (d1, d4, g1, g4, g1+g4, d2, d3, g2, g3, g2+g3, d1, d4, d2, d3))

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
