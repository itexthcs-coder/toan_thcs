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

def bt_dang12_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        gocBAH = randint(18, 32)
        gocOAH = randint(8, 20)
        gocA = 2 * gocBAH + gocOAH
        gocB = 90 - gocBAH
        kq_str = str(gocB)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (105:1.6);
\\coordinate (B) at (215:1.6);
\\coordinate (C) at (-35:1.6);
\\coordinate (H) at (-0.15,0.65);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(O) (A)--(H);
\\draw[line width=1pt, dashed] (B)--(H)--(C);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác nhọn $%s%s%s$ ($%s%s < %s%s$) nội tiếp đường tròn $(O)$. Gọi $H$ là trực tâm của tam giác $%s%s%s$. Biết $\\widehat{%s%s%s} = %s^\\circ$ và $\\widehat{O%sH} = %s^\\circ$. Số đo góc $\\widehat{%s%s%s}$ bằng bao nhiêu độ?%s'''
                         % (A, B, C, A, B, A, C, A, B, C, B, A, C, gocA, A, gocOAH, A, B, C, hinh_ve))

        loigiai = ('''Theo tính chất liên hệ giữa trực tâm $H$ và tâm đường tròn ngoại tiếp $O$ của tam giác nhọn $%s%s%s$, ta có $\\widehat{%s%sH} = \\widehat{O%s%s}$.\\\\
Vì $%s%s < %s%s$ nên tia $%sH$ nằm giữa hai tia $%s%s$ và $%sO$, do đó:
$$\\widehat{%s%sH} + \\widehat{O%sH} + \\widehat{O%s%s} = \\widehat{%s%s%s} \\Rightarrow 2\\widehat{%s%sH} + %s^\\circ = %s^\\circ \\Rightarrow \\widehat{%s%sH} = %s^\\circ.$$
Gọi $K$ là chân đường cao kẻ từ $%s$ xuống $%s%s$. Xét tam giác $%s%sK$ vuông tại $K$, ta có:
$$\\widehat{%s%s%s} = 90^\\circ - \\widehat{%s%sH} = 90^\\circ - %s^\\circ = %s^\\circ.$$'''
                   % (A, B, C, B, A, A, C, A, B, A, C, A, A, B, A, B, A, A, A, C, B, A, C, B, A, gocOAH, gocA, B, A, gocBAH, A, B, C, A, B, A, B, C, B, A, gocBAH, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
