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

def bt_dang19_p2_b5_c7_ds8(self):
    # Dạng 19 (Thực tế): Chuyển động thẳng đều của hai xe trên cùng tuyến đường
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [(60, 75, 20, 8, 20), (50, 70, 30, 8, 30), (60, 80, 30, 8, 30)]
        v1, v2, d0, h_meet, m_meet = random.choice(cases)
        t_meet = Fraction(d0, v2 - v1)

        nb_da_1_d = '\\True Vận tốc của xe thứ nhất là $%d\\text{ km/h}$ và của xe thứ hai là $%d\\text{ km/h}$ chính là hệ số góc của hai đường thẳng biểu diễn chuyển động' % (v1, v2)
        nb_da_1_s = 'Vận tốc của xe thứ nhất là $%d\\text{ km/h}$ và của xe thứ hai là $%d\\text{ km/h}$' % (d0, v2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Trong hàm số $s_1 = %dt + %d$ và $s_2 = %dt$, các hệ số góc $a_1 = %d$ và $a_2 = %d$ lần lượt biểu thị vận tốc của xe thứ nhất và xe thứ hai.'''
                        % (v1, d0, v2, v1, v2))

        th_da_1_d = '\\True Tại thời điểm xuất phát ($t = 0$), xe thứ nhất cách trạm thu phí xa hơn xe thứ hai $%d\\text{ km}$' % d0
        th_da_1_s = 'Tại thời điểm xuất phát ($t = 0$), xe thứ hai cách trạm thu phí xa hơn xe thứ nhất $%d\\text{ km}$' % d0
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $t = 0$ ta được $s_1(0) = %d\\text{ km}$ và $s_2(0) = 0\\text{ km}$, nên xe thứ nhất xuất phát phía trước xe thứ hai $%d\\text{ km}$.'''
                        % (d0, d0))

        vd_da_1_d = '\\True Vì hai đường thẳng có hệ số góc khác nhau ($%d \\neq %d$) nên đồ thị của chúng cắt nhau, tức là xe thứ hai đuổi kịp xe thứ nhất' % (v1, v2)
        vd_da_1_s = 'Hai đường thẳng biểu diễn chuyển động của hai xe song song với nhau nên hai xe không bao giờ gặp nhau'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì $a_1 = %d \\neq a_2 = %d$ nên hai đường thẳng cắt nhau tại một điểm có hoành độ $t > 0$, nghĩa là xe thứ hai đuổi kịp xe thứ nhất.'''
                        % (v1, v2))

        vdc_da_1_d = '\\True Thời điểm xe thứ hai đuổi kịp xe thứ nhất là lúc $%d\\text{ giờ } %d\\text{ phút}$ sáng' % (h_meet, m_meet)
        vdc_da_1_s = 'Thời điểm xe thứ hai đuổi kịp xe thứ nhất là lúc $%d\\text{ giờ } %d\\text{ phút}$ sáng' % (h_meet + 1, m_meet)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Giải phương trình hoành độ giao điểm: $%dt = %dt + %d \\Leftrightarrow %dt = %d \\Leftrightarrow t = %s$ giờ $= 1$ giờ $%d$ phút. Cộng thêm thời điểm xuất phát lúc $7$ giờ sáng ta được lúc $%d$ giờ $%d$ phút sáng.'''
                         % (v2, v1, d0, v2 - v1, d0, fmt_num(t_meet), m_meet, h_meet, m_meet))

        noidungcauhoi = ('''Hai ô tô cùng xuất phát lúc $7\\text{ giờ}$ sáng từ hai vị trí khác nhau trên cùng một tuyến đường cao tốc thẳng hướng về thành phố B. Quãng đường $s$ (km) từ vị trí mỗi xe đến trạm thu phí đầu tuyến sau $t$ (giờ) kể từ lúc $7\\text{ giờ}$ được cho bởi: \\
\\begin{tabular}{|l|c|c|}
\\hline
\\textbf{Phương tiện} & \textbf{Xe thứ nhất} & \textbf{Xe thứ hai} \\
\\hline
\\textbf{Phương trình chuyển động} & $s_1 = %dt + %d$ & $s_2 = %dt$ \\
\\hline
\\end{tabular}'''
                         % (v1, d0, v2))

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
