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


def bt_dang2_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        von = random.choice([100, 200, 250, 400, 500])
        lai_suat = random.choice([5, 6, 7, 8, 9])
        r_dec = Decimal(lai_suat) / Decimal(100)
        he_so = Decimal(1) + r_dec
        tong_tien = Decimal(von) * (he_so ** 2)
        ti_so = he_so ** 2
        tong_tien_str = str(tong_tien.normalize()).replace('.', ',')
        ti_so_str = str(ti_so.normalize()).replace('.', ',')
        he_so_str = str(he_so.normalize()).replace('.', ',')
        r_str = str(r_dec.normalize()).replace('.', ',')

        noidungcauhoi = ('''Chú Hùng gửi $%s$ triệu đồng vào ngân hàng với kì hạn $12$ tháng theo thể thức lãi kép. Sau năm thứ nhất, chú không rút tiền ra mà tiếp tục gửi thêm $12$ tháng nữa với lãi suất như cũ. Sau $2$ năm, chú Hùng nhận được cả vốn lẫn lãi là $%s$ triệu đồng. Hỏi lãi suất gửi tiết kiệm của ngân hàng là bao nhiêu phần trăm một năm?'''
                         % (str(von), tong_tien_str))

        loigiai = ('''Gọi lãi suất gửi tiết kiệm của ngân hàng là $x\\%%$ một năm. Điều kiện: $x > 0$.\\\\
                   Sau kì gửi thứ nhất ($12$ tháng), số tiền cả vốn lẫn lãi chú Hùng có được là:\\\\
                   $%s + %s \\cdot \\dfrac{x}{100} = %s\\left(1 + \\dfrac{x}{100}\\right)$ (triệu đồng).\\\\
                   Sau kì gửi thứ hai ($12$ tháng tiếp theo), số tiền cả vốn lẫn lãi chú Hùng nhận được là:\\\\
                   $%s\\left(1 + \\dfrac{x}{100}\\right) + %s\\left(1 + \\dfrac{x}{100}\\right) \\cdot \\dfrac{x}{100} = %s\\left(1 + \\dfrac{x}{100}\\right)^2$ (triệu đồng).\\\\
                   Theo đề bài, ta có phương trình:\\\\
                   $%s\\left(1 + \\dfrac{x}{100}\\right)^2 = %s$ hay $\\left(1 + \\dfrac{x}{100}\\right)^2 = %s$.\\\\
                   Vì $x > 0$ nên $1 + \\dfrac{x}{100} > 1$, suy ra $1 + \\dfrac{x}{100} = %s \\Leftrightarrow \\dfrac{x}{100} = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy lãi suất gửi tiết kiệm của ngân hàng là $%s\\%%$ một năm.'''
                   % (str(von), str(von), str(von),
                      str(von), str(von), str(von),
                      str(von), tong_tien_str, ti_so_str,
                      he_so_str, r_str, str(lai_suat), str(lai_suat)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(lai_suat))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
