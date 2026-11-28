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


def bt_dang5_p4_b2_c8_ds8(self):
    # Dạng 5: Lập số tự nhiên có hai chữ số từ tập hợp cho trước và tính xác suất
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        digits = sorted(random.sample([1, 2, 3, 4, 5, 6, 7], 5))
        div_k = random.choice([3, 4, 5])
        nums = []
        for a in digits:
            for b in digits:
                if a != b:
                    nums.append(10 * a + b)
        fav = [x for x in nums if x % div_k == 0]
        tong_kq = len(nums)
        so_tl = len(fav)
        f = frac(so_tl, tong_kq)
        xs_str = '0' if so_tl == 0 else ('\\frac{%s}{%s}' % (f.numerator, f.denominator))

        digits_str = '; '.join([str(d) for d in digits])
        nums_str = '; '.join([str(x) for x in nums])
        fav_str = '; '.join([str(x) for x in fav]) if fav else '\\emptyset'

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\foreach \\i/\\d in {0/%s, 1.1/%s, 2.2/%s, 3.3/%s, 4.4/%s}{\n'
            '  \\draw[line width=1pt] (\\i,0) circle (0.4);\n'
            '  \\node at (\\i,0) {$\\d$};\n'
            '}\n'
            '\\node at (2.2,-0.75) {Tập chữ số dùng để lập số có hai chữ số khác nhau};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (digits[0], digits[1], digits[2], digits[3], digits[4])

        noidungcauhoi = (
            'Từ các chữ số $%s$, người ta lập tất cả các số tự nhiên có hai chữ số khác nhau và viết mỗi số lên một mảnh giấy giống nhau. '
            'Chọn ngẫu nhiên một mảnh giấy. Tính xác suất để số ghi trên mảnh giấy đó chia hết cho $%s$.%s'
        ) % (digits_str, div_k, tikz_img)

        loigiai = (
            'Từ $5$ chữ số $%s$, các số tự nhiên có hai chữ số khác nhau lập được là:\\\\\n'
            '$%s$.\\\\\n'
            'Có tất cả $5 \\cdot 4 = %s$ số. Vì các mảnh giấy giống nhau nên khi chọn ngẫu nhiên một mảnh giấy thì có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Trong các số trên, các số chia hết cho $%s$ là: $%s$.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi cho biến cố số ghi trên mảnh giấy chia hết cho $%s$.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{%s} = %s$.'
        ) % (
            digits_str, nums_str, tong_kq, tong_kq,
            div_k, fav_str, so_tl, div_k,
            so_tl, tong_kq, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
