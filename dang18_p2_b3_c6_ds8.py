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
def bt_dang18_p2_b3_c6_ds8(self):
    # Dạng 18: Thực tế chuyển động có thay đổi vận tốc
    # Quãng đường 2*s km, nửa đầu s km vận tốc x, nửa sau s km vận tốc x - v
    # Tổng thời gian = s/x + s/(x - v) = s*(2x - v)/(x*(x - v))
    bo = [
        (6, 3, 3, 15, '0,45'),
        (8, 4, 2, 10, '1,3'),
        (12, 6, 3, 15, '0,9'),
        (10, 5, 5, 25, '0,45')
    ]
    tong_s, nua_s, giam_v, x_val, tg_str = random.choice(bo)
    tu_tong = '%sx - %s' % (tong_s, nua_s * giam_v)
    
    noidungcauhoi = ('Một bạn học sinh đi xe đạp từ nhà đến trường dài $%s\\text{ km}$. Nửa quãng đường đầu bạn đi với vận tốc $x\\text{ (km/h)}$ ($x > %s$). Nửa quãng đường sau, do đường đông xe nên vận tốc giảm đi $%s\\text{ km/h}$. Xét tính đúng, sai của các khẳng định sau:' % (tong_s, giam_v, giam_v))
    
    list_nb_da_1 = [
        '\\True Thời gian bạn đi nửa quãng đường đầu là $\\dfrac{%s}{x}$ (giờ)' % nua_s,
        'Thời gian bạn đi nửa quãng đường đầu là $\\dfrac{%s}{x}$ (giờ)' % tong_s
    ]
    loigiai_nb_1 = ('Nửa quãng đường đầu dài $%s\\text{ km}$ nên thời gian đi hết đoạn này là $\\dfrac{%s}{x}$ (giờ).' % (nua_s, nua_s))
    
    list_th_da_1 = [
        '\\True Thời gian bạn đi nửa quãng đường sau là $\\dfrac{%s}{x - %s}$ (giờ)' % (nua_s, giam_v),
        'Thời gian bạn đi nửa quãng đường sau là $\\dfrac{%s}{x + %s}$ (giờ)' % (nua_s, giam_v)
    ]
    loigiai_th_1 = ('Vận tốc nửa quãng đường sau là $x - %s\\text{ (km/h)}$ nên thời gian đi là $\\dfrac{%s}{x - %s}$ (giờ).' % (giam_v, nua_s, giam_v))
    
    list_vd_da_1 = [
        '\\True Tổng thời gian đi từ nhà đến trường là $\\dfrac{%s}{x(x - %s)}$ (giờ)' % (tu_tong, giam_v),
        'Tổng thời gian đi từ nhà đến trường là $\\dfrac{%s}{2x - %s}$ (giờ)' % (tong_s, giam_v)
    ]
    loigiai_vd_1 = ('Tổng thời gian đi là: $\\dfrac{%s}{x} + \\dfrac{%s}{x - %s} = \\dfrac{%s(x - %s) + %sx}{x(x - %s)} = \\dfrac{%s}{x(x - %s)}$ (giờ).' % (nua_s, nua_s, giam_v, nua_s, giam_v, nua_s, giam_v, tu_tong, giam_v))
    
    list_vdc_da_1 = [
        '\\True Nếu $x = %s\\text{ km/h}$ thì tổng thời gian đi từ nhà đến trường là $%s$ giờ' % (x_val, tg_str),
        'Nếu $x = %s\\text{ km/h}$ thì tổng thời gian đi từ nhà đến trường là $1$ giờ' % x_val
    ]
    loigiai_vdc_1 = ('Thay $x = %s$ vào biểu thức thời gian: $\\dfrac{%s}{%s} + \\dfrac{%s}{%s - %s} = %s$ (giờ).' % (x_val, nua_s, x_val, nua_s, x_val, giam_v, tg_str))
    
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
            
    combined = list(zip(answers, [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
