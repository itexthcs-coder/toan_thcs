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


def bt_dang6_p2_b2_c7_ds9(self):
    bo_goc = random.choice([(126, 90, 108, 36, 35, 25, 30), (144, 72, 108, 36, 40, 20, 30)])
    g1, g2, g3, g4, p1, p2, p3 = bo_goc

    hinh_quat = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) circle (2);\n'
        '\\draw[line width=1pt] (0,0) -- (0:2);\n'
        '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
        '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
        '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
        '\\node at (%s:1.2) {$%s^\\circ$};\n'
        '\\node at (%s:1.2) {$%s^\\circ$};\n'
        '\\node at (%s:1.2) {$%s^\\circ$};\n'
        '\\node at (%s:1.2) {$x^\\circ$};\n'
        '\\node[right] at (2.3, 1.0) {Trang trí trại: $%s^\\circ$};\n'
        '\\node[right] at (2.3, 0.3) {Âm thanh: $%s^\\circ$};\n'
        '\\node[right] at (2.3, -0.4) {Ẩm thực: $%s^\\circ$};\n'
        '\\node[right] at (2.3, -1.1) {Dự phòng: $x^\\circ$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (g1, g1+g2, g1+g2+g3, int(g1/2), g1, int(g1+g2/2), g2, int(g1+g2+g3/2), g3, int(g1+g2+g3+g4/2), g1, g2, g3)

    noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu chi phí tổ chức hội trại của một trường THCS gồm 4 hạng mục:%sXét tính đúng sai của các khẳng định sau:' % (hinh_quat))

    nb_da_1_d = '\\True Số đo góc ở tâm của hạng mục Dự phòng là $x = %s^\\circ$' % (g4)
    nb_da_1_s = 'Số đo góc ở tâm của hạng mục Dự phòng là $x = %s^\\circ$' % (g4 + 18)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Vì tổng số đo các góc ở tâm bằng $360^\\circ$ nên $x = 360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = %s^\\circ$.' % (g1, g2, g3, g4))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Hạng mục Âm thanh chiếm $%s\\%%$ tổng chi phí' % (p2)
    th_da_1_s = 'Hạng mục Âm thanh chiếm $%s\\%%$ tổng chi phí' % (p2 + 5)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Tỉ lệ chi phí cho hạng mục Âm thanh là $\\frac{%s^\\circ}{360^\\circ} \\cdot 100\\%% = %s\\%%$.' % (g2, p2))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Chi phí cho Trang trí trại chiếm tỉ lệ lớn nhất và bằng $%s\\%%$ tổng chi phí' % (p1)
    vd_da_1_s = 'Chi phí cho Trang trí trại chiếm $%s\\%%$ tổng chi phí' % (p1 - 5)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Hạng mục Trang trí trại có góc ở tâm lớn nhất ($%s^\\circ$) và chiếm $\\frac{%s^\\circ}{360^\\circ} \\cdot 100\\%% = %s\\%%$.' % (g1, g1, p1))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tần số tương đối của hạng mục Ẩm thực lớn hơn hạng mục Âm thanh'
    vdc_da_1_s = 'Tần số tương đối của hạng mục Ẩm thực nhỏ hơn hạng mục Âm thanh'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Hạng mục Ẩm thực chiếm $\\frac{%s^\\circ}{360^\\circ} \\cdot 100\\%% = %s\\%% > %s\\%%$ (hạng mục Âm thanh).' % (g3, p3, p2))
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
