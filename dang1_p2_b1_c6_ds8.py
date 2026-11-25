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


def bt_dang1_p2_b1_c6_ds8(self):
    # Dạng 1: Phân tích điều kiện để một biểu thức là phân thức đại số và nhận diện đa thức nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([2, 3, 5, 7])
        c = random.choice([2, 3, 4, 6])
        d = random.choice([2, 3, 5, 8])
        k = random.choice([1, 2, 3, 4])
        
        btA = '\\dfrac{%sx^2 - 1}{%sx + %s}' % (a, b, c)
        btB = '%sx^3 - %sx + %s' % (c, d, k)
        btC = '\\dfrac{x + %s}{0}' % k
        btD = '\\dfrac{x - %s}{1 + \\frac{%s}{x}}' % (a, b)
        
        noidungcauhoi = ('Cho các biểu thức đại số: $A = %s$; $B = %s$; $C = %s$; $D = %s$. Xét tính đúng sai của các khẳng định sau:'
                         % (btA, btB, btC, btD))
        
        nb_da_1_d = '\\True Biểu thức $A$ là một phân thức đại số có tử thức là $%sx^2 - 1$ và mẫu thức là $%sx + %s$' % (a, b, c)
        nb_da_1_s = 'Biểu thức $A$ không phải là phân thức đại số vì tử thức có bậc lớn hơn mẫu thức'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Biểu thức $A = %s$ có tử thức là $%sx^2 - 1$ và mẫu thức là $%sx + %s$ đều là các đa thức với mẫu thức khác đa thức $0$.' % (btA, a, b, c)
        loigiai_nb_s = 'Sai. Phân thức đại số không yêu cầu bậc của tử thức nhỏ hơn bậc của mẫu thức; $A$ có tử và mẫu đều là đa thức (mẫu khác đa thức $0$) nên $A$ là phân thức đại số.'
        
        th_da_1_d = '\\True Biểu thức $B$ là một phân thức đại số với mẫu thức bằng $1$'
        th_da_1_s = 'Biểu thức $B$ không phải là phân thức đại số vì không có mẫu thức'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Mỗi đa thức đều được coi là một phân thức đại số với mẫu thức bằng $1$, tức là $B = \\dfrac{%s}{1}$.' % btB
        loigiai_th_s = 'Sai. Mỗi đa thức đều được coi là một phân thức đại số với mẫu thức bằng $1$.'
        
        vd_da_1_d = '\\True Biểu thức $C$ không phải là phân thức đại số vì mẫu thức bằng $0$'
        vd_da_1_s = 'Biểu thức $C$ là phân thức đại số vì tử thức $x + %s$ là một đa thức' % k
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Điều kiện của phân thức $\\dfrac{M}{N}$ là mẫu thức $N$ khác đa thức $0$, nên $C = %s$ không là phân thức.' % btC
        loigiai_vd_s = 'Sai. Mặc dù tử thức $x + %s$ là đa thức nhưng mẫu thức bằng $0$ nên $C$ không phải là phân thức đại số.' % k
        
        vdc_da_1_d = '\\True Biểu thức $D$ không phải là phân thức đại số vì mẫu thức $1 + \\frac{%s}{x}$ không phải là đa thức' % b
        vdc_da_1_s = 'Biểu thức $D$ là phân thức đại số có mẫu thức là $1 + \\frac{%s}{x}$' % b
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Biểu thức $1 + \\frac{%s}{x}$ chứa phép chia cho biến $x$ nên không phải là đa thức, do đó $D$ không phải là phân thức đại số.' % b
        loigiai_vdc_s = 'Sai. Vì $1 + \\frac{%s}{x}$ không phải là đa thức nên $D$ không thỏa mãn định nghĩa phân thức đại số.' % b
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
