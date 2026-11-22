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


def bt_dang5_p2_b2_c3_hh8(self):
    bo_dinh = [('A', 'B', 'C', 'D', 'H'), ('M', 'N', 'P', 'Q', 'K'), ('E', 'F', 'G', 'H', 'I')]
    d1, d2, d3, d4, chan = random.choice(bo_dinh)
    ten_ht = d1 + d2 + d3 + d4
    day1, day2 = d1 + d2, d3 + d4
    cb1, cb2 = d1 + d4, d2 + d3
    canh_ben = random.randint(5, 11)

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (3.6,0);
    \\coordinate (A) at (0.9,1.8);
    \\coordinate (B) at (2.7,1.8);
    \\coordinate (H) at (0.9,0);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\draw[line width=1pt, dashed] (A)--(H);
    \\draw[line width=1pt] (0.9,0.22)--(1.12,0.22)--(1.12,0);
    \\fill (A) circle (1pt) node[above left] {$%s$};
    \\fill (B) circle (1pt) node[above right] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[below left] {$%s$};
    \\fill (H) circle (1pt) node[below] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4, chan)

    noidungcauhoi = ('''Cho hình thang cân $%s$ có $%s // %s$, $%s < %s$ và $%s = %s\\text{ cm}$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_ht, day1, day2, day1, day2, cb1, canh_ben, hinh_ve))

    nb_da_1_d = '\\True Cạnh bên $%s$ có độ dài bằng $%s\\text{ cm}$' % (cb2, canh_ben)
    nb_da_1_s = 'Cạnh bên $%s$ có độ dài bằng $%s\\text{ cm}$' % (cb2, canh_ben + 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo Định lí $1$, trong hình thang cân hai cạnh bên bằng nhau nên $%s = %s = %s\\text{ cm}$.''' % (cb2, cb1, canh_ben))

    th_da_1_d = '\\True Tổng độ dài hai cạnh bên $%s + %s$ bằng $%s\\text{ cm}$' % (cb1, cb2, 2 * canh_ben)
    th_da_1_s = 'Tổng độ dài hai cạnh bên $%s + %s$ bằng $%s\\text{ cm}$' % (cb1, cb2, canh_ben)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $%s + %s = %s + %s = %s\\text{ cm}$.''' % (cb1, cb2, canh_ben, canh_ben, 2 * canh_ben))

    vd_da_1_d = '\\True Cạnh đáy $%s$ không nhất thiết phải có độ dài bằng $%s\\text{ cm}$' % (day1, canh_ben)
    vd_da_1_s = 'Cạnh đáy $%s$ luôn có độ dài bằng $%s\\text{ cm}$' % (day1, canh_ben)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong hình thang cân chỉ có hai cạnh bên bằng nhau, còn hai đáy có thể có độ dài bất kì.''')

    vdc_da_1_d = '\\True Đường cao $%s$ ($%s \\in %s$) có độ dài nhỏ hơn $%s\\text{ cm}$' % (d1+chan, chan, day2, canh_ben)
    vdc_da_1_s = 'Đường cao $%s$ ($%s \\in %s$) luôn có độ dài bằng $%s\\text{ cm}$' % (d1+chan, chan, day2, canh_ben)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Trong tam giác vuông $%s%s%s$ vuông tại $%s$, cạnh góc vuông $%s$ nhỏ hơn cạnh huyền $%s = %s\\text{ cm}$.''' % (d1, chan, d4, chan, d1+chan, cb1, canh_ben))

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
