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

def bt_dang12_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_so = random.choice([(4, 8, 10), (6, 12, 15), (8, 16, 20), (3, 9, 15), (5, 15, 25)])
        h, a, R = bo_so
        AB = 2 * a
        dk = 2 * R
        kq_str = str(dk)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một nhà khảo cổ tìm được một mảnh vỡ của một chiếc đĩa gốm cổ hình tròn. Ông đo được một dây cung $AB = %s\\text{ cm}$ trên mảnh vỡ và khoảng cách từ điểm chính giữa $M$ của cung nhỏ $\\overparen{AB}$ đến dây $AB$ bằng $%s\\text{ cm}$ (như hình vẽ). Tính đường kính của chiếc đĩa gốm cổ ban đầu (đơn vị: $\\text{cm}$).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (A) at (143:2.0);
        \\coordinate (B) at (37:2.0);
        \\coordinate (H) at (0,1.2);
        \\coordinate (M) at (0,2.0);
        \\draw[line width=1pt, dashed] (O) circle (2.0);
        \\draw[line width=1pt] (B) arc (37:143:2.0);
        \\draw[line width=1pt] (A)--(B);
        \\draw[line width=1pt, dashed] (O)--(A) (O)--(M);
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (H) circle (1pt) node[below right] {$H$};
        \\fill (M) circle (1pt) node[above] {$M$};
        \\end{tikzpicture}
        \\end{center}''' % (AB, h))

        # Nội dung lời giải
        loigiai = ('''Gọi $O$ là tâm và $R\\text{ (cm)}$ là bán kính của chiếc đĩa ban đầu.\\\\
        Vì $M$ là điểm chính giữa cung nhỏ $\\overparen{AB}$ nên $OM \\perp AB$ tại trung điểm $H$ của $AB$.\\\\
        Ta có $AH = \\dfrac{AB}{2} = \\dfrac{%s}{2} = %s\\text{ cm}$, $MH = %s\\text{ cm}$ và $OH = OM - MH = R - %s\\text{ (cm)}$.\\\\
        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
        $(R - %s)^2 + %s^2 = R^2 \\Leftrightarrow R^2 - %sR + %s + %s = R^2 \\Leftrightarrow %sR = %s \\Leftrightarrow R = %s\\text{ cm}$.\\\\
        Vậy đường kính của chiếc đĩa ban đầu là $2R = 2 \\cdot %s = %s\\text{ cm}$.'''
                   % (AB, a, h, h, h, a, 2*h, h*h, a*a, 2*h, h*h + a*a, R, R, dk))

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
