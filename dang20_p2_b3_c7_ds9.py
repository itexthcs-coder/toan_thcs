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


def bt_dang20_p2_b3_c7_ds9(self):
    n = random.choice([50, 100])
    bd_1 = (n * 50) // 100
    bd_2 = (n * 18) // 100
    duoi_180 = (n * 16) // 100
    hieu_ngay = bd_2 - duoi_180

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Mực nước ($\\text{cm}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1.5,1.12) -- (2.5,2.38) -- (3.5,2.24) -- (4.5,1.26);
\\fill (1.5,1.12) circle (1pt) node[above] {$16\\%%$};
\\fill (2.5,2.38) circle (1pt) node[above] {$34\\%%$};
\\fill (3.5,2.24) circle (1pt) node[above right] {$32\\%%$};
\\fill (4.5,1.26) circle (1pt) node[above] {$18\\%%$};
\\node[below] at (1,0) {$150$};
\\node[below] at (2,0) {$180$};
\\node[below] at (3,0) {$210$};
\\node[below] at (4,0) {$240$};
\\node[below] at (5,0) {$270$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Một trạm quan trắc thủy văn ghi nhận mực nước sông (đơn vị: $\\text{cm}$) trong $%s$ ngày mùa lũ và biểu diễn bởi biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng dưới đây:
%s
Biết mức báo động I là từ $210\\text{ cm}$ đến dưới $240\\text{ cm}$, và mức báo động II là từ $240\\text{ cm}$ trở lên.''' % (n, tikz_code))

    list_nb_da_1 = [
        '\\True Giá trị đại diện của nhóm mực nước ở mức báo động I là $225\\text{ cm}$',
        'Giá trị đại diện của nhóm mực nước ở mức báo động I là $210\\text{ cm}$'
    ]
    loigiai_nb_1 = ('''Mức báo động I ứng với nhóm $[210; 240)$ có giá trị đại diện là $\\dfrac{210 + 240}{2} = 225\\text{ (cm)}$.''')

    list_th_da_1 = [
        '\\True Trong $%s$ ngày quan trắc, có $%s$ ngày mực nước sông từ mức báo động I trở lên' % (n, bd_1),
        'Trong $%s$ ngày quan trắc, có $%s$ ngày mực nước sông từ mức báo động I trở lên' % (n, bd_1 - 5)
    ]
    loigiai_th_1 = ('''Tỉ lệ ngày mực nước từ $210\\text{ cm}$ trở lên là $32\\%% + 18\\%% = 50\\%%$, tương ứng $\\dfrac{%s \\cdot 50}{100} = %s$ (ngày).''' % (n, bd_1))

    list_vd_da_1 = [
        '\\True Số ngày mực nước ở mức báo động II nhiều hơn số ngày mực nước dưới $180\\text{ cm}$ là $%s$ ngày' % hieu_ngay,
        'Số ngày mực nước ở mức báo động II nhiều hơn số ngày mực nước dưới $180\\text{ cm}$ là $%s$ ngày' % (hieu_ngay + 2)
    ]
    loigiai_vd_1 = ('''Số ngày mức báo động II là $\\dfrac{%s \\cdot 18}{100} = %s$ ngày; dưới $180\\text{ cm}$ là $\\dfrac{%s \\cdot 16}{100} = %s$ ngày. Nhiều hơn $%s - %s = %s$ (ngày).''' % (n, bd_2, n, duoi_180, bd_2, duoi_180, hieu_ngay))

    list_vdc_da_1 = [
        '\\True Trên biểu đồ, đoạn thẳng nối điểm đại diện của nhóm $[180; 210)$ và nhóm $[210; 240)$ đi xuống từ trái sang phải',
        'Trên biểu đồ, đoạn thẳng nối điểm đại diện của nhóm $[180; 210)$ và nhóm $[210; 240)$ đi lên từ trái sang phải'
    ]
    loigiai_vdc_1 = ('''Tần số tương đối giảm từ $34\\%%$ (nhóm $[180; 210)$) xuống $32\\%%$ (nhóm $[210; 240)$) nên đoạn thẳng nối hai điểm đi xuống từ trái sang phải.''')

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
