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

def bt_dang20_p2_b3_c5_ds8(self):
    # Dạng 20: Bài toán liên môn Vật lí - Giao thông: Tính vận tốc trung bình từ biểu đồ đoạn thẳng quãng đường - thời gian
    v1 = random.choice([48, 50, 52])
    s1 = int(Decimal(v1) * Decimal('1.5')) # 72, 75, 78
    v2 = random.choice([58, 60, 62])
    s2 = s1 + 2 * v2 # 192, 195, 198
    
    v_tb_dec = (Decimal(s2) / Decimal(4)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    v_tb_str = str(v_tb_dec).rstrip('0').rstrip('.').replace('.', ',')
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Thời điểm};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Quãng đường ($\\text{km}$)};\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\coordinate (P0) at (0.8,0);\n' +
        '\\coordinate (P1) at (2.4,1.5);\n' +
        '\\coordinate (P2) at (3.2,1.5);\n' +
        '\\coordinate (P3) at (5.4,3.8);\n' +
        '\\draw[line width=1pt] (P0)--(P1)--(P2)--(P3);\n' +
        '\\fill (P0) circle (1pt) (P1) circle (1pt) (P2) circle (1pt) (P3) circle (1pt);\n' +
        '\\node[above left] at (P1) {$%s$};\n' % s1 +
        '\\node[above right] at (P2) {$%s$};\n' % s1 +
        '\\node[above] at (P3) {$%s$};\n' % s2 +
        '\\node[below] at (0.8,0) {$7\\text{h}00$};\n' +
        '\\node[below] at (2.4,0) {$8\\text{h}30$};\n' +
        '\\node[below] at (3.2,0) {$9\\text{h}00$};\n' +
        '\\node[below] at (5.4,0) {$11\\text{h}00$};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây mô tả hành trình của một xe khách đi từ bến xe $A$ đến bến xe $B$: xuất phát lúc $7\\text{h}00$ ($0\\text{ km}$), lúc $8\\text{h}30$ đi được $%s\\text{ km}$, dừng nghỉ đến $9\\text{h}00$ ($%s\\text{ km}$), và đến bến $B$ lúc $11\\text{h}00$ ($%s\\text{ km}$):\n' % (s1, s1, s2) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Đoạn thẳng trên biểu đồ ứng với khoảng thời gian từ $8\\text{h}30$ đến $9\\text{h}00$ nằm ngang song song với trục thời gian'
    nb_da_1_s = 'Đoạn thẳng trên biểu đồ ứng với khoảng thời gian từ $8\\text{h}30$ đến $9\\text{h}00$ đi xuống về phía trục ngang'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Trong khoảng thời gian từ $8\\text{h}30$ đến $9\\text{h}00$, xe dừng nghỉ nên quãng đường không đổi ($%s\\text{ km}$), do đó đoạn thẳng nối hai điểm nằm ngang song song với trục thời gian.' % s1)
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Vận tốc trung bình của xe trong $1,5$ giờ đầu tiên (từ $7\\text{h}00$ đến $8\\text{h}30$) là $%s\\text{ km/h}$' % v1
    th_da_1_s = 'Vận tốc trung bình của xe trong $1,5$ giờ đầu tiên (từ $7\\text{h}00$ đến $8\\text{h}30$) là $45\\text{ km/h}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Từ $7\\text{h}00$ đến $8\\text{h}30$ hết $1,5$ giờ, xe đi được $%s\\text{ km}$ nên vận tốc trung bình là $\\dfrac{%s}{1,5} = %s\\text{ (km/h)}$.' % (s1, s1, v1))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Trong chặng cuối (từ $9\\text{h}00$ đến $11\\text{h}00$), xe chạy nhanh hơn so với chặng đầu tiên (đạt $%s\\text{ km/h}$)' % v2
    vd_da_1_s = 'Trong chặng cuối (từ $9\\text{h}00$ đến $11\\text{h}00$), xe chạy chậm hơn so với chặng đầu tiên'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Trong $2$ giờ cuối (từ $9\\text{h}00$ đến $11\\text{h}00$), xe đi được $%s - %s = %s\\text{ km}$, vận tốc đạt $\\dfrac{%s}{2} = %s\\text{ km/h} > %s\\text{ km/h}$.' % (s2, s1, s2 - s1, s2 - s1, v2, v1))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Tính trên toàn bộ hành trình từ $7\\text{h}00$ đến $11\\text{h}00$ (kể cả thời gian nghỉ), vận tốc trung bình của xe khách là $%s\\text{ km/h}$' % v_tb_str
    vdc_da_1_s = 'Tính trên toàn bộ hành trình từ $7\\text{h}00$ đến $11\\text{h}00$ (kể cả thời gian nghỉ), vận tốc trung bình của xe khách là $55\\text{ km/h}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng thời gian từ $7\\text{h}00$ đến $11\\text{h}00$ là $4$ giờ và tổng quãng đường là $%s\\text{ km}$ nên vận tốc trung bình toàn hành trình là $\\dfrac{%s}{4} = %s\\text{ (km/h)}$.' % (s2, s2, v_tb_str))
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
