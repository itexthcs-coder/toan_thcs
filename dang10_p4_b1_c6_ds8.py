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


def bt_dang10_p4_b1_c6_ds8(self):
    # Dạng 10: Tìm giá trị nguyên của x để hai phân thức đồng thời nhận giá trị nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # A = (x + 5)/(x - 1) = 1 + 6/(x - 1) -> x in {-5, -2, -1, 0, 2, 3, 4, 7}
        # B = (2x - 1)/(x + 2) = 2 - 5/(x + 2) -> x in {-7, -3, -1, 3}
        # Giao nhau: {-1, 3}
        k = random.choice([1, 2])
        if k == 1:
            pA, aA, rA = 1, 1, 6
            cA = pA * aA + rA # 7 -> A = (x + 5)/(x - 1)
            tuA = 'x + 5'
            mauA = 'x - 1'
            xA_list = [-5, -2, -1, 0, 2, 3, 4, 7]
            tuB = '2x - 1'
            mauB = 'x + 2'
            rB = 5
            xB_list = [-7, -3, -1, 3]
            giao_str = '-1; 3'
            sol_detail = ('- Phân thức $A = \\dfrac{x + 5}{x - 1} = 1 + \\dfrac{6}{x - 1}$ ($x \\neq 1$) nhận giá trị nguyên khi $x - 1 \\in \\text{Ư}(6) = \\{-6; -3; -2; -1; 1; 2; 3; 6\\}$, suy ra $x \\in \\{-5; -2; -1; 0; 2; 3; 4; 7\\}$.\\\n'
                          '- Phân thức $B = \\dfrac{2x - 1}{x + 2} = 2 - \\dfrac{5}{x + 2}$ ($x \\neq -2$) nhận giá trị nguyên khi $x + 2 \\in \\text{Ư}(5) = \\{-5; -1; 1; 5\\}$, suy ra $x \\in \\{-7; -3; -1; 3\\}$.\\\n'
                          '- Đối chiếu hai tập hợp trên, các giá trị nguyên của $x$ để cả hai phân thức cùng nhận giá trị nguyên là $x \\in \\{-1; 3\\}$.')
        else:
            tuA = 'x + 4'
            mauA = 'x - 2'
            tuB = '3x + 2'
            mauB = 'x + 1'
            sol_detail = ('- Phân thức $A = \\dfrac{x + 4}{x - 2} = 1 + \\dfrac{6}{x - 2}$ ($x \\neq 2$) nhận giá trị nguyên khi $x - 2 \\in \\text{Ư}(6) = \\{-6; -3; -2; -1; 1; 2; 3; 6\\}$, suy ra $x \\in \\{-4; -1; 0; 1; 3; 4; 5; 8\\}$.\\\n'
                          '- Phân thức $B = \\dfrac{3x + 2}{x + 1} = 3 - \\dfrac{1}{x + 1}$ ($x \\neq -1$) nhận giá trị nguyên khi $x + 1 \\in \\text{Ư}(1) = \\{-1; 1\\}$, suy ra $x \\in \\{-2; 0\\}$.\\\n'
                          '- Đối chiếu hai tập hợp trên, giá trị nguyên duy nhất của $x$ để cả hai phân thức cùng nhận giá trị nguyên là $x = 0$.')
        
        noidungcauhoi = ('Tìm tất cả các số nguyên $x$ để cả hai phân thức $A = \\dfrac{%s}{%s}$ và $B = \\dfrac{%s}{%s}$ đều nhận giá trị nguyên.'
                         % (tuA, mauA, tuB, mauB))
        
        loigiai = sol_detail

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
