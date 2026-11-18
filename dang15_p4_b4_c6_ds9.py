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


def bt_dang15_p4_b4_c6_ds9(self):
    def fmt_vn(val):
        s = f"{val.normalize():f}"
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (200, 50, 8),
            (200, 60, 10),
            (300, 80, 10),
            (250, 50, 8),
            (400, 100, 5)
        ])
        von_dau, rut_ra, lai_pt = bo_so
        x_dec = Decimal(lai_pt) / Decimal('100')
        t_duong = Decimal('1') + x_dec

        nam_1_con = Decimal(von_dau) * t_duong - Decimal(rut_ra)
        tong_thu = nam_1_con * t_duong

        g = math.gcd(von_dau, math.gcd(rut_ra, int(tong_thu)))
        a_pt = von_dau // g
        b_pt = -rut_ra // g
        c_pt = -int(tong_thu) // g

        delta = b_pt**2 - 4 * a_pt * c_pt
        can_delta = int(math.isqrt(delta))
        t_am = Decimal(-b_pt - can_delta) / Decimal(2 * a_pt)

        tong_thu_str = fmt_vn(tong_thu)
        nam_1_str = fmt_vn(nam_1_con)
        t_duong_str = fmt_vn(t_duong)
        t_am_str = fmt_vn(t_am)
        x_dec_str = fmt_vn(x_dec)

        noidungcauhoi = ('''Chị Mai đầu tư $%s$ triệu đồng vào một chứng chỉ quỹ với lãi suất không đổi theo năm (lãi nhập gốc sau mỗi năm). Hết năm thứ nhất, chị Mai rút ra $%s$ triệu đồng để chi tiêu việc gia đình, số tiền còn lại tiếp tục để đầu tư sang năm thứ hai. Hết năm thứ hai, chị Mai tất toán toàn bộ tài khoản và nhận về $%s$ triệu đồng. \\\\
a) Tính lãi suất năm của chứng chỉ quỹ này. \\\\
b) Tính số tiền còn lại trong tài khoản của chị Mai ngay sau khi rút tiền ở cuối năm thứ nhất.'''
                         %(latex(von_dau), latex(rut_ra), tong_thu_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x$ là lãi suất năm của chứng chỉ quỹ ($x$ viết dưới dạng số thập phân). Điều kiện: $x > 0$. \\\\
Sau năm thứ nhất, tổng số tiền cả vốn lẫn lãi là $%s(1 + x)$ (triệu đồng). \\\\
Sau khi rút ra $%s$ triệu đồng, số tiền còn lại để tiếp tục đầu tư sang năm thứ hai là $%s(1 + x) - %s$ (triệu đồng). \\\\
Hết năm thứ hai, số tiền chị Mai nhận về là $[%s(1 + x) - %s](1 + x)$ (triệu đồng). \\\\
Theo đề bài, ta có phương trình: \\\\
$[%s(1 + x) - %s](1 + x) = %s$. \\\\
Đặt $t = 1 + x$ ($t > 1$), phương trình trở thành: \\\\
$%st^2 - %st - %s = 0$ hay $%st^2 - %st - %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot %s \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$t_1 = %s$ (loại); \\quad $t_2 = %s$ (thoả mãn điều kiện $t > 1$). \\\\
Với $t = %s \\Rightarrow 1 + x = %s \\Rightarrow x = %s$ (thoả mãn điều kiện). \\\\
Vậy lãi suất năm của chứng chỉ quỹ là $%s\\%%$/năm.
\\item Số tiền còn lại ngay sau khi rút tiền ở cuối năm thứ nhất là: $%s \\cdot (1 + %s) - %s = %s$ (triệu đồng).
\\end{enumEX}'''
                   %(latex(von_dau), latex(rut_ra), latex(von_dau), latex(rut_ra),
                     latex(von_dau), latex(rut_ra), latex(von_dau), latex(rut_ra), tong_thu_str,
                     latex(von_dau), latex(rut_ra), tong_thu_str, latex(a_pt), latex(abs(b_pt)), latex(abs(c_pt)),
                     latex(abs(b_pt)), latex(a_pt), latex(abs(c_pt)), latex(delta), latex(can_delta),
                     t_am_str, t_duong_str, t_duong_str, t_duong_str, x_dec_str,
                     latex(lai_pt), latex(von_dau), x_dec_str, latex(rut_ra), nam_1_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
