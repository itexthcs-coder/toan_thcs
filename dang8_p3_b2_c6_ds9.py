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

def bt_dang8_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            p = random.choice([3, 5, 7, 9])
            q = randint(2, 5)
            if p != 2 and q != 1:
                break
                
        a2 = randint(2, 5)
        a1 = a2 + p - 2*q
        rhs = a1 + a2 + p*q
        
        x_neg = Rational(-p, 2)
        number = Decimal(str(float(x_neg)))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        
        dau_a1 = '+' if a1 >= 0 else '-'
        term1 = '\\frac{x %s %s}{x - 1}' % (dau_a1, abs(a1))
        str_a1 = '+ %s' % a1 if a1 >= 0 else '- %s' % (-a1)
        str_a1_1 = '+ %s' % (a1 + 1) if a1 + 1 >= 0 else '- %s' % (-(a1 + 1))
        str_b_pt = '+ %s' % (p - 2*q) if p - 2*q >= 0 else '- %s' % (-(p - 2*q))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm nghiệm âm của phương trình $%s + \\frac{x - %s}{x + 1} = \\frac{%s}{x^2 - 1}$.'''
                         %(term1, str(a2), str(rhs)
                         ))

        # Nội dung lời giải
        loigiai = ('''Điều kiện xác định: $x \\neq 1$ và $x \\neq -1$. \\\\
                   Quy đồng mẫu thức hai vế và khử mẫu, ta được: \\\\
                   $(x %s)(x + 1) + (x - %s)(x - 1) = %s$ \\\\
                   $\\Leftrightarrow x^2 %s x %s + x^2 - %sx + %s = %s$ \\\\
                   $\\Leftrightarrow 2x^2 %s x - %s = 0$. \\\\
                   Tính biệt thức $\\Delta = (%s)^2 - 4 \\cdot 2 \\cdot (-%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt $x_1 = %s$ (thỏa mãn ĐKXĐ) và $x_2 = %s = %s$ (thỏa mãn ĐKXĐ). \\\\
                   Vậy nghiệm âm của phương trình đã cho là $%s$.'''
                   %(str_a1, str(a2), str(rhs),
                     str_a1_1, str_a1, str(a2+1), str(a2), str(rhs),
                     str_b_pt, str(p*q),
                     str(p-2*q), str(p*q), str((p-2*q)**2 + 8*p*q),
                     str(q), latex(x_neg), kq_str,
                     kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
