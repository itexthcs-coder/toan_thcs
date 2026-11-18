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


def bt_dang16_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (20, 20),
            (10, 10),
            (40, 80)
        ])
        k_chia, x_nuoc = bo_so
        m_dd_dau = 200
        c1_pt = 15
        c2_pt = 25
        m_muoi_dau = 30
        m_muoi_them = (x_nuoc**2) // k_chia
        tong_dd_sau = m_dd_dau + x_nuoc + m_muoi_them

        a_pt = 3
        b_pt = -k_chia
        c_pt = -80 * k_chia
        delta = b_pt**2 - 4 * a_pt * c_pt
        can_delta = int(math.isqrt(delta))
        nghiem_am = Rational(-b_pt - can_delta, 2 * a_pt)

        noidungcauhoi = ('''Trong phòng thí nghiệm, có một bình chứa $%s\\text{ g}$ dung dịch muối ăn nồng độ $%s\\%%$. Người ta đổ thêm vào bình $x\\text{ (g)}$ nước tinh khiết, sau đó lại cho thêm $\\frac{x^2}{%s}\\text{ (g)}$ muối ăn nguyên chất thì thu được dung dịch mới có nồng độ $%s\\%%$. \\\\
a) Tính khối lượng nước tinh khiết $x$ đã đổ thêm vào bình. \\\\
b) Tính tổng khối lượng của dung dịch thu được sau khi pha chế.'''
                         %(latex(m_dd_dau), latex(c1_pt), latex(k_chia), latex(c2_pt)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Điều kiện của ẩn là $x > 0$. \\\\
Khối lượng muối ăn nguyên chất có trong bình ban đầu là: $%s \\cdot %s\\%% = %s\\text{ (g)}$. \\\\
Sau khi thêm $x\\text{ (g)}$ nước tinh khiết và $\\frac{x^2}{%s}\\text{ (g)}$ muối ăn nguyên chất, khối lượng muối ăn có trong bình là $%s + \\frac{x^2}{%s}\\text{ (g)}$ và tổng khối lượng dung dịch là $%s + x + \\frac{x^2}{%s}\\text{ (g)}$. \\\\
Vì dung dịch mới có nồng độ $%s\\%% = \\frac{1}{4}$ nên ta có phương trình: \\\\
$\\frac{%s + \\frac{x^2}{%s}}{%s + x + \\frac{x^2}{%s}} = \\frac{1}{4}$. \\\\
Nhân chéo và khử mẫu, ta được: \\\\
$4\\left(%s + \\frac{x^2}{%s}\\right) = %s + x + \\frac{x^2}{%s}$ hay $3x^2 - %sx - %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 3 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = %s$ (loại); \\quad $x_2 = %s$ (thoả mãn điều kiện). \\\\
Vậy khối lượng nước tinh khiết đã đổ thêm vào bình là $%s\\text{ g}$.
\\item Khối lượng muối ăn nguyên chất cho thêm là $\\frac{%s^2}{%s} = %s\\text{ (g)}$. \\\\
Tổng khối lượng dung dịch thu được sau khi pha chế là: $%s + %s + %s = %s\\text{ (g)}$.
\\end{enumEX}'''
                   %(latex(m_dd_dau), latex(c1_pt), latex(m_muoi_dau),
                     latex(k_chia), latex(m_muoi_dau), latex(k_chia), latex(m_dd_dau), latex(k_chia),
                     latex(c2_pt), latex(m_muoi_dau), latex(k_chia), latex(m_dd_dau), latex(k_chia),
                     latex(m_muoi_dau), latex(k_chia), latex(m_dd_dau), latex(k_chia), latex(k_chia), latex(abs(c_pt)),
                     latex(k_chia), latex(abs(c_pt)), latex(delta), latex(can_delta),
                     latex(nghiem_am), latex(x_nuoc), latex(x_nuoc),
                     latex(x_nuoc), latex(k_chia), latex(m_muoi_them),
                     latex(m_dd_dau), latex(x_nuoc), latex(m_muoi_them), latex(tong_dd_sau)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
