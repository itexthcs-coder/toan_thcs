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


def bt_dang5_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = randint(12, 42)
        b1 = 90 - a1
        a2 = randint(15, 44)
        b2 = 90 - a2
        k1 = randint(2, 6)
        kq_a = 2 - k1

        c1 = randint(10, 40)
        d1 = 90 - c1
        c2 = randint(18, 43)
        d2 = 90 - c2
        k2 = randint(2, 7)
        kq_b = k2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tính giá trị của các biểu thức sau: \\\\
a) $A = \\dfrac{\\sin %s^\\circ}{\\cos %s^\\circ} + \\tan %s^\\circ \\cdot \\tan %s^\\circ - %s\\cot 45^\\circ$. \\\\
b) $B = \\cos %s^\\circ - \\sin %s^\\circ + %s \\cdot \\dfrac{\\tan %s^\\circ}{\\cot %s^\\circ}$.'''
                         % (str(a1), str(b1), str(a2), str(b2), str(k1),
                            str(c1), str(d1), str(k2), str(c2), str(d2)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Ta có $%s^\\circ + %s^\\circ = 90^\\circ$ nên $\\sin %s^\\circ = \\cos %s^\\circ$. \\\\
Lại có $%s^\\circ + %s^\\circ = 90^\\circ$ nên $\\tan %s^\\circ = \\cot %s^\\circ$, suy ra $\\tan %s^\\circ \\cdot \\tan %s^\\circ = \\tan %s^\\circ \\cdot \\cot %s^\\circ = 1$. \\\\
Và $\\cot 45^\\circ = 1$. Do đó: \\\\
$A = 1 + 1 - %s \\cdot 1 = 2 - %s = %s$. \n
\\item Ta có $%s^\\circ + %s^\\circ = 90^\\circ$ nên $\\sin %s^\\circ = \\cos %s^\\circ$. \\\\
Và $%s^\\circ + %s^\\circ = 90^\\circ$ nên $\\tan %s^\\circ = \\cot %s^\\circ$. \\\\
Thay vào biểu thức $B$, ta được: \\\\
$B = (\\cos %s^\\circ - \\cos %s^\\circ) + %s \\cdot 1 = 0 + %s = %s$. \n
\\end{enumEX} \n'''
                   % (str(a1), str(b1), str(a1), str(b1),
                      str(a2), str(b2), str(b2), str(a2), str(a2), str(b2), str(a2), str(a2),
                      str(k1), str(k1), str(kq_a),
                      str(c1), str(d1), str(d1), str(c1),
                      str(c2), str(d2), str(c2), str(d2),
                      str(c1), str(c1), str(k2), str(k2), str(kq_b)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
