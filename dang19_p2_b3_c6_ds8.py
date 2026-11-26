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
def bt_dang19_p2_b3_c6_ds8(self):
    # Dạng 19: Thực tế pha chế dung dịch và nồng độ phần trăm
    # Bình chứa V1 lít nước muối nồng độ x%, đổ thêm V2 lít nước lọc
    bo = [
        (20, 5, 25, 5, 4),
        (30, 10, 40, 10, 3),
        (15, 5, 20, 20, 3),
        (40, 10, 50, 5, 2)
    ]
    v1, v2, v_tong, k_muoi, tu_nong_do = random.choice(bo)
    # Lượng muối = v1*x / 100 = x / k_muoi
    # Nồng độ mới = ((v1*x/100) / v_tong)*100% = (v1/v_tong)*x% = (tu_nong_do / 5)*x%
    g = math.gcd(v1, v_tong)
    nd_tu = v1 // g
    nd_mau = v_tong // g
    
    noidungcauhoi = ('Một bình chứa $%s$ lít nước muối có nồng độ muối là $x\\%%$ (tức là có $\\dfrac{%sx}{100}$ lít muối nguyên chất, với $x > 0$). Người ta đổ thêm $%s$ lít nước lọc (không chứa muối) vào bình. Xét tính đúng, sai của các khẳng định sau:' % (v1, v1, v2))
    
    list_nb_da_1 = [
        '\\True Lượng muối nguyên chất trong bình trước khi đổ thêm nước lọc là $\\dfrac{x}{%s}$ (lít)' % k_muoi,
        'Lượng muối nguyên chất trong bình trước khi đổ thêm nước lọc là $\\dfrac{%s}{x}$ (lít)' % k_muoi
    ]
    loigiai_nb_1 = ('Rút gọn phân thức $\\dfrac{%sx}{100}$ ta được $\\dfrac{x}{%s}$ (lít).' % (v1, k_muoi))
    
    list_th_da_1 = [
        '\\True Tổng thể tích dung dịch trong bình sau khi đổ thêm nước lọc là $%s$ (lít)' % v_tong,
        'Tổng thể tích dung dịch trong bình sau khi đổ thêm nước lọc là $%s$ (lít)' % (v1 - v2)
    ]
    loigiai_th_1 = ('Tổng thể tích dung dịch sau khi pha thêm nước lọc là $%s + %s = %s$ (lít).' % (v1, v2, v_tong))
    
    list_vd_da_1 = [
        '\\True Nồng độ phần trăm muối mới của dung dịch sau khi pha thêm nước lọc là $\\dfrac{%sx}{%s}\\%%$' % (nd_tu, nd_mau),
        'Nồng độ phần trăm muối mới của dung dịch sau khi pha thêm nước lọc là $\\dfrac{x}{%s}\\%%$' % nd_mau
    ]
    loigiai_vd_1 = ('Nồng độ phần trăm muối mới là $\\dfrac{\\frac{%sx}{100}}{%s} \\cdot 100\\%% = \\dfrac{%sx}{%s}\\%% = \\dfrac{%sx}{%s}\\%%$.' % (v1, v_tong, v1, v_tong, nd_tu, nd_mau))
    
    list_vdc_da_1 = [
        '\\True Khi đổ thêm nước lọc, nồng độ phần trăm muối giảm đi một lượng bằng $\\dfrac{%sx}{%s}\\%%$' % (nd_mau - nd_tu, nd_mau),
        'Khi đổ thêm nước lọc, nồng độ phần trăm muối không thay đổi'
    ]
    loigiai_vdc_1 = ('Độ giảm nồng độ phần trăm muối là $x\\%% - \\dfrac{%sx}{%s}\\%% = \\dfrac{%sx}{%s}\\%%$.' % (nd_tu, nd_mau, nd_mau - nd_tu, nd_mau))
    
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
