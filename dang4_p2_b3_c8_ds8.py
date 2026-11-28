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

def bt_dang4_p2_b3_c8_ds8(self):
    # Dạng 4: Kiểm tra nông sản xuất khẩu (Biến cố đối với dữ liệu lớn)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([2000, 2500, 4000, 5000])
        loi1 = random.choice([60, 75, 80, 100])
        loi2 = random.choice([40, 50, 60])
        tong_loi = loi1 + loi2
        tong_loi_sai = loi1 - loi2
        pct_loi1 = fmt_dec(Fraction(loi1 * 100, n), 2)
        pct_loi1_sai = fmt_dec(Fraction(loi2 * 100, n), 2)
        p_dat = fmt_dec(Fraction(n - tong_loi, n), 4)
        p_dat_sai = fmt_dec(Fraction(tong_loi, n), 4)
        p_d_val = fmt_dec(Fraction(loi2, tong_loi), 4)
        p_d_sai = fmt_dec(Fraction(loi1, tong_loi), 4)

        noidungcauhoi = (
            'Một hợp tác xã kiểm tra chất lượng $%s$ quả xoài cát Hòa Lộc trước khi đóng thùng xuất khẩu thì phát hiện $%s$ quả bị sâu cuống và $%s$ quả không đạt trọng lượng chuẩn (không có quả nào mắc cả hai lỗi). Chọn ngẫu nhiên một quả xoài trong lô đã kiểm tra. Xét tính đúng sai của các khẳng định sau:'
            % (n, loi1, loi2)
        )

        nb_da_1_d = '\\True Tổng số quả xoài không đạt tiêu chuẩn xuất khẩu là $%s$ quả' % tong_loi
        nb_da_1_s = 'Tổng số quả xoài không đạt tiêu chuẩn xuất khẩu là $%s$ quả' % tong_loi_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Quả xoài bị sâu cuống" được ước lượng là $%s\\%%$' % pct_loi1
        th_da_1_s = 'Xác suất thực nghiệm của biến cố "Quả xoài bị sâu cuống" được ước lượng là $%s\\%%$' % pct_loi1_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Quả xoài đạt tiêu chuẩn xuất khẩu" là $%s$' % p_dat
        vd_da_1_s = 'Xác suất thực nghiệm của biến cố "Quả xoài đạt tiêu chuẩn xuất khẩu" là $%s$' % p_dat_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Nếu chọn ngẫu nhiên $1$ quả trong số các quả không đạt chuẩn, xác suất để quả đó không đạt trọng lượng là $%s$' % p_d_val
        vdc_da_1_s = 'Nếu chọn ngẫu nhiên $1$ quả trong số các quả không đạt chuẩn, xác suất để quả đó không đạt trọng lượng là $%s$' % p_d_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Vì không có quả xoài nào mắc cả hai lỗi nên tổng số quả xoài không đạt tiêu chuẩn xuất khẩu là $%s + %s = %s$ (quả).'
            % (loi1, loi2, tong_loi)
        )
        loigiai_th_1 = (
            'Xác suất thực nghiệm của biến cố "Quả xoài bị sâu cuống" là $\\dfrac{%s}{%s} = %s\\%%$.'
            % (loi1, n, pct_loi1)
        )
        loigiai_vd_1 = (
            'Số quả xoài đạt tiêu chuẩn xuất khẩu là $%s - %s = %s$ (quả).\\'
            'Xác suất thực nghiệm của biến cố "Quả xoài đạt tiêu chuẩn xuất khẩu" là $\\dfrac{%s}{%s} = %s$.'
            % (n, tong_loi, n - tong_loi, n - tong_loi, n, p_dat)
        )
        loigiai_vdc_1 = (
            'Trong số $%s$ quả không đạt chuẩn, có $%s$ quả không đạt trọng lượng.\\'
            'Xác suất cần tìm là $\\dfrac{%s}{%s} = %s$.'
            % (tong_loi, loi2, loi2, tong_loi, p_d_val)
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
