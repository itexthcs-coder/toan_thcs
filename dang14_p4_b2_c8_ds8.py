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


def bt_dang14_p4_b2_c8_ds8(self):
    # Dạng 14: Bài toán ngược tìm số lượng phần tử khi biết xác suất biến cố đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            tu_ti, mau_ti = random.choice([(2, 3), (3, 4), (2, 5), (3, 5)])
            k = random.choice([3, 4, 5, 6])
            cam = tu_ti * k
            buoi = mau_ti * k
            cam_buoi = cam + buoi
            chanh = random.choice([10, 12, 15, 18, 20])
            tong = cam_buoi + chanh
            f = frac(cam_buoi, tong)
            if f.denominator <= 10:
                break

        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (7.2,1.1);\n'
            '\\draw[line width=1pt] (2.2,0) -- (2.2,1.1) (4.8,0) -- (4.8,1.1);\n'
            '\\node at (1.1,0.55) {Cây cam};\n'
            '\\node at (3.5,0.55) {Cây bưởi};\n'
            '\\node at (6.0,0.55) {Cây chanh};\n'
            '\\node at (3.6,-0.4) {Vườn ươm có tổng cộng $%s$ cây giống};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % tong

        noidungcauhoi = (
            'Một vườn ươm có $%s$ cây giống gồm ba loại: cam, bưởi và chanh. Trong đó số cây cam bằng $\\frac{%s}{%s}$ số cây bưởi. '
            'Người làm vườn chọn ngẫu nhiên một cây để đem đi trồng. Biết rằng xác suất để không chọn được cây chanh là $%s$. '
            'Tính số cây mỗi loại trong vườn ươm.%s'
        ) % (tong, tu_ti, mau_ti, xs_str, tikz_img)

        loigiai = (
            'Khi chọn ngẫu nhiên một cây trong vườn ươm gồm $%s$ cây thì có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Biến cố ``Không chọn được cây chanh\'\' chính là biến cố ``Chọn được cây cam hoặc cây bưởi\'\'.\\\\\n'
            'Gọi tổng số cây cam và cây bưởi là $S$ (cây, $S \\in \\mathbb{N}^*$, $S < %s$).\\\\\n'
            'Theo đề bài, xác suất để không chọn được cây chanh là $%s$, nên ta có: $\\frac{S}{%s} = %s$.\\\\\n'
            'Suy ra $S = %s \\cdot %s = %s$ (cây).\\\\\n'
            'Do đó, số cây chanh trong vườn ươm là: $%s - %s = %s$ (cây).\\\\\n'
            'Gọi số cây bưởi là $x$ (cây, $x \\in \\mathbb{N}^*$). Khi đó số cây cam là $\\frac{%s}{%s}x$ (cây).\\\\\n'
            'Ta có phương trình: $x + \\frac{%s}{%s}x = %s$\\\\\n'
            '$\\frac{%s}{%s}x = %s$\\\\\n'
            '$x = %s$ (cây).\\\\\n'
            'Suy ra số cây cam là $\\frac{%s}{%s} \\cdot %s = %s$ (cây).\\\\\n'
            'Vậy vườn ươm có $%s$ cây cam, $%s$ cây bưởi và $%s$ cây chanh.'
        ) % (
            tong, tong, tong,
            xs_str, tong, xs_str,
            tong, xs_str, cam_buoi,
            tong, cam_buoi, chanh,
            tu_ti, mau_ti,
            tu_ti, mau_ti, cam_buoi,
            tu_ti + mau_ti, mau_ti, cam_buoi,
            buoi,
            tu_ti, mau_ti, buoi, cam,
            cam, buoi, chanh
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
