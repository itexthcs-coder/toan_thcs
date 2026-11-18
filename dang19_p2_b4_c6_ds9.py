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


def bt_dang19_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (5, 7, 2, 55),
            (4, 6, 2, 24),
            (3, 6, 2, 0),
            (6, 9, 3, 36)
        ]
        t1, t2, gio_c, phut_c = random.choice(bo_so)
        chenh = t2 - t1
        t_chung_rat = Rational(t1 * t2, t1 + t2)
        ns_chung_rat = Rational(1, t_chung_rat)
        tu_ns = ns_chung_rat.p
        mau_ns = ns_chung_rat.q

        a_eq = tu_ns
        b_eq = 2 * mau_ns - tu_ns * chenh
        c_eq = mau_ns * chenh
        g = math.gcd(math.gcd(abs(a_eq), abs(b_eq)), abs(c_eq))
        a_s, b_s, c_s = a_eq // g, b_eq // g, c_eq // g
        a_str = '' if a_s == 1 else fmt_num(a_s)

        str_tg = ('%s\\text{ giờ } %s\\text{ phút}' % (fmt_num(gio_c), fmt_num(phut_c))) if phut_c > 0 else ('%s\\text{ giờ}' % fmt_num(gio_c))

        noidungcauhoi = ('''Một bể chứa nước sạch của khu chung cư có gắn hai vòi cấp nước. Nếu mở đồng thời cả hai vòi thì sau $%s$ sẽ đầy bể. Nếu mở riêng từng vòi thì vòi thứ nhất chảy đầy bể nhanh hơn vòi thứ hai là $%s\\text{ giờ}$. Gọi $x\\text{ (giờ)}$ là thời gian vòi thứ nhất chảy một mình đầy bể ($x > 0$).''' % (str_tg, fmt_num(chenh)))

        nb_da_1_d = '\\True Đổi $%s$ sang đơn vị giờ ta được $%s\\text{ giờ}$' % (str_tg, latex(t_chung_rat))
        nb_da_1_s = 'Đổi $%s$ sang đơn vị giờ ta được $%s\\text{ giờ}$' % (str_tg, latex(t_chung_rat + 1))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $%s = %s + \\frac{%s}{60} = %s\\text{ (giờ)}$.''' % (str_tg, fmt_num(gio_c), fmt_num(phut_c), latex(t_chung_rat)))

        th_da_1_d = '\\True Phương trình biểu thị lượng nước hai vòi chảy trong $1\\text{ giờ}$ là $\\frac{1}{x} + \\frac{1}{x + %s} = %s$' % (fmt_num(chenh), latex(ns_chung_rat))
        th_da_1_s = 'Phương trình biểu thị lượng nước hai vòi chảy trong $1\\text{ giờ}$ là $\\frac{1}{x} + \\frac{1}{x + %s} = %s$' % (fmt_num(chenh), latex(t_chung_rat))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Trong $1\\text{ giờ}$, vòi một chảy được $\\frac{1}{x}$ bể, vòi hai chảy được $\\frac{1}{x + %s}$ bể, cả hai vòi chảy được $1 : %s = %s$ bể. \\\\ Ta có phương trình: $\\frac{1}{x} + \\frac{1}{x + %s} = %s$.''' % (fmt_num(chenh), latex(t_chung_rat), latex(ns_chung_rat), fmt_num(chenh), latex(ns_chung_rat)))

        sign_b = '-' if b_s > 0 else '+'
        abs_b = abs(b_s)
        vd_da_1_d = '\\True Sau khi khử mẫu và thu gọn, ta thu được phương trình bậc hai $%sx^2 %s %sx - %s = 0$' % (a_str, sign_b, fmt_num(abs_b), fmt_num(c_s))
        vd_da_1_s = 'Sau khi khử mẫu và thu gọn, ta thu được phương trình bậc hai $%sx^2 %s %sx + %s = 0$' % (a_str, sign_b, fmt_num(abs_b), fmt_num(c_s))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Quy đồng khử mẫu phương trình $\\frac{1}{x} + \\frac{1}{x + %s} = \\frac{%s}{%s}$, ta được: \\\\ $%s(2x + %s) = %sx(x + %s) \\Leftrightarrow %sx^2 %s %sx - %s = 0$.''' % (fmt_num(chenh), fmt_num(tu_ns), fmt_num(mau_ns), fmt_num(mau_ns), fmt_num(chenh), fmt_num(tu_ns), fmt_num(chenh), a_str, sign_b, fmt_num(abs_b), fmt_num(c_s)))

        vdc_da_1_d = '\\True Nếu chỉ mở một mình vòi thứ hai thì phải mất $%s\\text{ giờ}$ mới đầy bể' % (fmt_num(t2))
        vdc_da_1_s = 'Nếu chỉ mở một mình vòi thứ hai thì phải mất $%s\\text{ giờ}$ mới đầy bể' % (fmt_num(t1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Giải phương trình bậc hai $%sx^2 %s %sx - %s = 0$, ta tìm được nghiệm dương duy nhất là $x = %s\\text{ (giờ)}$. \\\\ Vậy vòi thứ hai chảy một mình đầy bể hết $%s + %s = %s\\text{ giờ}$.''' % (a_str, sign_b, fmt_num(abs_b), fmt_num(c_s), fmt_num(t1), fmt_num(t1), fmt_num(chenh), fmt_num(t2)))

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
