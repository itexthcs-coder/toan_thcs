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

def bt_dang14_p3_b3_c5_ds8(self):
    # Dạng 14: Tính tiền điện bậc thang dựa trên biểu đồ cột tiêu thụ điện năng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        e4 = random.randint(250, 290)
        diff_e = random.choice([40, 50, 60, 70])
        e5 = e4 + diff_e
        gia_vuot = Decimal('2.5') # nghìn đồng/kWh
        tien_them = int(Decimal(diff_e) * gia_vuot)
        kq_str = str(tien_them)
        
        y4 = round(e4 / 100.0, 2)
        y5 = round(e5 / 100.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Tháng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Điện năng ($\\text{kWh}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.9,0) rectangle (1.9,%s); \\node[above] at (1.4,%s) {$%s$}; \\node[below] at (1.4,0) {Tháng $4$};\n' % (y4, y4, e4) +
            '\\draw[line width=1pt, fill=black!40] (2.7,0) rectangle (3.7,%s); \\node[above] at (3.2,%s) {$%s$}; \\node[below] at (3.2,0) {Tháng $5$};\n' % (y5, y5, e5) +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột dưới đây biểu diễn lượng điện tiêu thụ (đơn vị: $\\text{kWh}$) của một hộ gia đình trong tháng $4$ và tháng $5$:\n' +
                         tikz_code + '\n' +
                         'Giả sử đơn giá điện sinh hoạt tính theo mức tiêu thụ như sau: $200\\text{ kWh}$ đầu tiên giá $2\\,000$ đồng/$\\text{kWh}$, phần vượt trên $200\\text{ kWh}$ tính giá $2\\,500$ đồng/$\\text{kWh}$. Hỏi tiền điện tháng $5$ của gia đình đó nhiều hơn tháng $4$ bao nhiêu nghìn đồng?')
        
        loigiai = ('Cả hai tháng gia đình đều sử dụng vượt mức $200\\text{ kWh}$ ($%s > 200$ và $%s > 200$).\\\\' +
                   'Lượng điện năng tháng $5$ tiêu thụ nhiều hơn tháng $4$ là: $%s - %s = %s\\text{ (kWh)}$.\\\\' +
                   'Vì phần chênh lệch này đều nằm ở bậc giá $2\\,500$ đồng/$\\text{kWh}$ ($2,5$ nghìn đồng/$\\text{kWh}$) nên tiền điện tháng $5$ nhiều hơn tháng $4$ là:\\\\' +
                   '$$%s \\cdot 2,5 = %s \\text{ (nghìn đồng)}.$$'
                   ) % (e4, e5, e5, e4, diff_e, diff_e, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
