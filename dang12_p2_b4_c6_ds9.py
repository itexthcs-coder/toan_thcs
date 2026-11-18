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


def bt_dang12_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (1200, 500, 100, 4.4, 96, 6, 24),
            (1200, 600, 200, 3.5, 90, 5, 30),
            (1500, 500, 250, 5.0, 60, 6, 60)
        ]
        s_bay, v_di, dv, t_bay, phut_nghi, gio_tong, phut_lech_bay = random.choice(bo_so)
        v_ve = v_di + dv

        noidungcauhoi = ('''Một máy bay thương mại bay từ sân bay Nội Bài đến sân bay Tân Sơn Nhất với quãng đường dài $%s\\text{ km}$. Sau khi trả khách và nạp nhiên liệu trong $%s\\text{ phút}$, máy bay quay trở về Nội Bài với vận tốc trung bình lớn hơn lúc đi là $%s\\text{ km/h}$ nhờ thuận chiều gió. Tổng thời gian cả hành trình (tính cả thời gian nghỉ) là $%s\\text{ giờ}$. Gọi $x\\text{ (km/h)}$ là vận tốc máy bay lúc đi ($x > 0$).''' % (fmt_num(s_bay), fmt_num(phut_nghi), fmt_num(dv), fmt_num(gio_tong)))

        nb_da_1_d = '\\True Thời gian máy bay thực hiện cả hai chặng bay (không tính thời gian nạp nhiên liệu) là $%s\\text{ giờ}$' % (fmt_num(t_bay))
        nb_da_1_s = 'Thời gian máy bay thực hiện cả hai chặng bay (không tính thời gian nạp nhiên liệu) là $%s\\text{ giờ}$' % (fmt_num(gio_tong))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        t_nghi_gio = phut_nghi / 60.0
        loigiai_nb_1 = ('''Đổi $%s\\text{ phút} = %s\\text{ giờ}$. Thời gian máy bay thực hiện cả hai chặng bay là $%s - %s = %s\\text{ (giờ)}$.''' % (fmt_num(phut_nghi), fmt_num(t_nghi_gio), fmt_num(gio_tong), fmt_num(t_nghi_gio), fmt_num(t_bay)))

        th_da_1_d = '\\True Phương trình lập được là $\\frac{%s}{x} + \\frac{%s}{x + %s} = %s$' % (fmt_num(s_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay))
        th_da_1_s = 'Phương trình lập được là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(s_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thời gian bay chặng đi là $\\frac{%s}{x}\\text{ (giờ)}$, thời gian bay chặng về là $\\frac{%s}{x + %s}\\text{ (giờ)}$. \\\\ Tổng thời gian hai chặng bay bằng $%s\\text{ giờ}$ nên ta có phương trình: $\\frac{%s}{x} + \\frac{%s}{x + %s} = %s$.''' % (fmt_num(s_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay), fmt_num(s_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay)))

        vd_da_1_d = '\\True Vận tốc của máy bay lúc đi là $%s\\text{ km/h}$' % (fmt_num(v_di))
        vd_da_1_s = 'Vận tốc của máy bay lúc đi là $%s\\text{ km/h}$' % (fmt_num(v_ve))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Quy đồng khử mẫu phương trình $\\frac{%s}{x} + \\frac{%s}{x + %s} = %s$, ta được: \\\\ $%s(2x + %s) = %sx(x + %s)$. Giải phương trình bậc hai thu được nghiệm dương duy nhất là $x = %s\\text{ (km/h)}$.''' % (fmt_num(s_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay), fmt_num(s_bay), fmt_num(dv), fmt_num(t_bay), fmt_num(dv), fmt_num(v_di)))

        vdc_da_1_d = '\\True Thời gian bay chặng về ngắn hơn thời gian bay chặng đi là $%s\\text{ phút}$' % (fmt_num(phut_lech_bay))
        vdc_da_1_s = 'Thời gian bay chặng về ngắn hơn thời gian bay chặng đi là $%s\\text{ phút}$' % (fmt_num(phut_lech_bay + 15))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        t_di_val = s_bay / v_di
        t_ve_val = s_bay / v_ve
        loigiai_vdc_1 = ('''Thời gian bay chặng đi là $\\frac{%s}{%s} = %s\\text{ (giờ)}$, thời gian bay chặng về là $\\frac{%s}{%s} = %s\\text{ (giờ)}$. \\\\ Chênh lệch thời gian giữa hai chặng là $%s - %s = %s\\text{ giờ} = %s\\text{ phút}$.''' % (fmt_num(s_bay), fmt_num(v_di), fmt_num(t_di_val), fmt_num(s_bay), fmt_num(v_ve), fmt_num(t_ve_val), fmt_num(t_di_val), fmt_num(t_ve_val), fmt_num(round(t_di_val - t_ve_val, 2)), fmt_num(phut_lech_bay)))

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
