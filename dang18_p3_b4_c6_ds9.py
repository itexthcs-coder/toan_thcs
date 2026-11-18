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


def bt_dang18_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_xe_vg = [(30, 40, 50), (15, 20, 25), (45, 60, 75), (20, 48, 52), (24, 32, 40)]
        v2, v1, kc = random.choice(bo_xe_vg)
        t = random.choice([1, 2])
        kc_t = kc * t
        dv = v1 - v2
        c_val = (kc**2 - dv**2) // 2
        delta_val = dv**2 + 4 * c_val
        sqrt_d = int(math.isqrt(delta_val))
        x1 = (-dv - sqrt_d) // 2
        x2 = (-dv + sqrt_d) // 2

        tikz = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (0,2.8);
    \\coordinate (B) at (3.6,0);
    \\draw[line width=1pt, ->] (O)--(0,3.5);
    \\draw[line width=1pt, ->] (O)--(4.3,0);
    \\draw[line width=1pt, dashed] (A)--(B);
    \\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
    \\fill (O) circle (1pt) node[below left] {$O$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\node[right] at (1.9,1.5) {$%s\\text{ km}$};
\\end{tikzpicture}
\\end{center}''' % (str(kc_t)))

        noidungcauhoi = ('''Hai chiếc xe xuất phát cùng một lúc từ một ngã tư đường phố theo hai hướng vuông góc với nhau. Xe thứ nhất chạy với vận tốc lớn hơn xe thứ hai là $%s\\text{ km/h}$. Sau $%s$ giờ, khoảng cách theo đường chim bay giữa hai xe là $%s\\text{ km}$. Tính vận tốc của xe thứ hai (đơn vị: km/h).'''
                         % (str(dv), str(t), str(kc_t)))

        loigiai = ('''%s\\\\
                   Gọi vận tốc của xe thứ hai là $x$ (km/h). Điều kiện: $x > 0$.\\\\
                   Khi đó, vận tốc của xe thứ nhất là $x + %s$ (km/h).\\\\
                   Sau $%s$ giờ, quãng đường xe thứ hai đi được là $%sx$ (km), quãng đường xe thứ nhất đi được là $%s(x + %s)$ (km).\\\\
                   Vì hai xe đi theo hai hướng vuông góc với nhau nên áp dụng định lí Pythagore, ta có phương trình:\\\\
                   $(%sx)^2 + [%s(x + %s)]^2 = %s^2$.\\\\
                   Chia cả hai vế cho $%s$, ta được:\\\\
                   $x^2 + (x + %s)^2 = %s^2$\\\\
                   $2x^2 + %sx - %s = 0$ hay $x^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{2} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{2} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy vận tốc của xe thứ hai là $%s\\text{ km/h}$.'''
                   % (tikz, str(dv), str(t), str(t), str(t), str(dv),
                      str(t), str(t), str(dv), str(kc_t), str(t**2),
                      str(dv), str(kc), str(2 * dv), str(kc**2 - dv**2), str(dv), str(c_val),
                      str(dv), str(c_val), str(delta_val), str(sqrt_d),
                      str(dv), str(sqrt_d), str(x1), str(dv), str(sqrt_d), str(x2), str(v2)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(v2))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
