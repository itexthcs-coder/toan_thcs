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


def bt_dang1_p4_b5_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y, z = symbols('x y z')
        b = random.choice([-9, -8, -7, -6])
        q = random.choice([-5, -4, -3, 3, 4, 5])
        a = b * q

        n_max = random.choice([3, 4])
        m_A = 2 * n_max
        k_A = n_max + 1
        p_A = random.choice([5, 6, 7])

        A = a * x**m_A * y**k_A * z**p_A
        B_nmax = b * x**(2 * n_max) * y**(n_max + 1) * z**4
        Q_nmax = q * z**(p_A - 4)

        ds_n = '; '.join([str(i) for i in range(1, n_max + 1)])

        noidungcauhoi = ('''Cho đơn thức $A = %s$ và đơn thức $B = %sx^{2n}y^{n+1}z^{4}$ với $n$ là số nguyên dương. \\\\
                         a) Tìm tất cả các giá trị nguyên dương của $n$ để đơn thức $A$ chia hết cho đơn thức $B$. \\\\
                         b) Với giá trị nguyên dương lớn nhất của $n$ vừa tìm được, hãy thực hiện phép chia $A : B$.'''
                         % (latex(A), b))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Để đơn thức $A = %s$ chia hết cho đơn thức $B = %sx^{2n}y^{n+1}z^{4}$ thì số mũ của mỗi biến trong $B$ phải không lớn hơn số mũ của biến đó trong $A$, tức là:
                        \\begin{align*}
                        \\begin{cases} 2n \\le %s \\\\ n + 1 \\le %s \\\\ 4 \\le %s \\end{cases} \\Leftrightarrow \\begin{cases} n \\le %s \\\\ n \\le %s \\end{cases} \\Leftrightarrow n \\le %s.
                        \\end{align*}
                        Vì $n$ là số nguyên dương nên $n \\in \\{%s\\}$.
                        \\item Giá trị nguyên dương lớn nhất của $n$ là $n = %s$. Khi đó $B = %s$ và:
                        \\begin{align*}
                        A : B = (%s) : (%s) = %s.
                        \\end{align*}
                        \\end{enumEX}'''
                   % (latex(A), b, m_A, k_A, p_A, n_max, n_max, n_max, ds_n,
                      n_max, latex(B_nmax), latex(A), latex(B_nmax), latex(Q_nmax)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
