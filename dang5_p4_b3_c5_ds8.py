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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang5_p4_b3_c5_ds8(self):
    # Dạng 5: Phân tích tốc độ đô thị hóa qua biểu đồ đoạn thẳng có khoảng cách năm không đều
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p90 = Decimal('19.5')
        p00 = Decimal('24.2')
        p10 = Decimal('30.5')
        p20 = Decimal('36.8')
        p25 = Decimal('40.2')
        
        r1 = (p00 - p90) / Decimal(10) # 0.47
        r2 = (p10 - p00) / Decimal(10) # 0.63
        r3 = (p20 - p10) / Decimal(10) # 0.63
        r4 = (p25 - p20) / Decimal(5)  # 0.68
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Năm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Tỉ lệ ($\\%%$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (P1) at (1.0,1.4);\n' +
            '\\coordinate (P2) at (2.1,1.8);\n' +
            '\\coordinate (P3) at (3.2,2.3);\n' +
            '\\coordinate (P4) at (4.3,2.8);\n' +
            '\\coordinate (P5) at (5.4,3.1);\n' +
            '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5);\n' +
            '\\fill (P1) circle (1pt) node[above left] {$19,5$};\n' +
            '\\fill (P2) circle (1pt) node[above left] {$24,2$};\n' +
            '\\fill (P3) circle (1pt) node[above left] {$30,5$};\n' +
            '\\fill (P4) circle (1pt) node[above left] {$36,8$};\n' +
            '\\fill (P5) circle (1pt) node[above] {$40,2$};\n' +
            '\\node[below] at (1.0,0) {$1990$};\n' +
            '\\node[below] at (2.1,0) {$2000$};\n' +
            '\\node[below] at (3.2,0) {$2010$};\n' +
            '\\node[below] at (4.3,0) {$2020$};\n' +
            '\\node[below] at (5.4,0) {$2025$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây ghi lại tỉ lệ dân số thành thị của một quốc gia qua các mốc năm $1990, 2000, 2010, 2020$ và $2025$. Trên trục ngang của biểu đồ, người vẽ đặt năm mốc năm này cách đều nhau mỗi khoảng $2\\text{ cm}$:\n' +
                         tikz_code + '\n' +
                         'a) Tính mức tăng tỉ lệ dân số thành thị trung bình mỗi năm (đơn vị: điểm phần trăm/năm) trong từng giai đoạn: $1990 - 2000$; $2000 - 2010$; $2010 - 2020$ và $2020 - 2025$.\\\n' +
                         'b) Giai đoạn nào có tốc độ tăng tỉ lệ dân số thành thị nhanh nhất? Vì sao trên biểu đồ đã vẽ, đoạn thẳng nối mốc $2020$ đến $2025$ trông thoải (ít dốc) hơn đoạn thẳng nối mốc $2010$ đến $2020$ dù tốc độ tăng trung bình mỗi năm thực tế lại cao hơn?')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Mức tăng tỉ lệ dân số thành thị trung bình mỗi năm trong từng giai đoạn là:\\\\' +
                   '- Giai đoạn $1990 - 2000$ ($10$ năm): $\\dfrac{24,2 - 19,5}{10} = \\dfrac{4,7}{10} = %s$ (điểm phần trăm/năm).\\\\' +
                   '- Giai đoạn $2000 - 2010$ ($10$ năm): $\\dfrac{30,5 - 24,2}{10} = \\dfrac{6,3}{10} = %s$ (điểm phần trăm/năm).\\\\' +
                   '- Giai đoạn $2010 - 2020$ ($10$ năm): $\\dfrac{36,8 - 30,5}{10} = \\dfrac{6,3}{10} = %s$ (điểm phần trăm/năm).\\\\' +
                   '- Giai đoạn $2020 - 2025$ ($5$ năm): $\\dfrac{40,2 - 36,8}{5} = \\dfrac{3,4}{5} = %s$ (điểm phần trăm/năm).\n' +
                   '\\item Giai đoạn $2020 - 2025$ có tốc độ tăng tỉ lệ dân số thành thị trung bình mỗi năm nhanh nhất ($%s$ điểm phần trăm/năm).\\\\' +
                   'Tuy nhiên, trên biểu đồ đoạn thẳng đã vẽ, đoạn nối $2020 - 2025$ trông thoải hơn đoạn $2010 - 2020$ là do trục ngang chia các khoảng cách bằng nhau ($2\\text{ cm}$) trong khi khoảng thời gian thực tế của giai đoạn cuối chỉ là $5$ năm (bằng một nửa giai đoạn $10$ năm trước đó).\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(r1), fmt_vn(r2), fmt_vn(r3), fmt_vn(r4), fmt_vn(r4))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
