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


def bt_dang10_p4_b2_c8_ds8(self):
    # Dạng 10: Xác suất trong bài toán lịch và thời gian (chọn ngày trong tháng)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        start_day = random.choice([0, 1, 2, 3, 4, 5, 6])
        day_names = ['Chủ nhật', 'thứ Hai', 'thứ Ba', 'thứ Tư', 'thứ Năm', 'thứ Sáu', 'thứ Bảy']
        start_name = day_names[start_day]

        saturdays = []
        sundays = []
        for d in range(1, 31):
            w = (start_day + d - 1) % 7
            if w == 6:
                saturdays.append(d)
            elif w == 0:
                sundays.append(d)

        so_tl = len(saturdays) + len(sundays)
        f = frac(so_tl, 30)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        sat_str = '; '.join([str(x) for x in saturdays])
        sun_str = '; '.join([str(x) for x in sundays])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (7,2.2);\n'
            '\\draw[line width=1pt] (0,1.6) -- (7,1.6);\n'
            '\\foreach \\x in {1,2,3,4,5,6}{ \\draw[line width=1pt] (\\x,0) -- (\\x,2.2); }\n'
            '\\foreach \\i/\\t in {0.5/T2, 1.5/T3, 2.5/T4, 3.5/T5, 4.5/T6, 5.5/T7, 6.5/CN}{ \\node at (\\i,1.9) {\\t}; }\n'
            '\\node at (3.5,0.8) {Lịch tháng có $30$ ngày (Ngày $1$ là %s)};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % start_name

        noidungcauhoi = (
            'Một công ty tổ chức bốc thăm trúng thưởng cho nhân viên dựa trên các ngày trong một tháng có $30$ ngày, biết ngày mùng $1$ của tháng đó là %s. '
            'Máy tính chọn ngẫu nhiên một ngày trong tháng đó. Tính xác suất để ngày được chọn rơi vào ngày thứ Bảy hoặc Chủ nhật.%s'
        ) % (start_name, tikz_img)

        loigiai = (
            'Tháng đó có $30$ ngày nên khi máy tính chọn ngẫu nhiên một ngày thì có $30$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Vì ngày mùng $1$ của tháng đó là %s nên:\\\\\n'
            '- Các ngày thứ Bảy trong tháng là các ngày: $%s$ (có $%s$ ngày).\\\\\n'
            '- Các ngày Chủ nhật trong tháng là các ngày: $%s$ (có $%s$ ngày).\\\\\n'
            'Do đó, tổng số ngày rơi vào thứ Bảy hoặc Chủ nhật trong tháng là $%s + %s = %s$ ngày.\\\\\n'
            'Vậy có $%s$ kết quả thuận lợi cho biến cố ngày được chọn rơi vào thứ Bảy hoặc Chủ nhật.\\\\\n'
            'Xác suất cần tìm là: $P = \\frac{%s}{30} = %s$.'
        ) % (
            start_name,
            sat_str, len(saturdays),
            sun_str, len(sundays),
            len(saturdays), len(sundays), so_tl,
            so_tl, so_tl, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
