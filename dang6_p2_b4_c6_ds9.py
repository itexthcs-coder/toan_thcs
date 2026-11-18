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


def bt_dang6_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            v_di = random.choice([40, 45, 50, 60])
            dv = random.choice([10, 15, 20])
            v_ve = v_di + dv
            phut_lech = random.choice([30, 45, 60])
            gio_lech = phut_lech / 60.0
            num = gio_lech * v_di * v_ve
            if num.is_integer() and int(num) % dv == 0:
                s_ab = int(num) // dv
                break

        c_eq = int(s_ab * dv / gio_lech)

        noidungcauhoi = ('''Một xe khách đi từ thành phố A đến thành phố B cách nhau $%s\\text{ km}$. Khi từ B quay trở về A, do đường vắng hơn nên tài xế tăng vận tốc thêm $%s\\text{ km/h}$ so với lúc đi. Vì vậy, thời gian về ít hơn thời gian đi là $%s\\text{ phút}$. Gọi $x\\text{ (km/h)}$ là vận tốc của xe khách lúc đi ($x > 0$).''' % (fmt_num(s_ab), fmt_num(dv), fmt_num(phut_lech)))

        nb_da_1_d = '\\True Thời gian xe khách đi từ A đến B là $\\frac{%s}{x}\\text{ (giờ)}$' % (fmt_num(s_ab))
        nb_da_1_s = 'Thời gian xe khách đi từ A đến B là $\\frac{x}{%s}\\text{ (giờ)}$' % (fmt_num(s_ab))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thời gian xe khách đi quãng đường $%s\\text{ km}$ với vận tốc $x\\text{ (km/h)}$ là $\\frac{%s}{x}\\text{ (giờ)}$.''' % (fmt_num(s_ab), fmt_num(s_ab)))

        th_da_1_d = '\\True Phương trình biểu thị mối quan hệ giữa thời gian đi và thời gian về là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_lech))
        th_da_1_s = 'Phương trình biểu thị mối quan hệ giữa thời gian đi và thời gian về là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(phut_lech))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Đổi $%s\\text{ phút} = %s\\text{ giờ}$. Vận tốc lúc về là $x + %s\\text{ (km/h)}$, thời gian lúc về là $\\frac{%s}{x + %s}\\text{ (giờ)}$. \\\\ Vì thời gian về ít hơn thời gian đi là $%s\\text{ giờ}$ nên ta có phương trình: $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$.''' % (fmt_num(phut_lech), fmt_num(gio_lech), fmt_num(dv), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_lech), fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_lech)))

        vd_da_1_d = '\\True Sau khi khử mẫu và thu gọn, ta được phương trình bậc hai $x^2 + %sx - %s = 0$' % (fmt_num(dv), fmt_num(c_eq))
        vd_da_1_s = 'Sau khi khử mẫu và thu gọn, ta được phương trình bậc hai $x^2 - %sx - %s = 0$' % (fmt_num(dv), fmt_num(c_eq))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Quy đồng khử mẫu phương trình $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$, ta được: \\\\ $%s(x + %s) - %sx = %sx(x + %s) \\Leftrightarrow %sx^2 + %sx - %s = 0 \\Leftrightarrow x^2 + %sx - %s = 0$.''' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_lech), fmt_num(s_ab), fmt_num(dv), fmt_num(s_ab), fmt_num(gio_lech), fmt_num(dv), fmt_num(gio_lech), fmt_num(gio_lech * dv), fmt_num(s_ab * dv), fmt_num(dv), fmt_num(c_eq)))

        vdc_da_1_d = '\\True Vận tốc của xe khách lúc đi từ A đến B là $%s\\text{ km/h}$' % (fmt_num(v_di))
        vdc_da_1_s = 'Vận tốc của xe khách lúc đi từ A đến B là $%s\\text{ km/h}$' % (fmt_num(v_ve))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        delta = dv**2 + 4 * c_eq
        sqrt_delta = int(math.isqrt(delta))
        loigiai_vdc_1 = ('''Giải phương trình $x^2 + %sx - %s = 0$: \\\\ Ta có $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\ Nghiệm của phương trình là $x_1 = \\frac{-%s + %s}{2} = %s$ (thoả mãn) và $x_2 = \\frac{-%s - %s}{2} = -%s$ (loại). \\\\ Vậy vận tốc của xe khách lúc đi là $%s\\text{ km/h}$.''' % (fmt_num(dv), fmt_num(c_eq), fmt_num(dv), fmt_num(c_eq), fmt_num(delta), fmt_num(sqrt_delta), fmt_num(dv), fmt_num(sqrt_delta), fmt_num(v_di), fmt_num(dv), fmt_num(sqrt_delta), fmt_num(v_ve), fmt_num(v_di)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
