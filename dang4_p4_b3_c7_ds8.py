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

def bt_dang4_p4_b3_c7_ds8(self):
    # Dạng 4: Hàm số phân thức g(x) = (a*x + b)/(x + c) và bài toán tìm x nguyên để g(x) nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4])
        c = random.choice([1, 2, 3])
        p = random.choice([3, 5, 7]) # số nguyên tố để ước là +-1, +-p
        # g(x) = a + p/(x + c) = (a*(x + c) + p)/(x + c)
        b = a * c + p
        x_eval = -c + p
        g_eval = a + 1

        # Các giá trị nguyên của x: x + c in {-p, -1, 1, p}
        x_vals = sorted([-c - p, -c - 1, -c + 1, -c + p])
        sum_x = sum(x_vals)

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (8.5,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (8.5,0.8);\n'
            '\\draw[line width=1pt] (2.5,0) -- (2.5,1.6) (4.5,0) -- (4.5,1.6) (6.5,0) -- (6.5,1.6);\n'
            '\\node at (1.25,1.2) {$x$};\n'
            '\\node at (1.25,0.4) {$g(x)$};\n'
            '\\node at (3.5,1.2) {$%s$};\n'
            '\\node at (3.5,0.4) {$%s$};\n'
            '\\node at (5.5,1.2) {$%s$};\n'
            '\\node at (5.5,0.4) {$%s$};\n'
            '\\node at (7.5,1.2) {$%s$};\n'
            '\\node at (7.5,0.4) {$?$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (-c - 1, a - p, -c + 1, a + p, x_eval)

        noidungcauhoi = (
            'Cho hàm số $y = g(x) = \\dfrac{%sx + %s}{x + %s}$ (với $x \\neq -%s$) có bảng giá trị một số điểm nguyên như sau:\\ %s'
        ) % (a, b, c, c, bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Điều kiện để biểu thức của hàm số $g(x)$ có nghĩa là $x \\neq -%s$' % (c)
        nb_da_1_s = 'Điều kiện để biểu thức của hàm số $g(x)$ có nghĩa là $x \\neq %s$' % (c)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Mẫu thức $x + %s \\neq 0 \\Leftrightarrow x \\neq -%s$.' % (c, c)

        # Thông hiểu
        th_da_1_d = '\\True Giá trị của hàm số tại $x = %s$ là $g(%s) = %s$' % (x_eval, x_eval, g_eval)
        th_da_1_s = 'Giá trị của hàm số tại $x = %s$ là $g(%s) = %s$' % (x_eval, x_eval, g_eval + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Thay $x = %s$ vào công thức ta được $g(%s) = \\dfrac{%s \\cdot %s + %s}{%s + %s} = %s$.' % (x_eval, x_eval, a, x_eval, b, x_eval, c, g_eval)

        # Vận dụng
        vd_da_1_d = '\\True Hàm số $g(x)$ có thể viết dưới dạng tách phần nguyên là $g(x) = %s + \\dfrac{%s}{x + %s}$' % (a, p, c)
        vd_da_1_s = 'Hàm số $g(x)$ có thể viết dưới dạng tách phần nguyên là $g(x) = %s + \\dfrac{%s}{x + %s}$' % (a, b, c)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Ta có $g(x) = \\dfrac{%s(x + %s) + %s}{x + %s} = %s + \\dfrac{%s}{x + %s}$.' % (a, c, p, c, a, p, c)

        # Vận dụng cao
        vdc_da_1_d = '\\True Có đúng $4$ giá trị nguyên của $x$ để $g(x)$ nhận giá trị nguyên và tổng của chúng bằng $%s$' % (sum_x)
        vdc_da_1_s = 'Chỉ có $2$ giá trị nguyên của $x$ để $g(x)$ nhận giá trị nguyên và tổng của chúng bằng $%s$' % (-2 * c)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Để $g(x) \\in \\mathbb{Z}$ với $x \\in \\mathbb{Z}$ thì $x + %s \\in \\text{Ư}(%s) = \\{-%s; -1; 1; %s\\}$.\\ '
            'Suy ra $x \\in \\{%s; %s; %s; %s\\}$. Có $4$ giá trị nguyên của $x$ và tổng của chúng bằng $%s$.'
        ) % (c, p, p, p, x_vals[0], x_vals[1], x_vals[2], x_vals[3], sum_x)

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
