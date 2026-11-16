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


def bt_dang12_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        thang = random.choice([3, 4, 5])
        goc = 65
        rad = math.radians(goc)
        chan_str = str(Decimal(str(thang * math.cos(rad))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        cao_str = str(Decimal(str(thang * math.sin(rad))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        chan_thu = 1.6 if thang == 3 else (2.2 if thang == 4 else 2.8)
        chan_thu_str = str(chan_thu).replace('.', ',')
        goc_thu = int(Decimal(str(math.degrees(math.acos(chan_thu / thang)))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (C) at (1.3,0);
    \\coordinate (B) at (1.3,2.78);
    \\draw[line width=1pt] (A)--(C)--(B)--cycle;
    \\draw[line width=1pt] (1.08,0)--(1.08,0.22)--(1.3,0.22);
    \\draw[line width=1pt] (0.5,0) arc (0:65:0.5);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\node[above left] at (0.65,1.4) {$%s\\text{ m}$};
    \\node at (0.72,0.32) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (thang, goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc thang cứu hộ $AB$ dài $%s\\text{ m}$ được đặt tựa vào một bức tường thẳng đứng $BC$ (như hình vẽ). Theo quy định an toàn lao động, góc tạo bởi thang và mặt đất $AC$ phải nằm trong khoảng từ $60^\\circ$ đến $70^\\circ$ (góc chuẩn an toàn là $%s^\\circ$). \\\\
    a) Cần đặt chân thang cách chân tường một khoảng bằng bao nhiêu mét (làm tròn đến chữ số thập phân thứ hai) để thang tạo với mặt đất góc chuẩn an toàn $%s^\\circ$? Khi đó đầu thang chạm tường ở độ cao bao nhiêu mét? \\\\
    b) Nếu một người đặt chân thang cách chân tường $%s\\text{ m}$ thì góc tạo bởi thang và mặt đất bằng bao nhiêu độ (làm tròn đến độ) và có đảm bảo quy định an toàn hay không?
    %s''' % (thang, goc, goc, chan_thu_str, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $ABC$ vuông tại $C$, theo Định lí 1 ta có:\\\\
    Khoảng cách từ chân thang đến chân tường là $AC = AB \\cdot \\cos A = %s \\cdot \\cos %s^\\circ \\approx %s\\text{ (m)}$.\\\\
    Độ cao đầu thang chạm tường là $BC = AB \\cdot \\sin A = %s \\cdot \\sin %s^\\circ \\approx %s\\text{ (m)}$.
    \\item Khi đặt chân thang cách chân tường $AC' = %s\\text{ m}$, ta có $\\cos \\widehat{BAC'} = \\dfrac{AC'}{AB} = \\dfrac{%s}{%s}$.\\\\
    Sử dụng máy tính cầm tay, tìm được $\\widehat{BAC'} \\approx %s^\\circ$.\\\\
    Vì $%s^\\circ < 60^\\circ$ (nằm ngoài khoảng an toàn từ $60^\\circ$ đến $70^\\circ$) nên cách đặt thang này không đảm bảo quy định an toàn.
    \\end{enumEX}'''
                   % (thang, goc, chan_str, thang, goc, cao_str,
                      chan_thu_str, chan_thu_str, thang, goc_thu, goc_thu))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
