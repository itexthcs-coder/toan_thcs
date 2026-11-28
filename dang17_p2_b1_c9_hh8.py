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

def bt_dang17_p2_b1_c9_hh8(self):
    # Dạng 17 (Thực tế): Đo bề rộng AB của khúc sông bằng cấu hình đồng hồ cát CDE ~ CBA
    mult = random.choice([3, 4, 5])
    CD = random.choice([12, 15, 18])
    CB = CD * mult
    DE = random.choice([14, 16, 18, 20])
    AB = DE * mult
    k = Fraction(1, mult)
    k_sai = Fraction(1, mult + 1)

    CE = random.choice([15, 20, 25])
    CA = CE * mult
    AE = CE + CA

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (C) at (2.5,2.2);'
        '\\coordinate (A) at (0.5,0);'
        '\\coordinate (B) at (4.5,0);'
        '\\coordinate (D) at (1.5,3.3);'
        '\\coordinate (E) at (3.5,3.3);'
        '\\draw[line width=1pt] (A)--(B)--(D)--(E)--cycle (A)--(E);'
        '\\fill (A) circle (1pt) node[left] {$A$};'
        '\\fill (B) circle (1pt) node[right] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (D) circle (1pt) node[left] {$D$};'
        '\\fill (E) circle (1pt) node[right] {$E$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Để đo bề rộng $AB$ của một khúc sông mà không cần sang bờ bên kia, nhóm kĩ sư đóng các cọc tiêu tại $A, B, C, D, E$ '
        'trên mặt đất phẳng sao cho $B, C, D$ thẳng hàng; $A, C, E$ thẳng hàng và $DE // AB$. '
        'Đo thực tế được $CD = %s\\text{ m}$, $CB = %s\\text{ m}$ và $DE = %s\\text{ m}$.%s'
        % (CD, CB, DE, tikz)
    )

    nb_da_1_d = '\\True $\\Delta CDE \\backsim \\Delta CBA$'
    nb_da_1_s = '$\\Delta CDE \\backsim \\Delta CAB$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét $\\Delta CBA$ có đường thẳng $DE$ cắt phần kéo dài của hai cạnh $CB, CA$ và $DE // AB$.\\ '
        'Theo chú ý của định lí hai tam giác đồng dạng, ta có $\\Delta CDE \\backsim \\Delta CBA$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tỉ số đồng dạng của $\\Delta CDE$ với $\\Delta CBA$ bằng $%s$' % fmt_num(k)
    th_da_1_s = 'Tỉ số đồng dạng của $\\Delta CDE$ với $\\Delta CBA$ bằng $%s$' % fmt_num(k_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Tỉ số đồng dạng của $\\Delta CDE$ với $\\Delta CBA$ là $k = \\dfrac{CD}{CB} = \\dfrac{%s}{%s} = %s$.'
        % (CD, CB, fmt_num(k))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Bề rộng $AB$ của khúc sông bằng $%s\\text{ m}$' % AB
    vd_da_1_s = 'Bề rộng $AB$ của khúc sông bằng $%s\\text{ m}$' % (AB - DE)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $\\Delta CDE \\backsim \\Delta CBA$ nên $\\dfrac{DE}{AB} = %s \\Rightarrow \\dfrac{%s}{AB} = %s$.\\ '
        'Suy ra $AB = %s \\cdot %s = %s\\text{ m}$.'
        % (fmt_num(k), DE, fmt_num(k), DE, mult, AB)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu khoảng cách $CE = %s\\text{ m}$ thì khoảng cách $AE$ bằng $%s\\text{ m}$' % (CE, AE)
    vdc_da_1_s = 'Nếu khoảng cách $CE = %s\\text{ m}$ thì khoảng cách $AE$ bằng $%s\\text{ m}$' % (CE, CA)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Ta có $\\dfrac{CE}{CA} = %s \\Rightarrow CA = %s \\cdot %s = %s\\text{ m}$.\\ '
        'Vì $C$ nằm giữa $A$ và $E$ nên $AE = AC + CE = %s + %s = %s\\text{ m}$.'
        % (fmt_num(k), CE, mult, CA, CA, CE, AE)
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
