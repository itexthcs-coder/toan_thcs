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

def bt_dang2_p4_b3_c7_ds8(self):
    # Dạng 2: Hàm số dạng y = a*x^2 + b và tính chất f(-x) = f(x)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([-3, -2, 2, 3])
        b = random.choice([-4, -1, 1, 4, 5])
        x0 = random.choice([1, 2, 3])
        y0 = a * (x0 ** 2) + b
        x_target = random.choice([2, 3, 4])
        while x_target == x0:
            x_target = random.choice([2, 3, 4])
        y_target = a * (x_target ** 2) + b

        sign_b = '+' if b >= 0 else '-'
        abs_b = abs(b)

        # Hình vẽ minh họa 3 điểm (-x0, y0), (0, b), (x0, y0)
        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1.5) -- (0,3) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-1.5,2);\n'
            '\\coordinate (B) at (1.5,2);\n'
            '\\coordinate (C) at (0,0.8);\n'
            '\\draw[line width=1pt, dashed] (-1.5,0) -- (A) -- (B) -- (1.5,0);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (A) circle (1pt) node[above left] {$M(-x_0; y_0)$};\n'
            '\\fill (B) circle (1pt) node[above right] {$N(x_0; y_0)$};\n'
            '\\fill (C) circle (1pt) node[right] {$P(0; b)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hàm số $y = f(x) = %sx^2 %s %s$ với tập xác định là tập hợp số thực $\\mathbb{R}$ và hình minh họa các điểm thuộc đồ thị hàm số dưới đây:\\ %s'
        ) % (a, sign_b, abs_b, hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Giá trị của hàm số tại $x = 0$ là $f(0) = %s$' % (b)
        nb_da_1_s = 'Giá trị của hàm số tại $x = 0$ là $f(0) = %s$' % (a + b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Thay $x = 0$ vào công thức hàm số ta được $f(0) = %s \\cdot 0^2 %s %s = %s$.' % (a, sign_b, abs_b, b)

        # Thông hiểu
        th_da_1_d = '\\True Với $x = %s$ và $x = -%s$, hàm số nhận cùng một giá trị bằng $%s$' % (x0, x0, y0)
        th_da_1_s = 'Với $x = %s$ và $x = -%s$, hàm số nhận hai giá trị đối nhau là $%s$ và $%s$' % (x0, x0, y0, -y0)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Ta có $f(%s) = %s \\cdot (%s)^2 %s %s = %s$ và $f(-%s) = %s \\cdot (-%s)^2 %s %s = %s$.\\ '
            'Vậy $f(%s) = f(-%s) = %s$.'
        ) % (x0, a, x0, sign_b, abs_b, y0, x0, a, x0, sign_b, abs_b, y0, x0, x0, y0)

        # Vận dụng
        vd_da_1_d = '\\True Có đúng $2$ giá trị của biến số $x$ để $f(x) = %s$, đó là $x = %s$ và $x = -%s$' % (y_target, x_target, x_target)
        vd_da_1_s = 'Chỉ có duy nhất $1$ giá trị của biến số $x$ để $f(x) = %s$, đó là $x = %s$' % (y_target, x_target)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Xét $f(x) = %s \\Leftrightarrow %sx^2 %s %s = %s \\Leftrightarrow %sx^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$.'
        ) % (y_target, a, sign_b, abs_b, y_target, a, y_target - b, x_target ** 2, x_target, x_target)

        # Vận dụng cao
        vdc_da_1_d = '\\True Biểu thức $y = f(x)$ vẫn xác định một hàm số của $x$ dù hai giá trị đối nhau của $x$ cho cùng một giá trị của $y$'
        vdc_da_1_s = 'Biểu thức $y = f(x)$ không phải là hàm số của $x$ vì có hai giá trị của $x$ cho cùng một giá trị của $y$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Theo định nghĩa hàm số, mỗi giá trị của $x$ chỉ cho duy nhất một giá trị tương ứng của $y$. '
            'Việc hai giá trị khác nhau của $x$ (như $x = %s$ và $x = -%s$) cho cùng một giá trị $y = %s$ không vi phạm định nghĩa hàm số.'
        ) % (x0, x0, y0)

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
