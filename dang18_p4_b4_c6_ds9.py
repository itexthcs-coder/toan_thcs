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


def bt_dang18_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (60, 40, 5),
            (50, 30, 5),
            (40, 24, 4),
            (70, 50, 5),
            (48, 32, 4)
        ])
        dai_ton, rong_ton, x_cat = bo_so
        dai_day = dai_ton - 2 * x_cat
        rong_day = rong_ton - 2 * x_cat
        dt_day = dai_day * rong_day
        the_tich = dt_day * x_cat
        max_x = rong_ton // 2

        b_pt = -(dai_ton + rong_ton) // 2
        c_pt = (dai_ton * rong_ton - dt_day) // 4
        delta = b_pt**2 - 4 * c_pt
        can_delta = int(math.isqrt(delta))
        x_loai = (-b_pt + can_delta) // 2

        noidungcauhoi = ('''Một xưởng cơ khí có một tấm tôn hình chữ nhật kích thước $%s\\text{ cm} \\times %s\\text{ cm}$. Người thợ cắt bỏ bốn hình vuông bằng nhau có cạnh $x\\text{ (cm)}$ ở bốn góc của tấm tôn, rồi gập các mép lên để hàn thành một chiếc khay đựng linh kiện dạng hình hộp chữ nhật không nắp. Biết diện tích đáy của chiếc khay thu được là $%s\\text{ cm}^2$. \\\\
a) Tính độ dài cạnh $x$ của mỗi hình vuông bị cắt bỏ. \\\\
b) Tính thể tích của chiếc khay đựng linh kiện tạo thành. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) rectangle (4.5,3);
\\draw[line width=1pt, dashed] (0.6,0.6) rectangle (3.9,2.4);
\\draw[line width=1pt] (0.6,0) -- (0.6,0.6) -- (0,0.6);
\\draw[line width=1pt] (3.9,0) -- (3.9,0.6) -- (4.5,0.6);
\\draw[line width=1pt] (0.6,3) -- (0.6,2.4) -- (0,2.4);
\\draw[line width=1pt] (3.9,3) -- (3.9,2.4) -- (4.5,2.4);
\\node[below] at (2.25,0) {$%s\\text{ cm}$};
\\node[left] at (0,1.5) {$%s\\text{ cm}$};
\\node[above] at (0.3,2.4) {$x$};
\\end{tikzpicture}
\\end{center}'''
                         %(latex(dai_ton), latex(rong_ton), latex(dt_day), latex(dai_ton), latex(rong_ton)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Điều kiện của cạnh hình vuông bị cắt bỏ là $0 < x < %s$. \\\\
Sau khi cắt bỏ bốn góc và gập mép lên, đáy của chiếc khay là hình chữ nhật có chiều dài là $%s - 2x\\text{ (cm)}$ và chiều rộng là $%s - 2x\\text{ (cm)}$. \\\\
Vì diện tích đáy của chiếc khay bằng $%s\\text{ cm}^2$ nên ta có phương trình: \\\\
$(%s - 2x)(%s - 2x) = %s$. \\\\
Khai triển và chia cả hai vế cho $4$, ta được phương trình bậc hai: \\\\
$x^2 %sx + %s = 0$. \\\\
Ta có: $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot %s = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{%s - %s}{2} = %s$ (thoả mãn điều kiện); \\quad $x_2 = \\frac{%s + %s}{2} = %s$ (loại vì lớn hơn $%s$). \\\\
Vậy độ dài cạnh của mỗi hình vuông bị cắt bỏ là $%s\\text{ cm}$.
\\item Chiều cao của chiếc khay hình hộp chữ nhật chính là $x = %s\\text{ cm}$. \\\\
Thể tích của chiếc khay đựng linh kiện tạo thành là: $V = S_{\\text{đáy}} \\cdot h = %s \\cdot %s = %s\\text{ (cm}^3)$.
\\end{enumEX}'''
                   %(latex(max_x), latex(dai_ton), latex(rong_ton), latex(dt_day),
                     latex(dai_ton), latex(rong_ton), latex(dt_day),
                     latex(b_pt), latex(c_pt),
                     latex(b_pt), latex(c_pt), latex(delta), latex(can_delta),
                     latex(abs(b_pt)), latex(can_delta), latex(x_cat), latex(abs(b_pt)), latex(can_delta), latex(x_loai), latex(max_x),
                     latex(x_cat),
                     latex(x_cat), latex(dt_day), latex(x_cat), latex(the_tich)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
