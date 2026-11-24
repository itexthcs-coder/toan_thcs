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
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang1_p2_b2_c4_hh8(self):
    A, B, C, M, N = random.choice([('A', 'B', 'C', 'M', 'N'), ('D', 'E', 'F', 'H', 'K')])
    bc = random.choice([12, 14, 16, 18, 20, 22, 24])
    mn = bc // 2
    goc_b = random.choice([50, 55, 60, 65, 70, 75])
    goc_bu = 180 - goc_b

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (1.5,3);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4.5,0);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s);
\\fill (%s) circle (1pt) node[above] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, M, A, B, N, A, C, A, B, C, M, N, A, A, B, B, C, C, M, M, N, N))

    noidungcauhoi = ('''Cho tam giác $%s%s%s$ có $%s%s = %s\\text{ cm}$, $\\widehat{%s%s%s} = %s^\\circ$. Gọi $%s, %s$ lần lượt là trung điểm của các cạnh $%s%s$ và $%s%s$ (như hình vẽ).%s''' % (A, B, C, B, C, fmt_num(bc), A, B, C, goc_b, M, N, A, B, A, C, hinhve))

    nb_da_1_d = '\\True Đoạn thẳng $%s%s$ là đường trung bình của tam giác $%s%s%s$' % (M, N, A, B, C)
    nb_da_1_s = 'Đoạn thẳng $%s%s$ là đường trung tuyến của tam giác $%s%s%s$' % (M, N, A, B, C)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Vì $%s, %s$ lần lượt là trung điểm của hai cạnh $%s%s$ và $%s%s$ nên đoạn thẳng $%s%s$ nối trung điểm hai cạnh của tam giác $%s%s%s$. Do đó $%s%s$ là đường trung bình của tam giác $%s%s%s$.' % (M, N, A, B, A, C, M, N, A, B, C, M, N, A, B, C)]

    th_da_1_d = '\\True Độ dài đoạn thẳng $%s%s$ bằng $%s\\text{ cm}$' % (M, N, fmt_num(mn))
    th_da_1_s = 'Độ dài đoạn thẳng $%s%s$ bằng $%s\\text{ cm}$' % (M, N, fmt_num(bc))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Theo tính chất đường trung bình của tam giác, ta có $%s%s = \\dfrac{1}{2}%s%s = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (M, N, B, C, fmt_num(bc), fmt_num(mn))]

    vd_da_1_d = '\\True Số đo của góc $\\widehat{%s%s%s}$ bằng $%s^\\circ$' % (A, M, N, goc_b)
    vd_da_1_s = 'Số đo của góc $\\widehat{%s%s%s}$ bằng $%s^\\circ$' % (A, M, N, goc_bu)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Vì $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$. Suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s} = %s^\\circ$ (hai góc đồng vị).' % (M, N, A, B, C, M, N, B, C, A, M, N, A, B, C, goc_b)]

    vdc_da_1_d = '\\True Đường thẳng qua $%s$ song song với $%s%s$ cắt $%s%s$ tại trung điểm của cạnh $%s%s$' % (N, A, B, B, C, B, C)
    vdc_da_1_s = 'Đường thẳng qua $%s$ song song với $%s%s$ cắt $%s%s$ tại trọng tâm của tam giác $%s%s%s$' % (N, A, B, B, C, A, B, C)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Trong tam giác $%s%s%s$, đường thẳng đi qua trung điểm $%s$ của cạnh $%s%s$ và song song với cạnh $%s%s$ thì đi qua trung điểm của cạnh thứ ba $%s%s$ (chú ý về tính chất đường trung bình).' % (A, B, C, N, A, C, A, B, B, C)]

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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
