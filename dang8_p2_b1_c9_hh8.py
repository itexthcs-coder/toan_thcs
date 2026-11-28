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

def bt_dang8_p2_b1_c9_hh8(self):
    # Dạng 8: Hình thang ABCD (AB // CD) có hai đường chéo AC và BD cắt nhau tại O
    m, n = random.choice([(2, 5), (1, 3), (2, 3), (3, 5), (1, 4)])
    tot = m + n
    mult = random.choice([2, 3, 4])
    AB = m * mult
    CD = n * mult
    k = Fraction(m, n)

    AC = tot * random.choice([2, 3])
    OA = (AC * m) // tot
    OC = AC - OA

    OB = m * random.choice([2, 3])
    BD = (OB * tot) // m
    BD_sai = (OB * n) // m

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (A) at (1.2,2.6);'
        '\\coordinate (B) at (3.2,2.6);'
        '\\coordinate (D) at (0,0);'
        '\\coordinate (C) at (5.0,0);'
        '\\coordinate (O) at (intersection of A--C and B--D);'
        '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);'
        '\\fill (A) circle (1pt) node[above] {$A$};'
        '\\fill (B) circle (1pt) node[above] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (D) circle (1pt) node[left] {$D$};'
        '\\fill (O) circle (1pt) node[above] {$O$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho hình thang $ABCD$ ($AB // CD$) có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. '
        'Biết $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$ và $AC = %s\\text{ cm}$.%s'
        % (AB, CD, AC, tikz)
    )

    nb_da_1_d = '\\True $\\Delta OAB \\backsim \\Delta OCD$'
    nb_da_1_s = '$\\Delta OAB \\backsim \\Delta ODC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét $\\Delta OCD$ có đường thẳng $AB$ cắt phần kéo dài của hai cạnh $OC, OD$ và $AB // CD$.\\ '
        'Theo chú ý của định lí hai tam giác đồng dạng, ta có $\\Delta OAB \\backsim \\Delta OCD$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OCD$ bằng $%s$' % fmt_num(k)
    th_da_1_s = 'Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OCD$ bằng $%s$' % fmt_num(Fraction(n, m))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OCD$ là $k = \\dfrac{AB}{CD} = \\dfrac{%s}{%s} = %s$.'
        % (AB, CD, fmt_num(k))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $OA$ bằng $%s\\text{ cm}$' % OA
    vd_da_1_s = 'Độ dài đoạn thẳng $OA$ bằng $%s\\text{ cm}$' % OC
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $\\Delta OAB \\backsim \\Delta OCD$ nên $\\dfrac{OA}{OC} = %s \\Rightarrow \\dfrac{OA}{OA + OC} = \\dfrac{%s}{%s + %s} \\Rightarrow \\dfrac{OA}{AC} = \\dfrac{%s}{%s}$.\\ '
        'Suy ra $OA = %s \\cdot \\dfrac{%s}{%s} = %s\\text{ cm}$.'
        % (fmt_num(k), m, m, n, m, tot, AC, m, tot, OA)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu $OB = %s\\text{ cm}$ thì $BD = %s\\text{ cm}$' % (OB, BD)
    vdc_da_1_s = 'Nếu $OB = %s\\text{ cm}$ thì $BD = %s\\text{ cm}$' % (OB, BD_sai)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Ta có $\\dfrac{OB}{OD} = \\dfrac{AB}{CD} = %s \\Rightarrow OD = \\dfrac{OB \\cdot %s}{%s} = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ cm}$.\\ '
        'Vậy $BD = OB + OD = %s + %s = %s\\text{ cm}$.'
        % (fmt_num(k), n, m, OB, n, m, BD - OB, OB, BD - OB, BD)
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
