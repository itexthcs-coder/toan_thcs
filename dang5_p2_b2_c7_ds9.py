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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang5_p2_b2_c7_ds9(self):
    don_vi = random.choice([5, 6, 8])
    s1, s2, s3, s4 = 6, 8, 4, 2
    tong = 20 * don_vi
    m1, m2, m3, m4 = s1 * don_vi, s2 * don_vi, s3 * don_vi, s4 * don_vi

    bang_tranh = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|l|}\n'
        '\\hline\n'
        'CLB Bóng rổ & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
        '\\hline\n'
        'CLB Nhảy hiện đại & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
        '\\hline\n'
        'CLB Tin học & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
        '\\hline\n'
        'CLB Mỹ thuật & $\\bullet\\ \\bullet$ \\\\ \n'
        '\\hline\n'
        '\\end{tabular}\\\\[4pt]\n'
        '\\textit{(Mỗi biểu tượng $\\bullet$ biểu diễn cho $%s$ học sinh)}\n'
        '\\end{center}'
    ) % (don_vi)

    noidungcauhoi = ('Biểu đồ tranh sau thống kê số học sinh khối 9 đăng kí tham gia các câu lạc bộ (mỗi học sinh chỉ chọn $1$ CLB):%sXét tính đúng sai của các khẳng định sau:' % (bang_tranh))

    nb_da_1_d = '\\True Tổng số học sinh khối 9 đăng kí tham gia các câu lạc bộ là $%s$ học sinh' % (tong)
    nb_da_1_s = 'Tổng số học sinh khối 9 đăng kí tham gia các câu lạc bộ là $%s$ học sinh' % (tong + 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tổng số biểu tượng là $6 + 8 + 4 + 2 = 20$ biểu tượng, tương ứng với $20 \\cdot %s = %s$ học sinh.' % (don_vi, tong))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tần số tương đối của số học sinh chọn CLB Bóng rổ là $30\\%$'
    th_da_1_s = 'Tần số tương đối của số học sinh chọn CLB Bóng rổ là $25\\%$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Số học sinh chọn CLB Bóng rổ là $%s$, chiếm $\\frac{%s}{%s} \\cdot 100\\% = 30\\%$.' % (m1, m1, tong))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tần số tương đối của số học sinh chọn CLB Mỹ thuật là $10\\%$'
    vd_da_1_s = 'Tần số tương đối của số học sinh chọn CLB Mỹ thuật là $2\\%$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Số học sinh chọn CLB Mỹ thuật là $%s$, chiếm $\\frac{%s}{%s} \\cdot 100\\% = 10\\%$.' % (m4, m4, tong))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu vẽ biểu đồ hình quạt tròn thì góc ở tâm của hình quạt biểu diễn CLB Nhảy hiện đại bằng $144^\\circ$'
    vdc_da_1_s = 'Nếu vẽ biểu đồ hình quạt tròn thì góc ở tâm của hình quạt biểu diễn CLB Nhảy hiện đại bằng $120^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('CLB Nhảy hiện đại chiếm $\\frac{%s}{%s} \\cdot 100\\%% = 40\\%%$ nên góc ở tâm tương ứng là $360^\\circ \\cdot 40\\%% = 144^\\circ$.' % (m2, tong))
    list_vdc_2 = [loigiai_vdc_1]
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

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
