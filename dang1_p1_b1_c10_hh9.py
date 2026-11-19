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


def bt_dang1_p1_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_ten = [
            ('A', 'B', 'C', 'D'),
            ('M', 'N', 'P', 'Q'),
            ('E', 'F', 'G', 'H')
        ]
        d1, d2, d3, d4 = random.choice(bo_ten)
        h_val = random.randint(4, 12)
        r_val = random.randint(2, 8)
        while r_val == h_val:
            r_val = random.randint(2, 8)

        # Các đáp án trắc nghiệm
        du = ['Đoạn thẳng $%s%s$' % (d2, d3), 'Đoạn thẳng $%s%s$' % (d1, d4)]
        da = random.choice(du)
        s = [
            'Đoạn thẳng $%s%s$' % (d1, d2),
            'Đoạn thẳng $%s%s$' % (d3, d4),
            'Đoạn thẳng $%s%s$' % (d1, d3),
            'Đoạn thẳng $%s%s$' % (d2, d4)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Khi quay một hình chữ nhật $%s%s%s%s$ một vòng quanh cạnh $%s%s$ cố định (với $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$), ta thu được một hình trụ. Bán kính đáy của hình trụ này có độ dài bằng độ dài đoạn thẳng nào sau đây?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (2,0);
\\coordinate (D) at (2,2.5);
\\draw[line width=1pt] (0,2.5) ellipse (2 and 0.45);
\\draw[line width=1pt] (-2,0) arc (180:360:2 and 0.45);
\\draw[line width=1pt, dashed] (2,0) arc (0:180:2 and 0.45);
\\draw[line width=1pt] (-2,0)--(-2,2.5) (2,0)--(2,2.5);
\\draw[line width=1pt, dashed] (A)--(B)--(C) (A)--(D);
\\draw[line width=1pt] (D)--(C);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\fill (D) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}'''
                         % (d1, d2, d3, d4, d1, d2, d1, d2, h_val, d2, d3, r_val,
                            d1, d2, d3, d4))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Khi quay hình chữ nhật $%s%s%s%s$ một vòng quanh cạnh $%s%s$ cố định thì ta được một hình trụ có:\\\\
- Hai đáy là hai hình tròn bằng nhau tâm $%s$ và tâm $%s$.\\\\
- Bán kính đáy của hình trụ bằng độ dài các cạnh vuông góc với trục quay $%s%s$, tức là bằng độ dài đoạn thẳng $%s%s$ hoặc $%s%s$ (cùng bằng $%s\\text{ cm}$).'''
                   % (d1, d2, d3, d4, d1, d2,
                      d1, d2,
                      d1, d2, d2, d3, d1, d4, r_val))

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
