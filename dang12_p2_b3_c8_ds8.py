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

def bt_dang12_p2_b3_c8_ds8(self):
    # Dạng 12: Khôi phục bảng thống kê bị mờ và dự báo
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t_duoi = 300
        t_tren = 200
        tong = 500
        tm_duoi = random.choice([45, 50, 60])
        ck_duoi = random.choice([165, 180])
        x_val = t_duoi - tm_duoi - ck_duoi

        tm_tren = random.choice([110, 115, 120])
        qt_tren = random.choice([40, 45])
        y_val = t_tren - tm_tren - qt_tren

        tong_tm = tm_duoi + tm_tren
        tong_ck = ck_duoi + y_val
        tong_qt = x_val + qt_tren

        p_tm_tren = fmt_dec(Fraction(tm_tren, t_tren), 3)
        p_tm_tren_sai = fmt_dec(Fraction(tm_tren, tong), 3)

        N_khach = 1200
        du_bao_ck = (N_khach * tong_ck) // tong
        du_bao_ck_sai = du_bao_ck + 24

        N_duoi = 600
        du_bao_qt_duoi = (N_duoi * x_val) // t_duoi
        du_bao_qt_duoi_sai = du_bao_qt_duoi - 10

        bang_tex = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|}\n'
            '\\hline\n'
            '\\textbf{Hình thức thanh toán} & Tiền mặt & Chuyển khoản & Quẹt thẻ & Tổng cộng \\\\ \n'
            '\\hline\n'
            '\\textbf{Khách hàng dưới $35$ tuổi} & $%s$ & $%s$ & $x$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\textbf{Khách hàng từ $35$ tuổi trở lên} & $%s$ & $y$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\textbf{Tổng số} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (tm_duoi, ck_duoi, t_duoi, tm_tren, qt_tren, t_tren, tong_tm, tong_ck, tong_qt, tong)
        )

        noidungcauhoi = (
            'Một siêu thị điện máy thống kê số lượng khách hàng mua hàng theo hình thức thanh toán trong tuần qua nhưng có hai ô số liệu bị nhòe mực (kí hiệu bởi $x, y$):%s'
            'Xét tính đúng sai của các khẳng định sau:'
            % bang_tex
        )

        nb_da_1_d = '\\True Giá trị của $x$ và $y$ lần lượt là $%s$ và $%s$' % (x_val, y_val)
        nb_da_1_s = 'Giá trị của $x$ và $y$ lần lượt là $%s$ và $%s$' % (y_val, x_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Chọn ngẫu nhiên một khách hàng từ $35$ tuổi trở lên, xác suất thực nghiệm để người đó thanh toán bằng tiền mặt là $%s$' % p_tm_tren
        th_da_1_s = 'Chọn ngẫu nhiên một khách hàng từ $35$ tuổi trở lên, xác suất thực nghiệm để người đó thanh toán bằng tiền mặt là $%s$' % p_tm_tren_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Nếu tuần tới siêu thị đón $%s$ lượt khách, dự đoán có khoảng $%s$ lượt khách thanh toán bằng hình thức chuyển khoản' % (N_khach, du_bao_ck)
        vd_da_1_s = 'Nếu tuần tới siêu thị đón $%s$ lượt khách, dự đoán có khoảng $%s$ lượt khách thanh toán bằng hình thức chuyển khoản' % (N_khach, du_bao_ck_sai)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Nếu tuần tới có $%s$ khách hàng dưới $35$ tuổi đến mua sắm, dự đoán có khoảng $%s$ người thanh toán bằng quẹt thẻ' % (N_duoi, du_bao_qt_duoi)
        vdc_da_1_s = 'Nếu tuần tới có $%s$ khách hàng dưới $35$ tuổi đến mua sắm, dự đoán có khoảng $%s$ người thanh toán bằng quẹt thẻ' % (N_duoi, du_bao_qt_duoi_sai)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Dựa vào tổng hàng, ta tìm được $x = %s - (%s + %s) = %s$ và $y = %s - (%s + %s) = %s$.'
            % (t_duoi, tm_duoi, ck_duoi, x_val, t_tren, tm_tren, qt_tren, y_val)
        )
        loigiai_th_1 = (
            'Trong $%s$ khách hàng từ $35$ tuổi trở lên, có $%s$ người thanh toán bằng tiền mặt.\\'
            'Xác suất thực nghiệm tương ứng là $\\dfrac{%s}{%s} = %s$.'
            % (t_tren, tm_tren, tm_tren, t_tren, p_tm_tren)
        )
        loigiai_vd_1 = (
            'Xác suất thực nghiệm khách thanh toán chuyển khoản là $\\dfrac{%s}{%s}$.\\'
            'Với $%s$ lượt khách, dự đoán số lượt thanh toán chuyển khoản là $%s \\cdot \\dfrac{%s}{%s} = %s$ (lượt).'
            % (tong_ck, tong, N_khach, N_khach, tong_ck, tong, du_bao_ck)
        )
        loigiai_vdc_1 = (
            'Trong nhóm khách dưới $35$ tuổi, xác suất thực nghiệm thanh toán quẹt thẻ là $\\dfrac{%s}{%s}$.\\'
            'Với $%s$ khách dưới $35$ tuổi, dự đoán có $%s \\cdot \\dfrac{%s}{%s} = %s$ (người).'
            % (x_val, t_duoi, N_duoi, N_duoi, x_val, t_duoi, du_bao_qt_duoi)
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
