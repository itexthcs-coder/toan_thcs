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

def bt_dang6_p2_b3_c4_hh8(self):
    # Dạng 6: Phân tích đường trung bình kết hợp trực tâm tam giác vuông
    bo_dinh = [
        ('A', 'B', 'C', 'H', 'I', 'K'),
        ('D', 'E', 'F', 'H', 'M', 'N')
    ]
    A, B, C, H, I, K = random.choice(bo_dinh)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (%s) at (1.5,2.5);\n'
        '\\coordinate (%s) at (0,0);\n'
        '\\coordinate (%s) at (4.5,0);\n'
        '\\coordinate (%s) at (1.5,0);\n'
        '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
        '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
        '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s);\n'
        '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[right] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (A, B, C, H, I, A, H, K, H, B, A, B, C, A, H, I, K, A, K, C, I, A, A, B, B, C, C, H, H, I, I, K, K)

    noidungcauhoi = (
        'Cho tam giác $%s%s%s$ vuông tại $%s$, đường cao $%s%s$ ($%s \\in %s%s$). Gọi $%s$ và $%s$ lần lượt là trung điểm của $%s%s$ và $%s%s$.\n%s'
        % (A, B, C, A, A, H, H, B, C, I, K, A, H, H, B, hinh_ve)
    )

    nb_da_1_d = '\\True $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$' % (I, K, A, B, H, I, K, A, B)
    nb_da_1_s = '$%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$' % (I, K, A, H, C, I, K, A, C)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì $%s$ là trung điểm của $%s%s$ và $%s$ là trung điểm của $%s%s$ nên $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s // %s%s$.' % (I, A, H, K, B, H, I, K, A, B, H, I, K, A, B)
    loigiai_nb_s = 'Sai. $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$.' % (I, K, A, B, H, I, K, A, B)

    th_da_1_d = '\\True $%s%s \\perp %s%s$' % (I, K, A, C)
    th_da_1_s = '$%s%s // %s%s$' % (I, K, A, C)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Vì $%s%s // %s%s$ và $%s%s \\perp %s%s$ (do tam giác $%s%s%s$ vuông tại $%s$) nên $%s%s \\perp %s%s$.' % (I, K, A, B, A, B, A, C, A, B, C, A, I, K, A, C)
    loigiai_th_s = 'Sai. Vì $%s%s // %s%s$ mà $%s%s \\perp %s%s$ nên $%s%s \\perp %s%s$.' % (I, K, A, B, A, B, A, C, I, K, A, C)

    vd_da_1_d = '\\True Điểm $%s$ là trực tâm của tam giác $%s%s%s$' % (I, A, K, C)
    vd_da_1_s = 'Điểm $%s$ là trực tâm của tam giác $%s%s%s$' % (K, A, I, C)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Trong tam giác $%s%s%s$, hai đường cao $%s%s$ ($%s%s \\perp %s%s$) và $%s%s$ ($%s%s \\perp %s%s$) cắt nhau tại $%s$ nên $%s$ là trực tâm của tam giác $%s%s%s$.' % (A, K, C, A, H, A, H, K, C, K, I, K, I, A, C, I, I, A, K, C)
    loigiai_vd_s = 'Sai. Điểm $%s$ là giao điểm của hai đường cao $%s%s$ và $%s%s$ trong tam giác $%s%s%s$ nên $%s$ là trực tâm của tam giác $%s%s%s$.' % (I, A, H, K, I, A, K, C, I, A, K, C)

    vdc_da_1_d = '\\True $%s%s \\perp %s%s$' % (A, K, C, I)
    vdc_da_1_s = '$%s%s // %s%s$' % (A, K, C, I)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Vì $%s$ là trực tâm của tam giác $%s%s%s$ nên $%s%s$ là đường cao thứ ba, suy ra $%s%s \\perp %s%s$.' % (I, A, K, C, C, I, C, I, A, K)
    loigiai_vdc_s = 'Sai. Vì $%s$ là trực tâm của tam giác $%s%s%s$ nên $%s%s \\perp %s%s$.' % (I, A, K, C, A, K, C, I)

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
