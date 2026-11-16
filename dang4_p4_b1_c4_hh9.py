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


def bt_dang4_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g1 = randint(55, 85)
        g2 = randint(50, 82)
        g3_deg = randint(52, 78)
        g3_min = randint(10, 50)
        g4 = randint(60, 88)

        g_sin = randint(20, 32)
        g_cos = randint(46, 62)
        g_phu = 90 - g_cos
        dau = '<' if g_sin < g_phu else '>'

        # Nội dung câu hỏi
        noidungcauhoi = ('''Thực hiện các yêu cầu sau: \\\\
a) Viết các tỉ số lượng giác sau thành tỉ số lượng giác của góc nhỏ hơn $45^\\circ$: $\\sin %s^\\circ$; $\\cos %s^\\circ$; $\\tan %s^\\circ %s'$; $\\cot %s^\\circ$. \\\\
b) So sánh $\\sin %s^\\circ$ và $\\cos %s^\\circ$.'''
                         % (str(g1), str(g2), str(g3_deg), str(g3_min), str(g4),
                            str(g_sin), str(g_cos)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Áp dụng định lí tỉ số lượng giác của hai góc phụ nhau, ta có: \\\\
$\\sin %s^\\circ = \\cos(90^\\circ - %s^\\circ) = \\cos %s^\\circ$; \\\\
$\\cos %s^\\circ = \\sin(90^\\circ - %s^\\circ) = \\sin %s^\\circ$; \\\\
$\\tan %s^\\circ %s' = \\cot(90^\\circ - %s^\\circ %s') = \\cot %s^\\circ %s'$; \\\\
$\\cot %s^\\circ = \\tan(90^\\circ - %s^\\circ) = \\tan %s^\\circ$. \n
\\item Ta có $\\cos %s^\\circ = \\sin(90^\\circ - %s^\\circ) = \\sin %s^\\circ$. \\\\
Vì góc nhọn càng lớn thì $\\sin$ của góc đó càng lớn nên từ $%s^\\circ %s %s^\\circ$ suy ra $\\sin %s^\\circ %s \\sin %s^\\circ$. \\\\
Vậy $\\sin %s^\\circ %s \\cos %s^\\circ$. \n
\\end{enumEX} \n'''
                   % (str(g1), str(g1), str(90 - g1),
                      str(g2), str(g2), str(90 - g2),
                      str(g3_deg), str(g3_min), str(g3_deg), str(g3_min), str(89 - g3_deg), str(60 - g3_min),
                      str(g4), str(g4), str(90 - g4),
                      str(g_cos), str(g_cos), str(g_phu),
                      str(g_sin), dau, str(g_phu), str(g_sin), dau, str(g_phu),
                      str(g_sin), dau, str(g_cos)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
