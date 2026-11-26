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


def bt_dang5_p4_b2_c7_ds8(self):
    # Dạng 5: Tìm tham số m khi biết phương trình có nghiệm âm cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x0 = random.randint(-6, -2)
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(1, 5)
        # (a*x + m)/3 - (x - b*m)/2 = (x + c)/6
        # Quy đồng 6: 2(a*x0 + m) - 3(x0 - b*m) = x0 + c
        # (2 + 3b)m = x0 + c - 2*a*x0 + 3*x0 = (4 - 2a)x0 + c
        num_m = (4 - 2 * a) * x0 + c
        den_m = 2 + 3 * b
        m_val = Rational(num_m, den_m)
        
        noidungcauhoi = ('''Cho phương trình ẩn $x$: $\\frac{%sx + m}{3} - \\frac{x - %sm}{2} = \\frac{x + %s}{6}$. Tìm giá trị của tham số $m$ để phương trình đã cho nhận $x = %s$ làm nghiệm.'''
                         % (a, b, c, x0))
        
        loigiai = ('''Vì phương trình nhận $x = %s$ làm nghiệm nên thay $x = %s$ vào phương trình đã cho, ta được: \\\\
$\\frac{%s \\cdot (%s) + m}{3} - \\frac{%s - %sm}{2} = \\frac{%s + %s}{6}$ \\\\
$\\Leftrightarrow \\frac{m + (%s)}{3} - \\frac{%s - %sm}{2} = \\frac{%s}{6}$. \\\\
Quy đồng mẫu thức hai vế với mẫu chung là $6$, ta được: \\\\
$2(m + (%s)) - 3(%s - %sm) = %s$ \\\\
$\\Leftrightarrow 2m + (%s) - (%s) + %sm = %s$ \\\\
$\\Leftrightarrow %sm + (%s) = %s$ \\\\
$\\Leftrightarrow %sm = %s \\Leftrightarrow m = %s$. \\\\
Vậy giá trị cần tìm là $m = %s$.'''
                   % (x0, x0,
                      a, x0, x0, b, x0, c,
                      a*x0, x0, b, x0 + c,
                      a*x0, x0, b, x0 + c,
                      2*a*x0, 3*x0, 3*b, x0 + c,
                      den_m, 2*a*x0 - 3*x0, x0 + c,
                      den_m, num_m, latex(m_val),
                      latex(m_val)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
