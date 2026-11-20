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


def bt_dang20_p3_b2_c10_hh9(self):
    # V_vo = 4/3 * pi * (R^3 - r^3). Khối lượng m = V_vo * D (g)
    R = random.choice([5, 6, 7])
    r = R - 1
    D = random.choice([7.8, 8.9]) # g/cm^3 (sắt hoặc đồng)
    V_vo = (4 / 3) * math.pi * (R**3 - r**3)
    m_exact = V_vo * D
    m_round = Decimal(str(m_exact)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    kq_str = str(m_round)

    def fmt(val):
        return str(val).replace('.', ',')

    noidungcauhoi = ('''Một quả cầu kim loại rỗng có dạng hình cầu với bán kính mặt ngoài bằng $%s\\text{ cm}$ và độ dày lớp vỏ kim loại đồng đều bằng $1\\text{ cm}$. Biết khối lượng riêng của kim loại làm quả cầu là $%s\\text{ g/cm}^3$. Tính khối lượng của quả cầu kim loại đó (làm tròn kết quả đến hàng đơn vị của gam).'''
                     % (R, fmt(D)))

    loigiai = ('''Bán kính mặt trong (phần rỗng) của quả cầu là: $r = %s - 1 = %s\\text{ (cm)}$.\\\nThể tích của khối cầu ngoài là: $V_{\\text{ngoài}} = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = \\dfrac{%s\\pi}{3}\\text{ (cm}^3\\text{)}$.\\\nThể tích phần rỗng bên trong là: $V_{\\text{trong}} = \\dfrac{4}{3}\\pi r^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = \\dfrac{%s\\pi}{3}\\text{ (cm}^3\\text{)}$.\\\nThể tích phần vỏ kim loại của quả cầu là:
$$V_{\\text{vỏ}} = V_{\\text{ngoài}} - V_{\\text{trong}} = \\dfrac{%s\\pi}{3} - \\dfrac{%s\\pi}{3} = \\dfrac{%s\\pi}{3}\\text{ (cm}^3\\text{)}.$$
Khối lượng của quả cầu kim loại là:
$$m = V_{\\text{vỏ}} \\cdot D = \\dfrac{%s\\pi}{3} \\cdot %s \\approx %s\\text{ (g)}.$$'''
               % (R, fmt(D), R, 4 * (R**3), r, 4 * (r**3), 4 * (R**3), 4 * (r**3), 4 * (R**3 - r**3), 4 * (R**3 - r**3), fmt(D), kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
