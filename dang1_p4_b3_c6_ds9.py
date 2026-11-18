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


def bt_dang1_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            b_val = randint(3, 9)
            c_val = randint(1, 6)
            delta = b_val**2 - 4*c_val
            if delta > 0 and int(math.isqrt(delta))**2 != delta:
                break
                
        S = b_val
        P = c_val
        tu_chung = S**2 - 2*P
        kq = Rational(tu_chung * S, P)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $x^{2} - %sx + %s = 0$ có hai nghiệm phân biệt $x_{1}, x_{2}$. Không giải phương trình, hãy tính giá trị của biểu thức $A = \\dfrac{x_{1}^{2} + %sx_{2} - %s}{x_{2}} + \\dfrac{x_{2}^{2} + %sx_{1} - %s}{x_{1}}$.'''
                         % (latex(S), latex(P), latex(S), latex(P), latex(S), latex(P)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0$ nên phương trình luôn có hai nghiệm phân biệt $x_{1}, x_{2}$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = %s \\\\ x_{1}x_{2} = %s \\end{cases}$. \\\\
Vì $x_{1}$ là nghiệm của phương trình đã cho nên $x_{1}^{2} - %sx_{1} + %s = 0 \\Rightarrow x_{1}^{2} - %s = %sx_{1}$. \\\\
Tương tự, vì $x_{2}$ là nghiệm của phương trình nên $x_{2}^{2} - %s = %sx_{2}$. \\\\
Thay vào biểu thức $A$, ta được: \\\\
$A = \\dfrac{%sx_{1} + %sx_{2}}{x_{2}} + \\dfrac{%sx_{2} + %sx_{1}}{x_{1}} = \\dfrac{%s(x_{1} + x_{2})}{x_{2}} + \\dfrac{%s(x_{1} + x_{2})}{x_{1}}$ \\\\
$= %s(x_{1} + x_{2}) \\left(\\dfrac{1}{x_{1}} + \\dfrac{1}{x_{2}}\\right) = \\dfrac{%s(x_{1} + x_{2})^{2}}{x_{1}x_{2}} = \\dfrac{%s \\cdot %s^{2}}{%s} = %s$.'''
                   % (latex(S), latex(P), latex(delta),
                      latex(S), latex(P),
                      latex(S), latex(P), latex(P), latex(S),
                      latex(P), latex(S),
                      latex(S), latex(S), latex(S), latex(S), latex(S), latex(S),
                      latex(S), latex(S), latex(S), latex(S), latex(P), latex(kq)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
