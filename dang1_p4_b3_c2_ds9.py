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


def bt_dang1_p4_b3_c2_ds9(self):
    while True:
        m1, m2, m3 = random.sample([2, 3, 4, 5, 6], 3)
        M = math.lcm(m1, m2, m3)
        a1 = random.choice([-4, -3, -2, 2, 3, 4])
        b1 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])
        a2 = random.choice([-4, -3, -2, 1, 2, 3, 4])
        b2 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])
        a3 = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        b3 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])

        k1, k2, k3 = M // m1, M // m2, M // m3
        he_so_x = k1 * a1 - k2 * a2 - k3 * a3
        hang_so = k3 * b3 - k1 * b1 + k2 * b2
        if he_so_x != 0 and hang_so != 0:
            nghiem = Rational(hang_so, he_so_x)
            break

    dau = random.choice([r'\le', r'\ge', '<', '>'])
    map_dau = {r'\le': r'\ge', r'\ge': r'\le', '<': '>', '>': '<'}
    dau_kq = dau if he_so_x > 0 else map_dau[dau]

    vt1 = latex(a1 * x + b1)
    vt2 = latex(a2 * x + b2)
    vp = latex(a3 * x + b3)

    buoc1_vt = f"{k1}({vt1}) - {k2}({vt2})"
    buoc1_vp = f"{k3}({vp})"

    rutgon_vt = latex((k1 * a1 - k2 * a2) * x + (k1 * b1 - k2 * b2))
    rutgon_vp = latex(k3 * a3 * x + k3 * b3)

    noidungcauhoi = (
        f"Giải bất phương trình: $\\dfrac{{{vt1}}}{{{m1}}} - \\dfrac{{{vt2}}}{{{m2}}} {dau} \\dfrac{{{vp}}}{{{m3}}}$."
    )

    loigiai = (
        f"Quy đồng mẫu số hai vế với mẫu chung là ${M}$, ta được:\\\n"
        f"$\\dfrac{{{buoc1_vt}}}{{{M}}} {dau} \\dfrac{{{buoc1_vp}}}{{{M}}}$\\\n"
        f"Nhân cả hai vế của bất phương trình với ${M} > 0$, ta được:\\\n"
        f"${buoc1_vt} {dau} {buoc1_vp}$\\\n"
        f"${rutgon_vt} {dau} {rutgon_vp}$\\\n"
        f"${latex(he_so_x * x)} {dau} {hang_so}$\\\n"
        f"$x {dau_kq} {latex(nghiem)}$.\\\n"
        f"Vậy nghiệm của bất phương trình là $x {dau_kq} {latex(nghiem)}$."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
