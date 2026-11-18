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


def bt_dang6_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (15, 5, 20, 15, Rational(1, 4)),
            (24, 4, 24, 12, Rational(1, 5)),
            (30, 5, 30, 12, Rational(1, 5)),
            (18, 3, 18, 12, Rational(1, 5)),
            (20, 4, 20, 15, Rational(1, 4)),
            (36, 6, 24, 30, Rational(1, 2))
        ])
        quang_duong, giam_v, v_di, phut_tre, gio_tre = bo_so
        v_ve = v_di - giam_v
        c_pt = (quang_duong * giam_v) // gio_tre
        nghiem_am = -(v_di - giam_v)
        delta = giam_v**2 + 4 * c_pt
        can_delta = int(math.isqrt(delta))

        noidungcauhoi = ('''Bạn Minh đi xe đạp điện từ nhà đến thư viện thành phố cách nhau $%s\\text{ km}$. Lúc về, do ngược gió nên vận tốc của Minh giảm đi $%s\\text{ km/h}$ so với lúc đi, vì vậy thời gian lúc về nhiều hơn thời gian lúc đi là $%s$ phút. \\\\
a) Tính vận tốc của Minh lúc đi từ nhà đến thư viện. \\\\
b) Tính vận tốc của Minh lúc đi từ thư viện về nhà.'''
                         %(latex(quang_duong), latex(giam_v), latex(phut_tre)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đổi $%s$ phút $= %s$ giờ. \\\\
Gọi $x\\text{ (km/h)}$ là vận tốc của Minh lúc đi. Điều kiện: $x > %s$. \\\\
Vận tốc của Minh lúc về là $x - %s\\text{ (km/h)}$. \\\\
Thời gian Minh đi từ nhà đến thư viện là $\\frac{%s}{x}$ (giờ) và thời gian lúc về là $\\frac{%s}{x - %s}$ (giờ). \\\\
Vì thời gian lúc về nhiều hơn thời gian lúc đi là $%s$ giờ nên ta có phương trình: \\\\
$\\frac{%s}{x - %s} - \\frac{%s}{x} = %s$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$x^2 - %sx - %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{%s - %s}{2} = %s$ (loại); \\quad $x_2 = \\frac{%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy vận tốc của Minh lúc đi là $%s\\text{ km/h}$.
\\item Vận tốc của Minh lúc đi từ thư viện về nhà là: $%s - %s = %s\\text{ (km/h)}$.
\\end{enumEX}'''
                   %(latex(phut_tre), latex(gio_tre), latex(giam_v),
                     latex(giam_v), latex(quang_duong), latex(quang_duong), latex(giam_v),
                     latex(gio_tre), latex(quang_duong), latex(giam_v), latex(quang_duong), latex(gio_tre),
                     latex(giam_v), latex(c_pt),
                     latex(giam_v), latex(c_pt), latex(delta), latex(can_delta),
                     latex(giam_v), latex(can_delta), latex(nghiem_am), latex(giam_v), latex(can_delta), latex(v_di),
                     latex(v_di), latex(v_di), latex(giam_v), latex(v_ve)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
