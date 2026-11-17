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


def bt_dang15_p3_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_vom = [(25, 15, 20), (50, 30, 40), (50, 40, 30), (130, 50, 120), (100, 60, 80), (100, 80, 60)]
        r_10, d_10, ah_10 = random.choice(bo_vom)
        r_val = Rational(r_10, 10)
        d_val = Rational(d_10, 10)
        ah_val = Rational(ah_10, 10)
        ab_val = Rational(2 * ah_10, 10)
        
        def fmt_num(val):
            if val.q == 1:
                return str(int(val))
            return str(Decimal(float(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        r_str = fmt_num(r_val)
        d_str = fmt_num(d_val)
        ah_str = fmt_num(ah_val)
        ab_str = fmt_num(ab_val)
        kq_str = ab_str

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2,1.5);
\\coordinate (B) at (2,1.5);
\\coordinate (H) at (0,1.5);
\\draw[line width=1pt] (2.5,0) arc (0:180:2.5);
\\draw[line width=1pt] (-2.5,0)--(2.5,0);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt, dashed] (O)--(H) (O)--(A) (O)--(B);
\\draw[line width=1pt] (0,1.25)--(0.25,1.25)--(0.25,1.5);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (H) circle (1pt) node[above] {$H$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cổng vòm hình bán nguyệt có bán kính $R = %s\\text{ m}$. Người ta cần lắp đặt một thanh xà ngang nằm ngang bên trong cổng vòm sao cho hai đầu thanh chạm vào mép vòm và khoảng cách từ thanh xà ngang xuống mặt sàn (đường kính của bán nguyệt) là $%s\\text{ m}$. Tính chiều dài của thanh xà ngang đó (đơn vị: mét).'''
                         %(r_str, d_str))
        
        # Nội dung lời giải
        loigiai = ('''%s \\\\
Mô hình hóa cổng vòm là nửa đường tròn tâm $O$ bán kính $R = %s\\text{ m}$, thanh xà ngang là dây cung $AB$ song song với đường kính đáy và cách $O$ một khoảng $OH = %s\\text{ m}$ ($OH \\perp AB$). \\\\
Xét tam giác $OAH$ vuông tại $H$, áp dụng định lí Pythagore ta có: \\\\
$AH = \\sqrt{OA^2 - OH^2} = \\sqrt{(%s)^2 - (%s)^2} = %s\\text{ (m)}$. \\\\
Vì $OH \\perp AB$ nên $H$ là trung điểm của dây cung $AB$. Do đó chiều dài thanh xà ngang là: \\\\
$AB = 2 \\cdot AH = 2 \\cdot %s = %s\\text{ (m)}$.'''
                   %(hinhve, r_str, d_str, r_str, d_str, ah_str, ah_str, ab_str))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
