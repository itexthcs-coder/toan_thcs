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
def bt_dang10_p4_b3_c6_ds8(self):
    # Dạng 10: Đồng nhất hệ số khi phân tích phân thức có mẫu là tích ba nhị thức bậc nhất
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([1, 2, 3])
        b = random.choice([2, 3, 4])
        c = random.choice([-2, -1, 1, 2])
        while b == c or (a + b + c) == 0:
            c = random.choice([-2, -1, 1, 2])
            
        p = a + b + c
        q = b - c
        
        str_p = 'x^2' if p == 1 else '%sx^2' % p
        if q == 1:
            str_q = '+ x'
        elif q == -1:
            str_q = '- x'
        elif q > 0:
            str_q = '+ %sx' % q
        else:
            str_q = '- %sx' % abs(q)
            
        noidungcauhoi = ('Tìm các số thực $a, b, c$ sao cho đẳng thức sau đúng với mọi $x \\neq 0, x \\neq 1, x \\neq -1$:\\'
                         '$$\\dfrac{%s %s - %s}{x(x - 1)(x + 1)} = \\dfrac{a}{x} + \\dfrac{b}{x - 1} + \\dfrac{c}{x + 1}.$$'
                         % (str_p, str_q, a))
        
        loigiai = ('Quy đồng mẫu thức vế phải với mẫu thức chung $x(x - 1)(x + 1)$, ta có:\\'
                   '$$\\begin{aligned}'
                   '\\dfrac{a}{x} + \\dfrac{b}{x - 1} + \\dfrac{c}{x + 1} &= \\dfrac{a(x - 1)(x + 1) + bx(x + 1) + cx(x - 1)}{x(x - 1)(x + 1)} \\\\'
                   '&= \\dfrac{a(x^2 - 1) + b(x^2 + x) + c(x^2 - x)}{x(x - 1)(x + 1)} \\\\'
                   '&= \\dfrac{(a + b + c)x^2 + (b - c)x - a}{x(x - 1)(x + 1)}.'
                   '\\end{aligned}$$\\'
                   'Đồng nhất hệ số của các lũy thừa cùng bậc của $x$ trên tử thức hai vế, ta được:\\'
                   '$-a = -%s \\Rightarrow a = %s$;\\'
                   '$a + b + c = %s \\Rightarrow b + c = %s - %s = %s$;\\'
                   '$b - c = %s$.\\'
                   'Từ $b + c = %s$ và $b - c = %s$, suy ra $2b = %s \\Rightarrow b = %s$ và $c = %s$.\\'
                   'Vậy $a = %s, b = %s, c = %s$.'
                   % (a, a, p, p, a, b + c, q, b + c, q, 2 * b, b, c, a, b, c))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
