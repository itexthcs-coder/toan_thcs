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

def bt_dang8_p3_b4_c7_ds8(self):
    # Dạng 8: Tìm tham số m để ba đường thẳng đồng quy
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a1 = random.choice([1, 2, 3])
        a2 = random.choice([-3, -2, -1])
        x0 = random.choice([1, 2, 3, 4])
        y0 = random.choice([-4, -2, 2, 4, 5, 6])
        b1 = y0 - a1 * x0
        b2 = y0 - a2 * x0
        k = random.choice([1, 2, 3])
        m_ans = random.choice([i for i in range(-6, 7) if i != 0 and i != k])
        b3 = y0 - (m_ans - k) * x0
        kq_str = str(m_ans)

        dau_b1 = '+' if b1 >= 0 else '-'
        dau_b2 = '+' if b2 >= 0 else '-'
        dau_b3 = '+' if b3 >= 0 else '-'
        str_a1 = 'x' if a1 == 1 else '%sx' % a1
        str_a2 = '-x' if a2 == -1 else '%sx' % a2

        noidungcauhoi = ('''Cho ba đường thẳng $d_1: y = %s %s %s$, $d_2: y = %s %s %s$ và $d_3: y = (m - %s)x %s %s$. Tìm giá trị của tham số $m$ để ba đường thẳng trên đồng quy tại một điểm.'''
                         % (str_a1, dau_b1, abs(b1), str_a2, dau_b2, abs(b2), k, dau_b3, abs(b3)))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

        loigiai = ('''Tìm tọa độ giao điểm của $d_1$ và $d_2$:\\\\
Phương trình hoành độ giao điểm của $d_1$ và $d_2$ là:\\\\
$%s %s %s = %s %s %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$.\\\\
Thay $x = %s$ vào $d_1$, ta được: $y = %s \\cdot %s %s %s = %s$.\\\\
Vậy giao điểm của $d_1$ và $d_2$ là $M(%s; %s)$.\\\\
Để ba đường thẳng $d_1, d_2, d_3$ đồng quy thì đường thẳng $d_3$ phải đi qua điểm $M(%s; %s)$ và có hệ số góc $m - %s \\neq 0$.\\\\
Thay $x = %s, y = %s$ vào phương trình $d_3$, ta được:\\\\
$%s = (m - %s) \\cdot %s %s %s \\Leftrightarrow %s(m - %s) = %s \\Leftrightarrow m - %s = %s \\Leftrightarrow m = %s$ (thỏa mãn $m - %s = %s \\neq 0$).\\\\
Vậy giá trị cần tìm là $m = %s$.'''
                   % (str_a1, dau_b1, abs(b1), str_a2, dau_b2, abs(b2), a1 - a2, b2 - b1, x0,
                      x0, a1, x0, dau_b1, abs(b1), y0,
                      x0, y0,
                      x0, y0, k,
                      x0, y0,
                      y0, k, x0, dau_b3, abs(b3), x0, k, y0 - b3, k, m_ans - k, kq_str, k, m_ans - k,
                      kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
