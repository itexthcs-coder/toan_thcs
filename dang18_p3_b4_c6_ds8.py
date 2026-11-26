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




def bt_dang18_p3_b4_c6_ds8(self):
    # Dạng 18: Bài toán chuyển động – Tính vận tốc tăng thêm ở chặng sau (Bài 6.44 SGK)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_cd = random.choice([
            (50, 4, 1.5, 0.5, 12.5), # S = 200, S1 = 75, S2 = 125, t_con = 2 => v2 = 62.5 => tang 12.5
            (60, 5, 2.5, 0.5, 15),   # S = 300, S1 = 150, S2 = 150, t_con = 2 => v2 = 75 => tang 15
            (48, 5, 2.5, 0.5, 12)    # S = 240, S1 = 120, S2 = 120, t_con = 2 => v2 = 60 => tang 12
        ])
        v1, t_tong, t1, t_nghi, tang_v = bo_cd
        s_tong = v1 * t_tong
        s1 = int(round(v1 * t1))
        s2 = s_tong - s1
        t_con = t_tong - (t1 + t_nghi)
        v2 = Rational(s2, int(round(t_con)))
        
        t1_str = str(t1).replace('.', ',')
        t_nghi_phut = int(round(t_nghi * 60))
        kq_str = str(tang_v).replace('.', ',')
        
        noidungcauhoi = ("""Một ô tô đi từ A đến B với vận tốc $%s\\text{ km/h}$ và dự kiến đến B sau $%s\\text{ giờ}$. Tuy nhiên, sau khi đi được $%s\\text{ giờ}$ với vận tốc $%s\\text{ km/h}$, xe dừng nghỉ $%s\\text{ phút}$. Hỏi trên quãng đường còn lại, xe phải tăng vận tốc thêm bao nhiêu $\\text{km/h}$ so với vận tốc ban đầu để đến B đúng thời gian dự kiến?"""
                         % (v1, t_tong, t1_str, v1, t_nghi_phut))
        
        loigiai = ("""Độ dài quãng đường AB là $%s \\cdot %s = %s\\text{ (km)}$.\\\\
        Quãng đường xe đi được trong chặng đầu là $%s \\cdot %s = %s\\text{ (km)}$, nên quãng đường còn lại là $%s - %s = %s\\text{ (km)}$.\\\\
        Gọi $x\\text{ (km/h)}$ ($x > 0$) là vận tốc tăng thêm ở chặng thứ hai. Đổi $%s\\text{ phút} = %s\\text{ giờ}$.\\\\
        Để xe đến B đúng thời gian dự kiến là $%s\\text{ giờ}$, ta có phương trình:\\\\
        $$%s + %s + \\frac{%s}{%s + x} = %s \\Leftrightarrow \\frac{%s}{%s + x} = %s \\Leftrightarrow %s + x = %s \\Leftrightarrow x = %s.$$\\\\
        Vậy xe phải tăng vận tốc thêm $%s\\text{ km/h}$."""
                   % (v1, t_tong, s_tong, v1, t1_str, s1, s_tong, s1, s2,
                      t_nghi_phut, str(t_nghi).replace('.', ','), t_tong,
                      t1_str, str(t_nghi).replace('.', ','), s2, v1, t_tong,
                      s2, v1, int(round(t_con)), v1, str(float(v2)).replace('.', ','), kq_str, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % kq_str
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
