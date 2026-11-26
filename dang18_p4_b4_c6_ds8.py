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




def bt_dang18_p4_b4_c6_ds8(self):
    # Dạng 18: Bài toán chuyển động đường bộ – Ô tô dừng nghỉ và tăng tốc (Bài 6.44 SGK)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v1 = 50
        t_du_kien = 6
        s_tong = v1 * t_du_kien # 300 km
        t1_str = '2\\frac{1}{2}'
        s1 = 125
        s2 = s_tong - s1 # 175 km
        # Thời gian đi chặng 1 + nghỉ 30 phút (1/2 giờ) = 2.5 + 0.5 = 3 giờ
        # T = 3 + 175/(50 + x)
        # Tại x = 20: T = 3 + 175/70 = 3 + 2.5 = 5.5 giờ (sớm hơn 0.5 giờ = 30 phút)
        # Tại x = 10: T = 3 + 175/60 = 5 + 11/12 giờ (sớm hơn 1/12 giờ = 5 phút)
        
        noidungcauhoi = ("""Một xe khách đi từ Thành phố A đến Thành phố B với vận tốc $50\\text{ km/h}$ và dự kiến đến B sau $6\\text{ giờ}$ chạy. Tuy nhiên, sau khi đi được $2\\frac{1}{2}\\text{ giờ}$ với vận tốc $50\\text{ km/h}$, xe dừng nghỉ $30\\text{ phút}$. Sau khi nghỉ, để đảm bảo hành trình, tài xế tăng vận tốc thêm $x\\text{ (km/h)}$ ($x > 0$) ở chặng thứ hai. \\\\
        a) Tính độ dài quãng đường AB và quãng đường còn lại sau khi xe dừng nghỉ. \\\\
        b) Viết biểu thức $T$ theo biến $x$ biểu thị tổng thời gian thực tế (tính bằng giờ) xe đi hết quãng đường AB (kể cả thời gian nghỉ). \\\\
        c) Tính giá trị của $T$ tại $x = 10$ và $x = 20$; cho biết trong mỗi trường hợp xe đến B đúng giờ, sớm hơn hay muộn hơn dự kiến bao nhiêu phút."""
                         )
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Độ dài quãng đường AB là $50 \\cdot 6 = 300\\text{ (km)}$.\\\\
        Quãng đường xe đi được trong chặng đầu là $50 \\cdot 2\\frac{1}{2} = 125\\text{ (km)}$, nên quãng đường còn lại sau khi dừng nghỉ là $300 - 125 = 175\\text{ (km)}$. \n
        \\item Đổi $30\\text{ phút} = \\frac{1}{2}\\text{ giờ}$. Tổng thời gian xe chạy ở chặng đầu và thời gian dừng nghỉ là $2\\frac{1}{2} + \\frac{1}{2} = 3\\text{ (giờ)}$.\\\\
        Vận tốc của xe ở chặng thứ hai là $50 + x\\text{ (km/h)}$, nên thời gian xe đi hết quãng đường còn lại là $\\frac{175}{50 + x}\\text{ (giờ)}$.\\\\
        Vậy biểu thức biểu thị tổng thời gian thực tế xe đi hết quãng đường AB là:\\\\
        $$T = 3 + \\frac{175}{50 + x}\\text{ (giờ)}.$$ \n
        \\item - Tại $x = 10$: $T = 3 + \\frac{175}{50 + 10} = 3 + \\frac{35}{12} = 5\\frac{11}{12}\\text{ (giờ)}$. Vì $5\\frac{11}{12} < 6$ nên xe đến B sớm hơn dự kiến $6 - 5\\frac{11}{12} = \\frac{1}{12}\\text{ giờ} = 5\\text{ phút}$.\\\\
        - Tại $x = 20$: $T = 3 + \\frac{175}{50 + 20} = 3 + 2{,}5 = 5{,}5\\text{ (giờ)}$. Vì $5{,}5 < 6$ nên xe đến B sớm hơn dự kiến $6 - 5{,}5 = 0{,}5\\text{ giờ} = 30\\text{ phút}$. \n
        \\end{enumEX} \n"""
                   )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
