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
from PyQt5.QtGui import QTextCursor, QFont
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
from mpl_toolkits.mplot3d import Axes3D








def bt_dang1_p2_b3_c5_hh9(self):
    R_val = random.choice([3, 6, 9, 12])
    goc_nho = random.choice([120, 150])
    goc_lon = 360 - goc_nho

    l_nho = Rational(goc_nho, 180) * R_val * pi
    l_lon = Rational(goc_lon, 180) * R_val * pi
    ti_so = Rational(goc_nho, 360)
    hieu_l = l_lon - l_nho

    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8]
        \\draw (0,0) circle (1.8cm);
        \\draw (0,0) -- (0:1.8cm) node[right] {$B$};
        \\draw (0,0) -- (%d:1.8cm) node[above left] {$A$};
        \\draw (0.45,0) arc (0:%d:0.45cm);
        \\node at (%d:0.85cm) {$%d^\\circ$};
        \\fill (0,0) circle (1.5pt) node[below left] {$O$};
    \\end{tikzpicture}
    \\end{center}''' % (goc_nho, goc_nho, goc_nho//2, goc_nho))

    noidungcauhoi = ('''Cho đường tròn $(O; %d\\text{ cm})$ và hai điểm $A, B$ nằm trên đường tròn sao cho góc ở tâm $\\widehat{AOB} = %d^\\circ$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s''' % (R_val, goc_nho, hinh_ve))

    nb_da_1_d = '\\True Số đo cung lớn $\\overparen{AB}$ bằng $%d^\\circ$' % goc_lon
    nb_da_1_s = 'Số đo cung lớn $\\overparen{AB}$ bằng $%d^\\circ$' % (180 - goc_nho)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Số đo cung nhỏ $\\overparen{AB}$ bằng $\\widehat{AOB} = %d^\\circ$. Suy ra số đo cung lớn $\\overparen{AB}$ là $360^\\circ - %d^\\circ = %d^\\circ$.''' % (goc_nho, goc_nho, goc_lon))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Độ dài cung nhỏ $\\overparen{AB}$ bằng $%s\\text{ cm}$' % latex(l_nho)
    th_da_1_s = 'Độ dài cung nhỏ $\\overparen{AB}$ bằng $%s\\text{ cm}$' % latex(l_nho + pi)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Độ dài cung nhỏ $\\overparen{AB}$ là $l_1 = \\dfrac{%d}{180}\\pi \\cdot %d = %s\\text{ (cm)}$.''' % (goc_nho, R_val, latex(l_nho)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tỉ số giữa độ dài cung nhỏ $\\overparen{AB}$ và độ dài cả đường tròn $(O; %d\\text{ cm})$ bằng $%s$' % (R_val, latex(ti_so))
    vd_da_1_s = 'Tỉ số giữa độ dài cung nhỏ $\\overparen{AB}$ và độ dài cả đường tròn $(O; %d\\text{ cm})$ bằng $%s$' % (R_val, latex(Rational(goc_nho, 180)))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Tỉ số giữa độ dài cung nhỏ $\\overparen{AB}$ và độ dài cả đường tròn là $\\dfrac{l_1}{C} = \\dfrac{%d}{360} = %s$.''' % (goc_nho, latex(ti_so)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Hiệu độ dài giữa cung lớn $\\overparen{AB}$ và cung nhỏ $\\overparen{AB}$ bằng $%s\\text{ cm}$' % latex(hieu_l)
    vdc_da_1_s = 'Hiệu độ dài giữa cung lớn $\\overparen{AB}$ và cung nhỏ $\\overparen{AB}$ bằng $%s\\text{ cm}$' % latex(hieu_l + pi)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Độ dài cung lớn $\\overparen{AB}$ là $l_2 = \\dfrac{%d}{180}\\pi \\cdot %d = %s\\text{ (cm)}$. \\\\ Hiệu độ dài hai cung là $l_2 - l_1 = %s - %s = %s\\text{ (cm)}$.''' % (goc_lon, R_val, latex(l_lon), latex(l_lon), latex(l_nho), latex(hieu_l)))
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
