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




def bt_dang19_p4_b4_c6_ds8(self):
    # Dạng 19: Bài toán năng suất làm chung – Hai đội công nhân sửa chữa đường
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_doi = random.choice([
            (12, 10, 20), # chung 12 ngày, đội 2 hơn 10 ngày, x = 20 (1/20 + 1/30 = 1/12)
            (6, 5, 10),   # chung 6 ngày, đội 2 hơn 5 ngày, x = 10 (1/10 + 1/15 = 1/6)
            (4, 6, 6)     # chung 4 ngày, đội 2 hơn 6 ngày, x = 6 (1/6 + 1/12 = 1/4)
        ])
        t_chung, d_hon, x0 = bo_doi
        ti_so = Rational(x0 + d_hon, x0)
        
        noidungcauhoi = ("""Hai đội công nhân cùng làm chung một đoạn đường thì hoàn thành trong $%s\\text{ ngày}$. Nếu làm riêng, đội thứ nhất cần $x\\text{ (ngày)}$ ($x > %s$) để hoàn thành toàn bộ công việc, còn đội thứ hai cần nhiều hơn đội thứ nhất $%s\\text{ ngày}$ mới hoàn thành. \\\\
        a) Viết các phân thức theo biến $x$ biểu thị phần công việc mỗi đội làm được trong $1\\text{ ngày}$ và tổng phần công việc cả hai đội làm được trong $1\\text{ ngày}$. \\\\
        b) Viết phân thức biểu thị tỉ số giữa năng suất làm việc trong $1\\text{ ngày}$ của đội thứ nhất và đội thứ hai. \\\\
        c) Biết rằng khi $x = %s$ thì hai đội hoàn thành công việc trong $%s\\text{ ngày}$. Hãy tính tỉ số năng suất giữa đội thứ nhất và đội thứ hai khi đó."""
                         % (t_chung, t_chung, d_hon, x0, t_chung))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Trong $1\\text{ ngày}$, đội thứ nhất làm được $\\frac{1}{x}$ (công việc) và đội thứ hai làm được $\\frac{1}{x + %s}$ (công việc).\\\\
        Tổng phần công việc cả hai đội làm được trong $1\\text{ ngày}$ là:\\\\
        $$\\frac{1}{x} + \\frac{1}{x + %s} = \\frac{x + %s + x}{x(x + %s)} = \\frac{2x + %s}{x(x + %s)}\\text{ (công việc)}.$$ \n
        \\item Tỉ số giữa năng suất làm việc trong $1\\text{ ngày}$ của đội thứ nhất và đội thứ hai là:\\\\
        $$\\frac{1}{x} : \\frac{1}{x + %s} = \\frac{1}{x} \\cdot \\frac{x + %s}{1} = \\frac{x + %s}{x}.$$ \n
        \\item Thay $x = %s$ vào phân thức tỉ số năng suất ở câu b, ta được:\\\\
        $$\\frac{%s + %s}{%s} = \\frac{%s}{%s} = %s.$$ \n
        \\end{enumEX} \n"""
                   % (d_hon, d_hon, d_hon, d_hon, d_hon, d_hon,
                      d_hon, d_hon, d_hon,
                      x0, x0, d_hon, x0, x0 + d_hon, x0, latex(ti_so)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
