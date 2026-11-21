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


def bt_dang17_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('A', 'B', 'C', 'D'),
        ('M', 'N', 'P', 'Q'),
        ('E', 'F', 'G', 'H')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4

    gn1 = random.randint(70, 95)
    gn2 = random.randint(80, 100)
    gn3 = random.randint(85, 110)
    gn4 = 360 - (gn1 + gn2 + gn3)
    gt4 = 180 - gn4

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0.8,0.8);
    \\coordinate (B) at (3.2,0.8);
    \\coordinate (C) at (2.8,2.5);
    \\coordinate (D) at (1.0,2.4);
    \\draw[line width=1pt] (0,0.8)--(B)--(3.2,0) (B)--(C)--(3.6,2.5) (C)--(D)--(1.0,3.2) (D)--(A)--(0.8,0);
    \\fill (A) circle (1pt) node[above right] {$%s$};
    \\fill (B) circle (1pt) node[above left] {$%s$};
    \\fill (C) circle (1pt) node[below left] {$%s$};
    \\fill (D) circle (1pt) node[below right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4)

    noidungcauhoi = ('''Cho tứ giác $%s$ có các góc ngoài tại bốn đỉnh $%s, %s, %s, %s$ lần lượt là $\\widehat{%s}_1$, $\\widehat{%s}_1$, $\\widehat{%s}_1$, $\\widehat{%s}_1$ (mỗi đỉnh lấy một góc ngoài, như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_tg, d1, d2, d3, d4, d1, d2, d3, d4, hinh_ve))

    nb_da_1_d = '\\True Tại mỗi đỉnh của tứ giác, tổng số đo góc trong và góc ngoài kề bù với nó bằng $180^\\circ$'
    nb_da_1_s = 'Tại mỗi đỉnh của tứ giác, tổng số đo góc trong và góc ngoài kề bù với nó bằng $360^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì góc trong và góc ngoài tại mỗi đỉnh của tứ giác là hai góc kề bù nên tổng số đo của chúng luôn bằng $180^\\circ$.''')

    th_da_1_d = '\\True Tổng của tất cả bốn góc trong và bốn góc ngoài của tứ giác bằng $720^\\circ$'
    th_da_1_s = 'Tổng của tất cả bốn góc trong và bốn góc ngoài của tứ giác bằng $540^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tứ giác có bốn đỉnh, tại mỗi đỉnh tổng góc trong và góc ngoài bằng $180^\\circ$ nên tổng của bốn góc trong và bốn góc ngoài bằng $4 \\cdot 180^\\circ = 720^\\circ$.''')

    vd_da_1_d = '\\True Tổng số đo bốn góc ngoài $\\widehat{%s}_1 + \\widehat{%s}_1 + \\widehat{%s}_1 + \\widehat{%s}_1$ bằng $360^\\circ$' % (d1, d2, d3, d4)
    vd_da_1_s = 'Tổng số đo bốn góc ngoài $\\widehat{%s}_1 + \\widehat{%s}_1 + \\widehat{%s}_1 + \\widehat{%s}_1$ bằng $180^\\circ$' % (d1, d2, d3, d4)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì tổng bốn góc trong bằng $360^\\circ$ nên tổng bốn góc ngoài bằng $720^\\circ - 360^\\circ = 360^\\circ$.''')

    vdc_da_1_d = '\\True Nếu $\\widehat{%s}_1 = %s^\\circ$, $\\widehat{%s}_1 = %s^\\circ$, $\\widehat{%s}_1 = %s^\\circ$ thì góc trong $\\widehat{%s}$ của tứ giác bằng $%s^\\circ$' % (d1, gn1, d2, gn2, d3, gn3, d4, gt4)
    vdc_da_1_s = 'Nếu $\\widehat{%s}_1 = %s^\\circ$, $\\widehat{%s}_1 = %s^\\circ$, $\\widehat{%s}_1 = %s^\\circ$ thì góc trong $\\widehat{%s}$ của tứ giác bằng $%s^\\circ$' % (d1, gn1, d2, gn2, d3, gn3, d4, gn4)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $\\widehat{%s}_1 = 360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = %s^\\circ$, suy ra góc trong $\\widehat{%s} = 180^\\circ - %s^\\circ = %s^\\circ$.'''
                     % (d4, gn1, gn2, gn3, gn4, d4, gn4, gt4))

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
