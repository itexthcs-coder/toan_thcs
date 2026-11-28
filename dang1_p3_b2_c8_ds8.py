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


def bt_dang1_p3_b2_c8_ds8(self):
    # Dạng 1: Bài toán ngược - Thêm phần tử vào không gian mẫu (Tìm số phần tử ban đầu)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        pairs = [(14, 6, 20, 0.65), (12, 8, 20, 0.7), (15, 5, 25, 0.6), (18, 6, 24, 0.625), (16, 4, 24, 0.64)]
        b_cam, them_trang, x_dung, p_val = random.choice(pairs)
        p_dec = Decimal(str(p_val))
        p_str = str(p_dec).replace('.', ',')
        kq_str = str(x_dung)
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (4,2.2);\n"
            "\\draw[line width=1pt] (0.8,0.6) circle (0.25);\n"
            "\\draw[line width=1pt] (1.6,1.4) circle (0.25);\n"
            "\\fill (2.6,0.7) circle (0.25);\n"
            "\\fill (3.2,1.5) circle (0.25);\n"
            "\\draw[line width=1pt, ->] (4.8,1.1) -- (4.1,1.1);\n"
            "\\draw[line width=1pt] (5.2,1.1) circle (0.25);\n"
            "\\node[below] at (2,0) {Hộp bóng};\n"
            "\\node[above] at (5.2,1.45) {$+%s$ trắng};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % them_trang
        )
        
        noidungcauhoi = (
            "Trong một hộp đựng các quả bóng bàn có kích thước và khối lượng như nhau, gồm một số bóng màu trắng và $%s$ bóng màu cam. "
            "Người ta bỏ thêm vào hộp $%s$ quả bóng màu trắng nữa. Lấy ngẫu nhiên một quả bóng từ hộp, biết xác suất lấy được bóng màu trắng là $%s$. "
            "Hỏi ban đầu trong hộp có bao nhiêu quả bóng màu trắng?\n%s"
            % (b_cam, them_trang, p_str, hinh_ve)
        )
        
        loigiai = (
            "Gọi số quả bóng màu trắng ban đầu có trong hộp là $x$ ($x \\in \\mathbb{N}^*$).\\\n"
            "Sau khi bỏ thêm $%s$ quả bóng màu trắng, số quả bóng màu trắng trong hộp là $x + %s$ (quả) và tổng số quả bóng trong hộp là $x + %s + %s = x + %s$ (quả).\\\n"
            "Vì lấy ngẫu nhiên một quả bóng trong hộp nên có $x + %s$ kết quả có thể và các kết quả này là đồng khả năng.\\\n"
            "Số kết quả thuận lợi cho biến cố lấy được bóng màu trắng là $x + %s$.\\\n"
            "Theo đề bài, xác suất lấy được bóng màu trắng là $%s$ nên ta có phương trình:\\\n"
            "$\\dfrac{x + %s}{x + %s} = %s \\Rightarrow x + %s = %s(x + %s) \\Rightarrow x = %s$.\\\n"
            "Vậy ban đầu trong hộp có $%s$ quả bóng màu trắng."
            % (them_trang, them_trang, b_cam, them_trang, b_cam + them_trang,
               b_cam + them_trang, them_trang, p_str,
               them_trang, b_cam + them_trang, p_str, them_trang, p_str, b_cam + them_trang, kq_str, kq_str)
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
