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
def bt_dang6_p2_b3_c6_ds8(self):
    # Dạng 6: Vận dụng tính chất giao hoán, kết hợp rút gọn biểu thức bốn phân thức
    a = random.choice([1, 2, 3])
    b = random.choice([2, 3, 4])
    m = random.choice([3, 4, 5])
    n = random.choice([2, 3, 4])
    k = random.choice([2, 3, 5])
    tong_mn = m + n
    
    noidungcauhoi = ('Cho biểu thức $E = \\dfrac{x + %s}{x - %s} + \\dfrac{%sx}{x + %s} + \\dfrac{%s - x}{x - %s} - \\dfrac{%sx}{x + %s}$ (với $x \\neq %s, x \\neq -%s$). Xét tính đúng, sai của các khẳng định sau:' % (m, a, k, b, n, a, k, b, a, b))
    
    list_nb_da_1 = [
        '\\True Cặp phân thức $\\dfrac{%sx}{x + %s}$ và $-\\dfrac{%sx}{x + %s}$ là hai phân thức đối nhau nên có tổng bằng $0$' % (k, b, k, b),
        'Cặp phân thức $\\dfrac{%sx}{x + %s}$ và $-\\dfrac{%sx}{x + %s}$ có tổng bằng $\\dfrac{%sx}{x + %s}$' % (k, b, k, b, 2 * k, b)
    ]
    loigiai_nb_1 = ('Hai phân thức $\\dfrac{%sx}{x + %s}$ và $-\\dfrac{%sx}{x + %s}$ đối nhau nên tổng của chúng bằng $0$.' % (k, b, k, b))
    
    list_th_da_1 = [
        '\\True Nhóm các phân thức cùng mẫu $x - %s$, ta được $\\dfrac{x + %s + %s - x}{x - %s}$' % (a, m, n, a),
        'Nhóm các phân thức cùng mẫu $x - %s$, ta được $\\dfrac{2x + %s}{x - %s}$' % (a, tong_mn, a)
    ]
    loigiai_th_1 = ('Áp dụng tính chất giao hoán và kết hợp: $\\dfrac{x + %s}{x - %s} + \\dfrac{%s - x}{x - %s} = \\dfrac{x + %s + %s - x}{x - %s}$.' % (m, a, n, a, m, n, a))
    
    list_vd_da_1 = [
        '\\True Biểu thức $E$ rút gọn thành $\\dfrac{%s}{x - %s}$' % (tong_mn, a),
        'Biểu thức $E$ rút gọn thành $\\dfrac{%s}{x - %s}$' % (abs(m - n) if m != n else m + 1, a)
    ]
    loigiai_vd_1 = ('Thu gọn tử thức: $x + %s + %s - x = %s$, nên $E = \\dfrac{%s}{x - %s} + 0 = \\dfrac{%s}{x - %s}$.' % (m, n, tong_mn, tong_mn, a, tong_mn, a))
    
    list_vdc_da_1 = [
        'Không tồn tại giá trị nguyên nào của $x$ để biểu thức $E$ nhận giá trị nguyên',
        '\\True Tồn tại giá trị nguyên của $x$ (ví dụ $x = %s$) để biểu thức $E$ nhận giá trị nguyên' % (a + 1)
    ]
    loigiai_vdc_1 = ('Khi $x = %s$ (thỏa mãn $x \\neq %s, x \\neq -%s$), ta có $E = \\dfrac{%s}{%s - %s} = %s \\in \\mathbb{Z}$.' % (a + 1, a, b, tong_mn, a + 1, a, tong_mn))
    
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
