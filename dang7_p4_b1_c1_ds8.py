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


def bt_dang7_p4_b1_c1_ds8(self):
    # Dạng 7: Biện luận tham số trong hệ số đơn thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tu = random.choice([1, 3])
        a_khong_bac = Rational(tu, 10)
        b_dec = random.choice(['2,4', '2,6', '3,4'])
        b_val = Rational(b_dec.replace(',', '.'))
        a_tong = Rational(-1 + b_val + Rational(tu, 5), 2)

        def fmt_dec(val):
            s = str(float(val)).replace('.', ',')
            return s[:-2] if s.endswith(',0') else s

        noidungcauhoi = ('Cho đơn thức $K = \\left(2a - \\frac{%s}{5}\\right)x^{4}y^{5}z^{2}$ (với $a$ là hằng số). \\\\\n'
                         'a) Tìm giá trị của $a$ để đơn thức $K$ không có bậc. \\\\\n'
                         'b) Tìm giá trị của $a$ để đơn thức $K$ đồng dạng với đơn thức $N = -%sx^{4}y^{5}z^{2}$ và có tổng $K + N = -x^{4}y^{5}z^{2}$.'
                         % (tu, b_dec))

        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Đơn thức $K$ không có bậc khi và chỉ khi $K = 0$, tức là hệ số của $K$ bằng $0$:\n'
                   '\\begin{align*}\n'
                   '2a - \\frac{%s}{5} = 0 \\Leftrightarrow 2a = \\frac{%s}{5} \\Leftrightarrow a = \\frac{%s}{10} = %s.\n'
                   '\\end{align*} \n'
                   '\\item Ta có $K + N = \\left(2a - \\frac{%s}{5} - %s\\right)x^{4}y^{5}z^{2}$. Theo đề bài, ta có:\n'
                   '\\begin{align*}\n'
                   '2a - %s - %s = -1 \\Leftrightarrow 2a = %s \\Leftrightarrow a = %s.\n'
                   '\\end{align*}\n'
                   'Với $a = %s$, hệ số của $K$ là $%s \\neq 0$ nên $K$ và $N$ đồng dạng. Vậy $a = %s$. \n'
                   '\\end{enumEX} \n'
                   % (tu, tu, tu, fmt_dec(a_khong_bac),
                      tu, b_dec, fmt_dec(Rational(tu, 5)), b_dec,
                      fmt_dec(-1 + b_val + Rational(tu, 5)),
                      fmt_dec(a_tong),
                      fmt_dec(a_tong),
                      fmt_dec(2 * a_tong - Rational(tu, 5)),
                      fmt_dec(a_tong)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
