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

def bt_dang20_p2_b5_c7_ds8(self):
    # Dạng 20 (Thực tế): Mức tiêu thụ pin của hai dòng điện thoại thông minh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (12.5, 100, 10, 80, 8, 4, 10),
            (20, 100, 16, 80, 5, 2.5, 10),
        ]
        rA, pA0, rB, pB0, t_zero, t_half, diff_half = random.choice(cases)
        str_rA = fmt_num(rA)
        str_rB = fmt_num(rB)
        str_t_half = fmt_num(t_half)

        nb_da_1_d = '\\True Hệ số góc của cả hai đường thẳng đều âm, biểu thị phần trăm pin giảm dần theo thời gian sử dụng'
        nb_da_1_s = 'Hệ số góc của cả hai đường thẳng đều dương vì phần trăm pin luôn không âm'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Các hệ số góc $a_A = -%s < 0$ và $a_B = -%s < 0$, biểu thị lượng pin giảm dần khi thời gian $t$ tăng.'''
                        % (str_rA, str_rB))

        th_da_1_d = '\\True Tốc độ hao pin mỗi giờ của điện thoại A nhanh hơn điện thoại B'
        th_da_1_s = 'Tốc độ hao pin mỗi giờ của điện thoại A chậm hơn điện thoại B'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Mỗi giờ điện thoại A giảm $%s\\%%$ pin còn điện thoại B giảm $%s\\%%$ pin ($%s > %s$), nên điện thoại A hao pin nhanh hơn.'''
                        % (str_rA, str_rB, str_rA, str_rB))

        vd_da_1_d = '\\True Hai chiếc điện thoại sẽ cạn sạch pin ($y = 0$) tại cùng một thời điểm sau $%d$ giờ sử dụng liên tục' % t_zero
        vd_da_1_s = 'Điện thoại B sẽ cạn sạch pin trước điện thoại A vì ban đầu có ít pin hơn'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Cho $y_A = 0 \\Rightarrow -%st + %d = 0 \\Rightarrow t = %d$ (giờ); cho $y_B = 0 \\Rightarrow -%st + %d = 0 \\Rightarrow t = %d$ (giờ). Vậy hai đường thẳng cắt nhau tại điểm $(%d; 0)$ trên trục hoành.'''
                        % (str_rA, pA0, t_zero, str_rB, pB0, t_zero, t_zero))

        vdc_da_1_d = '\\True Sau $%s$ giờ sử dụng liên tục, lượng pin còn lại của điện thoại A nhiều hơn điện thoại B là $%d\\%%$' % (str_t_half, diff_half)
        vdc_da_1_s = 'Sau $%s$ giờ sử dụng liên tục, lượng pin còn lại của hai điện thoại bằng nhau' % str_t_half
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Tại $t = %s$, $y_A = -%s \\cdot %s + %d = 50\\%%$ và $y_B = -%s \\cdot %s + %d = 40\\%%$. Vậy điện thoại A còn nhiều hơn điện thoại B là $50\\%% - 40\\%% = %d\\%%$.'''
                         % (str_t_half, str_rA, str_t_half, pA0, str_rB, str_t_half, pB0, diff_half))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (2,0);
\\coordinate (T) at (0.5,2.25);
\\draw[line width=1pt, ->] (-2,0)--(4,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.5)--(0,3.8) node[left] {$y$};
\\draw[line width=1pt] (-0.5,3.75)--(3,-1.5) node[right] {$y=ax+b$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (T) circle (1pt) node[right] {$T$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Trong một bài kiểm tra thực tế về thời lượng pin khi phát video liên tục ở độ sáng tối đa, phần trăm pin còn lại $y$ ($\\%%$) của hai chiếc điện thoại A và B sau $t$ (giờ) sử dụng được mô hình hóa gần đúng bởi các hàm số bậc nhất: \\
\\begin{tabular}{|l|c|c|}
\\hline
\\textbf{Thiết bị} & \textbf{Điện thoại A} & \textbf{Điện thoại B} \\
\\hline
\\textbf{Hàm số phần trăm pin} & $y_A = -%st + %d$ & $y_B = -%st + %d$ \\
\\hline
\\end{tabular} \\ %s'''
                         % (str_rA, pA0, str_rB, pB0, tikz_fig))

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
