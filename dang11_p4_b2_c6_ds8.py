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


def bt_dang11_p4_b2_c6_ds8(self):
    # Dạng 11: Đồng nhất hệ số khi phân tích một phân thức thành tổng các phân thức đơn giản
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a_val = random.choice([1, 2])
        b_val = random.choice([2, 3])
        c_val = random.choice([1, 2])

        tu_vp = expand(a_val * (x - 1) * (x + 2) + b_val * x * (x + 2) + c_val * x * (x - 1))
        c2 = int(tu_vp.coeff(x, 2))
        c1 = int(tu_vp.coeff(x, 1))
        c0 = int(tu_vp.coeff(x, 0))

        noidungcauhoi = ('Tìm các hằng số $a, b, c$ sao cho đẳng thức sau đúng với mọi $x \\notin \\{0; 1; -2\\}$:\\\n'
                         '$\\dfrac{%s}{x(x - 1)(x + 2)} = \\dfrac{a}{x} + \\dfrac{b}{x - 1} + \\dfrac{c}{x + 2}$.'
                         % latex(tu_vp))

        loigiai = ('Quy đồng mẫu thức vế phải với mẫu thức chung là $x(x - 1)(x + 2)$, ta có:\\\n'
                   '$\\dfrac{a}{x} + \\dfrac{b}{x - 1} + \\dfrac{c}{x + 2} = \\dfrac{a(x - 1)(x + 2) + bx(x + 2) + cx(x - 1)}{x(x - 1)(x + 2)}$\\\n'
                   '$= \\dfrac{a(x^2 + x - 2) + b(x^2 + 2x) + c(x^2 - x)}{x(x - 1)(x + 2)} = \\dfrac{(a + b + c)x^2 + (a + 2b - c)x - 2a}{x(x - 1)(x + 2)}$.\\\n'
                   'Đồng nhất hệ số của $x^2$, $x$ và hệ số tự do ở tử thức của hai vế, ta được:\\\n'
                   '$-2a = %s \\Rightarrow a = %s$.\\\n'
                   'Thay $a = %s$ vào hai phương trình còn lại:\\\n'
                   '$b + c = %s - %s = %s$ và $2b - c = %s - %s = %s$.\\\n'
                   'Cộng vế theo vế hai đẳng thức trên ta được $3b = %s \\Rightarrow b = %s$, suy ra $c = %s$.\\\n'
                   'Vậy $a = %s$, $b = %s$, $c = %s$.'
                   % (c0, a_val, a_val, c2, a_val, b_val + c_val, c1, a_val, 2 * b_val - c_val, 3 * b_val, b_val, c_val, a_val, b_val, c_val))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
