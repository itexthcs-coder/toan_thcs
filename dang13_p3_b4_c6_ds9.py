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


def bt_dang13_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ns_kh = random.choice([40, 50, 60, 80])
        ngay_kh = random.choice([20, 24, 25, 30])
        tong_kh = ns_kh * ngay_kh
        vuot_ns = random.choice([10, 15, 20])
        som_ngay = random.choice([2, 3, 4])
        tong_tt = (ns_kh + vuot_ns) * (ngay_kh - som_ngay)
        lam_them = tong_tt - tong_kh
        a_c = som_ngay
        b_c = som_ngay * vuot_ns + lam_them
        c_c = -tong_kh * vuot_ns
        delta_val = b_c**2 - 4 * a_c * c_c
        sqrt_d = int(math.isqrt(delta_val))
        x1_frac = Rational(-b_c - sqrt_d, 2 * a_c)
        x2_val = (-b_c + sqrt_d) // (2 * a_c)

        noidungcauhoi = ('''Một phân xưởng theo kế hoạch phải sản xuất $%s$ sản phẩm trong một số ngày quy định. Do cải tiến kĩ thuật, mỗi ngày phân xưởng làm vượt mức $%s$ sản phẩm nên không những hoàn thành sớm hơn dự định $%s$ ngày mà còn làm thêm được $%s$ sản phẩm. Tính số sản phẩm phân xưởng phải làm mỗi ngày theo kế hoạch.'''
                         % (str(tong_kh), str(vuot_ns), str(som_ngay), str(lam_them)))

        loigiai = ('''Gọi số sản phẩm phân xưởng phải làm mỗi ngày theo kế hoạch là $x$ (sản phẩm). Điều kiện: $x \\in \\mathbb{N}^*$.\\\\
                   Thời gian hoàn thành công việc theo kế hoạch là $\\dfrac{%s}{x}$ (ngày).\\\\
                   Thực tế, mỗi ngày phân xưởng làm được $x + %s$ (sản phẩm) và tổng số sản phẩm làm được là $%s + %s = %s$ (sản phẩm), nên thời gian thực tế đã làm là $\\dfrac{%s}{x + %s}$ (ngày).\\\\
                   Vì phân xưởng hoàn thành sớm hơn dự định $%s$ ngày nên ta có phương trình:\\\\
                   $\\dfrac{%s}{x} - \\dfrac{%s}{x + %s} = %s$.\\\\
                   Quy đồng mẫu và khử mẫu hai vế của phương trình, ta được:\\\\
                   $%s(x + %s) - %sx = %sx(x + %s)$\\\\
                   $%sx^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = %s^2 - 4 \\cdot %s \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{%s} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{%s} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy theo kế hoạch, mỗi ngày phân xưởng phải làm $%s$ sản phẩm.'''
                   % (str(tong_kh), str(vuot_ns), str(tong_kh), str(lam_them), str(tong_tt),
                      str(tong_tt), str(vuot_ns), str(som_ngay),
                      str(tong_kh), str(tong_tt), str(vuot_ns), str(som_ngay),
                      str(tong_kh), str(vuot_ns), str(tong_tt), str(som_ngay), str(vuot_ns),
                      str(a_c), str(b_c), str(abs(c_c)),
                      str(b_c), str(a_c), str(abs(c_c)), str(delta_val), str(sqrt_d),
                      str(b_c), str(sqrt_d), str(2 * a_c), latex(x1_frac), str(b_c), str(sqrt_d), str(2 * a_c), str(x2_val), str(ns_kh)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(ns_kh))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
