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


def bt_dang9_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a_val = randint(2, 4)
        b_val = a_val - 2
        
        heso_m = 3 - 2*a_val
        const_M = a_val**2 - 3*b_val
        m_min = Rational(-heso_m, 2)
        gt_min = const_M - Rational(heso_m**2, 4)
        
        if b_val == 0:
            str_c = "- m"
        elif b_val > 0:
            str_c = "- m + %s" % latex(b_val)
        else:
            str_c = "- m - %s" % latex(abs(b_val))

        heso_m_delta = 4 - 2*a_val
        str_heso_m_delta = "+ %s" % latex(heso_m_delta) if heso_m_delta >= 0 else "- %s" % latex(abs(heso_m_delta))
        const_delta = a_val**2 - 4*b_val
        if 2 - a_val == 0:
            str_bp_delta = "m^{2}"
        elif 2 - a_val > 0:
            str_bp_delta = "(m + %s)^{2}" % latex(2 - a_val)
        else:
            str_bp_delta = "(m - %s)^{2}" % latex(abs(2 - a_val))
            
        str_heso_m_M = "+ %s" % latex(heso_m) if heso_m >= 0 else "- %s" % latex(abs(heso_m))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $x^{2} + (m - %s)x %s = 0$. Tìm giá trị của tham số $m$ để phương trình có hai nghiệm $x_{1}, x_{2}$ sao cho biểu thức $M = x_{1}^{2} + x_{2}^{2} - x_{1}x_{2}$ đạt giá trị nhỏ nhất.'''
                         % (latex(a_val), str_c))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta = (m - %s)^{2} - 4 \\cdot 1 \\cdot (%s) = m^{2} %sm + %s = %s + 4 > 0$ với mọi $m$. \\\\
Do đó phương trình luôn có hai nghiệm phân biệt $x_{1}, x_{2}$ với mọi giá trị của $m$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = -(m - %s) \\\\ x_{1}x_{2} = %s \\end{cases}$. \\\\
Ta có: $M = x_{1}^{2} + x_{2}^{2} - x_{1}x_{2} = (x_{1} + x_{2})^{2} - 3x_{1}x_{2}$ \\\\
$= [-(m - %s)]^{2} - 3(%s) = m^{2} - %sm + %s + 3m - %s = m^{2} %sm + %s$ \\\\
$= \\left(m - %s\\right)^{2} + %s \\ge %s$ với mọi $m$. \\\\
Dấu ``='' xảy ra khi và chỉ khi $m - %s = 0 \\Leftrightarrow m = %s$. \\\\
Vậy giá trị nhỏ nhất của $M$ là $%s$, đạt được khi $m = %s$.'''
                   % (latex(a_val), str_c, str_heso_m_delta, latex(const_delta), str_bp_delta,
                      latex(a_val), str_c,
                      latex(a_val), str_c, latex(2*a_val), latex(a_val**2), latex(3*b_val), str_heso_m_M, latex(const_M),
                      latex(m_min), latex(gt_min), latex(gt_min),
                      latex(m_min), latex(m_min),
                      latex(gt_min), latex(m_min)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
