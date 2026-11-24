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

def bt_dang12_p2_b3_c4_hh8(self):
    # Dạng 12: Bài toán chia tỉ lệ chu vi và diện tích qua đường trung bình
    cv_mnp = random.choice([16, 18, 20, 22, 24])
    cv_abc = 2 * cv_mnp
    s_mnp = random.choice([12, 15, 16, 18, 20])
    s_abc = 4 * s_mnp
    s_bmnc = 3 * s_mnp

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (1.7,3.2);\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (4.6,0);\n'
        '\\coordinate (M) at ($(A)!0.5!(B)$);\n'
        '\\coordinate (N) at ($(A)!0.5!(C)$);\n'
        '\\coordinate (P) at ($(B)!0.5!(C)$);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N)--(P)--cycle;\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (M) circle (1pt) node[left] {$M$};\n'
        '\\fill (N) circle (1pt) node[right] {$N$};\n'
        '\\fill (P) circle (1pt) node[below] {$P$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tam giác $ABC$ có chu vi bằng $%s\\text{ cm}$ và diện tích bằng $%s\\text{ cm}^2$. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $AB, AC, BC$.\n%s'
        % (cv_abc, s_abc, hinh_ve)
    )

    nb_da_1_d = '\\True Chu vi của tam giác $MNP$ bằng $%s\\text{ cm}$' % cv_mnp
    nb_da_1_s = 'Chu vi của tam giác $MNP$ bằng $%s\\text{ cm}$' % cv_abc
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì $MN, NP, MP$ là ba đường trung bình của tam giác $ABC$ nên chu vi tam giác $MNP$ bằng một nửa chu vi tam giác $ABC$, tức là $\\frac{%s}{2} = %s\\text{ cm}$.' % (cv_abc, cv_mnp)
    loigiai_nb_s = 'Sai. Chu vi tam giác $MNP$ bằng $\\frac{1}{2}$ chu vi tam giác $ABC$, tức là bằng $%s\\text{ cm}$.' % cv_mnp

    th_da_1_d = '\\True Bốn tam giác $AMN, MBP, NPC, PNM$ có chu vi bằng nhau'
    th_da_1_s = 'Chu vi tam giác $AMN$ lớn hơn chu vi tam giác $MNP$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Bốn tam giác $AMN, MBP, NPC, PNM$ có các cạnh tương ứng bằng nhau (cùng bằng nửa độ dài ba cạnh của tam giác $ABC$) nên chu vi của chúng bằng nhau và cùng bằng $%s\\text{ cm}$.' % cv_mnp
    loigiai_th_s = 'Sai. Bốn tam giác $AMN, MBP, NPC, PNM$ bằng nhau (c.c.c) nên có chu vi bằng nhau.'

    vd_da_1_d = '\\True Diện tích của tam giác $MNP$ bằng $%s\\text{ cm}^2$' % s_mnp
    vd_da_1_s = 'Diện tích của tam giác $MNP$ bằng $%s\\text{ cm}^2$' % (2 * s_mnp)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Bốn tam giác $AMN, MBP, NPC, PNM$ bằng nhau nên có diện tích bằng nhau và cùng bằng $\\frac{1}{4}$ diện tích tam giác $ABC$, tức là $\\frac{%s}{4} = %s\\text{ cm}^2$.' % (s_abc, s_mnp)
    loigiai_vd_s = 'Sai. Diện tích tam giác $MNP$ bằng $\\frac{1}{4}$ diện tích tam giác $ABC$, tức là bằng $%s\\text{ cm}^2$.' % s_mnp

    vdc_da_1_d = '\\True Diện tích hình thang $BMNC$ bằng $%s\\text{ cm}^2$' % s_bmnc
    vdc_da_1_s = 'Diện tích hình thang $BMNC$ bằng $%s\\text{ cm}^2$' % (2 * s_mnp)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Ta có $S_{BMNC} = S_{\\Delta ABC} - S_{\\Delta AMN} = %s - %s = %s\\text{ cm}^2$.' % (s_abc, s_mnp, s_bmnc)
    loigiai_vdc_s = 'Sai. Ta có $S_{BMNC} = S_{\\Delta ABC} - S_{\\Delta AMN} = %s - %s = %s\\text{ cm}^2$.' % (s_abc, s_mnp, s_bmnc)

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
