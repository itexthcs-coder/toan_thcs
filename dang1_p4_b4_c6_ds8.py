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




def bt_dang1_p4_b4_c6_ds8(self):
    # Dạng 1: Thực hiện dãy phép nhân, chia phân thức kết hợp phân tích đa thức bằng phương pháp nhóm hạng tử
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        y_sym = sp.Symbol('y')
        a = random.randint(2, 5)
        x0 = random.choice([i for i in range(1, 7) if i != a])
        y0 = random.choice([-2025, -2026, 2026, 2027])
        
        tu1 = sp.expand(x**2 + x*y_sym - a*x - a*y_sym)
        mau1 = sp.expand(x**2 - a**2)
        tu2 = sp.expand(x + y_sym)
        mau2 = sp.expand((x + a)**2)
        
        gt_A = Rational(x0 + a, x0 - a)
        
        noidungcauhoi = ("""Cho biểu thức $A = \\frac{%s}{%s} : \\frac{%s}{%s}$ với $x \\neq \\pm %s$ và $x \\neq -y$. \\\\
        a) Phân tích tử thức và mẫu thức của các phân thức thành nhân tử rồi rút gọn biểu thức $A$. \\\\
        b) Tính giá trị của biểu thức $A$ tại $x = %s$ và $y = %s$."""
                         % (latex(tu1), latex(mau1), latex(tu2), latex(mau2), a, x0, y0))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Ta phân tích các tử thức và mẫu thức thành nhân tử:\\\\
        $%s = x(x + y) - %s(x + y) = (x - %s)(x + y)$;\\\\
        $%s = (x - %s)(x + %s)$;\\\\
        $%s = (x + %s)^2$.\\\\
        Khi đó:\\\\
        $$A = \\frac{(x - %s)(x + y)}{(x - %s)(x + %s)} \\cdot \\frac{(x + %s)^2}{x + y} = \\frac{x + %s}{x - %s}.$$ \n
        \\item Thay $x = %s$ (thỏa mãn điều kiện xác định) vào biểu thức rút gọn của $A$, ta được:\\\\
        $$A = \\frac{%s + %s}{%s - %s} = %s.$$ \n
        \\end{enumEX} \n"""
                   % (latex(tu1), a, a, latex(mau1), a, a, latex(mau2), a,
                      a, a, a, a, a, a, x0, x0, a, x0, a, latex(gt_A)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
