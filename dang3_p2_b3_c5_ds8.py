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

def bt_dang3_p2_b3_c5_ds8(self):
    # Dạng 3: Phân tích độ dốc biểu đồ đoạn thẳng ghi nhận tiến độ công trình (Trục ngang chia không đều)
    rate = random.choice([15, 20, 25])
    s0 = random.choice([100, 120, 150])
    # Các mốc ngày: 1/3, 5/3 (+4 ngày), 10/3 (+5 ngày), 30/3 (+20 ngày)
    s1 = s0 + 4 * rate
    s2 = s1 + 5 * rate
    s3 = s2 + 20 * rate
    
    ds_12 = s2 - s1
    ds_23 = s3 - s2
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[below] {Ngày};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Chiều dài ($\\text{m}$)};\n' +
        '\\coordinate (P1) at (1.0,0.8);\n' +
        '\\coordinate (P2) at (2.3,1.4);\n' +
        '\\coordinate (P3) at (3.6,2.1);\n' +
        '\\coordinate (P4) at (4.9,4.0);\n' +
        '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4);\n' +
        '\\fill (P1) circle (1pt) node[above left] {$%s$};\n' % s0 +
        '\\fill (P2) circle (1pt) node[above left] {$%s$};\n' % s1 +
        '\\fill (P3) circle (1pt) node[above left] {$%s$};\n' % s2 +
        '\\fill (P4) circle (1pt) node[above] {$%s$};\n' % s3 +
        '\\node[below] at (1.0,0) {$1/3$};\n' +
        '\\node[below] at (2.3,0) {$5/3$};\n' +
        '\\node[below] at (3.6,0) {$10/3$};\n' +
        '\\node[below] at (4.9,0) {$30/3$};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Một nhà thầu theo dõi tổng số mét đường bê tông đã hoàn thành tại các mốc thời gian: Ngày $1/3$ ($%s\\text{ m}$), Ngày $5/3$ ($%s\\text{ m}$), Ngày $10/3$ ($%s\\text{ m}$) và Ngày $30/3$ ($%s\\text{ m}$). Khi vẽ biểu đồ đoạn thẳng, người vẽ đặt $4$ mốc ngày này cách đều nhau trên trục ngang:\n' % (s0, s1, s2, s3) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Trên biểu đồ vẽ như trên, đoạn thẳng nối mốc $10/3$ đến $30/3$ có độ dốc lớn nhất'
    nb_da_1_s = 'Trên biểu đồ vẽ như trên, đoạn thẳng nối mốc $1/3$ đến $5/3$ có độ dốc lớn nhất'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Vì khoảng cách ngang giữa các điểm được vẽ bằng nhau trong khi độ tăng tung độ từ $%s$ lên $%s$ (tăng $%s\\text{ m}$) lớn nhất nên đoạn thẳng cuối cùng dốc đứng nhất.' % (s2, s3, ds_23))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Sai)
    th_da_1_d = '\\True Tốc độ thi công trung bình mỗi ngày trong giai đoạn từ $10/3$ đến $30/3$ bằng với giai đoạn từ $5/3$ đến $10/3$ (cùng đạt $%s\\text{ m/ngày}$)' % rate
    th_da_1_s = 'Tốc độ thi công trung bình mỗi ngày trong giai đoạn từ $10/3$ đến $30/3$ nhanh gấp đôi giai đoạn từ $5/3$ đến $10/3$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Từ $5/3$ đến $10/3$ ($5$ ngày), đội làm được $\\dfrac{%s - %s}{5} = %s\\text{ m/ngày}$. Từ $10/3$ đến $30/3$ ($20$ ngày), đội làm được $\\dfrac{%s - %s}{20} = %s\\text{ m/ngày}$. Vậy tốc độ thi công không đổi.' % (s2, s1, rate, s3, s2, rate))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Nguyên nhân đoạn cuối trên biểu đồ dốc đứng lên là do khoảng cách thời gian $20$ ngày bị nén lại bằng với khoảng cách $4$ ngày và $5$ ngày trước đó'
    vd_da_1_s = 'Nguyên nhân đoạn cuối trên biểu đồ dốc đứng lên là do đội thi công đã tăng gấp đôi nhân công sau ngày $10/3$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Do trục ngang chia khoảng cách không tỉ lệ với số ngày thực tế ($4$ ngày, $5$ ngày và $20$ ngày đều vẽ bằng một đoạn ngang bằng nhau) nên độ dốc bị sai lệch.' )
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Nếu chia trục ngang đúng tỉ lệ số ngày thực tế thì bốn điểm biểu diễn trên biểu đồ sẽ nằm thẳng hàng'
    vdc_da_1_s = 'Nếu chia trục ngang đúng tỉ lệ số ngày thực tế thì đường gấp khúc sẽ bị gãy khúc mạnh hơn'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Vì tốc độ thi công đều đặn $%s\\text{ m/ngày}$ trong suốt các giai đoạn nên nếu chia trục ngang đúng tỉ lệ thời gian thì bốn điểm biểu diễn cùng nằm trên một đường thẳng.' % rate)
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
