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


def bt_dang2_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        von = random.choice([100, 150, 200, 250, 300, 400, 500])
        lai_phan_tram = random.choice([4, 5, 6, 7, 8, 9, 10])
        x_val = Decimal(lai_phan_tram) / Decimal(100)
        he_so = (Decimal(1) + x_val) ** 2
        tong_tien = Decimal(von) * he_so

        noidungcauhoi = ('''Cô Mai gửi $%s\\text{ triệu đồng}$ vào ngân hàng theo thể thức lãi kép với kì hạn $12\\text{ tháng}$ (lãi năm thứ nhất nhập vào gốc để tính lãi năm thứ hai). Sau $2\\text{ năm}$, cô Mai rút toàn bộ cả vốn lẫn lãi được $%s\\text{ triệu đồng}$. Gọi $x$ là lãi suất gửi tiết kiệm một năm ($x$ viết dưới dạng số thập phân, $x > 0$).''' % (fmt_num(von), fmt_num(tong_tien)))

        nb_da_1_d = '\\True Số tiền cả vốn lẫn lãi cô Mai có được sau năm thứ nhất là $%s(1 + x)$ triệu đồng' % (fmt_num(von))
        nb_da_1_s = 'Số tiền cả vốn lẫn lãi cô Mai có được sau năm thứ nhất là $%s + x$ triệu đồng' % (fmt_num(von))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Sau năm thứ nhất, số tiền lãi là $%sx$ (triệu đồng) nên tổng số tiền cả vốn lẫn lãi thu được là $%s + %sx = %s(1 + x)$ (triệu đồng).''' % (fmt_num(von), fmt_num(von), fmt_num(von), fmt_num(von)))

        th_da_1_d = '\\True Phương trình biểu thị số tiền nhận được sau $2\\text{ năm}$ là $%s(1 + x)^2 = %s$' % (fmt_num(von), fmt_num(tong_tien))
        th_da_1_s = 'Phương trình biểu thị số tiền nhận được sau $2\\text{ năm}$ là $%s(1 + 2x) = %s$' % (fmt_num(von), fmt_num(tong_tien))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Sau năm thứ hai, số tiền cả vốn lẫn lãi là $%s(1 + x) + %s(1 + x)x = %s(1 + x)^2$ (triệu đồng). \\\\ Theo đề bài, ta có phương trình: $%s(1 + x)^2 = %s$.''' % (fmt_num(von), fmt_num(von), fmt_num(von), fmt_num(von), fmt_num(tong_tien)))

        vd_da_1_d = '\\True Giá trị của $x$ tìm được từ phương trình là $x = %s$' % (fmt_num(x_val))
        vd_da_1_s = 'Giá trị của $x$ tìm được từ phương trình là $x = %s$' % (fmt_num(x_val + Decimal('0.02')))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Ta có $%s(1 + x)^2 = %s \\Leftrightarrow (1 + x)^2 = %s$. \\\\ Vì $x > 0$ nên $1 + x > 1$, suy ra $1 + x = %s \\Leftrightarrow x = %s$.''' % (fmt_num(von), fmt_num(tong_tien), fmt_num(he_so), fmt_num(Decimal(1) + x_val), fmt_num(x_val)))

        vdc_da_1_d = '\\True Lãi suất gửi tiết kiệm ngân hàng của cô Mai là $%s\\%%/\\text{năm}$' % (fmt_num(lai_phan_tram))
        vdc_da_1_s = 'Lãi suất gửi tiết kiệm ngân hàng của cô Mai là $%s\\%%/\\text{năm}$' % (fmt_num(lai_phan_tram + 2))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Đổi $x = %s = %s\\%%$. Vậy lãi suất gửi tiết kiệm ngân hàng của cô Mai là $%s\\%%/\\text{năm}$.''' % (fmt_num(x_val), fmt_num(lai_phan_tram), fmt_num(lai_phan_tram)))

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
