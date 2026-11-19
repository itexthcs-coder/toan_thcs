# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang14_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([30, 32, 34, 36, 38, 40])
        nua_R = R // 2
        OH_approx = str(Decimal(float(nua_R * math.sqrt(3))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = ('''Một sân vận động có phần khúc cua ở hai đầu là hai nửa đường tròn bằng nhau bán kính $R = %s\\text{ m}$. Ở một đầu cua nửa đường tròn đường kính $AB$ tâm $O$, người ta căng một sợi dây thẳng nối điểm $A$ với điểm $M$ nằm trên nửa đường tròn sao cho $\\text{sđ}\\overset\\frown{AM} = 60^\\circ$ (như hình vẽ).\\\\
                         a) Tính độ dài sợi dây thẳng $AM$.\\\\
                         b) Tính khoảng cách từ tâm $O$ đến sợi dây thẳng $AM$ (làm tròn đến hàng phần trăm).
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (-1.8,0);
                         \\coordinate (B) at (1.8,0);
                         \\coordinate (M) at (120:1.8);
                         \\coordinate (H) at (-1.35,0.78);
                         \\draw[line width=1pt] (B) arc (0:180:1.8);
                         \\draw[line width=1pt] (A)--(B) (A)--(M) (O)--(M);
                         \\draw[line width=1pt, dashed] (O)--(H);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[left] {$A$};
                         \\fill (B) circle (1pt) node[right] {$B$};
                         \\fill (M) circle (1pt) node[above] {$M$};
                         \\fill (H) circle (1pt) node[above left] {$H$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì góc ở tâm $\\widehat{AOM}$ chắn cung nhỏ $\\overset\\frown{AM}$ có số đo bằng $60^\\circ$ nên $\\widehat{AOM} = 60^\\circ$.\\\\
                        Xét tam giác $OAM$ có $OA = OM = R = %s\\text{ m}$ và $\\widehat{AOM} = 60^\\circ$ nên tam giác $OAM$ là tam giác đều.\\\\
                        Vậy độ dài sợi dây thẳng $AM = OA = %s\\text{ m}$.
                        \\item Kẻ $OH \\perp AM$ tại $H$, khi đó $H$ là trung điểm của $AM$ nên $AH = \\dfrac{AM}{2} = \\dfrac{%s}{2} = %s\\text{ m}$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
                        $OH = \\sqrt{OA^2 - AH^2} = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3} \\approx %s\\text{ m}$.\\\\
                        Vậy khoảng cách từ tâm $O$ đến sợi dây thẳng $AM$ xấp xỉ $%s\\text{ m}$.
                        \\end{enumEX}'''
                   % (R, R, R, nua_R, R, nua_R, nua_R, OH_approx, OH_approx))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
