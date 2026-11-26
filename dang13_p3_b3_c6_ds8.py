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
def bt_dang13_p3_b3_c6_ds8(self):
    # Dạng 13: Biến đổi phân thức bậc hai trên tử và mẫu có dạng bình phương hoàn chỉnh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # S = (x^2 - 2ax + a^2)/(x^2 - a^2) + (x + a)/(a - x) = (x - a)/(x + a) - (x + a)/(x - a) = -4ax / (x^2 - a^2)
        bo = [
            (2, 6, '-1,5', -48, 32),   # -8*6 / (36 - 4) = -48/32 = -1,5
            (1, 3, '-1,5', -12, 8),    # -4*3 / (9 - 1) = -12/8 = -1,5
            (3, 5, '-3,75', -60, 16),  # 5 ký tự -> tránh
            (2, 10, '-0,83', -80, 96), # vô hạn -> tránh
            (4, 12, '-1,5', -192, 128),# -16*12 / (144 - 16) = -192/128 = -1,5
            (3, 9, '-1,5', -108, 72)   # -12*9 / (81 - 9) = -108/72 = -1,5
        ]
        bo_chuan = [
            (2, 6, '-1,5', -48, 32),
            (1, 3, '-1,5', -12, 8),
            (4, 12, '-1,5', -192, 128),
            (3, 9, '-1,5', -108, 72)
        ]
        a, x_val, kq_str, tu_so, mau_so = random.choice(bo_chuan)
        hai_a = 2 * a
        a2 = a ** 2
        bon_a = 4 * a
        
        noidungcauhoi = ('Tính giá trị của biểu thức $S = \\dfrac{x^2 - %sx + %s}{x^2 - %s} + \\dfrac{x + %s}{%s - x}$ tại $x = %s$.' % (hai_a, a2, a2, a, a, x_val))
        
        loigiai = ('Điều kiện xác định: $x \\neq \\pm %s$.\\'
                   'Rút gọn phân thức thứ nhất và đổi dấu phân thức thứ hai, ta có:\\'
                   '$$\\begin{aligned}'
                   'S &= \\dfrac{(x - %s)^2}{(x - %s)(x + %s)} - \\dfrac{x + %s}{x - %s} = \\dfrac{x - %s}{x + %s} - \\dfrac{x + %s}{x - %s} \\\\'
                   '&= \\dfrac{(x - %s)^2 - (x + %s)^2}{x^2 - %s} = \\dfrac{-%sx}{x^2 - %s}.'
                   '\\end{aligned}$$\\'
                   'Thay $x = %s$ vào biểu thức rút gọn, ta được $S = \\dfrac{-%s \\cdot %s}{%s - %s} = \\dfrac{%s}{%s} = %s$.'
                   % (a, a, a, a, a, a, a, a, a, a, a, a, a2, bon_a, a2, x_val, bon_a, x_val, x_val ** 2, a2, tu_so, mau_so, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
