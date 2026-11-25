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

def bt_dang16_p2_b3_c5_ds8(self):
    # Dạng 16: Phân tích bài toán mật độ che phủ rừng và diện tích đất tự nhiên (Liên môn Địa lí)
    area_a = 6400
    area_b = 9200
    pa20, pa24 = Decimal('42.5'), Decimal('45.0')
    pb20, pb24 = Decimal('54.0'), Decimal('51.5')
    
    for_a24 = int(Decimal(area_a) * pa24 / Decimal(100)) # 2880
    for_a_inc = int(Decimal(area_a) * (pa24 - pa20) / Decimal(100)) # 160
    for_b24 = int(Decimal(area_b) * pb24 / Decimal(100)) # 4738
    diff_ba = for_b24 - for_a24 # 1858
    
    def fmt_int(n):
        return f"{n:,}".replace(",", "\\,")
        
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (4.6,0) node[below] {Năm};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Tỉ lệ ($\\%%$)};\n' +
        '\\node[left] at (0,0) {$40$};\n' +
        '\\node[left] at (0,3.5) {$56$};\n' +
        '\\coordinate (A1) at (1.2,0.55);\n' +
        '\\coordinate (A2) at (3.4,1.1);\n' +
        '\\draw[line width=1pt] (A1)--(A2);\n' +
        '\\fill (A1) circle (1pt) node[below] {$42,5$};\n' +
        '\\fill (A2) circle (1pt) node[above] {$45,0$};\n' +
        '\\coordinate (B1) at (1.2,3.05);\n' +
        '\\coordinate (B2) at (3.4,2.5);\n' +
        '\\draw[line width=1pt, dashed] (B1)--(B2);\n' +
        '\\fill (B1) circle (1pt) node[above] {$54,0$};\n' +
        '\\fill (B2) circle (1pt) node[below] {$51,5$};\n' +
        '\\node[below] at (1.2,0) {$2020$};\n' +
        '\\node[below] at (3.4,0) {$2024$};\n' +
        '\\draw[line width=1pt] (4.8,2.8) -- (5.5,2.8) node[right] {Tỉnh $A$};\n' +
        '\\draw[line width=1pt, dashed] (4.8,2.1) -- (5.5,2.1) node[right] {Tỉnh $B$};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Quan sát biểu đồ đoạn thẳng dưới đây biểu diễn tỉ lệ diện tích đất có rừng trên tổng diện tích đất tự nhiên của tỉnh $A$ (tổng diện tích $%s\\text{ km}^2$) và tỉnh $B$ (tổng diện tích $%s\\text{ km}^2$):\n' % (fmt_int(area_a), fmt_int(area_b)) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Từ năm $2020$ đến năm $2024$, tỉ lệ che phủ rừng của tỉnh $A$ tăng lên trong khi của tỉnh $B$ giảm xuống'
    nb_da_1_s = 'Từ năm $2020$ đến năm $2024$, tỉ lệ che phủ rừng của cả hai tỉnh $A$ và $B$ đều tăng lên'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Đường biểu diễn của tỉnh $A$ đi lên từ $42,5\\%%$ lên $45,0\\%%$, còn của tỉnh $B$ đi xuống từ $54,0\\%%$ xuống $51,5\\%%$.' )
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Diện tích đất có rừng của tỉnh $A$ năm $2024$ là $%s\\text{ km}^2$' % fmt_int(for_a24)
    th_da_1_s = 'Diện tích đất có rừng của tỉnh $A$ năm $2024$ là $%s\\text{ km}^2$' % fmt_int(for_a24 - 160)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Diện tích đất có rừng của tỉnh $A$ năm $2024$ là $%s \\cdot 45,0\\%% = %s\\text{ (km}^2\\text{)}$.' % (fmt_int(area_a), fmt_int(for_a24)))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Trong giai đoạn $2020 - 2024$, tỉnh $A$ đã trồng mới và phục hồi thêm được $%s\\text{ km}^2$ rừng' % fmt_int(for_a_inc)
    vd_da_1_s = 'Trong giai đoạn $2020 - 2024$, tỉnh $A$ đã trồng mới và phục hồi thêm được $250\\text{ km}^2$ rừng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tỉ lệ che phủ rừng tỉnh $A$ tăng $45,0\\%% - 42,5\\%% = 2,5\\%%$, tương ứng diện tích rừng tăng thêm $%s \\cdot 2,5\\%% = %s\\text{ (km}^2\\text{)}$.' % (fmt_int(area_a), fmt_int(for_a_inc)))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Năm $2024$, diện tích đất có rừng của tỉnh $B$ nhiều hơn tỉnh $A$ là $%s\\text{ km}^2$' % fmt_int(diff_ba)
    vdc_da_1_s = 'Năm $2024$, diện tích đất có rừng của tỉnh $B$ nhiều hơn tỉnh $A$ là $1\\,800\\text{ km}^2$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Diện tích rừng tỉnh $B$ năm $2024$ là $%s \\cdot 51,5\\%% = %s\\text{ km}^2$. Chênh lệch diện tích rừng giữa tỉnh $B$ và tỉnh $A$ là $%s - %s = %s\\text{ (km}^2\\text{)}$.' % (fmt_int(area_b), fmt_int(for_b24), fmt_int(for_b24), fmt_int(for_a24), fmt_int(diff_ba)))
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
