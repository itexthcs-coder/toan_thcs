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


def bt_dang13_p3_b2_c8_ds8(self):
    # Dạng 13: Bài toán lập số tự nhiên từ các chữ số cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_so = random.choice([[1, 2, 3, 4], [1, 2, 3, 5], [2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5]])
        cac_so = [10*a + b for a in bo_so for b in bo_so if a != b]
        chia_het_3 = [n for n in cac_so if n % 3 == 0]
        
        tong_so = len(cac_so)
        so_tl = len(chia_het_3)
        p_dec = (Decimal(so_tl) / Decimal(tong_so)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        
        str_bo = "; ".join(str(x) for x in bo_so)
        str_cac_so = "; ".join(str(x) for x in cac_so)
        str_tl = "; ".join(str(x) for x in chia_het_3)
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (0.9,0.9);\n"
            "\\draw[line width=1pt] (1.2,0) rectangle (2.1,0.9);\n"
            "\\draw[line width=1pt] (2.4,0) rectangle (3.3,0.9);\n"
            "\\draw[line width=1pt] (3.6,0) rectangle (4.5,0.9);\n"
            "\\node at (0.45,0.45) {$%s$};\n"
            "\\node at (1.65,0.45) {$%s$};\n"
            "\\node at (2.85,0.45) {$%s$};\n"
            "\\node at (4.05,0.45) {$%s$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % tuple(bo_so)
        )
        
        noidungcauhoi = (
            "Từ bốn chữ số $%s$, người ta lập tất cả các số tự nhiên có hai chữ số khác nhau. "
            "Chọn ngẫu nhiên một số trong các số vừa lập được. Tính xác suất để chọn được một số chia hết cho $3$ "
            "(viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm).\n%s"
            % (str_bo, hinh_ve)
        )
        
        loigiai = (
            "Từ bốn chữ số $%s$, ta lập được các số tự nhiên có hai chữ số khác nhau là:\\\n"
            "$%s$, gồm có $%s$ số.\\\n"
            "Vì chọn ngẫu nhiên một số nên có $%s$ kết quả có thể là đồng khả năng.\\\n"
            "Trong các số trên, các số chia hết cho $3$ là: $%s$, gồm có $%s$ số.\\\n"
            "Vậy xác suất để chọn được một số chia hết cho $3$ là: $P = \\dfrac{%s}{%s} \\approx %s$."
            % (str_bo, str_cac_so, tong_so, tong_so, str_tl, so_tl, so_tl, tong_so, p_str)
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
