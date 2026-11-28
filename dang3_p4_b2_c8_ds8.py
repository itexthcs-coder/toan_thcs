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


def bt_dang3_p4_b2_c8_ds8(self):
    # Dạng 3: Xác suất kết hợp điều kiện tỉ số phần trăm trong kinh doanh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            tong = random.choice([80, 100, 120, 140, 150, 160, 200])
            pt = random.choice([30, 35, 40, 45, 50])
            if (tong * pt) % 100 == 0:
                tam_trung = (tong * pt) // 100
                con_lai = tong - tam_trung
                chenh = random.choice([6, 8, 10, 12, 14, 16, 18, 20])
                if con_lai > chenh and (con_lai - chenh) % 2 == 0:
                    cao_cap = (con_lai - chenh) // 2
                    pho_thong = cao_cap + chenh
                    if cao_cap > 0:
                        break

        f = frac(cao_cap, tong)
        if f.denominator == 1:
            xs_str = str(f.numerator)
        else:
            xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (7.5,1.1);\n'
            '\\draw[line width=1pt] (3.2,0) -- (3.2,1.1) (5.6,0) -- (5.6,1.1);\n'
            '\\node at (1.6,0.55) {Tầm trung ($%s\\%%$)};\n'
            '\\node at (4.4,0.55) {Phổ thông};\n'
            '\\node at (6.55,0.55) {Cao cấp};\n'
            '\\draw[<->, line width=1pt] (0,-0.35) -- (7.5,-0.35) node[below, midway] {Tổng cộng: $%s$ chiếc điện thoại};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (pt, tong)

        noidungcauhoi = (
            'Một cửa hàng điện máy nhập về một lô hàng gồm $%s$ chiếc điện thoại thuộc ba dòng: phổ thông, tầm trung và cao cấp. '
            'Số điện thoại tầm trung chiếm $%s\\%%$ tổng số máy, số điện thoại cao cấp ít hơn số điện thoại phổ thông là $%s$ chiếc. '
            'Chọn ngẫu nhiên một chiếc điện thoại trong lô để kiểm tra chất lượng. '
            'Tính xác suất để chiếc điện thoại được chọn thuộc dòng cao cấp.%s'
        ) % (tong, pt, chenh, tikz_img)

        loigiai = (
            'Số chiếc điện thoại thuộc dòng tầm trung là: $%s \\cdot %s\\%% = %s$ (chiếc).\\\\\n'
            'Tổng số chiếc điện thoại thuộc hai dòng phổ thông và cao cấp là: $%s - %s = %s$ (chiếc).\\\\\n'
            'Gọi số chiếc điện thoại dòng cao cấp là $x$ (chiếc, điều kiện: $x \\in \\mathbb{N}^*$, $x < %s$).\\\\\n'
            'Khi đó, số chiếc điện thoại dòng phổ thông là $x + %s$ (chiếc).\\\\\n'
            'Theo đề bài, ta có phương trình: $x + (x + %s) = %s$\\\\\n'
            '$2x + %s = %s$\\\\\n'
            '$2x = %s$\\\\\n'
            '$x = %s$ (thỏa mãn điều kiện).\\\\\n'
            'Vậy có $%s$ chiếc điện thoại thuộc dòng cao cấp.\\\\\n'
            'Khi chọn ngẫu nhiên một chiếc điện thoại trong lô gồm $%s$ chiếc thì có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Do có $%s$ kết quả thuận lợi nên xác suất để chiếc điện thoại được chọn thuộc dòng cao cấp là: $P = \\frac{%s}{%s} = %s$.'
        ) % (
            tong, pt, tam_trung,
            tong, tam_trung, con_lai,
            con_lai, chenh,
            chenh, con_lai, chenh, con_lai, con_lai - chenh, cao_cap,
            cao_cap, tong, tong,
            cao_cap, cao_cap, tong, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
