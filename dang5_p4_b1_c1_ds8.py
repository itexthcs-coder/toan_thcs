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


def bt_dang5_p4_b1_c1_ds8(self):
    # Dạng 5: Sắp xếp các đơn thức đồng dạng thành từng nhóm và tính tổng toàn bộ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(2, 4)
        c_nhom2 = k + 3
        x0 = random.choice([-2, 2])
        y0 = random.choice([2, 3])
        gt_tong = (x0 ** 3) * (y0 ** 2)

        noidungcauhoi = ('Cho các đơn thức: $\\frac{3}{4}x^{3}y^{2}$; $-%sx^{2}y^{3}$; $-0,75x^{3}y^{2}$; $%sx^{2}y^{3}$; $x^{3}y^{2}$; $-3x^{2}y^{3}$. \\\\\n'
                         'a) Hãy sắp xếp các đơn thức trên thành từng nhóm các đơn thức đồng dạng và tính tổng các đơn thức trong mỗi nhóm. \\\\\n'
                         'b) Tính tổng của tất cả các đơn thức đã cho tại $x = %s$ và $y = %s$.'
                         % (k, c_nhom2, x0, y0))

        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Ta sắp xếp các đơn thức đã cho thành $2$ nhóm đồng dạng:\\\\\n'
                   '- Nhóm 1 (phần biến $x^{3}y^{2}$): $\\frac{3}{4}x^{3}y^{2}$; $-0,75x^{3}y^{2}$ và $x^{3}y^{2}$.\\\\\n'
                   'Tổng của nhóm 1 là: $\\left(\\frac{3}{4} - 0,75 + 1\\right)x^{3}y^{2} = (0,75 - 0,75 + 1)x^{3}y^{2} = x^{3}y^{2}$.\\\\\n'
                   '- Nhóm 2 (phần biến $x^{2}y^{3}$): $-%sx^{2}y^{3}$; $%sx^{2}y^{3}$ và $-3x^{2}y^{3}$.\\\\\n'
                   'Tổng của nhóm 2 là: $(-%s + %s - 3)x^{2}y^{3} = 0 \\cdot x^{2}y^{3} = 0$. \n'
                   '\\item Tổng của tất cả các đơn thức đã cho là: $S = x^{3}y^{2} + 0 = x^{3}y^{2}$.\\\\\n'
                   'Thay $x = %s$ và $y = %s$ vào $S$, ta được: $S = (%s)^{3} \\cdot %s^{2} = %s \\cdot %s = %s$. \n'
                   '\\end{enumEX} \n'
                   % (k, c_nhom2, k, c_nhom2, x0, y0, x0, y0, x0 ** 3, y0 ** 2, gt_tong))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
