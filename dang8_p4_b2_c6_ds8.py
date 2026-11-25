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


def bt_dang8_p4_b2_c6_ds8(self):
    # Dạng 8: Tìm giá trị nguyên của x để hai phân thức đồng thời nhận giá trị nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([1, 2, 3])
        r1 = random.choice([4, 6])
        r2 = random.choice([3, 5])
        tu_p = latex(expand(3 * (x - a) + r1))
        tu_q = latex(expand(2 * x * (x - a) + r2))
        mau_str = latex(x - a)

        uoc1 = sorted([d for d in range(-r1, r1 + 1) if d != 0 and r1 % d == 0])
        uoc2 = sorted([d for d in range(-r2, r2 + 1) if d != 0 and r2 % d == 0])
        uoc_chung = sorted(list(set(uoc1).intersection(set(uoc2))))
        tap_x1 = [a + d for d in uoc1]
        tap_x_chung = [a + d for d in uoc_chung]

        noidungcauhoi = ('Cho hai phân thức $P = \\dfrac{%s}{%s}$ và $Q = \\dfrac{%s}{%s}$ (với $x \\neq %s$).\\\n'
                         'a) Tìm tập hợp các giá trị nguyên của $x$ để phân thức $P$ nhận giá trị nguyên.\\\n'
                         'b) Tìm tất cả các giá trị nguyên của $x$ để cả hai phân thức $P$ và $Q$ đồng thời nhận giá trị nguyên.'
                         % (tu_p, mau_str, tu_q, mau_str, a))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Ta có $P = \\dfrac{3(%s) + %s}{%s} = 3 + \\dfrac{%s}{%s}$.\\\n'
                   'Với $x \\in \\mathbb{Z}$ ($x \\neq %s$), $P \\in \\mathbb{Z} \\Leftrightarrow (%s) \\in \\text{Ư}(%s) = \\{%s\\}$.\\\n'
                   'Suy ra tập hợp các giá trị nguyên của $x$ để $P$ nguyên là $S_1 = \\{%s\\}$.\n'
                   '\\item Ta có $Q = \\dfrac{2x(%s) + %s}{%s} = 2x + \\dfrac{%s}{%s}$.\\\n'
                   'Với $x \\in \\mathbb{Z}$ ($x \\neq %s$), $Q \\in \\mathbb{Z} \\Leftrightarrow (%s) \\in \\text{Ư}(%s) = \\{%s\\}$.\\\n'
                   'Để cả hai phân thức $P$ và $Q$ đồng thời nhận giá trị nguyên thì $(%s)$ phải là ước chung của $%s$ và $%s$, tức là $(%s) \\in \\{-1; 1\\}$.\\\n'
                   'Vậy $x \\in \\{%s\\}$.\n'
                   '\\end{enumEX}'
                   % (mau_str, r1, mau_str, r1, mau_str, a, mau_str, r1, ', '.join(map(str, uoc1)), ', '.join(map(str, tap_x1)),
                      mau_str, r2, mau_str, r2, mau_str, a, mau_str, r2, ', '.join(map(str, uoc2)), mau_str, r1, r2, mau_str, ', '.join(map(str, tap_x_chung))))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
