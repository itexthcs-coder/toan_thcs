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

def bt_dang5_p2_b3_c8_ds8(self):
    # Dạng 5: Khảo sát nhóm học sinh tham gia câu lạc bộ (Bảng chéo 2x2)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([100, 120, 150, 160])
        nam = random.randint(n // 2 + 2, n // 2 + 15)
        nu = n - nam
        nam_clb = random.randint(15, nam - 10)
        nu_clb = random.randint(15, nu - 10)
        nu_k_clb = nu - nu_clb
        nam_k_clb = nam - nam_clb
        tong_clb = nam_clb + nu_clb

        p_nu_k_tex = fmt_frac(nu_k_clb, n)
        p_nu_k_sai_tex = fmt_frac(nu_clb, n)
        p_clb_dec = fmt_dec(Fraction(tong_clb, n), 4)
        p_clb_sai_dec = fmt_dec(Fraction(n - tong_clb, n), 4)
        p_nam_k_tex = fmt_frac(nam_k_clb, n)
        p_nam_k_sai_tex = fmt_frac(nam_clb, n)

        noidungcauhoi = (
            'Khối $8$ của một trường có $%s$ học sinh, trong đó có $%s$ học sinh nam. Trong đợt đăng ký câu lạc bộ nghệ thuật, có $%s$ bạn nam và $%s$ bạn nữ tham gia. Chọn ngẫu nhiên một học sinh khối $8$. Xét tính đúng sai của các khẳng định sau:'
            % (n, nam, nam_clb, nu_clb)
        )

        nb_da_1_d = '\\True Có $%s$ học sinh nữ trong khối $8$' % nu
        nb_da_1_s = 'Có $%s$ học sinh nữ trong khối $8$' % (nu + 5)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất để chọn được một bạn nữ không tham gia câu lạc bộ nghệ thuật là $%s$' % p_nu_k_tex
        th_da_1_s = 'Xác suất để chọn được một bạn nữ không tham gia câu lạc bộ nghệ thuật là $%s$' % p_nu_k_sai_tex
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất để chọn được một học sinh có tham gia câu lạc bộ nghệ thuật là $%s$' % p_clb_dec
        vd_da_1_s = 'Xác suất để chọn được một học sinh có tham gia câu lạc bộ nghệ thuật là $%s$' % p_clb_sai_dec
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất để chọn được một bạn nam không tham gia câu lạc bộ nghệ thuật bằng $%s$' % p_nam_k_tex
        vdc_da_1_s = 'Xác suất để chọn được một bạn nam không tham gia câu lạc bộ nghệ thuật bằng $%s$' % p_nam_k_sai_tex
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Số học sinh nữ trong khối $8$ là $%s - %s = %s$ (học sinh).'
            % (n, nam, nu)
        )
        loigiai_th_1 = (
            'Số học sinh nữ không tham gia câu lạc bộ nghệ thuật là $%s - %s = %s$ (học sinh).\\'
            'Xác suất để chọn được một bạn nữ không tham gia câu lạc bộ là $\\dfrac{%s}{%s} = %s$.'
            % (nu, nu_clb, nu_k_clb, nu_k_clb, n, p_nu_k_tex)
        )
        loigiai_vd_1 = (
            'Tổng số học sinh tham gia câu lạc bộ nghệ thuật là $%s + %s = %s$ (học sinh).\\'
            'Xác suất để chọn được một học sinh có tham gia câu lạc bộ là $\\dfrac{%s}{%s} = %s$.'
            % (nam_clb, nu_clb, tong_clb, tong_clb, n, p_clb_dec)
        )
        loigiai_vdc_1 = (
            'Số học sinh nam không tham gia câu lạc bộ nghệ thuật là $%s - %s = %s$ (học sinh).\\'
            'Xác suất để chọn được một bạn nam không tham gia câu lạc bộ là $\\dfrac{%s}{%s} = %s$.'
            % (nam, nam_clb, nam_k_clb, nam_k_clb, n, p_nam_k_tex)
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
