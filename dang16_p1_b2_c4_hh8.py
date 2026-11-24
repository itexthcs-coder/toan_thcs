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


def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def bt_dang16_p1_b2_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_diem = random.choice([
            ('A', 'B', 'C', 'D', 'E'),
            ('M', 'N', 'P', 'H', 'K')
        ])
        A, B, C, D, E = bo_diem
        s_abc = random.choice([16, 20, 24, 28, 32, 36, 40, 48, 60])
        s_ade = s_abc // 4
    
        du = ['$%s\\text{ cm}^2$' % fmt_num(s_ade)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}^2$' % fmt_num(s_abc // 2),
            '$%s\\text{ cm}^2$' % fmt_num(s_abc // 3),
            '$%s\\text{ cm}^2$' % fmt_num(s_ade + 3),
            '$%s\\text{ cm}^2$' % fmt_num(s_ade * 3),
            '$%s\\text{ cm}^2$' % fmt_num(s_abc * 2)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (1.5,3);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4.5,0);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s);
\\fill (%s) circle (1pt) node[above] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, A, B, E, A, C, A, B, C, D, E, A, A, B, B, C, C, D, D, E, E))
    
        noidungcauhoi = ('''Cho tam giác $%s%s%s$ có diện tích bằng $%s\\text{ cm}^2$. Gọi $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$ (như hình vẽ). Diện tích của tam giác $%s%s%s$ bằng%s''' % (A, B, C, fmt_num(s_abc), D, E, A, B, A, C, A, D, E, hinhve))
    
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        loigiai = ('''Xét tam giác $%s%s%s$ có $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$.\\
Do đó, $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s = \\dfrac{1}{2}%s%s$ và $%s%s // %s%s$.\\
Kẻ đường cao $%sH$ của tam giác $%s%s%s$ ($H \\in %s%s$), cắt $%s%s$ tại $K$. Vì $%s%s // %s%s$ và $%s$ là trung điểm $%s%s$ nên $K$ là trung điểm $%sH$, hay $%sK = \\dfrac{1}{2}%sH$.\\
Diện tích tam giác $%s%s%s$ là:\\
$S_{%s%s%s} = \\dfrac{1}{2} \\cdot %sK \\cdot %s%s = \\dfrac{1}{2} \\cdot \\left(\\dfrac{1}{2}%sH\\right) \\cdot \\left(\\dfrac{1}{2}%s%s\\right) = \\dfrac{1}{4} S_{%s%s%s} = \\dfrac{1}{4} \\cdot %s = %s\\text{ cm}^2$.\\
Vậy diện tích của tam giác $%s%s%s$ bằng $%s\\text{ cm}^2$.''' % (A, B, C, D, E, A, B, A, C, D, E, A, B, C, D, E, B, C, D, E, B, C, A, A, B, C, B, C, D, E, D, E, B, C, D, A, B, A, A, A, A, D, E, A, D, E, A, D, E, A, B, C, A, B, C, fmt_num(s_abc), fmt_num(s_ade), A, D, E, fmt_num(s_ade)))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
