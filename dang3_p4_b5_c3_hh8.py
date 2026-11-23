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


def bt_dang3_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F'),
            ('M', 'N', 'P', 'Q', 'I', 'K')
        ])
        A, B, C, D, E, F = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (F) at (2,0);
\\coordinate (D) at (4,0);
\\coordinate (B) at (0.8,1.8);
\\coordinate (E) at (2.8,1.8);
\\coordinate (C) at (4.8,1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (E)--(F) (B)--(F) (E)--(D);
\\fill (A) circle (1pt) node[below left] {$%s$};
\\fill (F) circle (1pt) node[below] {$%s$};
\\fill (D) circle (1pt) node[below right] {$%s$};
\\fill (B) circle (1pt) node[above left] {$%s$};
\\fill (E) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[above right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, F, D, B, E, C))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình bình hành $%s%s%s%s$ có $%s%s = 2%s%s$. Gọi $%s$ và $%s$ lần lượt là trung điểm của các cạnh $%s%s$ và $%s%s$. \\\\
a) Chứng minh tứ giác $%s%s%s%s$ là hình thoi. \\\\
b) Tứ giác $%s%s%s%s$ là hình gì? Vì sao? \\\\
c) Hình bình hành $%s%s%s%s$ cần thêm điều kiện gì về góc để tứ giác $%s%s%s%s$ trở thành hình vuông?%s'''
                         % (A, B, C, D, A, D, A, B, E, F, B, C, A, D,
                            A, B, E, F,
                            B, F, D, C,
                            A, B, C, D, A, B, E, F, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n\\item Vì $%s%s%s%s$ là hình bình hành nên $%s%s // %s%s$ và $%s%s = %s%s$.\\\\\nMà $%s$ là trung điểm $%s%s$, $%s$ là trung điểm $%s%s$ nên $%s%s = %s%s = \\dfrac{%s%s}{2} = \\dfrac{%s%s}{2} = %s%s = %s%s$ và $%s%s // %s%s$.\\\\\nSuy ra tứ giác $%s%s%s%s$ là hình bình hành.\\\\\nMặt khác $%s%s = 2%s%s \\Rightarrow %s%s = \\dfrac{%s%s}{2} = %s%s$.\\\\\nHình bình hành $%s%s%s%s$ có hai cạnh kề $%s%s = %s%s$ nên là hình thoi.\n\\item Ta có $%s%s = %s%s$ (cùng bằng $\\dfrac{%s%s}{2}$) và $%s%s // %s%s$ (vì $%s%s // %s%s$).\\\\\nSuy ra tứ giác $%s%s%s%s$ có một cặp cạnh đối song song và bằng nhau nên tứ giác $%s%s%s%s$ là hình bình hành.\n\\item Theo dấu hiệu nhận biết hình vuông: Hình thoi có một góc vuông là hình vuông.\\\\\nDo đó hình thoi $%s%s%s%s$ trở thành hình vuông khi có $\\widehat{%s%s%s} = 90^\\circ$.\\\\\nVậy hình bình hành $%s%s%s%s$ cần thêm điều kiện có một góc vuông (tức là $%s%s%s%s$ là hình chữ nhật).\n\\end{enumEX} \n'''
                   % (A, B, C, D, B, C, A, D, B, C, A, D, E, B, C, F, A, D, B, E, A, F, B, C, A, D, E, C, F, D, B, E, A, F, A, B, E, F, A, D, A, B, A, F, A, D, A, B, A, B, E, F, A, B, A, F, E, C, F, D, A, D, E, C, F, D, B, C, A, D, B, F, D, C, B, F, D, C, A, B, E, F, B, A, F, A, B, C, D, A, B, C, D))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
