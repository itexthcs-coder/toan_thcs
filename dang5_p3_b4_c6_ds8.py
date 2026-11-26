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




def bt_dang5_p3_b4_c6_ds8(self):
    # Dạng 5: Tính tổng các giá trị nguyên của biến để thương hai phân thức nhận giá trị nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([1, 2, 3, 4])
        while b == a:
            b = random.choice([1, 2, 3, 4])
        p = random.choice([3, 5, 7]) # số nguyên tố lẻ -> 4 ước: +-1, +-p
        
        tu1 = sp.expand(p * (x + b))
        mau1 = sp.expand(x**2 - a**2)
        tu2 = sp.expand(x + b)
        mau2 = sp.expand(x - a)
        
        # D = p / (x + a). Ước của p là +-1, +-p => x + a in {-p, -1, 1, p}
        uoc_list = [-p, -1, 1, p]
        x_vals = [u - a for u in uoc_list]
        # Kiểm tra x != a và x != -b (luôn đúng nếu a != b và p không trùng 2a)
        while a in x_vals or -b in x_vals:
            b = random.choice([1, 2, 3, 4, 5, 6])
            tu1 = sp.expand(p * (x + b))
            tu2 = sp.expand(x + b)
            
        tong_x = sum(x_vals)
        kq_str = str(tong_x)
        
        noidungcauhoi = ("""Tìm tổng tất cả các giá trị nguyên của $x$ (thỏa mãn điều kiện xác định) để biểu thức $D = \\frac{%s}{%s} : \\frac{%s}{%s}$ nhận giá trị nguyên."""
                         % (latex(tu1), latex(mau1), latex(tu2), latex(mau2)))
        
        loigiai = ("""Điều kiện xác định: $x \\neq \\pm %s$ và $x \\neq %s$.\\\\
        Ta rút gọn biểu thức $D$:\\\\
        $$D = \\frac{%s(%s)}{(%s)(%s)} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}.$$\\\\
        Với $x \\in \\mathbb{Z}$, $D$ nhận giá trị nguyên khi và chỉ khi $%s$ là ước của $%s$, tức là:\\\\
        $$%s \\in \\{-%s; -1; 1; %s\\} \\Leftrightarrow x \\in \\{%s; %s; %s; %s\\}.$$\\\\
        Các giá trị trên đều thỏa mãn điều kiện xác định. Tổng của chúng bằng $(%s) + (%s) + (%s) + (%s) = %s$."""
                   % (a, -b, p, latex(tu2), latex(x - a), latex(x + a), latex(mau2), latex(tu2), p, latex(x + a),
                      latex(x + a), p, latex(x + a), p, p,
                      x_vals[0], x_vals[1], x_vals[2], x_vals[3],
                      x_vals[0], x_vals[1], x_vals[2], x_vals[3], tong_x))
        
        dapan = '\\shortans[0]{$%s$}\n' % kq_str
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
