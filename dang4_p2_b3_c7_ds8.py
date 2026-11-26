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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p2_b3_c7_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c = random.choice([1, 2, 3])
        # Chọn tử số N chia hết cho c và một số ước khác
        N = c * random.choice([4, 6, 8])
        g0 = -N // c
        
        d_target = random.choice([2, 4])
        while N % d_target != 0:
            d_target = random.choice([2, 3, 4, 6])
        x_target = c + (N // d_target)
        
        # Đếm số ước dương của N
        uoc_duong = [u for u in range(1, N + 1) if N % u == 0]
        so_uoc = len(uoc_duong)
        
        # Tính g(c + k) + g(c - k)
        k_sym = random.choice([1, 2, 3])
        x_p = c + k_sym
        x_m = c - k_sym

        noidungcauhoi = (
            'Cho hàm số $y = g(x) = \\dfrac{%s}{x - %s}$ với $x \\neq %s$. Xét tính đúng sai của các khẳng định sau:'
        ) % (N, c, c)

        nb_da_1_d = '\\True Giá trị $g(0)$ bằng $%s$' % g0
        nb_da_1_s = 'Giá trị $g(0)$ bằng $%s$' % (-g0)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            'Thay $x = 0$ vào công thức hàm số, ta được: $g(0) = \\dfrac{%s}{0 - %s} = \\dfrac{%s}{-%s} = %s$.'
        ) % (N, c, N, c, g0)

        th_da_1_d = '\\True Nếu $g(x) = %s$ thì giá trị tương ứng của biến số $x$ là $%s$' % (d_target, x_target)
        th_da_1_s = 'Nếu $g(x) = %s$ thì giá trị tương ứng của biến số $x$ là $%s$' % (d_target, x_target - 2 * c)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Ta có $g(x) = %s \\Leftrightarrow \\dfrac{%s}{x - %s} = %s \\Leftrightarrow x - %s = \\dfrac{%s}{%s} = %s \\Leftrightarrow x = %s + %s = %s$.'
        ) % (d_target, N, c, d_target, c, N, d_target, N // d_target, N // d_target, c, x_target)

        vd_da_1_d = '\\True Tổng $g(%s) + g(%s)$ luôn bằng $0$' % (x_p, x_m)
        vd_da_1_s = 'Tổng $g(%s) + g(%s)$ bằng $%s$' % (x_p, x_m, 2 * (N // k_sym))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Ta có $g(%s) = \\dfrac{%s}{%s - %s} = \\dfrac{%s}{%s}$ và $g(%s) = \\dfrac{%s}{%s - %s} = \\dfrac{%s}{-%s} = -\\dfrac{%s}{%s}$. '
            'Suy ra $g(%s) + g(%s) = 0$.'
        ) % (x_p, N, x_p, c, N, k_sym, x_m, N, x_m, c, N, k_sym, N, k_sym, x_p, x_m)

        vdc_da_1_d = '\\True Khi $x$ nhận giá trị nguyên lớn hơn $%s$, có đúng $%s$ giá trị nguyên của $x$ để $g(x)$ nhận giá trị nguyên' % (c, so_uoc)
        vdc_da_1_s = 'Khi $x$ nhận giá trị nguyên lớn hơn $%s$, có đúng $%s$ giá trị nguyên của $x$ để $g(x)$ nhận giá trị nguyên' % (c, so_uoc - 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        uoc_str = '; '.join([str(u) for u in uoc_duong])
        loigiai_vdc_1 = (
            'Với $x \\in \\mathbb{Z}$ và $x > %s$, ta có $x - %s$ là số nguyên dương. '
            'Để $g(x) = \\dfrac{%s}{x - %s}$ nhận giá trị nguyên thì $x - %s$ phải là ước nguyên dương của $%s$, '
            'tức là $x - %s \\in \\{%s\\}$. Vậy có đúng $%s$ giá trị nguyên của $x$ thỏa mãn.'
        ) % (c, c, N, c, c, N, c, uoc_str, so_uoc)

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

