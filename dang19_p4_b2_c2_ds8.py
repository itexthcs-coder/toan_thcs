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


def bt_dang19_p4_b2_c2_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap = random.choice([
            ('0,5', 1, 6),
            ('1', 2, 5),
            ('1,5', 3, 7)
        ])
        kc_str, tang, x0 = cap
        c2 = 3 * tang
        c1 = 3 * (tang ** 2)
        c0 = tang ** 3
        kq_b = c2 * (x0 ** 2) + c1 * x0 + c0

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khối rubik hình lập phương ban đầu có độ dài cạnh là $x\\text{ (cm)}$ ($x > 0$). Người ta thiết kế một hộp đựng hình lập phương bao bên ngoài sao cho khoảng cách từ mỗi mặt của khối rubik đến mặt tương ứng của hộp là $%s\\text{ cm}$. \\\\
                         a) Viết đa thức thu gọn biểu thị thể tích của chiếc hộp đựng theo $x$. \\\\
                         b) Tính phần thể tích khoảng trống bên trong hộp (không bị khối rubik chiếm chỗ) khi $x = %s\\text{ cm}$.'''
                         % (kc_str, x0))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                    \\item Vì khoảng cách ở hai mặt đối diện đều là $%s\\text{ cm}$ nên độ dài cạnh của hộp đựng hình lập phương là $x + 2 \\cdot %s = x + %s\\text{ (cm)}$. \\\\
                    Thể tích của chiếc hộp đựng là:
                    \\begin{align*}
                    V_{\\text{hộp}} = (x + %s)^3 = x^3 + %sx^2 + %sx + %s\\text{ (cm}^3).
                    \\end{align*}
                    \\item Thể tích của khối rubik là $V_{\\text{rubik}} = x^3\\text{ (cm}^3)$. \\\\
                    Phần thể tích khoảng trống bên trong hộp là:
                    \\begin{align*}
                    \\Delta V = (x + %s)^3 - x^3 = %sx^2 + %sx + %s\\text{ (cm}^3).
                    \\end{align*}
                    Khi $x = %s\\text{ cm}$, phần thể tích khoảng trống là:
                    \\begin{align*}
                    \\Delta V = %s \\cdot %s^2 + %s \\cdot %s + %s = %s\\text{ (cm}^3).
                    \\end{align*}
                    \\end{enumEX}'''
                   % (kc_str, kc_str, tang, tang, c2, c1, c0, tang, c2, c1, c0, x0, c2, x0, c1, x0, c0, kq_b))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
