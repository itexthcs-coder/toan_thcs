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


def bt_dang19_p4_b2_c1_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t2_x = random.choice([25, 30, 35])
        t2_y = random.choice([15, 20, 25])
        t4_x = random.choice([35, 40, 45])
        t4_y = random.choice([20, 25, 30])
        t6_x = random.choice([20, 25, 30])
        t6_y = random.choice([30, 35, 40])
        
        tong_x = t2_x + t4_x + t6_x
        tong_y = t2_y + t4_y + t6_y
        
        x0 = randint(10, 13)
        y0 = randint(7, 9)
        calo = tong_x * x0 + tong_y * y0
        
        noidungcauhoi = ('''Trong một tuần tập luyện, anh Minh chạy bộ với vận tốc tiêu hao trung bình $x$ (kcal/phút) và đạp xe với vận tốc tiêu hao trung bình $y$ (kcal/phút). Ngày thứ Hai anh chạy bộ $%s$ phút và đạp xe $%s$ phút; ngày thứ Tư anh chạy bộ $%s$ phút và đạp xe $%s$ phút; ngày thứ Sáu anh chạy bộ $%s$ phút và đạp xe $%s$ phút. \\\\
a) Viết đa thức thu gọn biểu thị tổng lượng calo anh Minh đã tiêu thụ trong cả ba ngày tập luyện. \\\\
b) Tính tổng lượng calo tiêu thụ biết $x = %s$ kcal/phút và $y = %s$ kcal/phút.'''
                         % (t2_x, t2_y, t4_x, t4_y, t6_x, t6_y, x0, y0))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tổng lượng calo anh Minh tiêu thụ trong ba ngày tập luyện là:
\\begin{align*}
C &= (%sx + %sy) + (%sx + %sy) + (%sx + %sy) \\\\
  &= (%s + %s + %s)x + (%s + %s + %s)y \\\\
  &= %sx + %sy \\text{ (kcal)}.
\\end{align*}
\\item Thay $x = %s$ và $y = %s$ vào đa thức $C$, ta được:
$$C = %s \\cdot %s + %s \\cdot %s = %s + %s = %s \\text{ (kcal)}.$$
\\end{enumEX}''' % (t2_x, t2_y, t4_x, t4_y, t6_x, t6_y, t2_x, t4_x, t6_x, t2_y, t4_y, t6_y, tong_x, tong_y,
                      x0, y0, tong_x, x0, tong_y, y0, tong_x * x0, tong_y * y0, calo))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
