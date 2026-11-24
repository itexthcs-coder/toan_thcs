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


def bt_dang14_p3_b1_c5_ds8(self):
    # Dạng 14: Đếm số cặp phân loại dữ liệu chính xác trong bảng đối chiếu
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        c1_ok = random.choice([True, False])
        c2_ok = random.choice([True, False])
        c3_ok = random.choice([True, False])
        c4_ok = random.choice([True, False])
        so_dung = sum([c1_ok, c2_ok, c3_ok, c4_ok])
        kq_str = str(so_dung)

        r1_right = "Số liệu rời rạc" if c1_ok else "Số liệu liên tục"
        r2_right = "Số liệu liên tục" if c2_ok else "Số liệu rời rạc"
        r3_right = "Dữ liệu không là số, không thể sắp thứ tự" if c3_ok else "Dữ liệu không là số, có thể sắp thứ tự"
        r4_right = "Dữ liệu không là số, có thể sắp thứ tự" if c4_ok else "Số liệu rời rạc"

        bang_gc = (
            "\\begin{center}\n"
            "\\begin{tabular}{|c|l|l|}\n"
            "\\hline\n"
            "\\textbf{STT} & \\textbf{Đối tượng dữ liệu} & \\textbf{Loại dữ liệu tương ứng} \\\\\n"
            "\\hline\n"
            "$1$ & Số đường tròn ngoại tiếp một tam giác & %s \\\\\n"
            "\\hline\n"
            "$2$ & Bán kính đường tròn nội tiếp tam giác & %s \\\\\n"
            "\\hline\n"
            "$3$ & Tên các loại tứ giác (Hình thang, Hình thoi, Hình vuông) & %s \\\\\n"
            "\\hline\n"
            "$4$ & Mức độ khó của bài toán (Dễ, Trung bình, Khó) & %s \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (r1_right, r2_right, r3_right, r4_right)
        )

        noidungcauhoi = ('''Cho bảng đối chiếu phân loại dữ liệu dưới đây:
%s
Có bao nhiêu dòng ghép cặp \\textbf{chính xác} trong bảng trên?''' % bang_gc)

        gt1 = "Đúng (thu được từ phép đếm nên là số liệu rời rạc)" if c1_ok else "Sai (phải là số liệu rời rạc)"
        gt2 = "Đúng (thu được từ phép đo độ dài nên là số liệu liên tục)" if c2_ok else "Sai (phải là số liệu liên tục)"
        gt3 = "Đúng (tên gọi phân loại không có thứ bậc nên là dữ liệu không là số, không thể sắp thứ tự)" if c3_ok else "Sai (phải là dữ liệu không là số, không thể sắp thứ tự)"
        gt4 = "Đúng (mức độ đánh giá sắp xếp theo thứ bậc nên là dữ liệu không là số, có thể sắp thứ tự)" if c4_ok else "Sai (phải là dữ liệu không là số, có thể sắp thứ tự)"

        loigiai = ('''Ta kiểm tra từng dòng trong bảng đối chiếu:\\\\
- Dòng $1$: %s.\\\\
- Dòng $2$: %s.\\\\
- Dòng $3$: %s.\\\\
- Dòng $4$: %s.\\\\
Vậy có tất cả $%s$ dòng ghép cặp chính xác.''' % (gt1, gt2, gt3, gt4, kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
