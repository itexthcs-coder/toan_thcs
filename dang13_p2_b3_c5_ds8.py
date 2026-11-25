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

def bt_dang13_p2_b3_c5_ds8(self):
    # Dạng 13: Phân tích chuyển dịch cơ cấu qua hai biểu đồ hình quạt tròn ở hai mốc thời gian khác nhau
    t15 = random.choice([40, 50])
    t25 = random.choice([80, 100])
    p_fos15, p_hyd15, p_ren15 = 78, 16, 6
    p_fos25, p_hyd25, p_ren25 = 62, 15, 23
    
    fos15 = Decimal(t15 * p_fos15) / Decimal(100)
    fos25 = Decimal(t25 * p_fos25) / Decimal(100)
    ren25 = Decimal(t25 * p_ren25) / Decimal(100)
    hyd15 = Decimal(t15 * p_hyd15) / Decimal(100)
    hyd25 = Decimal(t25 * p_hyd25) / Decimal(100)
    diff_hyd = hyd25 - hyd15
    
    def fmt_dec(d):
        return str(d).rstrip('0').rstrip('.').replace('.', ',')
        
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        # Biểu đồ 2015
        '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:280.8:1.6) -- cycle;\n' +
        '\\draw[line width=1pt, fill=black!35] (0,0) -- (280.8:1.6) arc (280.8:338.4:1.6) -- cycle;\n' +
        '\\draw[line width=1pt, fill=white] (0,0) -- (338.4:1.6) arc (338.4:360:1.6) -- cycle;\n' +
        '\\node at (140:0.9) {$78\\%%$};\n' +
        '\\node at (309:1.1) {$16\\%%$};\n' +
        '\\node at (349:1.25) {$6\\%%$};\n' +
        '\\node[below] at (0,-1.8) {Năm $2015$ ($%s$ triệu TOE)};\n' % t15 +
        # Biểu đồ 2025
        '\\begin{scope}[xshift=4.6cm]\n' +
        '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:223.2:1.6) -- cycle;\n' +
        '\\draw[line width=1pt, fill=black!35] (0,0) -- (223.2:1.6) arc (223.2:277.2:1.6) -- cycle;\n' +
        '\\draw[line width=1pt, fill=white] (0,0) -- (277.2:1.6) arc (277.2:360:1.6) -- cycle;\n' +
        '\\node at (111:0.9) {$62\\%%$};\n' +
        '\\node at (250:1.1) {$15\\%%$};\n' +
        '\\node at (318:1.05) {$23\\%%$};\n' +
        '\\node[below] at (0,-1.8) {Năm $2025$ ($%s$ triệu TOE)};\n' % t25 +
        '\\end{scope}\n' +
        # Chú thích
        '\\draw[line width=1pt, fill=black!15] (6.8,0.8) rectangle (7.2,1.1) node[right, yshift=-4pt] {Hóa thạch};\n' +
        '\\draw[line width=1pt, fill=black!35] (6.8,0.0) rectangle (7.2,0.3) node[right, yshift=-4pt] {Thủy điện};\n' +
        '\\draw[line width=1pt, fill=white] (6.8,-0.8) rectangle (7.2,-0.5) node[right, yshift=-4pt] {Tái tạo khác};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Hai biểu đồ hình quạt tròn dưới đây cho biết cơ cấu sử dụng nguồn năng lượng của một quốc gia vào năm $2015$ (tổng tiêu thụ $%s$ triệu TOE) và năm $2025$ (tổng tiêu thụ $%s$ triệu TOE):\n' % (t15, t25) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Sau $10$ năm, tỉ trọng nhiên liệu hóa thạch trong cơ cấu năng lượng giảm $16$ điểm phần trăm'
    nb_da_1_s = 'Sau $10$ năm, tỉ trọng nhiên liệu hóa thạch trong cơ cấu năng lượng giảm $20$ điểm phần trăm'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tỉ trọng nhiên liệu hóa thạch giảm từ $78\\%%$ (năm $2015$) xuống $62\\%%$ (năm $2025$), tức giảm $78\\%% - 62\\%% = 16$ điểm phần trăm.' )
    list_nb_2 = [loigiai_nb_1]
    
    # b (Sai)
    th_da_1_d = '\\True Lượng nhiên liệu hóa thạch tiêu thụ thực tế năm $2025$ tăng lên so với năm $2015$ (từ $%s$ lên $%s$ triệu TOE)' % (fmt_dec(fos15), fmt_dec(fos25))
    th_da_1_s = 'Lượng nhiên liệu hóa thạch tiêu thụ thực tế năm $2025$ giảm so với năm $2015$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Năm $2015$ tiêu thụ $%s \\cdot 78\\%% = %s$ triệu TOE; năm $2025$ tiêu thụ $%s \\cdot 62\\%% = %s$ triệu TOE. Dù tỉ trọng giảm nhưng tổng quy mô tăng nên lượng tiêu thụ thực tế vẫn tăng.' % (t15, fmt_dec(fos15), t25, fmt_dec(fos25)))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Sản lượng năng lượng tái tạo khác năm $2025$ đạt $%s$ triệu TOE' % fmt_dec(ren25)
    vd_da_1_s = 'Sản lượng năng lượng tái tạo khác năm $2025$ đạt $%s$ triệu TOE' % fmt_dec(ren25 + Decimal(2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Sản lượng năng lượng tái tạo khác năm $2025$ là $%s \\cdot 23\\%% = %s$ (triệu TOE).' % (t25, fmt_dec(ren25)))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Sản lượng thủy điện năm $2025$ tăng thêm $%s$ triệu TOE so với năm $2015$' % fmt_dec(diff_hyd)
    vdc_da_1_s = 'Sản lượng thủy điện năm $2025$ giảm đi $1$ triệu TOE so với năm $2015$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Sản lượng thủy điện năm $2015$ là $%s \\cdot 16\\%% = %s$ triệu TOE; năm $2025$ là $%s \\cdot 15\\%% = %s$ triệu TOE. Mức tăng thêm là $%s - %s = %s$ (triệu TOE).' % (t15, fmt_dec(hyd15), t25, fmt_dec(hyd25), fmt_dec(hyd25), fmt_dec(hyd15), fmt_dec(diff_hyd)))
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
