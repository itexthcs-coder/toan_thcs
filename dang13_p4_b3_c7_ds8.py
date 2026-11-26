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

def bt_dang13_p4_b3_c7_ds8(self):
    # Dạng 13: Tìm quy luật biến thiên của hàm số y = f(x) qua bảng giá trị cách đều và tính giá trị tại điểm xa
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([-5, -4, -3, 3, 4, 5])
        b = random.choice([-2, 1, 3, 7])
        xs = [-2, -1, 0, 1, 2]
        ys = [a * x + b for x in xs]
        x_far = random.choice([8, 10, 12])
        y_far = a * x_far + b

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (10.5,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (10.5,0.8);\n'
            '\\draw[line width=1pt] (3,0) -- (3,1.6) (4.5,0) -- (4.5,1.6) (6,0) -- (6,1.6) (7.5,0) -- (7.5,1.6) (9,0) -- (9,1.6);\n'
            '\\node at (1.5,1.2) {$x$};\n'
            '\\node at (1.5,0.4) {$y = f(x)$};\n'
            '\\node at (3.75,1.2) {$-2$};\n'
            '\\node at (3.75,0.4) {$%s$};\n'
            '\\node at (5.25,1.2) {$-1$};\n'
            '\\node at (5.25,0.4) {$%s$};\n'
            '\\node at (6.75,1.2) {$0$};\n'
            '\\node at (6.75,0.4) {$%s$};\n'
            '\\node at (8.25,1.2) {$1$};\n'
            '\\node at (8.25,0.4) {$%s$};\n'
            '\\node at (9.75,1.2) {$2$};\n'
            '\\node at (9.75,0.4) {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (ys[0], ys[1], ys[2], ys[3], ys[4])

        noidungcauhoi = (
            'Cho hàm số bậc nhất $y = f(x) = ax + b$ có bảng giá trị tương ứng tại các điểm nguyên liên tiếp như sau:\\ %s'
        ) % (bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Giá trị của hàm số tại $x = 0$ là $f(0) = %s$' % (ys[2])
        nb_da_1_s = 'Giá trị của hàm số tại $x = 0$ là $f(0) = %s$' % (ys[3])
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Quan sát cột tương ứng với $x = 0$ trong bảng, ta có $f(0) = %s$.' % (ys[2])

        # Thông hiểu
        change_desc_true = 'tăng thêm $%s$ đơn vị' % (a) if a > 0 else 'giảm đi $%s$ đơn vị' % (abs(a))
        change_desc_false = 'giảm đi $%s$ đơn vị' % (a) if a > 0 else 'tăng thêm $%s$ đơn vị' % (abs(a))
        th_da_1_d = '\\True Khi giá trị của biến $x$ tăng thêm $1$ đơn vị thì giá trị tương ứng của hàm số $y$ luôn %s' % (change_desc_true)
        th_da_1_s = 'Khi giá trị của biến $x$ tăng thêm $1$ đơn vị thì giá trị tương ứng của hàm số $y$ luôn %s' % (change_desc_false)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Ta thấy $f(-1) - f(-2) = %s - (%s) = %s$, $f(0) - f(-1) = %s$, nên mỗi khi $x$ tăng $1$ đơn vị thì $y$ %s.' % (ys[1], ys[0], a, a, change_desc_true)

        # Vận dụng
        sign_b = '+' if b >= 0 else '-'
        abs_b = abs(b)
        vd_da_1_d = '\\True Công thức biểu diễn hàm số đã cho là $y = f(x) = %sx %s %s$' % (a, sign_b, abs_b)
        vd_da_1_s = 'Công thức biểu diễn hàm số đã cho là $y = f(x) = %sx %s %s$' % (-a, sign_b, abs_b)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Từ $f(0) = b = %s$ và $f(1) = a + b = %s \\Rightarrow a = %s$. Vậy $y = f(x) = %sx %s %s$.' % (b, ys[3], a, a, sign_b, abs_b)

        # Vận dụng cao
        vdc_da_1_d = '\\True Giá trị của hàm số tại $x = %s$ là $f(%s) = %s$' % (x_far, x_far, y_far)
        vdc_da_1_s = 'Giá trị của hàm số tại $x = %s$ là $f(%s) = %s$' % (x_far, x_far, y_far + a)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Thay $x = %s$ vào công thức $f(x) = %sx %s %s$, ta được $f(%s) = %s \\cdot %s %s %s = %s$.' % (x_far, a, sign_b, abs_b, x_far, a, x_far, sign_b, abs_b, y_far)

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
