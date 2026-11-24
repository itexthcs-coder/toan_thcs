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


def bt_dang1_p3_b1_c5_ds8(self):
    # Dạng 1: Đếm số cột số liệu liên tục trong bảng dữ liệu đa biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a1 = random.randint(2, 5)
        a2 = random.randint(3, 6)
        a3 = random.randint(4, 8)
        kq_int = 3
        kq_str = str(kq_int)

        bang_hh = (
            "\\begin{center}\n"
            "\\begin{tabular}{|c|c|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Mã khối} & \\textbf{Cạnh đáy (cm)} & \\textbf{Số đỉnh} & \\textbf{Diện tích toàn phần (cm$^2$)} & \\textbf{Thể tích (cm$^3$)} \\\\\n"
            "\\hline\n"
            "$H_1$ & $%s,5$ & $8$ & $%s,5$ & $%s,25$ \\\\\n"
            "\\hline\n"
            "$H_2$ & $%s,0$ & $8$ & $%s,0$ & $%s,0$ \\\\\n"
            "\\hline\n"
            "$H_3$ & $%s,2$ & $8$ & $%s,24$ & $%s,48$ \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (a1, 6 * a1 * a1, a1**3, a2, 6 * a2 * a2, a2**3, a3, 6 * a3 * a3, a3**3)
        )

        noidungcauhoi = ('''Cho bảng dữ liệu thống kê thông tin của ba hình lập phương gồm $5$ cột sau:
%s
Có bao nhiêu cột trong bảng trên thuộc loại \\textbf{số liệu liên tục}?''' % bang_hh)

        loigiai = ('''Ta phân loại dữ liệu của từng cột trong bảng thống kê:\\\\
- Cột \\textbf{Mã khối} ($H_1, H_2, H_3$): là dữ liệu không là số.\\\\
- Cột \\textbf{Cạnh đáy (cm)}: thu được từ phép đo độ dài nên là số liệu liên tục.\\\\
- Cột \\textbf{Số đỉnh}: thu được từ phép đếm nên là số liệu rời rạc.\\\\
- Cột \\textbf{Diện tích toàn phần (cm$^2$)}: thu được từ phép đo diện tích nên là số liệu liên tục.\\\\
- Cột \\textbf{Thể tích (cm$^3$)}: thu được từ phép đo thể tích nên là số liệu liên tục.\\\\
Vậy có tất cả $%s$ cột thuộc loại số liệu liên tục.''' % kq_str)

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
