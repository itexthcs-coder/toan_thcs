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


def bt_dang19_p1_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ten_p1 = random.choice(['P_1', 'C_1'])
        ten_p2 = random.choice(['P_2', 'C_2'])

        # Các đáp án trắc nghiệm
        du = ['$0 < b < a$']
        da = random.choice(du)
        s = [
            '$0 < a < b$',
            '$a < b < 0$',
            '$b < a < 0$',
            '$a < 0 < b$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Trên cùng một mặt phẳng tọa độ $Oxy$, xét hai parabol $(%s): y=ax^2$ và $(%s): y=bx^2$ đều nằm phía trên trục hoành. Biết rằng với mọi $x \\neq 0$, các điểm thuộc $(%s)$ luôn nằm phía trên các điểm có cùng hoành độ thuộc $(%s)$. Khẳng định nào sau đây đúng?'''
                         % (ten_p1, ten_p2, ten_p1, ten_p2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Vì cả hai parabol $(%s): y=ax^2$ và $(%s): y=bx^2$ đều nằm phía trên trục hoành nên $a > 0$ và $b > 0$.\\\\
                    Xét tại điểm có hoành độ $x = 1 \\neq 0$, tung độ điểm thuộc $(%s)$ là $y_1 = a \\cdot 1^2 = a$ và tung độ điểm thuộc $(%s)$ là $y_2 = b \\cdot 1^2 = b$.\\\\
                    Do điểm thuộc $(%s)$ nằm phía trên điểm có cùng hoành độ thuộc $(%s)$ nên $y_1 > y_2 > 0$, suy ra $a > b > 0$ hay $0 < b < a$, như hình minh họa sau:\\\\
                    \\begin{center}
                    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                    \\coordinate (O) at (0,0);
                    \\draw[->, line width=1pt] (-2.2,0)--(2.2,0) node[below] {$x$};
                    \\draw[->, line width=1pt] (0,-0.4)--(0,2.8) node[left] {$y$};
                    \\draw[line width=1pt, smooth, samples=100, domain=-1.2:1.2] plot (\\x, {1.8*\\x*\\x});
                    \\draw[line width=1pt, dashed, smooth, samples=100, domain=-1.8:1.8] plot (\\x, {0.6*\\x*\\x});
                    \\fill (O) circle (1pt) node[below left] {$O$};
                    \\node[left] at (-1.1,2.2) {$(%s)$};
                    \\node[right] at (1.7,1.8) {$(%s)$};
                    \\end{tikzpicture}
                    \\end{center}
                    Vậy khẳng định đúng là $0 < b < a$.'''
                   % (ten_p1, ten_p2, ten_p1, ten_p2, ten_p1, ten_p2, ten_p1, ten_p2))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
