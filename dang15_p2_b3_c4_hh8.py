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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang15_p2_b3_c4_hh8(self):
    # Dạng 15: Kết hợp tính chất đường phân giác và tỉ số diện tích tam giác
    p = random.choice([2, 3])
    q = random.choice([3, 5])
    while p >= q or math.gcd(p, q) != 1:
        p = random.choice([2, 3])
        q = random.choice([3, 5])
    k = random.choice([3, 4, 5])
    ab = p * k
    ac = q * k
    m = random.choice([10, 12, 15])
    s_abd = p * m
    s_acd = q * m
    s_abc = (p + q) * m

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (1.5,3.2);\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (4.6,0);\n'
        '\\coordinate (D) at (1.84,0);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D);\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (D) circle (1pt) node[below] {$D$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, diện tích bằng $%s\\text{ cm}^2$. Đường phân giác của góc $BAC$ cắt cạnh $BC$ tại $D$.\n%s'
        % (ab, ac, s_abc, hinh_ve)
    )

    nb_da_1_d = '\\True $\\frac{BD}{CD} = \\frac{%s}{%s}$' % (p, q)
    nb_da_1_s = '$\\frac{BD}{CD} = \\frac{%s}{%s}$' % (q, p)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Theo tính chất đường phân giác của tam giác, $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s} = \\frac{%s}{%s}$.' % (ab, ac, p, q)
    loigiai_nb_s = 'Sai. Theo tính chất đường phân giác, $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s} = \\frac{%s}{%s}$.' % (ab, ac, p, q)

    th_da_1_d = '\\True $\\frac{S_{\\Delta ABD}}{S_{\\Delta ACD}} = \\frac{%s}{%s}$' % (p, q)
    th_da_1_s = '$\\frac{S_{\\Delta ABD}}{S_{\\Delta ACD}} = \\frac{%s}{%s}$' % (p * p, q * q)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Hai tam giác $ABD$ và $ACD$ có chung đường cao hạ từ $A$ xuống $BC$ nên $\\frac{S_{\\Delta ABD}}{S_{\\Delta ACD}} = \\frac{BD}{CD} = \\frac{%s}{%s}$.' % (p, q)
    loigiai_th_s = 'Sai. Hai tam giác $ABD$ và $ACD$ có chung chiều cao hạ từ $A$ nên tỉ số diện tích bằng tỉ số hai đáy: $\\frac{S_{\\Delta ABD}}{S_{\\Delta ACD}} = \\frac{BD}{CD} = \\frac{%s}{%s}$.' % (p, q)

    vd_da_1_d = '\\True Diện tích tam giác $ABD$ bằng $%s\\text{ cm}^2$' % s_abd
    vd_da_1_s = 'Diện tích tam giác $ABD$ bằng $%s\\text{ cm}^2$' % s_acd
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Ta có $S_{\\Delta ABD} = \\frac{%s}{%s + %s} \\cdot S_{\\Delta ABC} = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}^2$.' % (p, p, q, p, p + q, s_abc, s_abd)
    loigiai_vd_s = 'Sai. Ta tính được $S_{\\Delta ABD} = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}^2$.' % (p, p + q, s_abc, s_abd)

    vdc_da_1_d = '\\True Diện tích tam giác $ACD$ bằng $%s\\text{ cm}^2$' % s_acd
    vdc_da_1_s = 'Diện tích tam giác $ACD$ bằng $%s\\text{ cm}^2$' % (s_acd + 5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Ta có $S_{\\Delta ACD} = S_{\\Delta ABC} - S_{\\Delta ABD} = %s - %s = %s\\text{ cm}^2$.' % (s_abc, s_abd, s_acd)
    loigiai_vdc_s = 'Sai. Ta có $S_{\\Delta ACD} = %s - %s = %s\\text{ cm}^2$.' % (s_abc, s_abd, s_acd)

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

    loigiai_nb_1 = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    loigiai_th_1 = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    loigiai_vd_1 = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    loigiai_vdc_1 = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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
