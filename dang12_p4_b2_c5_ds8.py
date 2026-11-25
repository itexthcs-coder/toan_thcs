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


def bt_dang12_p4_b2_c5_ds8(self):
    # Dạng 12 (Tự luận - Vận dụng): Phân tích biến động qua hai biểu đồ quạt tròn và dựng biểu đồ cột kép
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        s24, s25 = 200 * k, 250 * k
        lt24, kt24, tk24 = s24 * 55 // 100, s24 * 25 // 100, s24 * 20 // 100
        lt25, kt25, tk25 = s25 * 48 // 100, s25 * 32 // 100, s25 * 20 // 100
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số nhân sự};
        \\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[right] {Bộ phận};
        \\draw[line width=1pt, fill=black!35] (0.5,0) rectangle (1.0,1.7) (2.2,0) rectangle (2.7,0.8) (3.9,0) rectangle (4.4,0.65);
        \\draw[line width=1pt, fill=white] (1.0,0) rectangle (1.5,1.9) (2.7,0) rectangle (3.2,1.25) (4.4,0) rectangle (4.9,0.8);
        \\node[above] at (0.75,1.7) {$%s$}; \\node[above] at (1.25,1.9) {$%s$};
        \\node[above] at (2.45,0.8) {$%s$}; \\node[above] at (2.95,1.25) {$%s$};
        \\node[above] at (4.15,0.65) {$%s$}; \\node[above] at (4.65,0.8) {$%s$};
        \\node[below] at (1.0,0) {Lập trình}; \\node[below] at (2.7,0) {Kiểm thử}; \\node[below] at (4.4,0) {Thiết kế};
        \\draw[line width=1pt, fill=black!35] (5.3,1.8) rectangle (5.6,2.1); \\node[right] at (5.6,1.95) {Năm $2024$};
        \\draw[line width=1pt, fill=white] (5.3,1.3) rectangle (5.6,1.6); \\node[right] at (5.6,1.45) {Năm $2025$};
        \\end{tikzpicture}
        \\end{center}""" % (lt24, lt25, kt24, kt25, tk24, tk25))
        
        noidungcauhoi = ("""Tại một công ty phần mềm, biểu đồ hình quạt tròn năm $2024$ cho biết công ty có $%s$ nhân sự gồm: Lập trình viên ($55\\%%$), Kiểm thử phần mềm ($25\\%%$) và Thiết kế đồ họa ($20\\%%$). Sang năm $2025$, tổng số nhân sự của công ty tăng lên $%s$ người, trong đó Lập trình viên chiếm $48\\%%$, Kiểm thử phần mềm chiếm $32\\%%$ và Thiết kế đồ họa chiếm $20\\%%$.\\\\
        a) Lập bảng thống kê số lượng nhân sự của từng bộ phận trong hai năm $2024$ và $2025$.\\\\
        b) Vẽ biểu đồ cột kép so sánh số lượng nhân sự từng bộ phận giữa hai năm $2024$ và $2025$. Nhận xét về sự thay đổi của bộ phận Lập trình viên."""
                         % (s24, s25))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Số lượng nhân sự từng bộ phận trong năm $2024$: Lập trình viên có $%s \\cdot 55\\%% = %s$ người; Kiểm thử phần mềm có $%s \\cdot 25\\%% = %s$ người; Thiết kế đồ họa có $%s \\cdot 20\\%% = %s$ người.\\\\
        Số lượng nhân sự từng bộ phận trong năm $2025$: Lập trình viên có $%s \\cdot 48\\%% = %s$ người; Kiểm thử phần mềm có $%s \\cdot 32\\%% = %s$ người; Thiết kế đồ họa có $%s \\cdot 20\\%% = %s$ người.\\\\
        Bảng thống kê nhân sự hai năm $2024$ và $2025$:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|}
        \\hline
        \\textbf{Năm / Bộ phận} & Lập trình viên & Kiểm thử phần mềm & Thiết kế đồ họa \\\\
        \\hline
        \\textbf{Năm $2024$} & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\textbf{Năm $2025$} & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Biểu đồ cột kép so sánh số lượng nhân sự giữa hai năm:%s
        Nhận xét: Mặc dù tỉ trọng của bộ phận Lập trình viên giảm từ $55\\%%$ xuống $48\\%%$, nhưng do tổng quy mô nhân sự của công ty tăng lên nên số lượng lập trình viên thực tế vẫn tăng thêm $%s - %s = %s$ người.
        \\end{enumEX}""" % (s24, lt24, s24, kt24, s24, tk24, s25, lt25, s25, kt25, s25, tk25, lt24, kt24, tk24, lt25, kt25, tk25, tikz_a, lt25, lt24, lt25 - lt24))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
