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


def bt_dang4_p2_b2_c7_ds9(self):
    tong_gio = random.choice([20, 40])
    t_toan = int(tong_gio * 35 / 100)
    t_van = int(tong_gio * 20 / 100)
    t_anh = int(tong_gio * 25 / 100)
    hieu_av = t_anh - t_van

    hinh_quat = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) circle (2);\n'
        '\\draw[line width=1pt] (0,0) -- (0:2);\n'
        '\\draw[line width=1pt] (0,0) -- (126:2);\n'
        '\\draw[line width=1pt] (0,0) -- (198:2);\n'
        '\\draw[line width=1pt] (0,0) -- (288:2);\n'
        '\\node at (63:1.2) {$35\\%$};\n'
        '\\node at (162:1.2) {$20\\%$};\n'
        '\\node at (243:1.2) {$25\\%$};\n'
        '\\node at (324:1.2) {$20\\%$};\n'
        '\\node[right] at (2.3, 1.0) {Toán: $35\\%$};\n'
        '\\node[right] at (2.3, 0.3) {Ngữ văn: $20\\%$};\n'
        '\\node[right] at (2.3, -0.4) {Tiếng Anh: $25\\%$};\n'
        '\\node[right] at (2.3, -1.1) {Môn khác: $20\\%$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = ('Trong một tuần, bạn Minh dành tổng cộng $%s$ giờ để tự học tại nhà. Biểu đồ hình quạt tròn dưới đây biểu diễn tỉ lệ thời gian tự học các môn của Minh:%sXét tính đúng sai của các khẳng định sau:' % (tong_gio, hinh_quat))

    nb_da_1_d = '\\True Thời gian Minh dành cho môn Toán là $%s$ giờ' % (t_toan)
    nb_da_1_s = 'Thời gian Minh dành cho môn Toán là $%s$ giờ' % (t_toan + 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Thời gian Minh dành cho môn Toán là $%s \\cdot 35\\%% = %s$ (giờ).' % (tong_gio, t_toan))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Thời gian Minh dành cho môn Tiếng Anh nhiều hơn môn Ngữ văn là $%s$ giờ' % (hieu_av)
    th_da_1_s = 'Thời gian Minh dành cho môn Tiếng Anh nhiều hơn môn Ngữ văn là $%s$ giờ' % (hieu_av + 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Thời gian học Tiếng Anh là $%s \\cdot 25\\%% = %s$ giờ; thời gian học Ngữ văn là $%s \\cdot 20\\%% = %s$ giờ. Vậy Tiếng Anh nhiều hơn Ngữ văn $%s - %s = %s$ (giờ).' % (tong_gio, t_anh, tong_gio, t_van, t_anh, t_van, hieu_av))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Trên biểu đồ hình quạt tròn, số đo cung biểu diễn tỉ lệ thời gian học môn Ngữ văn là $72^\\circ$'
    vd_da_1_s = 'Trên biểu đồ hình quạt tròn, số đo cung biểu diễn tỉ lệ thời gian học môn Ngữ văn là $90^\\circ$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Số đo cung biểu diễn môn Ngữ văn ($20\\%$) là $360^\\circ \\cdot 20\\% = 72^\\circ$.')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tổng thời gian Minh học Toán và Tiếng Anh chiếm $60\\%$ tổng thời gian tự học'
    vdc_da_1_s = 'Tổng thời gian Minh học Toán và Tiếng Anh chiếm $50\\%$ tổng thời gian tự học'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng tỉ lệ thời gian học Toán và Tiếng Anh là $35\\% + 25\\% = 60\\%$.')
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
