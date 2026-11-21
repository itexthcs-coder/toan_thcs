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


def bt_dang17_p2_b4_c2_ds8(self):
    r_nho = Decimal(str(random.choice([3.5, 4.5, 5.5])))
    r_lon = r_nho + Decimal('1.0')
    r_nho_str = str(r_nho).replace('.', ',')
    r_lon_str = str(r_lon).replace('.', ',')
    tong_r = int(r_lon + r_nho)
    
    tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.8);
    \\draw[line width=1pt] (O) circle (0.9);
    \\fill (O) circle (1pt) node[below left] {$O$};
    \\draw[line width=1pt, ->] (O) -- (30:1.8) node[midway, above left] {$R$};
    \\draw[line width=1pt, ->] (O) -- (-45:0.9) node[midway, below left] {$r$};
\\end{tikzpicture}
\\end{center}'''
    
    noidungcauhoi = ('''Trong một xưởng cơ khí, người ta cắt từ một tấm thép tròn có bán kính $R\\text{ (cm)}$ một lỗ tròn đồng tâm ở chính giữa có bán kính $r\\text{ (cm)}$ ($R > r > 0$) để tạo thành một vòng đệm kim loại (hình vành khuyên). Biết công thức tính diện tích hình tròn bán kính $R$ là $\\pi R^2$.''' + tikz_hinh)
    
    nb_da_1_d = '\\True Diện tích bề mặt của vòng đệm kim loại là $S = \\pi R^2 - \\pi r^2\\text{ (cm}^2\\text{)}$'
    nb_da_1_s = 'Diện tích bề mặt của vòng đệm kim loại là $S = \\pi(R - r)^2\\text{ (cm}^2\\text{)}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['''Diện tích hình vành khuyên bằng hiệu diện tích hai hình tròn đồng tâm: $S = \\pi R^2 - \\pi r^2\\text{ (cm}^2\\text{)}$.''']
    
    th_da_1_d = '\\True Phân tích biểu thức diện tích $S$ thành nhân tử ta được $S = \\pi(R - r)(R + r)\\text{ (cm}^2\\text{)}$'
    th_da_1_s = 'Phân tích biểu thức diện tích $S$ thành nhân tử ta được $S = \\pi(R^2 + r^2)\\text{ (cm}^2\\text{)}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['''Đặt nhân tử chung $\\pi$ rồi dùng hằng đẳng thức hiệu hai bình phương: $S = \\pi(R^2 - r^2) = \\pi(R - r)(R + r)$.''']
    
    vd_da_1_d = '\\True Với $R = %s\\text{ cm}$ và $r = %s\\text{ cm}$, diện tích bề mặt của vòng đệm bằng $%s\\pi\\text{ (cm}^2\\text{)}$' % (r_lon_str, r_nho_str, tong_r)
    vd_da_1_s = 'Với $R = %s\\text{ cm}$ và $r = %s\\text{ cm}$, diện tích bề mặt của vòng đệm bằng $%s\\pi\\text{ (cm}^2\\text{)}$' % (r_lon_str, r_nho_str, tong_r * 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['''Thay $R = %s$ và $r = %s$: $S = \\pi(%s - %s)(%s + %s) = \\pi \\cdot 1 \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.'''
                 % (r_lon_str, r_nho_str, r_lon_str, r_nho_str, r_lon_str, r_nho_str, tong_r, tong_r)]
    
    vdc_da_1_d = '\\True Nếu tăng đồng thời cả bán kính $R$ và bán kính $r$ thêm $1\\text{ cm}$ thì diện tích vòng đệm tăng lên'
    vdc_da_1_s = 'Nếu tăng đồng thời cả bán kính $R$ và bán kính $r$ thêm $1\\text{ cm}$ thì diện tích vòng đệm không đổi'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['''Khi tăng mỗi bán kính thêm $1\\text{ cm}$: $S_{\\text{mới}} = \\pi[(R + 1) - (r + 1)][(R + 1) + (r + 1)] = \\pi(R - r)(R + r + 2) > S$.''']

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
