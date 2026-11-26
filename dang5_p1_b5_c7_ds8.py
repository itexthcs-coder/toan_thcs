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


def bt_dang5_p1_b5_c7_ds8(self):
    def fmt_num(val):
        if isinstance(val, Fraction):
            if val.denominator == 1:
                return str(val.numerator)
            if val.numerator < 0:
                return '-\\dfrac{%s}{%s}' % (abs(val.numerator), val.denominator)
            return '\\dfrac{%s}{%s}' % (val.numerator, val.denominator)
        if isinstance(val, float):
            s_val = ('%g' % val).replace('.', ',')
            return s_val
        return str(val)

    def fmt_line(a_val, b_val):
        # Định dạng y = ax + b với a_val, b_val là int hoặc Fraction
        if isinstance(a_val, Fraction) and a_val.denominator != 1:
            if a_val.numerator < 0:
                str_a = '-\\dfrac{%s}{%s}x' % (abs(a_val.numerator), a_val.denominator)
            else:
                str_a = '\\dfrac{%s}{%s}x' % (a_val.numerator, a_val.denominator)
        else:
            ai = int(a_val)
            if ai == 1:
                str_a = 'x'
            elif ai == -1:
                str_a = '-x'
            else:
                str_a = '%sx' % ai

        if b_val == 0:
            return 'y = %s' % str_a
        if isinstance(b_val, Fraction) and b_val.denominator != 1:
            if b_val.numerator < 0:
                str_b = '- \\dfrac{%s}{%s}' % (abs(b_val.numerator), b_val.denominator)
            else:
                str_b = '+ \\dfrac{%s}{%s}' % (b_val.numerator, b_val.denominator)
        else:
            bi = int(b_val)
            if bi > 0:
                str_b = '+ %s' % bi
            else:
                str_b = '- %s' % abs(bi)
        return 'y = %s %s' % (str_a, str_b)

    # Dạng 5: Nhận biết chiều đi lên/đi xuống của đồ thị từ trái sang phải
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mode = random.choice(['xuong', 'len'])
        a_neg = random.choice([-4, -3, -2, -1])
        b_neg = random.choice([1, 2, 3, 4, 5])
        a_pos1 = random.choice([1, 2, 3, 4])
        b_pos1 = random.choice([-5, -3, -1, 2, 4])
        a_pos2 = random.choice([2, 3, 5])
        b_pos2 = random.choice([1, 3, 5])
        a_pos3 = random.choice([1, 2, 4])
        b_pos3 = random.choice([-4, -2, 1, 3])

        pt_neg = 'y = %s %sx' % (b_neg, a_neg if a_neg != -1 else '-')
        pt_p1 = fmt_line(a_pos1, b_pos1)
        pt_p2 = fmt_line(a_pos2, b_pos2)
        pt_p3 = fmt_line(a_pos3, b_pos3)

        if mode == 'xuong':
            yeu_cau = 'đi xuống từ trái sang phải'
            da = '$%s$' % pt_neg
            s = ['$%s$' % pt_p1, '$%s$' % pt_p2, '$%s$' % pt_p3]
            gt = ('Đường thẳng $y = ax + b$ ($a \\neq 0$) đi xuống từ trái sang phải khi và chỉ khi hệ số góc $a < 0$.\\\\'
                  'Xét các phương án:\\\\'
                  '- Đường thẳng $%s$ có hệ số góc $a = %s < 0$ nên đi xuống từ trái sang phải.\\\\'
                  '- Các đường thẳng còn lại đều có hệ số góc dương ($a > 0$) nên đi lên từ trái sang phải.'
                  % (pt_neg, a_neg))
        else:
            yeu_cau = 'đi lên từ trái sang phải'
            a_neg2 = random.choice([-5, -3, -2])
            a_neg3 = random.choice([-4, -2, -1])
            pt_n2 = fmt_line(a_neg2, b_pos2)
            pt_n3 = fmt_line(a_neg3, b_pos3)
            da = '$%s$' % pt_p1
            s = ['$%s$' % pt_neg, '$%s$' % pt_n2, '$%s$' % pt_n3]
            gt = ('Đường thẳng $y = ax + b$ ($a \\neq 0$) đi lên từ trái sang phải khi và chỉ khi hệ số góc $a > 0$.\\\\'
                  'Xét các phương án:\\\\'
                  '- Đường thẳng $%s$ có hệ số góc $a = %s > 0$ nên đi lên từ trái sang phải.\\\\'
                  '- Các đường thẳng còn lại đều có hệ số góc âm ($a < 0$) nên đi xuống từ trái sang phải.'
                  % (pt_p1, a_pos1))

        noidungcauhoi = ('Trong các hàm số bậc nhất sau, đồ thị của hàm số nào là đường thẳng %s?' % yeu_cau)
        da_d = ('\\True ' + da)
        list_1 = [da_d, s[0], s[1], s[2]]
        random.shuffle(list_1)
        loigiai = gt

    # Xuất câu trắc nghiệm
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
