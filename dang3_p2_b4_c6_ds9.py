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


def bt_dang3_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x_du_kien = random.randint(15, 35)
            vang = random.randint(3, 8)
            x_thuc_te = x_du_kien - vang
            tang_them = random.randint(2, 6)
            num = tang_them * x_du_kien * x_thuc_te
            if num % vang == 0:
                tong_qua = num // vang
                break

        noidungcauhoi = ('''Ban tổ chức một hội nghị chuẩn bị $%s$ phần quà giống nhau để chia đều cho các đại biểu tham dự. Đến giờ khai mạc, có $%s$ đại biểu bận công tác đột xuất không đến dự nên mỗi đại biểu có mặt được nhận thêm $%s$ phần quà so với dự kiến. Gọi $x$ là số đại biểu tham dự theo dự kiến ban đầu ($x \\in \\mathbb{N}^*, x > %s$).''' % (fmt_num(tong_qua), fmt_num(vang), fmt_num(tang_them), fmt_num(vang)))

        nb_da_1_d = '\\True Số phần quà mỗi đại biểu nhận được theo dự kiến là $\\frac{%s}{x}$ (phần)' % (fmt_num(tong_qua))
        nb_da_1_s = 'Số phần quà mỗi đại biểu nhận được theo dự kiến là $\\frac{x}{%s}$ (phần)' % (fmt_num(tong_qua))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Chia đều $%s$ phần quà cho $x$ đại biểu theo dự kiến thì mỗi người nhận được $\\frac{%s}{x}$ (phần quà).''' % (fmt_num(tong_qua), fmt_num(tong_qua)))

        th_da_1_d = '\\True Số đại biểu thực tế có mặt tại hội nghị là $x - %s$ (người)' % (fmt_num(vang))
        th_da_1_s = 'Số đại biểu thực tế có mặt tại hội nghị là $x + %s$ (người)' % (fmt_num(vang))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Vì có $%s$ đại biểu vắng mặt nên số đại biểu thực tế có mặt tại hội nghị là $x - %s$ (người).''' % (fmt_num(vang), fmt_num(vang)))

        vd_da_1_d = '\\True Phương trình biểu thị mối quan hệ giữa các đại lượng là $\\frac{%s}{x - %s} - \\frac{%s}{x} = %s$' % (fmt_num(tong_qua), fmt_num(vang), fmt_num(tong_qua), fmt_num(tang_them))
        vd_da_1_s = 'Phương trình biểu thị mối quan hệ giữa các đại lượng là $\\frac{%s}{x} - \\frac{%s}{x - %s} = %s$' % (fmt_num(tong_qua), fmt_num(tong_qua), fmt_num(vang), fmt_num(tang_them))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Thực tế mỗi đại biểu nhận được $\\frac{%s}{x - %s}$ (phần quà). Vì thực tế mỗi người nhận nhiều hơn dự kiến $%s$ phần quà nên ta có phương trình: $\\frac{%s}{x - %s} - \\frac{%s}{x} = %s$.''' % (fmt_num(tong_qua), fmt_num(vang), fmt_num(tang_them), fmt_num(tong_qua), fmt_num(vang), fmt_num(tong_qua), fmt_num(tang_them)))

        vdc_da_1_d = '\\True Số đại biểu thực tế tham dự hội nghị là $%s\\text{ người}$' % (fmt_num(x_thuc_te))
        vdc_da_1_s = 'Số đại biểu thực tế tham dự hội nghị là $%s\\text{ người}$' % (fmt_num(x_du_kien))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        c_coef = (tong_qua * vang) // tang_them
        delta = vang**2 + 4 * c_coef
        sqrt_delta = int(math.isqrt(delta))
        loigiai_vdc_1 = ('''Quy đồng khử mẫu phương trình $\\frac{%s}{x - %s} - \\frac{%s}{x} = %s$, ta được: \\\\ $%sx - %s(x - %s) = %sx(x - %s) \\Leftrightarrow %sx^2 - %sx - %s = 0 \\Leftrightarrow x^2 - %sx - %s = 0$. \\\\ Ta có $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\ Nghiệm của phương trình là $x_1 = %s$ (thoả mãn) và $x_2 = -%s$ (loại). \\\\ Vậy số đại biểu thực tế tham dự hội nghị là $%s - %s = %s\\text{ người}$.''' % (fmt_num(tong_qua), fmt_num(vang), fmt_num(tong_qua), fmt_num(tang_them), fmt_num(tong_qua), fmt_num(tong_qua), fmt_num(vang), fmt_num(tang_them), fmt_num(vang), fmt_num(tang_them), fmt_num(tang_them * vang), fmt_num(tong_qua * vang), fmt_num(vang), fmt_num(c_coef), fmt_num(vang), fmt_num(c_coef), fmt_num(delta), fmt_num(sqrt_delta), fmt_num(x_du_kien), fmt_num(x_thuc_te), fmt_num(x_du_kien), fmt_num(vang), fmt_num(x_thuc_te)))

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
