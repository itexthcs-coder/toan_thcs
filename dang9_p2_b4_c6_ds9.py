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


def bt_dang9_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            w = random.randint(12, 24)
            l = random.randint(w + 10, w + 30)
            dw = random.randint(3, 8)
            if (dw * l) % (w + dw) == 0:
                dl = (dw * l) // (w + dw)
                if dl > 0 and l > dl:
                    area = w * l
                    break

        noidungcauhoi = ('''Một trang trại có một thửa ruộng hình chữ nhật diện tích $%s\\text{ m}^2$. Để thuận tiện cho việc lắp đặt hệ thống tưới tiêu tự động, chủ trang trại quyết định mở rộng chiều rộng thêm $%s\\text{ m}$ và thu hẹp chiều dài đi $%s\\text{ m}$ thì thấy diện tích thửa ruộng không thay đổi. Gọi $x\\text{ (m)}$ là chiều rộng ban đầu của thửa ruộng ($x > 0$).
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4.5,0);
\\coordinate (C) at (4.5,2);
\\coordinate (D) at (0,2);
\\coordinate (E) at (3.6,0);
\\coordinate (F) at (3.6,2.6);
\\coordinate (G) at (0,2.6);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (D)--(G)--(F)--(E);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\node at (2.25,-0.3) {$\\frac{%s}{x}\\text{ (m)}$};
\\node[left] at (-0.1,1) {$x\\text{ (m)}$};
\\end{tikzpicture}
\\end{center}''' % (fmt_num(area), fmt_num(dw), fmt_num(dl), fmt_num(area)))

        nb_da_1_d = '\\True Chiều dài ban đầu của thửa ruộng là $\\frac{%s}{x}\\text{ (m)}$' % (fmt_num(area))
        nb_da_1_s = 'Chiều dài ban đầu của thửa ruộng là $\\frac{x}{%s}\\text{ (m)}$' % (fmt_num(area))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Do diện tích ban đầu của thửa ruộng hình chữ nhật là $%s\\text{ m}^2$ và chiều rộng là $x\\text{ (m)}$ nên chiều dài ban đầu là $\\frac{%s}{x}\\text{ (m)}$.''' % (fmt_num(area), fmt_num(area)))

        th_da_1_d = '\\True Chiều dài của thửa ruộng sau khi cải tạo là $\\frac{%s}{x} - %s\\text{ (m)}$' % (fmt_num(area), fmt_num(dl))
        th_da_1_s = 'Chiều dài của thửa ruộng sau khi cải tạo là $\\frac{%s}{x} + %s\\text{ (m)}$' % (fmt_num(area), fmt_num(dl))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thu hẹp chiều dài đi $%s\\text{ m}$ nên chiều dài mới của thửa ruộng là $\\frac{%s}{x} - %s\\text{ (m)}$.''' % (fmt_num(dl), fmt_num(area), fmt_num(dl)))

        vd_da_1_d = '\\True Phương trình biểu thị diện tích không đổi là $(x + %s)\\left(\\frac{%s}{x} - %s\\right) = %s$' % (fmt_num(dw), fmt_num(area), fmt_num(dl), fmt_num(area))
        vd_da_1_s = 'Phương trình biểu thị diện tích không đổi là $(x - %s)\\left(\\frac{%s}{x} + %s\\right) = %s$' % (fmt_num(dw), fmt_num(area), fmt_num(dl), fmt_num(area))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Chiều rộng mới là $x + %s\\text{ (m)}$, chiều dài mới là $\\frac{%s}{x} - %s\\text{ (m)}$. Vì diện tích không đổi nên ta có phương trình: $(x + %s)\\left(\\frac{%s}{x} - %s\\right) = %s$.''' % (fmt_num(dw), fmt_num(area), fmt_num(dl), fmt_num(dw), fmt_num(area), fmt_num(dl), fmt_num(area)))

        vdc_da_1_d = '\\True Chiều dài ban đầu của thửa ruộng là $%s\\text{ m}$' % (fmt_num(l))
        vdc_da_1_s = 'Chiều dài ban đầu của thửa ruộng là $%s\\text{ m}$' % (fmt_num(w))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        c_eq = (area * dw) // dl
        delta = dw**2 + 4 * c_eq
        sqrt_delta = int(math.isqrt(delta))
        loigiai_vdc_1 = ('''Khai triển và thu gọn phương trình $(x + %s)\\left(\\frac{%s}{x} - %s\\right) = %s$: \\\\ $%s - %sx + \\frac{%s}{x} - %s = %s \\Leftrightarrow %sx^2 + %sx - %s = 0 \\Leftrightarrow x^2 + %sx - %s = 0$. \\\\ Ta có $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\ Nghiệm của phương trình là $x_1 = %s$ (thoả mãn) và $x_2 = -%s$ (loại). \\\\ Vậy chiều rộng ban đầu là $%s\\text{ m}$ và chiều dài ban đầu là $\\frac{%s}{%s} = %s\\text{ m}$.''' % (fmt_num(dw), fmt_num(area), fmt_num(dl), fmt_num(area), fmt_num(area), fmt_num(dl), fmt_num(area * dw), fmt_num(dw * dl), fmt_num(area), fmt_num(dl), fmt_num(dw * dl), fmt_num(area * dw), fmt_num(dw), fmt_num(c_eq), fmt_num(dw), fmt_num(c_eq), fmt_num(delta), fmt_num(sqrt_delta), fmt_num(w), fmt_num(w + dw), fmt_num(w), fmt_num(area), fmt_num(w), fmt_num(l)))

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
