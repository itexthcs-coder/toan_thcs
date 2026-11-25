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


def bt_dang12_p2_b2_c5_ds8(self):
    # Dạng 12 (Vận dụng - Thuần túy toán học): Tìm ẩn số x để thỏa mãn điều kiện tỉ lệ phần trăm trên biểu đồ quạt tròn
    k = random.choice([1, 2])
    x_val = 38 * k
    c_x, c_y, c_z = 10 * k, 10 * k, 20 * k
    val_x = 3 * x_val + c_x
    val_y = 5 * x_val - c_y
    val_z = 2 * x_val + c_z
    tong = val_x + val_y + val_z
    
    noidungcauhoi = ("""Cho bảng thống kê số lượng phần tử của ba nhóm $X, Y, Z$ lần lượt là $3x + %s$; $5x - %s$ và $2x + %s$ (với $x$ là số nguyên dương). Biết rằng khi biểu diễn bảng dữ liệu này bằng biểu đồ hình quạt tròn thì hình quạt biểu diễn nhóm $Y$ chiếm đúng $45\\%%$ tổng thể. Xét tính đúng sai của các khẳng định sau:"""
                     % (c_x, c_y, c_z))
    
    nb_da_1_d = '\\True Tổng số phần tử của cả ba nhóm tính theo $x$ là $10x + %s$' % (c_x - c_y + c_z)
    nb_da_1_s = 'Tổng số phần tử của cả ba nhóm tính theo $x$ là $10x + %s$' % (c_x + c_y + c_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tổng số phần tử của cả ba nhóm là: $(3x + %s) + (5x - %s) + (2x + %s) = 10x + %s$.""" % (c_x, c_y, c_z, c_x - c_y + c_z))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Phương trình tìm $x$ từ điều kiện tỉ lệ của nhóm $Y$ là $\\dfrac{5x - %s}{10x + %s} = \\dfrac{45}{100}$' % (c_y, c_x - c_y + c_z)
    th_da_1_s = 'Phương trình tìm $x$ từ điều kiện tỉ lệ của nhóm $Y$ là $\\dfrac{3x + %s}{10x + %s} = \\dfrac{45}{100}$' % (c_x, c_x - c_y + c_z)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tỉ lệ phần trăm của nhóm $Y$ trong tổng thể bằng $45\\%%$ nên ta có phương trình: $\\dfrac{5x - %s}{10x + %s} = \\dfrac{45}{100}$.""" % (c_y, c_x - c_y + c_z))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Giải phương trình trên ta tìm được $x = %s$' % x_val
    vd_da_1_s = 'Giải phương trình trên ta tìm được $x = %s$' % (x_val + 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Từ $\\dfrac{5x - %s}{10x + %s} = \\dfrac{9}{20} \\Rightarrow 20(5x - %s) = 9(10x + %s) \\Leftrightarrow 100x - %s = 90x + %s \\Leftrightarrow 10x = %s \\Leftrightarrow x = %s$."""
                    % (c_y, c_x - c_y + c_z, c_y, c_x - c_y + c_z, 20*c_y, 9*(c_x - c_y + c_z), 10*x_val, x_val))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Khi đó tỉ lệ phần trăm của nhóm $X$ bằng $35\\%%$'
    vdc_da_1_d = 'Khi đó tỉ lệ phần trăm của nhóm $X$ bằng $31\\%%$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Với $x = %s$, nhóm $X$ có $3 \\cdot %s + %s = %s$ phần tử, tổng thể có $10 \\cdot %s + %s = %s$ phần tử. Tỉ lệ nhóm $X$ là $\\dfrac{%s}{%s} \\cdot 100\\%% = 31\\%%$ (không phải $35\\%%$)."""
                     % (x_val, x_val, c_x, val_x, x_val, c_x - c_y + c_z, tong, val_x, tong))
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
