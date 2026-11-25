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


def bt_dang16_p4_b1_c6_ds8(self):
    # Dạng 16: Bài toán chuyển động đường bộ có thời gian nghỉ giữa chặng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (180, 100, 30, 20, 80, '3\\text{ giờ } 5\\text{ phút}'),  # 100/80 + 0,5 + 80/60 = 1,25 + 0,5 + 4/3 = 37/12 h = 3h 5p
            (210, 120, 30, 15, 60, '4\text{ giờ } 30\\text{ phút}'), # 120/60 + 0,5 + 90/45 = 2 + 0,5 + 2 = 4,5 h = 4h 30p
            (150, 90, 15, 15, 60, '3\\text{ giờ } 15\\text{ phút}')   # 90/60 + 0,25 + 60/45 -> đổi: (150, 90, 30, 15, 60, '3\text{ giờ } 20\text{ phút}') -> 1,5 + 0,5 + 4/3 = 10/3 h = 3h 20p
        ]
        S_ab, s_ct, phut_nghi, dv, x_val, tong_tg_str = random.choice(scenarios)
        if S_ab == 150:
            phut_nghi = 30
            tong_tg_str = '3\\text{ giờ } 20\\text{ phút}'
        s_ql = S_ab - s_ct
        
        noidungcauhoi = ('Một xe khách xuất phát từ tỉnh $A$ đến tỉnh $B$ cách nhau $%s\\text{ km}$. Trong $%s\\text{ km}$ đầu tiên trên đường cao tốc, xe chạy với vận tốc trung bình $x\\text{ (km/h)}$ ($x > %s$). Sau đó xe dừng nghỉ $%s\\text{ phút}$ tại trạm dừng chân rồi tiếp tục đi nốt quãng đường còn lại trên quốc lộ với vận tốc giảm đi $%s\\text{ km/h}$ so với trên đường cao tốc.\\\\'
                         'a) Viết các phân thức biểu thị thời gian xe chạy trên đường cao tốc và thời gian xe chạy trên quốc lộ.\\\\'
                         'b) Tính tổng thời gian kể từ lúc xe xuất phát tại $A$ đến khi tới $B$ (bao gồm cả thời gian nghỉ) nếu vận tốc xe trên đường cao tốc là $%s\\text{ km/h}$.'
                         % (S_ab, s_ct, dv, phut_nghi, dv, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Phân thức biểu thị thời gian xe chạy hết $%s\\text{ km}$ đường cao tốc với vận tốc $x\\text{ (km/h)}$ là $\\dfrac{%s}{x}$ (giờ).\\\\'
                   'Quãng đường quốc lộ còn lại dài $%s - %s = %s\\text{ (km)}$, vận tốc trên quốc lộ là $x - %s\\text{ (km/h)}$ nên phân thức biểu thị thời gian xe chạy trên quốc lộ là $\\dfrac{%s}{x - %s}$ (giờ).\n'
                   '\\item Đổi $%s\\text{ phút} = 0,5\\text{ giờ}$. Thay $x = %s$ vào các phân thức trên, tổng thời gian kể từ lúc xe xuất phát tại $A$ đến khi tới $B$ là:\\\\'
                   '$T = \\dfrac{%s}{%s} + 0,5 + \\dfrac{%s}{%s - %s} = %s$ ($%s$).\n'
                   '\\end{enumEX}'
                   % (s_ct, s_ct, S_ab, s_ct, s_ql, dv, s_ql, dv,
                      phut_nghi, x_val, s_ct, x_val, s_ql, x_val, dv,
                      str(Fraction(s_ct, x_val) + Fraction(1, 2) + Fraction(s_ql, x_val - dv)).replace('/', '\\dfrac{', 1) if False else '\\dfrac{%s}{%s}\\text{ giờ}' % (
                          (Fraction(s_ct, x_val) + Fraction(1, 2) + Fraction(s_ql, x_val - dv)).numerator,
                          (Fraction(s_ct, x_val) + Fraction(1, 2) + Fraction(s_ql, x_val - dv)).denominator
                      ), tong_tg_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
