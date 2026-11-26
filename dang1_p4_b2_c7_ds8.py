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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang1_p4_b2_c7_ds8(self):
    # Dạng 1: Giải phương trình chứa phân thức có mẫu số theo quy luật
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        S = random.randint(2018, 2032)
        m1 = random.randint(2000, 2010)
        d = random.choice([2, 3])
        m2 = m1 + d
        m3 = m1 + 2 * d
        m4 = m1 + 3 * d
        m5 = m1 + 4 * d
        m6 = m1 + 5 * d
        
        a1 = S - m1
        a2 = S - m2
        a3 = S - m3
        a4 = S - m4
        a5 = S - m5
        a6 = S - m6
        x_val = -S
        
        noidungcauhoi = ('''Giải phương trình sau: \\\\
$\\frac{x + %s}{%s} + \\frac{x + %s}{%s} + \\frac{x + %s}{%s} = \\frac{x + %s}{%s} + \\frac{x + %s}{%s} + \\frac{x + %s}{%s}$.'''
                         % (a1, m1, a2, m2, a3, m3, a4, m4, a5, m5, a6, m6))
        
        loigiai = ('''Cộng $1$ vào mỗi hạng tử ở cả hai vế của phương trình (tức là cộng $3$ vào mỗi vế), ta được: \\\\
$\\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right) = \\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right)$ \\\\
$\\Leftrightarrow \\frac{x + %s}{%s} + \\frac{x + %s}{%s} + \\frac{x + %s}{%s} = \\frac{x + %s}{%s} + \\frac{x + %s}{%s} + \\frac{x + %s}{%s}$ \\\\
$\\Leftrightarrow (x + %s)\\left(\\frac{1}{%s} + \\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s}\\right) = 0$. \\\\
Vì $\\frac{1}{%s} > \\frac{1}{%s}$, $\\frac{1}{%s} > \\frac{1}{%s}$, $\\frac{1}{%s} > \\frac{1}{%s}$ nên $\\frac{1}{%s} + \\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s} > 0$. \\\\
Do đó $x + %s = 0 \\Leftrightarrow x = %s$. \\\\
Vậy nghiệm của phương trình là $x = %s$.'''
                   % (a1, m1, a2, m2, a3, m3, a4, m4, a5, m5, a6, m6,
                      S, m1, S, m2, S, m3, S, m4, S, m5, S, m6,
                      S, m1, m2, m3, m4, m5, m6,
                      m1, m4, m2, m5, m3, m6, m1, m2, m3, m4, m5, m6,
                      S, x_val,
                      x_val))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
