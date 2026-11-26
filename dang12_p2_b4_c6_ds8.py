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




def bt_dang12_p2_b4_c6_ds8(self):
    # Dạng 12: Rút gọn dãy phép tính nhân và chia liên tiếp (Bài 6.32a SGK)
    a = random.choice([2, 3])
    b = random.choice([1, 3, 5])
    while math.gcd(a, b) != 1:
        b = random.choice([1, 3, 5])
    c = random.choice([2, 3, 5])
    
    tu1 = sp.expand(2 * (a*x - b))
    mau1 = sp.expand(x * (c*x - 1))
    tu2 = sp.expand((c*x - 1)**2)
    mau2 = sp.expand(b**3 - (a*x)**3)
    tu3 = sp.expand(c*x - 1)
    mau3 = sp.expand(b**2 + a*b*x + a**2*x**2)
    
    nb_da_1_d = '\\True Nhân tử $%s$ phân tích thành $(%s)(%s)$.' % (latex(mau2), latex(b - a*x), latex(mau3))
    nb_da_1_s = 'Nhân tử $%s$ phân tích thành $(%s)(%s)$.' % (latex(mau2), latex(a*x - b), latex(mau3))
    loigiai_nb_1 = """Áp dụng hằng đẳng thức hiệu hai lập phương, ta có $%s = %s^3 - (%sx)^3 = (%s)(%s)$.""" % (latex(mau2), b, a, latex(b - a*x), latex(mau3))
    
    th_da_1_d = '\\True Tích của hai phân thức đầu tiên bằng $-\\frac{2(%s)}{x(%s)}$.' % (latex(tu3), latex(mau3))
    th_da_1_s = 'Tích của hai phân thức đầu tiên bằng $\\frac{2(%s)}{x(%s)}$.' % (latex(tu3), latex(mau3))
    loigiai_th_1 = """Ta có $\\frac{2(%s)}{x(%s)} \\cdot \\frac{(%s)^2}{(%s)(%s)} = -\\frac{2(%s)}{x(%s)}$.""" % (
        latex(a*x - b), latex(tu3), latex(tu3), latex(b - a*x), latex(mau3), latex(tu3), latex(mau3)
    )
    
    vd_da_1_d = '\\True Kết quả rút gọn cuối cùng của biểu thức $K$ là $-\\frac{2}{x}$.'
    vd_da_1_s = 'Kết quả rút gọn cuối cùng của biểu thức $K$ là $\\frac{2}{x}$.'
    loigiai_vd_1 = """Ta có $K = -\\frac{2(%s)}{x(%s)} \\cdot \\frac{%s}{%s} = -\\frac{2}{x}$.""" % (latex(tu3), latex(mau3), latex(mau3), latex(tu3))
    
    vdc_da_1_d = '\\True Tại $x = -2$, giá trị của $K$ bằng $1$.'
    vdc_da_1_s = 'Tại $x = -2$, giá trị của $K$ bằng $-1$.'
    loigiai_vdc_1 = """Thay $x = -2$ (thỏa mãn điều kiện xác định) vào $K = -\\frac{2}{x}$, ta được $K = -\\frac{2}{-2} = 1$."""
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho biểu thức $K = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} : \\frac{%s}{%s}$ (với các mẫu thức và phân thức chia đều khác $0$). Xét tính đúng sai của các khẳng định sau:"""
                     % (latex(tu1), latex(mau1), latex(tu2), latex(mau2), latex(tu3), latex(mau3)))
                     
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
