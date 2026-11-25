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


def bt_dang18_p3_b2_c6_ds8(self):
    # Dạng 18: Chuyển động đường bộ có thời gian nghỉ - Tính tổng thời gian hành trình
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        v1 = random.choice([40, 45, 50])
        dv = 15 if v1 == 45 else 10
        v2 = v1 + dv
        t1_int = 2
        t2_int = random.choice([2, 3])
        s1 = v1 * t1_int
        s2 = v2 * t2_int
        s_tong = s1 + s2
        nghi_phut = random.choice([15, 30])
        t_nghi = Decimal(nghi_phut) / Decimal(60)
        tong_tg = (Decimal(t1_int + t2_int) + t_nghi).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
        t_nghi_str = str(t_nghi.normalize()).replace('.', ',')
        kq_str = str(tong_tg).replace('.', ',')

        noidungcauhoi = ('Lúc $6$ giờ $30$ phút sáng, một ô tô xuất phát từ tỉnh A đi đến tỉnh B cách nhau $%s\\text{ km}$. Khi đi được $%s\\text{ km}$ đầu tiên với vận tốc $x\\ (\\text{km/h})$, xe dừng lại nghỉ $%s$ phút. Sau đó xe tiếp tục đi quãng đường còn lại với vận tốc tăng thêm $%s\\text{ km/h}$. Nếu vận tốc trên $%s\\text{ km}$ đầu là $%s\\text{ km/h}$ thì tổng thời gian kể từ lúc xuất phát đến khi xe tới tỉnh B là bao nhiêu giờ? (Viết kết quả dưới dạng số thập phân).' % (s_tong, s1, nghi_phut, dv, s1, v1))

        loigiai = ('Phân thức biểu thị thời gian xe chạy trên $%s\\text{ km}$ đầu tiên là $\\dfrac{%s}{x}$ (giờ).\\\n'
                   'Quãng đường còn lại dài $%s - %s = %s\\text{ km}$ nên phân thức biểu thị thời gian chạy trên quãng đường còn lại là $\\dfrac{%s}{x + %s}$ (giờ).\\\n'
                   'Đổi $%s$ phút $= %s$ giờ. Với $x = %s\\text{ km/h}$, tổng thời gian từ lúc xuất phát đến khi tới tỉnh B là:\\\n'
                   '$\\dfrac{%s}{%s} + %s + \\dfrac{%s}{%s + %s} = %s + %s + %s = %s$ (giờ).'
                   % (s1, s1, s_tong, s1, s2, s2, dv, nghi_phut, t_nghi_str, v1, s1, v1, t_nghi_str, s2, v1, dv, t1_int, t_nghi_str, t2_int, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
