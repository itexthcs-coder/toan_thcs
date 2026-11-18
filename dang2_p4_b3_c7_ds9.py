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


def bt_dang2_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mD, mC, mB, mA = random.choice([
            (2, 5, 9, 4),
            (3, 6, 8, 3),
            (2, 6, 7, 5)
        ])
        ds = ['D'] * mD + ['C'] * mC + ['B'] * mB + ['A'] * mA
        random.shuffle(ds)
        ds_str = ', '.join(ds)

        fD, fC, fB, fA = mD * 5, mC * 5, mB * 5, mA * 5
        f_dat = fB + fA

        noidungcauhoi = ('''Theo tiêu chuẩn xếp loại năng suất lao động hằng ngày của công nhân xưởng may: Loại D (dưới $40$ sản phẩm), Loại C (từ $40$ đến dưới $50$ sản phẩm), Loại B (từ $50$ đến dưới $60$ sản phẩm), Loại A (từ $60$ đến dưới $70$ sản phẩm). Ghi nhận kết quả làm việc trong một ngày của $20$ công nhân tổ $1$ như sau:\\
\\textit{%s.}\\
a) Lập bảng tần số ghép nhóm theo số sản phẩm hoàn thành trong ngày của $20$ công nhân trên.\\
b) Lập bảng tần số tương đối ghép nhóm và tính tỉ lệ phần trăm công nhân đạt năng suất từ $50$ sản phẩm trở lên.''' % (ds_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Quy đổi các mức xếp loại sang các nhóm số sản phẩm tương ứng: Loại D là $[0; 40)$ có $%s$ người; Loại C là $[40; 50)$ có $%s$ người; Loại B là $[50; 60)$ có $%s$ người; Loại A là $[60; 70)$ có $%s$ người. Ta có bảng tần số ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Số sản phẩm & $[0; 40)$ & $[40; 50)$ & $[50; 60)$ & $[60; 70)$ \\\\
\\hline
Số công nhân & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Với cỡ mẫu $n = 20$, ta có bảng tần số tương đối ghép nhóm sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Số sản phẩm & $[0; 40)$ & $[40; 50)$ & $[50; 60)$ & $[60; 70)$ \\\\
\\hline
Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
Tỉ lệ phần trăm công nhân đạt năng suất từ $50$ sản phẩm trở lên là: $%s\\%% + %s\\%% = %s\\%%$.
\\end{enumEX}''' % (mD, mC, mB, mA, mD, mC, mB, mA, fD, fC, fB, fA, fB, fA, f_dat))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
