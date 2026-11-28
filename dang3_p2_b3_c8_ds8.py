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

def fmt_dec(val, places=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*places) if places > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = format(d, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')

def fmt_frac(num, den):
    f = Fraction(num, den)
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang3_p2_b3_c8_ds8(self):
    # Dạng 3: Dữ liệu tỉ lệ phần trăm về phương tiện đi học (kèm biểu đồ cột TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([300, 400, 500, 600])
        p_dd = random.choice([40, 45, 50])
        p_dt = random.choice([25, 30])
        p_bm = random.choice([15, 20])
        p_db = 100 - p_dd - p_dt - p_bm

        so_db = (n * p_db) // 100
        so_db_sai = so_db + 10
        dec_dt = fmt_dec(Fraction(p_dt, 100), 2)
        dec_dt_sai = fmt_dec(Fraction(p_dt + 5, 100), 2)
        frac_k_dd = fmt_frac(100 - p_dd, 100)
        frac_k_dd_sai = fmt_frac(p_dd, 100)
        dec_tu_di = fmt_dec(Fraction(100 - p_bm, 100), 2)
        dec_tu_di_sai = fmt_dec(Fraction(p_bm, 100), 2)

        h1 = round(p_dd * 0.06, 2)
        h2 = round(p_dt * 0.06, 2)
        h3 = round(p_bm * 0.06, 2)
        h4 = round(p_db * 0.06, 2)

        tikz_tex = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt, ->] (0,0) -- (7.5,0);\n'
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.5) node[above] {Tỉ lệ ($\\%%$)};\n'
            '\\draw[line width=1pt] (0.6,0) rectangle (1.6,%s);\n'
            '\\node[above] at (1.1,%s) {$%s\\%%$};\n'
            '\\node[below] at (1.1,0) {Xe đạp điện};\n'
            '\\draw[line width=1pt] (2.3,0) rectangle (3.3,%s);\n'
            '\\node[above] at (2.8,%s) {$%s\\%%$};\n'
            '\\node[below] at (2.8,0) {Xe đạp};\n'
            '\\draw[line width=1pt] (4.0,0) rectangle (5.0,%s);\n'
            '\\node[above] at (4.5,%s) {$%s\\%%$};\n'
            '\\node[below] at (4.5,0) {Đưa đón};\n'
            '\\draw[line width=1pt] (5.7,0) rectangle (6.7,%s);\n'
            '\\node[above] at (6.2,%s) {$%s\\%%$};\n'
            '\\node[below] at (6.2,0) {Đi bộ};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (h1, h1, p_dd, h2, h2, p_dt, h3, h3, p_bm, h4, h4, p_db)
        )

        noidungcauhoi = (
            'Khảo sát phương tiện đến trường của $%s$ học sinh khối $8$ thu được biểu đồ tỉ lệ phần trăm như sau:%s'
            'Chọn ngẫu nhiên một học sinh trong cuộc khảo sát. Xét tính đúng sai của các khẳng định sau:'
            % (n, tikz_tex)
        )

        nb_da_1_d = '\\True Có $%s$ học sinh trong cuộc khảo sát đi bộ đến trường' % so_db
        nb_da_1_s = 'Có $%s$ học sinh trong cuộc khảo sát đi bộ đến trường' % so_db_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Học sinh được chọn đi xe đạp thường" là $%s$' % dec_dt
        th_da_1_s = 'Xác suất thực nghiệm của biến cố "Học sinh được chọn đi xe đạp thường" là $%s$' % dec_dt_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Học sinh được chọn không đi xe đạp điện" là $%s$' % frac_k_dd
        vd_da_1_s = 'Xác suất thực nghiệm của biến cố "Học sinh được chọn không đi xe đạp điện" là $%s$' % frac_k_dd_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Học sinh được chọn tự đi học (xe đạp thường, xe đạp điện hoặc đi bộ)" là $%s$' % dec_tu_di
        vdc_da_1_s = 'Xác suất thực nghiệm của biến cố "Học sinh được chọn tự đi học (xe đạp thường, xe đạp điện hoặc đi bộ)" là $%s$' % dec_tu_di_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Tỉ lệ học sinh đi bộ là $100\\%% - (%s\\%% + %s\\%% + %s\\%%) = %s\\%%$.\\'
            'Số học sinh đi bộ đến trường là $%s \\cdot %s\\%% = %s$ (học sinh).'
            % (p_dd, p_dt, p_bm, p_db, n, p_db, so_db)
        )
        loigiai_th_1 = (
            'Tỉ lệ học sinh đi xe đạp thường là $%s\\%%$, nên xác suất thực nghiệm của biến cố tương ứng là $%s\\%% = %s$.'
            % (p_dt, p_dt, dec_dt)
        )
        loigiai_vd_1 = (
            'Tỉ lệ học sinh không đi xe đạp điện là $100\\%% - %s\\%% = %s\\%%$.\\'
            'Xác suất thực nghiệm của biến cố đó là $\\dfrac{%s}{100} = %s$.'
            % (p_dd, 100 - p_dd, 100 - p_dd, frac_k_dd)
        )
        loigiai_vdc_1 = (
            'Biến cố đối của biến cố "Học sinh tự đi học" là "Học sinh được bố mẹ đưa đón" (chiếm $%s\\%% = %s$).\\'
            'Do đó, xác suất thực nghiệm của biến cố "Học sinh tự đi học" là $1 - %s = %s$.'
            % (p_bm, dec_tu_di_sai, dec_tu_di_sai, dec_tu_di)
        )

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
        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)
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
