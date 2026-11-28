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


def bt_dang13_p4_b2_c8_ds8(self):
    # Dạng 13: Bài toán phân chia nhóm và chọn đại diện
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        sub = random.choice(['it_nhat_1_nu', '1_nam_1_nu'])
        all_members = [('An', 'nam'), ('Bình', 'nam'), ('Cường', 'nam'), ('Dũng', 'nam'), ('Hoa', 'nu'), ('Lan', 'nu')]

        all_pairs = []
        fav_pairs = []
        for i in range(6):
            for j in range(i + 1, 6):
                p1, p2 = all_members[i], all_members[j]
                all_pairs.append((p1[0], p2[0]))
                if sub == 'it_nhat_1_nu':
                    if p1[1] == 'nu' or p2[1] == 'nu':
                        fav_pairs.append((p1[0], p2[0]))
                else:
                    if p1[1] != p2[1]:
                        fav_pairs.append((p1[0], p2[0]))

        tong_kq = len(all_pairs)
        so_tl = len(fav_pairs)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        all_str = '; '.join(['(%s, %s)' % p for p in all_pairs])
        fav_str = '; '.join(['(%s, %s)' % p for p in fav_pairs])
        dk_hoi = 'trong $2$ bạn được chọn có ít nhất một bạn nữ' if sub == 'it_nhat_1_nu' else 'trong $2$ bạn được chọn có đúng một bạn nam và một bạn nữ'

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (4.2,1.3);\n'
            '\\node at (2.1,0.85) {$4$ bạn nam};\n'
            '\\node at (2.1,0.35) {An, Bình, Cường, Dũng};\n'
            '\\draw[line width=1pt] (4.8,0) rectangle (7.8,1.3);\n'
            '\\node at (6.3,0.85) {$2$ bạn nữ};\n'
            '\\node at (6.3,0.35) {Hoa, Lan};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một tổ học sinh có $4$ bạn nam là An, Bình, Cường, Dũng và $2$ bạn nữ là Hoa, Lan. '
            'Giáo viên chủ nhiệm chọn ngẫu nhiên $2$ bạn trong tổ đi trực nhật. Tính xác suất để %s.%s'
        ) % (dk_hoi, tikz_img)

        loigiai = (
            'Liệt kê tất cả các cặp $2$ bạn có thể được chọn từ $6$ bạn trong tổ:\\\\\n'
            '%s.\\\\\n'
            'Có tất cả $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Các cặp thuận lợi cho biến cố ``%s\'\' là:\\\\\n'
            '%s.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{%s} = %s$.'
        ) % (all_str, tong_kq, dk_hoi, fav_str, so_tl, so_tl, tong_kq, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
