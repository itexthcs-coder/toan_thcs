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

def bt_dang8_p2_b2_c5_hh9(self):
    R = randint(4, 12)
    sd_ab = 50
    sd_bc = 70
    sd_cd = 120
    sd_ac = sd_ab + sd_bc
    sd_abcd = sd_ac + sd_cd
    sd_ad_nho = 360 - sd_abcd
    sd_bd_lon = sd_bc + sd_cd

    noidungcauhoi = ('''Trên đường tròn $(O; %s\\text{ cm})$ lấy bốn điểm $A, B, C, D$ theo thứ tự đó sao cho $\\text{sđ}\\overset\\frown{AB} = %s^\\circ$, $\\text{sđ}\\overset\\frown{BC} = %s^\\circ$ và $\\text{sđ}\\overset\\frown{CD} = %s^\\circ$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (10:1.8);
    \\coordinate (B) at (60:1.8);
    \\coordinate (C) at (130:1.8);
    \\coordinate (D) at (250:1.8);
    \\draw[line width=1pt] (O) circle (1.8);
    \\draw[line width=1pt] (O)--(A) (O)--(B) (O)--(C) (O)--(D) (A)--(C);
    \\fill (O) circle (1pt) node[below right] {$O$};
    \\fill (A) circle (1pt) node[right] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[above left] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\end{tikzpicture}
    \\end{center}''' % (R, sd_ab, sd_bc, sd_cd))

    nb_da_1_d = '\\True Số đo của cung nhỏ $\\overset\\frown{AC}$ bằng $%s^\\circ$' % (sd_ac)
    nb_da_1_s = 'Số đo của cung nhỏ $\\overset\\frown{AC}$ bằng $%s^\\circ$' % (sd_bc - sd_ab)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì điểm $B$ nằm trên cung nhỏ $\\overset\\frown{AC}$ nên $\\text{sđ}\\overset\\frown{AC} = \\text{sđ}\\overset\\frown{AB} + \\text{sđ}\\overset\\frown{BC} = %s^\\circ + %s^\\circ = %s^\\circ$.''' % (sd_ab, sd_bc, sd_ac))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo của cung nhỏ $\\overset\\frown{AD}$ bằng $%s^\\circ$ nên đoạn thẳng $AD$ không phải là đường kính' % (sd_ad_nho)
    th_da_1_s = 'Đoạn thẳng $AD$ là một đường kính của đường tròn $(O)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $\\text{sđ}\\overset\\frown{ABCD} = %s^\\circ + %s^\\circ + %s^\\circ = %s^\\circ$. \\\\ Suy ra số đo cung nhỏ $\\overset\\frown{AD}$ là $360^\\circ - %s^\\circ = %s^\\circ \\neq 180^\\circ$, do đó $AD$ không là đường kính của $(O)$.''' % (sd_ab, sd_bc, sd_cd, sd_abcd, sd_abcd, sd_ad_nho))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài dây cung $AC$ bằng $%s\\sqrt{3}\\text{ cm}$' % (R)
    vd_da_1_s = 'Độ dài dây cung $AC$ bằng $%s\\text{ cm}$' % (R)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $\\text{sđ}\\overset\\frown{AC}_{\\text{nhỏ}} = 120^\\circ$ nên $\\widehat{AOC} = 120^\\circ$. Kẻ $OH \\perp AC$ tại $H$, ta có $\\widehat{AOH} = 60^\\circ$. \\\\ Suy ra $AH = OA \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2}$, nên $AC = 2AH = %s\\sqrt{3}\\text{ cm}$.''' % (R, R))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số đo của cung lớn $\\overset\\frown{BD}$ bằng $%s^\\circ$' % (sd_bd_lon)
    vdc_da_1_s = 'Số đo của cung lớn $\\overset\\frown{BD}$ bằng $%s^\\circ$' % (360 - sd_bd_lon)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Cung $\\overset\\frown{BCD}$ có số đo là $\\text{sđ}\\overset\\frown{BC} + \\text{sđ}\\overset\\frown{CD} = %s^\\circ + %s^\\circ = %s^\\circ > 180^\\circ$ nên chính là cung lớn $\\overset\\frown{BD}$ có số đo bằng $%s^\\circ$.''' % (sd_bc, sd_cd, sd_bd_lon, sd_bd_lon))
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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
