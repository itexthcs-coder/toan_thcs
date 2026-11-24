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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang18_p4_b3_c4_hh8(self):
    # Dạng 18: Thiết kế hệ thống thanh chống giằng mái nhà hình tam giác (Thực tế)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (6, 9, 10, 4, 6, 3.6, 7.6, 1900),
            (8, 12, 15, 6, 9, 4.8, 10.8, 2700),
            (4, 6, 5, 2, 3, 2.4, 4.4, 1100)
        ]
        ab, ac, bc, bd, cd, de, tong, chi_phi = random.choice(bo_so)
        s_de = fmt_num(de)
        s_tong = fmt_num(tong)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (2.0,2.5);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5.2,0);\n'
            '\\coordinate (D) at (2.08,0);\n'
            '\\coordinate (E) at ($(A)!0.4!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (D)--(E);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một khung vì kèo mái nhà có dạng tam giác $ABC$ với hai thanh kèo nghiêng $AB = %s\\text{ m}$, $AC = %s\\text{ m}$ và thanh xà ngang $BC = %s\\text{ m}$. Kỹ sư lắp thanh chống $AD$ ($D \\in BC$) là tia phân giác của góc $BAC$ và lắp thêm thanh giằng $DE // AB$ ($E \\in AC$).\\\\\n'
            'a) Tính khoảng cách từ điểm chân chống $D$ đến hai đầu mút $B$ và $C$ của thanh xà ngang.\\\\\n'
            'b) Tính chiều dài thanh giằng $DE$ và tổng chi phí vật liệu làm hai đoạn $BD, DE$ biết đơn giá thép là $250\\text{ nghìn đồng/mét}$.\n%s'
            % (ab, ac, bc, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Trong tam giác $ABC$ có $AD$ là tia phân giác của góc $BAC$ ($D \\in BC$) nên $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $\\frac{BD}{BC} = \\frac{%s}{%s + %s} \\Rightarrow BD = \\frac{%s}{%s} \\cdot %s = %s\\text{ m}$, và $CD = %s - %s = %s\\text{ m}$. \n'
            '\\item Vì $DE // AB$ nên theo hệ quả của định lí Thalès trong tam giác $ABC$, ta có: $\\frac{DE}{AB} = \\frac{CD}{BC} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $DE = \\frac{%s}{%s} \\cdot %s = %s\\text{ m}$.\\\\'
            'Tổng chiều dài hai đoạn $BD$ và $DE$ là $%s + %s = %s\\text{ m}$.\\\\'
            'Tổng chi phí vật liệu là $%s \\cdot 250 = %s\\text{ nghìn đồng}$. \n'
            '\\end{enumEX} \n'
            % (ab, ac, ab, ab, ac, ab, ab + ac, bc, bd, bc, bd, cd, cd, bc, cd, bc, ab, s_de, bd, s_de, s_tong, s_tong, chi_phi)
        )

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
