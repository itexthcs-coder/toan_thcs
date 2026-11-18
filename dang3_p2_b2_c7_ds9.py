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


def bt_dang3_p2_b2_c7_ds9(self):
    n = random.choice([150, 200, 250])
    m1 = int(n * 54 / 100)
    m2 = int(n * 16 / 100)
    m3 = int(n * 22 / 100)
    m4 = int(n * 8 / 100)
    hieu_13 = m1 - m3

    hinh_cot = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt, ->] (0,0) -- (6.5,0) node[right] {Phương tiện};\n'
        '\\draw[line width=1pt, ->] (0,0) -- (0,3.5) node[above] {Tỉ lệ ($\\%$)};\n'
        '\\foreach \\y/\\lbl in {1/20, 2/40, 3/60} {\n'
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (6.0,\\y);\n'
        '    \\node[left] at (0,\\y) {$\\lbl\\%$};\n'
        '}\n'
        '\\draw[line width=1pt] (0.7,0) rectangle (1.3,2.7); \\node[above] at (1.0,2.7) {$54\\%$}; \\node[below] at (1.0,0) {Xe máy};\n'
        '\\draw[line width=1pt] (2.2,0) rectangle (2.8,0.8); \\node[above] at (2.5,0.8) {$16\\%$}; \\node[below] at (2.5,0) {Ô tô};\n'
        '\\draw[line width=1pt] (3.7,0) rectangle (4.3,1.1); \\node[above] at (4.0,1.1) {$22\\%$}; \\node[below] at (4.0,0) {Xe buýt};\n'
        '\\draw[line width=1pt] (5.2,0) rectangle (5.8,0.4); \\node[above] at (5.5,0.4) {$8\\%$}; \\node[below] at (5.5,0) {Xe đạp};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = ('Biểu đồ cột dưới đây biểu diễn tần số tương đối các loại phương tiện mà $%s$ nhân viên một công ty sử dụng để đi làm hằng ngày:%sXét tính đúng sai của các khẳng định sau:' % (n, hinh_cot))

    nb_da_1_d = '\\True Tổng các tần số tương đối của bốn loại phương tiện trên bằng $100\\%$'
    nb_da_1_s = 'Phương tiện được sử dụng nhiều thứ hai là Ô tô cá nhân'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tổng các tần số tương đối là $54\\% + 16\\% + 22\\% + 8\\% = 100\\%$, và phương tiện đứng thứ hai là Xe buýt ($22\\%$).')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số nhân viên đi làm bằng xe máy nhiều hơn số nhân viên đi bằng xe buýt là $%s$ người' % (hieu_13)
    th_da_1_s = 'Số nhân viên đi làm bằng xe máy nhiều hơn số nhân viên đi bằng xe buýt là $%s$ người' % (hieu_13 + 10)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Số nhân viên đi xe máy là $%s \\cdot 54\\%% = %s$ người; số nhân viên đi xe buýt là $%s \\cdot 22\\%% = %s$ người. Chênh lệch là $%s - %s = %s$ người.' % (n, m1, n, m3, m1, m3, hieu_13))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Có đúng $%s$ nhân viên đi làm bằng ô tô cá nhân' % (m2)
    vd_da_1_s = 'Có đúng $%s$ nhân viên đi làm bằng ô tô cá nhân' % (m2 + 6)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Số nhân viên đi làm bằng ô tô cá nhân là $%s \\cdot 16\\%% = %s$ người.' % (n, m2))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số nhân viên đi làm bằng xe đạp chiếm tỉ lệ ít nhất và bằng $%s$ người' % (m4)
    vdc_da_1_s = 'Số nhân viên đi làm bằng xe đạp chiếm tỉ lệ ít nhất và bằng $8$ người'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Xe đạp chiếm $8\\%%$ (ít nhất), tương ứng với số nhân viên là $%s \\cdot 8\\%% = %s$ người.' % (n, m4))
    list_vdc_2 = [loigiai_vdc_1]
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

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
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
            '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
