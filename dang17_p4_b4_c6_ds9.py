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


def bt_dang17_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (10, 15, 6),
            (6, 12, 4),
            (12, 24, 8),
            (15, 30, 10),
            (20, 30, 12)
        ])
        t1, t2, t_chung = bo_so
        chenh = t2 - t1

        b_pt = chenh - 2 * t_chung
        c_pt = -t_chung * chenh
        delta = b_pt**2 - 4 * c_pt
        can_delta = int(math.isqrt(delta))
        nghiem_am = (-b_pt - can_delta) // 2

        noidungcauhoi = ('''Một bể chứa nước sạch của khu dân cư có lắp hai vòi cấp nước. Nếu mở cả hai vòi cùng chảy vào bể cạn thì sau $%s$ giờ đầy bể. Nếu mở từng vòi chảy riêng thì vòi thứ nhất chảy đầy bể nhanh hơn vòi thứ hai là $%s$ giờ. \\\\
a) Tính thời gian vòi thứ nhất chảy riêng một mình đầy bể. \\\\
b) Tính thời gian vòi thứ hai chảy riêng một mình đầy bể.'''
                         %(latex(t_chung), latex(chenh)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $1$ giờ, cả hai vòi cùng chảy được $\\frac{1}{%s}$ bể. \\\\
Gọi $x$ (giờ) là thời gian vòi thứ nhất chảy riêng đầy bể. Điều kiện: $x > 0$. \\\\
Thời gian vòi thứ hai chảy riêng đầy bể là $x + %s$ (giờ). \\\\
Trong $1$ giờ, vòi thứ nhất chảy được $\\frac{1}{x}$ bể và vòi thứ hai chảy được $\\frac{1}{x + %s}$ bể. \\\\
Theo đề bài, ta có phương trình: \\\\
$\\frac{1}{x} + \\frac{1}{x + %s} = \\frac{1}{%s}$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$%s = 0$. \\\\
Ta có: $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot (%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{-%s - %s}{2} = %s$ (loại); \\quad $x_2 = \\frac{-%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy vòi thứ nhất chảy riêng một mình thì sau $%s$ giờ sẽ đầy bể.
\\item Thời gian vòi thứ hai chảy riêng một mình đầy bể là: $%s + %s = %s$ (giờ).
\\end{enumEX}'''
                   %(latex(t_chung), latex(chenh), latex(chenh), latex(chenh), latex(t_chung),
                     latex(x**2 + b_pt * x + c_pt),
                     latex(b_pt), latex(c_pt), latex(delta), latex(can_delta),
                     latex(b_pt), latex(can_delta), latex(nghiem_am), latex(b_pt), latex(can_delta), latex(t1),
                     latex(t1),
                     latex(t1), latex(chenh), latex(t2)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
