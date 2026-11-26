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


def bt_dang8_p1_b2_c7_ds8(self):
    # Dạng 8: Biểu diễn biểu thức tính cước dịch vụ theo ẩn x
    lisdang = ['1', '2']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cuoc_tb = random.choice([30, 32, 35, 38, 40])
        gia_phut = random.choice([700, 800, 900, 1000])
        gia_phut_nghin = gia_phut / 1000
        # Format số thập phân dấu phẩy
        str_gia = str(gia_phut_nghin).replace('.', ',')
        noidungcauhoi = "Một công ty viễn thông đưa ra gói cước điện thoại cố định có cước thuê bao hằng tháng là $%s\\,000$ đồng và giá cước mỗi phút gọi là $%s$ đồng. Gọi $x$ là số phút gọi trong tháng ($x \\in \\mathbb{N}$). Biểu thức biểu thị số tiền phải trả trong tháng (tính theo nghìn đồng) khi sử dụng gói cước này là:" % (cuoc_tb, gia_phut)
        da = "$%s + %sx$" % (cuoc_tb, str_gia)
        s = [
            "$%s + %sx$" % (cuoc_tb, gia_phut),
            "$%sx + %s$" % (cuoc_tb, str_gia),
            "$%s - %sx$" % (cuoc_tb, str_gia)
        ]
        loigiai = "Đổi $%s$ đồng $= %s$ nghìn đồng.\\\\Số tiền cước gọi cho $x$ phút là $%sx$ (nghìn đồng).\\\\Tổng số tiền phải trả trong tháng (tính theo nghìn đồng) là: $%s + %sx$." % (gia_phut, str_gia, str_gia, cuoc_tb, str_gia)
    else:
        mo_cua = random.choice([10, 12, 15])
        gia_km = random.choice([12, 14, 15, 16])
        noidungcauhoi = "Một hãng taxi tính giá mở cửa (cho kilômét đầu tiên) là $%s\\,000$ đồng và mỗi kilômét tiếp theo tính giá $%s\,000$ đồng. Nếu gọi $x$ ($\\text{km}$) ($x > 1$) là quãng đường khách đã đi thì số tiền (tính theo nghìn đồng) khách phải trả là:" % (mo_cua, gia_km)
        da = "$%s + %s(x - 1)$" % (mo_cua, gia_km)
        s = [
            "$%s + %sx$" % (mo_cua, gia_km),
            "$%sx$" % (mo_cua + gia_km),
            "$%sx - %s$" % (gia_km, mo_cua)
        ]
        loigiai = "Vì kilômét đầu tiên tính giá mở cửa là $%s$ nghìn đồng nên quãng đường còn lại tính theo đơn giá $%s$ nghìn đồng/km là $x - 1$ ($\\text{km}$).\\\\Vậy tổng số tiền khách phải trả (tính theo nghìn đồng) là: $%s + %s(x - 1)$." % (mo_cua, gia_km, mo_cua, gia_km)

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    da_d = ('\\True ' + str(da))
    list_1 = [da_d, str(das1), str(das2), str(das3)]
    random.shuffle(list_1)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
