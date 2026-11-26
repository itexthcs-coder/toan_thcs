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

def bt_dang1_p4_b3_c7_ds8(self):
    # Dạng 1: Hàm số bậc nhất chứa tham số xác định qua giá trị cho trước và tính chất đồng biến/nghịch biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([-4, -3, -2, 2, 3, 4, 5])
        m_val = random.choice([-3, -2, -1, 1, 2, 3, 4])
        k = random.choice([1, 2, 3])
        # f(x) = (m - k)*x + 2*m + b_const -> đặt a = m_val - k => m_val = a + k
        m_true = a + k
        b_true = random.choice([-5, -3, -1, 1, 3, 5])
        c_const = b_true - 2 * m_true
        x1 = random.choice([-2, -1, 1, 2])
        y1 = a * x1 + b_true
        x2 = x1 + random.choice([2, 3])
        y2 = a * x2 + b_true
        x3 = random.choice([3, 4, 5])
        y3 = a * x3 + b_true

        sign_c = '+' if c_const >= 0 else '-'
        abs_c = abs(c_const)
        sign_b = '+' if b_true >= 0 else '-'
        abs_b = abs(b_true)

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (8,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (8,0.8);\n'
            '\\draw[line width=1pt] (2,0) -- (2,1.6) (4,0) -- (4,1.6) (6,0) -- (6,1.6);\n'
            '\\node at (1,1.2) {$x$};\n'
            '\\node at (1,0.4) {$y = f(x)$};\n'
            '\\node at (3,1.2) {$%s$};\n'
            '\\node at (3,0.4) {$%s$};\n'
            '\\node at (5,1.2) {$%s$};\n'
            '\\node at (5,0.4) {$%s$};\n'
            '\\node at (7,1.2) {$%s$};\n'
            '\\node at (7,0.4) {$?$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (x1, y1, x2, y2, x3)

        noidungcauhoi = (
            'Cho hàm số $y = f(x) = (m - %s)x + 2m %s %s$ (với $m$ là tham số) có một phần bảng giá trị tương ứng như hình vẽ dưới đây:\\ %s'
        ) % (k, sign_c, abs_c, bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Với $x = %s$ thì giá trị tương ứng của hàm số là $f(%s) = %s$' % (x1, x1, y1)
        nb_da_1_s = 'Với $x = %s$ thì giá trị tương ứng của hàm số là $f(%s) = %s$' % (x1, x1, y2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Dựa vào bảng giá trị tương ứng, tại $x = %s$ ta có $y = f(%s) = %s$.' % (x1, x1, y1)

        # Thông hiểu
        th_da_1_d = '\\True Giá trị của tham số $m$ thỏa mãn bảng giá trị trên là $m = %s$' % (m_true)
        th_da_1_s = 'Giá trị của tham số $m$ thỏa mãn bảng giá trị trên là $m = %s$' % (m_true + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Thay $x = %s$ và $y = %s$ vào công thức hàm số ta được: $%s = (m - %s) \\cdot (%s) + 2m %s %s$.\\ '
            'Giải phương trình tìm được $m = %s$.'
        ) % (x1, y1, y1, k, x1, sign_c, abs_c, m_true)

        # Vận dụng
        vd_da_1_d = '\\True Giá trị cần điền vào dấu hỏi chấm trong bảng là $f(%s) = %s$' % (x3, y3)
        vd_da_1_s = 'Giá trị cần điền vào dấu hỏi chấm trong bảng là $f(%s) = %s$' % (x3, y3 + a)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Với $m = %s$, hàm số có dạng $y = f(x) = %sx %s %s$.\\ '
            'Khi $x = %s$ thì $f(%s) = %s \\cdot %s %s %s = %s$.'
        ) % (m_true, a, sign_b, abs_b, x3, x3, a, x3, sign_b, abs_b, y3)

        # Vận dụng cao
        tang_giam_true = 'tăng' if a > 0 else 'giảm'
        tang_giam_false = 'giảm' if a > 0 else 'tăng'
        vdc_da_1_d = '\\True Khi giá trị của biến số $x$ tăng lên thì giá trị tương ứng của hàm số $y$ luôn %s' % (tang_giam_true)
        vdc_da_1_s = 'Khi giá trị của biến số $x$ tăng lên thì giá trị tương ứng của hàm số $y$ luôn %s' % (tang_giam_false)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Vì hệ số góc $a = %s %s 0$ nên khi giá trị của $x$ tăng thì giá trị tương ứng của $y = %sx %s %s$ luôn %s.'
        ) % (a, '>' if a > 0 else '<', a, sign_b, abs_b, tang_giam_true)

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

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]
        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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
