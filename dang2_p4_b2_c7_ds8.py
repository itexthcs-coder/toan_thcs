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


def bt_dang2_p4_b2_c7_ds8(self):
    # Dạng 2: Giải phương trình bậc nhất có chứa phân số tầng (liên phân số)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(1, 3)
        b = random.randint(2, 4)
        c = random.randint(2, 5)
        d = random.randint(2, 5)
        e = random.randint(3, 6)
        k = random.randint(2, 4)
        x_val = Rational(random.choice([1, 2, 3, 5, 7]), random.choice([2, 3, 4]))
        while x_val.q == 1:
            x_val = Rational(random.choice([1, 2, 3, 5, 7]), random.choice([2, 3, 4]))
            
        t4 = e + Rational(x_val, k)
        t3 = c + Rational(d, t4)
        rhs = a + Rational(b, t3)
        
        # Điều kiện xác định:
        # 5 + x/2 != 0 => x != -e*k
        dk1 = -e * k
        # c + d/(e + x/k) != 0 => e + x/k != -d/c => x != -k*(e + Rational(d, c))
        dk2 = -k * (e + Rational(d, c))
        
        noidungcauhoi = ('''Giải phương trình sau: \\\\
$%s + \\frac{%s}{%s + \\frac{%s}{%s + \\frac{x}{%s}}} = %s$.'''
                         % (a, b, c, d, e, k, latex(rhs)))
        
        loigiai = ('''Điều kiện xác định: $x \\neq %s$ và $x \\neq %s$. \\\\
Biến đổi phương trình theo từng tầng phân số từ ngoài vào trong, ta được: \\\\
$\\frac{%s}{%s + \\frac{%s}{%s + \\frac{x}{%s}}} = %s - %s = %s$ \\\\
$\\Rightarrow %s + \\frac{%s}{%s + \\frac{x}{%s}} = %s : %s = %s$ \\\\
$\\Rightarrow \\frac{%s}{%s + \\frac{x}{%s}} = %s - %s = %s$ \\\\
$\\Rightarrow %s + \\frac{x}{%s} = %s : %s = %s$ \\\\
$\\Rightarrow \\frac{x}{%s} = %s - %s = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện xác định). \\\\
Vậy nghiệm của phương trình là $x = %s$.'''
                   % (latex(dk1), latex(dk2),
                      b, c, d, e, k, latex(rhs), a, latex(rhs - a),
                      c, d, e, k, b, latex(rhs - a), latex(t3),
                      d, e, k, latex(t3), c, latex(t3 - c),
                      e, k, d, latex(t3 - c), latex(t4),
                      k, latex(t4), e, latex(t4 - e), latex(x_val),
                      latex(x_val)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
