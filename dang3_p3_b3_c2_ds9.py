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
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang3_p3_b3_c2_ds9(self):
    x = symbols('x')
    m1, m2 = random.sample([2, 3, 4, 5, 6], 2)
    bcnn = math.lcm(m1, m2)
    a1 = randint(1, 4)
    b1 = randint(-7, 7)
    a2 = randint(1, 4)
    b2 = randint(-7, 7)
    while a1 * (bcnn // m1) == a2 * (bcnn // m2):
        a2 = randint(1, 5)
        
    t1 = a1 * (bcnn // m1)
    c1 = b1 * (bcnn // m1)
    t2 = a2 * (bcnn // m2)
    c2 = b2 * (bcnn // m2)
    
    nghiem_bien = Rational(c2 - c1, t1 - t2)
    if t1 - t2 > 0:
        if nghiem_bien <= 1:
            b2 += (t1 - t2) * randint(3, 8)
            c2 = b2 * (bcnn // m2)
            nghiem_bien = Rational(c2 - c1, t1 - t2)
        ans = math.ceil(float(nghiem_bien)) - 1
        dau_kq = "<"
        loai_nghiem = "nguyên dương"
    else:
        if nghiem_bien >= -1:
            b2 += abs(t1 - t2) * randint(4, 10)
            c2 = b2 * (bcnn // m2)
            nghiem_bien = Rational(c2 - c1, t1 - t2)
        ans = abs(math.floor(float(nghiem_bien)) + 1)
        dau_kq = ">"
        loai_nghiem = "nguyên âm"
        
    kq_str = str(ans)
    tu1_str = f"{a1 if a1>1 else ''}x {f'+ {b1}' if b1>=0 else f'- {-b1}'}"
    tu2_str = f"{a2 if a2>1 else ''}x {f'+ {b2}' if b2>=0 else f'- {-b2}'}"
    
    noidungcauhoi = ('''Bất phương trình $\\dfrac{%s}{%s} < \\dfrac{%s}{%s}$ có bao nhiêu nghiệm %s?'''
                     % (tu1_str, m1, tu2_str, m2, loai_nghiem))
    
    loigiai = ('''Quy đồng khử mẫu hai vế với mẫu chung là $%s$, ta được: \\
               $%s(%s) < %s(%s)$ \\
               $%sx %s < %sx %s$ \\
               $%sx < %s$ \\
               $x %s %s$. \\
               Suy ra bất phương trình có tất cả $%s$ nghiệm %s.'''
               % (bcnn,
                  bcnn//m1, tu1_str, bcnn//m2, tu2_str,
                  t1, f"+ {c1}" if c1>=0 else f"- {-c1}", t2, f"+ {c2}" if c2>=0 else f"- {-c2}",
                  t1 - t2, c2 - c1,
                  dau_kq, latex(nghiem_bien),
                  kq_str, loai_nghiem))
    
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
