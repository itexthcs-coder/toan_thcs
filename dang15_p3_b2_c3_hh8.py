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


def bt_dang15_p3_b2_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ma_dec = Decimal(random.randint(3, 6)) + Decimal('0.5')
        mb_dec = Decimal(random.randint(4, 7)) + Decimal('0.5')
        mc_dec = Decimal(random.randint(5, 8)) + Decimal('0.5')
        chu_vi_dec = ma_dec + mb_dec + mc_dec
        kq = mc_dec.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        ma_str = str(ma_dec).replace('.', ',')
        mb_str = str(mb_dec).replace('.', ',')
        cv_str = str(chu_vi_dec).replace('.', ',')
        tong_ab_str = str(ma_dec + mb_dec).replace('.0', '')

        hinh_ve = '''
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (2,3.46);
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4,0);
        \\coordinate (M) at (1.8,1.3);
        \\coordinate (P) at (1.05,1.82);
        \\coordinate (Q) at (2.55,0);
        \\coordinate (R) at (2.55,2.51);
        \\draw[line width=1pt] (A)--(B)--(C)--(A) (P)--(Q)--(R)--(P);
        \\draw[line width=1pt, dashed] (M)--(P) (M)--(Q) (M)--(R);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (P) circle (1pt) node[left] {$P$};
        \\fill (Q) circle (1pt) node[below] {$Q$};
        \\fill (R) circle (1pt) node[right] {$R$};
        \\end{tikzpicture}
        \\end{center}'''

        noidungcauhoi = ('''Cho điểm $M$ nằm trong tam giác đều $ABC$. Qua $M$ kẻ các đường thẳng song song với $BC$, $CA$, $AB$ lần lượt cắt $AB$, $BC$, $CA$ tại $P$, $Q$, $R$ (như hình vẽ). Biết tam giác $PQR$ có chu vi bằng $%s\\text{ cm}$, $MA = %s\\text{ cm}$ và $MB = %s\\text{ cm}$. Tính độ dài đoạn thẳng $MC$ (đơn vị: $\\text{cm}$). %s'''
                         % (cv_str, ma_str, mb_str, hinh_ve))

        loigiai = ('''Vì các tứ giác $APMR$, $BQMP$, $CRMQ$ đều là hình thang cân nên $PR = MA$, $PQ = MB$, $QR = MC$.\\\\
                   Do đó chu vi tam giác $PQR$ bằng $MA + MB + MC = %s\\text{ cm}$.\\\\
                   Suy ra $MC = %s - (%s + %s) = %s - %s = %s\\text{ cm}$.\\\\
                   Vậy $MC = %s\\text{ cm}$.'''
                   % (cv_str, cv_str, ma_str, mb_str, cv_str, tong_ab_str, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
