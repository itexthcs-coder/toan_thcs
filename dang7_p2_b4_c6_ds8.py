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




def bt_dang7_p2_b4_c6_ds8(self):
    # Dạng 7: Rút gọn biểu thức đại số hỗn hợp chứa hằng đẳng thức lập phương (Bài 6.33b SGK)
    p = random.choice([2, 3, 4])
    
    nb_da_1_d = '\\True Hiệu hai phân thức trong ngoặc rút gọn bằng $\\frac{y - x}{xy}$.'
    nb_da_1_s = 'Hiệu hai phân thức trong ngoặc rút gọn bằng $\\frac{x - y}{xy}$.'
    loigiai_nb_1 = """Ta có $\\frac{x + y}{xy} - \\frac{2}{x} = \\frac{x + y - 2y}{xy} = \\frac{y - x}{xy}$."""
    
    th_da_1_d = '\\True Đa thức $x^3 - y^3$ phân tích thành nhân tử là $(x - y)(x^2 + xy + y^2)$.'
    th_da_1_s = 'Đa thức $x^3 - y^3$ phân tích thành nhân tử là $(x - y)(x^2 - xy + y^2)$.'
    loigiai_th_1 = """Áp dụng hằng đẳng thức hiệu hai lập phương, ta có $x^3 - y^3 = (x - y)(x^2 + xy + y^2)$."""
    
    vd_da_1_d = '\\True Kết quả rút gọn cuối cùng của $D$ là $-\\frac{x^{%s} y^{%s}}{x^2 + xy + y^2}$.' % (p - 1, p - 1)
    vd_da_1_s = 'Kết quả rút gọn cuối cùng của $D$ là $\\frac{x^{%s} y^{%s}}{x^2 + xy + y^2}$.' % (p - 1, p - 1)
    loigiai_vd_1 = """Ta có $D = \\frac{y - x}{xy} \\cdot \\frac{x^{%s} y^{%s}}{(x - y)(x^2 + xy + y^2)} = -\\frac{x^{%s} y^{%s}}{x^2 + xy + y^2}$.""" % (p, p, p - 1, p - 1)
    
    vdc_da_1_d = '\\True Tại $x = 2, y = 1$, giá trị của biểu thức $D$ bằng $-\\frac{%s}{7}$.' % (4**(p - 1))
    vdc_da_1_s = 'Tại $x = 2, y = 1$, giá trị của biểu thức $D$ bằng $\\frac{%s}{7}$.' % (4**(p - 1))
    loigiai_vdc_1 = """Thay $x = 2, y = 1$ vào $D = -\\frac{x^{%s} y^{%s}}{x^2 + xy + y^2}$, ta được $D = -\\frac{2^{%s} \\cdot 1^{%s}}{2^2 + 2 \\cdot 1 + 1^2} = -\\frac{%s}{7}$.""" % (
        p - 1, p - 1, p - 1, p - 1, 4**(p - 1)
    )
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho biểu thức $D = \\left(\\frac{x + y}{xy} - \\frac{2}{x}\\right) \\cdot \\frac{x^{%s} y^{%s}}{x^3 - y^3}$ với $x \\neq 0, y \\neq 0, x \\neq y$. Xét tính đúng sai của các khẳng định sau:"""
                     % (p, p))
                     
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
