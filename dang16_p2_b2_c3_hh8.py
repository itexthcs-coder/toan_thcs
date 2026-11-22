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


def bt_dang16_p2_b2_c3_hh8(self):
    bo_dinh = [('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q'), ('E', 'F', 'G', 'H')]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4
    day1, day2 = d1 + d2, d3 + d4

    g_ad = random.choice([105, 120])
    tong_bc = 360 - 2 * g_ad
    g3 = tong_bc // 3
    g2 = 2 * g3

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (3.6,0);
    \\coordinate (A) at (0.8,1.8);
    \\coordinate (B) at (2.8,1.8);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\fill (A) circle (1pt) node[above left] {$%s$} node[below right] {$%s^\\circ$};
    \\fill (B) circle (1pt) node[above right] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[below left] {$%s$} node[above right] {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, g_ad, d2, d3, d4, g_ad)

    noidungcauhoi = ('''Cho tứ giác $%s$ có $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$ và $\\widehat{%s} = 2\\widehat{%s}$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_tg, d1, g_ad, d4, g_ad, d2, d3, hinh_ve))

    nb_da_1_d = '\\True Tổng số đo hai góc $\\widehat{%s} + \\widehat{%s}$ bằng $%s^\\circ$' % (d2, d3, tong_bc)
    nb_da_1_s = 'Tổng số đo hai góc $\\widehat{%s} + \\widehat{%s}$ bằng $%s^\\circ$' % (d2, d3, tong_bc + 10)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong tứ giác $%s$, ta có $\\widehat{%s} + \\widehat{%s} = 360^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.''' % (ten_tg, d2, d3, g_ad, g_ad, tong_bc))

    th_da_1_d = '\\True Số đo của góc $\\widehat{%s}$ bằng $%s^\\circ$' % (d3, g3)
    th_da_1_s = 'Số đo của góc $\\widehat{%s}$ bằng $%s^\\circ$' % (d3, g3 + 5)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $\\widehat{%s} = 2\\widehat{%s}$ nên $3\\widehat{%s} = %s^\\circ \\Rightarrow \\widehat{%s} = %s^\\circ$.''' % (d2, d3, d3, tong_bc, d3, g3))

    vd_da_1_d = '\\True Số đo của góc $\\widehat{%s}$ bằng $%s^\\circ$' % (d2, g2)
    vd_da_1_s = 'Số đo của góc $\\widehat{%s}$ bằng $%s^\\circ$' % (d2, g2 - 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\widehat{%s} = 2 \\cdot %s^\\circ = %s^\\circ$.''' % (d2, g3, g2))

    vdc_da_1_d = '\\True Nếu $%s // %s$ thì tứ giác $%s$ là hình thang cân' % (day1, day2, ten_tg)
    vdc_da_1_s = 'Nếu $%s // %s$ thì tứ giác $%s$ không phải là hình thang cân' % (day1, day2, ten_tg)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Nếu $%s // %s$ thì tứ giác $%s$ là hình thang có hai góc kề cạnh bên $\\widehat{%s} + \\widehat{%s} = 180^\\circ$ (khi $g_ad = 90^\\circ$) hoặc với đề bài trên thì $\\widehat{%s} + \\widehat{%s} = %s^\\circ \\neq 180^\\circ$ nên thực tế $%s$ không song song với $%s$, do đó mệnh đề điều kiện đúng theo logic hình học.''' % (day1, day2, ten_tg, d1, d4, d1, d4, 2*g_ad, day1, day2))
    # Sửa ý d cho thật tự nhiên, chính xác 100%:
    vdc_da_1_d = '\\True Trong tứ giác $%s$, hai cạnh $%s$ và $%s$ không song song với nhau' % (ten_tg, day1, day2)
    vdc_da_1_s = 'Trong tứ giác $%s$, hai cạnh $%s$ và $%s$ song song với nhau' % (ten_tg, day1, day2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì tổng hai góc trong cùng phía $\\widehat{%s} + \\widehat{%s} = %s^\\circ + %s^\\circ = %s^\\circ \\neq 180^\\circ$ nên $%s$ và $%s$ không song song với nhau.''' % (d1, d4, g_ad, g_ad, 2*g_ad, day1, day2))

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
