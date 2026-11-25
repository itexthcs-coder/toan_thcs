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

def bt_dang5_p2_b3_c5_ds8(self):
    # Dạng 5: Đối chiếu hai biểu đồ đoạn thẳng biểu diễn cùng dãy dữ liệu khi thay đổi tỉ lệ trục đứng
    base = random.choice([40, 50, 60])
    v = [base + 2, base + 5, base + 3, base + 6, base + 8]
    y_max1 = base + 10
    y_max2 = base + 60
    
    ys1 = [round((x - base) * 0.3, 2) for x in v]
    ys2 = [round(x * 3.0 / y_max2, 2) for x in v]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (4.5,0) node[below] {Tuần};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Tấn};\n' +
        '\\node[left] at (0,0) {$%s$};\n' % base +
        '\\node[left] at (0,3) {$%s$};\n' % y_max1 +
        '\\coordinate (A1) at (0.7,%s);\n' % ys1[0] +
        '\\coordinate (A2) at (1.5,%s);\n' % ys1[1] +
        '\\coordinate (A3) at (2.3,%s);\n' % ys1[2] +
        '\\coordinate (A4) at (3.1,%s);\n' % ys1[3] +
        '\\coordinate (A5) at (3.9,%s);\n' % ys1[4] +
        '\\draw[line width=1pt] (A1)--(A2)--(A3)--(A4)--(A5);\n' +
        '\\fill (A1) circle (1pt) (A2) circle (1pt) (A3) circle (1pt) (A4) circle (1pt) (A5) circle (1pt);\n' +
        '\\node[below] at (2.2,-0.4) {Hình $1$};\n' +
        '\\begin{scope}[xshift=6.2cm]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (4.5,0) node[below] {Tuần};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Tấn};\n' +
        '\\node[left] at (0,0) {$0$};\n' +
        '\\node[left] at (0,3) {$%s$};\n' % y_max2 +
        '\\coordinate (B1) at (0.7,%s);\n' % ys2[0] +
        '\\coordinate (B2) at (1.5,%s);\n' % ys2[1] +
        '\\coordinate (B3) at (2.3,%s);\n' % ys2[2] +
        '\\coordinate (B4) at (3.1,%s);\n' % ys2[3] +
        '\\coordinate (B5) at (3.9,%s);\n' % ys2[4] +
        '\\draw[line width=1pt] (B1)--(B2)--(B3)--(B4)--(B5);\n' +
        '\\fill (B1) circle (1pt) (B2) circle (1pt) (B3) circle (1pt) (B4) circle (1pt) (B5) circle (1pt);\n' +
        '\\node[below] at (2.2,-0.4) {Hình $2$};\n' +
        '\\end{scope}\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Hai biểu đồ đoạn thẳng (Hình $1$ và Hình $2$) cùng biểu diễn lượng hàng tồn kho (tấn) của một kho vận trong $5$ tuần liên tiếp lần lượt là $%s; %s; %s; %s; %s$. Trong Hình $1$, trục đứng chia từ $%s$ đến $%s$; trong Hình $2$, trục đứng chia từ $0$ đến $%s$:\n' % (v[0], v[1], v[2], v[3], v[4], base, y_max1, y_max2) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Bảng thống kê số liệu lập được từ Hình $1$ và Hình $2$ là hoàn toàn giống nhau'
    nb_da_1_s = 'Bảng thống kê lập được từ Hình $1$ có các giá trị lớn hơn Hình $2$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Cả hai biểu đồ đều biểu diễn cùng một dãy số liệu ($%s; %s; %s; %s; %s$ tấn) nên bảng thống kê thu được là hoàn toàn như nhau.' % (v[0], v[1], v[2], v[3], v[4]))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Đường gấp khúc ở Hình $1$ có độ biến thiên (độ dốc lên xuống) rõ rệt hơn nhiều so với Hình $2$'
    th_da_1_s = 'Đường gấp khúc ở Hình $1$ và Hình $2$ có độ dốc hoàn toàn bằng nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Do khoảng chia trên trục đứng của Hình $1$ được phóng to (từ $%s$ đến $%s$) nên sự lên xuống giữa các điểm trên Hình $1$ dốc hơn hẳn so với Hình $2$.' % (base, y_max1))
    list_th_2 = [loigiai_th_1]
    
    # c (Sai)
    vd_da_1_d = '\\True Lượng hàng tồn kho ở Tuần $5$ trong cả hai biểu đồ đều bằng nhau và cùng bằng $%s$ tấn' % v[4]
    vd_da_1_s = 'Lượng hàng tồn kho thực tế ở Tuần $5$ trong Hình $1$ tăng mạnh hơn so với Tuần $5$ trong Hình $2$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Sự thay đổi tỉ lệ trục đứng chỉ làm thay đổi hình dạng trực quan của đường gấp khúc chứ không làm thay đổi giá trị thực tế của dữ liệu ($%s$ tấn).' % v[4])
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Việc kéo giãn khoảng chia trên trục đứng giúp quan sát chi tiết các biến động nhỏ, nhưng dễ làm phóng đại mức độ biến động'
    vdc_da_1_s = 'Việc kéo giãn khoảng chia trên trục đứng luôn làm sai lệch giá trị số liệu gốc của bảng thống kê'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Kéo giãn trục đứng là kĩ thuật thường dùng để soi rõ các dao động nhỏ của dữ liệu nhưng người đọc cần lưu ý thang đo trên trục đứng để tránh ngộ nhận mức biến động.' )
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
