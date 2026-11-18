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


def bt_dang15_p3_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Tổng 35 HS: A(5; 4), B(6; m), C(7; n), D(8; 6) => m + n = 25; n = 1,5m => m = 10, n = 15
        f_a = random.choice([4, 6])
        f_d = 10 - f_a
        m_val = 10
        n_val = 15
        kq_str = str(n_val)
        ya = round(f_a * 0.22, 2)
        yb = round(m_val * 0.22, 2)
        yc = round(n_val * 0.22, 2)
        yd = round(f_d * 0.22, 2)
        # Nội dung câu hỏi
        noidungcauhoi = ('''Đa giác tần số dưới đây biểu diễn số giờ tự học buổi tối trong tuần của $35$ học sinh lớp $9K$. Biết tần số của giá trị $7$ giờ gấp $1,5$ lần tần số của giá trị $6$ giờ ($n = 1,5m$):
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Số giờ tự học};
\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Số học sinh};
\\foreach \\y/\\lbl in {1.1/5, 2.2/10, 3.3/15}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (4.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\coordinate (A) at (1,%s);
\\coordinate (B) at (2,%s);
\\coordinate (C) at (3,%s);
\\coordinate (D) at (4,%s);
\\draw[line width=1pt] (A) -- (B) -- (C) -- (D);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[above] {$m$};
\\fill (C) circle (1pt) node[above] {$n$};
\\fill (D) circle (1pt) node[above] {$%s$};
\\node[below] at (1,0) {$5$};
\\node[below] at (2,0) {$6$};
\\node[below] at (3,0) {$7$};
\\node[below] at (4,0) {$8$};
\\end{tikzpicture}
\\end{center}
Giá trị của $n$ bằng bao nhiêu?''' % (ya, yb, yc, yd, f_a, f_d))
        
        # Nội dung lời giải
        loigiai = ('''Vì lớp $9K$ có $35$ học sinh nên tổng các tần số là: $%s + m + n + %s = 35 \\Leftrightarrow m + n = 25$.\\\\
Thay $n = 1,5m$ vào phương trình trên ta được: $m + 1,5m = 25 \\Leftrightarrow 2,5m = 25 \\Leftrightarrow m = 10$.\\\\
Suy ra $n = 1,5 \\cdot 10 = 15$. Vậy giá trị của $n$ bằng $15$.''' % (f_a, f_d))
        
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
