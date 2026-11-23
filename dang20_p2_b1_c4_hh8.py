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


def bt_dang20_p2_b1_c4_hh8(self):
    k = random.choice([1, 2])
    bc = 60 * k
    ab = 9 * k
    ce = 20 * k
    ek = 25 * k
    kb = bc - ce - ek
    ts_cd_ca = Rational(1, 3)
    ts_dh_ac = Rational(5, 12)
    ts_ah_hc = Rational(1, 3)

    noidungcauhoi = ("""Một đoạn đường dẫn lên cầu vượt được mô hình hóa bởi tam giác vuông $ABC$ vuông tại $B$, trong đó mặt đất nằm ngang là $BC = %s\\text{ m}$, trụ đỡ chính tại đầu cầu là $AB = %s\\text{ m}$ và mặt đường dốc là $AC$. Để gia cố kết cấu, kĩ sư bố trí thêm hai trụ đỡ phụ $DE$ và $HK$ cùng thẳng đứng vuông góc với mặt đất $BC$ ($D, H \\in AC$ và $E, K \\in BC$) sao cho $CE = %s\\text{ m}$ và $EK = %s\\text{ m}$ (như hình vẽ bên dưới). Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (A) at (0,2.7);
\\coordinate (C) at (5.4,0);
\\coordinate (E) at (3.6,0);
\\coordinate (D) at (3.6,0.9);
\\coordinate (K) at (1.35,0);
\\coordinate (H) at (1.35,2.025);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E) (H)--(K);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (3.6,0.25)--(3.85,0.25)--(3.85,0);
\\draw[line width=1pt] (1.35,0.25)--(1.6,0.25)--(1.6,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (E) circle (1pt) node[below] {$E$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\end{tikzpicture}
\\end{center}"""
                     % (bc, ab, ce, ek))

    nb_da_1_d = '\\True Các trụ đỡ $DE$, $HK$ và $AB$ đôi một song song với nhau'
    nb_da_1_s = 'Các trụ đỡ $DE$ và $HK$ vuông góc với trụ đỡ $AB$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì các trụ đỡ $DE$, $HK$ và $AB$ cùng vuông góc với mặt đất $BC$ nên chúng đôi một song song với nhau.""")

    th_da_1_d = '\\True Tỉ số độ dài đoạn dốc $\\dfrac{CD}{CA}$ bằng $\\dfrac{1}{3}$'
    th_da_1_s = 'Tỉ số độ dài đoạn dốc $\\dfrac{CD}{CA}$ bằng $\\dfrac{1}{4}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Xét $\\Delta CAB$ có $DE // AB$, theo định lí Thalès trong tam giác ta có $\\dfrac{CD}{CA} = \\dfrac{CE}{CB} = \\dfrac{%s}{%s} = \\dfrac{1}{3}$."""
                    % (ce, bc))

    vd_da_1_d = '\\True Độ dài đoạn dốc $DH$ bằng $\\dfrac{5}{12}$ độ dài toàn bộ đường dốc $AC$'
    vd_da_1_s = 'Độ dài đoạn dốc $DH$ bằng $\\dfrac{3}{4}$ độ dài toàn bộ đường dốc $AC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Xét $\\Delta CAB$ có $HK // AB$, theo định lí Thalès ta có $\\dfrac{DH}{CA} = \\dfrac{EK}{CB} = \\dfrac{%s}{%s} = \\dfrac{5}{12}$, suy ra $DH = \\dfrac{5}{12} AC$."""
                    % (ek, bc))

    vdc_da_1_d = '\\True Tỉ số $\\dfrac{AH}{HC}$ bằng $\\dfrac{1}{3}$'
    vdc_da_1_s = 'Tỉ số $\\dfrac{AH}{HC}$ bằng $\\dfrac{3}{4}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Ta có $KB = BC - CE - EK = %s - %s - %s = %s\\text{ (m)}$ và $CK = CE + EK = %s + %s = %s\\text{ (m)}$. \\\\ Theo định lí Thalès, $\\dfrac{AH}{HC} = \\dfrac{BK}{KC} = \\dfrac{%s}{%s} = \\dfrac{1}{3}$."""
                     % (bc, ce, ek, kb, ce, ek, ce + ek, kb, ce + ek))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
