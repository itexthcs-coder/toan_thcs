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




def bt_dang15_p4_b4_c6_ds8(self):
    # Dạng 15: So sánh giá trị của hai biểu thức phân thức bằng phép chia và xét hiệu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4])
        
        tu_M1 = sp.expand(x**2 + a*x)
        mau_M1 = sp.expand((x + a)**2)
        
        tu_N1 = sp.expand(x**2 - 1)
        mau_N1 = sp.expand((x - 1)**2)
        
        # M = x(x+a)/(x+a)^2 : x/(x+a) = x/(x+a) * (x+a)/x = 1
        # N = (x-1)(x+1)/(x-1)^2 * (x-1)/(x+1) = 1 -> chỉnh N để N = x/(x + a + 1) để so sánh!
        # Chọn N = (x^2 - 1)/((x - 1)(x + a + 1)) * x/(x + 1) = x/(x + a + 1)
        tu_N = sp.expand(x**2 - 1)
        mau_N = sp.expand((x - 1)*(x + a + 1))
        
        noidungcauhoi = ("""Cho hai biểu thức $M = \\frac{%s}{%s} : \\frac{x}{x + %s}$ và $N = \\frac{%s}{%s} \\cdot \\frac{x}{x + 1}$ với $x > 0$ và $x \\neq 1$. \\\\
        a) Rút gọn hai biểu thức $M$ và $N$. \\\\
        b) Tính tỉ số $\\frac{M}{N}$ và so sánh $M$ với $N$ khi $x > 0, x \\neq 1$."""
                         % (latex(tu_M1), latex(mau_M1), a, latex(tu_N), latex(mau_N)))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Với $x > 0$ và $x \\neq 1$, ta rút gọn $M$ và $N$:\\\\
        $$M = \\frac{x(x + %s)}{(x + %s)^2} \\cdot \\frac{x + %s}{x} = 1.$$\\\\
        $$N = \\frac{(x - 1)(x + 1)}{(x - 1)(x + %s)} \\cdot \\frac{x}{x + 1} = \\frac{x}{x + %s}.$$ \n
        \\item Tỉ số $\\frac{M}{N}$ là:\\\\
        $$\\frac{M}{N} = 1 : \\frac{x}{x + %s} = \\frac{x + %s}{x} = 1 + \\frac{%s}{x}.$$\\\\
        Vì $x > 0$ nên $\\frac{%s}{x} > 0$, suy ra $\\frac{M}{N} = 1 + \\frac{%s}{x} > 1$.\\\\
        Mặt khác $N = \\frac{x}{x + %s} > 0$ (do $x > 0$), nên từ $\\frac{M}{N} > 1$ suy ra $M > N$. \n
        \\end{enumEX} \n"""
                   % (a, a, a, a + 1, a + 1, a + 1, a + 1, a + 1, a + 1, a + 1, a + 1))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
