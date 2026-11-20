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


def bt_dang18_p3_b2_c10_hh9(self):
    R_coc = random.choice([4, 5, 6])
    h_coc = random.choice([12, 14, 15])
    h_nuoc = random.choice([7, 8, 9])
    r_bi = random.choice([1, 2])
    # Thể tích phần trống trong cốc: V_trong = pi * R_coc^2 * (h_coc - h_nuoc)
    # Thể tích 1 viên bi: V_bi = 4/3 * pi * r_bi^3
    # Số bi tối đa không tràn = floor(V_trong / V_bi)
    V_trong_heso = (R_coc**2) * (h_coc - h_nuoc)
    so_bi_float = (3 * V_trong_heso) / (4 * (r_bi**3))
    so_bi_max = math.floor(so_bi_float)
    so_bi_str = str(Decimal(str(so_bi_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
    kq_str = str(so_bi_max)

    noidungcauhoi = ('''Một chiếc cốc hình trụ có bán kính đáy bên trong $R = %s\\text{ cm}$ và chiều cao bên trong $h = %s\\text{ cm}$, đang chứa nước ở độ cao $%s\\text{ cm}$. Người ta thả lần lượt từng viên bi thủy tinh đặc hình cầu có bán kính $r = %s\\text{ cm}$ vào cốc. Hỏi có thể thả vào cốc nhiều nhất bao nhiêu viên bi như vậy để nước trong cốc không bị tràn ra ngoài?'''
                     % (R_coc, h_coc, h_nuoc, r_bi))

    loigiai = ('''Chiều cao phần trống phía trên mặt nước của chiếc cốc là: $h_{\\text{trống}} = %s - %s = %s\\text{ (cm)}$.\\\nThể tích phần không gian trống trong cốc là:
$$V_{\\text{trống}} = \\pi R^2 h_{\\text{trống}} = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Thể tích của một viên bi thủy tinh hình cầu là:
$$V_{\\text{bi}} = \\dfrac{4}{3}\\pi r^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}.$$
Ta có tỉ số: $\\dfrac{V_{\\text{trống}}}{V_{\\text{bi}}} = \\dfrac{%s\\pi}{%s\\pi} \\approx %s$.\\\nVậy có thể thả vào cốc nhiều nhất $%s$ viên bi để nước không bị tràn ra ngoài.'''
               % (h_coc, h_nuoc, h_coc - h_nuoc, R_coc, h_coc - h_nuoc, V_trong_heso, r_bi, latex(Rational(4, 3)*(r_bi**3)), V_trong_heso, latex(Rational(4, 3)*(r_bi**3)), so_bi_str, so_bi_max))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
