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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang7_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r1 = randint(-2, 1)
        r2 = r1 + randint(3, 5)
        b_coef = -(r1 + r2)
        c_coef = r1 * r2
        
        b_str = "- %sm" % abs(b_coef) if b_coef < 0 else ("+ %sm" % b_coef if b_coef > 0 else "")
        c_str = "- %s" % abs(c_coef) if c_coef < 0 else ("+ %s" % c_coef if c_coef > 0 else "")
        
        term1 = "(m + %s)" % abs(r1) if r1 < 0 else ("m" if r1 == 0 else "(m - %s)" % r1)
        term2 = "(m + %s)" % abs(r2) if r2 < 0 else ("m" if r2 == 0 else "(m - %s)" % r2)
        ineq1_a = "m + %s > 0" % abs(r1) if r1 < 0 else ("m > 0" if r1 == 0 else "m - %s > 0" % r1)
        ineq1_b = "m + %s < 0" % abs(r2) if r2 < 0 else ("m < 0" if r2 == 0 else "m - %s < 0" % r2)
        
        int_list = [str(val) for val in range(r1 + 1, r2)]
        int_ans = "; ".join(int_list)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y = (m^2 %s %s)x^2$. Tìm tất cả các giá trị nguyên của tham số $m$ để đồ thị của hàm số đã cho là một đường parabol nằm hoàn toàn phía dưới trục hoành.'''
                         %(b_str, c_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) nằm hoàn toàn phía dưới trục hoành khi và chỉ khi hệ số $a < 0$. \\\\
Áp dụng vào hàm số đã cho, ta cần điều kiện: \\\\
$m^2 %s %s < 0$ \\\\
Phân tích vế trái thành nhân tử, ta được: \\\\
$%s%s < 0$ \\\\
Vì $%s < %s$ nên bất phương trình tương đương với: \\\\
$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} m > %s \\\\ m < %s \\end{cases} \\Leftrightarrow %s < m < %s$. \\\\
Vì $m$ là số nguyên nên $m \\in \\{%s\\}$. \\\\
Vậy các giá trị nguyên cần tìm của $m$ là $%s$.'''
                   %(b_str, c_str,
                     term1, term2,
                     latex(r1), latex(r2),
                     ineq1_a, ineq1_b, latex(r1), latex(r2), latex(r1), latex(r2),
                     int_ans,
                     int_ans
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
