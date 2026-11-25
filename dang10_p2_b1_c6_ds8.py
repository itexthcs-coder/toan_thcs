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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang10_p2_b1_c6_ds8(self):
    # Dạng 10: Tìm điều kiện xác định của phân thức chứa hai biến x, y
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([2, 3, 5])
        x0 = random.choice([3, 4, 5])
        y0 = random.choice([1, 2])
        
        tu_val = a * x0 + b * y0
        mau_val = x0**2 - y0**2
        g = math.gcd(tu_val, mau_val)
        tu_rg = tu_val // g
        mau_rg = mau_val // g
        str_val = str(tu_rg) if mau_rg == 1 else '\\dfrac{%s}{%s}' % (tu_rg, mau_rg)
        
        noidungcauhoi = ('Cho phân thức hai biến $F = \\dfrac{%sx + %sy}{x^2 - y^2}$. Xét tính đúng sai của các khẳng định sau:'
                         % (a, b))
        
        nb_da_1_d = '\\True Điều kiện xác định của phân thức $F$ là $x^2 - y^2 \\neq 0$'
        nb_da_1_s = 'Điều kiện xác định của phân thức $F$ là $%sx + %sy \\neq 0$' % (a, b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Điều kiện xác định của phân thức là điều kiện của các biến để mẫu thức khác $0$, tức là $x^2 - y^2 \\neq 0$.'
        loigiai_nb_s = 'Sai. Điều kiện xác định đặt cho mẫu thức $x^2 - y^2 \\neq 0$, không đặt cho tử thức.'
        
        th_da_1_d = '\\True Phân thức $F$ xác định khi và chỉ khi $x \\neq y$ và $x \\neq -y$'
        th_da_1_s = 'Phân thức $F$ xác định khi và chỉ khi $x \\neq y$ hoặc $x \\neq -y$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Ta có $x^2 - y^2 = (x - y)(x + y) \\neq 0$ khi đồng thời cả hai thừa số khác $0$, tức là $x \\neq y$ và $x \\neq -y$.'
        loigiai_th_s = 'Sai. Tích $(x - y)(x + y) \\neq 0$ đòi hỏi cả hai nhân tử đều phải khác $0$, nên phải dùng từ "và" chứ không phải "hoặc".'
        
        vd_da_1_d = '\\True Tại cặp giá trị $x = %s, y = -%s$, phân thức $F$ không xác định' % (x0, x0)
        vd_da_1_s = 'Tại cặp giá trị $x = %s, y = -%s$, phân thức $F$ xác định và bằng $0$' % (x0, x0)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Khi $x = %s, y = -%s$, mẫu thức bằng $(%s)^2 - (-%s)^2 = 0$ nên phân thức không xác định.' % (x0, x0, x0, x0)
        loigiai_vd_s = 'Sai. Khi $x = %s, y = -%s$ thì $x = -y$, làm cho mẫu thức bằng $0$ nên phân thức không xác định.' % (x0, x0)
        
        vdc_da_1_d = '\\True Tại cặp giá trị $x = %s, y = %s$, phân thức $F$ xác định và có giá trị bằng $%s$' % (x0, y0, str_val)
        vdc_da_1_s = 'Tại cặp giá trị $x = %s, y = %s$, phân thức $F$ có giá trị bằng $%s$' % (x0, y0, tu_val)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Thay $x = %s, y = %s$ vào $F$, ta được $\\dfrac{%s \\cdot %s + %s \\cdot %s}{%s^2 - %s^2} = \\dfrac{%s}{%s} = %s$.' % (x0, y0, a, x0, b, y0, x0, y0, tu_val, mau_val, str_val)
        loigiai_vdc_s = 'Sai. Thay $x = %s, y = %s$ vào $F$ ta được giá trị là $\\dfrac{%s}{%s} = %s$.' % (x0, y0, tu_val, mau_val, str_val)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
