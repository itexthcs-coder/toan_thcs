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


def bt_dang16_p4_b2_c8_ds8(self):
    # Dạng 16: Xác suất kết hợp phương trình nghiệm nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        box1 = [1, 2, 3, 4]
        box2 = [2, 4, 6, 8]
        rhs = random.choice([8, 10, 12])
        fav_pairs = []
        for a in box1:
            for b in box2:
                if 2 * a + b == rhs:
                    fav_pairs.append((a, b))

        tong_kq = len(box1) * len(box2)
        so_tl = len(fav_pairs)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        fav_str = '; '.join(['(%s; %s)' % p for p in fav_pairs])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (3.2,1.3);\n'
            '\\node at (1.6,0.85) {Hộp I};\n'
            '\\node at (1.6,0.35) {Thẻ: $1; 2; 3; 4$};\n'
            '\\draw[line width=1pt] (4.2,0) rectangle (7.4,1.3);\n'
            '\\node at (5.8,0.85) {Hộp II};\n'
            '\\node at (5.8,0.35) {Thẻ: $2; 4; 6; 8$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hai hộp thẻ: Hộp I chứa $4$ thẻ ghi các số $1; 2; 3; 4$; Hộp II chứa $4$ thẻ ghi các số $2; 4; 6; 8$ (các thẻ trong mỗi hộp giống hệt nhau). '
            'Rút ngẫu nhiên từ mỗi hộp một tấm thẻ. Gọi $a$ là số trên thẻ rút từ Hộp I, $b$ là số trên thẻ rút từ Hộp II. '
            'Tính xác suất để cặp số $(a; b)$ thỏa mãn đẳng thức $2a + b = %s$.%s'
        ) % (rhs, tikz_img)

        loigiai = (
            'Hộp I có $4$ thẻ, Hộp II có $4$ thẻ. Khi rút ngẫu nhiên từ mỗi hộp một tấm thẻ, mỗi kết quả có thể là một cặp số $(a; b)$ với $a \\in \\{1; 2; 3; 4\\}$ và $b \\in \\{2; 4; 6; 8\\}$.\\\\\n'
            'Tổng số kết quả có thể là $4 \\cdot 4 = 16$ cặp số và các kết quả này là đồng khả năng.\\\\\n'
            'Ta tìm các cặp số $(a; b)$ thỏa mãn $2a + b = %s$:\\\\\n'
            '- Thay lần lượt $a \\in \\{1; 2; 3; 4\\}$ vào hệ thức $b = %s - 2a$, ta được các cặp số thỏa mãn điều kiện đề bài là: $%s$.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi cho biến cố $2a + b = %s$.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{16} = %s$.'
        ) % (rhs, rhs, fav_str, so_tl, rhs, so_tl, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
