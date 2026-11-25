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

def bt_dang16_p3_b3_c5_ds8(self):
    # Dạng 16: Bài toán chuyển đổi đơn vị năng lượng KTOE trên biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p_than, p_dau, p_khi, p_tt = 44, 24, 18, 14
        khi_ktoe = random.choice([8100, 9000, 9900, 10800])
        tong_ktoe = int(khi_ktoe * 100 // p_khi)
        than_ktoe = int(tong_ktoe * p_than // 100)
        than_nghin = Decimal(than_ktoe) / Decimal(1000)
        kq_str = str(than_nghin).rstrip('0').rstrip('.').replace('.', ',')
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:158.4:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (158.4:1.9) arc (158.4:244.8:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (244.8:1.9) arc (244.8:309.6:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (309.6:1.9) arc (309.6:360:1.9) -- cycle;\n' +
            '\\node at (79:1.15) {$44\\%%$};\n' +
            '\\node at (201:1.2) {$24\\%%$};\n' +
            '\\node at (277:1.25) {$18\\%%$};\n' +
            '\\node at (335:1.35) {$14\\%%$};\n' +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Than};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Dầu thô};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Khí tự nhiên};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Năng lượng tái tạo};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu nguồn cung cấp năng lượng sơ cấp của một quốc gia năm $2025$:\n' +
                         tikz_code + '\n' +
                         'Biết lượng năng lượng từ Khí tự nhiên đạt $%s\\text{ KTOE}$. Hỏi lượng năng lượng từ Than của quốc gia đó đạt bao nhiêu nghìn $\\text{KTOE}$?' % khi_ktoe)
        
        loigiai = ('Vì Khí tự nhiên chiếm $18\\%%$ tổng nguồn cung năng lượng và đạt $%s\\text{ KTOE}$ nên tổng nguồn cung năng lượng của quốc gia đó là:\\\\' +
                   '$$\\dfrac{%s}{18\\%%} = %s \\text{ (KTOE)}.$$\\\\' +
                   'Lượng năng lượng từ Than chiếm $44\\%%$, bằng:\\\\' +
                   '$$%s \\cdot 44\\%% = %s \\text{ (KTOE)} = %s \\text{ (nghìn KTOE)}.$$'
                   ) % (khi_ktoe, khi_ktoe, tong_ktoe, tong_ktoe, than_ktoe, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
