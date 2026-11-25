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


def bt_dang1_p4_b2_c6_ds8(self):
    # Dạng 1: Tìm điều kiện xác định, rút gọn phân thức và tính giá trị tại các điểm đặc biệt
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([2, 3])
        tu_str = latex(x**4 - a**4)
        mau_str = latex(expand((x - a) * (x**2 + a**2)))
        x_val = 20 - a
        gt_val = x_val + a

        noidungcauhoi = ('Cho phân thức $P = \\dfrac{%s}{%s}$.\\\n'
                         'a) Tìm điều kiện xác định của phân thức $P$.\\\n'
                         'b) Rút gọn phân thức $P$.\\\n'
                         'c) Tính giá trị của phân thức $P$ tại $x = %s$ (nếu có) và tại $x = %s$.\\\n'
                         'd) Tìm các giá trị của $x$ để phân thức $P$ nhận giá trị bằng $0$.'
                         % (tu_str, mau_str, a, x_val))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Ta phân tích mẫu thức thành nhân tử:\\\n'
                   '$%s = x^2(x - %s) + %s(x - %s) = (x - %s)(x^2 + %s)$.\\\n'
                   'Vì $x^2 + %s > 0$ với mọi $x \\in \\mathbb{R}$ nên mẫu thức khác $0$ khi và chỉ khi $x - %s \\neq 0$, hay $x \\neq %s$.\\\n'
                   'Vậy điều kiện xác định của phân thức $P$ là $x \\neq %s$.\n'
                   '\\item Với $x \\neq %s$, ta rút gọn phân thức $P$:\\\n'
                   '$P = \\dfrac{%s}{%s} = \\dfrac{(x^2 - %s)(x^2 + %s)}{(x - %s)(x^2 + %s)} = \\dfrac{(x - %s)(x + %s)}{x - %s} = x + %s$.\n'
                   '\\item Tại $x = %s$, phân thức $P$ không xác định vì $x = %s$ không thỏa mãn điều kiện xác định.\\\n'
                   'Tại $x = %s$ (thỏa mãn điều kiện xác định $x \\neq %s$), thay vào biểu thức đã rút gọn ta được:\\\n'
                   '$P = %s + %s = %s$.\n'
                   '\\item Để $P = 0$ thì $x + %s = 0$, suy ra $x = -%s$.\\\n'
                   'Giá trị $x = -%s$ thỏa mãn điều kiện xác định $x \\neq %s$. Vậy $x = -%s$ thì $P = 0$.\n'
                   '\\end{enumEX}'
                   % (mau_str, a, a**2, a, a, a**2, a**2, a, a, a, a,
                      tu_str, mau_str, a**2, a**2, a, a**2, a, a, a, a,
                      a, a, x_val, a, x_val, a, gt_val,
                      a, a, a, a, a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
