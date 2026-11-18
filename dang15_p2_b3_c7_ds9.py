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


def bt_dang15_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    m1, m2, m3, m4 = 12 * k, 18 * k, 6 * k, 4 * k
    them = 10 * k
    n_sang = 40 * k
    n_moi = 50 * k

    noidungcauhoi = ('''Một cửa hàng cà phê thống kê thời gian phục vụ (đơn vị: phút) cho $%s$ khách hàng trong buổi sáng:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian (phút) & $[1; 3)$ & $[3; 5)$ & $[5; 7)$ & $[7; 9)$ \\\\
\\hline
Số khách hàng & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Vào buổi trưa, cửa hàng phục vụ thêm $%s$ khách hàng nữa và cả $%s$ khách này đều có thời gian phục vụ thuộc nhóm $[3; 5)$.''' % (n_sang, m1, m2, m3, m4, them, them))

    list_nb_da_1 = [
        '\\True Trong buổi sáng, tỉ lệ khách hàng được phục vụ dưới $5$ phút là $75\\%%$',
        'Trong buổi sáng, tỉ lệ khách hàng được phục vụ dưới $5$ phút là $45\\%%$'
    ]
    loigiai_nb_1 = ('''Số khách được phục vụ dưới $5$ phút buổi sáng là $%s + %s = %s$, chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 75\\%%$.''' % (m1, m2, m1 + m2, m1 + m2, n_sang))

    list_th_da_1 = [
        '\\True Tính chung cả buổi sáng và buổi trưa, tần số tương đối của nhóm $[3; 5)$ tăng thêm $11\\%%$ so với buổi sáng',
        'Tính chung cả buổi sáng và buổi trưa, tần số tương đối của nhóm $[3; 5)$ tăng thêm $10\\%%$ so với buổi sáng'
    ]
    loigiai_th_1 = ('''Buổi sáng nhóm $[3; 5)$ chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 45\\%%$. Sau khi thêm, nhóm này chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 56\\%%$, tăng $56\\%% - 45\\%% = 11\\%%$.''' % (m2, n_sang, m2 + them, n_moi))

    list_vd_da_1 = [
        '\\True Tần số tương đối của nhóm $[1; 3)$ sau khi gộp thêm khách buổi trưa giảm xuống còn $24\\%%$',
        'Tần số tương đối của nhóm $[1; 3)$ sau khi gộp thêm khách buổi trưa vẫn giữ nguyên là $30\\%%$'
    ]
    loigiai_vd_1 = ('''Vì cỡ mẫu tăng từ $%s$ lên $%s$ trong khi tần số nhóm $[1; 3)$ giữ nguyên là $%s$ nên tần số tương đối mới là $\\dfrac{%s}{%s} \\cdot 100\\%% = 24\\%%$.''' % (n_sang, n_moi, m1, m1, n_moi))

    list_vdc_da_1 = [
        '\\True Sau khi gộp cả hai buổi, tỉ lệ khách hàng phải chờ từ $7$ phút trở lên giảm xuống còn $8\\%%$',
        'Sau khi gộp cả hai buổi, tỉ lệ khách hàng phải chờ từ $7$ phút trở lên là $10\\%%$'
    ]
    loigiai_vdc_1 = ('''Tần số tương đối của nhóm $[7; 9)$ sau khi gộp là $\\dfrac{%s}{%s} \\cdot 100\\%% = 8\\%%$.''' % (m4, n_moi))

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
