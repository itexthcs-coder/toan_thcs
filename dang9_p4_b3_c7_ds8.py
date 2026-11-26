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

def bt_dang9_p4_b3_c7_ds8(self):
    # Dạng 9: Điều kiện hai điểm trùng nhau trên mặt phẳng tọa độ Oxy để tìm hai tham số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_true = random.choice([1, 2, 3])
        b_true = random.choice([-2, -1, 2, 3])
        x_N = random.choice([2, 3, 4])
        y_N = random.choice([-3, -2, 1, 4])
        # Điểm P(a + 2b; 3a - b) trùng với N(x_N; y_N)
        x_N = a_true + 2 * b_true
        y_N = 3 * a_true - b_true
        sum_ab = a_true + b_true
        prod_ab = a_true * b_true

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,2.5) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (N) at (1.8,1.5);\n'
            '\\draw[line width=1pt, dashed] (1.8,0) node[below] {$x_0$} -- (N) -- (0,1.5) node[left] {$y_0$};\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (N) circle (1pt) node[above right] {$P \\equiv N(x_0; y_0)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $Oxy$, cho điểm $P(a + 2b; 3a - b)$ và điểm $N(%s; %s)$ với $a, b$ là các tham số thực (hình minh họa):\\ %s'
        ) % (x_N, y_N, hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Hoành độ của điểm $P$ là $a + 2b$ và tung độ của điểm $P$ là $3a - b$'
        nb_da_1_s = 'Hoành độ của điểm $P$ là $3a - b$ và tung độ của điểm $P$ là $a + 2b$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Trong kí hiệu tọa độ $P(x_P; y_P)$, số viết trước là hoành độ $a + 2b$, số viết sau là tung độ $3a - b$.'

        # Thông hiểu
        th_da_1_d = '\\True Hai điểm $P$ và $N$ trùng nhau khi và chỉ khi $a + 2b = %s$ và $3a - b = %s$' % (x_N, y_N)
        th_da_1_s = 'Hai điểm $P$ và $N$ trùng nhau khi và chỉ khi $a + 2b = %s$ và $3a - b = %s$' % (y_N, x_N)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Mỗi điểm trên mặt phẳng tọa độ xác định duy nhất một cặp tọa độ nên $P \\equiv N \\Leftrightarrow \\begin{cases} x_P = x_N \\\\ y_P = y_N \\end{cases} \\Leftrightarrow \\begin{cases} a + 2b = %s \\\\ 3a - b = %s \\end{cases}$.' % (x_N, y_N)

        # Vận dụng
        vd_da_1_d = '\\True Để điểm $P$ trùng với điểm $N$ thì giá trị của hai tham số là $a = %s$ và $b = %s$' % (a_true, b_true)
        vd_da_1_s = 'Để điểm $P$ trùng với điểm $N$ thì giá trị của hai tham số là $a = %s$ và $b = %s$' % (a_true + 1, b_true - 1)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Từ $3a - b = %s \\Rightarrow b = 3a - %s$. Thay vào phương trình thứ nhất: $a + 2(3a - %s) = %s \\Leftrightarrow 7a = %s \\Leftrightarrow a = %s$.\\ '
            'Từ đó suy ra $b = 3 \\cdot %s - %s = %s$.'
        ) % (y_N, y_N, y_N, x_N, x_N + 2 * y_N, a_true, a_true, y_N, b_true)

        # Vận dụng cao
        vdc_da_1_d = '\\True Khi $P$ trùng với $N$, giá trị của biểu thức $T = a + b + ab$ bằng $%s$' % (sum_ab + prod_ab)
        vdc_da_1_s = 'Khi $P$ trùng với $N$, giá trị của biểu thức $T = a + b + ab$ bằng $%s$' % (sum_ab - prod_ab + 2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Với $a = %s$ và $b = %s$, ta tính được $T = %s + (%s) + %s \\cdot (%s) = %s$.' % (a_true, b_true, a_true, b_true, a_true, b_true, sum_ab + prod_ab)

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
