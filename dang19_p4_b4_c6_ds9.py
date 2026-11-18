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


def bt_dang19_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (1200, 60, 8, 10, 2),
            (1000, 50, 5, 10, 3),
            (1500, 75, 6, 15, 2),
            (900, 45, 5, 15, 3),
            (1600, 80, 5, 20, 3)
        ])
        tong_m, m_kh, ngay_dau, tang_m, som_ngay = bo_so
        ngay_kh = tong_m // m_kh
        ngay_tt = ngay_kh - som_ngay

        a_pt = som_ngay
        b_pt = (som_ngay + ngay_dau) * tang_m
        c_pt = -tong_m * tang_m

        g = math.gcd(a_pt, math.gcd(b_pt, abs(c_pt)))
        a_pt //= g
        b_pt //= g
        c_pt //= g

        delta = b_pt**2 - 4 * a_pt * c_pt
        can_delta = int(math.isqrt(delta))
        nghiem_am = Rational(-b_pt - can_delta, 2 * a_pt)

        noidungcauhoi = ('''Một đội công nhân nhận thầu làm $%s\\text{ m}$ đường giao thông nông thôn trong một thời gian quy định. Trong $%s$ ngày đầu, đội làm đúng theo tiến độ kế hoạch. Những ngày còn lại, nhờ bổ sung thêm máy móc nên mỗi ngày đội làm vượt mức $%s\\text{ m}$ đường so với kế hoạch. Vì vậy, đội đã hoàn thành toàn bộ công việc sớm hơn quy định $%s$ ngày. \\\\
a) Tính số mét đường đội công nhân dự định làm mỗi ngày theo kế hoạch. \\\\
b) Tính thời gian thực tế đội công nhân đã hoàn thành toàn bộ đoạn đường.'''
                         %(latex(tong_m), latex(ngay_dau), latex(tang_m), latex(som_ngay)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x\\text{ (m)}$ là số mét đường đội dự định làm mỗi ngày theo kế hoạch. Điều kiện: $x > 0$. \\\\
Thời gian hoàn thành công việc theo kế hoạch là $\\frac{%s}{x}$ (ngày). \\\\
Trong $%s$ ngày đầu, đội làm được $%sx\\text{ (m)}$ nên khối lượng công việc còn lại là $%s - %sx\\text{ (m)}$. \\\\
Năng suất những ngày còn lại là $x + %s\\text{ (m/ngày)}$ nên thời gian làm phần việc còn lại là $\\frac{%s - %sx}{x + %s}$ (ngày). \\\\
Vì đội hoàn thành sớm hơn quy định $%s$ ngày nên ta có phương trình: \\\\
$%s + \\frac{%s - %sx}{x + %s} = \\frac{%s}{x} - %s$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$%s = 0$. \\\\
Ta có: $\\Delta = %s^2 - 4 \\cdot %s \\cdot (%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = %s$ (loại); \\quad $x_2 = %s$ (thoả mãn điều kiện). \\\\
Vậy theo kế hoạch ban đầu, mỗi ngày đội công nhân phải làm $%s\\text{ m}$ đường.
\\item Thời gian hoàn thành theo kế hoạch là $\\frac{%s}{%s} = %s$ (ngày). \\\\
Vậy thời gian thực tế đội đã hoàn thành công việc là: $%s - %s = %s$ (ngày).
\\end{enumEX}'''
                   %(latex(tong_m), latex(ngay_dau), latex(ngay_dau), latex(tong_m), latex(ngay_dau),
                     latex(tang_m), latex(tong_m), latex(ngay_dau), latex(tang_m),
                     latex(som_ngay), latex(ngay_dau), latex(tong_m), latex(ngay_dau), latex(tang_m), latex(tong_m), latex(som_ngay),
                     latex(a_pt * x**2 + b_pt * x + c_pt),
                     latex(b_pt), latex(a_pt), latex(c_pt), latex(delta), latex(can_delta),
                     latex(nghiem_am), latex(m_kh), latex(m_kh),
                     latex(tong_m), latex(m_kh), latex(ngay_kh), latex(ngay_kh), latex(som_ngay), latex(ngay_tt)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
