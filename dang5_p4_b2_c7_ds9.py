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


def bt_dang5_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        don_vi = random.choice([2, 3])
        m1, m2, m3 = 6*don_vi, 9*don_vi, 5*don_vi
        tong = 20*don_vi

        bang_tranh = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|l|}\n'
            '\\hline\n'
            'Huy chương Vàng & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
            '\\hline\n'
            'Huy chương Bạc & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
            '\\hline\n'
            'Huy chương Đồng & $\\bullet\\ \\bullet\\ \\bullet\\ \\bullet\\ \\bullet$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\\\\[4pt]\n'
            '\\textit{(Mỗi biểu tượng $\\bullet$ biểu diễn cho $%s$ huy chương)}\n'
            '\\end{center}'
        ) % (don_vi)

        hinh_quat = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) circle (2);\n'
            '\\draw[line width=1pt] (0,0) -- (0:2);\n'
            '\\draw[line width=1pt] (0,0) -- (108:2);\n'
            '\\draw[line width=1pt] (0,0) -- (270:2);\n'
            '\\node at (54:1.15) {$30\\%$};\n'
            '\\node at (189:1.15) {$45\\%$};\n'
            '\\node at (315:1.15) {$25\\%$};\n'
            '\\node[right] at (2.3, 0.7) {Huy chương Vàng: $30\\%$};\n'
            '\\node[right] at (2.3, 0.0) {Huy chương Bạc: $45\\%$};\n'
            '\\node[right] at (2.3, -0.7) {Huy chương Đồng: $25\\%$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Biểu đồ tranh sau biểu diễn số lượng huy chương đạt được của đoàn thể thao học sinh tại Hội khỏe Phù Đổng:%s'
            'a) Lập bảng tần số tương đối cho dữ liệu trên.\\\\ '
            'b) Vẽ biểu đồ hình quạt tròn biểu diễn bảng tần số tương đối thu được.'
        ) % (bang_tranh)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Số huy chương Vàng, Bạc, Đồng lần lượt là $%s; %s; %s$ chiếc. Tổng số huy chương là $n = %s$.\\\\ '
            'Tần số tương đối tương ứng là: Vàng ($30\\%%$), Bạc ($45\\%%$), Đồng ($25\\%%$).\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|}\n'
            '\\hline\n'
            'Loại huy chương & Vàng & Bạc & Đồng \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $30\\%%$ & $45\\%%$ & $25\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Số đo cung tương ứng: Vàng ($360^\\circ \\cdot 30\\%% = 108^\\circ$); Bạc ($360^\\circ \\cdot 45\\%% = 162^\\circ$); Đồng ($360^\\circ \\cdot 25\\%% = 90^\\circ$).\\\\ '
            'Biểu đồ hình quạt tròn:%s\n'
            '\\end{enumEX}'
        ) % (m1, m2, m3, tong, hinh_quat)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
