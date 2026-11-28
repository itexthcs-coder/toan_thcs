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


def bt_dang20_p3_b2_c8_ds8(self):
    # Dạng 20: Tổng hợp biến cố hợp và biến cố đối trong tình huống trò chơi rút thăm
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tong_tham = random.choice([40, 50, 60, 80, 100])
        d1, d2 = random.choice([(10, 4), (10, 6), (12, 8), (15, 10)])
        
        tap_d1 = [n for n in range(1, tong_tham + 1) if n % d1 == 0]
        tap_d2 = [n for n in range(1, tong_tham + 1) if n % d2 == 0]
        tap_trung = sorted(list(set(tap_d1) | set(tap_d2)))
        tap_giao = sorted(list(set(tap_d1) & set(tap_d2)))
        
        so_trung = len(tap_trung)
        so_khong_trung = tong_tham - so_trung
        
        p_dec = (Decimal(so_khong_trung) / Decimal(tong_tham)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (4.2,1.8);\n"
            "\\draw[line width=1pt] (0.4,1.8) -- (0.8,2.3) -- (3.4,2.3) -- (3.8,1.8);\n"
            "\\node at (2.1,0.9) {Hộp $%s$ lá thăm ($1 \\rightarrow %s$)};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % (tong_tham, tong_tham)
        )
        
        noidungcauhoi = (
            "Trong một buổi tiệc tất niên có $%s$ lá thăm may mắn được đánh số từ $1$ đến $%s$. "
            "Ban tổ chức quy định: thăm mang số chia hết cho $%s$ trúng giải Nhất; thăm mang số chia hết cho $%s$ "
            "(nhưng không chia hết cho $%s$) trúng giải Nhì; các thăm còn lại không trúng giải. "
            "Một nhân viên rút ngẫu nhiên một lá thăm. Tính xác suất để nhân viên đó không trúng giải "
            "(viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm).\n%s"
            % (tong_tham, tong_tham, d1, d2, d1, hinh_ve)
        )
        
        loigiai = (
            "Có tất cả $%s$ lá thăm được đánh số từ $1$ đến $%s$. Khi rút ngẫu nhiên một lá thăm, có $%s$ kết quả có thể là đồng khả năng.\\\n"
            "- Từ $1$ đến $%s$ có $%s$ số chia hết cho $%s$ (trúng giải Nhất).\\\n"
            "- Từ $1$ đến $%s$ có $%s$ số chia hết cho $%s$, trong đó có $%s$ số chia hết cho cả $%s$ và $%s$. "
            "Do đó có $%s - %s = %s$ lá thăm trúng giải Nhì.\\\n"
            "Tổng số lá thăm trúng giải là: $%s + %s = %s$ (lá thăm).\\\n"
            "Số lá thăm không trúng giải là: $%s - %s = %s$ (lá thăm).\\\n"
            "Vậy xác suất để nhân viên đó không trúng giải là: $P = \\dfrac{%s}{%s} \\approx %s$."
            % (tong_tham, tong_tham, tong_tham,
               tong_tham, len(tap_d1), d1,
               tong_tham, len(tap_d2), d2, len(tap_giao), d1, d2,
               len(tap_d2), len(tap_giao), len(tap_d2) - len(tap_giao),
               len(tap_d1), len(tap_d2) - len(tap_giao), so_trung,
               tong_tham, so_trung, so_khong_trung,
               so_khong_trung, tong_tham, p_str)
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
