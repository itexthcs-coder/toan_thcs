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


def bt_dang15_p1_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        loai = random.choice(['trai_dau', 'hai_duong', 'hai_am'])

        if loai == 'trai_dau':
            a = random.choice([2, 3, 4, 5])
            b = random.choice([-9, -7, -5, 5, 7, 11])
            c = random.choice([-7, -5, -3, -2])
            pt = sp.latex(a*x**2 + b*x + c)
            P = Rational(c, a)
            da_str = 'Hai nghiệm trái dấu'
            sai_list = ['Hai nghiệm dương phân biệt', 'Hai nghiệm âm phân biệt', 'Vô nghiệm']
            lg = ('''Phương trình $%s=0$ có tích hai nghiệm $x_1x_2=\\frac{c}{a}=%s<0$ (vì $a=%s$ và $c=%s$ trái dấu).\\\\
Do đó phương trình có hai nghiệm trái dấu.''' % (pt, latex(P), a, c))

        elif loai == 'hai_duong':
            a = random.choice([1, 2])
            b = random.choice([-9, -8, -7])
            c = random.choice([2, 3, 5])
            pt = sp.latex(a*x**2 + b*x + c)
            delta = b**2 - 4 * a * c
            S = Rational(-b, a)
            P = Rational(c, a)
            da_str = 'Hai nghiệm dương phân biệt'
            sai_list = ['Hai nghiệm trái dấu', 'Hai nghiệm âm phân biệt', 'Vô nghiệm']
            lg = ('''Ta có: $\\Delta=(%s)^2-4\\cdot %s\\cdot %s=%s>0$ nên phương trình có hai nghiệm phân biệt $x_1$, $x_2$.\\\\
Theo định lí Viète, ta có: $x_1+x_2=%s>0$ và $x_1x_2=%s>0$.\\\\
Do tổng và tích đều dương nên phương trình có hai nghiệm dương phân biệt.''' % (b, a, c, delta, latex(S), latex(P)))

        else:
            a = random.choice([1, 2])
            b = random.choice([7, 8, 9])
            c = random.choice([2, 3, 5])
            pt = sp.latex(a*x**2 + b*x + c)
            delta = b**2 - 4 * a * c
            S = Rational(-b, a)
            P = Rational(c, a)
            da_str = 'Hai nghiệm âm phân biệt'
            sai_list = ['Hai nghiệm trái dấu', 'Hai nghiệm dương phân biệt', 'Vô nghiệm']
            lg = ('''Ta có: $\\Delta=%s^2-4\\cdot %s\\cdot %s=%s>0$ nên phương trình có hai nghiệm phân biệt $x_1$, $x_2$.\\\\
Theo định lí Viète, ta có: $x_1+x_2=%s<0$ và $x_1x_2=%s>0$.\\\\
Do tích dương và tổng âm nên phương trình có hai nghiệm âm phân biệt.''' % (b, a, c, delta, latex(S), latex(P)))

        # Các đáp án trắc nghiệm
        du = [da_str]
        da = random.choice(du)
        s = list(sai_list)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Không giải phương trình, hãy cho biết phương trình $%s=0$ có hai nghiệm như thế nào?'''
                         % (pt))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = lg

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
