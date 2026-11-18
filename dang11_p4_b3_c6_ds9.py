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


def bt_dang11_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            a_val = randint(1, 4)
            b_val = randint(a_val + 1, 7)
            if math.gcd(b_val, 2*a_val) == 1:
                break
                
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $mx^{2} - 2(m - %s)x + m - %s = 0$ ($m \\ne 0$). Tìm một hệ thức liên hệ giữa hai nghiệm $x_{1}, x_{2}$ của phương trình (trong trường hợp phương trình có nghiệm) sao cho hệ thức đó độc lập với tham số $m$.'''
                         % (latex(a_val), latex(b_val)))
        
        # Nội dung lời giải
        loigiai = ('''Với $m \\ne 0$, giả sử phương trình có hai nghiệm $x_{1}, x_{2}$. Theo định lí Viète, ta có: \\\\
$\\begin{cases} x_{1} + x_{2} = \\dfrac{2(m - %s)}{m} = 2 - \\dfrac{%s}{m} \\\\ x_{1}x_{2} = \\dfrac{m - %s}{m} = 1 - \\dfrac{%s}{m} \\end{cases} \\Leftrightarrow \\begin{cases} \\dfrac{%s}{m} = 2 - (x_{1} + x_{2}) \\quad (1) \\\\ \\dfrac{%s}{m} = 1 - x_{1}x_{2} \\quad (2) \\end{cases}$. \\\\
Nhân hai vế của $(1)$ với $%s$ và nhân hai vế của $(2)$ với $%s$, ta được: \\\\
$\\begin{cases} \\dfrac{%s}{m} = %s - %s(x_{1} + x_{2}) \\\\ \\dfrac{%s}{m} = %s - %sx_{1}x_{2} \\end{cases}$. \\\\
Suy ra: $%s - %s(x_{1} + x_{2}) = %s - %sx_{1}x_{2} \\Leftrightarrow %s(x_{1} + x_{2}) - %sx_{1}x_{2} = %s$. \\\\
Đây là hệ thức liên hệ giữa hai nghiệm $x_{1}, x_{2}$ không phụ thuộc vào tham số $m$.'''
                   % (latex(a_val), latex(2*a_val), latex(b_val), latex(b_val),
                      latex(2*a_val), latex(b_val),
                      latex(b_val), latex(2*a_val),
                      latex(2*a_val*b_val), latex(2*b_val), latex(b_val),
                      latex(2*a_val*b_val), latex(2*a_val), latex(2*a_val),
                      latex(2*b_val), latex(b_val), latex(2*a_val), latex(2*a_val),
                      latex(b_val), latex(2*a_val), latex(2*b_val - 2*a_val)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
