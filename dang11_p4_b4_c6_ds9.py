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


def bt_dang11_p4_b4_c6_ds9(self):
    def fmt_int_vn(n):
        return f"{n:,}".replace(",", "\\,")

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (800, 20, 100, 5, 8450, 5, 15),
            (600, 20, 120, 5, 7280, 2, 4),
            (500, 25, 80, 5, 4050, 1, 3),
            (1000, 50, 60, 5, 6200, 2, 6)
        ])
        gia_chuc_nghin, giam_chuc_nghin, khach_dau, tang_khach, dt_chuc_nghin, x1_val, x2_val = bo_so

        gia_dau = gia_chuc_nghin * 1000
        giam_gia = giam_chuc_nghin * 1000
        doanh_thu = dt_chuc_nghin * 10000
        max_lan = gia_chuc_nghin // giam_chuc_nghin

        tong_x = x1_val + x2_val
        tich_x = x1_val * x2_val
        delta = tong_x**2 - 4 * tich_x
        can_delta = int(math.isqrt(delta))

        gia_toi_uu = gia_dau - giam_gia * x2_val
        khach_toi_uu = khach_dau + tang_khach * x2_val

        noidungcauhoi = ('''Một công ty lữ hành tổ chức tour tham quan Vịnh Hạ Long. Nếu giá vé là $%s$ đồng/người thì có $%s$ khách đăng ký. Cứ mỗi lần giảm giá vé đi $%s$ đồng/người thì số lượng khách đăng ký lại tăng thêm $%s$ người. Công ty muốn đạt tổng doanh thu từ tiền bán vé là $%s$ đồng. \\\\
a) Tìm số lần giảm giá vé để công ty đạt được mức doanh thu trên. \\\\
b) Để thu hút được nhiều khách tham gia nhất mà vẫn đạt doanh thu $%s$ đồng, công ty nên bán vé với giá bao nhiêu?'''
                         %(fmt_int_vn(gia_dau), latex(khach_dau), fmt_int_vn(giam_gia), latex(tang_khach),
                           fmt_int_vn(doanh_thu), fmt_int_vn(doanh_thu)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x$ là số lần giảm giá vé. Điều kiện: $x \\in \\mathbb{N}^*$ và $x < %s$. \\\\
Sau $x$ lần giảm giá, giá mỗi vé là $%s - %sx$ (đồng) và tổng số khách đăng ký là $%s + %sx$ (người). \\\\
Vì tổng doanh thu đạt $%s$ đồng nên ta có phương trình: \\\\
$(%s - %sx)(%s + %sx) = %s$. \\\\
Khai triển và rút gọn hai vế, ta được phương trình bậc hai: \\\\
$x^2 - %sx + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot %s = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{%s - %s}{2} = %s$ (thoả mãn điều kiện); \\quad $x_2 = \\frac{%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy công ty có thể giảm giá vé $%s$ lần hoặc $%s$ lần để đạt được doanh thu mong muốn.
\\item Để thu hút được nhiều khách tham gia nhất, công ty cần chọn số lần giảm giá lớn hơn là $x = %s$. \\\\
Khi đó, giá bán mỗi vé là: $%s - %s \\cdot %s = %s$ (đồng/người) với $%s$ khách tham gia.
\\end{enumEX}'''
                   %(latex(max_lan), fmt_int_vn(gia_dau), fmt_int_vn(giam_gia), latex(khach_dau), latex(tang_khach),
                     fmt_int_vn(doanh_thu), fmt_int_vn(gia_dau), fmt_int_vn(giam_gia), latex(khach_dau), latex(tang_khach), fmt_int_vn(doanh_thu),
                     latex(tong_x), latex(tich_x),
                     latex(tong_x), latex(tich_x), latex(delta), latex(can_delta),
                     latex(tong_x), latex(can_delta), latex(x1_val), latex(tong_x), latex(can_delta), latex(x2_val),
                     latex(x1_val), latex(x2_val),
                     latex(x2_val), fmt_int_vn(gia_dau), fmt_int_vn(giam_gia), latex(x2_val), fmt_int_vn(gia_toi_uu), latex(khach_toi_uu)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
