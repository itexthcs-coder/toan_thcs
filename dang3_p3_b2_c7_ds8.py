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


def bt_dang3_p3_b2_c7_ds8(self):
    # Dạng 3: Tìm tham số để hai phương trình bậc nhất có cùng tập nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x0 = random.randint(2, 7)
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(a + 1, a + 4)
        rhs1 = d * x0 - (a * (x0 - b) + c)
        
        m_val = random.randint(-5, 6)
        while m_val == 0:
            m_val = random.randint(-5, 6)
        p = random.randint(3, 6)
        r = random.randint(1, p - 1)
        q = random.randint(2, 4)
        s = (p - r) * x0 - q * m_val
        
        dau_rhs1 = '- %s' % rhs1 if rhs1 > 0 else '+ %s' % abs(rhs1)
        if rhs1 == 0:
            dau_rhs1 = ''
        dau_s = '+ %s' % s if s > 0 else '- %s' % abs(s)
        if s == 0:
            dau_s = ''
            
        kq_str = str(m_val)
        
        noidungcauhoi = ('''Tìm giá trị của tham số $m$ để hai phương trình $%s(x - %s) + %s = %sx %s$ và $%sx - %sm = %sx %s$ có cùng tập nghiệm.'''
                         % (a, b, c, d, dau_rhs1, p, q, r, dau_s))
        
        loigiai = ('''Giải phương trình thứ nhất: \\\\
$%s(x - %s) + %s = %sx %s$ \\\\
$\\Leftrightarrow %sx - %s + %s = %sx %s$ \\\\
$\\Leftrightarrow %sx - %sx = %s + %s - %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\
Để hai phương trình có cùng tập nghiệm thì $x = %s$ cũng là nghiệm của phương trình thứ hai. \\\\
Thay $x = %s$ vào phương trình $%sx - %sm = %sx %s$, ta được: \\\\
$%s \\cdot %s - %sm = %s \\cdot %s %s$ \\\\
$\\Leftrightarrow %s - %sm = %s$ \\\\
$\\Leftrightarrow -%sm = %s \\Leftrightarrow m = %s$.'''
                   % (a, b, c, d, dau_rhs1,
                      a, a*b, c, d, dau_rhs1,
                      a, d, -rhs1, a*b, c,
                      a - d, (a - d)*x0, x0,
                      x0,
                      x0, p, q, r, dau_s,
                      p, x0, q, r, x0, dau_s,
                      p*x0, q, r*x0 + s,
                      q, r*x0 + s - p*x0, m_val))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
