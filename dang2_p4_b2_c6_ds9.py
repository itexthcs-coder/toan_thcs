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


def bt_dang2_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(2, 4)
        x1 = -randint(1, 3)
        m_val = randint(2, 6)
        p = randint(2, 5)
        c_const = (m_val + p)*x1 - a*(x1**2) - m_val
        
        b_pt = -(m_val + p)
        c_pt = c_const + m_val
        
        delta = b_pt**2 - 4*a*c_pt
        x2 = Rational(-b_pt, a) - x1
        
        sign_c = "+" if c_const >= 0 else "-"
        abs_c = abs(c_const)
        
        sign_b_pt = "+" if b_pt >= 0 else "-"
        abs_b_pt = abs(b_pt)
        sign_c_pt = "+" if c_pt >= 0 else "-"
        abs_c_pt = abs(c_pt)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình bậc hai $%sx^2 - (m + %s)x + m %s %s = 0$ (với $m$ là tham số). Tìm giá trị của tham số $m$ để phương trình nhận $x = %s$ là một nghiệm. Với giá trị $m$ vừa tìm được, hãy xác định nghiệm còn lại của phương trình.'''
                         %(latex(a), latex(p), sign_c, latex(abs_c), latex(x1)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì phương trình nhận $x = %s$ là một nghiệm nên thay $x = %s$ vào phương trình đã cho, ta được: \\\\
                   $%s \\cdot (%s)^2 - (m + %s) \\cdot (%s) + m %s %s = 0$ \\\\
                   $\\Leftrightarrow %s - (%s m %s %s) + m %s %s = 0$ \\\\
                   $\\Leftrightarrow %s m + %s = 0$ \\\\
                   $\\Leftrightarrow m = %s$. \\\\
                   Thay $m = %s$ vào phương trình ban đầu, ta được phương trình bậc hai: \\\\
                   $%sx^2 %s %sx %s %s = 0$. \\\\
                   Ta có biệt thức $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt là $x_1 = %s$ và $x_2 = %s$. \\\\
                   Vậy $m = %s$ và nghiệm còn lại của phương trình là $x = %s$.'''
                   %(latex(x1), latex(x1),
                     latex(a), latex(x1), latex(p), latex(x1), sign_c, latex(abs_c),
                     latex(a*(x1**2)), latex(x1), "+" if p*x1 >= 0 else "-", latex(abs(p*x1)), sign_c, latex(abs_c),
                     latex(1 - x1), latex(a*(x1**2) - p*x1 + c_const),
                     latex(m_val),
                     latex(m_val),
                     latex(a), sign_b_pt, latex(abs_b_pt), sign_c_pt, latex(abs_c_pt),
                     latex(b_pt), latex(a), latex(c_pt), latex(delta),
                     latex(x1), latex(x2),
                     latex(m_val), latex(x2)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
