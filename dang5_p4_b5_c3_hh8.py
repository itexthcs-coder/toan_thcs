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


def bt_dang5_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([6, 8, 10, 12, 14, 16])
        dien_tich = (ab ** 2) // 2

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (C) at (0,1.8);
\\coordinate (D) at (0,-1.8);
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (A)--(C)--(B)--(D)--cycle (A)--(B) (C)--(D);
\\draw[line width=1pt] (-0.14,1.66)--(0,1.52)--(0.14,1.66);
\\draw[line width=1pt] (-0.14,-1.66)--(0,-1.52)--(0.14,-1.66);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (O) circle (1pt) node[below right] {$O$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đoạn thẳng $AB$. Trên hai nửa mặt phẳng đối nhau bờ $AB$, vẽ hai tam giác vuông cân tại $C$ và $D$ là $\\Delta ABC$ và $\\Delta ABD$. \\\\
a) Chứng minh tứ giác $ACBD$ là hình vuông. \\\\
b) Gọi $O$ là giao điểm của $AB$ và $CD$. Biết $AB = %s\\text{ cm}$, tính diện tích của hình vuông $ACBD$.%s'''
                         % (ab, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Vì $\\Delta ABC$ vuông cân tại $C$ nên $\\widehat{ACB} = 90^\\circ$ và $\\widehat{CAB} = \\widehat{CBA} = 45^\\circ$.\\\\
Vì $\\Delta ABD$ vuông cân tại $D$ nên $\\widehat{ADB} = 90^\\circ$ và $\\widehat{DAB} = \\widehat{DBA} = 45^\\circ$.\\\\
Suy ra $\\widehat{CAD} = \\widehat{CAB} + \\widehat{DAB} = 45^\\circ + 45^\\circ = 90^\\circ$.\\\\
Tứ giác $ACBD$ có $\\widehat{ACB} = \\widehat{CAD} = \\widehat{ADB} = 90^\\circ$ nên là hình chữ nhật.\\\\
Mặt khác $\\Delta ABC$ cân tại $C$ nên $CA = CB$.\\\\
Hình chữ nhật $ACBD$ có hai cạnh kề bằng nhau nên là hình vuông.
\\item Vì $ACBD$ là hình vuông nên hai đường chéo bằng nhau: $CD = AB = %s\\text{ cm}$ và $AC \\perp BD$ tại $O$ (hay $AB \\perp CD$).\\\\
Diện tích hình vuông $ACBD$ là:\\\\
$S_{ACBD} = \\dfrac{1}{2}AB \\cdot CD = \\dfrac{1}{2}AB^2 = \\dfrac{%s^2}{2} = %s\\text{ (cm}^2)$.
\\end{enumEX} \n'''
                   % (ab, ab, dien_tich))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
