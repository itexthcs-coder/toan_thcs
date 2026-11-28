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

def bt_dang17_p2_b3_c8_ds8(self):
    # Dạng 17: Kiểm soát chất lượng dây chuyền sản xuất (Tính toán lợi nhuận dự kiến)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = 300
        loai1 = random.choice([276, 279, 282])
        loai2 = random.choice([12, 15])
        loi = n - loai1 - loai2
        pct_loi = fmt_dec(Fraction(loi * 100, n), 1)
        pct_loi_sai = fmt_dec(Fraction(loai2 * 100, n), 1)

        N_lo = 1500
        db_1 = (N_lo * loai1) // n
        db_2 = (N_lo * loai2) // n
        db_loi = (N_lo * loi) // n
        lai_tong = db_1 * 50 + db_2 * 10 - db_loi * 80  # đơn vị: nghìn đồng
        lai_sai = db_1 * 50 + db_2 * 10

        noidungcauhoi = (
            'Một xưởng may kiểm tra ngẫu nhiên $%s$ chiếc áo sơ mi xuất xưởng thì thấy có $%s$ chiếc đạt loại $1$, $%s$ chiếc đạt loại $2$ và số còn lại là hàng lỗi không thể bán. Biết mỗi chiếc áo loại $1$ lãi $50\,000$ đồng, loại $2$ lãi $10\,000$ đồng, và hàng lỗi bị lỗ $80\,000$ đồng. Xét tính đúng sai của các khẳng định sau:'
            % (n, loai1, loai2)
        )

        nb_da_1_d = '\\True Xác suất thực nghiệm để một chiếc áo xuất xưởng là hàng lỗi bằng $%s\\%%$' % pct_loi
        nb_da_1_s = 'Xác suất thực nghiệm để một chiếc áo xuất xưởng là hàng lỗi bằng $%s\\%%$' % pct_loi_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Trong lô hàng $%s$ chiếc áo tiếp theo, dự đoán có khoảng $%s$ chiếc đạt loại $1$' % (N_lo, db_1)
        th_da_1_s = 'Trong lô hàng $%s$ chiếc áo tiếp theo, dự đoán có khoảng $%s$ chiếc đạt loại $1$' % (N_lo, db_1 - 30)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Trong lô hàng $%s$ chiếc áo đó, dự đoán có khoảng $%s$ chiếc đạt loại $2$' % (N_lo, db_2)
        vd_da_1_s = 'Trong lô hàng $%s$ chiếc áo đó, dự đoán có khoảng $%s$ chiếc đạt loại $2$' % (N_lo, db_2 + 15)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Tổng số tiền lãi dự kiến thu được từ lô hàng $%s$ chiếc áo này là $%s\,000$ đồng' % (N_lo, f"{lai_tong:,}".replace(",", "\,"))
        vdc_da_1_s = 'Tổng số tiền lãi dự kiến thu được từ lô hàng $%s$ chiếc áo này là $%s\,000$ đồng' % (N_lo, f"{lai_sai:,}".replace(",", "\,"))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Số áo lỗi trong mẫu kiểm tra là $%s - %s - %s = %s$ (chiếc).\\'
            'Xác suất thực nghiệm để một chiếc áo là hàng lỗi bằng $\\dfrac{%s}{%s} = %s\\%%$.'
            % (n, loai1, loai2, loi, loi, n, pct_loi)
        )
        loigiai_th_1 = (
            'Trong lô hàng $%s$ chiếc áo, số áo đạt loại $1$ dự đoán là $%s \\cdot \\dfrac{%s}{%s} = %s$ (chiếc).'
            % (N_lo, N_lo, loai1, n, db_1)
        )
        loigiai_vd_1 = (
            'Trong lô hàng $%s$ chiếc áo, số áo đạt loại $2$ dự đoán là $%s \\cdot \\dfrac{%s}{%s} = %s$ (chiếc).'
            % (N_lo, N_lo, loai2, n, db_2)
        )
        loigiai_vdc_1 = (
            'Số áo lỗi dự đoán trong lô hàng là $%s \\cdot \\dfrac{%s}{%s} = %s$ (chiếc).\\'
            'Tổng số tiền lãi dự kiến là $%s \\cdot 50\,000 + %s \\cdot 10\,000 - %s \\cdot 80\,000 = %s\,000$ (đồng).'
            % (N_lo, loi, n, db_loi, db_1, db_2, db_loi, f"{lai_tong:,}".replace(",", "\,"))
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
