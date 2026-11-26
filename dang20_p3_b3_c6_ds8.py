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
def bt_dang20_p3_b3_c6_ds8(self):
    # Dạng 20: Bài toán vật lí về điện trở tương đương của đoạn mạch song song
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # 1/R = 1/x + 1/(x + d) = (2x + d)/(x*(x + d)) => R = x*(x + d)/(2x + d)
        bo = [
            (3, 6, '3,6', 54, 15),
            (6, 6, '4', 72, 18),
            (4, 4, '2,4', 32, 12),   # 32/12 vô hạn -> tránh
            (5, 10, '6', 150, 25),
            (9, 6, '4,5', 90, 20),
            (8, 8, '4,8', 128, 24)  # vô hạn -> tránh
        ]
        bo_chuan = [
            (3, 6, '3,6', 54, 15),
            (6, 6, '4', 72, 18),
            (5, 10, '6', 150, 25),
            (9, 6, '4,5', 90, 20)
        ]
        d_ohm, x_val, kq_str, tu_so, mau_so = random.choice(bo_chuan)
        
        noidungcauhoi = ('Trong một mạch điện mắc song song gồm hai điện trở $R_1 = x\\text{ (}\\Omega\\text{)}$ ($x > 0$) và $R_2 = x + %s\\text{ (}\\Omega\\text{)}$, điện trở tương đương $R$ của đoạn mạch thỏa mãn công thức $\\dfrac{1}{R} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2}$. Tính điện trở tương đương $R$ (đơn vị: $\\Omega$) khi $x = %s$.' % (d_ohm, x_val))
        
        loigiai = ('Ta có:\\'
                   '$$\\dfrac{1}{R} = \\dfrac{1}{x} + \\dfrac{1}{x + %s} = \\dfrac{(x + %s) + x}{x(x + %s)} = \\dfrac{2x + %s}{x(x + %s)}.$$\\'
                   'Suy ra điện trở tương đương của đoạn mạch là $R = \\dfrac{x(x + %s)}{2x + %s}\\text{ (}\\Omega\\text{)}$.\\'
                   'Thay $x = %s$ vào biểu thức trên, ta được $R = \\dfrac{%s \\cdot (%s + %s)}{2 \\cdot %s + %s} = \\dfrac{%s}{%s} = %s\\text{ (}\\Omega\\text{)}$.'
                   % (d_ohm, d_ohm, d_ohm, d_ohm, d_ohm, d_ohm, d_ohm, x_val, x_val, x_val, d_ohm, x_val, d_ohm, tu_so, mau_so, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
