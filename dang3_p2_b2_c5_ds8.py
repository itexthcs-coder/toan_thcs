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


def bt_dang3_p2_b2_c5_ds8(self):
    # Dạng 3 (Thông hiểu - Thuần túy toán học): Chuyển đổi biểu đồ tranh có nửa biểu tượng và tính trung bình cộng
    unit = random.choice([8, 12, 16, 20])
    half_u = unit // 2
    
    v1 = 3 * unit + half_u
    v2 = 5 * unit
    v3 = 2 * unit + half_u
    v4 = 4 * unit
    
    diff_max_min = v2 - v3
    tong = v1 + v2 + v3 + v4
    tbc = Decimal(str(tong)) / Decimal('4')
    s_tbc = str(tbc).replace(".", ",")
    s_tbc_sai = str(tbc + Decimal('3')).replace(".", ",")
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (-1.0, 0.2) rectangle (5.2, 3.4);
    \\draw[line width=1pt] (0.3, 0.2) -- (0.3, 3.4);
    \\draw[line width=1pt] (-1.0, 2.6) -- (5.2, 2.6);
    \\draw[line width=1pt] (-1.0, 1.8) -- (5.2, 1.8);
    \\draw[line width=1pt] (-1.0, 1.0) -- (5.2, 1.0);
    \\node at (-0.35, 3.0) {$X_1$};
    \\node at (-0.35, 2.2) {$X_2$};
    \\node at (-0.35, 1.4) {$X_3$};
    \\node at (-0.35, 0.6) {$X_4$};
    \\draw[line width=1pt] (0.8,2.8) rectangle (1.2,3.2) (1.5,2.8) rectangle (1.9,3.2) (2.2,2.8) rectangle (2.6,3.2) (2.9,2.8) rectangle (3.1,3.2);
    \\draw[line width=1pt] (0.8,2.0) rectangle (1.2,2.4) (1.5,2.0) rectangle (1.9,2.4) (2.2,2.0) rectangle (2.6,2.4) (2.9,2.0) rectangle (3.3,2.4) (3.6,2.0) rectangle (4.0,2.4);
    \\draw[line width=1pt] (0.8,1.2) rectangle (1.2,1.6) (1.5,1.2) rectangle (1.9,1.6) (2.2,1.2) rectangle (2.4,1.6);
    \\draw[line width=1pt] (0.8,0.4) rectangle (1.2,0.8) (1.5,0.4) rectangle (1.9,0.8) (2.2,0.4) rectangle (2.6,0.8) (2.9,0.4) rectangle (3.3,0.8);
    \\draw[line width=1pt] (0.2,-0.45) rectangle (0.6,-0.05);
    \\node[right] at (0.7,-0.25) {$= %s$ đơn vị;};
    \\draw[line width=1pt] (2.9,-0.45) rectangle (3.1,-0.05);
    \\node[right] at (3.2,-0.25) {$= %s$ đơn vị};
    \\end{tikzpicture}
    \\end{center}""" % (unit, half_u))
    
    noidungcauhoi = ("""Biểu đồ tranh dưới đây biểu diễn giá trị của bốn đại lượng $X_1, X_2, X_3, X_4$:%sXét tính đúng sai của các khẳng định sau:""" % tikz_code)
    
    nb_da_1_d = '\\True Giá trị của đại lượng $X_1$ là $%s$' % v1
    nb_da_1_s = 'Giá trị của đại lượng $X_1$ là $%s$' % (4 * unit)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Đại lượng $X_1$ gồm $3$ biểu tượng nguyên và $1$ nửa biểu tượng nên có giá trị là: $3 \\cdot %s + %s = %s$.""" % (unit, half_u, v1))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất trong bốn đại lượng là $%s$' % diff_max_min
    th_da_1_s = 'Hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất trong bốn đại lượng là $%s$' % (diff_max_min - half_u)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Ta có $X_1 = %s$, $X_2 = 5 \\cdot %s = %s$, $X_3 = 2 \\cdot %s + %s = %s$, $X_4 = 4 \\cdot %s = %s$. Hiệu giữa giá trị lớn nhất ($X_2$) và nhỏ nhất ($X_3$) là: $%s - %s = %s$."""
                    % (v1, unit, v2, unit, half_u, v3, unit, v4, v2, v3, diff_max_min))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Tổng giá trị của cả bốn đại lượng bằng $%s$' % tong
    vd_da_1_s = 'Tổng giá trị của cả bốn đại lượng bằng $%s$' % (tong + unit)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tổng giá trị của cả bốn đại lượng là: $%s + %s + %s + %s = %s$.""" % (v1, v2, v3, v4, tong))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Giá trị trung bình cộng của bốn đại lượng trên là $%s$' % s_tbc_sai
    vdc_da_1_d = 'Giá trị trung bình cộng của bốn đại lượng trên là $%s$' % s_tbc
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Giá trị trung bình cộng của bốn đại lượng trên là: $\\frac{%s}{4} = %s$.""" % (tong, s_tbc))
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
