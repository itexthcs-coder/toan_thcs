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


def bt_dang17_p4_b1_c6_ds8(self):
    # Dạng 17: Bài toán làm chung - làm riêng công việc trong xây dựng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x_val = random.choice([10, 12, 15])
        diff_d = random.choice([5, 6, 8])
        y_val = x_val + diff_d
        fr_sum = Fraction(1, x_val) + Fraction(1, y_val)
        pct = (Decimal(fr_sum.numerator * 100) / Decimal(fr_sum.denominator)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        pct_str = str(pct).replace('.', ',')
        
        noidungcauhoi = ('Hai đội công nhân cùng tham gia thi công lát gạch vỉa hè một tuyến phố. Nếu làm riêng thì đội thứ nhất hoàn thành toàn bộ công việc trong $x$ ngày ($x > 0$), còn đội thứ hai cần nhiều hơn đội thứ nhất $%s$ ngày mới hoàn thành công việc.\\\n'
                         'a) Viết các phân thức biểu thị khối lượng công việc mỗi đội làm được trong $1$ ngày.\\\n'
                         'b) Nếu đội thứ nhất làm riêng mất $%s$ ngày thì xong công việc, hỏi trong $1$ ngày cả hai đội cùng làm sẽ hoàn thành được bao nhiêu phần trăm khối lượng công việc (làm tròn đến hàng phần mười)?'
                         % (diff_d, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Trong $1$ ngày, đội thứ nhất làm được $\\dfrac{1}{x}$ (công việc).\\\n'
                   'Thời gian đội thứ hai làm riêng xong công việc là $x + %s$ (ngày) nên trong $1$ ngày, đội thứ hai làm được $\\dfrac{1}{x + %s}$ (công việc).\n'
                   '\\item Thay $x = %s$, trong $1$ ngày cả hai đội cùng làm được số phần công việc là:\\\n'
                   '$\\dfrac{1}{%s} + \\dfrac{1}{%s + %s} = \\dfrac{1}{%s} + \\dfrac{1}{%s} = \\dfrac{%s}{%s}$ (công việc).\\\n'
                   'Quy đổi sang tỉ số phần trăm: $\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%$.\n'
                   '\\end{enumEX}'
                   % (diff_d, diff_d, x_val, x_val, x_val, diff_d, x_val, y_val,
                      fr_sum.numerator, fr_sum.denominator, fr_sum.numerator, fr_sum.denominator, pct_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
