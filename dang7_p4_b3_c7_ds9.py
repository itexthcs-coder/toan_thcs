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


def bt_dang7_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        m1, m2, m3, m4 = 12 * k, 32 * k, 24 * k, 12 * k
        n = 80 * k

        noidungcauhoi = ('''Một phòng khám nha khoa thống kê thời gian khám và điều trị (đơn vị: phút) của $%s$ bệnh nhân trong tuần qua như sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian (phút) & $[10; 20)$ & $[20; 30)$ & $[30; 40)$ & $[40; 50)$ \\\\
\\hline
Số bệnh nhân & $%s$ & $?$ & $%s$ & $?$ \\\\
\\hline
Tần số tương đối & $?$ & $40\\%%$ & $?$ & $?$ \\\\
\\hline
\\end{tabular}
\\end{center}
a) Tìm các giá trị còn thiếu và hoàn thiện đầy đủ bảng thống kê trên.\\
b) Tính tỉ lệ phần trăm số bệnh nhân có thời gian điều trị từ $30$ phút trở lên.''' % (n, m1, m3))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Ta tính các giá trị còn thiếu:
\\begin{itemize}
\\item Tần số nhóm $[20; 30)$: $m_2 = \\dfrac{%s \\cdot 40}{100} = %s$.
\\item Tần số nhóm $[40; 50)$: $m_4 = %s - (%s + %s + %s) = %s$.
\\item Tần số tương đối nhóm $[10; 20)$: $f_1 = \\dfrac{%s}{%s} \\cdot 100\\%% = 15\\%%$.
\\item Tần số tương đối nhóm $[30; 40)$: $f_3 = \\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$.
\\item Tần số tương đối nhóm $[40; 50)$: $f_4 = \\dfrac{%s}{%s} \\cdot 100\\%% = 15\\%%$.
\\end{itemize}
Bảng thống kê hoàn chỉnh:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian (phút) & $[10; 20)$ & $[20; 30)$ & $[30; 40)$ & $[40; 50)$ \\\\
\\hline
Số bệnh nhân & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
Tần số tương đối & $15\\%%$ & $40\\%%$ & $30\\%%$ & $15\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Tỉ lệ phần trăm số bệnh nhân có thời gian điều trị từ $30$ phút trở lên là: $30\\%% + 15\\%% = 45\\%%$.
\\end{enumEX}''' % (n, m2, n, m1, m2, m3, m4, m1, n, m3, n, m4, n, m1, m2, m3, m4))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
