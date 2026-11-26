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
def bt_dang20_p2_b3_c6_ds8(self):
    # Dạng 20: Thực tế thời gian hoàn thành công việc của hai vòi nước
    # Bể V m^3, vòi 1 chảy x m^3/h, vòi 2 chảy x + d m^3/h
    # Hiệu thời gian = V/x - V/(x + d) = V*d / (x*(x + d))
    bo = [
        (30, 2, 3, 4),
        (40, 2, 4, 3),
        (60, 3, 3, 10),
        (24, 2, 4, 2)
    ]
    dung_tich, chenh_lech, x_val, hieu_tg = random.choice(bo)
    tu_hieu = dung_tich * chenh_lech
    
    noidungcauhoi = ('Một bể nước có dung tích $%s\\text{ m}^3$. Vòi thứ nhất chảy vào bể mỗi giờ được $x\\text{ (m}^3\\text{)}$ ($x > 0$), vòi thứ hai chảy vào bể mỗi giờ nhiều hơn vòi thứ nhất $%s\\text{ m}^3$. Xét tính đúng, sai của các khẳng định sau:' % (dung_tich, chenh_lech))
    
    list_nb_da_1 = [
        '\\True Thời gian để vòi thứ nhất chảy đầy bể một mình là $\\dfrac{%s}{x}$ (giờ)' % dung_tich,
        'Thời gian để vòi thứ nhất chảy đầy bể một mình là $\\dfrac{x}{%s}$ (giờ)' % dung_tich
    ]
    loigiai_nb_1 = ('Vòi thứ nhất chảy đầy bể $%s\\text{ m}^3$ với lưu lượng $x\\text{ m}^3\\text{/giờ}$ mất $\\dfrac{%s}{x}$ (giờ).' % (dung_tich, dung_tich))
    
    list_th_da_1 = [
        '\\True Thời gian để vòi thứ hai chảy đầy bể một mình là $\\dfrac{%s}{x + %s}$ (giờ)' % (dung_tich, chenh_lech),
        'Thời gian để vòi thứ hai chảy đầy bể một mình là $\\dfrac{%s}{x - %s}$ (giờ)' % (dung_tich, chenh_lech)
    ]
    loigiai_th_1 = ('Mỗi giờ vòi thứ hai chảy được $x + %s\\text{ (m}^3\\text{)}$ nên thời gian chảy đầy bể là $\\dfrac{%s}{x + %s}$ (giờ).' % (chenh_lech, dung_tich, chenh_lech))
    
    list_vd_da_1 = [
        '\\True Hiệu thời gian chảy đầy bể của vòi thứ nhất và vòi thứ hai là $\\dfrac{%s}{x(x + %s)}$ (giờ)' % (tu_hieu, chenh_lech),
        'Hiệu thời gian chảy đầy bể của vòi thứ nhất và vòi thứ hai là $\\dfrac{%s}{x(x + %s)}$ (giờ)' % (dung_tich, chenh_lech)
    ]
    loigiai_vd_1 = ('Hiệu thời gian chảy đầy bể của vòi thứ nhất và vòi thứ hai là $\\dfrac{%s}{x} - \\dfrac{%s}{x + %s} = \\dfrac{%s(x + %s) - %sx}{x(x + %s)} = \\dfrac{%s}{x(x + %s)}$ (giờ).' % (dung_tich, dung_tich, chenh_lech, dung_tich, chenh_lech, dung_tich, chenh_lech, tu_hieu, chenh_lech))
    
    list_vdc_da_1 = [
        '\\True Nếu $x = %s\\text{ (m}^3\\text{/giờ)}$ thì vòi thứ hai chảy đầy bể nhanh hơn vòi thứ nhất $%s$ giờ' % (x_val, hieu_tg),
        'Nếu $x = %s\\text{ (m}^3\\text{/giờ)}$ thì vòi thứ hai chảy đầy bể nhanh hơn vòi thứ nhất $%s$ giờ' % (x_val, hieu_tg + 1)
    ]
    loigiai_vdc_1 = ('Thay $x = %s$ vào biểu thức hiệu thời gian: $\\dfrac{%s}{%s \\cdot (%s + %s)} = \\dfrac{%s}{%s} = %s$ (giờ).' % (x_val, tu_hieu, x_val, x_val, chenh_lech, tu_hieu, x_val * (x_val + chenh_lech), hieu_tg))
    
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
