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


def bt_dang17_p1_b1_c9_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        gA = random.choice([40, 50, 70, 80])
        gE = (180 - gA) // 2
        he_so = random.choice([2, 3, 4])
        tu = random.choice([2, 3])
        mau = random.choice([3, 4, 5])
        while math.gcd(tu, mau) != 1 or tu == mau:
            mau = random.choice([3, 4, 5])
        ab = tu * he_so
        de = mau * he_so
        da = '$\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $\\frac{%s}{%s}$' % (tu, mau)
        s = [
            '$\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $\\frac{%s}{%s}$' % (mau, tu),
            '$\\Delta ABC$ và $\\Delta DEF$ không đồng dạng với nhau',
            '$\\Delta ABC \\backsim \\Delta EFD$ theo tỉ số đồng dạng $\\frac{%s}{%s}$' % (tu, mau),
            '$\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $1$'
        ]
        das1, das2, das3 = random.sample(s, 3)
        noidungcauhoi = ('Cho $\\Delta ABC$ cân tại $A$ có $\\widehat{A} = %s^\\circ$ và $\\Delta DEF$ cân tại $D$ có $\\widehat{E} = %s^\\circ$. Biết $AB = %s\\text{ cm}$, $DE = %s\\text{ cm}$. Khẳng định nào sau đây là đúng?' % (gA, gE, ab, de))
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = ('Vì $\\Delta ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C} = \\frac{180^\\circ - \\widehat{A}}{2} = \\frac{180^\\circ - %s^\\circ}{2} = %s^\\circ$.\\\\ '
                   'Vì $\\Delta DEF$ cân tại $D$ nên $\\widehat{F} = \\widehat{E} = %s^\\circ$ và $\\widehat{D} = 180^\\circ - 2 \\cdot %s^\\circ = %s^\\circ$.\\\\ '
                   'Suy ra $\\widehat{A} = \\widehat{D}$, $\\widehat{B} = \\widehat{E}$, $\\widehat{C} = \\widehat{F}$.\\\\ '
                   'Mặt khác, $AC = AB = %s\\text{ cm}$ và $DF = DE = %s\\text{ cm}$ nên $\\frac{AB}{DE} = \\frac{AC}{DF} = \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\ '
                   'Tương tự, tỉ số cạnh đáy $\\frac{BC}{EF} = \\frac{%s}{%s}$. Vậy $\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $\\frac{%s}{%s}$.'
                   % (gA, gE, gE, gE, gA, ab, de, ab, de, tu, mau, tu, mau, tu, mau))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
