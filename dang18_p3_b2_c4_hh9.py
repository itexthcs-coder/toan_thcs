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


def bt_dang18_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        rong = random.choice([15, 17, 19])
        dai = random.choice([22, 24, 26])
        beta_val = math.degrees(math.atan(dai / rong))
        alpha_val = 180.0 - 2.0 * beta_val

        beta_str = str(Decimal(str(beta_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        number = Decimal(str(alpha_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2.4,0);
    \\coordinate (C) at (2.4,3.4);
    \\coordinate (D) at (0,3.4);
    \\coordinate (O) at (1.2,1.7);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\draw[line width=1pt] (0.95,1.35) arc (234.8:305.2:0.43);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (D) circle (1pt) node[above left] {$D$};
    \\fill (O) circle (1pt) node[above] {$O$};
    \\node[below] at (1.2,0) {$%s\\text{ cm}$};
    \\node[right] at (2.4,1.7) {$%s\\text{ cm}$};
    \\node at (1.2,1.08) {$\\alpha$};
    \\end{tikzpicture}
    \\end{center}''' % (rong, dai))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cuốn sách khổ $%s \\times %s\\text{ cm}$ (chiều rộng $AB = %s\\text{ cm}$, chiều dài $BC = %s\\text{ cm}$). Gọi $\\alpha = \\widehat{AOB}$ là góc nhọn tạo bởi hai đường chéo $AC$ và $BD$ của trang sách đó (như hình vẽ). Tính số đo góc $\\alpha$ theo đơn vị độ (làm tròn kết quả đến hàng đơn vị).
    %s''' % (rong, dai, rong, dai, hinhve))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABC$ vuông tại $B$, ta có $\\tan \\widehat{BAC} = \\dfrac{BC}{AB} = \\dfrac{%s}{%s} \\Rightarrow \\widehat{BAC} \\approx %s^\\circ$.\\\\
    Vì $ABCD$ là hình chữ nhật nên $OA = OB$, suy ra tam giác $OAB$ cân tại $O$ và $\\widehat{OBA} = \\widehat{OAB} \\approx %s^\\circ$.\\\\
    Do đó số đo góc nhọn tạo bởi hai đường chéo là $\\alpha = \\widehat{AOB} = 180^\\circ - 2 \\cdot \\widehat{OAB} \\approx 180^\\circ - 2 \\cdot %s^\\circ \\approx %s^\\circ$.'''
                   % (dai, rong, beta_str, beta_str, beta_str, str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
