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




def bt_dang18_p2_b4_c6_ds8(self):
    # Dạng 18: Bài toán chuyển động – Ô tô đi từ Hà Nội đến Cửa Lò (Bài 6.44 SGK)
    nb_da_1_d = '\\True Độ dài quãng đường Hà Nội – Cửa Lò là $300\\text{ km}$ và quãng đường còn lại sau khi dừng nghỉ là $140\\text{ km}$.'
    nb_da_1_s = 'Độ dài quãng đường Hà Nội – Cửa Lò là $300\\text{ km}$ và quãng đường còn lại sau khi dừng nghỉ là $160\\text{ km}$.'
    loigiai_nb_1 = """Quãng đường Hà Nội – Cửa Lò dài $60 \\cdot 5 = 300\\text{ (km)}$. Chặng đầu xe đi được $60 \\cdot 2\\frac{2}{3} = 160\\text{ (km)}$, nên quãng đường còn lại là $300 - 160 = 140\\text{ (km)}$."""
    
    th_da_1_d = '\\True Biểu thức $P$ biểu thị tổng thời gian thực tế (tính bằng giờ) xe chạy hết quãng đường (kể cả thời gian nghỉ) là $P = 3 + \\frac{140}{60 + x}$.'
    th_da_1_s = 'Biểu thức $P$ biểu thị tổng thời gian thực tế (tính bằng giờ) xe chạy hết quãng đường (kể cả thời gian nghỉ) là $P = 2\\frac{2}{3} + \\frac{140}{60 + x}$.'
    loigiai_th_1 = """Thời gian chặng đầu và thời gian nghỉ $20$ phút ($\\frac{1}{3}$ giờ) là $2\\frac{2}{3} + \\frac{1}{3} = 3$ (giờ). Thời gian đi chặng hai là $\\frac{140}{60 + x}$ (giờ). Vậy $P = 3 + \\frac{140}{60 + x}$."""
    
    vd_da_1_d = '\\True Nếu tăng vận tốc thêm $10\\text{ km/h}$ ở chặng thứ hai thì xe đến Cửa Lò đúng thời gian dự kiến là $5\\text{ giờ}$.'
    vd_da_1_s = 'Nếu tăng vận tốc thêm $10\\text{ km/h}$ ở chặng thứ hai thì xe đến Cửa Lò muộn hơn dự kiến $1\\text{ giờ}$.'
    loigiai_vd_1 = """Thay $x = 10$ vào $P$, ta được $P = 3 + \\frac{140}{60 + 10} = 3 + 2 = 5$ (giờ), đúng bằng thời gian dự kiến."""
    
    vdc_da_1_d = '\\True Nếu tăng vận tốc thêm $15\\text{ km/h}$ ở chặng thứ hai thì xe đến Cửa Lò sớm hơn dự kiến $\\frac{2}{15}\\text{ giờ}$.'
    vdc_da_1_s = 'Nếu tăng vận tốc thêm $15\\text{ km/h}$ ở chặng thứ hai thì xe đến Cửa Lò sớm hơn dự kiến $\\frac{1}{3}\\text{ giờ}$.'
    loigiai_vdc_1 = """Thay $x = 15$ vào $P$, ta được $P = 3 + \\frac{140}{75} = 4\\frac{13}{15}$ (giờ), sớm hơn dự kiến $5 - 4\\frac{13}{15} = \\frac{2}{15}$ (giờ)."""
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Một xe ô tô đi từ Hà Nội đến Cửa Lò với vận tốc $60\\text{ km/h}$ và dự kiến đến Cửa Lò sau $5\\text{ giờ}$ xe chạy. Tuy nhiên, sau $2\\frac{2}{3}\\text{ giờ}$ chạy với vận tốc $60\\text{ km/h}$, xe dừng nghỉ $20\\text{ phút}$. Sau khi dừng nghỉ, xe tăng vận tốc thêm $x\\text{ (km/h)}$ ($x > 0$) ở chặng thứ hai. Xét tính đúng sai của các khẳng định sau:""")
                     
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
