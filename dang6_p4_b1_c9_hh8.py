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


def bt_dang6_p4_b1_c9_hh8(self):
    # Dạng 6: Tính diện tích tam giác và tứ giác thông qua tỉ số đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        q = random.choice([3, 4, 5])
        bm_num = random.choice([1, 2])
        p = q - bm_num
        S_ABC = (q ** 2) * random.choice([2, 3, 4])
        S_AMN = (p ** 2) * (S_ABC // (q ** 2))
        S_BMNC = S_ABC - S_AMN
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (1.8,3.6);\n'
            '\\coordinate (M) at ($(A)!0.66!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.66!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có diện tích bằng $%s\\text{ cm}^2$. Trên cạnh $AB$ lấy điểm $M$ sao cho $BM = \\dfrac{%s}{%s}AB$. '
            'Qua $M$ kẻ đường thẳng song song với $BC$ cắt $AC$ tại $N$.\\\n'
            'a) Chứng minh $\\Delta AMN \\backsim \\Delta ABC$ và tìm tỉ số đồng dạng.\\\n'
            'b) Tính diện tích tứ giác $BMNC$.\\\n%s'
            % (S_ABC, bm_num, q, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AB$, $N \\in AC$) nên $\\Delta AMN \\backsim \\Delta ABC$.\\\n'
            'Vì $M$ nằm trên cạnh $AB$ và $BM = \\dfrac{%s}{%s}AB$ nên $AM = AB - BM = AB - \\dfrac{%s}{%s}AB = \\dfrac{%s}{%s}AB$.\\\n'
            'Vậy $\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{AM}{AB} = \\dfrac{%s}{%s}$.\n'
            '\\item Kẻ đường cao $AH$ của $\\Delta ABC$ cắt $MN$ tại $K$. Vì $MN // BC$ và $AH \\perp BC$ nên $AK \\perp MN$, hay $AK$ là đường cao của $\\Delta AMN$.\\\n'
            'Xét $\\Delta AHM$ có $MK // BH$ nên $\\Delta AMK \\backsim \\Delta ABH$, suy ra $\\dfrac{AK}{AH} = \\dfrac{AM}{AB} = \\dfrac{%s}{%s}$.\\\n'
            'Ta có: $\\dfrac{S_{\\Delta AMN}}{S_{\\Delta ABC}} = \\dfrac{\\dfrac{1}{2}AK \\cdot MN}{\\dfrac{1}{2}AH \\cdot BC} = \\dfrac{AK}{AH} \\cdot \\dfrac{MN}{BC} = \\dfrac{%s}{%s} \\cdot \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.\\\n'
            'Suy ra $S_{\\Delta AMN} = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm}^2\\text{)}$.\\\n'
            'Diện tích tứ giác $BMNC$ là: $S_{BMNC} = S_{\\Delta ABC} - S_{\\Delta AMN} = %s - %s = %s\\text{ (cm}^2\\text{)}$.\n'
            '\\end{enumEX}'
            % (bm_num, q, bm_num, q, p, q, p, q,
               p, q, p, q, p, q, p**2, q**2,
               p**2, q**2, S_ABC, S_AMN,
               S_ABC, S_AMN, S_BMNC)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
