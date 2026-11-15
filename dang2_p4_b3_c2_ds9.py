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


def bt_dang2_p4_b3_c2_ds9(self):
    while True:
        m1, m2 = random.sample([2, 3, 4, 5], 2)
        M = math.lcm(m1, m2)
        k = random.choice([2, 3, 4])
        b0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        a1 = random.choice([2, 3, 4, 5])
        b1 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])
        c = random.choice([1, 2, 3, 4])
        a2 = random.choice([1, 2, 3, 4])
        b2 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])

        q1, q2 = M // m1, M // m2
        he_so_x = M * k - q1 * a1 - M * c + q2 * a2
        hang_so = -q2 * b2 - M * k * b0 + q1 * b1
        if he_so_x != 0 and hang_so != 0:
            nghiem = Rational(hang_so, he_so_x)
            break

    dau = random.choice(['>', '<', r'\ge', r'\le'])
    map_dau = {r'\le': r'\ge', r'\ge': r'\le', '<': '>', '>': '<'}
    dau_kq = dau if he_so_x > 0 else map_dau[dau]

    bt0 = latex(x + b0)
    bt1 = latex(a1 * x + b1)
    bt2 = latex(a2 * x + b2)
    cx_str = "x" if c == 1 else f"{c}x"

    noidungcauhoi = (
        f"Giải bất phương trình: ${k}({bt0}) - \\dfrac{{{bt1}}}{{{m1}}} {dau} {cx_str} - \\dfrac{{{bt2}}}{{{m2}}}$."
    )

    loigiai = (
        f"Quy đồng mẫu số hai vế với mẫu chung là ${M}$ và khử mẫu dương, ta được:\\\n"
        f"${M * k}({bt0}) - {q1}({bt1}) {dau} {M * c}x - {q2}({bt2})$\\\n"
        f"${latex((M * k - q1 * a1) * x + (M * k * b0 - q1 * b1))} {dau} {latex((M * c - q2 * a2) * x - q2 * b2)}$\\\n"
        f"${latex(he_so_x * x)} {dau} {hang_so}$\\\n"
        f"$x {dau_kq} {latex(nghiem)}$.\\\n"
        f"Vậy nghiệm của bất phương trình là $x {dau_kq} {latex(nghiem)}$."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
