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

def bt_dang2_p2_b3_c5_ds8(self):
    # Dạng 2: Đánh giá sự sai lệch thị giác trên biểu đồ cột quảng cáo sản phẩm (Gốc trục đứng khác 0)
    g0 = random.choice([50, 100, 150])
    d_n = random.choice([2, 3, 4])
    k = random.choice([3, 4, 5])
    val_n = g0 + d_n
    val_m = g0 + k * d_n
    diff = val_m - val_n
    
    ratio_dec = (Decimal(val_m) / Decimal(val_n)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    ratio_str = str(ratio_dec).replace('.', ',')
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Loại sản phẩm};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,%s) node[left] {Vitamin C ($\\text{mg}$)};\n' % (k + 0.8) +
        '\\node[left] at (0,0) {$%s$};\n' % g0 +
        '\\draw[line width=1pt, dashed] (0,1) -- (4.2,1);\n' +
        '\\node[left] at (0,1) {$%s$};\n' % val_n +
        '\\draw[line width=1pt, dashed] (0,%s) -- (4.2,%s);\n' % (k, k) +
        '\\node[left] at (0,%s) {$%s$};\n' % (k, val_m) +
        '\\draw[line width=1pt, fill=black!35] (0.8,0) rectangle (1.8,%s);\n' % k +
        '\\node[above] at (1.3,%s) {$%s$};\n' % (k, val_m) +
        '\\node[below] at (1.3,0) {Loại M};\n' +
        '\\draw[line width=1pt, fill=black!15] (2.6,0) rectangle (3.6,1);\n' +
        '\\node[above] at (3.1,1) {$%s$};\n' % val_n +
        '\\node[below] at (3.1,0) {Loại N};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Một hãng nước giải khát đưa ra biểu đồ cột so sánh lượng vitamin C (tính theo $\\text{mg}$) trong mỗi chai dung tích $500\\text{ ml}$ của hãng mình (Loại M: $%s\\text{ mg}$) và đối thủ cạnh tranh (Loại N: $%s\\text{ mg}$) với gốc của trục đứng đặt tại $%s\\text{ mg}$:\n' % (val_m, val_n, g0) +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Hai cột trên biểu đồ biểu diễn chính xác giá trị số liệu của Loại M ($%s\\text{ mg}$) và Loại N ($%s\\text{ mg}$)' % (val_m, val_n)
    nb_da_1_s = 'Hai cột trên biểu đồ đã ghi sai giá trị số liệu thực tế của Loại M và Loại N'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Số liệu ghi trên đỉnh hai cột lần lượt là $%s\\text{ mg}$ và $%s\\text{ mg}$, hoàn toàn khớp với số liệu thực tế của hai loại sản phẩm.' % (val_m, val_n))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Trên hình vẽ, cột của Loại M cao gấp $%s$ lần cột của Loại N' % k
    th_da_1_s = 'Trên hình vẽ, cột của Loại M cao gấp $2$ lần cột của Loại N'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Vì gốc trục đứng bắt đầu từ $%s$ nên chiều cao cột Loại M tỉ lệ với $%s - %s = %s$ và chiều cao cột Loại N tỉ lệ với $%s - %s = %s$. Do đó cột Loại M cao gấp $\\dfrac{%s}{%s} = %s$ lần cột Loại N.' % (g0, val_m, g0, k * d_n, val_n, g0, d_n, k * d_n, d_n, k))
    list_th_2 = [loigiai_th_1]
    
    # c (Sai)
    vd_da_1_d = '\\True Lượng vitamin C thực tế trong Loại M chỉ nhiều hơn Loại N là $%s\\text{ mg}$ (tỉ số xấp xỉ $%s$ lần)' % (diff, ratio_str)
    vd_da_1_s = 'Lượng vitamin C thực tế trong Loại M nhiều gấp $%s$ lần Loại N' % k
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Lượng vitamin C thực tế trong Loại M hơn Loại N là $%s - %s = %s\\text{ mg}$ và tỉ số thực tế là $\\dfrac{%s}{%s} \\approx %s \\neq %s$.' % (val_m, val_n, diff, val_m, val_n, ratio_str, k))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Việc đặt gốc trục đứng tại $%s$ dễ gây hiểu lầm về mặt thị giác rằng chất lượng Loại M vượt trội gấp nhiều lần Loại N' % g0
    vdc_da_1_s = 'Việc đặt gốc trục đứng tại $%s$ giúp phản ánh trung thực nhất tỉ lệ chênh lệch giữa hai loại sản phẩm' % g0
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Trong biểu đồ cột, khi gốc trục đứng khác $0$ thì tỉ lệ chiều cao các cột bị phóng đại so với tỉ lệ số liệu thực tế, dễ làm người xem ngộ nhận về sự chênh lệch.' )
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
