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


def bt_dang20_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        AB = random.choice([20, 24, 30, 36, 40])
        R = AB // 2
        val_CH = (R * math.sqrt(3)) / 2.0
        kq_CH = str(Decimal(str(val_CH)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-2.4,0);\n'
            '\\coordinate (B) at (2.4,0);\n'
            '\\coordinate (C) at (120:2.4);\n'
            '\\coordinate (D) at (30:2.4);\n'
            '\\coordinate (K) at (intersection of A--D and B--C);\n'
            '\\coordinate (H) at ($(A)!(C)!(B)$);\n'
            '\\draw[line width=1pt] (2.4,0) arc (0:180:2.4cm) -- cycle;\n'
            '\\draw[line width=1pt] (A)--(D) (B)--(C);\n'
            '\\draw[line width=1pt, dashed] (C)--(H) (O)--(C);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\fill (K) circle (1pt) node[above] {$K$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một cây cầu đi bộ có vòm đỡ phía trên dạng nửa đường tròn tâm $O$, đường kính $AB = %s\\text{ m}$ nằm ngang mặt cầu. Để tăng độ cứng cho vòm, kỹ sư bố trí hai điểm neo $C$ và $D$ trên vòm (theo thứ tự $A, C, D, B$) sao cho $\\text{sđ}\\overparen{AC} = 60^\\circ$ và $\\text{sđ}\\overparen{BD} = 30^\\circ$. Hai thanh giằng thẳng nối $AD$ và $BC$ cắt nhau tại điểm $K$ như hình vẽ.\\\\'
            'a) Tính số đo các góc nội tiếp $\\widehat{ABC}$ và $\\widehat{BAD}$.\\\\'
            'b) Tính góc nhọn tạo bởi hai thanh giằng $AD$ và $BC$ tại điểm giao $K$.\\\\'
            'c) Tính chiều cao từ mặt cầu $AB$ lên tới điểm neo $C$ (làm tròn kết quả đến hàng phần trăm của mét).\n%s'
            % (AB, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong nửa đường tròn $(O)$ đường kính $AB$, góc nội tiếp $\\widehat{ABC}$ chắn cung $AC$ nên $\\widehat{ABC} = \\dfrac{1}{2}\\text{sđ}\\overparen{AC} = \\dfrac{60^\\circ}{2} = 30^\\circ$.\\\\'
            'Góc nội tiếp $\\widehat{BAD}$ chắn cung $BD$ nên $\\widehat{BAD} = \\dfrac{1}{2}\\text{sđ}\\overparen{BD} = \\dfrac{30^\\circ}{2} = 15^\\circ$.\n'
            '\\item Xét $\\triangle KAB$, góc $\\widehat{CKA}$ (hoặc $\\widehat{BKD}$) là góc ngoài tại đỉnh $K$ nên $\\widehat{CKA} = \\widehat{KAB} + \\widehat{KBA} = 15^\\circ + 30^\\circ = 45^\\circ$. Vậy góc nhọn tạo bởi hai thanh giằng $AD$ và $BC$ tại $K$ bằng $45^\\circ$.\n'
            '\\item Bán kính của vòm cầu là $R = \\dfrac{AB}{2} = %s\\text{ m}$. Kẻ $CH \\perp AB$ tại $H$. Vì $\\text{sđ}\\overparen{AC} = 60^\\circ$ nên góc ở tâm $\\widehat{AOC} = 60^\\circ$.\\\\'
            'Xét $\\triangle OCH$ vuông tại $H$ có $OC = %s\\text{ m}$ và $\\widehat{COH} = 60^\\circ$, ta có $CH = OC \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} \\approx %s\\text{ m}$.\n'
            '\\end{enumEX}'
            % (R, R, R, kq_CH)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
