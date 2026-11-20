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

def bt_dang18_p3_b4_c1_ds8(self):
    x = symbols('x')
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c = random.choice([15, 20])
        lai_goc = random.choice([10, 12])
        p0 = c + lai_goc
        q0 = random.choice([60, 80, 100])
        giam = random.choice([2, 4])
        x0 = random.choice([5, 6, 8])

        L_bt = expand((lai_goc + x) * (q0 - giam * x))
        L0 = lai_goc * q0
        L_moi = L_bt.subs(x, x0)
        chenh = L_moi - L0

        noidungcauhoi = ('''Một cửa hàng nhập một loại áo với giá $%s$ nghìn đồng/chiếc và bán ra với giá $%s$ nghìn đồng/chiếc thì mỗi tuần bán được $%s$ chiếc. Cửa hàng nhận thấy nếu tăng giá bán thêm $x$ nghìn đồng mỗi chiếc thì số áo bán ra mỗi tuần giảm đi $%sx$ chiếc. Hỏi nếu tăng giá bán thêm $%s$ nghìn đồng mỗi chiếc thì lợi nhuận mỗi tuần của cửa hàng tăng thêm bao nhiêu nghìn đồng so với ban đầu?'''
                         % (c, p0, q0, giam, x0))

        loigiai = ('''Lợi nhuận thu được trên mỗi chiếc áo sau khi tăng giá là $(%s + x) - %s = %s + x$ (nghìn đồng).\\
Số lượng áo bán ra mỗi tuần là $%s - %sx$ (chiếc).\\
Đa thức biểu thị tổng lợi nhuận mỗi tuần của cửa hàng là:
\\begin{align*}
L(x) &= (%s + x)(%s - %sx) \\\\
&= %s \\ (\\text{nghìn đồng}).
\\end{align*}
Lợi nhuận ban đầu (khi $x = 0$) là $L(0) = %s$ (nghìn đồng).\\
Khi tăng giá thêm $%s$ nghìn đồng ($x = %s$), lợi nhuận là $L(%s) = (%s + %s)(%s - %s \\cdot %s) = %s$ (nghìn đồng).\\
Vậy lợi nhuận tăng thêm là $%s - %s = %s$ (nghìn đồng).'''
                   % (p0, c, lai_goc,
                      q0, giam,
                      lai_goc, q0, giam,
                      latex(L_bt),
                      L0,
                      x0, x0, x0, lai_goc, x0, q0, giam, x0, L_moi,
                      L_moi, L0, chenh))

        dapan = '\\shortans[0]{$%s$}\n' % chenh

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
