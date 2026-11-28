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

def bt_dang19_p2_b3_c8_ds8(self):
    # Dạng 19: Dự báo lượng khách du lịch theo mùa (4 quý)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        q1 = random.choice([40000, 42500, 45000])
        q2 = random.choice([30000, 31000, 32500])
        q4 = random.choice([25000, 27500])
        q3 = 125000 - q1 - q2 - q4
        tong_cu = 125000
        tong_moi = 150000

        p_q1 = fmt_dec(Fraction(q1, tong_cu), 3)
        p_q1_sai = fmt_dec(Fraction(q2, tong_cu), 3)
        db_6thang = (tong_moi * (q1 + q2)) // tong_cu
        db_6thang_sai = db_6thang - 3000
        db_q4 = (tong_moi * q4) // tong_cu
        tang_q4 = db_q4 - q4
        tang_q4_sai = tang_q4 + 2500

        noidungcauhoi = (
            'Khu du lịch sinh thái Tràng An thống kê số lượt khách tham quan trong $4$ quý của năm ngoái: Quý I có $%s$ lượt; Quý II có $%s$ lượt; Quý III có $%s$ lượt; Quý IV có $%s$ lượt. Năm nay, ban quản lý đặt mục tiêu đón tổng cộng $150\,000$ lượt khách và dự kiến tỉ lệ phân bổ khách giữa các quý giữ nguyên như năm ngoái. Xét tính đúng sai của các khẳng định sau:'
            % (f"{q1:,}".replace(",", "\,"), f"{q2:,}".replace(",", "\,"), f"{q3:,}".replace(",", "\,"), f"{q4:,}".replace(",", "\,"))
        )

        nb_da_1_d = '\\True Tổng số lượt khách tham quan khu du lịch trong năm ngoái là $125\,000$ lượt'
        nb_da_1_s = 'Tổng số lượt khách tham quan khu du lịch trong năm ngoái là $135\,000$ lượt'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm một du khách đến tham quan vào Quý I năm ngoái là $%s$' % p_q1
        th_da_1_s = 'Xác suất thực nghiệm một du khách đến tham quan vào Quý I năm ngoái là $%s$' % p_q1_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Theo dự báo, lượng khách đến tham quan trong $6$ tháng đầu năm nay (Quý I và Quý II) vào khoảng $%s$ lượt' % f"{db_6thang:,}".replace(",", "\,")
        vd_da_1_s = 'Theo dự báo, lượng khách đến tham quan trong $6$ tháng đầu năm nay (Quý I và Quý II) vào khoảng $%s$ lượt' % f"{db_6thang_sai:,}".replace(",", "\,")
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Lượng khách dự kiến trong Quý IV năm nay tăng thêm $%s$ lượt so với Quý IV năm ngoái' % f"{tang_q4:,}".replace(",", "\,")
        vdc_da_1_s = 'Lượng khách dự kiến trong Quý IV năm nay tăng thêm $%s$ lượt so với Quý IV năm ngoái' % f"{tang_q4_sai:,}".replace(",", "\,")
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Tổng số lượt khách năm ngoái là $%s + %s + %s + %s = 125\,000$ (lượt).'
            % (f"{q1:,}".replace(",", "\,"), f"{q2:,}".replace(",", "\,"), f"{q3:,}".replace(",", "\,"), f"{q4:,}".replace(",", "\,"))
        )
        loigiai_th_1 = (
            'Xác suất thực nghiệm một du khách tham quan vào Quý I năm ngoái là $\\dfrac{%s}{125\,000} = %s$.'
            % (f"{q1:,}".replace(",", "\,"), p_q1)
        )
        loigiai_vd_1 = (
            'Xác suất thực nghiệm khách tham quan trong $6$ tháng đầu năm là $\\dfrac{%s + %s}{125\,000}$.\\'
            'Lượng khách dự kiến trong $6$ tháng đầu năm nay là $150\,000 \\cdot \\dfrac{%s}{125\,000} = %s$ (lượt).'
            % (f"{q1:,}".replace(",", "\,"), f"{q2:,}".replace(",", "\,"), f"{q1+q2:,}".replace(",", "\,"), f"{db_6thang:,}".replace(",", "\,"))
        )
        loigiai_vdc_1 = (
            'Lượng khách dự kiến trong Quý IV năm nay là $150\,000 \\cdot \\dfrac{%s}{125\,000} = %s$ (lượt).\\'
            'So với năm ngoái, lượng khách Quý IV tăng thêm $%s - %s = %s$ (lượt).'
            % (f"{q4:,}".replace(",", "\,"), f"{db_q4:,}".replace(",", "\,"), f"{db_q4:,}".replace(",", "\,"), f"{q4:,}".replace(",", "\,"), f"{tang_q4:,}".replace(",", "\,"))
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
