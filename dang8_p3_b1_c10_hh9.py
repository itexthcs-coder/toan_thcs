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


def bt_dang8_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (216, 3, 5, 15, 9, 12),
            (216, 3, 5, 10, 6, 8),
            (288, 4, 5, 15, 12, 9),
            (288, 4, 5, 10, 8, 6)
        ]
        goc_deg, tu_so, mau_so, l_val, r_val, h_val = random.choice(cau_hinh)
        c_day = 2 * r_val
        kq_str = str(h_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cắt một hình quạt tròn tâm $S$, bán kính $SA = %s\\text{ cm}$ có số đo cung bằng $%s^\\circ$ (tức là bằng $\\frac{%s}{%s}$ hình tròn bán kính $%s\\text{ cm}$). Cuộn hình quạt tròn này lại sao cho $SA$ và $SB$ trùng khít nhau để tạo thành một hình nón đỉnh $S$ (như hình vẽ). Tính chiều cao của hình nón tạo thành (đơn vị: $\\text{cm}$).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S1) at (0,1.4);
\\draw[line width=1pt] (S1)--(-1.1,2.2) arc (144:-144:1.36) -- cycle;
\\draw[->, line width=1pt] (1.9,1.4)--(3.1,1.4);
\\coordinate (S2) at (5.2,2.7);
\\coordinate (O2) at (5.2,0.2);
\\coordinate (A2) at (4.1,0.2);
\\coordinate (B2) at (6.3,0.2);
\\draw[line width=1pt] (S2)--(A2) (S2)--(B2);
\\draw[line width=1pt] (4.1,0.2) arc (180:360:1.1 and 0.28);
\\draw[line width=1pt, dashed] (6.3,0.2) arc (0:180:1.1 and 0.28);
\\draw[line width=1pt, dashed] (S2)--(O2);
\\fill (S1) circle (1pt) node[right] {$S$};
\\fill (S2) circle (1pt) node[above] {$S$};
\\fill (O2) circle (1pt) node[below] {$O$};
\\end{tikzpicture}
\\end{center}'''
                         % (l_val, goc_deg, tu_so, mau_so, l_val))

        # Nội dung lời giải
        loigiai = ('''Khi cuộn hình quạt tròn thành hình nón, độ dài đường sinh của hình nón bằng bán kính hình quạt tròn: $l = SA = %s\\text{ cm}$. \\\\
Chu vi đáy của hình nón bằng độ dài cung $AB$ của hình quạt tròn:
$$C = \\frac{%s}{%s} \\cdot 2\\pi \\cdot %s = %s\\pi\\text{ (cm)}.$$
Suy ra bán kính đáy của hình nón là: $2\\pi r = %s\\pi \\Rightarrow r = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore, chiều cao của hình nón tạo thành là:
$$h = \\sqrt{l^2 - r^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$'''
                   % (l_val, tu_so, mau_so, l_val, c_day, c_day, r_val, l_val, r_val, h_val))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
