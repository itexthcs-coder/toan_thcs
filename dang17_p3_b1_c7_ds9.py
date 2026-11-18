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


def bt_dang17_p3_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # N = 50: f0 = 22, f3 = 4 => f1 + f2 = 24; f1 = 2 * f2 => f2 = 8, f1 = 16
        f0 = random.choice([20, 22, 26])
        f3 = 26 - f0 + 4
        tong_12 = 50 - f0 - f3
        f2 = tong_12 // 3
        f1 = 2 * f2
        kq_str = str(f1)
        y0 = round(f0 * 0.14, 2)
        y3 = round(f3 * 0.14, 2)
        # Nội dung câu hỏi
        noidungcauhoi = ('''Biểu đồ tần số dạng cột biểu diễn số lỗi vi phạm nội quy của $50$ tập thể lớp trong tháng thi đua gồm các mức: $0$ lỗi, $1$ lỗi, $2$ lỗi, $3$ lỗi. Biết rằng cột $0$ lỗi có tần số là $%s$, cột $3$ lỗi có tần số là $%s$, và chiều cao cột $1$ lỗi gấp đôi chiều cao cột $2$ lỗi:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[below] {Số lỗi};
\\draw[line width=1pt, ->] (0,0) -- (0,4.0) node[left] {Số lớp};
\\foreach \\y/\\lbl in {1.4/10, 2.8/20}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.0,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\draw[line width=1pt] (0.7,0) rectangle (1.3,%s);
\\node[above] at (1,%s) {$%s$};
\\node[below] at (1,0) {$0$};
\\draw[line width=1pt, dashed] (1.9,0) rectangle (2.5,2.2);
\\node at (2.2,1.1) {$?$};
\\node[below] at (2.2,0) {$1$};
\\draw[line width=1pt, dashed] (3.1,0) rectangle (3.7,1.1);
\\node at (3.4,0.55) {$?$};
\\node[below] at (3.4,0) {$2$};
\\draw[line width=1pt] (4.3,0) rectangle (4.9,%s);
\\node[above] at (4.6,%s) {$%s$};
\\node[below] at (4.6,0) {$3$};
\\end{tikzpicture}
\\end{center}
Tần số của mức $1$ lỗi là bao nhiêu?''' % (f0, f3, y0, y0, f0, y3, y3, f3))
        
        # Nội dung lời giải
        loigiai = ('''Vì có $50$ tập thể lớp nên tổng tần số của hai cột $1$ lỗi và $2$ lỗi là: $50 - (%s + %s) = %s$.\\\\
Gọi tần số của mức $2$ lỗi là $x$ ($x \\in \\mathbb{N}^*$) thì tần số của mức $1$ lỗi là $2x$.\\\\
Ta có: $2x + x = %s \\Leftrightarrow 3x = %s \\Leftrightarrow x = %s$.\\\\
Vậy tần số của mức $1$ lỗi là $2 \\cdot %s = %s$.''' % (f0, f3, tong_12, tong_12, tong_12, f2, f2, f1))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
        # Xuất câu hỏi
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   str(dapan) +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
