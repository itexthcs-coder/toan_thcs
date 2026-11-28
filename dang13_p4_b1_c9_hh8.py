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


def bt_dang13_p4_b1_c9_hh8(self):
    # Dạng 13: Bài toán kết hợp trọng tâm tam giác và định lí đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        BC = random.choice([9, 12, 15, 18])
        EF = BC * 2 // 3
        S_ABC = 9 * random.choice([4, 5, 6, 7, 8])
        S_AEF = S_ABC * 4 // 9
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5.4,0);\n'
            '\\coordinate (A) at (2.1,3.9);\n'
            '\\coordinate (M) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (G) at ($(A)!0.6667!(M)$);\n'
            '\\coordinate (E) at ($(A)!0.6667!(B)$);\n'
            '\\coordinate (F) at ($(A)!0.6667!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (E)--(F);\n'
            '\\draw[line width=1pt, dashed] (A)--(M);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\fill (G) circle (1pt) node[below right] {$G$};\n'
            '\\fill (E) circle (1pt) node[left] {$E$};\n'
            '\\fill (F) circle (1pt) node[right] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có trọng tâm $G$, cạnh $BC = %s\\text{ cm}$ và diện tích bằng $%s\\text{ cm}^2$. '
            'Đường thẳng đi qua $G$ và song song với $BC$ cắt $AB, AC$ lần lượt tại $E$ và $F$.\\\n'
            'a) Chứng minh $\\Delta AEF \\backsim \\Delta ABC$ và tìm tỉ số đồng dạng.\\\n'
            'b) Tính độ dài đoạn thẳng $EF$ và diện tích $\\Delta AEF$.\\\n%s'
            % (BC, S_ABC, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Gọi $M$ là trung điểm của $BC$. Vì $G$ là trọng tâm của $\\Delta ABC$ nên $G \\in AM$ và $\\dfrac{AG}{AM} = \\dfrac{2}{3}$.\\\n'
            'Xét $\\Delta ABM$ có $EG // BM$ ($E \\in AB$, $G \\in AM$) nên $\\Delta AEG \\backsim \\Delta ABM$, suy ra $\\dfrac{AE}{AB} = \\dfrac{AG}{AM} = \\dfrac{2}{3}$.\\\n'
            'Xét $\\Delta ABC$ có $EF // BC$ ($E \\in AB$, $F \\in AC$) nên $\\Delta AEF \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{AE}{AB} = \\dfrac{2}{3}$.\n'
            '\\item Vì $\\Delta AEF \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{2}{3}$ nên $\\dfrac{EF}{BC} = \\dfrac{2}{3}$.\\\n'
            'Suy ra $EF = \\dfrac{2}{3} \\cdot %s = %s\\text{ (cm)}$.\\\n'
            'Tương tự như tỉ số các cạnh, tỉ số hai đường cao tương ứng kẻ từ $A$ của $\\Delta AEF$ và $\\Delta ABC$ cũng bằng $\\dfrac{2}{3}$.\\\n'
            'Do đó $\\dfrac{S_{\\Delta AEF}}{S_{\\Delta ABC}} = \\left(\\dfrac{2}{3}\\right)^2 = \\dfrac{4}{9} \\Rightarrow S_{\\Delta AEF} = \\dfrac{4}{9} \\cdot %s = %s\\text{ (cm}^2\\text{)}$.\n'
            '\\end{enumEX}'
            % (BC, EF, S_ABC, S_AEF)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
