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




def bt_dang12_p4_b4_c6_ds8(self):
    # Dạng 12: Rút gọn biểu thức phân thức ba biến có điều kiện đối xứng a + b + c = 0
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([2, 3, 4])
        m = random.choice([2, 3, 5])
        
        noidungcauhoi = ("""Cho ba số thực $a, b, c$ đôi một khác nhau và khác $0$ thỏa mãn $a + b + c = 0$. \\\\
        a) Chứng minh rằng $a^2 - b^2 - c^2 = 2bc$. \\\\
        b) Rút gọn và tính giá trị của biểu thức $P = \\left(\\frac{a^2}{a^2 - b^2 - c^2} + \\frac{b^2}{b^2 - c^2 - a^2} + \\frac{c^2}{c^2 - a^2 - b^2}\\right) \\cdot \\frac{%sx + %s}{%sx + %s}$ (với $x \\neq -%s$)."""
                         % (2*k, 2*k*m, 3*k, 3*k*m, m))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Từ giả thiết $a + b + c = 0 \\Rightarrow b + c = -a$. Bình phương hai vế ta được:\\\\
        $$(b + c)^2 = (-a)^2 \\Leftrightarrow b^2 + 2bc + c^2 = a^2 \\Leftrightarrow a^2 - b^2 - c^2 = 2bc.$$ \n
        \\item Tương tự câu a, ta có $b^2 - c^2 - a^2 = 2ca$ và $c^2 - a^2 - b^2 = 2ab$.\\\\
        Mặt khác, từ $a + b + c = 0$ ta biến đổi được:\\\\
        $$a^3 + b^3 + c^3 = (a + b)^3 - 3ab(a + b) + c^3 = (-c)^3 - 3ab(-c) + c^3 = 3abc.$$\\\\
        Do đó tổng trong ngoặc bằng:\\\\
        $$\\frac{a^2}{2bc} + \\frac{b^2}{2ca} + \\frac{c^2}{2ab} = \\frac{a^3 + b^3 + c^3}{2abc} = \\frac{3abc}{2abc} = \\frac{3}{2}.$$\\\\
        Thay vào biểu thức $P$, ta được:\\\\
        $$P = \\frac{3}{2} \\cdot \\frac{%s(x + %s)}{%s(x + %s)} = \\frac{3}{2} \\cdot \\frac{2}{3} = 1.$$ \n
        \\end{enumEX} \n"""
                   % (2*k, m, 3*k, m))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
