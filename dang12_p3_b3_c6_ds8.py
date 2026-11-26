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
def bt_dang12_p3_b3_c6_ds8(self):
    # Dạng 12: Tìm tổng các giá trị nguyên của biến để hiệu hai phân thức là số nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # H = (2x + a)/(x - k) - (x - b)/(x - k) = (x + a + b)/(x - k) = 1 + (k + a + b)/(x - k)
        # N = k + a + b là số nguyên dương không chính phương để có số ước chẵn (2m ước), tổng x = 2m * k
        bo = [
            (2, 3, 1, 6, 8, 16),    # N = 6 (8 ước) => tổng = 8*2 = 16
            (3, 4, 1, 8, 8, 24),    # N = 8 (8 ước) => tổng = 8*3 = 24
            (1, 3, 2, 6, 8, 8),     # N = 6 (8 ước) => tổng = 8*1 = 8
            (2, 5, 3, 10, 8, 16),   # N = 10 (8 ước) => tổng = 8*2 = 16
            (3, 5, 4, 12, 12, 36)   # N = 12 (12 ước) => tổng = 12*3 = 36
        ]
        k, a, b, N, so_uoc, tong_x = random.choice(bo)
        c_tu = a + b
        
        noidungcauhoi = ('Tính tổng tất cả các giá trị nguyên của $x$ để biểu thức $H = \\dfrac{2x + %s}{x - %s} - \\dfrac{x - %s}{x - %s}$ nhận giá trị nguyên.' % (a, k, b, k))
        
        loigiai = ('Điều kiện xác định: $x \\neq %s$.\\'
                   'Ta có:\\'
                   '$$H = \\dfrac{(2x + %s) - (x - %s)}{x - %s} = \\dfrac{x + %s}{x - %s} = \\dfrac{(x - %s) + %s}{x - %s} = 1 + \\dfrac{%s}{x - %s}.$$\\'
                   'Với $x \\in \\mathbb{Z}$, $H$ nhận giá trị nguyên khi và chỉ khi $x - %s$ là ước nguyên của $%s$.\\'
                   'Vì các ước nguyên của $%s$ luôn chia thành từng cặp đối nhau nên tổng của $%s$ ước nguyên đó bằng $0$.\\'
                   'Do đó tổng tất cả $%s$ giá trị nguyên của $x$ bằng $0 + %s \\cdot %s = %s$.'
                   % (k, a, b, k, c_tu, k, k, N, k, N, k, k, N, N, so_uoc, so_uoc, so_uoc, k, tong_x))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(tong_x)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
