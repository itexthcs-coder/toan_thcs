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


def bt_dang18_p4_b5_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v = symbols('v')
        he_so_v = random.choice([4, 5])
        t_A = random.choice([12, 15])
        S_A_coef = he_so_v * t_A

        ti_so = Rational(random.choice([4, 5, 6]), 3)
        t_B = int(S_A_coef * ti_so)

        noidungcauhoi = ('''Trong một buổi thử nghiệm xe tự hành, xe A chạy nhanh gấp $%s$ lần xe B. Tuy nhiên, sau khi chạy được $%s$ phút, xe A gặp sự cố kỹ thuật nên dừng lại, trong khi xe B vẫn tiếp tục chạy đều trong $%s$ phút để hoàn thành chặng đường. Gọi $v$ ($\\text{m/phút}$) là vận tốc chạy của xe B ($v > 0$). \\\\
                         a) Viết các đơn thức biểu thị quãng đường mà xe A và xe B đã chạy được. \\\\
                         b) Hỏi quãng đường xe B chạy được dài gấp bao nhiêu lần quãng đường xe A đã chạy?'''
                         % (he_so_v, t_A, t_B))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vận tốc của xe A là $%sv$ ($\\text{m/phút}$). \\\\
                        Đơn thức biểu thị quãng đường xe A đã chạy được là:
                        \\begin{align*}
                        S_{A} = %sv \\cdot %s = %sv \\,\\, (\\text{m}).
                        \\end{align*}
                        Đơn thức biểu thị quãng đường xe B đã chạy được là:
                        \\begin{align*}
                        S_{B} = v \\cdot %s = %sv \\,\\, (\\text{m}).
                        \\end{align*}
                        \\item Quãng đường xe B chạy được dài gấp số lần quãng đường xe A đã chạy là:
                        \\begin{align*}
                        (%sv) : (%sv) = %s \\,\\, (\\text{lần}).
                        \\end{align*}
                        \\end{enumEX}'''
                   % (he_so_v, he_so_v, t_A, S_A_coef, t_B, t_B,
                      t_B, S_A_coef, latex(ti_so)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
