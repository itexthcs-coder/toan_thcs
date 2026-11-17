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

def bt_dang10_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_chon = random.choice([
            (15, 13, 14, 9, 5, 12),
            (10, 17, 21, 6, 15, 8),
            (25, 17, 28, 20, 8, 15)
        ])
        R1, R2, O1O2, x_val, y_val, AH = bo_chon
        AB = 2 * AH
        kq_str = str(AB)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ cắt nhau tại hai điểm phân biệt $A$ và $B$ (như hình vẽ). Biết khoảng cách giữa hai tâm $O_1O_2 = %s\\text{ cm}$. Tính độ dài dây cung chung $AB$ (đơn vị: $\\text{cm}$).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O1) at (-1.1,0);
        \\coordinate (O2) at (1.1,0);
        \\coordinate (H) at (0.15,0);
        \\coordinate (A) at (0.15,1.25);
        \\coordinate (B) at (0.15,-1.25);
        \\draw[line width=1pt] (O1) circle (1.77);
        \\draw[line width=1pt] (O2) circle (1.57);
        \\draw[line width=1pt] (O1)--(O2) (A)--(B) (O1)--(A) (O2)--(A);
        \\fill (O1) circle (1pt) node[left] {$O_1$};
        \\fill (O2) circle (1pt) node[right] {$O_2$};
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (H) circle (1pt) node[below right] {$H$};
        \\end{tikzpicture}
        \\end{center}''' % (R1, R2, O1O2))

        # Nội dung lời giải
        loigiai = ('''Vì $O_1A = O_1B = %s\\text{ cm}$ và $O_2A = O_2B = %s\\text{ cm}$ nên $O_1O_2$ là đường trung trực của dây cung chung $AB$.\\\\
        Gọi $H$ là giao điểm của $O_1O_2$ và $AB$, ta có $O_1O_2 \\perp AB$ tại trung điểm $H$ của $AB$.\\\\
        Đặt $O_1H = x\\text{ (cm)}$ ($0 < x < %s$), suy ra $O_2H = %s - x\\text{ (cm)}$.\\\\
        Áp dụng định lí Pythagore trong hai tam giác vuông $O_1HA$ và $O_2HA$, ta có:\\\\
        $AH^2 = O_1A^2 - O_1H^2 = O_2A^2 - O_2H^2 \\Rightarrow %s^2 - x^2 = %s^2 - (%s - x)^2$.\\\\
        Giải phương trình trên ta được $x = %s\\text{ cm}$.\\\\
        Suy ra $AH = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$, vậy độ dài dây cung chung $AB = 2AH = 2 \\cdot %s = %s\\text{ cm}$.'''
                   % (R1, R2, O1O2, O1O2, R1, R2, O1O2, x_val, R1, x_val, AH, AH, AB))

        #Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
