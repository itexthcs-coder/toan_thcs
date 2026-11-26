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


def bt_dang10_p4_b2_c7_ds8(self):
    # Dạng 10: Phương trình nghiệm đúng với mọi x và tính giá trị biểu thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a_val = random.randint(1, 4)
        b_val = random.randint(2, 5)
        k = random.randint(2, 3)
        # (k*a - b + c1)x + (a + k*b - c2) = 0
        c1 = b_val - k * a_val
        c2 = a_val + k * b_val
        dau_c1 = '+ %s' % c1 if c1 > 0 else '- %s' % abs(c1)
        if c1 == 0:
            dau_c1 = ''
        P_val = a_val ** 2 + b_val ** 2
        
        noidungcauhoi = ('''Tìm các hằng số $a$ và $b$ sao cho phương trình $(%sa - b %s)x + (a + %sb - %s) = 0$ nghiệm đúng với mọi số thực $x$. Từ đó tính giá trị của biểu thức $P = a^2 + b^2$.'''
                         % (k, dau_c1, k, c2))
        
        loigiai = ('''Phương trình $(%sa - b %s)x + (a + %sb - %s) = 0$ nghiệm đúng với mọi số thực $x$ khi và chỉ khi hệ số của $x$ và hạng tử tự do đồng thời bằng $0$: \\\\
$\\begin{cases} %sa - b %s = 0 \\\\ a + %sb - %s = 0 \\end{cases}$ \\\\
Từ phương trình đầu suy ra $b = %sa %s$. Thay vào phương trình thứ hai, ta được: \\\\
$a + %s(%sa %s) - %s = 0$ \\\\
$\\Leftrightarrow a + %sa + (%s) - %s = 0$ \\\\
$\\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$. \\\\
Suy ra $b = %s \\cdot %s %s = %s$. \\\\
Khi đó giá trị của biểu thức $P$ là: $P = %s^2 + %s^2 = %s + %s = %s$. \\\\
Vậy $a = %s$, $b = %s$ và $P = %s$.'''
                   % (k, dau_c1, k, c2,
                      k, dau_c1, k, c2,
                      k, dau_c1,
                      k, k, dau_c1, c2,
                      k*k, k*c1, c2,
                      1 + k*k, c2 - k*c1, a_val,
                      k, a_val, dau_c1, b_val,
                      a_val, b_val, a_val**2, b_val**2, P_val,
                      a_val, b_val, P_val))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
