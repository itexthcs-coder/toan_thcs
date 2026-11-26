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

def bt_dang14_p4_b3_c7_ds8(self):
    # Dạng 14: Đồ thị hàm số gồm 5 điểm rời rạc trên mặt phẳng tọa độ Oxy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        y_common = random.choice([2, 3])
        y_N = random.choice([-1, 0])
        y_P = random.choice([-2, -3])
        y_R = random.choice([4, 5])
        # M(-3, y_common), N(-1, y_N), P(0, y_P), Q(2, y_common), R(3, y_R)
        expr_val = y_common + y_common - 2 * y_P

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-4,0) -- (4.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-3.5) -- (0,5.5) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (M) at (-3,%s);\n'
            '\\coordinate (N) at (-1,%s);\n'
            '\\coordinate (P) at (0,%s);\n'
            '\\coordinate (Q) at (2,%s);\n'
            '\\coordinate (R) at (3,%s);\n'
            '\\draw[line width=1pt, dashed] (-3,0) -- (M) -- (0,%s);\n'
            '\\draw[line width=1pt, dashed] (2,0) -- (Q) -- (0,%s);\n'
            '\\draw[line width=1pt, dashed] (3,0) -- (R) -- (0,%s);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (M) circle (1pt) node[above left] {$M(-3;%s)$};\n'
            '\\fill (N) circle (1pt) node[below left] {$N(-1;%s)$};\n'
            '\\fill (P) circle (1pt) node[right] {$P(0;%s)$};\n'
            '\\fill (Q) circle (1pt) node[above right] {$Q(2;%s)$};\n'
            '\\fill (R) circle (1pt) node[above right] {$R(3;%s)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (y_common, y_N, y_P, y_common, y_R, y_common, y_common, y_R, y_common, y_N, y_P, y_common, y_R)

        noidungcauhoi = (
            'Đồ thị của hàm số $y = f(x)$ chỉ gồm $5$ điểm $M, N, P, Q, R$ trên mặt phẳng tọa độ $Oxy$ như hình vẽ dưới đây:\\ %s'
        ) % (hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Tập xác định của hàm số $y = f(x)$ gồm $5$ giá trị của $x$ là $\\{-3; -1; 0; 2; 3\\}$'
        nb_da_1_s = 'Tập xác định của hàm số $y = f(x)$ là toàn bộ tập hợp số thực $\\mathbb{R}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Vì đồ thị hàm số chỉ gồm $5$ điểm $M, N, P, Q, R$ nên biến số $x$ chỉ nhận $5$ giá trị tương ứng là hoành độ của các điểm đó: $-3; -1; 0; 2; 3$.'

        # Thông hiểu
        th_da_1_d = '\\True Giá trị của hàm số tại $x = 0$ là $f(0) = %s$ và tại $x = 3$ là $f(3) = %s$' % (y_P, y_R)
        th_da_1_s = 'Giá trị của hàm số tại $x = 0$ là $f(0) = %s$ và tại $x = 3$ là $f(3) = %s$' % (y_R, y_P)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Từ tọa độ điểm $P(0; %s)$ suy ra $f(0) = %s$; từ tọa độ điểm $R(3; %s)$ suy ra $f(3) = %s$.' % (y_P, y_P, y_R, y_R)

        # Vận dụng
        vd_da_1_d = '\\True Giá trị của biểu thức $B = f(-3) + f(2) - 2f(0)$ bằng $%s$' % (expr_val)
        vd_da_1_s = 'Giá trị của biểu thức $B = f(-3) + f(2) - 2f(0)$ bằng $%s$' % (expr_val + 2 * y_P)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Ta có $B = f(-3) + f(2) - 2f(0) = %s + %s - 2 \\cdot (%s) = %s$.' % (y_common, y_common, y_P, expr_val)

        # Vận dụng cao
        vdc_da_1_d = '\\True Có đúng hai giá trị của $x$ để $f(x) = %s$, đó là $x = -3$ và $x = 2$' % (y_common)
        vdc_da_1_s = 'Chỉ có duy nhất một giá trị của $x$ để $f(x) = %s$, đó là $x = 2$' % (y_common)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Trên đồ thị có hai điểm có tung độ bằng $%s$ là $M(-3; %s)$ và $Q(2; %s)$, nên $f(x) = %s \\Leftrightarrow x \\in \\{-3; 2\\}$.' % (y_common, y_common, y_common, y_common)

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
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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

        content = (
            '\\begin{minipage}{\\textwidth} \n'
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
            '\\end{ex}\n \\end{minipage}\n\n'
        )
        return content
