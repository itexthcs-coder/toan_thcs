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


def bt_dang7_p2_b2_c5_ds8(self):
    # Dạng 7 (Thông hiểu - Thuần túy toán học): Đọc biểu đồ đoạn thẳng và tính tốc độ biến thiên
    k = random.choice([1, 2])
    y1, y2, y3, y4, y5 = 120 * k, 150 * k, 135 * k, 180 * k, 225 * k
    inc_max = 45 * k
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {$y$};
    \\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[right] {$t$};
    \\coordinate (A) at (0.8,0.6);
    \\coordinate (B) at (2.0,1.2);
    \\coordinate (C) at (3.2,0.9);
    \\coordinate (D) at (4.4,1.8);
    \\coordinate (E) at (5.5,2.5);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(E);
    \\fill (A) circle (1pt) node[above left] {$%s$};
    \\fill (B) circle (1pt) node[above] {$%s$};
    \\fill (C) circle (1pt) node[below] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\fill (E) circle (1pt) node[above] {$%s$};
    \\node[below] at (0.8,0) {$t_1$};
    \\node[below] at (2.0,0) {$t_2$};
    \\node[below] at (3.2,0) {$t_3$};
    \\node[below] at (4.4,0) {$t_4$};
    \\node[below] at (5.5,0) {$t_5$};
    \\end{tikzpicture}
    \\end{center}""" % (y1, y2, y3, y4, y5))
    
    noidungcauhoi = ("""Cho biểu đồ đoạn thẳng ghi lại giá trị của hàm số $y = f(t)$ tại các mốc thời điểm $t_1, t_2, t_3, t_4, t_5$:%sXét tính đúng sai của các khẳng định sau:""" % tikz_code)
    
    nb_da_1_d = '\\True Đại lượng $y$ có xu hướng giảm trong khoảng thời gian từ $t_2$ đến $t_3$'
    nb_da_1_s = 'Đại lượng $y$ có xu hướng tăng trong khoảng thời gian từ $t_2$ đến $t_3$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Từ $t_2$ đến $t_3$, đoạn thẳng đi xuống (giá trị giảm từ $%s$ xuống $%s$) nên đại lượng $y$ có xu hướng giảm.""" % (y2, y3))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Mức tăng tuyệt đối lớn nhất giữa hai mốc liên tiếp là $%s$ đơn vị' % inc_max
    th_da_1_s = 'Mức tăng tuyệt đối lớn nhất giữa hai mốc liên tiếp là $%s$ đơn vị' % (30 * k)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Từ $t_3$ đến $t_4$ tăng $%s - %s = %s$; từ $t_4$ đến $t_5$ tăng $%s - %s = %s$. Đây là mức tăng tuyệt đối lớn nhất giữa hai mốc liên tiếp.""" % (y4, y3, inc_max, y5, y4, inc_max))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True So với mốc $t_1$, giá trị tại mốc $t_2$ đã tăng thêm $25\\%%$'
    vd_da_1_s = 'So với mốc $t_1$, giá trị tại mốc $t_2$ đã tăng thêm $20\\%%$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tỉ lệ phần trăm tăng thêm từ $t_1$ đến $t_2$ là: $\\dfrac{%s - %s}{%s} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = 25\\%%$.""" % (y2, y1, y1, y2 - y1, y1))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Tỉ lệ phần trăm tăng thêm từ $t_3$ đến $t_4$ bằng tỉ lệ phần trăm tăng thêm từ $t_4$ đến $t_5$'
    vdc_da_1_d = 'Tỉ lệ phần trăm tăng thêm từ $t_3$ đến $t_4$ lớn hơn tỉ lệ phần trăm tăng thêm từ $t_4$ đến $t_5$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Từ $t_3$ đến $t_4$ tăng $\\dfrac{%s}{%s} \\cdot 100\\%% = 33,3\\%%$, còn từ $t_4$ đến $t_5$ tăng $\\dfrac{%s}{%s} \\cdot 100\\%% = 25\\%%$ nên hai tỉ lệ này không bằng nhau.""" % (inc_max, y3, inc_max, y4))
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
