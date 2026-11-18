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


def bt_dang14_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (40, 10, 30, 2),
            (45, 15, 30, 2),
            (50, 10, 30, 2),
            (40, 20, 30, 2),
            (60, 15, 30, 2)
        ])
        v_tai, hon_v, tre_phut, t_tai = bo_so
        v_khach = v_tai + hon_v
        tre_gio = Rational(tre_phut, 60)
        t_khach = t_tai - tre_gio
        s_tai = int(v_tai * t_tai)
        s_khach = int(v_khach * t_khach)
        tong_s = s_tai + s_khach

        a_pt = int(tre_gio * 2)
        b_pt = int(tre_gio * 2 * hon_v - 2 * (s_tai - s_khach))
        c_pt = int(-2 * s_tai * hon_v)

        delta = b_pt**2 - 4 * a_pt * c_pt
        can_delta = int(math.isqrt(delta))
        nghiem_am = Rational(-b_pt - can_delta, 2 * a_pt)
        gio_gap = 7 + t_tai

        noidungcauhoi = ('''Hai thành phố $A$ và $B$ cách nhau $%s\\text{ km}$. Lúc $7$ giờ sáng, một xe tải khởi hành từ $A$ đi về $B$. Sau đó $%s$ phút, một xe khách khởi hành từ $B$ đi về $A$ với vận tốc lớn hơn vận tốc xe tải là $%s\\text{ km/h}$. Hai xe gặp nhau tại một trạm dừng nghỉ cách $A$ một khoảng $%s\\text{ km}$. \\\\
a) Tính vận tốc của xe tải và vận tốc của xe khách. \\\\
b) Hỏi hai xe gặp nhau lúc mấy giờ?'''
                         %(latex(tong_s), latex(tre_phut), latex(hon_v), latex(s_tai)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đổi $%s$ phút $= %s$ giờ. Quãng đường xe khách đi được từ lúc xuất phát đến khi gặp nhau là: $%s - %s = %s\\text{ (km)}$. \\\\
Gọi $x\\text{ (km/h)}$ là vận tốc của xe tải. Điều kiện: $x > 0$. \\\\
Vận tốc của xe khách là $x + %s\\text{ (km/h)}$. \\\\
Thời gian xe tải đi đến điểm gặp nhau là $\\frac{%s}{x}$ (giờ) và thời gian xe khách đi là $\\frac{%s}{x + %s}$ (giờ). \\\\
Vì xe khách xuất phát sau xe tải $%s$ giờ nên ta có phương trình: \\\\
$\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$%s = 0$. \\\\
Ta có: $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = %s$ (loại); \\quad $x_2 = %s$ (thoả mãn điều kiện). \\\\
Vậy vận tốc của xe tải là $%s\\text{ km/h}$ và vận tốc của xe khách là $%s + %s = %s\\text{ km/h}$.
\\item Thời gian xe tải đi từ $A$ đến điểm gặp nhau là: $\\frac{%s}{%s} = %s$ (giờ). \\\\
Vậy hai xe gặp nhau lúc $7 + %s = %s$ giờ sáng cùng ngày.
\\end{enumEX}'''
                   %(latex(tre_phut), latex(tre_gio), latex(tong_s), latex(s_tai), latex(s_khach),
                     latex(hon_v), latex(s_tai), latex(s_khach), latex(hon_v),
                     latex(tre_gio), latex(s_tai), latex(s_khach), latex(hon_v), latex(tre_gio),
                     latex(a_pt * x**2 + b_pt * x + c_pt),
                     latex(b_pt), latex(a_pt), latex(c_pt), latex(delta), latex(can_delta),
                     latex(nghiem_am), latex(v_tai),
                     latex(v_tai), latex(v_tai), latex(hon_v), latex(v_khach),
                     latex(s_tai), latex(v_tai), latex(t_tai), latex(t_tai), latex(gio_gap)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
