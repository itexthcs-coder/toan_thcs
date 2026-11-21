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


def bt_dang16_p4_b5_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        a1 = random.choice([3, 4])
        b1 = random.choice([4, 5])
        c1 = random.choice([5, 6])
        V_khoi = (a1 * b1 * c1) * x**2 * y

        s_coef = random.choice([10, 12, 15])
        while (a1 * b1 * c1) % s_coef != 0:
            a1 = random.choice([3, 4, 5])
            b1 = random.choice([4, 6])
            c1 = random.choice([5, 6])
            V_khoi = (a1 * b1 * c1) * x**2 * y

        h_coef = (a1 * b1 * c1) // s_coef
        S_day2 = s_coef * x * y
        h_khoi2 = h_coef * x

        x_val_str = '2,5'
        x_val_frac = Rational(5, 2)
        h_so = h_coef * x_val_frac
        number = Decimal(float(h_so))
        if h_so.q == 1:
            h_so_str = str(int(h_so))
        else:
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            h_so_str = str(kq).replace('.', ',')

        noidungcauhoi = ('''Trong một xưởng đúc cấu kiện xây dựng, người ta thiết kế hai khối bê tông dạng hình hộp chữ nhật có cùng thể tích. Khối thứ nhất có ba kích thước là $%sx$ (dm), $%sx$ (dm) và $%sy$ (dm) (với $x > 0, y > 0$). Khối thứ hai có diện tích mặt đáy là $S = %s$ ($\\text{dm}^{2}$). \\\\
                         a) Viết đơn thức biểu thị thể tích của khối bê tông thứ nhất và tính chiều cao của khối bê tông thứ hai theo $x$. \\\\
                         b) Khi $x = %s$ (dm), chiều cao của khối bê tông thứ hai bằng bao nhiêu đề-xi-mét?'''
                         % (a1, b1, c1, latex(S_day2), x_val_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Đơn thức biểu thị thể tích của khối bê tông thứ nhất là:
                        \\begin{align*}
                        V = %sx \\cdot %sx \\cdot %sy = %s \\,\\, (\\text{dm}^{3}).
                        \\end{align*}
                        Vì hai khối bê tông có cùng thể tích nên chiều cao của khối bê tông thứ hai là:
                        \\begin{align*}
                        h = V : S = (%s) : (%s) = %s \\,\\, (\\text{dm}).
                        \\end{align*}
                        \\item Khi $x = %s$ (dm), chiều cao của khối bê tông thứ hai là:
                        \\begin{align*}
                        h = %s \\cdot %s = %s \\,\\, (\\text{dm}).
                        \\end{align*}
                        \\end{enumEX}'''
                   % (a1, b1, c1, latex(V_khoi), latex(V_khoi), latex(S_day2), latex(h_khoi2),
                      x_val_str, h_coef, x_val_str, h_so_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
