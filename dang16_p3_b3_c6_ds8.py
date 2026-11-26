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
def bt_dang16_p3_b3_c6_ds8(self):
    # Dạng 16: Bài toán chuyển động đường thủy (xuôi dòng và ngược dòng)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # s km xuôi dòng và s km ngược dòng, v_nuoc = v0, v_tau = x => t = 2*s*x / (x^2 - v0^2)
        bo = [
            (24, 2, 10, '5', 480, 96),
            (30, 3, 12, '5,3', 720, 135),   # vô hạn -> tránh
            (18, 3, 9, '4,5', 324, 72),
            (36, 3, 15, '5', 1080, 216),
            (15, 2, 8, '4', 240, 60)
        ]
        bo_chuan = [
            (24, 2, 10, '5', 480, 96),
            (18, 3, 9, '4,5', 324, 72),
            (36, 3, 15, '5', 1080, 216),
            (15, 2, 8, '4', 240, 60)
        ]
        s_km, v_nuoc, x_val, kq_str, tu_so, mau_so = random.choice(bo_chuan)
        hai_s = 2 * s_km
        v0_2 = v_nuoc ** 2
        
        noidungcauhoi = ('Một ca nô chạy xuôi dòng một khúc sông dài $%s\\text{ km}$, sau đó chạy ngược dòng trở về điểm xuất phát. Biết vận tốc của dòng nước là $%s\\text{ km/h}$ và vận tốc riêng của ca nô là $x\\text{ (km/h)}$ ($x > %s$). Khi vận tốc riêng của ca nô là $%s\\text{ km/h}$, tổng thời gian cả đi và về của ca nô là bao nhiêu giờ?' % (s_km, v_nuoc, v_nuoc, x_val))
        
        loigiai = ('Vận tốc ca nô khi xuôi dòng là $x + %s\\text{ (km/h)}$, khi ngược dòng là $x - %s\\text{ (km/h)}$.\\'
                   'Phân thức biểu thị tổng thời gian cả đi và về của ca nô là:\\'
                   '$$t = \\dfrac{%s}{x + %s} + \\dfrac{%s}{x - %s} = \\dfrac{%s(x - %s) + %s(x + %s)}{x^2 - %s} = \\dfrac{%sx}{x^2 - %s}\\text{ (giờ)}.$$\\'
                   'Thay $x = %s$ vào biểu thức trên, ta được tổng thời gian cả đi và về của ca nô là:\\'
                   '$$t = \\dfrac{%s \\cdot %s}{%s^2 - %s} = \\dfrac{%s}{%s} = %s\\text{ (giờ)}.$$'
                   % (v_nuoc, v_nuoc, s_km, v_nuoc, s_km, v_nuoc, s_km, v_nuoc, s_km, v_nuoc, v0_2, hai_s, v0_2, x_val, hai_s, x_val, x_val, v0_2, tu_so, mau_so, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
