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


def bt_dang12_p1_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_so = random.choice([
            ([2, 5, 8], 5, 'chia hết cho $5$'),
            ([1, 2, 4], 2, 'chia hết cho $2$'),
            ([2, 3, 6], 4, 'chia hết cho $4$'),
            ([1, 3, 5], 3, 'chia hết cho $3$')
        ])
        ds, uoc, dk_text = bo_so
        a, b, c = ds[0], ds[1], ds[2]
        all_nums = [10 * i + j for i in ds for j in ds]
        thuan_loi = [num for num in all_nums if num % uoc == 0]
        so_tl = len(thuan_loi)
        xs = Rational(so_tl, 9)
        da_str = '$\\dfrac{%s}{%s}$' % (xs.p, xs.q)
        chuoi_tl = '; '.join([str(x) for x in thuan_loi])

        du = [da_str]
        da = random.choice(du)
        tat_ca = ['$\\dfrac{1}{9}$', '$\\dfrac{2}{9}$', '$\\dfrac{1}{3}$', '$\\dfrac{4}{9}$', '$\\dfrac{5}{9}$', '$\\dfrac{2}{3}$']
        tat_ca.remove(da_str)
        das1 = random.choice(tat_ca)
        tat_ca.remove(das1)
        das2 = random.choice(tat_ca)
        tat_ca.remove(das2)
        das3 = random.choice(tat_ca)

        noidungcauhoi = ('''Cho hai túi I và II, mỗi túi chứa $3$ tấm thẻ ghi các số $%s; %s; %s$. Rút ngẫu nhiên từ mỗi túi một tấm thẻ và ghép thành số có hai chữ số, trong đó chữ số rút từ túi I làm hàng chục. Xác suất để số tạo thành %s là'''
                         % (a, b, c, dk_text))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|}
\\hline
Túi I $\\backslash$ Túi II & $%s$ & $%s$ & $%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
$%s$ & $%s%s$ & $%s%s$ & $%s%s$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (a, b, c, a, a, a, a, b, a, c, b, b, a, b, b, b, c, c, c, a, c, b, c, c)

        loigiai = ('''Ta lập bảng liệt kê tất cả các số có hai chữ số tạo thành:%s
Không gian mẫu $\\Omega$ gồm $9$ số đồng khả năng nên $n(\\Omega) = 9$.\\\\
Gọi $E$ là biến cố ``Số tạo thành %s''.\\\\
Các kết quả thuận lợi cho biến cố $E$ là: $%s$. Suy ra $n(E) = %s$.\\\\
Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{n(E)}{n(\\Omega)} = \\dfrac{%s}{%s}$.'''
                   % (bang_mau, dk_text, chuoi_tl, so_tl, xs.p, xs.q))

    # Xuất câu trắc nghiệm
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
