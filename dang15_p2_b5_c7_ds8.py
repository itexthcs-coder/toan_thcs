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

def bt_dang15_p2_b5_c7_ds8(self):
    # Dạng 15: Phép tịnh tiến đồ thị và sự bảo toàn hệ số góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = -random.choice([2, 3, 4])
        b_val = random.choice([3, 5, 7])
        p_right = random.choice([2, 3])
        q_down = random.choice([2, 4, 5])

        x_old = Fraction(-b_val, a_val)
        x_new = x_old + p_right
        b_new = -a_val * p_right + b_val - q_down

        nb_da_1_d = '\\True Đường thẳng $(d\')$ và đường thẳng $(d)$ có cùng hệ số góc'
        nb_da_1_s = 'Hệ số góc của đường thẳng $(d\')$ nhỏ hơn hệ số góc của $(d)$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Phép tịnh tiến giữ nguyên hướng của đường thẳng nên $(d\')$ song song hoặc trùng với $(d)$, suy ra hai đường thẳng có cùng hệ số góc $a = %d$.'''
                        % a_val)

        th_da_1_d = '\\True Khi tịnh tiến $(d)$ sang phải $%d$ đơn vị, giao điểm mới với trục hoành có hoành độ là $%s$' % (p_right, fmt_num(x_new))
        th_da_1_s = 'Khi tịnh tiến $(d)$ sang phải $%d$ đơn vị, giao điểm mới với trục hoành có hoành độ là $%s$' % (p_right, fmt_num(x_old - p_right))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Ban đầu $(d)$ cắt trục hoành tại điểm có hoành độ $x_0 = %s$. Khi tịnh tiến sang phải $%d$ đơn vị, hoành độ giao điểm mới là $%s + %d = %s$.'''
                        % (fmt_num(x_old), p_right, fmt_num(x_old), p_right, fmt_num(x_new)))

        vd_da_1_d = '\\True Phương trình của đường thẳng $(d\')$ là $y = %s$' % fmt_line(a_val, b_new)
        vd_da_1_s = 'Phương trình của đường thẳng $(d\')$ là $y = %s$' % fmt_line(a_val, b_new + 2 * a_val * p_right)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Điểm $(0; %d) \\in (d)$ qua phép tịnh tiến sang phải $%d$ đơn vị và xuống dưới $%d$ đơn vị biến thành điểm $(%d; %d) \\in (d\')$. Vì $(d\')$ có hệ số góc $a = %d$ nên $%d = %d \\cdot %d + b\' \\Rightarrow b\' = %d$. Vậy $(d\'): y = %s$.'''
                        % (b_val, p_right, q_down, p_right, b_val - q_down, a_val, b_val - q_down, a_val, p_right, b_new, fmt_line(a_val, b_new)))

        vdc_da_1_d = '\\True Góc tạo bởi đường thẳng $(d\')$ và trục $Ox$ bằng góc tạo bởi đường thẳng $(d)$ và trục $Ox$'
        vdc_da_1_s = 'Góc tạo bởi đường thẳng $(d\')$ và trục $Ox$ lớn hơn góc tạo bởi đường thẳng $(d)$ và trục $Ox$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Vì $(d)$ và $(d\')$ có cùng hệ số góc $a = %d$ nên góc tạo bởi hai đường thẳng này với trục $Ox$ bằng nhau.'''
                         % a_val)

        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho đường thẳng $(d): y = %s$. Người ta thực hiện tịnh tiến đường thẳng $(d)$ sang phải $%d$ đơn vị, sau đó tịnh tiến xuống dưới $%d$ đơn vị để thu được đường thẳng $(d\')$.'''
                         % (fmt_line(a_val, b_val), p_right, q_down))

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
