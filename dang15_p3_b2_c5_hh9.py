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

def bt_dang15_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        so_cabin = random.choice([18, 20, 24, 30, 36])
        goc_1 = 360 // so_cabin
        c1 = randint(1, 4)
        so_khoang = randint(3, so_cabin // 2 - 2)
        c2 = c1 + so_khoang
        cung_nho = so_khoang * goc_1
        cung_lon = 360 - cung_nho
        kq_str = str(cung_lon)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vòng đu quay hình tròn tâm $O$ gắn $%s$ cabin cách đều nhau trên vành tròn, được đánh số liên tiếp từ $1$ đến $%s$ theo chiều kim đồng hồ (hình vẽ minh họa). Tính số đo của cung lớn nối từ cabin số $%s$ đến cabin số $%s$ (đơn vị: độ).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\draw[line width=1pt] (O) circle (1.8);
        \\foreach \\k in {0,30,...,330} {
            \\draw[line width=1pt] (O)--(\\k:1.8);
            \\fill (\\k:1.8) circle (1.5pt);
        }
        \\fill (O) circle (1pt) node[below right] {$O$};
        \\end{tikzpicture}
        \\end{center}''' % (so_cabin, so_cabin, c1, c2))

        # Nội dung lời giải
        loigiai = ('''Vì $%s$ cabin chia đường tròn $360^\\circ$ thành $%s$ cung bằng nhau nên mỗi khoảng giữa hai cabin kề nhau ứng với cung có số đo bằng $\\dfrac{360^\\circ}{%s} = %s^\\circ$.\\\\
        Từ cabin số $%s$ đến cabin số $%s$ có $%s - %s = %s$ khoảng chia đều, nên cung nhỏ nối hai cabin này có số đo bằng $%s \\cdot %s^\\circ = %s^\\circ$.\\\\
        Vậy số đo của cung lớn nối từ cabin số $%s$ đến cabin số $%s$ bằng $360^\\circ - %s^\\circ = %s^\\circ$.'''
                   % (so_cabin, so_cabin, so_cabin, goc_1, c1, c2, c2, c1, so_khoang, so_khoang, goc_1, cung_nho, c1, c2, cung_nho, cung_lon))

        #Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
