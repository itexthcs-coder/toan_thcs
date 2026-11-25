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


def bt_dang16_p3_b1_c6_ds8(self):
    # Dạng 16: Bài toán chuyển động đường bộ nhiều chặng (tính tổng thời gian hành trình từ phân thức)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (25, 6, 4, 15, 4, 6, 10, '2,75'), # 6/6 + 4/16 + 15/10 = 1 + 0,25 + 1,5 = 2,75
            (36, 9, 5, 22, 3, 8, 12, '3,25'), # 9/9 + 5/20 + 22/11 -> chỉnh 22 thành 24: S=38, 24/12=2 -> 1+0,25+2=3,25
            (30, 8, 6, 16, 4, 4, 8, '4,5')    # 8/4 + 6/12 + 16/8 = 2 + 0,5 + 2 = 4,5
        ]
        S_all, s1, s2, s3, dv1, dv2, x_val, ans_str = random.choice(scenarios)
        if S_all == 36:
            S_all = 38
            s3 = 24
            
        t1 = Fraction(s1, x_val - dv1)
        t2 = Fraction(s2, x_val + dv2)
        t3 = Fraction(s3, x_val)
        
        def fmt_f(fr):
            if fr.denominator == 1:
                return str(fr.numerator)
            return str(float(fr)).replace('.', ',')
            
        noidungcauhoi = ('Trong một giải chạy địa hình cự li $%s\\text{ km}$, vận động viên phải vượt qua ba chặng: $%s\\text{ km}$ đường dốc lên, $%s\\text{ km}$ đường dốc xuống và $%s\\text{ km}$ đường bằng. Biết vận tốc chạy trên đường bằng là $x\\text{ (km/h)}$ ($x > %s$), vận tốc khi lên dốc kém vận tốc đường bằng $%s\\text{ km/h}$ và vận tốc khi xuống dốc hơn vận tốc đường bằng $%s\\text{ km/h}$. Nếu vận tốc trên đường bằng của một vận động viên là $%s\\text{ km/h}$, hãy tính tổng thời gian (tính theo giờ) để người đó hoàn thành toàn bộ cuộc đua.'
                         % (S_all, s1, s2, s3, dv1, dv1, dv2, x_val))
        
        loigiai = ('Vận tốc khi lên dốc là $x - %s\\text{ (km/h)}$, vận tốc khi xuống dốc là $x + %s\\text{ (km/h)}$.\\\n'
                   'Phân thức biểu thị tổng thời gian hoàn thành ba chặng đua là:\\\n'
                   '$T = \\dfrac{%s}{x - %s} + \\dfrac{%s}{x + %s} + \\dfrac{%s}{x}$ (giờ).\\\n'
                   'Thay $x = %s$ vào biểu thức trên, ta được tổng thời gian hoàn thành cuộc đua là:\\\n'
                   '$T = \\dfrac{%s}{%s - %s} + \\dfrac{%s}{%s + %s} + \\dfrac{%s}{%s} = %s + %s + %s = %s$ (giờ).'
                   % (dv1, dv2, s1, dv1, s2, dv2, s3, x_val,
                      s1, x_val, dv1, s2, x_val, dv2, s3, x_val,
                      fmt_f(t1), fmt_f(t2), fmt_f(t3), ans_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % ans_str

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
