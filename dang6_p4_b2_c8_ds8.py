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


def bt_dang6_p4_b2_c8_ds8(self):
    # Dạng 6: Xác suất dựa trên tỉ số diện tích hình học (trò chơi ném phi tiêu)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([30, 40, 50, 60])
        r = random.choice([8, 10, 12, 15])
        s_vuong = a * a
        pi_dec = Decimal('3.14')
        r_dec = Decimal(str(r))
        s_vuong_dec = Decimal(str(s_vuong))
        s_tron_dec = pi_dec * r_dec * r_dec
        xs_dec = (s_tron_dec / s_vuong_dec).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        s_tron_str = str(s_tron_dec).replace('.', ',')
        xs_str = str(xs_dec).replace('.', ',')

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (3,0);\n'
            '\\coordinate (C) at (3,3);\n'
            '\\coordinate (D) at (0,3);\n'
            '\\coordinate (O) at (1.5,1.5);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt] (O) circle (0.75);\n'
            '\\draw[line width=1pt, dashed] (O) -- (2.25,1.5) node[above, midway] {$R$};\n'
            '\\fill (O) circle (1pt) node[left] {$O$};\n'
            '\\draw[<->, line width=1pt] (0,-0.35) -- (3,-0.35) node[below, midway] {$%s\\text{ cm}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % a

        noidungcauhoi = (
            'Một bảng phi tiêu hình vuông có cạnh dài $%s\\text{ cm}$. Ở chính giữa bảng người ta vẽ một hình tròn tâm $O$ bán kính $R = %s\\text{ cm}$ làm vùng tính điểm thưởng. '
            'Giả sử một người ném phi tiêu luôn trúng vào bảng và khả năng phi tiêu cắm vào mọi điểm trên bảng là như nhau (lấy $\\pi \\approx 3,14$). '
            'Tính xác suất để mũi phi tiêu cắm vào vùng tính điểm thưởng (kết quả làm tròn đến hàng phần trăm).%s'
        ) % (a, r, tikz_img)

        loigiai = (
            'Diện tích của bảng phi tiêu hình vuông là: $S_{\\text{vuông}} = %s^2 = %s\\text{ (cm}^2\\text{)}$.\\\\\n'
            'Diện tích của vùng tính điểm thưởng hình tròn là: $S_{\\text{tròn}} = \\pi \\cdot R^2 \\approx 3,14 \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}$.\\\\\n'
            'Vì khả năng phi tiêu cắm vào mọi điểm trên bảng là như nhau nên xác suất để mũi phi tiêu cắm vào vùng tính điểm thưởng bằng tỉ số giữa diện tích hình tròn và diện tích hình vuông:\\\\\n'
            '$P = \\frac{S_{\\text{tròn}}}{S_{\\text{vuông}}} \\approx \\frac{%s}{%s} \\approx %s$.\\\\\n'
            'Vậy xác suất để mũi phi tiêu cắm vào vùng tính điểm thưởng khoảng $%s$.'
        ) % (
            a, s_vuong,
            r, s_tron_str,
            s_tron_str, s_vuong, xs_str,
            xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
