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
def bt_dang8_p3_b3_c6_ds8(self):
    # Dạng 8: Rút gọn biểu thức chứa nhiều dấu ngoặc và hằng đẳng thức hiệu hai bình phương
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Q = 2ax/(x^2 - a^2) - [ 2/(x - a) - ( 2/(x + a) - 2ax/(x^2 - a^2) ) ]
        # Bỏ ngoặc: 2ax/(x^2 - a^2) - 2/(x - a) + 2/(x + a) - 2ax/(x^2 - a^2) = -4a / (x^2 - a^2)
        bo = [
            (4, 6, '-0,8'),   # -16 / (36 - 16) = -16/20 = -0,8
            (3, 5, '-0,75'),  # -12 / (25 - 9) = -12/16 = -0,75 (5 ký tự -> tránh)
            (5, 7, '-0,83'),  # vô hạn -> tránh
            (2, 6, '-0,25'),  # 5 ký tự -> tránh
            (3, 9, '-0,16'),  # vô hạn -> tránh
            (2, 4, '-0,66'),  # vô hạn -> tránh
            (5, 15, '-0,1'),  # -20 / (225 - 25) = -20/200 = -0,1 (4 ký tự!)
            (4, 12, '-0,125'),
            (1, 3, '-0,5'),   # -4 / (9 - 1) = -4/8 = -0,5 (4 ký tự!)
            (3, 7, '-0,3')    # -12 / (49 - 9) = -12/40 = -0,3 (4 ký tự!)
        ]
        bo_chuan = [
            (4, 6, '-0,8', -16, 20),
            (5, 15, '-0,1', -20, 200),
            (1, 3, '-0,5', -4, 8),
            (3, 7, '-0,3', -12, 40)
        ]
        a, x_val, kq_str, tu_so, mau_so = random.choice(bo_chuan)
        a2 = a ** 2
        hai_a = 2 * a
        
        noidungcauhoi = ('Tính giá trị của biểu thức $Q = \\dfrac{%sx}{x^2 - %s} - \\left[ \\dfrac{2}{x - %s} - \\left( \\dfrac{2}{x + %s} - \\dfrac{%sx}{x^2 - %s} \\right) \\right]$ tại $x = %s$.' % (hai_a, a2, a, a, hai_a, a2, x_val))
        
        loigiai = ('Điều kiện xác định: $x \\neq \\pm %s$.\\'
                   'Áp dụng quy tắc dấu ngoặc từ trong ra ngoài:\\'
                   '$$\\begin{aligned}'
                   'Q &= \\dfrac{%sx}{x^2 - %s} - \\left( \\dfrac{2}{x - %s} - \\dfrac{2}{x + %s} + \\dfrac{%sx}{x^2 - %s} \\right) \\\\'
                   '&= \\dfrac{%sx}{x^2 - %s} - \\dfrac{2}{x - %s} + \\dfrac{2}{x + %s} - \\dfrac{%sx}{x^2 - %s} \\\\'
                   '&= \\dfrac{2}{x + %s} - \\dfrac{2}{x - %s} = \\dfrac{2(x - %s) - 2(x + %s)}{x^2 - %s} = \\dfrac{%s}{x^2 - %s}.'
                   '\\end{aligned}$$\\'
                   'Thay $x = %s$ vào biểu thức rút gọn, ta được $Q = \\dfrac{%s}{%s - %s} = \\dfrac{%s}{%s} = %s$.'
                   % (a, hai_a, a2, a, a, hai_a, a2, hai_a, a2, a, a, hai_a, a2, a, a, a, a, a2, tu_so, a2, x_val, tu_so, x_val ** 2, a2, tu_so, mau_so, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
