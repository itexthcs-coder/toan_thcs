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




def bt_dang2_p4_b4_c6_ds8(self):
    # Dạng 2: Tìm phân thức chưa biết trong hệ hai đẳng thức nhân và chia chứa hằng đẳng thức bậc ba
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(2, 4)
        b = random.choice([2, 3])
        
        tu_A1 = sp.expand(x**2 - a*x + a**2)
        mau_A1 = sp.expand(x - a)
        tu_B1 = sp.expand(x**3 + a**3)
        mau_B1 = sp.expand(x**2 - a**2)
        
        tu_A2 = sp.expand((b*x)**2 - 1)
        mau_A2 = sp.expand((b*x)**3 - 1)
        tu_B2 = sp.expand(b*x + 1)
        mau_B2 = sp.expand(b**2 * x**2 + b*x + 1)
        
        noidungcauhoi = ("""Tìm hai phân thức $P$ và $Q$ (với các mẫu thức đều khác $0$) thỏa mãn các đẳng thức sau: \\\\
        a) $P \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
        b) $\\frac{%s}{%s} : Q = \\frac{%s}{%s}$."""
                         % (latex(tu_A1), latex(mau_A1), latex(tu_B1), latex(mau_B1),
                            latex(tu_A2), latex(mau_A2), latex(tu_B2), latex(mau_B2)))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Từ đẳng thức đã cho, ta có:\\\\
        $$P = \\frac{%s}{%s} : \\frac{%s}{%s} = \\frac{(x + %s)(%s)}{(x - %s)(x + %s)} \\cdot \\frac{x - %s}{%s} = 1.$$ \n
        \\item Từ đẳng thức đã cho, ta có:\\\\
        $$Q = \\frac{%s}{%s} : \\frac{%s}{%s} = \\frac{(%s)(%s)}{(%s)(%s)} \\cdot \\frac{%s}{%s} = 1.$$ \n
        \\end{enumEX} \n"""
                   % (latex(tu_B1), latex(mau_B1), latex(tu_A1), latex(mau_A1),
                      a, latex(tu_A1), a, a, a, latex(tu_A1),
                      latex(tu_A2), latex(mau_A2), latex(tu_B2), latex(mau_B2),
                      latex(b*x - 1), latex(b*x + 1), latex(b*x - 1), latex(mau_B2),
                      latex(mau_B2), latex(tu_B2)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
