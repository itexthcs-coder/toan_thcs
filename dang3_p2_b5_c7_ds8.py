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


def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def fmt_num(val):
    if isinstance(val, int):
        return str(val)
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val.numerator < 0:
            return '-\\frac{%d}{%d}' % (-val.numerator, val.denominator)
        return '\\frac{%d}{%d}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val)

def fmt_line(a, b, var='x'):
    if a == 1:
        sa = var
    elif a == -1:
        sa = '-' + var
    else:
        sa = '%s%s' % (fmt_num(a), var)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_num(b))
    else:
        return '%s - %s' % (sa, fmt_num(-b))

def bt_dang3_p2_b5_c7_ds8(self):
    # Dạng 3: Tìm điều kiện tham số để hàm số bậc nhất có hệ số góc cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
        k2 = k * k
        m_target = k + random.choice([1, 2])
        a_target = m_target * m_target - k2
        m_test = k - 1
        a_test = m_test * m_test - k2
        c_parallel = random.choice([-5, -3, 3, 5, 7])

        nb_da_1_d = '\\True Hàm số đã cho là hàm số bậc nhất khi và chỉ khi $m \\neq %d$ và $m \\neq -%d$' % (k, k)
        nb_da_1_s = 'Hàm số đã cho luôn là hàm số bậc nhất với mọi giá trị của $m$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Hàm số $y = (m^2 - %d)x + m - %d$ là hàm số bậc nhất khi hệ số của $x$ khác $0$, tức là $m^2 - %d \\neq 0 \\Leftrightarrow m \\neq %d$ và $m \\neq -%d$.'''
                        % (k2, k, k2, k, k))

        th_da_1_d = '\\True Để đồ thị hàm số là đường thẳng có hệ số góc bằng $%d$ thì $m = %d$ hoặc $m = -%d$' % (a_target, m_target, m_target)
        th_da_1_s = 'Để đồ thị hàm số là đường thẳng có hệ số góc bằng $%d$ thì chỉ có $m = %d$' % (a_target, m_target)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Hệ số góc bằng $%d$ khi $m^2 - %d = %d \\Leftrightarrow m^2 = %d \\Leftrightarrow m = %d$ hoặc $m = -%d$ (đều thỏa mãn $m \\neq \\pm %d$).'''
                        % (a_target, k2, a_target, m_target * m_target, m_target, m_target, k))

        vd_da_1_d = '\\True Khi $m = %d$, góc tạo bởi đồ thị hàm số với trục $Ox$ là góc tù' % m_test
        vd_da_1_s = 'Khi $m = %d$, góc tạo bởi đồ thị hàm số với trục $Ox$ là góc nhọn' % m_test
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Thay $m = %d$ vào hệ số góc ta được $a = %d^2 - %d = %d < 0$. Vì $a < 0$ nên góc tạo bởi đường thẳng với trục $Ox$ là góc tù.'''
                        % (m_test, m_test, k2, a_test))

        vdc_da_1_d = '\\True Có hai giá trị của $m$ để đồ thị hàm số song song với đường thẳng $y = %s$' % fmt_line(a_target, c_parallel)
        vdc_da_1_s = 'Có duy nhất một giá trị của $m$ để đồ thị hàm số song song với đường thẳng $y = %s$' % fmt_line(a_target, c_parallel)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Để đồ thị hàm số song song với đường thẳng $y = %s$ thì $m^2 - %d = %d$ và $m - %d \\neq %d$. Giải $m^2 - %d = %d$ được $m = %d$ hoặc $m = -%d$. Cả hai giá trị này đều thỏa mãn $m - %d \\neq %d$ nên có $2$ giá trị của $m$.'''
                         % (fmt_line(a_target, c_parallel), k2, a_target, k, c_parallel, k2, a_target, m_target, m_target, k, c_parallel))

        noidungcauhoi = ('''Cho hàm số $y = (m^2 - %d)x + m - %d$ với $m$ là tham số.''' % (k2, k))

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
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
