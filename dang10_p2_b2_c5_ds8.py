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


def bt_dang10_p2_b2_c5_ds8(self):
    # Dạng 10 (Vận dụng - Thuần túy toán học): Bài toán kết hợp biểu đồ quạt tròn và biểu đồ cột đơn
    p1, p2, p3, px = 15, 35, 30, 20
    k = random.choice([3, 4, 5, 6])
    h2 = p2 * k
    tong = 100 * k
    h1 = p1 * k
    h3 = p3 * k
    h4 = px * k
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) circle (1.5);
    \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (54:1.5) (0,0) -- (180:1.5) (0,0) -- (288:1.5);
    \\node at (27:0.9) {$15\\%%$};
    \\node at (117:0.9) {$35\\%%$};
    \\node at (234:0.9) {$30\\%%$};
    \\node at (324:0.9) {$x\\%%$};
    \\node[right] at (1.9, 0.8) {$H_1: 15\\%%$};
    \\node[right] at (1.9, 0.25) {$H_2: 35\\%%$};
    \\node[right] at (1.9, -0.3) {$H_3: 30\\%%$};
    \\node[right] at (1.9, -0.85) {$H_4: x\\%%$};
    \\end{tikzpicture}
    \\end{center}""" )
    
    noidungcauhoi = ("""Một tập dữ liệu gồm $4$ hạng mục $H_1, H_2, H_3, H_4$ được biểu diễn bằng biểu đồ hình quạt tròn dưới đây:%sKhi chuyển sang biểu đồ cột đơn, cột biểu diễn hạng mục $H_2$ có trị số là $%s$. Xét tính đúng sai của các khẳng định sau:"""
                     % (tikz_code, h2))
    
    nb_da_1_d = '\\True Giá trị của $x$ bằng $20$'
    nb_da_1_s = 'Giá trị của $x$ bằng $25$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì tổng các tỉ lệ trong biểu đồ hình quạt tròn là $100\\%%$ nên $x = 100 - (15 + 35 + 30) = 20$.""")
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Tổng giá trị của cả bốn hạng mục bằng $%s$' % tong
    th_da_1_s = 'Tổng giá trị của cả bốn hạng mục bằng $%s$' % (tong + 100)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Hạng mục $H_2$ chiếm $35\\%%$ và ứng với $%s$, do đó tổng giá trị cả bốn hạng mục là: $\\dfrac{%s}{35\\%%} = %s$.""" % (h2, h2, tong))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Trên biểu đồ cột đơn, cột biểu diễn hạng mục $H_1$ có trị số bằng $%s$' % h1
    vd_da_1_s = 'Trên biểu đồ cột đơn, cột biểu diễn hạng mục $H_1$ có trị số bằng $%s$' % (h1 + 15)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Trị số của cột $H_1$ là: $%s \\cdot 15\\%% = %s$.""" % (tong, h1))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Trên biểu đồ cột đơn, cột biểu diễn hạng mục $H_3$ cao gấp đôi cột biểu diễn hạng mục $H_4$'
    vdc_da_1_d = 'Trên biểu đồ cột đơn, cột biểu diễn hạng mục $H_3$ cao gấp $1,5$ lần cột biểu diễn hạng mục $H_4$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Trị số của $H_3$ là $%s \\cdot 30\\%% = %s$; trị số của $H_4$ là $%s \\cdot 20\\%% = %s$. Tỉ số chiều cao là $\\dfrac{%s}{%s} = \\dfrac{30}{20} = 1,5$ (không phải gấp đôi).""" % (tong, h3, tong, h4, h3, h4))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
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
