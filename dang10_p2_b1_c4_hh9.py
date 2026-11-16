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


def bt_dang10_p2_b1_c4_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        def format_vn(val):
            return str(val).replace(".", ",")

        def goc_sang_do_phut(deg_float):
            tong_phut = int(Decimal(str(deg_float * 60)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
            do = tong_phut // 60
            phut = tong_phut % 60
            return do, phut

        cos_val = random.choice([0.6, 0.7, 0.75, 0.8])
        deg_cos = math.degrees(math.acos(cos_val))
        do_cos, phut_cos = goc_sang_do_phut(deg_cos)

        tan_val = random.choice([2, 4, 5])
        cot_val = Decimal(str(1 / tan_val)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        cot_x_val = random.choice([1.5, 2.5, 3.5])
        deg_cot = math.degrees(math.atan(1 / cot_x_val))
        do_cot, phut_cot = goc_sang_do_phut(deg_cot)
        deg_tan_y = math.degrees(math.atan(cot_x_val))
        do_tan_y, phut_tan_y = goc_sang_do_phut(deg_tan_y)

        noidungcauhoi = (
            "Cho góc nhọn $x$ được xác định thông qua máy tính cầm tay (làm tròn kết quả số đo góc đến phút):"
        )

        nb_da_1_d = "\\True Nếu $\\sin x = 0,5$ thì $x = 30^\\circ$"
        nb_da_1_s = "Nếu $\\sin x = 0,5$ thì $x = 60^\\circ$"
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            "Ta có $\\sin x = 0,5 = \\dfrac{1}{2}$, suy ra $x = 30^\\circ$."
        )
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = "\\True Nếu $\\cos x = %s$ thì $x \\approx %s^\\circ %s'$" % (format_vn(cos_val), do_cos, phut_cos)
        th_da_1_s = "Nếu $\\cos x = %s$ thì $x \\approx %s^\\circ %s'$" % (format_vn(cos_val), 89 - do_cos, 60 - phut_cos)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            "Sử dụng máy tính cầm tay bấm phím $\\text{SHIFT} \\rightarrow \\cos \\rightarrow %s \\rightarrow = \\rightarrow {}^{\\circ}\\,\\text{'}\\,\\text{''}$, ta được $x \\approx %s^\\circ %s'$."
            % (format_vn(cos_val), do_cos, phut_cos)
        )
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = "\\True Nếu $\\tan x = %s$ thì $\\cot x = %s$" % (tan_val, format_vn(cot_val))
        vd_da_1_s = "Nếu $\\tan x = %s$ thì $\\cot x = %s$" % (tan_val, format_vn(tan_val))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            "Vì $\\cot x = \\dfrac{1}{\\tan x}$ nên khi $\\tan x = %s$ thì $\\cot x = \\dfrac{1}{%s} = %s$."
            % (tan_val, tan_val, format_vn(cot_val))
        )
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = "\\True Nếu $\\cot x = %s$ và $\\tan y = %s$ ($y$ nhọn) thì $x + y = 90^\\circ$" % (format_vn(cot_x_val), format_vn(cot_x_val))
        vdc_da_1_s = "Nếu $\\cot x = %s$ và $\\tan y = %s$ ($y$ nhọn) thì $x = y$" % (format_vn(cot_x_val), format_vn(cot_x_val))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            "Ta có $\\cot x = %s = \\tan y$, mà $\\tan y = \\cot(90^\\circ - y)$ nên $x = 90^\\circ - y$, suy ra $x + y = 90^\\circ$ (cụ thể $x \\approx %s^\\circ %s'$ và $y \\approx %s^\\circ %s'$)."
            % (format_vn(cot_x_val), do_cot, phut_cot, do_tan_y, phut_tan_y)
        )
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
