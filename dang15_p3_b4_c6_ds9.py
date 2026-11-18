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


def bt_dang15_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        von = 300
        rut = 100
        ls = random.choice([5, 6, 7, 8])
        r_rat = Rational(ls, 100)
        t_ans_rat = 1 + r_rat
        nam1_rat = von * t_ans_rat - rut
        nam2_rat = nam1_rat * t_ans_rat
        nam2_dec = Decimal(nam2_rat.p) / Decimal(nam2_rat.q)
        nam2_str = str(nam2_dec.normalize()).replace('.', ',')
        t_ans_str = str((Decimal(t_ans_rat.p) / Decimal(t_ans_rat.q)).normalize()).replace('.', ',')
        r_str = str((Decimal(r_rat.p) / Decimal(r_rat.q)).normalize()).replace('.', ',')

        t_sym = symbols('t')
        eq = sp.Eq(300 * t_sym**2 - 100 * t_sym - nam2_rat, 0)
        sols = sp.solve(eq, t_sym)
        t_neg = [s for s in sols if s < 0][0]
        delta_p = Rational(50**2) + 300 * nam2_rat
        sqrt_dp = sp.sqrt(delta_p)
        delta_p_str = str((Decimal(delta_p.p) / Decimal(delta_p.q)).normalize()).replace('.', ',')
        sqrt_dp_rat = Rational(sqrt_dp)
        sqrt_dp_str = str((Decimal(sqrt_dp_rat.p) / Decimal(sqrt_dp_rat.q)).normalize()).replace('.', ',')

        noidungcauhoi = ('''Cô Mai gửi $%s$ triệu đồng vào ngân hàng với kì hạn $12$ tháng. Sau $1$ năm, cô Mai rút ra $%s$ triệu đồng để sửa nhà, số tiền còn lại (gồm cả gốc còn lại và lãi năm đầu) tiếp tục gửi thêm $12$ tháng nữa với lãi suất như cũ. Kết thúc năm thứ hai, cô Mai tất toán nhận được $%s$ triệu đồng. Tính lãi suất gửi tiết kiệm một năm (đơn vị: \\%%).'''
                         % (str(von), str(rut), nam2_str))

        loigiai = ('''Gọi lãi suất gửi tiết kiệm một năm là $x\\%%$. Điều kiện: $x > 0$.\\\\
                   Đặt $t = 1 + \\dfrac{x}{100}$ (điều kiện: $t > 1$).\\\\
                   Sau năm thứ nhất, số tiền cả vốn lẫn lãi cô Mai có được là $%st$ (triệu đồng).\\\\
                   Sau khi rút ra $%s$ triệu đồng, số tiền gốc cô Mai gửi tiếp cho năm thứ hai là $%st - %s$ (triệu đồng).\\\\
                   Kết thúc năm thứ hai, số tiền cô Mai nhận được là $(%st - %s)t$ (triệu đồng).\\\\
                   Theo đề bài, ta có phương trình:\\\\
                   $(%st - %s)t = %s$ hay $%st^2 - %st - %s = 0$.\\\\
                   Ta có: $\\Delta' = (-50)^2 - %s \\cdot (-%s) = %s$; $\\sqrt{\\Delta'} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $t_1 = \\dfrac{50 - %s}{%s} = %s$ (loại); $t_2 = \\dfrac{50 + %s}{%s} = %s$ (thỏa mãn điều kiện $t > 1$).\\\\
                   Với $t = %s$, ta có $1 + \\dfrac{x}{100} = %s \\Leftrightarrow \\dfrac{x}{100} = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy lãi suất gửi tiết kiệm một năm là $%s\\%%$.'''
                   % (str(von), str(rut), str(von), str(rut), str(von), str(rut),
                      str(von), str(rut), nam2_str, str(von), str(rut), nam2_str,
                      str(von), nam2_str, delta_p_str, sqrt_dp_str,
                      sqrt_dp_str, str(von), latex(t_neg),
                      sqrt_dp_str, str(von), t_ans_str,
                      t_ans_str, t_ans_str, r_str, str(ls), str(ls)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(ls))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
