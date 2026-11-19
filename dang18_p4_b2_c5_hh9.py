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

def bt_dang18_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([40, 50, 60, 70])
        goc_quay = random.choice([210, 216, 220, 240, 250])
        cung_nho = 360 - goc_quay
        nua_cung_nho = cung_nho // 2
        AB_val = 2 * R * math.sin(math.radians(nua_cung_nho))
        AB_round = str(Decimal(str(AB_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = ('''Một tang trống cuốn cáp điện có mặt cắt ngang hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$. Khi tang trống quay được một góc ở tâm bằng $%s^\\circ$, một điểm $A$ trên vành ngoài của tang trống di chuyển đến vị trí $B$ (như hình vẽ).\\\\
                         a) Tính số đo cung nhỏ $\\overset\\frown{AB}$ tạo bởi vị trí đầu và vị trí cuối của điểm $A$.\\\\
                         b) Tính khoảng cách thẳng giữa hai điểm $A$ và $B$ (làm tròn đến hàng phần mười của $\\text{cm}$).
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (18:1.8);
                         \\coordinate (B) at (162:1.8);
                         \\coordinate (H) at (0,0.56);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(B) (O)--(A) (O)--(B);
                         \\draw[line width=1pt, dashed] (O)--(H);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[right] {$A$};
                         \\fill (B) circle (1pt) node[left] {$B$};
                         \\fill (H) circle (1pt) node[above] {$H$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R, goc_quay))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì tang trống quay được một góc ở tâm bằng $%s^\\circ > 180^\\circ$ nên điểm $A$ vạch nên cung lớn $\\overset\\frown{AB}$ có số đo bằng $%s^\\circ$.\\\\
                        Suy ra số đo của cung nhỏ $\\overset\\frown{AB}$ là $\\text{sđ}\\overset\\frown{AB}_{\\text{nhỏ}} = 360^\\circ - %s^\\circ = %s^\\circ$.
                        \\item Vì $\\text{sđ}\\overset\\frown{AB}_{\\text{nhỏ}} = %s^\\circ$ nên góc ở tâm $\\widehat{AOB} = %s^\\circ$.\\\\
                        Kẻ $OH \\perp AB$ tại $H$, khi đó $AB = 2AH$ và $\\widehat{AOH} = \\dfrac{\\widehat{AOB}}{2} = \\dfrac{%s^\\circ}{2} = %s^\\circ$.\\\\
                        Trong tam giác $OHA$ vuông tại $H$, ta có $AH = OA \\cdot \\sin %s^\\circ = %s \\cdot \\sin %s^\\circ$.\\\\
                        Vậy khoảng cách thẳng giữa hai điểm $A$ và $B$ là $AB = 2AH = 2 \\cdot %s \\cdot \\sin %s^\\circ \\approx %s\\text{ cm}$.
                        \\end{enumEX}'''
                   % (goc_quay, goc_quay, goc_quay, cung_nho,
                      cung_nho, cung_nho, cung_nho, nua_cung_nho,
                      nua_cung_nho, R, nua_cung_nho, R, nua_cung_nho, AB_round))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
