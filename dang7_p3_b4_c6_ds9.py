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


def bt_dang7_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_ghe = [(20, 16, 4, 4), (24, 15, 4, 3), (15, 16, 3, 4), (25, 12, 5, 3), (18, 20, 3, 4)]
        day_bd, ghe_moi_day, bot_day, them_ghe = random.choice(bo_ghe)
        tong_ghe = day_bd * ghe_moi_day
        c_val = (tong_ghe * bot_day) // them_ghe
        delta_val = bot_day**2 + 4 * c_val
        sqrt_d = int(math.isqrt(delta_val))
        x1 = (bot_day - sqrt_d) // 2
        x2 = (bot_day + sqrt_d) // 2

        noidungcauhoi = ('''Một hội trường có $%s$ ghế ngồi được xếp thành các dãy đều nhau. Nếu bớt đi $%s$ dãy ghế và mỗi dãy còn lại xếp thêm $%s$ ghế thì tổng số ghế trong hội trường không đổi. Hỏi ban đầu hội trường có bao nhiêu dãy ghế?'''
                         % (str(tong_ghe), str(bot_day), str(them_ghe)))

        loigiai = ('''Gọi số dãy ghế ban đầu của hội trường là $x$ (dãy). Điều kiện: $x \\in \\mathbb{N}^*$, $x > %s$.\\\\
                   Khi đó, số ghế trong mỗi dãy ban đầu là $\\dfrac{%s}{x}$ (ghế).\\\\
                   Nếu bớt đi $%s$ dãy ghế thì số dãy ghế còn lại là $x - %s$ (dãy), và số ghế mỗi dãy lúc này là $\\dfrac{%s}{x} + %s$ (ghế).\\\\
                   Vì tổng số ghế trong hội trường không đổi nên ta có phương trình:\\\\
                   $(x - %s)\\left(\\dfrac{%s}{x} + %s\\right) = %s$\\\\
                   $%s + %sx - \\dfrac{%s}{x} - %s = %s$\\\\
                   $%sx - \\dfrac{%s}{x} - %s = 0$.\\\\
                   Nhân cả hai vế với $x$ để khử mẫu, ta được:\\\\
                   $%sx^2 - %sx - %s = 0$ hay $x^2 - %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{%s - %s}{2} = %s$ (loại); $x_2 = \\dfrac{%s + %s}{2} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy ban đầu hội trường có $%s$ dãy ghế.'''
                   % (str(bot_day), str(tong_ghe), str(bot_day), str(bot_day), str(tong_ghe), str(them_ghe),
                      str(bot_day), str(tong_ghe), str(them_ghe), str(tong_ghe),
                      str(tong_ghe), str(them_ghe), str(tong_ghe * bot_day), str(bot_day * them_ghe), str(tong_ghe),
                      str(them_ghe), str(tong_ghe * bot_day), str(bot_day * them_ghe),
                      str(them_ghe), str(bot_day * them_ghe), str(tong_ghe * bot_day), str(bot_day), str(c_val),
                      str(bot_day), str(c_val), str(delta_val), str(sqrt_d),
                      str(bot_day), str(sqrt_d), str(x1), str(bot_day), str(sqrt_d), str(x2), str(day_bd)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(day_bd))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
