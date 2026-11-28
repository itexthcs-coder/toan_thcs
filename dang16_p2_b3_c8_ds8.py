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

def bt_dang16_p2_b3_c8_ds8(self):
    # Dạng 16: Xác suất hình học kết hợp thực nghiệm (Ném phi tiêu tính số pi + TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh = random.choice([20, 30, 40])
        ban_kinh = canh // 2
        dt_vuong = canh * canh
        n = 500
        k = random.choice([392, 393])
        p_tn = fmt_dec(Fraction(k, n), 3)
        p_tn_sai = fmt_dec(Fraction(n - k, n), 3)
        pi_gan_dung = fmt_dec(Fraction(4 * k, n), 3)
        pi_sai = '3,14'

        tikz_tex = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (-1.6,-1.6);\n'
            '\\coordinate (B) at (1.6,-1.6);\n'
            '\\coordinate (C) at (1.6,1.6);\n'
            '\\coordinate (D) at (-1.6,1.6);\n'
            '\\coordinate (O) at (0,0);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt] (O) circle (1.6cm);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\node[below] at (0,-1.7) {Cạnh hình vuông bằng $%s\\text{ cm}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % canh
        )

        noidungcauhoi = (
            'Một tấm bia hình vuông cạnh $%s\\text{ cm}$ có vẽ một hình tròn nội tiếp (tiếp xúc với cả $4$ cạnh của hình vuông). Một người chơi ném ngẫu nhiên $%s$ phi tiêu trúng vào tấm bia và đếm được $%s$ phi tiêu nằm bên trong hình tròn. Biết xác suất lí thuyết phi tiêu rơi vào hình tròn bằng tỉ số diện tích giữa hình tròn và hình vuông.%s'
            'Xét tính đúng sai của các mệnh đề sau:'
            % (canh, n, k, tikz_tex)
        )

        nb_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Phi tiêu nằm trong hình tròn" là $%s$' % p_tn
        nb_da_1_s = 'Xác suất thực nghiệm của biến cố "Phi tiêu nằm trong hình tròn" là $%s$' % p_tn_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Diện tích của tấm bia hình vuông là $%s\\text{ cm}^2$ và bán kính hình tròn là $%s\\text{ cm}$' % (dt_vuong, ban_kinh)
        th_da_1_s = 'Diện tích của tấm bia hình vuông là $%s\\text{ cm}^2$ và bán kính hình tròn là $%s\\text{ cm}$' % (dt_vuong, canh)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Theo lí thuyết, xác suất phi tiêu rơi vào hình tròn bằng $\\dfrac{\\pi}{4}$'
        vd_da_1_s = 'Theo lí thuyết, xác suất phi tiêu rơi vào hình tròn bằng $\\dfrac{\\pi}{2}$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Từ thí nghiệm ném phi tiêu trên, giá trị gần đúng của số $\\pi$ tính được là $%s$' % pi_gan_dung
        vdc_da_1_s = 'Từ thí nghiệm ném phi tiêu trên, giá trị gần đúng của số $\\pi$ tính được là $%s$' % pi_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Xác suất thực nghiệm của biến cố "Phi tiêu nằm trong hình tròn" là $\\dfrac{%s}{%s} = %s$.'
            % (k, n, p_tn)
        )
        loigiai_th_1 = (
            'Diện tích hình vuông là $%s^2 = %s\\text{ cm}^2$. Đường kính hình tròn bằng cạnh hình vuông nên bán kính $R = \\dfrac{%s}{2} = %s\\text{ cm}$.'
            % (canh, dt_vuong, canh, ban_kinh)
        )
        loigiai_vd_1 = (
            'Diện tích hình tròn là $\\pi R^2 = %s\\pi\\text{ cm}^2$.\\'
            'Xác suất lí thuyết phi tiêu rơi vào hình tròn là $\\dfrac{%s\\pi}{%s} = \\dfrac{\\pi}{4}$.'
            % (ban_kinh * ban_kinh, ban_kinh * ban_kinh, dt_vuong)
        )
        loigiai_vdc_1 = (
            'Ước lượng xác suất lí thuyết bằng xác suất thực nghiệm, ta có $\\dfrac{\\pi}{4} \\approx %s \\Rightarrow \\pi \\approx 4 \\cdot %s = %s$.'
            % (p_tn, p_tn, pi_gan_dung)
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
