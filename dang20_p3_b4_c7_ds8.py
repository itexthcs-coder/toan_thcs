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

def bt_dang20_p3_b4_c7_ds8(self):
    # Dạng 20 (Ứng dụng thực tế): Tính số sản phẩm cần bán để đạt mức thu nhập mục tiêu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        luong_cb = random.choice([5, 6, 7, 8, 9, 10])
        hh_num = random.choice([2, 3, 4, 5])
        hh_val = Fraction(hh_num, 10)
        hh_str = str(Decimal(str(float(hh_val)))).replace('.', ',')
        sp_ans = random.choice([10, 15, 20, 25, 30, 35, 40, 45, 50])
        thu_nhap = int(luong_cb + hh_val * sp_ans)
        kq_str = str(sp_ans)

        noidungcauhoi = ('''Một nhân viên bán hàng có mức lương cơ bản hằng tháng là $%s\\text{ triệu đồng}$ và được hưởng thêm tiền hoa hồng là $%s\\text{ triệu đồng}$ cho mỗi sản phẩm bán được trong tháng. Để đạt tổng thu nhập trong tháng là $%s\\text{ triệu đồng}$, nhân viên đó cần bán được bao nhiêu sản phẩm?'''
                         % (luong_cb, hh_str, thu_nhap))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

        loigiai = ('''Gọi $x$ (sản phẩm) là số sản phẩm nhân viên đó bán được trong tháng ($x \\in \\mathbb{N}$) và $y$ (triệu đồng) là tổng thu nhập nhận được trong tháng.\\\\
Công thức hàm số bậc nhất biểu thị tổng thu nhập $y$ theo số sản phẩm $x$ là:\\\\
$y = %sx + %s$.\\\\
Để tổng thu nhập trong tháng đạt $y = %s\\text{ triệu đồng}$, ta thay vào công thức trên:\\\\
$%sx + %s = %s$\\\\
$\\Leftrightarrow %sx = %s - %s$\\\\
$\\Leftrightarrow %sx = %s$\\\\
$\\Leftrightarrow x = \\dfrac{%s}{%s} = %s$.\\\\
Vậy nhân viên đó cần bán được $%s$ sản phẩm trong tháng.'''
                   % (hh_str, luong_cb,
                      thu_nhap,
                      hh_str, luong_cb, thu_nhap,
                      hh_str, thu_nhap, luong_cb,
                      hh_str, thu_nhap - luong_cb,
                      thu_nhap - luong_cb, hh_str, kq_str,
                      kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
