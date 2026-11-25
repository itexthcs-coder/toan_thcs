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


def bt_dang4_p2_b2_c5_ds8(self):
    # Dạng 4 (Thông hiểu - Thuần túy toán học): Phân tích biểu đồ cột đơn có giá trị thập phân và tỉ số
    k = random.choice([1, 2])
    p = Decimal('14.4') * k
    q = Decimal('18.0') * k
    r = Decimal('10.8') * k
    s_val = Decimal('16.8') * k
    tong = p + q + r + s_val
    diff_qr = q - r
    
    def fmt_vn(val):
        return f"{val:.1f}".replace(".", ",")
        
    max_y = float(q)
    scale_y = 2.4 / max_y
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {Giá trị};
    \\draw[line width=1pt, ->] (0,0) -- (5.8,0) node[right] {Đại lượng};
    \\draw[line width=1pt, fill=black!20] (0.6,0) rectangle (1.3,%.2f);
    \\node[above] at (0.95,%.2f) {$%s$};
    \\node[below] at (0.95,0) {$P$};
    \\draw[line width=1pt, fill=black!20] (1.8,0) rectangle (2.5,%.2f);
    \\node[above] at (2.15,%.2f) {$%s$};
    \\node[below] at (2.15,0) {$Q$};
    \\draw[line width=1pt, fill=black!20] (3.0,0) rectangle (3.7,%.2f);
    \\node[above] at (3.35,%.2f) {$%s$};
    \\node[below] at (3.35,0) {$R$};
    \\draw[line width=1pt, fill=black!20] (4.2,0) rectangle (4.9,%.2f);
    \\node[above] at (4.55,%.2f) {$%s$};
    \\node[below] at (4.55,0) {$S$};
    \\end{tikzpicture}
    \\end{center}""" % (float(p)*scale_y, float(p)*scale_y, fmt_vn(p),
                          float(q)*scale_y, float(q)*scale_y, fmt_vn(q),
                          float(r)*scale_y, float(r)*scale_y, fmt_vn(r),
                          float(s_val)*scale_y, float(s_val)*scale_y, fmt_vn(s_val)))
    
    noidungcauhoi = ("""Cho biểu đồ cột biểu diễn giá trị của bốn đại lượng $P, Q, R, S$:%sXét tính đúng sai của các khẳng định sau:""" % tikz_code)
    
    nb_da_1_d = '\\True Tổng giá trị của bốn đại lượng $P, Q, R, S$ bằng $%s$' % int(tong)
    nb_da_1_s = 'Tổng giá trị của bốn đại lượng $P, Q, R, S$ bằng $%s$' % (int(tong) + 10)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tổng giá trị của bốn đại lượng là: $%s + %s + %s + %s = %s$.""" % (fmt_vn(p), fmt_vn(q), fmt_vn(r), fmt_vn(s_val), int(tong)))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Đại lượng $Q$ lớn hơn đại lượng $R$ đúng $%s$ đơn vị' % fmt_vn(diff_qr)
    th_da_1_s = 'Đại lượng $Q$ lớn hơn đại lượng $R$ đúng $%s$ đơn vị' % fmt_vn(diff_qr + Decimal('1.0'))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Hiệu giá trị giữa $Q$ và $R$ là: $%s - %s = %s$.""" % (fmt_vn(q), fmt_vn(r), fmt_vn(diff_qr)))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Tỉ số giữa giá trị của $P$ và giá trị của $Q$ bằng $\\dfrac{4}{5}$'
    vd_da_1_s = 'Tỉ số giữa giá trị của $P$ và giá trị của $Q$ bằng $\\dfrac{3}{4}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tỉ số giữa giá trị của $P$ và $Q$ là: $\\dfrac{%s}{%s} = \\dfrac{144}{180} = \\dfrac{4}{5}$.""" % (fmt_vn(p), fmt_vn(q)))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Nếu chuyển dữ liệu này sang biểu đồ hình quạt tròn thì hình quạt biểu diễn $S$ chiếm $30\\%%$'
    vdc_da_1_d = 'Nếu chuyển dữ liệu này sang biểu đồ hình quạt tròn thì hình quạt biểu diễn $S$ chiếm $28\\%%$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Tỉ lệ phần trăm của đại lượng $S$ trong tổng thể là: $\\dfrac{%s}{%s} \\cdot 100\\%% = 28\\%%$ (không phải $30\\%%$).""" % (fmt_vn(s_val), int(tong)))
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
