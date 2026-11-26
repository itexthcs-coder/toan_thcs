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




def bt_dang19_p2_b4_c6_ds8(self):
    # Dạng 19: Bài toán tài chính – Tính tiền vốn gửi tiết kiệm ngân hàng (Bài 6.40 SGK)
    ls_mau = random.choice([4, 5, 8])
    lai_mau = random.choice([8, 10, 12])
    goc_mau = (100 * lai_mau) // ls_mau
    
    nb_da_1_d = '\\True Lãi suất một năm viết dưới dạng phân thức là $\\frac{x}{100}$.'
    nb_da_1_s = 'Lãi suất một năm viết dưới dạng phân thức là $\\frac{100}{x}$.'
    loigiai_nb_1 = """Theo định nghĩa phần trăm, mức lãi suất $x\\%$ một năm viết dưới dạng phân thức là $\\frac{x}{100}$."""
    
    th_da_1_d = '\\True Số tiền gốc người đó đã gửi vào ngân hàng là $\\frac{100a}{x}$ (đồng).'
    th_da_1_s = 'Số tiền gốc người đó đã gửi vào ngân hàng là $\\frac{ax}{100}$ (đồng).'
    loigiai_th_1 = """Gọi số tiền gốc là $T$. Ta có $T \\cdot \\frac{x}{100} = a \\Rightarrow T = a : \\frac{x}{100} = \\frac{100a}{x}$ (đồng)."""
    
    vd_da_1_d = '\\True Tổng số tiền cả gốc lẫn lãi người đó nhận được sau một năm là $\\frac{a(x + 100)}{x}$ (đồng).'
    vd_da_1_s = 'Tổng số tiền cả gốc lẫn lãi người đó nhận được sau một năm là $\\frac{100a + x}{x}$ (đồng).'
    loigiai_vd_1 = """Tổng số tiền cả gốc lẫn lãi sau một năm là $\\frac{100a}{x} + a = \\frac{100a + ax}{x} = \\frac{a(x + 100)}{x}$ (đồng)."""
    
    vdc_da_1_d = '\\True Nếu lãi suất là $%s\\%%/\\text{năm}$ và tiền lãi nhận được sau một năm là $%s$ triệu đồng thì số tiền gốc đã gửi là $%s$ triệu đồng.' % (ls_mau, lai_mau, goc_mau)
    vdc_da_1_s = 'Nếu lãi suất là $%s\\%%/\\text{năm}$ và tiền lãi nhận được sau một năm là $%s$ triệu đồng thì số tiền gốc đã gửi là $%s$ triệu đồng.' % (ls_mau, lai_mau, goc_mau // 2)
    loigiai_vdc_1 = """Thay $x = %s, a = %s$ vào công thức tiền gốc, ta được $T = \\frac{100 \\cdot %s}{%s} = %s$ (triệu đồng).""" % (ls_mau, lai_mau, lai_mau, ls_mau, goc_mau)
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Một người gửi một khoản tiền vào ngân hàng với mức lãi suất một năm là $x\\%$ ($x > 0$). Sau một năm, người đó nhận được số tiền lãi là $a$ đồng ($a > 0$). Xét tính đúng sai của các khẳng định sau:""")
                     
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
