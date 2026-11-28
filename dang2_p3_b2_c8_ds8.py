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


def bt_dang2_p3_b2_c8_ds8(self):
    # Dạng 2: Bài toán ngược - Bớt phần tử khỏi không gian mẫu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        configs = [
            (32, 7, 12, 20),
            (30, 5, 10, 20),
            (40, 10, 12, 28),
            (28, 8, 9, 19),
            (36, 6, 18, 18)
        ]
        tong_dau, bot_bo, xop, bo_dau = random.choice(configs)
        con_lai = tong_dau - bot_bo
        p_dec = (Decimal(xop) / Decimal(con_lai)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        kq_str = str(bo_dau)
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) -- (3.6,0) -- (3.2,-1.6) -- (0.4,-1.6) -- cycle;\n"
            "\\draw[line width=1pt] (0.8,0) arc (180:0:1);\n"
            "\\draw[line width=1pt, ->] (2.6,-0.6) -- (4.2,-0.6);\n"
            "\\node[below] at (1.8,-1.7) {Giỏ quà gồm $%s$ gói bánh};\n"
            "\\node[above] at (3.5,-0.5) {$-%s$ gói quy bơ};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % (tong_dau, bot_bo)
        )
        
        noidungcauhoi = (
            "Một giỏ quà có $%s$ gói bánh cùng kích thước gồm hai loại: bánh quy bơ và bánh xốp. "
            "Sau khi lấy bớt ra $%s$ gói bánh quy bơ để tặng bạn, người ta chọn ngẫu nhiên một gói bánh trong giỏ thì thấy xác suất chọn được gói bánh xốp là $%s$. "
            "Hỏi ban đầu trong giỏ có bao nhiêu gói bánh quy bơ?\n%s"
            % (tong_dau, bot_bo, p_str, hinh_ve)
        )
        
        loigiai = (
            "Sau khi lấy bớt ra $%s$ gói bánh quy bơ, tổng số gói bánh còn lại trong giỏ là:\\\n"
            "$%s - %s = %s$ (gói).\\\n"
            "Vì các gói bánh có cùng kích thước và được chọn ngẫu nhiên nên có $%s$ kết quả có thể là đồng khả năng.\\\n"
            "Gọi số gói bánh xốp có trong giỏ là $y$ ($y \\in \\mathbb{N}^*$).\\\n"
            "Theo đề bài, xác suất chọn được gói bánh xốp lúc sau là $%s$ nên ta có:\\\n"
            "$\\dfrac{y}{%s} = %s \\Rightarrow y = %s \\cdot %s = %s$ (gói).\\\n"
            "Vì chỉ lấy bớt bánh quy bơ nên số gói bánh xốp ban đầu vẫn là $%s$ gói.\\\n"
            "Vậy ban đầu trong giỏ có số gói bánh quy bơ là: $%s - %s = %s$ (gói)."
            % (bot_bo, tong_dau, bot_bo, con_lai, con_lai, p_str, con_lai, p_str, con_lai, p_str, xop, xop, tong_dau, xop, kq_str)
        )
        
        dapan = "\\shortans[0]{$%s$}\n" % kq_str

    content = (
        "\\begin{minipage}{\\textwidth}\n"
        "\\begin{ex}\n" +
        str(noidungcauhoi) + str(dapan) +
        "\\loigiai{\n" + str(loigiai) + "}\n"
        "\\end{ex}\n\\end{minipage}\n\n"
    )
    return content
