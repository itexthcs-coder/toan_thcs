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


def bt_dang12_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (6, 8, 10),
            (12, 16, 20),
            (12, 5, 13)
        ]
        r_val, h_non, l_non = random.choice(bo_pythagore)
        while l_non % 2 != 0:
            r_val, h_non, l_non = random.choice(bo_pythagore)
        h_tru = l_non // 2
        sxq = 2 * r_val * h_tru
        kq_str = str(h_non)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình trụ và một hình nón có cùng bán kính đáy $R = %s\\text{ cm}$ (như hình vẽ). Biết diện tích xung quanh của hình trụ bằng diện tích xung quanh của hình nón, và chiều cao của hình trụ là $h_{\\text{trụ}} = %s\\text{ cm}$. Tính chiều cao của hình nón đó (đơn vị: $\\text{cm}$).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.2) ellipse (1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (1.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0)--(-1.2,2.2) (1.2,0)--(1.2,2.2);
\\draw[line width=1pt, dashed] (0,0)--(1.2,0);
\\node[below] at (0.6,0) {$R$};
\\coordinate (S) at (4,2.6);
\\coordinate (O) at (4,0);
\\coordinate (A) at (2.8,0);
\\coordinate (B) at (5.2,0);
\\draw[line width=1pt] (S)--(A) (S)--(B);
\\draw[line width=1pt] (2.8,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (5.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt, dashed] (S)--(O)--(B);
\\node[below] at (4.6,0) {$R$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_val, h_tru))

        # Nội dung lời giải
        loigiai = ('''Diện tích xung quanh của hình trụ là: $S_{xq\\text{ (trụ)}} = 2\\pi R h_{\\text{trụ}} = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Vì diện tích xung quanh của hình nón bằng diện tích xung quanh của hình trụ nên:
$$\\pi R l = %s\\pi \\Rightarrow l = \\frac{%s\\pi}{%s\\pi} = %s\\text{ (cm)}.$$
Chiều cao của hình nón là:
$$h_{\\text{nón}} = \\sqrt{l^2 - R^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$'''
                   % (r_val, h_tru, sxq, sxq, sxq, r_val, l_non, l_non, r_val, h_non))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
