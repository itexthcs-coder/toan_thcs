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




def bt_dang11_p2_b4_c6_ds8(self):
    # Dạng 11: Tìm đa thức ẩn trong đẳng thức phân thức chứa hằng đẳng thức (Bài 6.41c,d SGK)
    a = random.randint(2, 4)
    b = random.randint(2, 5)
    
    tu_1 = sp.expand((x - a)**2)
    mau_1 = sp.expand(x**2 - b**2)
    nhan_1 = sp.expand(x - a)
    mau_nhan_1 = sp.expand(x + b)
    
    tu_2 = sp.expand(x**2 - a**2)
    mau_2 = sp.expand(x * (x + b))
    chia_2 = sp.expand(x**2 - b**2)
    mau_chia_2 = sp.expand(2 * (x + a))
    
    nb_da_1_d = '\\True Ở đẳng thức (1), đa thức $P$ là $\\frac{x - %s}{x - %s}$ (là một phân thức đại số, không phải đa thức nguyên).' % (a, b)
    nb_da_1_s = 'Ở đẳng thức (1), đa thức $P$ là $x - %s$.' % a
    loigiai_nb_1 = """Từ (1), ta có $P = \\frac{(x - %s)^2}{(x - %s)(x + %s)} \\cdot \\frac{x + %s}{x - %s} = \\frac{x - %s}{x - %s}$.""" % (a, b, b, b, a, a, b)
    
    th_da_1_d = '\\True Ở đẳng thức (2), $P = \\frac{(x - %s)(x - %s)}{2x}$.' % (a, b)
    th_da_1_s = 'Ở đẳng thức (2), $P = \\frac{2x}{(x - %s)(x - %s)}$.' % (a, b)
    loigiai_th_1 = """Từ (2), ta có $P = \\frac{(x - %s)(x + %s)}{x(x + %s)} \\cdot \\frac{(x - %s)(x + %s)}{2(x + %s)} = \\frac{(x - %s)(x - %s)}{2x}$.""" % (a, a, b, b, b, a, a, b)
    
    vd_da_1_d = '\\True Nếu $Q \\cdot \\frac{x + %s}{x^2 - %sx + %s} = \\frac{x^3 + %s}{x^2 - %s}$, thì rút gọn $Q$ ta được $Q = \\frac{(x^2 - %sx + %s)^2}{x - %s}$.' % (a, a, a**2, a**3, a**2, a, a**2, a)
    vd_da_1_s = 'Nếu $Q \\cdot \\frac{x + %s}{x^2 - %sx + %s} = \\frac{x^3 + %s}{x^2 - %s}$, thì rút gọn $Q$ ta được $Q = \\frac{1}{x - %s}$.' % (a, a, a**2, a**3, a**2, a)
    loigiai_vd_1 = """Ta có $Q = \\frac{(x + %s)(x^2 - %sx + %s)}{(x - %s)(x + %s)} \\cdot \\frac{x^2 - %sx + %s}{x + %s} = \\frac{(x^2 - %sx + %s)^2}{x - %s}$.""" % (a, a, a**2, a, a, a, a**2, a, a, a**2, a)
    
    vdc_da_1_d = '\\True Đa thức $H$ thỏa mãn $\\frac{H}{x - %s} = \\frac{x^3 - %s}{x^2 + %sx + %s}$ là $H = (x - %s)^2$.' % (a, a**3, a, a**2, a)
    vdc_da_1_s = 'Đa thức $H$ thỏa mãn $\\frac{H}{x - %s} = \\frac{x^3 - %s}{x^2 + %sx + %s}$ là $H = x - %s$.' % (a, a**3, a, a**2, a)
    loigiai_vdc_1 = """Ta có $\\frac{x^3 - %s}{x^2 + %sx + %s} = \\frac{(x - %s)(x^2 + %sx + %s)}{x^2 + %sx + %s} = x - %s$, suy ra $H = (x - %s)^2$.""" % (a**3, a, a**2, a, a, a**2, a, a**2, a, a)
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho hai đẳng thức: (1) $P \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$ và (2) $P : \\frac{%s}{%s} = \\frac{%s}{%s}$ (với các phân thức đều có nghĩa). Xét tính đúng sai của các khẳng định sau:"""
                     % (latex(nhan_1), latex(mau_nhan_1), latex(tu_1), latex(mau_1),
                        latex(chia_2), latex(mau_chia_2), latex(tu_2), latex(mau_2)))
                     
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
