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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang6_p4_b2_c7_ds8(self):
    # Dạng 6: Tìm tham số m để phương trình có nghiệm duy nhất thỏa mãn điều kiện phụ
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(2, 5)
        k = random.randint(2, 4)
        # (m - a)x + k(m^2 - a^2) = 0 => với m != a, x = -k(m + a)
        # Điều kiện phụ: x^2 - 2*x0*x + x0^2 = 0 <=> (x - x0)^2 = 0 <=> x = x0
        x0 = random.choice([-4, -2, 2, 4])
        while x0 % k != 0:
            x0 = random.choice([-6, -4, -3, -2, 2, 3, 4, 6])
        m_val = -(x0 // k) - a
        while m_val == a:
            x0 = -x0
            m_val = -(x0 // k) - a
            
        ka2 = k * a * a
        b_quad = -2 * x0
        c_quad = x0 * x0
        dau_b = '+ %s' % b_quad if b_quad > 0 else '- %s' % abs(b_quad)
        
        noidungcauhoi = ('''Cho phương trình $(m - %s)x + %sm^2 - %s = 0$ ($m$ là tham số). Tìm $m$ để phương trình có nghiệm duy nhất $x$ thỏa mãn điều kiện $x^2 %sx + %s = 0$.'''
                         % (a, k, ka2, dau_b, c_quad))
        
        loigiai = ('''Để phương trình $(m - %s)x + %sm^2 - %s = 0$ có nghiệm duy nhất thì hệ số của $x$ phải khác $0$: \\\\
$m - %s \\neq 0 \\Leftrightarrow m \\neq %s$. \\\\
Khi đó nghiệm duy nhất của phương trình là: \\\\
$x = \\frac{-%sm^2 + %s}{m - %s} = \\frac{-%s(m^2 - %s)}{m - %s} = \\frac{-%s(m - %s)(m + %s)}{m - %s} = -%s(m + %s)$. \\\\
Theo đề bài, nghiệm $x$ thỏa mãn điều kiện: \\\\
$x^2 %sx + %s = 0 \\Leftrightarrow (x - (%s))^2 = 0 \\Leftrightarrow x = %s$. \\\\
Thay $x = %s$ vào biểu thức của $x$ theo $m$, ta được: \\\\
$-%s(m + %s) = %s \\Leftrightarrow m + %s = %s \\Leftrightarrow m = %s$ (thỏa mãn điều kiện $m \\neq %s$). \\\\
Vậy giá trị cần tìm là $m = %s$.'''
                   % (a, k, ka2,
                      a, a,
                      k, ka2, a, k, a*a, a, k, a, a, a, k, a,
                      dau_b, c_quad, x0, x0,
                      x0,
                      k, a, x0, a, -x0 // k, m_val, a,
                      m_val))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
