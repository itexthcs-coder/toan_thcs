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


def fmt_vn(val):
    if isinstance(val, Decimal):
        s = str(val)
    elif isinstance(val, float):
        s = str(round(val, 6))
        if s.endswith('.0'):
            s = s[:-2]
    else:
        s = str(val)
    return s.replace('.', ',')


def fmt_frac_tex(fr):
    if fr.denominator == 1:
        return str(fr.numerator)
    if fr.numerator < 0:
        return '-\\frac{%s}{%s}' % (abs(fr.numerator), fr.denominator)
    return '\\frac{%s}{%s}' % (fr.numerator, fr.denominator)


def fmt_linear_tex(a_fr, b_fr, var='x'):
    # Định dạng ax + b với a_fr, b_fr là Fraction
    parts = []
    if a_fr != 0:
        if a_fr == 1:
            parts.append(var)
        elif a_fr == -1:
            parts.append('-%s' % var)
        else:
            parts.append('%s%s' % (fmt_frac_tex(a_fr), var))
    if b_fr != 0:
        if not parts:
            parts.append(fmt_frac_tex(b_fr))
        else:
            if b_fr > 0:
                parts.append('+ %s' % fmt_frac_tex(b_fr))
            else:
                parts.append('- %s' % fmt_frac_tex(abs(b_fr)))
    if not parts:
        return '0'
    return ' '.join(parts)


def bt_dang17_p2_b4_c7_ds8(self):
    # Dạng 17 (Thực tế 2): Bể chứa nước y = rate * x + v_init
    rate = random.choice([20, 25, 30])
    v_init = random.choice([200, 300, 400])
    t_fill = random.choice([40, 48, 50])
    v_max = v_init + rate * t_fill

    t_check = 20
    v_check = v_init + rate * t_check

    noidungcauhoi = (
        '''Một bể chứa nước sạch của gia đình có dung tích $%s\\text{ lít}$, hiện đang chứa sẵn $%s\\text{ lít}$ nước. Người ta mở một vòi bơm nước vào bể với lưu lượng đều đặn là $%s\\text{ lít/phút}$. Gọi $y$ (lít) là lượng nước có trong bể sau $x$ (phút) mở vòi ($0 \\le x \\le %s$). Xét tính đúng sai của các khẳng định sau:'''
        % (v_max, v_init, rate, t_fill)
    )

    # Ý a
    nb_da_1_d = '\\True Công thức tính lượng nước $y$ theo thời gian $x$ là $y = %sx + %s$' % (rate, v_init)
    nb_da_1_s = 'Công thức tính lượng nước $y$ theo thời gian $x$ là $y = %sx + %s$' % (v_init, rate)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        '''Sau $x$ phút, lượng nước vòi bơm thêm vào bể là $%sx$ (lít). Cộng với $%s$ lít có sẵn ban đầu, tổng lượng nước trong bể là $y = %sx + %s$.'''
        % (rate, v_init, rate, v_init)
    )
    list_nb_2 = [loigiai_nb_1]

    # Ý b
    th_da_1_d = '\\True Sau $%s\\text{ phút}$ bơm nước, lượng nước trong bể đạt mức $%s\\text{ lít}$' % (t_check, v_check)
    th_da_1_s = 'Sau $%s\\text{ phút}$ bơm nước, lượng nước trong bể đạt mức $%s\\text{ lít}$' % (t_check, rate * t_check)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        '''Thay $x = %s$ vào công thức hàm số ta được: $y = %s \\cdot %s + %s = %s$ (lít).'''
        % (t_check, rate, t_check, v_init, v_check)
    )
    list_th_2 = [loigiai_th_1]

    # Ý c
    vd_da_1_d = '\\True Đồ thị của hàm số trên là một đoạn thẳng không đi qua gốc tọa độ'
    vd_da_1_s = 'Đồ thị của hàm số trên đi qua gốc tọa độ $O(0; 0)$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        '''Vì hệ số tự do $b = %s \\neq 0$ nên đồ thị hàm số cắt trục tung tại điểm $(0; %s)$, không đi qua gốc tọa độ $O(0; 0)$.'''
        % (v_init, v_init)
    )
    list_vd_2 = [loigiai_vd_1]

    # Ý d
    vdc_da_1_d = '\\True Thời gian cần thiết để bơm đầy bể nước (tính từ lúc bắt đầu mở vòi) là $%s\\text{ phút}$' % t_fill
    vdc_da_1_s = 'Thời gian cần thiết để bơm đầy bể nước (tính từ lúc bắt đầu mở vòi) là $%s\\text{ phút}$' % (v_max // rate)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        '''Khi bể đầy nước thì $y = %s$. Ta có phương trình: $%sx + %s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (phút).'''
        % (v_max, rate, v_init, v_max, rate, v_max - v_init, t_fill)
    )
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \end{minipage}\n\n')
    return content
