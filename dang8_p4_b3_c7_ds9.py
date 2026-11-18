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


def bt_dang8_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        m1, m2, m3, m4 = 15 * k, 45 * k, 36 * k, 24 * k
        n = 120 * k

        noidungcauhoi = ('''Thống kê tuổi thọ (đơn vị: tháng) của một lô lốp xe máy tại cửa hàng bảo dưỡng thu được kết quả:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Tuổi thọ (tháng) & $[12; 18)$ & $[18; 24)$ & $[24; 30)$ & $[30; 36)$ \\\\
\\hline
Số lốp xe & $%s$ & $%s$ & $m_3$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Biết rằng nhóm tuổi thọ $[18; 24)$ chiếm $37,5\\%%$ tổng số lốp xe được thống kê.\\
a) Tìm tổng số lốp xe được thống kê và giá trị của $m_3$.\\
b) Lập bảng tần số tương đối ghép nhóm cho bảng thống kê trên.''' % (m1, m2, m4))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tổng số lốp xe được thống kê là:
$$n = \\dfrac{%s}{37,5\\%%} = %s \\text{ (lốp xe)}.$$
Giá trị của $m_3$ là: $m_3 = %s - (%s + %s + %s) = %s$.
\\item Tính tần số tương đối của các nhóm: $f_1 = \\dfrac{%s}{%s} \\cdot 100\\%% = 12,5\\%%$; $f_2 = 37,5\\%%$; $f_3 = \\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$; $f_4 = \\dfrac{%s}{%s} \\cdot 100\\%% = 20\\%%$. Ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Tuổi thọ (tháng) & $[12; 18)$ & $[18; 24)$ & $[24; 30)$ & $[30; 36)$ \\\\
\\hline
Tần số tương đối & $12,5\\%%$ & $37,5\\%%$ & $30\\%%$ & $20\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\end{enumEX}''' % (m2, n, n, m1, m2, m4, m3, m1, n, m3, n, m4, n))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
