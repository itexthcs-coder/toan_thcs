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

def bt_dang15_p2_b2_c5_hh9(self):
    so_cabin = random.choice([18, 20, 24, 30, 36])
    goc_1_khoang = 360 // so_cabin
    nua_cabin = so_cabin // 2
    cb_doi = 3 + nua_cabin
    k_nho = randint(3, nua_cabin - 2)
    cb_cuoi = 2 + k_nho
    cung_nho_val = k_nho * goc_1_khoang
    cung_lon_val = 360 - cung_nho_val

    noidungcauhoi = ('''Một vòng đu quay khổng lồ có dạng đường tròn tâm $O$ gắn $%s$ cabin chở khách được bố trí cách đều nhau trên vành tròn (hình vẽ minh họa). Đánh số các cabin liên tiếp từ $1$ đến $%s$ theo chiều kim đồng hồ.
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.8);
    \\foreach \\k in {0,30,...,330} {
        \\draw[line width=1pt] (O)--(\\k:1.8);
        \\fill (\\k:1.8) circle (1.5pt);
    }
    \\fill (O) circle (1pt) node[below right] {$O$};
    \\end{tikzpicture}
    \\end{center}''' % (so_cabin, so_cabin))

    nb_da_1_d = '\\True Hai cabin liên tiếp bất kì tạo với tâm $O$ một góc ở tâm có số đo bằng $%s^\\circ$' % (goc_1_khoang)
    nb_da_1_s = 'Hai cabin liên tiếp bất kì tạo với tâm $O$ một góc ở tâm có số đo bằng $%s^\\circ$' % (goc_1_khoang * 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $%s$ cabin chia đường tròn $360^\\circ$ thành $%s$ cung bằng nhau nên góc ở tâm chắn cung giữa hai cabin liên tiếp bằng $\\dfrac{360^\\circ}{%s} = %s^\\circ$.''' % (so_cabin, so_cabin, so_cabin, goc_1_khoang))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo cung nhỏ nối từ cabin số $1$ đến cabin số $4$ bằng $%s^\\circ$' % (3 * goc_1_khoang)
    th_da_1_s = 'Số đo cung nhỏ nối từ cabin số $1$ đến cabin số $4$ bằng $%s^\\circ$' % (4 * goc_1_khoang)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Từ cabin số $1$ đến cabin số $4$ có $4 - 1 = 3$ khoảng chia đều nên số đo cung nhỏ bằng $3 \\cdot %s^\\circ = %s^\\circ$.''' % (goc_1_khoang, 3 * goc_1_khoang))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đoạn thẳng nối cabin số $3$ và cabin số $%s$ đi qua tâm $O$ của vòng đu quay' % (cb_doi)
    vd_da_1_s = 'Đoạn thẳng nối cabin số $3$ và cabin số $%s$ không đi qua tâm $O$ của vòng đu quay' % (cb_doi)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Từ cabin số $3$ đến cabin số $%s$ có $%s - 3 = %s$ khoảng, ứng với cung có số đo bằng $%s \\cdot %s^\\circ = 180^\\circ$ (nửa đường tròn). \\\\ Do đó đoạn thẳng nối hai cabin này là đường kính, tức là đi qua tâm $O$.''' % (cb_doi, cb_doi, nua_cabin, nua_cabin, goc_1_khoang))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số đo cung lớn nối từ cabin số $2$ đến cabin số $%s$ bằng $%s^\\circ$' % (cb_cuoi, cung_lon_val)
    vdc_da_1_s = 'Số đo cung lớn nối từ cabin số $2$ đến cabin số $%s$ bằng $%s^\\circ$' % (cb_cuoi, cung_nho_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Từ cabin số $2$ đến cabin số $%s$ có $%s - 2 = %s$ khoảng nên cung nhỏ có số đo bằng $%s \\cdot %s^\\circ = %s^\\circ$. \\\\ Suy ra cung lớn có số đo bằng $360^\\circ - %s^\\circ = %s^\\circ$.''' % (cb_cuoi, cb_cuoi, k_nho, k_nho, goc_1_khoang, cung_nho_val, cung_nho_val, cung_lon_val))
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
