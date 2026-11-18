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


def bt_dang4_p4_b4_c6_ds9(self):
    def fmt_vn(val):
        s = f"{val:g}"
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        don_t1 = random.choice([1000, 2000, 2500, 4000, 5000])
        phan_tram = random.choice([5, 8, 10, 12, 15, 20])
        x_dec = Rational(phan_tram, 100)
        ti_so = (1 + x_dec)**2
        don_t3 = int(don_t1 * ti_so)
        don_t2 = int(don_t1 * (1 + x_dec))

        ti_so_str = fmt_vn(float(ti_so))
        can_ti_so_str = fmt_vn(float(1 + x_dec))
        x_dec_str = fmt_vn(float(x_dec))
        am_str = fmt_vn(float(-2 - x_dec))

        noidungcauhoi = ('''Một cửa hàng kinh doanh trực tuyến ghi nhận số lượng đơn hàng trong tháng $1$ là $%s$ đơn. Nhờ chạy chiến dịch quảng bá hiệu quả, số lượng đơn hàng tăng đều qua các tháng với tỉ lệ phần trăm mỗi tháng là như nhau. Đến tháng $3$ cùng năm, cửa hàng đạt được $%s$ đơn hàng. \\\\
a) Tính tỉ lệ phần trăm tăng trưởng đơn hàng trung bình mỗi tháng của cửa hàng. \\\\
b) Tính số đơn hàng mà cửa hàng đã đạt được trong tháng $2$.'''
                         %(latex(don_t1), latex(don_t3)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x$ là tỉ lệ tăng trưởng đơn hàng mỗi tháng ($x$ viết dưới dạng số thập phân). Điều kiện: $x > 0$. \\\\
Số đơn hàng đạt được trong tháng $2$ là $%s(1 + x)$ (đơn). \\\\
Số đơn hàng đạt được trong tháng $3$ là $%s(1 + x)(1 + x) = %s(1 + x)^2$ (đơn). \\\\
Theo đề bài, đến tháng $3$ cửa hàng đạt $%s$ đơn hàng nên ta có phương trình: \\\\
$%s(1 + x)^2 = %s$ hay $(1 + x)^2 = %s$. \\\\
Suy ra $1 + x = %s$ hoặc $1 + x = -%s$. \\\\
Giải ra ta được $x_1 = %s$ (thoả mãn điều kiện) hoặc $x_2 = %s$ (loại). \\\\
Vậy tỉ lệ tăng trưởng đơn hàng trung bình mỗi tháng của cửa hàng là $%s\\%%$.
\\item Số đơn hàng cửa hàng đạt được trong tháng $2$ là: $%s \\cdot (1 + %s) = %s$ (đơn).
\\end{enumEX}'''
                   %(latex(don_t1), latex(don_t1), latex(don_t1),
                     latex(don_t3), latex(don_t1), latex(don_t3), ti_so_str,
                     can_ti_so_str, can_ti_so_str, x_dec_str, am_str,
                     latex(phan_tram), latex(don_t1), x_dec_str, latex(don_t2)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
