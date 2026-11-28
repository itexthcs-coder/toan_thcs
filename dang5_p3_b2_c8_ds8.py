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


def bt_dang5_p3_b2_c8_ds8(self):
    # Dạng 5: Không gian mẫu là tập hợp số tự nhiên có 2 chữ số thỏa mãn điều kiện chia hết
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        d1, d2 = random.choice([(5, 3), (4, 3), (6, 5), (5, 4), (3, 4)])
        ds_mau = [n for n in range(10, 100) if n % d1 == 0]
        bcnn = math.lcm(d1, d2)
        ds_thuan_loi = [n for n in ds_mau if n % bcnn == 0]
        
        so_mau = len(ds_mau)
        so_tl = len(ds_thuan_loi)
        p_dec = (Decimal(so_tl) / Decimal(so_mau)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        
        str_mau = "; ".join(str(x) for x in ds_mau[:4]) + "; \\dots; " + str(ds_mau[-1])
        str_tl = "; ".join(str(x) for x in ds_thuan_loi)
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) ellipse (2.6 and 1.1);\n"
            "\\draw[line width=1pt] (0.6,0) ellipse (1.3 and 0.65);\n"
            "\\node[left] at (-0.6,0) {Chia hết cho $%s$};\n"
            "\\node at (0.6,0) {Chia hết cho $%s$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % (d1, bcnn)
        )
        
        noidungcauhoi = (
            "Viết ngẫu nhiên một số tự nhiên có hai chữ số chia hết cho $%s$. "
            "Tính xác suất để số được viết ra cũng chia hết cho $%s$ "
            "(viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm).\n%s"
            % (d1, d2, hinh_ve)
        )
        
        loigiai = (
            "Tập hợp các số tự nhiên có hai chữ số chia hết cho $%s$ là: $\\{%s\\}$.\\\n"
            "Số kết quả có thể của hành động viết ngẫu nhiên một số trong tập hợp trên là: $\\dfrac{%s - %s}{%s} + 1 = %s$ (số).\\\n"
            "Vì viết ngẫu nhiên nên $%s$ kết quả có thể này là đồng khả năng.\\\n"
            "Một số chia hết cho cả $%s$ và $%s$ thì chia hết cho $\\text{BCNN}(%s, %s) = %s$.\\\n"
            "Các số tự nhiên có hai chữ số chia hết cho $%s$ là: $\\{%s\\}$, gồm có $%s$ số.\\\n"
            "Vậy xác suất để số được viết ra chia hết cho $%s$ là: $P = \\dfrac{%s}{%s} \\approx %s$."
            % (d1, str_mau, ds_mau[-1], ds_mau[0], d1, so_mau, so_mau,
               d1, d2, d1, d2, bcnn, bcnn, str_tl, so_tl, d2, so_tl, so_mau, p_str)
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
