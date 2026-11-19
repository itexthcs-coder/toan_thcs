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


def bt_dang4_p3_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        bo_the = random.choice([
            ([1, 2, 4, 7], [2, 5], 3, 'là bội của $3$'),
            ([1, 3, 5, 7], [2, 4], 4, 'chia hết cho $4$'),
            ([2, 3, 4, 6], [1, 5], 5, 'chia hết cho $5$')
        ])
        h1, h2, uoc, nd_dk = bo_the
        a1, a2, a3, a4 = h1
        b1, b2 = h2
        all_nums = [10 * x + y for x in h1 for y in h2]
        tl_nums = [num for num in all_nums if num % uoc == 0]
        so_tl = len(tl_nums)
        xs = Rational(so_tl, 8)
        kq_val = float(xs)
        kq_str = ('%g' % kq_val).replace('.', ',')
        chuoi_tl = '; '.join([str(x) for x in tl_nums])

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Hộp 1 $\\backslash$ Hộp 2 & $%s$ & $%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (b1, b2, a1, a1, b1, a1, b2, a2, a2, b1, a2, b2, a3, a3, b1, a3, b2, a4, a4, b1, a4, b2)

        noidungcauhoi = ('''Hộp thứ nhất chứa $4$ tấm thẻ ghi các số $%s; %s; %s; %s$. Hộp thứ hai chứa $2$ tấm thẻ ghi các số $%s; %s$. Rút ngẫu nhiên từ mỗi hộp một tấm thẻ và ghép thành số có hai chữ số, trong đó chữ số rút từ hộp thứ nhất đứng ở hàng chục. Tính xác suất của biến cố $C$: ``Số tạo thành %s''.'''
                         % (a1, a2, a3, a4, b1, b2, nd_dk))

        loigiai = ('''Ta lập bảng liệt kê các số có hai chữ số được tạo thành:%s
Không gian mẫu $\\Omega$ gồm $8$ số đồng khả năng nên $n(\\Omega) = 8$.\\\\
Các kết quả thuận lợi cho biến cố $C$ (số tạo thành %s) là: $%s$, suy ra $n(C) = %s$.\\\\
Vậy xác suất của biến cố $C$ là $P(C) = \\dfrac{%s}{8} = %s$.'''
                   % (bang_mau, nd_dk, chuoi_tl, so_tl, so_tl, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
