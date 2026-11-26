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


def bt_dang12_p2_b4_c7_ds8(self):
    # Dạng 12: Điểm M(x0; y0) trên (d): y = -1/2 x + b thỏa mãn quan hệ giữa x0 và y0
    # Chọn b chia hết cho 3 và 5 để tọa độ đẹp: b = 3 hoặc 6
    b_val = random.choice([3, 6])
    # y = -1/2 x + b
    # a) x0 = 4 => y0 = -2 + b
    y_at_4 = -2 + b_val
    # b) y0 = 2 x0 => 2 x0 = -1/2 x0 + b => 5/2 x0 = b => x0 = 2b/5, y0 = 4b/5
    x_2x = Fraction(2 * b_val, 5)
    y_2x = Fraction(4 * b_val, 5)
    # c) Cách đều 2 trục tọa độ: |y0| = |x0| => y0 = x0 hoặc y0 = -x0
    # TH1: x0 = -1/2 x0 + b => 3/2 x0 = b => x0 = 2b/3, y0 = 2b/3
    # TH2: -x0 = -1/2 x0 + b => -1/2 x0 = b => x0 = -2b, y0 = 2b
    x_eq = (2 * b_val) // 3
    x_opp = -2 * b_val
    y_opp = 2 * b_val

    noidungcauhoi = (
        '''Cho hàm số bậc nhất $y = -\\dfrac{1}{2}x + %s$ có đồ thị là đường thẳng $(d)$. Gọi $M(x_0; y_0)$ là một điểm thuộc đường thẳng $(d)$. Xét tính đúng sai của các khẳng định sau:'''
        % b_val
    )

    # Ý a
    nb_da_1_d = '\\True Nếu hoành độ của $M$ bằng $4$ thì tung độ của $M$ bằng $%s$' % y_at_4
    nb_da_1_s = 'Nếu hoành độ của $M$ bằng $4$ thì tung độ của $M$ bằng $%s$' % (2 + b_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        '''Thay $x_0 = 4$ vào phương trình $(d)$ ta được $y_0 = -\\dfrac{1}{2} \\cdot 4 + %s = -2 + %s = %s$.'''
        % (b_val, b_val, y_at_4)
    )
    list_nb_2 = [loigiai_nb_1]

    # Ý b
    th_da_1_d = '\\True Nếu tung độ của $M$ gấp đôi hoành độ của $M$ thì tọa độ điểm $M$ là $\\left(%s; %s\\right)$' % (fmt_frac_tex(x_2x), fmt_frac_tex(y_2x))
    th_da_1_s = 'Nếu tung độ của $M$ gấp đôi hoành độ của $M$ thì tọa độ điểm $M$ là $\\left(%s; %s\\right)$' % (fmt_frac_tex(y_2x), fmt_frac_tex(x_2x))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        '''Theo giả thiết $y_0 = 2x_0$. Thay vào phương trình $(d)$ ta được: $2x_0 = -\\dfrac{1}{2}x_0 + %s \\Leftrightarrow \\dfrac{5}{2}x_0 = %s \\Leftrightarrow x_0 = %s$.\\
Suy ra $y_0 = 2 \\cdot %s = %s$. Vậy $M\\left(%s; %s\\right)$.'''
        % (b_val, b_val, fmt_frac_tex(x_2x), fmt_frac_tex(x_2x), fmt_frac_tex(y_2x), fmt_frac_tex(x_2x), fmt_frac_tex(y_2x))
    )
    list_th_2 = [loigiai_th_1]

    # Ý c
    vd_da_1_d = '\\True Trên đường thẳng $(d)$, có hai điểm cách đều hai trục tọa độ là $(%s; %s)$ và $(%s; %s)$' % (x_eq, x_eq, x_opp, y_opp)
    vd_da_1_s = 'Trên đường thẳng $(d)$, chỉ có duy nhất một điểm cách đều hai trục tọa độ'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        '''Điểm $M(x_0; y_0)$ cách đều hai trục tọa độ khi $|y_0| = |x_0| \\Leftrightarrow y_0 = x_0$ hoặc $y_0 = -x_0$.\\
- Với $y_0 = x_0$: $x_0 = -\\dfrac{1}{2}x_0 + %s \\Leftrightarrow \\dfrac{3}{2}x_0 = %s \\Leftrightarrow x_0 = %s \\Rightarrow M_1(%s; %s)$.\\
- Với $y_0 = -x_0$: $-x_0 = -\\dfrac{1}{2}x_0 + %s \\Leftrightarrow -\\dfrac{1}{2}x_0 = %s \\Leftrightarrow x_0 = %s \\Rightarrow M_2(%s; %s)$.\\
Vậy có hai điểm thỏa mãn yêu cầu bài toán.'''
        % (b_val, b_val, x_eq, x_eq, x_eq, b_val, b_val, x_opp, x_opp, y_opp)
    )
    list_vd_2 = [loigiai_vd_1]

    # Ý d
    vdc_da_1_d = '\\True Điểm $N(%s; %s)$ là điểm duy nhất trên $(d)$ có hoành độ và tung độ bằng nhau' % (x_eq, x_eq)
    vdc_da_1_s = 'Điểm $N(%s; %s)$ là điểm nằm trên $(d)$ có hoành độ và tung độ bằng nhau' % (b_val, b_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        '''Điều kiện hoành độ bằng tung độ là $y_0 = x_0$, giải ra ta được duy nhất $x_0 = y_0 = %s$, tức là điểm $N(%s; %s)$.'''
        % (x_eq, x_eq, x_eq)
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
