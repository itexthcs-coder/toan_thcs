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


def bt_dang1_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        rong = randint(10, 25)
        chenh = randint(4, 15)
        dai = rong + chenh
        dientich = rong * dai
        chuvi = 2 * (rong + dai)
        nghiem_am = -dai
        delta = chenh**2 + 4 * dientich
        can_delta = int(math.isqrt(delta))

        noidungcauhoi = ('''Một bác nông dân có một mảnh vườn hình chữ nhật dùng để trồng bưởi da xanh. Biết chiều dài mảnh vườn lớn hơn chiều rộng $%s\\text{ m}$ và tổng diện tích của mảnh vườn là $%s\\text{ m}^2$. \\\\
a) Tính chiều rộng và chiều dài của mảnh vườn đó. \\\\
b) Tính chu vi của mảnh vườn đó. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) rectangle (4,2.5);
\\node[below] at (2,0) {$x + %s$};
\\node[left] at (0,1.25) {$x$};
\\node at (2,1.25) {$S = %s\\text{ m}^2$};
\\end{tikzpicture}
\\end{center}'''
                         %(latex(chenh), latex(dientich), latex(chenh), latex(dientich)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x\\text{ (m)}$ là chiều rộng của mảnh vườn. Điều kiện: $x > 0$. \\\\
Khi đó, chiều dài của mảnh vườn là $x + %s\\text{ (m)}$. \\\\
Vì diện tích của mảnh vườn là $%s\\text{ m}^2$ nên ta có phương trình: \\\\
$x(x + %s) = %s$ hay $x^2 + %sx - %s = 0$. \\\\
Ta có: $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{-%s - %s}{2} = %s$ (loại); \\quad $x_2 = \\frac{-%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy chiều rộng mảnh vườn là $%s\\text{ m}$ và chiều dài mảnh vườn là $%s + %s = %s\\text{ m}$.
\\item Chu vi của mảnh vườn hình chữ nhật là: $2 \\cdot (%s + %s) = %s\\text{ (m)}$.
\\end{enumEX}'''
                   %(latex(chenh), latex(dientich), latex(chenh), latex(dientich), latex(chenh), latex(dientich),
                     latex(chenh), latex(dientich), latex(delta), latex(can_delta),
                     latex(chenh), latex(can_delta), latex(nghiem_am), latex(chenh), latex(can_delta), latex(rong),
                     latex(rong), latex(rong), latex(chenh), latex(dai),
                     latex(rong), latex(dai), latex(chuvi)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
