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


def bt_dang5_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        loi_di = randint(1, 2)
        canh_co = randint(4, 10)
        canh_san = canh_co + 2 * loi_di
        dt_co = canh_co**2
        dt_san = canh_san**2
        dt_loi_di = dt_san - dt_co
        hai_loi = 2 * loi_di
        nghiem_am = -canh_co + hai_loi

        noidungcauhoi = ('''Một sân thượng hình vuông có cạnh bằng $x\\text{ (m)}$. Chủ nhà muốn làm một lối đi rộng $%s\\text{ m}$ chạy xung quanh sát mép tường của sân thượng, phần diện tích hình vuông ở chính giữa còn lại dùng để trồng cỏ nhân tạo. Biết diện tích phần trồng cỏ nhân tạo bằng $%s\\text{ m}^2$. \\\\
a) Tính độ dài cạnh của sân thượng và diện tích toàn bộ sân thượng. \\\\
b) Tính diện tích phần lối đi lát gạch xung quanh sân thượng. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) rectangle (3.6,3.6);
\\draw[line width=1pt] (0.6,0.6) rectangle (3,3);
\\draw[line width=1pt, <->] (0,1.8) -- (0.6,1.8) node[midway, above] {$%s\\text{ m}$};
\\node[below] at (1.8,0) {$x\\text{ (m)}$};
\\node at (1.8,1.8) {$%s\\text{ m}^2$};
\\end{tikzpicture}
\\end{center}'''
                         %(latex(loi_di), latex(dt_co), latex(loi_di), latex(dt_co)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Điều kiện của cạnh sân thượng là $x > %s$. \\\\
Vì lối đi rộng $%s\\text{ m}$ chạy xung quanh sát mép tường nên độ dài cạnh của hình vuông trồng cỏ nhân tạo ở chính giữa là $x - %s\\text{ (m)}$. \\\\
Theo đề bài, diện tích phần trồng cỏ nhân tạo bằng $%s\\text{ m}^2$ nên ta có phương trình: \\\\
$(x - %s)^2 = %s$. \\\\
Suy ra $x - %s = %s$ hoặc $x - %s = -%s$. \\\\
Giải ra ta được $x_1 = %s$ (thoả mãn điều kiện) hoặc $x_2 = %s$ (loại). \\\\
Vậy độ dài cạnh của sân thượng là $%s\\text{ m}$ và diện tích toàn bộ sân thượng là $%s^2 = %s\\text{ m}^2$.
\\item Diện tích phần lối đi lát gạch xung quanh sân thượng là: $%s - %s = %s\\text{ (m}^2)$.
\\end{enumEX}'''
                   %(latex(hai_loi), latex(loi_di), latex(hai_loi), latex(dt_co),
                     latex(hai_loi), latex(dt_co), latex(hai_loi), latex(canh_co), latex(hai_loi), latex(canh_co),
                     latex(canh_san), latex(nghiem_am),
                     latex(canh_san), latex(canh_san), latex(dt_san),
                     latex(dt_san), latex(dt_co), latex(dt_loi_di)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
