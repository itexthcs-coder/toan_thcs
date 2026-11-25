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

def bt_dang6_p2_b3_c5_ds8(self):
    # Dạng 6: Phân tích xu thế biến động lãi suất tiết kiệm qua biểu đồ đa đường
    m_vals = [6.2, 5.8, 5.4, 5.1]
    n_vals = [5.5, 5.6, 5.9, 6.3]
    shift = random.choice([0.0, 0.2, 0.4])
    m_vals = [round(x + shift, 1) for x in m_vals]
    n_vals = [round(x + shift, 1) for x in n_vals]
    
    def fmt_vn(val):
        return str(val).replace('.', ',')
        
    ms = [fmt_vn(x) for x in m_vals]
    ns = [fmt_vn(x) for x in n_vals]
    
    ym = [round((x - (5.0 + shift)) * 2.0 + 0.5, 2) for x in m_vals]
    yn = [round((x - (5.0 + shift)) * 2.0 + 0.5, 2) for x in n_vals]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[below] {Quý};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Lãi suất ($\\%%/\\text{năm}$)};\n' +
        '\\coordinate (M1) at (1.0,%s);\n' % ym[0] +
        '\\coordinate (M2) at (2.2,%s);\n' % ym[1] +
        '\\coordinate (M3) at (3.4,%s);\n' % ym[2] +
        '\\coordinate (M4) at (4.6,%s);\n' % ym[3] +
        '\\draw[line width=1pt] (M1)--(M2)--(M3)--(M4);\n' +
        '\\fill (M1) circle (1pt) node[above] {$%s$};\n' % ms[0] +
        '\\fill (M2) circle (1pt) node[above] {$%s$};\n' % ms[1] +
        '\\fill (M3) circle (1pt) node[below] {$%s$};\n' % ms[2] +
        '\\fill (M4) circle (1pt) node[below] {$%s$};\n' % ms[3] +
        '\\coordinate (N1) at (1.0,%s);\n' % yn[0] +
        '\\coordinate (N2) at (2.2,%s);\n' % yn[1] +
        '\\coordinate (N3) at (3.4,%s);\n' % yn[2] +
        '\\coordinate (N4) at (4.6,%s);\n' % yn[3] +
        '\\draw[line width=1pt, dashed] (N1)--(N2)--(N3)--(N4);\n' +
        '\\fill (N1) circle (1pt) node[below] {$%s$};\n' % ns[0] +
        '\\fill (N2) circle (1pt) node[below] {$%s$};\n' % ns[1] +
        '\\fill (N3) circle (1pt) node[above] {$%s$};\n' % ns[2] +
        '\\fill (N4) circle (1pt) node[above] {$%s$};\n' % ns[3] +
        '\\node[below] at (1.0,0) {Quý I};\n' +
        '\\node[below] at (2.2,0) {Quý II};\n' +
        '\\node[below] at (3.4,0) {Quý III};\n' +
        '\\node[below] at (4.6,0) {Quý IV};\n' +
        '\\draw[line width=1pt] (5.3,2.8) -- (6.0,2.8) node[right] {Ngân hàng M};\n' +
        '\\draw[line width=1pt, dashed] (5.3,2.1) -- (6.0,2.1) node[right] {Ngân hàng N};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ đoạn thẳng kép dưới đây theo dõi lãi suất huy động kì hạn $12$ tháng ($\\%%/\\text{năm}$) của Ngân hàng M và Ngân hàng N qua bốn quý của năm:\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Lãi suất của Ngân hàng M giảm liên tục qua cả $4$ quý'
    nb_da_1_s = 'Lãi suất của Ngân hàng M tăng liên tục qua cả $4$ quý'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Từ Quý I đến Quý IV, lãi suất của Ngân hàng M lần lượt là $%s\\%%; %s\\%%; %s\\%%; %s\\%%$, giảm liên tục qua từng quý.' % (ms[0], ms[1], ms[2], ms[3]))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Lãi suất của Ngân hàng N tăng liên tục qua cả $4$ quý'
    th_da_1_s = 'Lãi suất của Ngân hàng N giữ nguyên không đổi qua cả $4$ quý'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Từ Quý I đến Quý IV, lãi suất của Ngân hàng N lần lượt là $%s\\%%; %s\\%%; %s\\%%; %s\\%%$, tăng liên tục qua từng quý.' % (ns[0], ns[1], ns[2], ns[3]))
    list_th_2 = [loigiai_th_1]
    
    # c (Sai)
    vd_da_1_d = '\\True Trong nửa đầu năm (Quý I và Quý II), lãi suất của Ngân hàng M luôn cao hơn Ngân hàng N'
    vd_da_1_s = 'Trong nửa đầu năm (Quý I và Quý II), lãi suất của Ngân hàng N luôn cao hơn Ngân hàng M'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tại Quý I ($%s\\%% > %s\\%%$) và Quý II ($%s\\%% > %s\\%%$), đường biểu diễn của Ngân hàng M nằm phía trên nên lãi suất Ngân hàng M cao hơn Ngân hàng N.' % (ms[0], ns[0], ms[1], ns[1]))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Hai đường biểu diễn của hai ngân hàng cắt nhau tại một thời điểm nằm giữa Quý II và Quý III'
    vdc_da_1_s = 'Hai đường biểu diễn của hai ngân hàng cắt nhau tại một thời điểm nằm giữa Quý III và Quý IV'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tại Quý II, lãi suất M ($%s\\%%$) cao hơn N ($%s\\%%$), nhưng sang Quý III lãi suất M ($%s\\%%$) thấp hơn N ($%s\\%%$) nên hai đường cắt nhau giữa Quý II và Quý III.' % (ms[1], ns[1], ms[2], ns[2]))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
