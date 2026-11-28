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
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        s = ('%.4f' % val).rstrip('0').rstrip('.')
        return s.replace('.', ',')
    if isinstance(val, Decimal):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        return '\dfrac{%s}{%s}' % (val.numerator, val.denominator)
    return str(val)

def bt_dang14_p2_b1_c9_hh8(self):
    # Dạng 14: Tam giác ABC ~ A'B'C', biết tỉ lệ 3 cạnh của A'B'C' là 3:4:5 và chu vi
    num, den = random.choice([(3, 2), (5, 2), (2, 1), (3, 4)])
    k = Fraction(num, den)

    unit = den * random.choice([1, 2])
    a1 = 3 * unit
    b1 = 4 * unit
    c1 = 5 * unit
    P1 = a1 + b1 + c1

    a = int(a1 * k)
    b = int(b1 * k)
    c = int(c1 * k)
    P = a + b + c

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (A) at (0,0);'
        '\\coordinate (B) at (0,2.7);'
        '\\coordinate (C) at (3.6,0);'
        '\\coordinate (A1) at (5.2,0);'
        '\\coordinate (B1) at (5.2,1.8);'
        '\\coordinate (C1) at (7.6,0);'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A1)--(B1)--(C1)--cycle;'
        '\\fill (A) circle (1pt) node[below left] {$A$};'
        '\\fill (B) circle (1pt) node[above] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (A1) circle (1pt) node[below left] {$A^{\prime}$};'
        '\\fill (B1) circle (1pt) node[above] {$B^{\prime}$};'
        '\\fill (C1) circle (1pt) node[right] {$C^{\prime}$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho $\\Delta ABC \\backsim \\Delta A^{\prime}B^{\prime}C^{\prime}$ theo tỉ số đồng dạng $k = %s$. '
        'Biết độ dài ba cạnh của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ tỉ lệ với $3 : 4 : 5$ và chu vi của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ bằng $%s\\text{ cm}$.%s'
        % (fmt_num(k), P1, tikz)
    )

    nb_da_1_d = '\\True Độ dài các cạnh của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ lần lượt là $%s\\text{ cm}$, $%s\\text{ cm}$, $%s\\text{ cm}$' % (a1, b1, c1)
    nb_da_1_s = 'Độ dài các cạnh của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ lần lượt là $%s\\text{ cm}$, $%s\\text{ cm}$, $%s\\text{ cm}$' % (a, b, c)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Gọi độ dài ba cạnh của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ lần lượt là $x, y, z$ ($x, y, z > 0$).\\ '
        'Ta có $\\dfrac{x}{3} = \\dfrac{y}{4} = \\dfrac{z}{5} = \\dfrac{x + y + z}{3 + 4 + 5} = \\dfrac{%s}{12} = %s$.\\ '
        'Suy ra $x = %s\\text{ cm}$, $y = %s\\text{ cm}$, $z = %s\\text{ cm}$.'
        % (P1, unit, a1, b1, c1)
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Cạnh ngắn nhất của $\\Delta ABC$ có độ dài bằng $%s\\text{ cm}$' % a
    th_da_1_s = 'Cạnh ngắn nhất của $\\Delta ABC$ có độ dài bằng $%s\\text{ cm}$' % a1
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Vì $\\Delta ABC \\backsim \\Delta A^{\prime}B^{\prime}C^{\prime}$ theo tỉ số đồng dạng $k = %s$ nên cạnh ngắn nhất của $\\Delta ABC$ '
        'tương ứng với cạnh ngắn nhất của $\\Delta A^{\prime}B^{\prime}C^{\prime}$ và có độ dài bằng $%s \\cdot %s = %s\\text{ cm}$.'
        % (fmt_num(k), a1, fmt_num(k), a)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Chu vi của $\\Delta ABC$ bằng $%s\\text{ cm}$' % P
    vd_da_1_s = 'Chu vi của $\\Delta ABC$ bằng $%s\\text{ cm}$' % (P + 6)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Ba cạnh của $\\Delta ABC$ lần lượt là $%s\\text{ cm}$, $%s\\text{ cm}$, $%s\\text{ cm}$.\\ '
        'Vậy chu vi của $\\Delta ABC$ bằng $%s + %s + %s = %s\\text{ cm}$.'
        % (a, b, c, a, b, c, P)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True $\\Delta ABC$ là một tam giác vuông'
    vdc_da_1_s = '$\\Delta ABC$ là một tam giác đều'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Xét $\\Delta ABC$ có $%s^2 + %s^2 = %s + %s = %s = %s^2$.\\ '
        'Theo định lí Pythagore đảo, $\\Delta ABC$ là một tam giác vuông.'
        % (a, b, a**2, b**2, c**2, c)
    )
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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
