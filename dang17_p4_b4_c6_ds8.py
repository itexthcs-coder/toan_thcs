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




def bt_dang17_p4_b4_c6_ds8(self):
    # Dạng 17: Bài toán năng suất lao động – Xưởng sản xuất cải tiến kĩ thuật (Bài 6.35 SGK)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_sx = random.choice([
            (90000, 10, 2000, 900),   # x = 100, tt = 92000/90 -> chọn bộ chia hết:
            (72000, 10, 800, 900),    # x = 80, tt = 72800 / 70 = 1040 -> hơn 140
            (60000, 5, 500, 1000),    # x = 60, tt = 60500 / 55 = 1100 -> hơn 100
            (80000, 11, 100, 800)     # x = 100, tt = 80100 / 89 = 900 -> hơn 100
        ])
        if bo_sx[0] == 90000:
            bo_sx = (72000, 10, 800, 900)
            
        kh, som, vuot, ns_kh = bo_sx
        tt = kh + vuot
        x_ngay = kh // ns_kh
        ns_tt = tt // (x_ngay - som)
        chenh = ns_tt - ns_kh
        
        ti_so = Rational(tt, kh)
        tu_ts = ti_so.p
        mau_ts = ti_so.q
        
        noidungcauhoi = ("""Một xưởng sản xuất lập kế hoạch làm $%s$ sản phẩm trong $x$ (ngày) ($x > %s$). Nhờ cải tiến quy trình kĩ thuật, xưởng đã hoàn thành kế hoạch sớm $%s$ ngày và làm vượt mức $%s$ sản phẩm. \\\\
        a) Viết các phân thức theo biến $x$ biểu thị số sản phẩm mỗi ngày xưởng làm được theo kế hoạch và theo thực tế. \\\\
        b) Viết phân thức biểu thị tỉ số giữa năng suất thực tế mỗi ngày và năng suất kế hoạch mỗi ngày, đồng thời viết biểu thức biểu thị số sản phẩm mỗi ngày xưởng làm được nhiều hơn so với kế hoạch. \\\\
        c) Nếu theo kế hoạch mỗi ngày xưởng làm $%s$ sản phẩm thì thực tế mỗi ngày xưởng làm được nhiều hơn kế hoạch bao nhiêu sản phẩm?"""
                         % (kh, som, som, vuot, ns_kh))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Phân thức biểu thị số sản phẩm mỗi ngày xưởng làm được theo kế hoạch là $\\frac{%s}{x}$ (sản phẩm).\\\\
        Thực tế xưởng làm được $%s + %s = %s$ sản phẩm trong $x - %s$ ngày, nên phân thức biểu thị số sản phẩm thực tế xưởng làm được mỗi ngày là $\\frac{%s}{x - %s}$ (sản phẩm). \n
        \\item Tỉ số giữa năng suất thực tế mỗi ngày và năng suất kế hoạch mỗi ngày là:\\\\
        $$\\frac{%s}{x - %s} : \\frac{%s}{x} = \\frac{%s}{x - %s} \\cdot \\frac{x}{%s} = \\frac{%sx}{%s(x - %s)}.$$\\\\
        Biểu thức biểu thị số sản phẩm mỗi ngày xưởng làm được nhiều hơn so với kế hoạch là:\\\\
        $$\\frac{%s}{x - %s} - \\frac{%s}{x} \\text{ (sản phẩm)}.$$ \n
        \\item Vì theo kế hoạch mỗi ngày xưởng làm $%s$ sản phẩm nên số ngày dự kiến là $x = \\frac{%s}{%s} = %s$ (ngày).\\\\
        Thay $x = %s$ vào biểu thức chênh lệch năng suất, ta được:\\\\
        $$\\frac{%s}{%s - %s} - \\frac{%s}{%s} = %s - %s = %s \\text{ (sản phẩm)}.$$ \n
        \\end{enumEX} \n"""
                   % (kh, kh, vuot, tt, som, tt, som,
                      tt, som, kh, tt, som, kh, tu_ts, mau_ts, som,
                      tt, som, kh,
                      ns_kh, kh, ns_kh, x_ngay,
                      x_ngay, tt, x_ngay, som, kh, x_ngay, ns_tt, ns_kh, chenh))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
