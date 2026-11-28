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

def bt_dang18_p2_b3_c8_ds8(self):
    # Dạng 18: Thống kê dịch tễ và xét nghiệm sàng lọc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_sot = 320
        n_ksot = 480
        tong = 800
        duong_sot = random.choice([96, 112])
        duong_ksot = random.choice([24, 16])
        if duong_sot == 96:
            duong_ksot = 24
        else:
            duong_ksot = 16

        tong_duong = duong_sot + duong_ksot
        pct_chung = fmt_dec(Fraction(tong_duong * 100, tong), 1)
        pct_chung_sai = fmt_dec(Fraction(duong_sot * 100, tong), 1)
        p_sot = fmt_dec(Fraction(duong_sot, n_sot), 2)
        p_sot_sai = fmt_dec(Fraction(duong_sot, tong), 2)
        he_so_gap = (duong_sot * n_ksot) // (n_sot * duong_ksot)
        he_so_gap_sai = duong_sot // duong_ksot

        N_ksot = 1500
        du_bao_ksot = (N_ksot * duong_ksot) // n_ksot
        du_bao_ksot_sai = du_bao_ksot + 25

        noidungcauhoi = (
            'Bệnh viện Y xét nghiệm tầm soát một loại virus cho $%s$ người dân trong vùng dịch, gồm $%s$ người có triệu chứng sốt và $%s$ người không có triệu chứng sốt. Kết quả cho thấy có $%s$ người có triệu chứng sốt dương tính với virus và $%s$ người không có triệu chứng sốt dương tính với virus. Xét tính đúng sai của các khẳng định sau:'
            % (tong, n_sot, n_ksot, duong_sot, duong_ksot)
        )

        nb_da_1_d = '\\True Xác suất thực nghiệm một người được xét nghiệm có kết quả dương tính là $%s\\%%$' % pct_chung
        nb_da_1_s = 'Xác suất thực nghiệm một người được xét nghiệm có kết quả dương tính là $%s\\%%$' % pct_chung_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Trong nhóm người có triệu chứng sốt, xác suất thực nghiệm dương tính với virus là $%s$' % p_sot
        th_da_1_s = 'Trong nhóm người có triệu chứng sốt, xác suất thực nghiệm dương tính với virus là $%s$' % p_sot_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Khả năng dương tính ở người có triệu chứng sốt cao gấp $%s$ lần ở người không có triệu chứng sốt' % he_so_gap
        vd_da_1_s = 'Khả năng dương tính ở người có triệu chứng sốt cao gấp $%s$ lần ở người không có triệu chứng sốt' % he_so_gap_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Nếu xét nghiệm thêm $%s$ người không có triệu chứng sốt khác trong vùng dịch, dự đoán có khoảng $%s$ người dương tính' % (N_ksot, du_bao_ksot)
        vdc_da_1_s = 'Nếu xét nghiệm thêm $%s$ người không có triệu chứng sốt khác trong vùng dịch, dự đoán có khoảng $%s$ người dương tính' % (N_ksot, du_bao_ksot_sai)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Tổng số ca dương tính là $%s + %s = %s$ (người).\\'
            'Xác suất thực nghiệm một người dương tính là $\\dfrac{%s}{%s} = %s\\%%$.'
            % (duong_sot, duong_ksot, tong_duong, tong_duong, tong, pct_chung)
        )
        loigiai_th_1 = (
            'Trong nhóm $%s$ người có triệu chứng sốt, xác suất thực nghiệm dương tính là $\\dfrac{%s}{%s} = %s$.'
            % (n_sot, duong_sot, n_sot, p_sot)
        )
        loigiai_vd_1 = (
            'Trong nhóm không có triệu chứng sốt, xác suất thực nghiệm dương tính là $\\dfrac{%s}{%s} = %s$.\\'
            'Tỉ số hai xác suất là $\\dfrac{%s}{%s} = %s$ (lần).'
            % (duong_ksot, n_ksot, fmt_dec(Fraction(duong_ksot, n_ksot), 3), p_sot, fmt_dec(Fraction(duong_ksot, n_ksot), 3), he_so_gap)
        )
        loigiai_vdc_1 = (
            'Nếu xét nghiệm thêm $%s$ người không có triệu chứng sốt, số ca dương tính dự đoán là $%s \\cdot \\dfrac{%s}{%s} = %s$ (người).'
            % (N_ksot, N_ksot, duong_ksot, n_ksot, du_bao_ksot)
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
