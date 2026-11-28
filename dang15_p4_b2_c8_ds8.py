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


def bt_dang15_p4_b2_c8_ds8(self):
    # Dạng 15: Xác suất trong tình huống mật khẩu hoặc mã khóa số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        sub = random.choice(['chan', 'le'])
        if sub == 'chan':
            digits = [0, 2, 4, 6, 8]
            tong_cap = random.choice([6, 8, 10])
        else:
            digits = [1, 3, 5, 7, 9]
            tong_cap = random.choice([8, 10, 12])

        all_codes = []
        fav_codes = []
        for a in digits:
            for b in digits:
                code_str = '%s%s' % (a, b)
                all_codes.append(code_str)
                if a + b == tong_cap:
                    fav_codes.append(code_str)

        tong_kq = len(all_codes)
        so_tl = len(fav_codes)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        digits_str = '; '.join([str(d) for d in digits])
        fav_str = '; '.join(fav_codes)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (3.4,1.6);\n'
            '\\draw[line width=1pt] (0.9,1.6) arc (180:0:0.8);\n'
            '\\draw[line width=1pt] (0.5,0.4) rectangle (1.5,1.2);\n'
            '\\draw[line width=1pt] (1.9,0.4) rectangle (2.9,1.2);\n'
            '\\node at (1.0,0.8) {$?$};\n'
            '\\node at (2.4,0.8) {$?$};\n'
            '\\node at (1.7,-0.4) {Khóa số $2$ chữ số từ tập $\\{%s\\}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (', '.join([str(d) for d in digits]))

        noidungcauhoi = (
            'Một chiếc khóa vali có mã số gồm $2$ chữ số được tạo thành từ các chữ số $%s$ (các chữ số có thể giống nhau). '
            'Bạn Minh quên mất mật khẩu nên bấm thử ngẫu nhiên một mã số gồm $2$ chữ số từ các chữ số trên. '
            'Tính xác suất để Minh mở được khóa ngay lần bấm đầu tiên, biết rằng Minh chỉ nhớ tổng hai chữ số của mật khẩu bằng $%s$.%s'
        ) % (digits_str, tong_cap, tikz_img)

        loigiai = (
            'Mỗi chữ số trong mã khóa có $5$ cách chọn từ tập hợp $\\{%s\\}$ (vì hai chữ số có thể giống nhau).\\\\\n'
            'Do đó, tổng số mã số gồm $2$ chữ số có thể tạo thành là $5 \\cdot 5 = %s$ mã số.\\\\\n'
            'Vì Minh bấm thử ngẫu nhiên một mã số nên có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Các mã số gồm $2$ chữ số lấy từ tập $\\{%s\\}$ có tổng hai chữ số bằng $%s$ là: %s.\\\\\n'
            'Như vậy, có $%s$ kết quả thuận lợi cho biến cố Minh mở được khóa ngay lần bấm đầu tiên.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{%s} = %s$.'
        ) % (
            ', '.join([str(d) for d in digits]), tong_kq,
            tong_kq, ', '.join([str(d) for d in digits]), tong_cap, fav_str,
            so_tl, so_tl, tong_kq, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
