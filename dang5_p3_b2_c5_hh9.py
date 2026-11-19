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

def bt_dang5_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tam = random.choice(['O', 'I'])
        bo_diem = random.choice([('M', 'A', 'B'), ('C', 'E', 'F'), ('K', 'P', 'Q')])
        d_giua, d1, d2 = bo_diem[0], bo_diem[1], bo_diem[2]
        kq_str = '240'

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho điểm $%s$ nằm trên đường tròn $(%s)$. Đường trung trực của đoạn thẳng $%s%s$ cắt đường tròn $(%s)$ tại hai điểm phân biệt $%s$ và $%s$ (như hình vẽ). Tính số đo của cung lớn $\\overset\\frown{%s%s}$ (đơn vị: độ).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (M) at (1.8,0);
        \\coordinate (A) at (60:1.8);
        \\coordinate (B) at (-60:1.8);
        \\draw[line width=1pt] (O) circle (1.8);
        \\draw[line width=1pt] (O)--(M) (O)--(A)--(M) (O)--(B)--(M);
        \\draw[line width=1pt, dashed] (0.9,-1.75)--(0.9,1.75);
        \\fill (O) circle (1pt) node[left] {$%s$};
        \\fill (M) circle (1pt) node[right] {$%s$};
        \\fill (A) circle (1pt) node[above right] {$%s$};
        \\fill (B) circle (1pt) node[below right] {$%s$};
        \\end{tikzpicture}
        \\end{center}''' % (d_giua, tam, tam, d_giua, tam, d1, d2, d1, d2, tam, d_giua, d1, d2))

        # Nội dung lời giải
        loigiai = ('''Vì $%s$ và $%s$ nằm trên đường trung trực của đoạn thẳng $%s%s$ nên ta có $%s%s = %s%s$ và $%s%s = %s%s$.\\\\
        Mặt khác, $%s%s = %s%s = %s%s$ (cùng bằng bán kính đường tròn $(%s)$).\\\\
        Suy ra $%s%s = %s%s = %s%s$ và $%s%s = %s%s = %s%s$, do đó hai tam giác $%s%s%s$ và $%s%s%s$ là các tam giác đều.\\\\
        Suy ra $\\widehat{%s%s%s} = 60^\\circ$ và $\\widehat{%s%s%s} = 60^\\circ$, dẫn đến $\\widehat{%s%s%s} = 60^\\circ + 60^\\circ = 120^\\circ$.\\\\
        Do đó số đo cung nhỏ $\\overset\\frown{%s%s}$ bằng $120^\\circ$, vậy số đo cung lớn $\\overset\\frown{%s%s}$ bằng $360^\\circ - 120^\\circ = 240^\\circ$.'''
                   % (d1, d2, tam, d_giua, d1, tam, d1, d_giua, d2, tam, d2, d_giua,
                      tam, d1, tam, d2, tam, d_giua, tam,
                      tam, d1, d1, d_giua, tam, d_giua, tam, d2, d2, d_giua, tam, d_giua, tam, d1, d_giua, tam, d2, d_giua,
                      d1, tam, d_giua, d2, tam, d_giua, d1, tam, d2,
                      d1, d2, d1, d2))

        #Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
