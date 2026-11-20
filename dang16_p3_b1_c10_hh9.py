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


def bt_dang16_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (15, 9, 24),
            (16, 10, 21),
            (18, 12, 24),
            (14, 8, 21)
        ]
        r_lon, r_nho, h_xo = random.choice(cau_hinh)
        v_pi = (h_xo * (r_lon ** 2 + r_lon * r_nho + r_nho ** 2)) // 3
        v_cm3 = Decimal(str(v_pi)) * Decimal('3.14')
        v_lit = (v_cm3 / Decimal('1000')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        v_cm3_str = str(v_cm3.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        kq_str = str(v_lit).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc xô tôn dạng hình nón cụt (không có nắp) dùng để đựng nước có bán kính miệng xô là $R = %s\\text{ cm}$, bán kính đáy xô là $r = %s\\text{ cm}$ và chiều cao của xô là $h = %s\\text{ cm}$ (như hình vẽ). Hỏi chiếc xô này chứa được tối đa bao nhiêu lít nước (làm tròn kết quả đến hàng phần mười, lấy $\\pi \\approx 3,14$ và $1\\text{ lít} = 1000\\text{ cm}^3$)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.2) ellipse (1.8 and 0.4);
\\draw[line width=1pt] (-1.1,0) arc (180:360:1.1 and 0.25);
\\draw[line width=1pt, dashed] (1.1,0) arc (0:180:1.1 and 0.25);
\\draw[line width=1pt] (-1.8,2.2)--(-1.1,0) (1.8,2.2)--(1.1,0);
\\draw[line width=1pt, dashed] (0,2.2)--(0,0)--(1.1,0) (0,2.2)--(1.8,2.2);
\\node[above] at (0.9,2.2) {$R$};
\\node[below] at (0.55,0) {$r$};
\\node[left] at (0,1.1) {$h$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_lon, r_nho, h_xo))

        # Nội dung lời giải
        loigiai = ('''Thể tích của chiếc xô dạng hình nón cụt được tính theo công thức:
$$V = \\frac{1}{3}\\pi h (R^2 + Rr + r^2) = \\frac{1}{3}\\pi \\cdot %s \\cdot (%s^2 + %s \\cdot %s + %s^2) = %s\\pi\\text{ (cm}^3\\text{)}.$$
Thay $\\pi \\approx 3,14$, ta được:
$$V \\approx %s \\cdot 3,14 = %s\\text{ (cm}^3\\text{)} \\approx %s\\text{ (lít)}.$$'''
                   % (h_xo, r_lon, r_lon, r_nho, r_nho, v_pi, v_pi, v_cm3_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
