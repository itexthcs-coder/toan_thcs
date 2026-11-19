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


def bt_dang19_p3_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        dk = random.choice([
            ('hạt vàng và trơn', '$(AA, Bb); (Aa, Bb); (aA, Bb)$', 3),
            ('hạt vàng và nhăn', '$(AA, bb); (Aa, bb); (aA, bb)$', 3),
            ('có kiểu hình hạt xanh', '$(aa, Bb); (aa, bb)$', 2),
            ('có kiểu hình hạt vàng', '$(AA, Bb); (AA, bb); (Aa, Bb); (Aa, bb); (aA, Bb); (aA, bb)$', 6)
        ])
        ten_kh, tap_kg, so_tl = dk
        xs = Rational(so_tl, 8)
        if xs.q in [1, 2, 4]:
            kq_str = ('%g' % float(xs)).replace('.', ',')
        else:
            number = Decimal(float(xs))
            kq_str = str(number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Mẹ $\\backslash$ Bố & $(A, B)$ & $(A, b)$ & $(a, B)$ & $(a, b)$ \\\\
\\hline
$(A, b)$ & $(AA, Bb)$ & $(AA, bb)$ & $(aA, Bb)$ & $(aA, bb)$ \\\\
\\hline
$(a, b)$ & $(Aa, Bb)$ & $(Aa, bb)$ & $(aa, Bb)$ & $(aa, bb)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Ở đậu Hà Lan, xét hai cặp gene phân li độc lập: $A$ (vàng) trội hoàn toàn so với $a$ (xanh); $B$ (trơn) trội hoàn toàn so với $b$ (nhăn). Cho lai cây bố có kiểu gene $(Aa, Bb)$ với cây mẹ có kiểu gene $(Aa, bb)$. Tính xác suất để cây con sinh ra %s (làm tròn kết quả đến hàng phần trăm nếu cần).'''
                         % (ten_kh))

        loigiai = ('''Cây bố $(Aa, Bb)$ tạo $4$ loại giao tử $(A, B); (A, b); (a, B); (a, b)$; cây mẹ $(Aa, bb)$ tạo $2$ loại giao tử $(A, b); (a, b)$. Ta lập bảng tổ hợp đời con:%s
Không gian mẫu $\\Omega$ gồm $4 \\cdot 2 = 8$ tổ hợp kiểu gene đồng khả năng.\\\\
Cây con %s ứng với các kiểu gene %s, suy ra có $%s$ kết quả thuận lợi.\\\\
Vậy xác suất cần tìm là $P = \\dfrac{%s}{8} \\approx %s$.'''
                   % (bang_mau, ten_kh, tap_kg, so_tl, so_tl, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
