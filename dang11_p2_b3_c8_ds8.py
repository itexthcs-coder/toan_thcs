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

def bt_dang11_p2_b3_c8_ds8(self):
    # Dạng 11: Dự báo tỉ lệ nảy mầm của hạt giống
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([400, 500, 800])
        pct_nay = random.choice([88, 90, 92, 95])
        k = (n * pct_nay) // 100
        pct_khong = 100 - pct_nay
        p_khong_dec = fmt_dec(Fraction(pct_khong, 100), 2)
        p_khong_sai = fmt_dec(Fraction(pct_nay, 100), 2)

        N_moi = random.choice([2000, 2500, 3000])
        du_bao_c = (N_moi * pct_nay) // 100
        du_bao_c_sai = du_bao_c - 100

        cay_can = pct_nay * 50
        hat_can = 5000
        hat_can_sai = 4800

        noidungcauhoi = (
            'Viện nghiên cứu cây trồng gieo thử nghiệm $%s$ hạt giống ngô lai mới và thấy có $%s$ hạt nảy mầm. Dựa vào kết quả này, người ta ước lượng xác suất nảy mầm của loại hạt giống này. Xét tính đúng sai của các khẳng định sau:'
            % (n, k)
        )

        nb_da_1_d = '\\True Xác suất nảy mầm của hạt giống ngô lai mới được ước lượng là $%s\\%%$' % pct_nay
        nb_da_1_s = 'Xác suất nảy mầm của hạt giống ngô lai mới được ước lượng là $%s\\%%$' % (pct_nay - 4)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất hạt giống không nảy mầm được ước lượng là $%s$' % p_khong_dec
        th_da_1_s = 'Xác suất hạt giống không nảy mầm được ước lượng là $%s$' % p_khong_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Nếu một nông dân gieo $%s$ hạt giống loại này, dự đoán sẽ có khoảng $%s$ hạt nảy mầm' % (N_moi, du_bao_c)
        vd_da_1_s = 'Nếu một nông dân gieo $%s$ hạt giống loại này, dự đoán sẽ có khoảng $%s$ hạt nảy mầm' % (N_moi, du_bao_c_sai)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Để thu được khoảng $%s$ cây ngô con nảy mầm, người nông dân cần gieo khoảng $%s$ hạt giống' % (cay_can, hat_can)
        vdc_da_1_s = 'Để thu được khoảng $%s$ cây ngô con nảy mầm, người nông dân cần gieo khoảng $%s$ hạt giống' % (cay_can, hat_can_sai)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Xác suất thực nghiệm của biến cố "Hạt giống nảy mầm" là $\\dfrac{%s}{%s} = %s\\%%$.\\'
            'Vậy xác suất nảy mầm của hạt giống được ước lượng là $%s\\%%$.'
            % (k, n, pct_nay, pct_nay)
        )
        loigiai_th_1 = (
            'Xác suất hạt giống không nảy mầm được ước lượng là $1 - %s\\%% = %s\\%% = %s$.'
            % (pct_nay, pct_khong, p_khong_dec)
        )
        loigiai_vd_1 = (
            'Khi gieo $%s$ hạt giống, số hạt nảy mầm dự đoán là $%s \\cdot %s\\%% = %s$ (hạt).'
            % (N_moi, N_moi, pct_nay, du_bao_c)
        )
        loigiai_vdc_1 = (
            'Gọi $M$ là số hạt giống cần gieo. Ta có $M \\cdot %s\\%% \\approx %s \\Rightarrow M \\approx \\dfrac{%s}{%s} = %s$ (hạt).'
            % (pct_nay, cay_can, cay_can, fmt_dec(Fraction(pct_nay, 100), 2), hat_can)
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
