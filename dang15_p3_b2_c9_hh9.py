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

def bt_dang15_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        goc_nhon = random.choice([30, 60])
        ti_so = sqrt(3) + 1
        number = Decimal(str(float(ti_so)))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (B) at (-1.7,0);
\\coordinate (C) at (1.7,0);
\\coordinate (A) at (60:1.7);
\\coordinate (I) at (0.38,0.45);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (I) circle (0.45);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (I) circle (1pt) node[above] {$I$};
\\fill (A) circle (1pt) node[above right] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ có $\\widehat{%s} = %s^\\circ$. Tỉ số giữa bán kính đường tròn ngoại tiếp $R$ và bán kính đường tròn nội tiếp $r$ của tam giác $%s%s%s$ bằng bao nhiêu (làm tròn kết quả đến hàng phần trăm)?%s'''
                         % (A, B, C, A, B, goc_nhon, A, B, C, hinh_ve))

        loigiai = ('''Tam giác $%s%s%s$ vuông tại $%s$ có một góc nhọn bằng $%s^\\circ$ nên góc nhọn còn lại bằng $%s^\\circ$.\\\\
Gọi độ dài cạnh góc vuông nhỏ là $a$ ($a > 0$), khi đó cạnh huyền bằng $2a$ và cạnh góc vuông lớn bằng $a\\sqrt{3}$.\\\\
Bán kính đường tròn ngoại tiếp tam giác $%s%s%s$ là $R = \\frac{2a}{2} = a$.\\\\
Bán kính đường tròn nội tiếp tam giác $%s%s%s$ là $r = \\frac{a + a\\sqrt{3} - 2a}{2} = \\frac{\\sqrt{3} - 1}{2}a$.\\\\
Vậy tỉ số giữa bán kính đường tròn ngoại tiếp và nội tiếp là:
$$\\frac{R}{r} = \\frac{a}{\\frac{\\sqrt{3} - 1}{2}a} = \\frac{2}{\\sqrt{3} - 1} = \\sqrt{3} + 1 \\approx %s.$$'''
                   % (A, B, C, A, goc_nhon, 90 - goc_nhon, A, B, C, A, B, C, str(kq_str)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
