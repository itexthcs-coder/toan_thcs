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

def bt_dang15_p2_b3_c8_ds8(self):
    # Dạng 15: Dự báo lưu lượng giao thông (Giao thoa hai biến cố)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = 250
        loi1 = random.choice([100, 110, 120])
        loi2 = random.choice([45, 50, 55])
        giao = random.choice([15, 20])
        chi_loi1 = loi1 - giao
        chi_loi1_sai = loi1 + giao
        hop = loi1 + loi2 - giao
        khong_loi = n - hop

        p_hop = fmt_dec(Fraction(hop, n), 3)
        p_hop_sai = fmt_dec(Fraction(loi1 + loi2, n), 3)
        p_khong = fmt_dec(Fraction(khong_loi, n), 3)
        p_khong_sai = fmt_dec(Fraction(hop, n), 3)
        du_bao_1000 = khong_loi * 4
        du_bao_1000_sai = hop * 4

        noidungcauhoi = (
            'Camera AI đếm lưu lượng phương tiện qua ngã tư X trong $%s$ lượt đèn xanh ghi nhận được: $%s$ lượt có xe máy vượt vạch trước khi đèn xanh bật, $%s$ lượt có ô tô đi sai làn, trong đó có $%s$ lượt xảy ra đồng thời cả hai lỗi trên. Xét tính đúng sai của các khẳng định sau:'
            % (n, loi1, loi2, giao)
        )

        nb_da_1_d = '\\True Số lượt đèn xanh chỉ có duy nhất lỗi xe máy vượt vạch là $%s$ lượt' % chi_loi1
        nb_da_1_s = 'Số lượt đèn xanh chỉ có duy nhất lỗi xe máy vượt vạch là $%s$ lượt' % chi_loi1_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Có ít nhất một trong hai lỗi vi phạm xảy ra trong một lượt đèn xanh" là $%s$' % p_hop
        th_da_1_s = 'Xác suất thực nghiệm của biến cố "Có ít nhất một trong hai lỗi vi phạm xảy ra trong một lượt đèn xanh" là $%s$' % p_hop_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Không có lỗi vi phạm nào trong hai lỗi trên xảy ra" là $%s$' % p_khong
        vd_da_1_s = 'Xác suất thực nghiệm của biến cố "Không có lỗi vi phạm nào trong hai lỗi trên xảy ra" là $%s$' % p_khong_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Trong một ngày ngã tư X có $1\,000$ lượt đèn xanh, dự đoán có khoảng $%s$ lượt không xảy ra hai lỗi vi phạm trên' % du_bao_1000
        vdc_da_1_s = 'Trong một ngày ngã tư X có $1\,000$ lượt đèn xanh, dự đoán có khoảng $%s$ lượt không xảy ra hai lỗi vi phạm trên' % du_bao_1000_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Số lượt đèn xanh chỉ có duy nhất lỗi xe máy vượt vạch là $%s - %s = %s$ (lượt).'
            % (loi1, giao, chi_loi1)
        )
        loigiai_th_1 = (
            'Số lượt đèn xanh có ít nhất một trong hai lỗi vi phạm là $%s + %s - %s = %s$ (lượt).\\'
            'Xác suất thực nghiệm tương ứng là $\\dfrac{%s}{%s} = %s$.'
            % (loi1, loi2, giao, hop, hop, n, p_hop)
        )
        loigiai_vd_1 = (
            'Xác suất thực nghiệm của biến cố "Không có lỗi vi phạm nào trong hai lỗi trên xảy ra" là $1 - %s = %s$.'
            % (p_hop, p_khong)
        )
        loigiai_vdc_1 = (
            'Trong $1\,000$ lượt đèn xanh, dự đoán số lượt không xảy ra hai lỗi trên là $1\,000 \\cdot %s = %s$ (lượt).'
            % (p_khong, du_bao_1000)
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
