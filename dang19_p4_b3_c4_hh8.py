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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang19_p4_b3_c4_hh8(self):
    # Dạng 19: Quy hoạch phân lô đất nông nghiệp tại ngã ba đường (Thực tế)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (40, 60, 50, 20, 30, 900, 360, 540),
            (30, 45, 50, 20, 30, 750, 300, 450),
            (60, 90, 100, 40, 60, 1500, 600, 900)
        ]
        ab, ac, bc, db, dc, s_tong, s_abd, s_acd = random.choice(bo_so)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.5,3.2);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.6,0);\n'
            '\\coordinate (D) at (1.84,0);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một thửa đất nông nghiệp hình tam giác $ABC$ có hai cạnh tiếp giáp đường lớn là $AB = %s\\text{ m}$, $AC = %s\\text{ m}$ và cạnh còn lại $BC = %s\\text{ m}$. Chủ đất mở một con mương tưới tiêu dọc theo tia phân giác $AD$ của góc $BAC$ ($D \\in BC$) để chia thửa đất thành hai mảnh $ABD$ trồng rau sạch và $ACD$ trồng cây ăn quả.\\\\\n'
            'a) Tính độ dài hai đoạn bờ mương chia trên cạnh $BC$ là $DB$ và $DC$.\\\\\n'
            'b) Biết tổng diện tích cả thửa đất $ABC$ là $%s\\text{ m}^2$. Tính diện tích từng mảnh đất $ABD$ và $ACD$.\n%s'
            % (ab, ac, bc, s_tong, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Trong tam giác $ABC$ có $AD$ là đường phân giác của góc $BAC$ ($D \\in BC$) nên $\\frac{DB}{DC} = \\frac{AB}{AC} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $\\frac{DB}{BC} = \\frac{%s}{%s + %s} \\Rightarrow DB = \\frac{%s}{%s} \\cdot %s = %s\\text{ m}$, và $DC = %s - %s = %s\\text{ m}$. \n'
            '\\item Hai tam giác $ABD$ và $ACD$ có chung đường cao hạ từ $A$ xuống $BC$ nên $\\frac{S_{\\Delta ABD}}{S_{\\Delta ACD}} = \\frac{DB}{DC} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $S_{\\Delta ABD} = \\frac{%s}{%s + %s} \\cdot %s = %s\\text{ m}^2$, và $S_{\\Delta ACD} = %s - %s = %s\\text{ m}^2$. \n'
            '\\end{enumEX} \n'
            % (ab, ac, ab, ab, ac, ab, ab + ac, bc, db, bc, db, dc, db, dc, db, db, dc, s_tong, s_abd, s_tong, s_abd, s_acd)
        )

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
