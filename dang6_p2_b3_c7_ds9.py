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


def bt_dang6_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    m1, m2, m3, m4 = 3 * k, 7 * k, 11 * k, 4 * k
    n = 25 * k

    noidungcauhoi = ('''Theo tiêu chuẩn đánh giá chất lượng giấc ngủ dựa trên tổng thời gian ngủ ban đêm của người trưởng thành: Thiếu ngủ nặng (dưới $5$ giờ), Thiếu ngủ nhẹ (từ $5$ đến dưới $6,5$ giờ), Ngủ đủ giấc (từ $6,5$ đến dưới $8$ giờ), Ngủ nhiều (từ $8$ đến dưới $10$ giờ). Khảo sát $%s$ nhân viên trực ca thu được kết quả: Thiếu ngủ nặng có $%s$ người; Thiếu ngủ nhẹ có $%s$ người; Ngủ đủ giấc có $%s$ người; Ngủ nhiều có $%s$ người.'''
                     % (n, m1, m2, m3, m4))

    list_nb_da_1 = [
        '\\True Nhóm số liệu tương ứng với mức ``Ngủ đủ giấc\'\' là $[6,5; 8)$',
        'Nhóm số liệu tương ứng với mức ``Ngủ đủ giấc\'\' là $[5; 6,5)$'
    ]
    loigiai_nb_1 = ('''Mức ``Ngủ đủ giấc\'\' gồm thời gian từ $6,5$ đến dưới $8$ giờ nên ứng với nhóm $[6,5; 8)$.''')

    list_th_da_1 = [
        '\\True Độ dài của các nhóm số liệu trong bảng thống kê trên không bằng nhau',
        'Độ dài của các nhóm số liệu trong bảng thống kê trên đều bằng nhau'
    ]
    loigiai_th_1 = ('''Các nhóm $[0; 5)$, $[5; 6,5)$, $[6,5; 8)$, $[8; 10)$ có độ dài lần lượt là $5$; $1,5$; $1,5$; $2$ nên không bằng nhau.''')

    list_vd_da_1 = [
        '\\True Tần số tương đối của nhóm $[5; 6,5)$ là $28\\%%$',
        'Tần số tương đối của nhóm $[5; 6,5)$ là $24\\%%$'
    ]
    loigiai_vd_1 = ('''Tần số tương đối của nhóm $[5; 6,5)$ là: $\\dfrac{%s}{%s} \\cdot 100\\%% = 28\\%%$.''' % (m2, n))

    list_vdc_da_1 = [
        '\\True Tỉ lệ nhân viên ngủ từ $6,5$ giờ trở lên chiếm $60\\%%$',
        'Tỉ lệ nhân viên ngủ từ $6,5$ giờ trở lên chiếm $44\\%%$'
    ]
    loigiai_vdc_1 = ('''Số nhân viên ngủ từ $6,5$ giờ trở lên là $%s + %s = %s$ (người), chiếm tỉ lệ $\\dfrac{%s}{%s} \\cdot 100\\%% = 60\\%%$.''' % (m3, m4, m3 + m4, m3 + m4, n))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

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
