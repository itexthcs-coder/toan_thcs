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


def bt_dang14_p2_b4_c7_ds8(self):
    # Dạng 14: Đường thẳng (d): y = mx + b (m != 0)
    b_val = random.choice([2, 4, 6])
    # Diện tích tam giác OAB bằng S => 1/2 * |b| * |b/m| = S => |m| = b^2 / (2S)
    # Chọn m_abs in {1, 2}, S = b^2 / (2 * m_abs)
    m_abs = random.choice([1, 2])
    s_area = (b_val * b_val) // (2 * m_abs)

    m_test = -2
    x_e = 3
    y_e = m_test * x_e + b_val

    noidungcauhoi = (
        '''Cho đường thẳng $(d): y = mx + %s$ ($m \\neq 0$). Xét tính đúng sai của các khẳng định sau:'''
        % b_val
    )

    # Ý a
    nb_da_1_d = '\\True Với mọi giá trị của $m \\neq 0$, đường thẳng $(d)$ luôn đi qua điểm cố định $K(0; %s)$' % b_val
    nb_da_1_s = 'Với mọi giá trị của $m \\neq 0$, đường thẳng $(d)$ luôn đi qua điểm cố định $K(%s; 0)$' % b_val
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        '''Khi $x = 0$, ta luôn có $y = m \\cdot 0 + %s = %s$ với mọi $m \\neq 0$. Vậy $(d)$ luôn đi qua điểm cố định $K(0; %s)$.'''
        % (b_val, b_val, b_val)
    )
    list_nb_2 = [loigiai_nb_1]

    # Ý b
    th_da_1_d = '\\True Khi $m > 0$, giao điểm của $(d)$ với trục hoành luôn có hoành độ âm'
    th_da_1_s = 'Khi $m > 0$, giao điểm của $(d)$ với trục hoành luôn có hoành độ dương'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        '''Cho $y = 0 \\Rightarrow mx + %s = 0 \\Leftrightarrow x = -\\dfrac{%s}{m}$. Vì $%s > 0$ và $m > 0$ nên $x = -\\dfrac{%s}{m} < 0$.'''
        % (b_val, b_val, b_val, b_val)
    )
    list_th_2 = [loigiai_th_1]

    # Ý c
    vd_da_1_d = '\\True Để đường thẳng $(d)$ tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$ thì $m = %s$ hoặc $m = -%s$' % (s_area, m_abs, m_abs)
    vd_da_1_s = 'Chỉ có duy nhất một giá trị của $m$ là $m = %s$ để đường thẳng $(d)$ tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$' % (m_abs, s_area)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        '''Đường thẳng $(d)$ cắt trục tung tại $A(0; %s)$ và cắt trục hoành tại $B\\left(-\\dfrac{%s}{m}; 0\\right)$.\\
Ta có $OA = %s$ và $OB = \\dfrac{%s}{|m|}$. Diện tích tam giác $OAB$ là: $S = \\dfrac{1}{2} OA \\cdot OB = \\dfrac{1}{2} \\cdot %s \\cdot \\dfrac{%s}{|m|} = \\dfrac{%s}{|m|}$.\\
Theo đề bài: $\\dfrac{%s}{|m|} = %s \\Leftrightarrow |m| = %s \\Leftrightarrow m = %s$ hoặc $m = -%s$.'''
        % (b_val, b_val, b_val, b_val, b_val, b_val, (b_val * b_val) // 2, (b_val * b_val) // 2, s_area, m_abs, m_abs, m_abs)
    )
    list_vd_2 = [loigiai_vd_1]

    # Ý d
    vdc_da_1_d = '\\True Khi $m = %s$, đường thẳng $(d)$ đi qua điểm $E(%s; %s)$' % (m_test, x_e, y_e)
    vdc_da_1_s = 'Khi $m = %s$, đường thẳng $(d)$ không đi qua điểm $E(%s; %s)$' % (m_test, x_e, y_e)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        '''Khi $m = %s$, hàm số có dạng $y = %sx + %s$. Thay $x = %s$ vào ta được $y = %s \\cdot %s + %s = %s$. Vậy $E(%s; %s) \\in (d)$.'''
        % (m_test, m_test, b_val, x_e, m_test, x_e, b_val, y_e, x_e, y_e)
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
