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


def bt_dang15_p2_b1_c6_ds8(self):
    # Dạng 15: So sánh giá trị của phân thức bằng cách tách phần nguyên (Vận dụng)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        q = random.choice([2, 3, 4])
        p = random.choice([3, 5, 7])
        c = q + p
        x_val = p - 1
        
        noidungcauhoi = ('Cho phân thức $K = \\dfrac{%sx + %s}{x + 1}$ (với $x \\neq -1$). Xét tính đúng sai của các khẳng định sau:'
                         % (q, c))
        
        nb_da_1_d = '\\True Phân thức $K$ có thể viết dưới dạng $K = %s + \\dfrac{%s}{x + 1}$ (với $x \\neq -1$)' % (q, p)
        nb_da_1_s = 'Phân thức $K$ có thể viết dưới dạng $K = %s + \\dfrac{%s}{x + 1}$ (với $x \\neq -1$)' % (q, c)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Ta có $%s(x + 1) + %s = %sx + %s + %s = %sx + %s$, nên $\\dfrac{%sx + %s}{x + 1} = %s + \\dfrac{%s}{x + 1}$.' % (q, p, q, q, p, q, c, q, c, q, p)
        loigiai_nb_s = 'Sai. Phân tích tử thức: $%sx + %s = %s(x + 1) + %s$, do đó phần dư là $%s$ chứ không phải $%s$.' % (q, c, q, p, p, c)
        
        th_da_1_d = '\\True Khi $x > -1$, giá trị của phân thức $K$ luôn lớn hơn $%s$' % q
        th_da_1_s = 'Khi $x > -1$, giá trị của phân thức $K$ luôn nhỏ hơn $%s$' % q
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Khi $x > -1$ thì $x + 1 > 0$, suy ra $\\dfrac{%s}{x + 1} > 0$, do đó $K = %s + \\dfrac{%s}{x + 1} > %s$.' % (p, q, p, q)
        loigiai_th_s = 'Sai. Với $x > -1$ thì $\\dfrac{%s}{x + 1} > 0$ nên $K > %s$.' % (p, q)
        
        vd_da_1_d = '\\True Khi $x = %s$, giá trị của phân thức $K$ bằng $%s$' % (x_val, q + 1)
        vd_da_1_s = 'Khi $x = %s$, giá trị của phân thức $K$ bằng $%s$' % (x_val, q + p)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Thay $x = %s$ vào $K$, ta được $K = %s + \\dfrac{%s}{%s + 1} = %s + 1 = %s$.' % (x_val, q, p, x_val, q, q + 1)
        loigiai_vd_s = 'Sai. Thay $x = %s$ vào $K$ ta được $K = %s + \\dfrac{%s}{%s} = %s$.' % (x_val, q, p, p, q + 1)
        
        vdc_da_1_d = '\\True Chỉ có duy nhất $1$ giá trị nguyên dương của $x$ để phân thức $K$ nhận giá trị nguyên'
        vdc_da_1_s = 'Có $4$ giá trị nguyên dương của $x$ để phân thức $K$ nhận giá trị nguyên'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Với $x \\in \\mathbb{Z}^*$, ta có $x + 1 > 1$. Để $K \\in \\mathbb{Z}$ thì $x + 1$ là ước của $%s$ và $x + 1 > 1$, suy ra $x + 1 = %s \\Leftrightarrow x = %s$ (duy nhất $1$ giá trị).' % (p, p, x_val)
        loigiai_vdc_s = 'Sai. Vì $x$ nguyên dương nên $x + 1 \\ge 2$, trong các ước của số nguyên tố $%s$ chỉ có $%s \\ge 2$, nên chỉ có $1$ giá trị $x = %s$.' % (p, p, x_val)
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
