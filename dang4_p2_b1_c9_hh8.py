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

def bt_dang4_p2_b1_c9_hh8(self):
    # Dạng 4: Đường thẳng song song cắt hai cạnh của tam giác
    den = random.choice([3, 4, 5])
    num = random.choice([1, 2])
    while num >= den:
        num = random.randint(1, den - 1)
    k = Fraction(num, den)

    m_ab = random.choice([3, 4])
    m_ac = random.choice([4, 5])
    m_bc = random.choice([5, 6])

    AB = den * m_ab
    AC = den * m_ac
    BC = den * m_bc

    AM = num * m_ab
    AN = num * m_ac
    MN = num * m_bc
    AN_sai = AC - AN if AC - AN != AN else AN + 2

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (A) at (1.8,3.2);'
        '\\coordinate (B) at (0,0);'
        '\\coordinate (C) at (4.5,0);'
        '\\coordinate (M) at ($(A)!0.38!(B)$);'
        '\\coordinate (N) at ($(A)!0.38!(C)$);'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);'
        '\\fill (A) circle (1pt) node[above] {$A$};'
        '\\fill (B) circle (1pt) node[left] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (M) circle (1pt) node[left] {$M$};'
        '\\fill (N) circle (1pt) node[right] {$N$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. '
        'Trên cạnh $AB$ lấy điểm $M$ sao cho $AM = %s\\text{ cm}$. Qua $M$ kẻ đường thẳng song song với $BC$ cắt $AC$ tại $N$.%s'
        % (AB, AC, BC, AM, tikz)
    )

    nb_da_1_d = '\\True $\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$' % fmt_num(k)
    nb_da_1_s = '$\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$' % fmt_num(Fraction(den, num))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$), theo định lí về đường thẳng song song với một cạnh của tam giác '
        'ta có $\\Delta AMN \\backsim \\Delta ABC$.\\ '
        'Tỉ số đồng dạng là $k = \\dfrac{AM}{AB} = \\dfrac{%s}{%s} = %s$.'
        % (AM, AB, fmt_num(k))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Độ dài đoạn thẳng $AN$ bằng $%s\\text{ cm}$' % AN
    th_da_1_s = 'Độ dài đoạn thẳng $AN$ bằng $%s\\text{ cm}$' % AN_sai
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Vì $\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$ nên $\\dfrac{AN}{AC} = %s$.\\ '
        'Suy ra $AN = AC \\cdot %s = %s \\cdot %s = %s\\text{ cm}$.'
        % (fmt_num(k), fmt_num(k), fmt_num(k), AC, fmt_num(k), AN)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % MN
    vd_da_1_s = 'Độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % (MN + 3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$ nên $\\dfrac{MN}{BC} = %s$.\\ '
        'Suy ra $MN = BC \\cdot %s = %s \\cdot %s = %s\\text{ cm}$.'
        % (fmt_num(k), fmt_num(k), fmt_num(k), BC, fmt_num(k), MN)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Chu vi $\\Delta AMN$ bằng $%s\\text{ cm}$' % (AM + AN + MN)
    vdc_da_1_s = 'Chu vi $\\Delta AMN$ bằng $%s\\text{ cm}$' % (AB + AC + BC)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Chu vi $\\Delta AMN$ là $P_{\\Delta AMN} = AM + AN + MN = %s + %s + %s = %s\\text{ cm}$.'
        % (AM, AN, MN, AM + AN + MN)
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
