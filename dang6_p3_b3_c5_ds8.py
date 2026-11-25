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

def bt_dang6_p3_b3_c5_ds8(self):
    # Dạng 6: Tính số học sinh tham gia đúng 2 môn trong khảo sát đa lựa chọn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_hs = random.randint(40, 48)
        m_toan = random.randint(25, 32)
        m_anh = random.randint(22, 30)
        giao = m_toan + m_anh - n_hs
        kq_str = str(giao)
        
        yt = round(m_toan / 8.0, 2)
        ya = round(m_anh / 8.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Môn học};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Số lượt chọn};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!20] (0.9,0) rectangle (1.9,%s); \\node[above] at (1.4,%s) {$%s$}; \\node[below] at (1.4,0) {Môn Toán};\n' % (yt, yt, m_toan) +
            '\\draw[line width=1pt, fill=black!20] (2.7,0) rectangle (3.7,%s); \\node[above] at (3.2,%s) {$%s$}; \\node[below] at (3.2,0) {Môn Tiếng Anh};\n' % (ya, ya, m_anh) +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một lớp học có $%s$ học sinh được khảo sát về việc đăng kí học bồi dưỡng hai môn Toán và Tiếng Anh (mỗi học sinh đều đăng kí ít nhất một trong hai môn). Kết quả biểu đồ cột cho thấy số lượt đăng kí từng môn như sau:\n' % n_hs +
                         tikz_code + '\n' +
                         'Hỏi có bao nhiêu học sinh của lớp đăng kí học cả hai môn Toán và Tiếng Anh?')
        
        loigiai = ('Tổng số lượt đăng kí của cả lớp là: $%s + %s = %s$ (lượt).\\\\' +
                   'Vì mỗi học sinh đều đăng kí ít nhất một trong hai môn nên số học sinh đăng kí cả hai môn Toán và Tiếng Anh là:\\\\' +
                   '$$%s - %s = %s \\text{ (học sinh)}.$$'
                   ) % (m_toan, m_anh, m_toan + m_anh, m_toan + m_anh, n_hs, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
