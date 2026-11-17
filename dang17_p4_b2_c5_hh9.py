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

def bt_dang17_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
        OH = 3 * k
        AH = 4 * k
        R = 5 * k
        AB = 2 * AH
        goc_aoh = round(math.degrees(math.asin(0.8)), 2)
        goc_aob = round(2 * goc_aoh)

        noidungcauhoi = ('''Một vòi phun nước tự động đặt tại tâm $O$ của một khu vườn, có tầm phun xa tối đa $R = %s\\text{ m}$ tạo thành vùng tưới hình tròn. Do vướng một bức tường rào thẳng chạy ngang qua vườn, dòng nước bị tường chắn lại theo một đoạn thẳng $AB$ dài $%s\\text{ m}$ (như hình vẽ).\\\\
                         a) Tính khoảng cách ngắn nhất từ vòi phun $O$ đến bức tường rào.\\\\
                         b) Tính góc quay hiệu dụng $\\widehat{AOB}$ (làm tròn đến độ) của vòi phun nếu chỉ tính phần góc quét bị bức tường chắn ngang.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (143:1.8);
                         \\coordinate (B) at (37:1.8);
                         \\coordinate (H) at (0,1.08);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (-2.1,1.08)--(2.1,1.08);
                         \\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(H);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[above left] {$A$};
                         \\fill (B) circle (1pt) node[above right] {$B$};
                         \\fill (H) circle (1pt) node[above] {$H$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R, AB))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Kẻ $OH \\perp AB$ tại $H$, khi đó $OH$ là khoảng cách ngắn nhất từ vòi phun $O$ đến bức tường rào.\\\\
                        Vì tam giác $OAB$ cân tại $O$ nên $H$ là trung điểm của $AB$, suy ra $AH = \\dfrac{AB}{2} = \\dfrac{%s}{2} = %s\\text{ m}$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
                        $OH = \\sqrt{OA^2 - AH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$.\\\\
                        Vậy khoảng cách ngắn nhất từ vòi phun $O$ đến bức tường rào bằng $%s\\text{ m}$.
                        \\item Trong tam giác $OHA$ vuông tại $H$, ta có $\\sin \\widehat{AOH} = \\dfrac{AH}{OA} = \\dfrac{%s}{%s} = 0,8 \\Rightarrow \\widehat{AOH} \\approx 53,13^\\circ$.\\\\
                        Vì $OH$ đồng thời là tia phân giác của $\\widehat{AOB}$ nên $\\widehat{AOB} = 2\\widehat{AOH} \\approx 2 \\cdot 53,13^\\circ = 106,26^\\circ \\approx %s^\\circ$.
                        \\end{enumEX}'''
                   % (AB, AH, R, AH, OH, OH, AH, R, goc_aob))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
