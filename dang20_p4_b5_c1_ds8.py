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


def bt_dang20_p4_b5_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        b = random.choice([4, 5, 6])
        Rong = b * x * y
        Dai = 3 * x**2 + 2 * x * y - y**2
        S_dat = expand(Dai * Rong)
        Chu_vi = 2 * (Dai + Rong)

        x0 = random.choice([3, 4])
        y0 = random.choice([2, 3])
        don_gia = random.choice([120, 150, 200])

        cv_so = int(Chu_vi.subs({x: x0, y: y0}))
        chi_phi = cv_so * don_gia

        noidungcauhoi = ('''Một trang trại quy hoạch một khu đất trồng cây ăn quả dạng hình chữ nhật có diện tích được biểu thị bởi đa thức $S = %s$ ($\\text{m}^{2}$), biết chiều rộng của khu đất là $%s$ (m) (với $x > 0, y > 0$ và $%s > 0$). \\\\
                         a) Tìm đa thức biểu thị chiều dài và đa thức biểu thị chu vi của khu đất hình chữ nhật đó. \\\\
                         b) Với $x = %s$ (m) và $y = %s$ (m), người ta muốn làm hàng rào bao quanh khu đất với chi phí $%s$ nghìn đồng cho mỗi mét dài hàng rào. Tính tổng chi phí làm hàng rào cho khu đất trên.'''
                         % (latex(S_dat), latex(Rong), latex(Dai), x0, y0, don_gia))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Đa thức biểu thị chiều dài của khu đất hình chữ nhật là:
                        \\begin{align*}
                        S : (%s) = (%s) : (%s) = %s \\,\\, (\\text{m}).
                        \\end{align*}
                        Đa thức biểu thị chu vi của khu đất hình chữ nhật là:
                        \\begin{align*}
                        C = 2 \\cdot (%s + %s) = %s \\,\\, (\\text{m}).
                        \\end{align*}
                        \\item Thay $x = %s$ và $y = %s$ vào đa thức chu vi $C$, ta được độ dài hàng rào cần làm là:
                        \\begin{align*}
                        C = %s \\,\\, (\\text{m}).
                        \\end{align*}
                        Tổng chi phí làm hàng rào cho khu đất trên là:
                        \\begin{align*}
                        %s \\cdot %s = %s \\,\\, (\\text{nghìn đồng}).
                        \\end{align*}
                        \\end{enumEX}'''
                   % (latex(Rong), latex(S_dat), latex(Rong), latex(Dai),
                      latex(Dai), latex(Rong), latex(Chu_vi),
                      x0, y0, cv_so, cv_so, don_gia, chi_phi))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
