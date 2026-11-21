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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D

def bt_dang10_p2_b1_c2_ds8(self):
    # Khai báo biến
    a = randint(2, 4)
    b = randint(1, 5)
    c = randint(b + 1, b + 6)
    x1 = Rational(b + c, a)
    x2 = Rational(b - c, a)
    tong_x = x1 + x2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét bài toán tìm số thực $x$ biết $(%sx - %s)^2 - %s = 0$. Các khẳng định sau đúng hay sai?''' % (latex(a), latex(b), latex(c**2)))

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Vế trái của đẳng thức viết được dưới dạng tích là $(%sx - %s)(%sx + %s)$.' % (latex(a), latex(b + c), latex(a), latex(c - b))
    nb_da_1_s = 'Vế trái của đẳng thức viết được dưới dạng tích là $(%sx - %s)(%sx + %s)$.' % (latex(a), latex(b + c**2), latex(a), latex(c**2 - b))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ('''Ta có $(%sx - %s)^2 - %s = (%sx - %s)^2 - %s^2 = (%sx - %s - %s)(%sx - %s + %s) = (%sx - %s)(%sx + %s)$.'''
                    % (latex(a), latex(b), latex(c**2), latex(a), latex(b), latex(c),
                       latex(a), latex(b), latex(c), latex(a), latex(b), latex(c),
                       latex(a), latex(b + c), latex(a), latex(c - b)))
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Đẳng thức đã cho tương đương với $%sx - %s = %s$ hoặc $%sx - %s = -%s$.' % (latex(a), latex(b), latex(c), latex(a), latex(b), latex(c))
    th_da_1_s = 'Đẳng thức đã cho chỉ tương đương với $%sx - %s = %s$.' % (latex(a), latex(b), latex(c))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ('''Từ $(%sx - %s)(%sx + %s) = 0$, ta suy ra $%sx - %s = 0$ hoặc $%sx + %s = 0$, tức là $%sx - %s = %s$ hoặc $%sx - %s = -%s$.'''
                    % (latex(a), latex(b + c), latex(a), latex(c - b),
                       latex(a), latex(b + c), latex(a), latex(c - b),
                       latex(a), latex(b), latex(c), latex(a), latex(b), latex(c)))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Có hai giá trị phân biệt của $x$ thỏa mãn đẳng thức đã cho.'
    vd_da_1_s = 'Có duy nhất một giá trị của $x$ thỏa mãn đẳng thức đã cho.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ('''Giải hai trường hợp ta tìm được hai giá trị phân biệt là $x = %s$ và $x = %s$.''' % (latex(x1), latex(x2)))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Tổng các giá trị của $x$ tìm được bằng $%s$.' % (latex(tong_x))
    vdc_da_1_s = 'Tổng các giá trị của $x$ tìm được bằng $0$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ('''Tổng hai giá trị của $x$ là $%s + \\left(%s\\right) = %s$.''' % (latex(x1), latex(x2), latex(tong_x)))
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
