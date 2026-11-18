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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang12_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    a1, a2, a3 = 10 * k, 18 * k, 12 * k
    b1, b2, b3 = 15 * k, 27 * k, 18 * k
    nA, nB = 40 * k, 60 * k
    n_tong = nA + nB
    m2_tong = a2 + b2

    noidungcauhoi = ('''Kết quả đo tốc độ giao bóng (đơn vị: $\\text{km/h}$) của các vận động viên quần vợt tại hai bảng đấu A và B được thống kê trong bảng sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|}
\\hline
Tốc độ ($\\text{km/h}$) & $[160; 170)$ & $[170; 180)$ & $[180; 190)$ \\\\
\\hline
Số VĐV bảng A & $%s$ & $%s$ & $%s$ \\\\
\\hline
Số VĐV bảng B & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Người ta gộp dữ liệu của cả hai bảng đấu thành một bảng thống kê chung.''' % (a1, a2, a3, b1, b2, b3))

    list_nb_da_1 = [
        '\\True Cỡ mẫu của bảng thống kê chung là $%s$ vận động viên' % n_tong,
        'Cỡ mẫu của bảng thống kê chung là $%s$ vận động viên' % (n_tong - 10)
    ]
    loigiai_nb_1 = ('''Tổng số vận động viên của cả hai bảng là $n = %s + %s = %s$ (người).''' % (nA, nB, n_tong))

    list_th_da_1 = [
        '\\True Tần số của nhóm $[170; 180)$ trong bảng thống kê chung là $%s$' % m2_tong,
        'Tần số của nhóm $[170; 180)$ trong bảng thống kê chung là $%s$' % (a1 + b1)
    ]
    loigiai_th_1 = ('''Tần số của nhóm $[170; 180)$ khi gộp hai bảng là $%s + %s = %s$.''' % (a2, b2, m2_tong))

    list_vd_da_1 = [
        '\\True Tần số tương đối của nhóm $[180; 190)$ ở bảng A bằng với ở bảng B',
        'Tần số tương đối của nhóm $[180; 190)$ ở bảng A lớn hơn ở bảng B'
    ]
    loigiai_vd_1 = ('''Tần số tương đối nhóm $[180; 190)$ ở bảng A là $\\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$; ở bảng B là $\\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$, hai tỉ lệ này bằng nhau.''' % (a3, nA, b3, nB))

    list_vdc_da_1 = [
        '\\True Trong bảng thống kê chung, tỉ lệ vận động viên giao bóng đạt tốc độ từ $170\\text{ km/h}$ trở lên là $75\\%%$',
        'Trong bảng thống kê chung, tỉ lệ vận động viên giao bóng đạt tốc độ từ $170\\text{ km/h}$ trở lên là $70\\%%$'
    ]
    loigiai_vdc_1 = ('''Số VĐV giao bóng từ $170\\text{ km/h}$ trở lên là $%s + %s = %s$ (người), chiếm tỉ lệ $\\dfrac{%s}{%s} \\cdot 100\\%% = 75\\%%$.''' % (m2_tong, a3 + b3, m2_tong + a3 + b3, m2_tong + a3 + b3, n_tong))

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
