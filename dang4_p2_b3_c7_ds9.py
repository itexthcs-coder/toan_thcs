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


def bt_dang4_p2_b3_c7_ds9(self):
    n = random.choice([80, 120])
    m1 = (n * 15) // 100
    m4 = (n * 20) // 100

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Điện năng ($\\text{kWh}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1,0) rectangle (2,1.05);
\\node[above] at (1.5,1.05) {$15\\%%$};
\\draw[line width=1pt] (2,0) rectangle (3,2.45);
\\node[above] at (2.5,2.45) {$35\\%%$};
\\draw[line width=1pt] (3,0) rectangle (4,2.1);
\\node[above] at (3.5,2.1) {$30\\%%$};
\\draw[line width=1pt] (4,0) rectangle (5,1.4);
\\node[above] at (4.5,1.4) {$20\\%%$};
\\node[below] at (1,0) {$100$};
\\node[below] at (2,0) {$150$};
\\node[below] at (3,0) {$200$};
\\node[below] at (4,0) {$250$};
\\node[below] at (5,0) {$300$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Biểu đồ tần số tương đối ghép nhóm dạng cột dưới đây biểu diễn lượng điện năng tiêu thụ trong tháng (đơn vị: $\\text{kWh}$) của $%s$ hộ gia đình ở một khu phố:
%s''' % (n, tikz_code))

    list_nb_da_1 = [
        '\\True Hai cột biểu diễn nhóm $[150; 200)$ và $[200; 250)$ có chung một cạnh đứng trên biểu đồ',
        'Hai cột biểu diễn nhóm $[150; 200)$ và $[200; 250)$ được vẽ tách rời nhau trên biểu đồ'
    ]
    loigiai_nb_1 = ('''Trên biểu đồ tần số tương đối ghép nhóm dạng cột, các cột hình chữ nhật của hai nhóm liên tiếp được dựng kề nhau nên có chung một cạnh đứng.''')

    list_th_da_1 = [
        '\\True Có $%s$ hộ gia đình tiêu thụ dưới $150\\text{ kWh}$ điện trong tháng' % m1,
        'Có $%s$ hộ gia đình tiêu thụ dưới $150\\text{ kWh}$ điện trong tháng' % (m1 + 8)
    ]
    loigiai_th_1 = ('''Số hộ gia đình tiêu thụ dưới $150\\text{ kWh}$ (thuộc nhóm $[100; 150)$) là: $\\dfrac{%s \\cdot 15}{100} = %s$ (hộ).''' % (n, m1))

    list_vd_da_1 = [
        '\\True Có đúng một nửa số hộ gia đình trong khu phố tiêu thụ từ $200\\text{ kWh}$ trở lên',
        'Hơn một nửa số hộ gia đình trong khu phố tiêu thụ từ $200\\text{ kWh}$ trở lên'
    ]
    loigiai_vd_1 = ('''Tỉ lệ hộ gia đình tiêu thụ từ $200\\text{ kWh}$ trở lên là $30\\%% + 20\\%% = 50\\%%$, tức đúng một nửa số hộ gia đình.''')

    list_vdc_da_1 = [
        '\\True Nếu mức điện tiêu thụ từ $250\\text{ kWh}$ trở lên bị tính giá bậc cao thì có $%s$ hộ rơi vào nhóm này' % m4,
        'Nếu mức điện tiêu thụ từ $250\\text{ kWh}$ trở lên bị tính giá bậc cao thì có $%s$ hộ rơi vào nhóm này' % (m4 + 6)
    ]
    loigiai_vdc_1 = ('''Số hộ gia đình thuộc nhóm $[250; 300)$ là: $\\dfrac{%s \\cdot 20}{100} = %s$ (hộ).''' % (n, m4))

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
