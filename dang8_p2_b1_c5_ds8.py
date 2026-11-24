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


def bt_dang8_p2_b1_c5_ds8(self):
    # Dạng 8: Lí giải bản chất khoảng giá trị của biến số
    v_min = random.choice([50, 60, 70])
    v_max = v_min + random.choice([30, 40, 50])
    k_val = random.randint(110, 150)

    tikz_v = (
        "\\begin{center}\n"
        "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
        "\\draw[line width=1pt, ->] (-0.5,0) -- (6.5,0);\n"
        "\\draw[line width=1pt] (1,-0.12) -- (1,0.12) node[above] {$%s$};\n"
        "\\draw[line width=1pt] (5,-0.12) -- (5,0.12) node[above] {$%s$};\n"
        "\\fill (3.2,0) circle (1pt) node[above] {$v$};\n"
        "\\node at (3,-0.4) {Khoảng vận tốc $v$ (km/h) trên đường cao tốc};\n"
        "\\end{tikzpicture}\n"
        "\\end{center}"
        % (v_min, v_max)
    )

    noidungcauhoi = ('''Xét hai đại lượng sau của giao thông trên một tuyến đường cao tốc:\\\\
- $v$ (đơn vị: $\\text{km/h}$) là vận tốc tức thời của một chiếc ô tô (minh họa trên trục số dưới đây).\\\\
- $k$ là số lượt xe đi qua trạm thu phí trong một giờ.
%s''' % tikz_v)

    nb_da_1_d = '\\True Vận tốc $v$ có thể nhận giá trị thực tùy ý trong khoảng từ $%s\\,\\text{km/h}$ đến $%s\\,\\text{km/h}$ nên $v$ là số liệu liên tục' % (v_min, v_max)
    nb_da_1_s = 'Vận tốc $v$ chỉ nhận các giá trị nguyên từ $%s$ đến $%s$ nên $v$ là số liệu rời rạc' % (v_min, v_max)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Vận tốc tức thời là đại lượng đo lường vật lí có thể nhận giá trị thực tùy ý trong khoảng $(%s; %s)$ nên $v$ là số liệu liên tục.''' % (v_min, v_max)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số lượt xe $k$ không thể nhận giá trị nằm giữa $%s$ và $%s$ nên $k$ là số liệu rời rạc' % (k_val, k_val + 1)
    th_da_1_s = 'Số lượt xe $k$ có thể nhận giá trị thập phân nằm giữa $%s$ và $%s$ nên $k$ là số liệu liên tục' % (k_val, k_val + 1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Số lượt xe đi qua trạm thu phí thu được từ phép đếm nên chỉ nhận giá trị nguyên không âm, không thể nhận giá trị nằm giữa $%s$ và $%s$. Do đó $k$ là số liệu rời rạc.''' % (k_val, k_val + 1)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Dù đồng hồ tốc độ điện tử trên xe chỉ hiển thị số nguyên thì đại lượng vận tốc $v$ vẫn là số liệu liên tục'
    vd_da_1_s = 'Nếu đồng hồ tốc độ điện tử trên xe chỉ hiển thị số nguyên thì vận tốc $v$ trở thành số liệu rời rạc'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Việc màn hình đồng hồ làm tròn giá trị hiển thị sang số nguyên không làm thay đổi bản chất liên tục của đại lượng vật lí vận tốc.'''
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Dữ liệu về số lượt xe $k$ thu được thông qua camera quan sát đếm xe tại trạm thu phí là thu thập dữ liệu trực tiếp'
    vdc_da_1_s = 'Dữ liệu về số lượt xe $k$ thu được thông qua camera quan sát đếm xe tại trạm thu phí là thu thập dữ liệu gián tiếp'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '''Quan sát và đếm số lượt xe thực tế đi qua trạm thu phí (trực tiếp hoặc qua thiết bị ghi hình tại chỗ) là hình thức thu thập dữ liệu trực tiếp.'''
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
