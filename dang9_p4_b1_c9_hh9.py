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


def bt_dang9_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 10)
        r = random.randint(3, 6)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (-1.4,0);\n'
            '\\coordinate (O1) at (1.0,0);\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (-2.8,0);\n'
            '\\coordinate (C) at (2.0,0);\n'
            '\\coordinate (D) at (-1.4+1.4*cos{60}, 1.4*sin{60});\n'
            '\\coordinate (E) at (1.0-1.0*cos{60}, -1.0*sin{60});\n'
            '\\draw[line width=1pt] (O) circle (1.4cm);\n'
            '\\draw[line width=1pt] (O1) circle (1.0cm);\n'
            '\\draw[line width=1pt] (B)--(C) (D)--(E) (B)--(D) (C)--(E);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (O1) circle (1pt) node[below] {$O\'$};\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[above] {$D$};\n'
            '\\fill (E) circle (1pt) node[below] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O\'; %s\\text{ cm})$ tiếp xúc ngoài tại điểm $A$. Vẽ đường kính $AB$ của $(O)$ và đường kính $AC$ của $(O\')$. Một đường thẳng $d$ đi qua $A$ cắt $(O)$ tại $D$ (khác $A$) và cắt $(O\')$ tại $E$ (khác $A$) như hình vẽ.\\\\'
            'a) Chứng minh $\\widehat{ADB} = \\widehat{AEC} = 90^\\circ$.\\\\'
            'b) Chứng minh $BD // CE$.\\\\'
            'c) Chứng minh tỉ số $\\dfrac{AD}{AE}$ không đổi khi đường thẳng $d$ quay quanh $A$.\n%s'
            % (R, r, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O)$, góc nội tiếp $\\widehat{ADB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{ADB} = 90^\\circ$. Trong đường tròn $(O\')$, góc nội tiếp $\\widehat{AEC}$ chắn nửa đường tròn đường kính $AC$ nên $\\widehat{AEC} = 90^\\circ$.\n'
            '\\item Vì hai đường tròn $(O)$ và $(O\')$ tiếp xúc ngoài tại $A$ nên ba điểm $O, A, O\'$ thẳng hàng, suy ra $B, A, C$ thẳng hàng.\\\\'
            'Ta có $BD \\perp DE$ (do $\\widehat{ADB} = 90^\\circ$) và $CE \\perp DE$ (do $\\widehat{AEC} = 90^\\circ$), suy ra $BD // CE$.\n'
            '\\item Xét hai tam giác vuông $\\triangle ADB$ và $\\triangle AEC$ có $\\widehat{DAB} = \\widehat{EAC}$ (hai góc đối đỉnh) nên $\\triangle ADB \\backsim \\triangle AEC$ (g.g).\\\\'
            'Suy ra $\\dfrac{AD}{AE} = \\dfrac{AB}{AC} = \\dfrac{2R}{2r} = \\dfrac{%s}{%s}$ không đổi khi đường thẳng $d$ quay quanh $A$.\n'
            '\\end{enumEX}'
            % (R, r)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
