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


def bt_dang1_p3_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ten = random.choice(['Khoa', 'Minh', 'Tuấn', 'Huy'])
        dk = random.choice([
            ('chia hết cho $4$', 4, 9, '$(1, 3); (2, 2); (3, 1); (2, 6); (3, 5); (4, 4); (5, 3); (6, 2); (6, 6)$'),
            ('chia hết cho $5$', 5, 7, '$(1, 4); (2, 3); (3, 2); (4, 1); (4, 6); (5, 5); (6, 4)$'),
            ('bằng $7$', 7, 6, '$(1, 6); (2, 5); (3, 4); (4, 3); (5, 2); (6, 1)$'),
            ('lớn hơn $9$', 10, 6, '$(4, 6); (5, 5); (5, 6); (6, 4); (6, 5); (6, 6)$')
        ])
        nd_dk, _, so_kq, chuoi_tl = dk
        kq_str = str(so_kq)

        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.5cm);
\\draw[line width=1pt] (0,-1.5)--(0,1.5);
\\draw[line width=1pt] (-1.3,0.75)--(1.3,-0.75);
\\draw[line width=1pt] (-1.3,-0.75)--(1.3,0.75);
\\draw[line width=1pt, ->] (0,0)--(0,-1.1);
\\fill (0,0) circle (1pt);
\\node at (-0.45,0.85) {$1$};
\\node at (0.45,0.85) {$2$};
\\node at (0.95,0) {$3$};
\\node at (0.45,-0.85) {$4$};
\\node at (-0.45,-0.85) {$5$};
\\node at (-0.95,0) {$6$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một tấm bìa cứng hình tròn được chia làm $6$ hình quạt bằng nhau, đánh số $1; 2; 3; 4; 5; 6$ và được gắn vào trục quay có mũi tên ở tâm như hình vẽ. Bạn %s quay tấm bìa hai lần liên tiếp, quan sát và ghi lại số của hình quạt mà mũi tên chỉ vào. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố $E$: ``Tổng hai số ghi trên hai hình quạt ở hai lần quay %s''?%s'''
                         % (ten, nd_dk, hinh_ve))

        loigiai = ('''Không gian mẫu $\\Omega$ gồm $6 \\cdot 6 = 36$ cặp số $(a, b)$ với $a, b \\in \\{1; 2; 3; 4; 5; 6\\}$.\\\\
Các kết quả thuận lợi cho biến cố $E$ (tổng hai số %s) gồm: %s.\\\\
Vậy có $%s$ kết quả thuận lợi cho biến cố $E$.'''
                   % (nd_dk, chuoi_tl, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
