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


def bt_dang19_p1_b2_c7_ds8(self):
    # Dạng 19: Bài toán tìm số tự nhiên có hai chữ số
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Số ab = 10x + (x + d), đổi chỗ ba = 10(x + d) + x
        x_chuc, d, tu, mau = random.choice([
            (4, 4, 7, 4),   # 48 và 84: 84/48 = 7/4
            (2, 4, 31, 13), # 26 và 62: 62/26 = 31/13
            (3, 3, 7, 4),   # 36 và 63: 63/36 = 7/4
            (1, 7, 81, 18)  # 18 và 81: 81/18 = 9/2
        ])
        if (x_chuc, d) == (1, 7):
            tu, mau = 9, 2
        y_dv = x_chuc + d
        so_ban_dau = 10 * x_chuc + y_dv
        so_moi = 10 * y_dv + x_chuc
        
        noidungcauhoi = "Tìm một số tự nhiên có hai chữ số, biết rằng chữ số hàng đơn vị lớn hơn chữ số hàng chục là $%s$ đơn vị và nếu đổi chỗ hai chữ số cho nhau thì được số mới bằng $\\dfrac{%s}{%s}$ số ban đầu." % (d, tu, mau)
        da = "$%s$" % so_ban_dau
        s = [
            "$%s$" % so_moi,
            "$%s$" % (so_ban_dau - 11),
            "$%s$" % (so_ban_dau + 11)
        ]
        loigiai = "Gọi $x$ là chữ số hàng chục của số cần tìm ($x \\in \\mathbb{N}^*$, $1 \\le x \\le %s$).\\\\Chữ số hàng đơn vị là $x + %s$.\\\\Số tự nhiên ban đầu là $10x + (x + %s) = 11x + %s$.\\\\Khi đổi chỗ hai chữ số cho nhau, ta được số mới là $10(x + %s) + x = 11x + %s$.\\\\Theo đề bài, ta có phương trình:\\\\$11x + %s = \\dfrac{%s}{%s}(11x + %s)$\\\\$%s(11x + %s) = %s(11x + %s)$\\\\$%sx + %s = %sx + %s$\\\\$%sx = %s$\\\\$x = %s$ (thỏa mãn điều kiện).\\\\Vậy số tự nhiên cần tìm là $%s$." % (
            9 - d, d, d, d, d, 10 * d,
            10 * d, tu, mau, d,
            mau, 10 * d, tu, d,
            11 * mau, 10 * d * mau, 11 * tu, d * tu,
            11 * (tu - mau), 10 * d * mau - d * tu, x_chuc, so_ban_dau
        )

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    da_d = ('\\True ' + str(da))
    list_1 = [da_d, str(das1), str(das2), str(das3)]
    random.shuffle(list_1)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
