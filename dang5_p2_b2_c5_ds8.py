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


def bt_dang5_p2_b2_c5_ds8(self):
    # Dạng 5 (Vận dụng - Thuần túy toán học): Thiết lập biểu đồ hình quạt tròn từ bảng tần số thô
    k = random.choice([1, 2])
    g1, g2, g3, g4 = 135 * k, 180 * k, 90 * k, 45 * k
    tong = g1 + g2 + g3 + g4
    
    noidungcauhoi = ("""Cho bảng thống kê phân chia một tập hợp gồm $N$ phần tử thành bốn nhóm $G_1, G_2, G_3, G_4$:\\\\
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|}
    \\hline
    \\textbf{Nhóm} & $G_1$ & $G_2$ & $G_3$ & $G_4$ \\\\
    \\hline
    \\textbf{Số phần tử} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Xét tính đúng sai của các khẳng định sau:""" % (g1, g2, g3, g4))
    
    nb_da_1_d = '\\True Tổng số phần tử của tập hợp là $N = %s$' % tong
    nb_da_1_s = 'Tổng số phần tử của tập hợp là $N = %s$' % (tong + 50)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tổng số phần tử của tập hợp là: $N = %s + %s + %s + %s = %s$.""" % (g1, g2, g3, g4, tong))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Khi biểu diễn bằng biểu đồ hình quạt tròn, nhóm $G_1$ chiếm tỉ lệ $30\\%%$'
    th_da_1_s = 'Khi biểu diễn bằng biểu đồ hình quạt tròn, nhóm $G_1$ chiếm tỉ lệ $35\\%%$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tỉ lệ phần trăm của nhóm $G_1$ là: $\\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$.""" % (g1, tong))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Tỉ lệ phần trăm của nhóm $G_2$ gấp đôi tỉ lệ phần trăm của nhóm $G_3$'
    vd_da_1_s = 'Tỉ lệ phần trăm của nhóm $G_2$ gấp ba lần tỉ lệ phần trăm của nhóm $G_3$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Nhóm $G_2$ chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 40\\%%$; nhóm $G_3$ chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 20\\%%$. Vậy tỉ lệ của $G_2$ gấp đôi $G_3$.""" % (g2, tong, g3, tong))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Góc ở tâm của hình quạt tròn biểu diễn nhóm $G_4$ có số đo bằng $45^\\circ$'
    vdc_da_1_d = 'Góc ở tâm của hình quạt tròn biểu diễn nhóm $G_4$ có số đo bằng $36^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Nhóm $G_4$ chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 10\\%%$, nên góc ở tâm của hình quạt biểu diễn $G_4$ bằng $360^\\circ \\cdot 10\\%% = 36^\\circ$ (không phải $45^\\circ$).""" % (g4, tong))
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
