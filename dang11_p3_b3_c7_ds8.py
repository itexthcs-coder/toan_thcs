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


def bt_dang11_p3_b3_c7_ds8(self):
    # Dạng 11: Tính giá trị hàm số thỏa mãn đẳng thức hàm f(x) + k*f(-x) = ax + b
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        k = random.choice([2, 3])
        x0 = random.randint(1, 5)
        f_x0 = random.randint(-6, 6)
        f_mx0 = random.randint(-6, 6)

        rhs1 = f_x0 + k * f_mx0
        rhs2 = f_mx0 + k * f_x0

        # rhs1 = a*x0 + b, rhs2 = -a*x0 + b => 2b = rhs1 + rhs2
        if (rhs1 + rhs2) % 2 != 0:
            f_mx0 += 1
            rhs1 = f_x0 + k * f_mx0
            rhs2 = f_mx0 + k * f_x0

        b = (rhs1 + rhs2) // 2
        a = (rhs1 - b) // x0
        if a == 0:
            a = 2
            rhs1 = a * x0 + b
            rhs2 = -a * x0 + b
            # Giải lại f_x0, f_mx0 nguyên
            f_x0 = random.randint(-5, 5)
            f_mx0 = random.randint(-5, 5)
            rhs1 = f_x0 + k * f_mx0
            rhs2 = f_mx0 + k * f_x0
            if (rhs1 + rhs2) % 2 != 0:
                f_mx0 += 1
                rhs1 = f_x0 + k * f_mx0
                rhs2 = f_mx0 + k * f_x0
            b = (rhs1 + rhs2) // 2
            a = (rhs1 - b) // x0

        kq_str = str(f_x0)
        dau_b = '+' if b >= 0 else '-'
        str_a = '' if a == 1 else ('-' if a == -1 else str(a))

        noidungcauhoi = ('''Cho hàm số $y = f(x)$ thỏa mãn hệ thức $f(x) + %sf(-x) = %sx %s %s$ với mọi số thực $x$. Tính giá trị của $f(%s)$.'''
                         % (k, str_a, dau_b, abs(b), x0))

        loigiai = ('''Thay $x = %s$ vào hệ thức đã cho, ta được: \\\\
$f(%s) + %sf(%s) = %s \\cdot %s %s %s = %s \\quad (1)$ \\\\
Thay $x = %s$ vào hệ thức đã cho, ta được: \\\\
$f(%s) + %sf(%s) = %s \\cdot (%s) %s %s = %s \\Rightarrow f(%s) = %s - %sf(%s) \\quad (2)$ \\\\
Thế $(2)$ vào $(1)$, ta có: \\\\
$f(%s) + %s\\left(%s - %sf(%s)\\right) = %s$ \\\\
$\\Leftrightarrow f(%s) + %s - %sf(%s) = %s$ \\\\
$\\Leftrightarrow %sf(%s) = %s \\Leftrightarrow f(%s) = %s$.'''
                   % (x0, x0, k, -x0, a, x0, dau_b, abs(b), rhs1,
                      -x0, -x0, k, x0, a, -x0, dau_b, abs(b), rhs2, -x0, rhs2, k, x0,
                      x0, k, rhs2, k, x0, rhs1,
                      x0, k * rhs2, k * k, x0, rhs1,
                      1 - k * k, x0, rhs1 - k * rhs2, x0, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
