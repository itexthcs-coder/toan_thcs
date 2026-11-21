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


def bt_dang8_p3_b4_c2_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chọn nghiệm âm thập phân có 1 chữ số sau dấu phẩy (-0,8; -0,6; -0,4; -1,2; -1,5; -2,5)
        cap_nghiem = random.choice([
            (4, 1, 1, 5, -0.8),   # (4x-1)^2 - (x+5)^2 = 0 => (3x-6)(5x+4)=0 => x=2; x=-0,8
            (3, 1, 2, 2, -0.6),   # (3x-1)^2 - (2x+2)^2 = 0 => (x-3)(5x+1)=0 => x=3; x=-0,2
            (4, 2, 1, 4, -1.2),   # (4x-2)^2 - (x+4)^2 = 0 => (3x-6)(5x+2)=0 => x=2; x=-0,4
            (3, 2, 1, 4, -1.5)    # (3x-2)^2 - (x+4)^2 = 0 => (2x-6)(4x+2)=0 => x=3; x=-0,5
        ])
        a, b, c, d, _ = cap_nghiem
        bt1 = a*x - b
        bt2 = c*x + d
        nt1 = expand(bt1 - bt2)
        nt2 = expand(bt1 + bt2)
        x1 = Rational(b + d, a - c)
        x2 = Rational(b - d, a + c)
        nghiem_am = min(x1, x2)
        dec_val = Decimal(str(float(nghiem_am))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(dec_val).replace('.', ',')
        
        noidungcauhoi = ('''Tìm nghiệm âm của phương trình $(%s)^2 - (%s)^2 = 0$ (kết quả viết dưới dạng số thập phân).'''
                         % (latex(bt1), latex(bt2)))
        
        loigiai = ('''Áp dụng hằng đẳng thức hiệu hai bình phương, ta có:
\\begin{align*}
(%s)^2 - (%s)^2 &= 0 \\\\
[(%s) - (%s)][(%s) + (%s)] &= 0 \\\\
(%s)(%s) &= 0.
\\end{align*}
Suy ra $%s = 0$ hoặc $%s = 0$, tức là $x = %s$ hoặc $x = %s = %s$.\\\\
Vậy nghiệm âm của phương trình là $%s$.'''
                   % (latex(bt1), latex(bt2), latex(bt1), latex(bt2), latex(bt1), latex(bt2),
                      latex(nt1), latex(nt2), latex(nt1), latex(nt2), latex(x1), latex(x2), kq_str, kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
