# -*- coding: utf-8 -*-
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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang16_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_lon = random.choice([10, 12, 14, 15, 16, 18])
        k_mau = random.choice([2, 3, 4])
        # S_nho = (1/k_mau) * S_thang => S_thang = k_mau * S_nho
        # S_lon = S_nho + 6 * k_mau * S_nho = (6*k_mau + 1) * S_nho
        he_so_tong = 6 * k_mau + 1
        canh_nho_rut_gon = Rational(canh_lon, he_so_tong) * sqrt(he_so_tong)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\foreach \\i in {0,60,...,300} {
    \\coordinate (A\\i) at (\\i:1.9);
    \\coordinate (B\\i) at (\\i:0.75);
    \\draw[line width=1pt] (A\\i)--(B\\i);
}
\\draw[line width=1pt] (A0)--(A60)--(A120)--(A180)--(A240)--(A300)--cycle;
\\draw[line width=1pt] (B0)--(B60)--(B120)--(B180)--(B240)--(B300)--cycle;
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một nghệ nhân mộc làm một chiếc khay đựng bánh kẹo bằng gỗ có dạng hình lục giác đều cạnh $%s\\text{ cm}$ (như hình vẽ). Lòng khay được chia thành $7$ ngăn gồm một ngăn hình lục giác đều nhỏ ở chính giữa cạnh $x\\text{ cm}$ ($0 < x < %s$) và $6$ ngăn xung quanh là các hình thang cân bằng nhau. Hỏi độ dài cạnh $x$ của ngăn lục giác đều nhỏ phải bằng bao nhiêu centimét để diện tích ngăn lục giác đều nhỏ bằng $\\frac{1}{%s}$ diện tích của mỗi ngăn hình thang cân? %s'''
                         % (canh_lon, canh_lon, k_mau, hinh_tikz))

        loigiai = ('''Gọi $S_1$ là diện tích của mỗi ngăn hình thang cân và $S_2$ là diện tích của ngăn hình lục giác đều nhỏ ở chính giữa. \\\\
Theo đề bài, $S_2 = \\frac{1}{%s} S_1 \\Rightarrow S_1 = %s S_2$. \\\\
Vì khay lục giác đều lớn được chia thành $1$ ngăn lục giác đều nhỏ và $6$ ngăn hình thang cân bằng nhau nên diện tích toàn bộ khay lục giác đều lớn là:
$$S = S_2 + 6 S_1 = S_2 + 6 \\cdot %s S_2 = %s S_2.$$
Mặt khác, diện tích của lục giác đều lớn cạnh $%s\\text{ cm}$ là $S = 6 \\cdot \\frac{%s^2\\sqrt{3}}{4} = \\frac{3 \\cdot %s^2\\sqrt{3}}{2}\\text{ (cm}^2\\text{)}$, và diện tích của lục giác đều nhỏ cạnh $x\\text{ cm}$ là $S_2 = 6 \\cdot \\frac{x^2\\sqrt{3}}{4} = \\frac{3x^2\\sqrt{3}}{2}\\text{ (cm}^2\\text{)}$. \\\\
Từ $S = %s S_2$ suy ra:
$$\\frac{3 \\cdot %s^2\\sqrt{3}}{2} = %s \\cdot \\frac{3x^2\\sqrt{3}}{2} \\Leftrightarrow x^2 = \\frac{%s^2}{%s} \\Leftrightarrow x = \\frac{%s}{\\sqrt{%s}} = %s\\text{ (cm) (vì } x > 0\\text{)}.$$
Vậy độ dài cạnh của ngăn lục giác đều nhỏ phải bằng $%s\\text{ cm}$.'''
                   % (k_mau, k_mau, k_mau, he_so_tong, canh_lon, canh_lon, canh_lon, he_so_tong, canh_lon, he_so_tong, canh_lon, he_so_tong, canh_lon, he_so_tong, latex(canh_nho_rut_gon), latex(canh_nho_rut_gon)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
