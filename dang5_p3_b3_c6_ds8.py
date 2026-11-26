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
def bt_dang5_p3_b3_c6_ds8(self):
    # Dạng 5: Tính tổng dãy phân thức sai phân có mẫu là tích hai nhị thức cách đều
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # D = 2/(x(x+2)) + 2/((x+2)(x+4)) + 2/((x+4)(x+6)) + 2/((x+6)(x+8)) = 1/x - 1/(x+8)
        # Chọn x_val = 2 => 1/2 - 1/10 = 0,4
        # Hoặc x_val = 4 => 1/4 - 1/12 = 1/6 (vô hạn); x_val = 12 => 1/12 - 1/20 = 1/30; x_val = 2 => 0,4;
        # Hoặc tổng 3 số hạng: 1/x - 1/(x+6), chọn x_val = 2 => 1/2 - 1/8 = 0,375 (5 ký tự -> tránh), chọn x_val = 4 => 1/4 - 1/10 = 0,15 (4 ký tự!)
        # Chọn x_val = 2 với 4 số hạng -> 0,4; x_val = 4 với 3 số hạng -> 0,15; x_val = 6 với 4 số hạng -> 1/6 - 1/14; x_val = 2 với 3 số hạng nhân 2 -> 0,75
        bo = [
            (2, 4, '0,4', '\\dfrac{1}{2} - \\dfrac{1}{10} = \\dfrac{4}{10} = 0,4'),
            (4, 3, '0,15', '\\dfrac{1}{4} - \\dfrac{1}{10} = \\dfrac{3}{20} = 0,15')
        ]
        x_val, so_hang, kq_str, buoc_tinh = random.choice(bo)
        
        if so_hang == 4:
            bt_str = '\\dfrac{2}{x(x + 2)} + \\dfrac{2}{(x + 2)(x + 4)} + \\dfrac{2}{(x + 4)(x + 6)} + \\dfrac{2}{(x + 6)(x + 8)}'
            dk_str = 'x \\neq 0, -2, -4, -6, -8'
            buoc_tach = '\\left(\\dfrac{1}{x} - \\dfrac{1}{x + 2}\\right) + \\left(\\dfrac{1}{x + 2} - \\dfrac{1}{x + 4}\\right) + \\left(\\dfrac{1}{x + 4} - \\dfrac{1}{x + 6}\\right) + \\left(\\dfrac{1}{x + 6} - \\dfrac{1}{x + 8}\\right) = \\dfrac{1}{x} - \\dfrac{1}{x + 8}'
        else:
            bt_str = '\\dfrac{2}{x(x + 2)} + \\dfrac{2}{(x + 2)(x + 4)} + \\dfrac{2}{(x + 4)(x + 6)}'
            dk_str = 'x \\neq 0, -2, -4, -6'
            buoc_tach = '\\left(\\dfrac{1}{x} - \\dfrac{1}{x + 2}\\right) + \\left(\\dfrac{1}{x + 2} - \\dfrac{1}{x + 4}\\right) + \\left(\\dfrac{1}{x + 4} - \\dfrac{1}{x + 6}\\right) = \\dfrac{1}{x} - \\dfrac{1}{x + 6}'
            
        noidungcauhoi = ('Tính giá trị của biểu thức $D = %s$ tại $x = %s$.' % (bt_str, x_val))
        
        loigiai = ('Điều kiện xác định: $%s$.\\'
                   'Sử dụng công thức tách $\\dfrac{2}{A(A + 2)} = \\dfrac{1}{A} - \\dfrac{1}{A + 2}$, ta có:\\'
                   '$$D = %s.$$\\'
                   'Thay $x = %s$ vào biểu thức rút gọn, ta được $D = %s$.'
                   % (dk_str, buoc_tach, x_val, buoc_tinh))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
