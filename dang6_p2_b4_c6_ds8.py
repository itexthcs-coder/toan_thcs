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




def bt_dang6_p2_b4_c6_ds8(self):
    # Dạng 6: Tìm hai phân thức chưa biết trong hệ hai đẳng thức nhân và chia (Bài 6.28 SGK)
    a = random.choice([2, 3, 4])
    b = random.randint(1, 4)
    
    tu_M1 = sp.expand(x + b)
    mau_M1 = sp.expand(a*x + 1)
    tu_M2 = sp.expand(x * (x + b))
    mau_M2 = sp.expand((a*x)**2 - 1)
    
    tu_N1 = x**2
    mau_N1 = sp.expand((x + a)**2)
    tu_N2 = sp.expand((x + 1)*(x + a))
    mau_N2 = sp.expand(x * (x - a))
    
    nb_da_1_d = '\\True Phân thức $M$ được tìm bằng phép chia $\\frac{%s}{%s} : \\frac{%s}{%s}$.' % (latex(tu_M2), latex(mau_M2), latex(tu_M1), latex(mau_M1))
    nb_da_1_s = 'Phân thức $M$ được tìm bằng phép nhân $\\frac{%s}{%s} \\cdot \\frac{%s}{%s}$.' % (latex(tu_M2), latex(mau_M2), latex(tu_M1), latex(mau_M1))
    loigiai_nb_1 = """Từ $M \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$, suy ra $M = \\frac{%s}{%s} : \\frac{%s}{%s}$.""" % (
        latex(tu_M1), latex(mau_M1), latex(tu_M2), latex(mau_M2), latex(tu_M2), latex(mau_M2), latex(tu_M1), latex(mau_M1)
    )
    
    th_da_1_d = '\\True Rút gọn phân thức $M$ ta được $M = \\frac{x}{%s}$.' % latex(a*x - 1)
    th_da_1_s = 'Rút gọn phân thức $M$ ta được $M = \\frac{x}{%s}$.' % latex(a*x + 1)
    loigiai_th_1 = """Ta có $M = \\frac{x(%s)}{(%s)(%s)} \\cdot \\frac{%s}{%s} = \\frac{x}{%s}$.""" % (
        latex(tu_M1), latex(a*x - 1), latex(a*x + 1), latex(mau_M1), latex(tu_M1), latex(a*x - 1)
    )
    
    vd_da_1_d = '\\True Rút gọn phân thức $N$ ta được $N = \\frac{x(x + 1)}{%s}$.' % latex(x**2 - a**2)
    vd_da_1_s = 'Rút gọn phân thức $N$ ta được $N = \\frac{x + 1}{x(%s)}$.' % latex(x - a)
    loigiai_vd_1 = """Ta có $N = \\frac{%s}{%s} \\cdot \\frac{x^2}{(%s)^2} = \\frac{(x + 1)(%s)}{x(%s)} \\cdot \\frac{x^2}{(%s)^2} = \\frac{x(x + 1)}{%s}$.""" % (
        latex(tu_N2), latex(mau_N2), latex(x + a), latex(x + a), latex(x - a), latex(x + a), latex(x**2 - a**2)
    )
    
    vdc_da_1_d = '\\True Tích $M \\cdot N$ bằng $\\frac{x^2(x + 1)}{(%s)(%s)}$.' % (latex(a*x - 1), latex(x**2 - a**2))
    vdc_da_1_s = 'Tích $M \\cdot N$ bằng $\\frac{x + 1}{(%s)(%s)}$.' % (latex(a*x - 1), latex(x - a))
    loigiai_vdc_1 = """Ta có $M \\cdot N = \\frac{x}{%s} \\cdot \\frac{x(x + 1)}{%s} = \\frac{x^2(x + 1)}{(%s)(%s)}$.""" % (
        latex(a*x - 1), latex(x**2 - a**2), latex(a*x - 1), latex(x**2 - a**2)
    )
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho hai phân thức $M$ và $N$ thỏa mãn $M \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$ và $N : \\frac{%s}{%s} = \\frac{%s}{%s}$ (với các mẫu thức đều khác $0$). Xét tính đúng sai của các khẳng định sau:"""
                     % (latex(tu_M1), latex(mau_M1), latex(tu_M2), latex(mau_M2), latex(tu_N1), latex(mau_N1), latex(tu_N2), latex(mau_N2)))
                     
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
