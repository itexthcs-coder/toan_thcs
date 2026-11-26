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


def bt_dang16_p1_b2_c7_ds8(self):
    # Dạng 16: Bài toán pha trộn hai dung dịch cùng loại có nồng độ khác nhau
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # c1*x + c2*m2 = c_mix*(x + m2) -> (c2 - c_mix)*m2 = (c_mix - c1)*x
        c1, c2, c_mix, m2, x_ans = random.choice([
            (10, 25, 15, 200, 400),   # 0.1*400 + 0.25*200 = 40 + 50 = 90 = 0.15*600
            (10, 40, 20, 150, 300),   # 0.1*300 + 0.4*150 = 30 + 60 = 90 = 0.2*450
            (15, 30, 20, 100, 200),   # 0.15*200 + 0.3*100 = 30 + 30 = 60 = 0.2*300
            (20, 50, 30, 100, 200)    # 0.2*200 + 0.5*100 = 40 + 50 = 90 = 0.3*300
        ])
        c1_tp = c1 / 100
        c2_tp = c2 / 100
        cm_tp = c_mix / 100
        
        str_c1 = str(c1_tp).replace('.', ',')
        str_c2 = str(c2_tp).replace('.', ',')
        str_cm = str(cm_tp).replace('.', ',')
        muoi_2 = int(round(c2_tp * m2))
        muoi_m = int(round(cm_tp * m2))
        hieu_c = str(round(cm_tp - c1_tp, 2)).replace('.', ',')

        noidungcauhoi = "Cần trộn bao nhiêu gam dung dịch muối ăn nồng độ $%s\\%%$ với $%s\\text{ g}$ dung dịch muối ăn nồng độ $%s\\%%$ để thu được dung dịch mới có nồng độ $%s\\%%$?" % (c1, m2, c2, c_mix)
        da = "$%s\\text{ g}$" % x_ans
        s = [
            "$%s\\text{ g}$" % (x_ans - 100),
            "$%s\\text{ g}$" % (x_ans + 100),
            "$%s\\text{ g}$" % m2
        ]
        loigiai = "Gọi $x$ ($\\text{g}$) là khối lượng dung dịch muối ăn nồng độ $%s\\%%$ cần lấy ($x > 0$).\\\\Khối lượng muối nguyên chất trong $x$ ($\\text{g}$) dung dịch $%s\\%%$ là $%sx$ ($\\text{g}$).\\\\Khối lượng muối nguyên chất trong $%s\\text{ g}$ dung dịch $%s\\%%$ là $%s \\cdot %s = %s$ ($\\text{g}$).\\\\Khối lượng dung dịch mới thu được là $x + %s$ ($\\text{g}$) và chứa $%s(x + %s)$ ($\\text{g}$) muối nguyên chất.\\\\Theo đề bài, ta có phương trình:\\\\$%sx + %s = %s(x + %s)$\\\\$%sx + %s = %sx + %s$\\\\$%sx = %s$\\\\$x = %s$ (thỏa mãn điều kiện).\\\\Vậy cần lấy $%s\\text{ g}$ dung dịch muối ăn nồng độ $%s\\%%$." % (
            c1, c1, str_c1, m2, c2, str_c2, m2, muoi_2, m2, str_cm, m2,
            str_c1, muoi_2, str_cm, m2,
            str_c1, muoi_2, str_cm, muoi_m,
            hieu_c, muoi_2 - muoi_m, x_ans, x_ans, c1
        )

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    da_d = ('\\True ' + str(da))
    list_1 = [da_d, str(das1), str(das2), str(das3)]
    random.shuffle(list_1)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
