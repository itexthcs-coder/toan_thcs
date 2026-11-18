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


def bt_dang5_p2_b3_c7_ds9(self):
    n = random.choice([60, 80])
    m3 = (n * 40) // 100

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Tốc độ ($\\text{km/h}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1,0.7) -- (2,1.75) -- (3,2.8) -- (4,1.4) -- (5,0.35);
\\fill (1,0.7) circle (1pt) node[above] {$10\\%%$};
\\fill (2,1.75) circle (1pt) node[above] {$25\\%%$};
\\fill (3,2.8) circle (1pt) node[above] {$40\\%%$};
\\fill (4,1.4) circle (1pt) node[above right] {$20\\%%$};
\\fill (5,0.35) circle (1pt) node[above] {$5\\%%$};
\\node[below] at (1,0) {$9$};
\\node[below] at (2,0) {$11$};
\\node[below] at (3,0) {$13$};
\\node[below] at (4,0) {$15$};
\\node[below] at (5,0) {$17$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng dưới đây thống kê tốc độ chạy trung bình (đơn vị: $\\text{km/h}$) của $%s$ vận động viên phong trào (trục ngang ghi giá trị đại diện của các nhóm có độ dài bằng nhau):
%s''' % (n, tikz_code))

    list_nb_da_1 = [
        '\\True Độ dài của mỗi nhóm tốc độ là $2\\text{ km/h}$',
        'Độ dài của mỗi nhóm tốc độ là $4\\text{ km/h}$'
    ]
    loigiai_nb_1 = ('''Độ dài của mỗi nhóm bằng khoảng cách giữa hai giá trị đại diện liên tiếp: $11 - 9 = 2\\text{ (km/h)}$.''')

    list_th_da_1 = [
        '\\True Điểm có hoành độ $13$ biểu diễn cho nhóm tốc độ $[12; 14)$',
        'Điểm có hoành độ $13$ biểu diễn cho nhóm tốc độ $[11; 15)$'
    ]
    loigiai_th_1 = ('''Vì nhóm có độ dài bằng $2$ và nhận $13$ làm trung điểm nên nhóm đó là $[12; 14)$.''')

    list_vd_da_1 = [
        '\\True Có $%s$ vận động viên đạt tốc độ trung bình từ $12\\text{ km/h}$ đến dưới $14\\text{ km/h}$' % m3,
        'Có $%s$ vận động viên đạt tốc độ trung bình từ $12\\text{ km/h}$ đến dưới $14\\text{ km/h}$' % (m3 + 6)
    ]
    loigiai_vd_1 = ('''Nhóm $[12; 14)$ có tần số tương đối là $40\\%%$ nên số vận động viên thuộc nhóm này là $\\dfrac{%s \\cdot 40}{100} = %s$ (người).''' % (n, m3))

    list_vdc_da_1 = [
        '\\True Số vận động viên chạy với tốc độ dưới $12\\text{ km/h}$ nhiều hơn số vận động viên chạy từ $14\\text{ km/h}$ trở lên',
        'Số vận động viên chạy với tốc độ dưới $12\\text{ km/h}$ ít hơn số vận động viên chạy từ $14\\text{ km/h}$ trở lên'
    ]
    loigiai_vdc_1 = ('''Tỉ lệ vận động viên chạy dưới $12\\text{ km/h}$ là $10\\%% + 25\\%% = 35\\%%$, lớn hơn tỉ lệ chạy từ $14\\text{ km/h}$ trở lên ($20\\%% + 5\\%% = 25\\%%$).''')

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
