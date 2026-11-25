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


def bt_dang19_p2_b2_c5_ds8(self):
    # Dạng 19 (Vận dụng - Thực tế): Thống kê rác thải nhựa tái chế học đường từ biểu đồ tranh
    unit = random.choice([20, 25, 30])
    c6, c7, c8, c9 = 6, 8, 9, 7
    v6, v7, v8, v9 = c6 * unit, c7 * unit, c8 * unit, c9 * unit
    tong = v6 + v7 + v8 + v9
    pct_7 = (Decimal(str(v7 * 100)) / Decimal(str(tong))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    s_pct_7 = str(pct_7).replace(".", ",")
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (-1.2, 0.2) rectangle (5.6, 3.4);
    \\draw[line width=1pt] (0.4, 0.2) -- (0.4, 3.4);
    \\draw[line width=1pt] (-1.2, 2.6) -- (5.6, 2.6);
    \\draw[line width=1pt] (-1.2, 1.8) -- (5.6, 1.8);
    \\draw[line width=1pt] (-1.2, 1.0) -- (5.6, 1.0);
    \\node at (-0.4, 3.0) {Khối 6};
    \\node at (-0.4, 2.2) {Khối 7};
    \\node at (-0.4, 1.4) {Khối 8};
    \\node at (-0.4, 0.6) {Khối 9};
    \\foreach \\i in {0,...,5} { \\draw[line width=1pt] (0.9 + \\i*0.52, 3.0) circle (0.18); }
    \\foreach \\i in {0,...,7} { \\draw[line width=1pt] (0.9 + \\i*0.52, 2.2) circle (0.18); }
    \\foreach \\i in {0,...,8} { \\draw[line width=1pt] (0.9 + \\i*0.52, 1.4) circle (0.18); }
    \\foreach \\i in {0,...,6} { \\draw[line width=1pt] (0.9 + \\i*0.52, 0.6) circle (0.18); }
    \\draw[line width=1pt] (0.5, -0.3) circle (0.18);
    \\node[right] at (0.8, -0.3) {ứng với $%s$ vỏ chai nhựa};
    \\end{tikzpicture}
    \\end{center}""" % unit)
    
    noidungcauhoi = (
        "Trong phong trào ``Kế hoạch nhỏ'' bảo vệ môi trường, số vỏ chai nhựa thu gom được của bốn khối lớp 6, 7, 8, 9 một trường THCS được biểu diễn bằng biểu đồ tranh dưới đây:"
        + tikz_code +
        "Xét tính đúng sai của các khẳng định sau:"
    )
    
    nb_da_1_d = '\\True Khối 8 thu gom được nhiều vỏ chai nhất với $%s$ vỏ chai' % v8
    nb_da_1_s = 'Khối 8 thu gom được nhiều vỏ chai nhất với $%s$ vỏ chai' % v7
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Khối 8 có nhiều biểu tượng nhất ($9$ biểu tượng), ứng với $9 \\cdot %s = %s$ (vỏ chai).""" % (unit, v8))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Tổng số vỏ chai nhựa toàn trường thu gom được là $%s$ vỏ chai' % tong
    th_da_1_s = 'Tổng số vỏ chai nhựa toàn trường thu gom được là $%s$ vỏ chai' % (tong + unit)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tổng số biểu tượng của cả bốn khối là $6 + 8 + 9 + 7 = 30$ biểu tượng, ứng với $30 \\cdot %s = %s$ (vỏ chai).""" % (unit, tong))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Nếu chuyển dữ liệu này sang biểu đồ hình quạt tròn để báo cáo tỉ lệ đóng góp của từng khối thì khối 7 chiếm $%s\\%%$ (làm tròn đến chữ số thập phân thứ nhất)' % s_pct_7
    vd_da_1_s = 'Nếu chuyển dữ liệu này sang biểu đồ hình quạt tròn thì khối 7 chiếm $30,0\\%%$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tỉ lệ đóng góp của khối 7 là: $\\dfrac{%s}{%s} \\cdot 100\\%% = \\dfrac{8}{30} \\cdot 100\\%% \\approx %s\\%%$.""" % (v7, tong, s_pct_7))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Số vỏ chai khối 8 thu gom được nhiều hơn khối 6 là $3$ vỏ chai'
    vdc_da_1_d = 'Số vỏ chai khối 8 thu gom được nhiều hơn khối 6 là $%s$ vỏ chai' % (v8 - v6)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Khối 8 nhiều hơn khối 6 là $3$ biểu tượng, ứng với $3 \\cdot %s = %s$ vỏ chai (không phải $3$ vỏ chai).""" % (unit, v8 - v6))
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
