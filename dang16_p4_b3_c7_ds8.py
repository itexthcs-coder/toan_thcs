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

def bt_dang16_p4_b3_c7_ds8(self):
    # Dạng 16 (Thực tế): Hàm số biểu diễn cước phí taxi công nghệ theo quãng đường di chuyển
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p0 = random.choice([10, 12, 14]) # nghìn đồng cho 1 km đầu
        p1 = random.choice([14, 15, 16]) # nghìn đồng cho mỗi km tiếp theo (1 < x <= 10)
        # y = p0 + p1*(x - 1) = p1*x + (p0 - p1)
        diff_p = p0 - p1 # âm vì p0 < p1
        abs_diff = abs(diff_p)
        x_trip = random.choice([6, 7, 8])
        y_trip = p0 + p1 * (x_trip - 1)
        x_paid = random.choice([9, 10])
        y_paid = p0 + p1 * (x_paid - 1)

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (9.5,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (9.5,0.8);\n'
            '\\draw[line width=1pt] (4.75,0) -- (4.75,1.6);\n'
            '\\node at (2.375,1.2) {Quãng đường $x$ ($\\text{km}$)};\n'
            '\\node at (2.375,0.4) {$0 < x \\le 1$};\n'
            '\\node at (7.125,1.2) {Giá cước (nghìn đồng)};\n'
            '\\node at (7.125,0.4) {$%s$ (giá mở cửa)};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (p0)

        noidungcauhoi = (
            'Một hãng taxi công nghệ quy định giá cước đối với xe $4$ chỗ như sau: Giá mở cửa cho $1\\text{ km}$ đầu tiên là $%s$ nghìn đồng; từ kilômét tiếp theo đến hết kilômét thứ $10$, giá cước là $%s$ nghìn đồng/$\\text{km}$. Gọi $y$ (nghìn đồng) là số tiền khách phải trả khi đi quãng đường $x$ ($\\text{km}$) với $1 < x \\le 10$:\\ %s'
        ) % (p0, p1, bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Với mỗi quãng đường $x$ ($1 < x \\le 10$), số tiền $y$ phải trả là duy nhất nên $y$ là một hàm số của $x$'
        nb_da_1_s = 'Số tiền $y$ không phải là hàm số của quãng đường $x$ vì giá cước thay đổi sau kilômét đầu tiên'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Ứng với mỗi giá trị của quãng đường $x$ ($1 < x \\le 10$), hành khách chỉ phải thanh toán duy nhất một số tiền $y$ nên $y$ là hàm số của $x$.'

        # Thông hiểu
        th_da_1_d = '\\True Công thức biểu thị số tiền $y$ (nghìn đồng) theo quãng đường $x$ ($1 < x \\le 10$) là $y = %sx - %s$' % (p1, abs_diff)
        th_da_1_s = 'Công thức biểu thị số tiền $y$ (nghìn đồng) theo quãng đường $x$ ($1 < x \\le 10$) là $y = %sx + %s$' % (p1, p0)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Quãng đường vượt quá $1\\text{ km}$ đầu là $(x - 1)\\text{ km}$, nên $y = %s + %s(x - 1) = %sx - %s$.' % (p0, p1, p1, abs_diff)

        # Vận dụng
        vd_da_1_d = '\\True Một hành khách đi quãng đường dài $%s\\text{ km}$ thì phải thanh toán số tiền là $%s$ nghìn đồng' % (x_trip, y_trip)
        vd_da_1_s = 'Một hành khách đi quãng đường dài $%s\\text{ km}$ thì phải thanh toán số tiền là $%s$ nghìn đồng' % (x_trip, p1 * x_trip)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Thay $x = %s$ vào công thức ta có $y = %s \\cdot %s - %s = %s$ (nghìn đồng).' % (x_trip, p1, x_trip, abs_diff, y_trip)

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu một hành khách trả hết $%s$ nghìn đồng tiền cước thì người đó đã đi quãng đường dài $%s\\text{ km}$' % (y_paid, x_paid)
        vdc_da_1_s = 'Nếu một hành khách trả hết $%s$ nghìn đồng tiền cước thì người đó đã đi quãng đường dài $%s\\text{ km}$' % (y_paid, x_paid - 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Giải phương trình $%sx - %s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s\\text{ (km)}$ (thỏa mãn $1 < x \\le 10$).' % (p1, abs_diff, y_paid, p1, y_paid + abs_diff, x_paid)

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
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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

        content = (
            '\\begin{minipage}{\\textwidth} \n'
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
            '\\end{ex}\n \\end{minipage}\n\n'
        )
        return content
