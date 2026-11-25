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

def bt_dang11_p4_b3_c5_ds8(self):
    # Dạng 11: Phân tích biến động dân số theo nhóm tuổi qua hai biểu đồ hình quạt tròn (Bài toán già hóa dân số)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        dan05 = Decimal('82.4')
        dan25 = Decimal('101.5')
        p65_05 = Decimal('6.5')
        p65_25 = Decimal('10.0')
        
        so65_05 = (dan05 * p65_05 / Decimal(100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        so65_25 = (dan25 * p65_25 / Decimal(100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.6) arc (0:99:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!30] (0,0) -- (99:1.6) arc (99:336.6:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (336.6:1.6) arc (336.6:360:1.6) -- cycle;\n' +
            '\\node at (49:1.0) {$27,5\\%%$};\n' +
            '\\node at (218:0.95) {$66,0\\%%$};\n' +
            '\\node at (348:1.25) {$6,5\\%%$};\n' +
            '\\node[below] at (0,-1.8) {Năm $2005$ ($82,4$ triệu người)};\n' +
            '\\begin{scope}[xshift=4.6cm]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.6) arc (0:79.2:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!30] (0,0) -- (79.2:1.6) arc (79.2:324:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (324:1.6) arc (324:360:1.6) -- cycle;\n' +
            '\\node at (39:1.0) {$22,0\\%%$};\n' +
            '\\node at (201:0.95) {$68,0\\%%$};\n' +
            '\\node at (342:1.2) {$10,0\\%%$};\n' +
            '\\node[below] at (0,-1.8) {Năm $2025$ ($101,5$ triệu người)};\n' +
            '\\end{scope}\n' +
            '\\draw[line width=1pt, fill=black!10] (6.8,0.8) rectangle (7.2,1.1) node[right, yshift=-4pt] {$0 - 14$ tuổi};\n' +
            '\\draw[line width=1pt, fill=black!30] (6.8,0.0) rectangle (7.2,0.3) node[right, yshift=-4pt] {$15 - 64$ tuổi};\n' +
            '\\draw[line width=1pt, fill=white] (6.8,-0.8) rectangle (7.2,-0.5) node[right, yshift=-4pt] {Từ $65$ tuổi trở lên};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Hai biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu dân số theo nhóm tuổi của một quốc gia vào năm $2005$ và năm $2025$:\n' +
                         tikz_code + '\n' +
                         'a) Tính số lượng người thuộc nhóm từ $65$ tuổi trở lên của quốc gia đó vào năm $2005$ và năm $2025$ (làm tròn đến chữ số thập phân thứ hai theo đơn vị triệu người).\\\n' +
                         'b) Theo quy ước của Liên Hợp Quốc, một quốc gia bước vào giai đoạn "dân số già" khi tỉ lệ người từ $65$ tuổi trở lên đạt từ $10\\%%$ trở lên. Dựa vào biểu đồ, hãy nhận xét xu hướng biến đổi cơ cấu dân số của quốc gia này sau $20$ năm.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item - Năm $2005$, số người thuộc nhóm từ $65$ tuổi trở lên là:\\\\' +
                   '$$82,4 \\cdot 6,5\\%% = 5,356 \\approx %s \\text{ (triệu người)}.$$\\\\' +
                   '- Năm $2025$, số người thuộc nhóm từ $65$ tuổi trở lên là:\\\\' +
                   '$$101,5 \\cdot 10,0\\%% = %s \\text{ (triệu người)}.$$\n' +
                   '\\item Nhận xét: Sau $20$ năm (từ $2005$ đến $2025$), tỉ lệ trẻ em ($0 - 14$ tuổi) giảm từ $27,5\\%%$ xuống còn $22,0\\%%$, trong khi tỉ lệ người cao tuổi (từ $65$ tuổi trở lên) tăng mạnh từ $6,5\\%%$ lên $10,0\\%%$ (số lượng tăng gần gấp đôi). Như vậy, cơ cấu dân số của quốc gia này đang chuyển dịch theo xu hướng già hóa nhanh và đã chính thức bước vào giai đoạn "dân số già" vào năm $2025$.\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(so65_05), fmt_vn(so65_25))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
