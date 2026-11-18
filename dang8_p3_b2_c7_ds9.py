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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang8_p3_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m1 = random.choice([4, 5])
        m2 = 9 - m1
        kq_dec = (Decimal(m1 * 100) / Decimal(15)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq_dec).replace('.', ',')

        hinh_dt = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[right] {Số bàn thắng};\n'
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[above] {Số trận};\n'
            '\\foreach \\y/\\lbl in {1/2, 2/4, 3/6} {\n'
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.5,\\y);\n'
            '    \\node[left] at (0,\\y) {$\\lbl$};\n'
            '}\n'
            '\\foreach \\x/\\lbl in {1/0, 2/1, 3/2, 4/3, 5/4} {\n'
            '    \\node[below] at (\\x,0) {$\\lbl$};\n'
            '}\n'
            '\\draw[line width=1pt] (1,1.0) -- (2,%s) -- (3,%s) -- (4,1.5) -- (5,0.5);\n'
            '\\fill (1,1.0) circle (1pt) node[above] {$2$};\n'
            '\\fill (2,%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (3,%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (4,1.5) circle (1pt) node[above] {$3$};\n'
            '\\fill (5,0.5) circle (1pt) node[above] {$1$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (m1/2, m2/2, m1/2, m1, m2/2, m2)

        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây ghi lại số bàn thắng trong mỗi trận đấu của một giải bóng đá phong trào:%sTần số tương đối của các trận đấu có đúng $1$ bàn thắng bằng bao nhiêu phần trăm (làm tròn kết quả đến hàng phần mười)?' % (hinh_dt))

        loigiai = ('Tổng số trận đấu của giải là $n = 2 + %s + %s + 3 + 1 = 15$ (trận).\\\\ Số trận có đúng $1$ bàn thắng là $m = %s$. Tần số tương đối tương ứng là: $$f = \\frac{%s}{15} \\cdot 100\\%% \\approx %s\\%%.$$' % (m1, m2, m1, m1, kq_str))
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
