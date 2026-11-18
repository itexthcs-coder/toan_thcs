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


def bt_dang4_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([(45, 20, 30, 5, 162, 72, 108, 18), (40, 25, 25, 10, 144, 90, 90, 36)])
        p1, p2, p3, p4, g1, g2, g3, g4 = bo_so

        bang = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|}\n'
            '\\hline\n'
            'Nhóm máu & Nhóm O & Nhóm A & Nhóm B & Nhóm AB \\\\ \n'
            '\\hline\n'
            'Tỉ lệ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
        ) % (p1, p2, p3, p4)

        hinh_quat = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) circle (2);\n'
            '\\draw[line width=1pt] (0,0) -- (0:2);\n'
            '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
            '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
            '\\draw[line width=1pt] (0,0) -- (%s:2);\n'
            '\\node at (%s:1.2) {$%s\%%$};\n'
            '\\node at (%s:1.2) {$%s\%%$};\n'
            '\\node at (%s:1.2) {$%s\%%$};\n'
            '\\node at (%s:1.45) {$%s\%%$};\n'
            '\\node[right] at (2.3, 1.0) {Nhóm O: $%s\%%$};\n'
            '\\node[right] at (2.3, 0.3) {Nhóm A: $%s\%%$};\n'
            '\\node[right] at (2.3, -0.4) {Nhóm B: $%s\%%$};\n'
            '\\node[right] at (2.3, -1.1) {Nhóm AB: $%s\%%$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (g1, g1+g2, g1+g2+g3, int(g1/2), p1, int(g1+g2/2), p2, int(g1+g2+g3/2), p3, int(g1+g2+g3+g4/2), p4, p1, p2, p3, p4)

        noidungcauhoi = (
            'Bảng tần số tương đối dưới đây thống kê tỉ lệ các nhóm máu của các tình nguyện viên tham gia hiến máu nhân đạo tại một phường:%s'
            'Hãy vẽ biểu đồ hình quạt tròn biểu diễn bảng tần số tương đối trên (trình bày rõ bước tính số đo cung tương ứng).'
        ) % (bang)

        loigiai = (
            'Bước 1. Số đo cung (góc ở tâm) tương ứng của mỗi hình quạt là:\\\\ '
            '- Nhóm O: $360^\\circ \\cdot %s\\%% = %s^\\circ$;\\\\ '
            '- Nhóm A: $360^\\circ \\cdot %s\\%% = %s^\\circ$;\\\\ '
            '- Nhóm B: $360^\\circ \\cdot %s\\%% = %s^\\circ$;\\\\ '
            '- Nhóm AB: $360^\\circ \\cdot %s\\%% = %s^\\circ$.\\\\ '
            'Bước 2 và 3. Vẽ hình tròn, chia hình quạt theo số đo cung trên và hoàn thiện chú giải:%s'
        ) % (p1, g1, p2, g2, p3, g3, p4, g4, hinh_quat)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
