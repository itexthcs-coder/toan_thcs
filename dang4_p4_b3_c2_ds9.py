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


def bt_dang4_p4_b3_c2_ds9(self):
    while True:
        a = random.randint(2, 6)
        n = random.randint(a**2 + 1, a**2 + 7)
        if math.isqrt(n)**2 != n:
            break
    b = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    c = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    while c == b:
        c = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    dau = random.choice([r'\ge', r'\le', '>', '<'])
    map_dau = {r'\le': r'\ge', r'\ge': r'\le', '<': '>', '>': '<'}
    dau_kq = map_dau[dau]

    he_so = a - sqrt(n)
    vp_moi = c - b
    nghiem = simplify(vp_moi / he_so)
    dau_b = f"+ {b}" if b > 0 else f"- {-b}"

    noidungcauhoi = (
        f"Giải bất phương trình: $({a} - \\sqrt{{{n}}})x {dau_b} {dau} {c}$."
    )

    loigiai = (
        f"Ta có: $({a} - \\sqrt{{{n}}})x {dau_b} {dau} {c}$\\\n"
        f"$({a} - \\sqrt{{{n}}})x {dau} {vp_moi}$\\\n"
        f"Vì ${a} = \\sqrt{{{a**2}}} < \\sqrt{{{n}}}$ nên ${a} - \\sqrt{{{n}}} < 0$.\\\n"
        f"Chia cả hai vế của bất phương trình cho số âm ${a} - \\sqrt{{{n}}}$ và đổi chiều bất đẳng thức, ta được:\\\n"
        f"$x {dau_kq} \\dfrac{{{vp_moi}}}{{{a} - \\sqrt{{{n}}}}}$\\\n"
        f"$x {dau_kq} {latex(nghiem)}$.\\\n"
        f"Vậy nghiệm của bất phương trình là $x {dau_kq} {latex(nghiem)}$."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
