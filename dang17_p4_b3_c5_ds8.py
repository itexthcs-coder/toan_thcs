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

def bt_dang17_p4_b3_c5_ds8(self):
    # Dạng 17: Phân tích biểu đồ đoạn thẳng quãng đường - thời gian của hai phương tiện chuyển động
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Người 1 xuất phát 7h00, vận tốc v1 = 12 km/h -> đến B (36 km) lúc 10h00 (hoặc 14,4 km/h -> 9h30)
        # Chọn v1 = 12 km/h, v2 = 18 km/h, xuất phát 7h00 và 7h30, AB = 36 km -> đẹp tuyệt đối!
        ab = 36
        v1 = 12
        v2 = 18
        # Người 1 đi 36 km hết 3h -> đến B lúc 10h00
        # Người 2 xuất phát 7h30, đi 36 km hết 2h -> đến B lúc 9h30
        # Gặp nhau: 12 * t = 18 * (t - 0,5) => 6t = 9 => t = 1,5h -> lúc 8h30, cách A: 12 * 1,5 = 18 km
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.8,0) node[below] {Thời điểm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.0) node[left] {Quãng đường ($\\text{km}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (A1) at (0,0); \\coordinate (B1) at (6.0,3.6);\n' +
            '\\coordinate (A2) at (1.0,0); \\coordinate (B2) at (5.0,3.6);\n' +
            '\\draw[line width=1pt] (A1)--(B1);\n' +
            '\\draw[line width=1pt, dashed] (A2)--(B2);\n' +
            '\\fill (A1) circle (1pt) (B1) circle (1pt) (A2) circle (1pt) (B2) circle (1pt) (3.0,1.8) circle (1pt);\n' +
            '\\node[below] at (0,0) {$7\\text{h}00$};\n' +
            '\\node[below] at (1.0,0) {$7\\text{h}30$};\n' +
            '\\node[below] at (3.0,0) {$8\\text{h}30$};\n' +
            '\\node[below] at (5.0,0) {$9\\text{h}30$};\n' +
            '\\node[below] at (6.0,0) {$10\\text{h}00$};\n' +
            '\\node[left] at (0,3.6) {$36$};\n' +
            '\\draw[line width=1pt] (6.8,2.8) -- (7.5,2.8) node[right] {Người thứ nhất};\n' +
            '\\draw[line width=1pt, dashed] (6.8,2.1) -- (7.5,2.1) node[right] {Người thứ hai};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Trên cùng một hệ trục tọa độ biểu diễn đồ thị quãng đường – thời gian của hai người đi xe đạp từ địa điểm $A$ đến địa điểm $B$ cách nhau $36\\text{ km}$: người thứ nhất xuất phát lúc $7\\text{h}00$, đi đều và đến $B$ lúc $10\\text{h}00$; người thứ hai xuất phát lúc $7\\text{h}30$, đi đều với vận tốc $18\\text{ km/h}$ không nghỉ cho đến khi tới $B$:\n' +
                         tikz_code + '\n' +
                         'a) Xác định thời điểm người thứ hai đến $B$ và tính vận tốc của người thứ nhất.\\\n' +
                         'b) Dựa vào đồ thị đoạn thẳng của hai người, xác định thời điểm hai đường biểu diễn cắt nhau (tức là thời điểm người thứ hai đuổi kịp người thứ nhất) và vị trí gặp nhau cách $A$ bao nhiêu ki-lô-mét.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Thời gian người thứ hai đi hết quãng đường $AB$ dài $36\\text{ km}$ là: $\\dfrac{36}{18} = 2$ (giờ).\\\\' +
                   'Vì xuất phát lúc $7\\text{h}30$ nên người thứ hai đến $B$ lúc: $7\\text{h}30 + 2\\text{ giờ} = 9\\text{h}30$.\\\\' +
                   'Thời gian người thứ nhất đi hết quãng đường $AB$ là: $10\\text{h}00 - 7\\text{h}00 = 3$ (giờ).\\\\' +
                   'Vận tốc của người thứ nhất là: $\\dfrac{36}{3} = 12\\text{ (km/h)}$.\n' +
                   '\\item Gọi $t$ (giờ) là thời gian di chuyển của người thứ nhất tính từ lúc $7\\text{h}00$ đến khi hai người gặp nhau ($t > 0,5$).\\\\' +
                   'Khi đó thời gian di chuyển của người thứ hai là $t - 0,5$ (giờ). Tại thời điểm gặp nhau, quãng đường hai người đi được bằng nhau nên:\\\\' +
                   '$$12t = 18(t - 0,5) \\Leftrightarrow 12t = 18t - 9 \\Leftrightarrow 6t = 9 \\Leftrightarrow t = 1,5 \\text{ (giờ)}.$$\\\\' +
                   'Vậy hai đường biểu diễn cắt nhau lúc $7\\text{h}00 + 1\\text{ giờ } 30\\text{ phút} = 8\\text{h}30$ và vị trí gặp nhau cách $A$ là: $12 \\cdot 1,5 = 18\\text{ (km)}$.\n' +
                   '\\end{enumEX}'
                   )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
