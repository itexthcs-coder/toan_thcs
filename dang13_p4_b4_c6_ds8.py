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




def bt_dang13_p4_b4_c6_ds8(self):
    # Dạng 13: Tìm hệ số để phép chia phân thức rút gọn thành đa thức bậc nhất
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Q = (2x^3 - 3x^2 + ax + b)/(x^2 - 1) : (2x - 1)/(x + 1) = (2x^3 - 3x^2 + ax + b)/((x - 1)(2x - 1))
        # Để Q là đa thức bậc nhất (x + k): (x - 1)(2x - 1)(x + k) = (2x^2 - 3x + 1)(x + k) = 2x^3 + (2k - 3)x^2 + (1 - 3k)x + k
        # So sánh hệ số x^2: 2k - 3 = -3 => k = 0!
        # Vậy đa thức bậc nhất là x, và a = 1, b = 0. Tổng quát với c: (x - 1)(cx - 1)x = cx^3 - (c + 1)x^2 + x
        c = random.choice([2, 3, 4])
        
        noidungcauhoi = ("""Cho biểu thức $Q = \\frac{%sx^3 - %sx^2 + ax + b}{x^2 - 1} : \\frac{%sx - 1}{x + 1}$ với $x \\neq \\pm 1$ và $x \\neq \\frac{1}{%s}$. \\\\
        a) Viết biểu thức $Q$ dưới dạng một phân thức duy nhất có mẫu thức là $(x - 1)(%sx - 1)$. \\\\
        b) Tìm các hệ số $a, b$ để biểu thức $Q$ rút gọn thành một đa thức bậc nhất."""
                         % (c, c + 1, c, c, c))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Với $x \\neq \\pm 1$ và $x \\neq \\frac{1}{%s}$, ta có:\\\\
        $$Q = \\frac{%sx^3 - %sx^2 + ax + b}{(x - 1)(x + 1)} \\cdot \\frac{x + 1}{%sx - 1} = \\frac{%sx^3 - %sx^2 + ax + b}{(x - 1)(%sx - 1)}.$$ \n
        \\item Mẫu thức $(x - 1)(%sx - 1) = %sx^2 - %sx + 1$. Để $Q$ rút gọn thành một đa thức bậc nhất (có hệ số cao nhất là $\\frac{%s}{%s} = 1$) thì đa thức bậc nhất đó có dạng $x + k$, tức là:\\\\
        $$%sx^3 - %sx^2 + ax + b = (%sx^2 - %sx + 1)(x + k) = %sx^3 + (%sk - %s)x^2 + (1 - %sk)x + k.$$\\\\
        Đồng nhất hệ số của $x^2$, ta có $%sk - %s = -%s \\Rightarrow k = 0$.\\\\
        Từ đó suy ra $a = 1 - %s \\cdot 0 = 1$ và $b = 0$. \n
        \\end{enumEX} \n"""
                   % (c, c, c + 1, c, c, c + 1, c,
                      c, c, c + 1, c, c,
                      c, c + 1, c, c + 1, c, c, c + 1, c + 1,
                      c, c + 1, c + 1, c + 1))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
