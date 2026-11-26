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

def bt_dang17_p2_b5_c7_ds8(self):
    # Dạng 17 (Thực tế): Độ dốc mái nhà và tiêu chuẩn thoát nước mưa
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        width = random.choice([8, 10])
        if width == 8:
            h_old = 1.6
            h_new = 2.0
        else:
            h_old = 1.8
            h_new = 2.2

        a_old = round(-h_old / width, 4)
        a_new = round(-h_new / width, 4)
        pct_old = int(round(abs(a_old) * 100))

        str_h_old = fmt_num(h_old)
        str_h_new = fmt_num(h_new)
        str_a_old = fmt_num(a_old)
        str_abs_a_old = fmt_num(abs(a_old))
        str_a_new = fmt_num(a_new)

        nb_da_1_d = '\\True Đường thẳng biểu diễn mặt cắt mái tôn đi xuống từ trái sang phải nên có hệ số góc $a < 0$'
        nb_da_1_s = 'Đường thẳng biểu diễn mặt cắt mái tôn đi xuống từ trái sang phải nên có hệ số góc $a > 0$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Khi $x$ tăng từ $0$ đến $%d$ thì $y$ giảm từ $%s$ về $0$, đường thẳng đi xuống từ trái sang phải nên hệ số góc $a < 0$.'''
                        % (width, str_h_old))

        th_da_1_d = '\\True Phương trình đường thẳng biểu diễn mặt cắt mái tôn là $y = %sx + %s$' % (str_a_old, str_h_old)
        th_da_1_s = 'Phương trình đường thẳng biểu diễn mặt cắt mái tôn là $y = %sx + %s$' % (str_abs_a_old, str_h_old)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Đường thẳng đi qua $B(0; %s)$ nên $b = %s$. Thay tọa độ $A(%d; 0)$ ta có $0 = a \\cdot %d + %s \\Rightarrow a = %s$. Vậy $y = %sx + %s$.'''
                        % (str_h_old, str_h_old, width, width, str_h_old, str_a_old, str_a_old, str_h_old))

        vd_da_1_d = '\\True Thiết kế mái tôn này đạt tiêu chuẩn thoát nước mưa của kỹ sư vì độ dốc bằng $%d\\%%$' % pct_old
        vd_da_1_s = 'Thiết kế mái tôn này không đạt tiêu chuẩn thoát nước mưa của kỹ sư'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Ta có $|a| = |%s| = %s = %d\\%% > 15\\%%$ nên mái tôn đạt tiêu chuẩn thoát nước mưa.'''
                        % (str_a_old, str_abs_a_old, pct_old))

        vdc_da_1_d = '\\True Nếu giữ nguyên điểm thấp nhất tại $(%d; 0)$ và nâng điểm cao nhất lên $%s\\text{ m}$ thì mái tôn mới không song song với mái tôn cũ' % (width, str_h_new)
        vdc_da_1_s = 'Nếu giữ nguyên điểm thấp nhất tại $(%d; 0)$ và nâng điểm cao nhất lên $%s\\text{ m}$ thì mái tôn mới song song với mái tôn cũ' % (width, str_h_new)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi nâng điểm cao nhất lên $%s\\text{ m}$, hệ số góc mới là $a' = -\\frac{%s}{%d} = %s \\neq %s$ nên hai đường thẳng cắt nhau tại $(%d; 0)$ chứ không song song.'''
                         % (str_h_new, str_h_new, width, str_a_new, str_a_old, width))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (B) at (0,2);
\\coordinate (A) at (4.5,0);
\\draw[line width=1pt, ->] (-1,0)--(5.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-0.8)--(0,3.2) node[left] {$y$};
\\draw[line width=1pt] (B)--(A);
\\draw[line width=1pt, dashed] (O)--(B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (A) circle (1pt) node[below] {$A$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Trong thiết kế xây dựng, mặt cắt nghiêng của một mái tôn được mô hình hóa trên hệ trục tọa độ $Oxy$ (đơn vị trên mỗi trục là mét, trục $Ox$ nằm ngang theo trần nhà) bởi đường thẳng $y = ax + b$ ($x \\ge 0$). Để thoát nước mưa tốt, kỹ sư quy định độ dốc tối thiểu của mái phải đạt $15\\%%$ (tức là $|a| \\ge 0,15$). Một ngôi nhà có chiều rộng mái theo phương ngang là $%d\\text{ m}$, điểm cao nhất của mái cách trần $%s\\text{ m}$ (tại $x = 0$) và điểm thấp nhất chạm trần (tại $x = %d$). \\ %s'''
                         % (width, str_h_old, width, tikz_fig))

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
