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


def bt_dang9_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (5, 12, 13),
            (3, 4, 5),
            (6, 8, 10),
            (8, 15, 17),
            (9, 12, 15)
        ]
        r_val, h_val, l_val = random.choice(bo_pythagore)
        s_day = r_val ** 2
        s_xq = r_val * l_val
        s_tp = s_day + s_xq
        v_pi = (s_day * h_val) // 3
        v_approx = (Decimal(str(v_pi)) * Decimal('3.14')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(v_approx)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình nón có diện tích toàn phần (tổng diện tích xung quanh và diện tích đáy) bằng $%s\\pi\\text{ cm}^2$, biết bán kính đáy $r = %s\\text{ cm}$ (như hình vẽ). Tính thể tích của hình nón đó theo đơn vị $\\text{cm}^3$ (làm tròn kết quả đến hàng đơn vị, lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S) at (0,2.8);
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.5,0);
\\coordinate (B) at (1.5,0);
\\draw[line width=1pt] (S)--(A) (S)--(B);
\\draw[line width=1pt] (-1.5,0) arc (180:360:1.5 and 0.35);
\\draw[line width=1pt, dashed] (1.5,0) arc (0:180:1.5 and 0.35);
\\draw[line width=1pt, dashed] (S)--(O)--(B);
\\node[below] at (0.75,0) {$r = %s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}'''
                         % (s_tp, r_val, r_val))

        # Nội dung lời giải
        loigiai = ('''Diện tích đáy của hình nón là: $S_{\\text{đáy}} = \\pi r^2 = \\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Diện tích xung quanh của hình nón là: $S_{xq} = S_{tp} - S_{\\text{đáy}} = %s\\pi - %s\\pi = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Độ dài đường sinh của hình nón là: $l = \\frac{S_{xq}}{\\pi r} = \\frac{%s\\pi}{%s\\pi} = %s\\text{ (cm)}$. \\\\
Chiều cao của hình nón là: $h = \\sqrt{l^2 - r^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$. \\\\
Thể tích của hình nón là:
$$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi \\approx %s \\cdot 3,14 \\approx %s\\text{ (cm}^3\\text{)}.$$'''
                   % (r_val, s_day, s_tp, s_day, s_xq, s_xq, r_val, l_val,
                      l_val, r_val, h_val, r_val, h_val, v_pi, v_pi, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
