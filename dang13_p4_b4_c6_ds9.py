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


def bt_dang13_p4_b4_c6_ds9(self):
    def fmt_vn(val):
        s = f"{val.normalize():f}"
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        chu_vi = random.choice([8, 10, 12, 14])
        nua_cv = chu_vi // 2

        pi_val = Decimal('3.14')
        dt_val = Decimal(2 * nua_cv - 2) - pi_val / Decimal('2')
        dt_str = fmt_vn(dt_val)

        noidungcauhoi = ('''Một kiến trúc sư thiết kế một khung cửa sổ gồm phần dưới là hình chữ nhật có chiều rộng $x\\text{ (m)}$, chiều cao $y\\text{ (m)}$ và phần trên là một nửa hình tròn có đường kính bằng chiều rộng của hình chữ nhật (như hình vẽ). Biết tổng chu vi đường bao ngoài của khung cửa sổ (không tính thanh ngang ngăn cách giữa hình chữ nhật và nửa hình tròn) là $%s\\text{ m}$. \\\\
a) Biểu thị chiều cao $y$ và diện tích toàn bộ khung cửa sổ $S$ theo $x$. \\\\
b) Tính diện tích khung cửa sổ khi chiều rộng $x = 2\\text{ m}$ (lấy $\\pi \\approx 3,14$). \\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) -- (2.4,0) -- (2.4,2.2) arc (0:180:1.2) -- (0,0);
\\draw[line width=1pt, dashed] (0,2.2) -- (2.4,2.2);
\\node[below] at (1.2,0) {$x$};
\\node[left] at (0,1.1) {$y$};
\\end{tikzpicture}
\\end{center}'''
                         %(latex(chu_vi)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Nửa hình tròn phía trên có đường kính $x\\text{ (m)}$ nên bán kính là $R = \\frac{x}{2}\\text{ (m)}$ và độ dài cung tròn phía trên là $\\frac{1}{2} \\cdot \\pi x = \\frac{\\pi x}{2}\\text{ (m)}$. \\\\
Tổng chu vi đường bao ngoài của khung cửa sổ là $x + 2y + \\frac{\\pi x}{2} = %s$. \\\\
Suy ra $2y = %s - x - \\frac{\\pi x}{2} \\Rightarrow y = %s - \\frac{x}{2} - \\frac{\\pi x}{4}\\text{ (m)}$. \\\\
Diện tích toàn bộ khung cửa sổ bằng tổng diện tích hình chữ nhật và nửa hình tròn: \\\\
$S = x \\cdot y + \\frac{1}{2} \\pi \\left(\\frac{x}{2}\\right)^2 = x\\left(%s - \\frac{x}{2} - \\frac{\\pi x}{4}\\right) + \\frac{\\pi x^2}{8} = %sx - \\frac{x^2}{2} - \\frac{\\pi x^2}{8}\\text{ (m}^2)$.
\\item Thay $x = 2\\text{ m}$ và $\\pi \\approx 3,14$ vào biểu thức diện tích $S$, ta được: \\\\
$S \\approx %s \\cdot 2 - \\frac{2^2}{2} - \\frac{3,14 \\cdot 2^2}{8} = %s - 2 - 1,57 = %s\\text{ (m}^2)$.
\\end{enumEX}'''
                   %(latex(chu_vi), latex(chu_vi), latex(nua_cv),
                     latex(nua_cv), latex(nua_cv),
                     latex(nua_cv), latex(2 * nua_cv), dt_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
