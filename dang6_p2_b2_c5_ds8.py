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


def bt_dang6_p2_b2_c5_ds8(self):
    # Dạng 6 (Vận dụng - Thuần túy toán học): Bài toán ngược từ biểu đồ hình quạt tròn tìm giá trị tổng thể và bộ phận
    p_a, p_b, p_c, p_d = 28, 32, 25, 15
    k = random.choice([4, 5, 6, 8])
    val_d = p_d * k
    tong = 100 * k
    val_a = p_a * k
    val_b = p_b * k
    val_c = p_c * k
    diff_ba = val_b - val_a
    sum_ac = val_a + val_c
    
    ang1 = p_a * 3.6
    ang2 = ang1 + p_b * 3.6
    ang3 = ang2 + p_c * 3.6
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) circle (1.6);
    \\draw[line width=1pt] (0,0) -- (0:1.6);
    \\draw[line width=1pt] (0,0) -- (%.1f:1.6);
    \\draw[line width=1pt] (0,0) -- (%.1f:1.6);
    \\draw[line width=1pt] (0,0) -- (%.1f:1.6);
    \\node at (50.4:0.95) {$28\\%%$};
    \\node at (158.4:0.95) {$32\\%%$};
    \\node at (261.0:0.95) {$25\\%%$};
    \\node at (333.0:1.05) {$D$};
    \\node[right] at (2.0, 0.9) {Thành phần $A$: $28\\%%$};
    \\node[right] at (2.0, 0.3) {Thành phần $B$: $32\\%%$};
    \\node[right] at (2.0, -0.3) {Thành phần $C$: $25\\%%$};
    \\node[right] at (2.0, -0.9) {Thành phần $D$: còn lại};
    \\end{tikzpicture}
    \\end{center}""" % (ang1, ang2, ang3))
    
    noidungcauhoi = ("""Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu bốn thành phần $A, B, C, D$ của một đại lượng tổng thể $M$:%sBiết giá trị thực tế của thành phần $D$ là $%s$ đơn vị. Xét tính đúng sai của các khẳng định sau:"""
                     % (tikz_code, val_d))
    
    nb_da_1_d = '\\True Tỉ lệ phần trăm của thành phần $D$ trong tổng thể là $15\\%%$'
    nb_da_1_s = 'Tỉ lệ phần trăm của thành phần $D$ trong tổng thể là $20\\%%$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tỉ lệ phần trăm của thành phần $D$ là: $100\\%% - (28\\%% + 32\\%% + 25\\%%) = 15\\%%$.""")
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Giá trị của đại lượng tổng thể $M$ bằng $%s$ đơn vị' % tong
    th_da_1_s = 'Giá trị của đại lượng tổng thể $M$ bằng $%s$ đơn vị' % (tong + 100)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Vì $15\\%%$ tổng thể $M$ ứng với $%s$ đơn vị nên giá trị của $M$ là: $M = \\dfrac{%s}{15\\%%} = %s$ (đơn vị).""" % (val_d, val_d, tong))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Giá trị thực tế của thành phần $B$ nhiều hơn thành phần $A$ là $%s$ đơn vị' % diff_ba
    vd_da_1_s = 'Giá trị thực tế của thành phần $B$ nhiều hơn thành phần $A$ là $%s$ đơn vị' % (diff_ba + 5)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Giá trị của $B$ nhiều hơn $A$ chiếm $32\\%% - 28\\%% = 4\\%%$ tổng thể, ứng với: $%s \\cdot 4\\%% = %s$ (đơn vị).""" % (tong, diff_ba))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Tổng giá trị của hai thành phần $A$ và $C$ bằng $%s$ đơn vị' % (sum_ac - 5)
    vdc_da_1_d = 'Tổng giá trị của hai thành phần $A$ và $C$ bằng $%s$ đơn vị' % sum_ac
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Tổng tỉ lệ của $A$ và $C$ là $28\\%% + 25\\%% = 53\\%%$, nên tổng giá trị của chúng bằng: $%s \\cdot 53\\%% = %s$ (đơn vị).""" % (tong, sum_ac))
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
