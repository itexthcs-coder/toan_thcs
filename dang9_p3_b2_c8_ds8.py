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


def bt_dang9_p3_b2_c8_ds8(self):
    # Dạng 9: Xác suất hình học (diện tích lưới ô vuông / hình chữ nhật)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        rong, dai = random.choice([(6, 10), (8, 10), (5, 8), (10, 10), (8, 15)])
        tong_o = rong * dai
        o_trong = (rong - 2) * (dai - 2)
        o_vien = tong_o - o_trong
        
        p_dec = (Decimal(o_vien) / Decimal(tong_o)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=0.45, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) grid (8,5);\n"
            "\\draw[line width=1pt] (1,1) rectangle (7,4);\n"
            "\\node[below] at (4,-0.3) {Bảng kích thước $%s \\text{ dm} \\times %s \\text{ dm}$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % (rong, dai)
        )
        
        noidungcauhoi = (
            "Một tấm bảng phi tiêu hình chữ nhật kích thước $%s\\text{ dm} \\times %s\\text{ dm}$ được chia thành các ô vuông đơn vị cạnh $1\\text{ dm}$. "
            "Người ta tô màu toàn bộ các ô vuông nằm ở đường viền ngoài cùng của tấm bảng. "
            "Phi tiêu phóng ngẫu nhiên và trúng vào một ô vuông bất kì trên bảng. "
            "Tính xác suất để phi tiêu trúng vào ô vuông được tô màu (viết kết quả dưới dạng số thập phân).\n%s"
            % (rong, dai, hinh_ve)
        )
        
        loigiai = (
            "Tổng số ô vuông đơn vị trên tấm bảng là: $%s \\cdot %s = %s$ (ô).\\\n"
            "Vì phi tiêu phóng ngẫu nhiên và các ô vuông có diện tích bằng nhau nên có $%s$ kết quả có thể là đồng khả năng.\\\n"
            "Phần hình chữ nhật ở bên trong không bị tô màu có kích thước là $(%s - 2)\\text{ dm} \\times (%s - 2)\\text{ dm} = %s\\text{ dm} \\times %s\\text{ dm}$.\\\n"
            "Số ô vuông không được tô màu là: $%s \\cdot %s = %s$ (ô).\\\n"
            "Số ô vuông được tô màu ở đường viền ngoài cùng là: $%s - %s = %s$ (ô).\\\n"
            "Vậy xác suất để phi tiêu trúng vào ô vuông được tô màu là: $P = \\dfrac{%s}{%s} = %s$."
            % (rong, dai, tong_o, tong_o, rong, dai, rong - 2, dai - 2,
               rong - 2, dai - 2, o_trong, tong_o, o_trong, o_vien, o_vien, tong_o, p_str)
        )
        
        dapan = "\\shortans[0]{$%s$}\n" % p_str

    content = (
        "\\begin{minipage}{\\textwidth}\n"
        "\\begin{ex}\n" +
        str(noidungcauhoi) + str(dapan) +
        "\\loigiai{\n" + str(loigiai) + "}\n"
        "\\end{ex}\n\\end{minipage}\n\n"
    )
    return content
