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


def bt_dang5_p3_b1_c6_ds8(self):
    # Dạng 5: Tính giá trị của phân thức hai biến x, y khi biết tỉ số x/y
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([2, 3, 4])
        # Tử: 2x^2 - 3xy + y^2; Mẫu: x^2 + xy - 2y^2
        # Với x = k*y: Tử = (2k^2 - 3k + 1)y^2; Mẫu = (k^2 + k - 2)y^2
        # Rút gọn (k-1): (2k - 1)/(k + 2). Chọn c1, c2 sao cho kết quả nguyên đẹp
        # Ta đặt M = (m * (x^2 + xy - 2y^2) + (x - k*y)*(x + y)) / (x^2 + xy - 2y^2)
        m_ans = random.choice([2, 3, 4, 5])
        a_tu = m_ans + 1
        b_tu = m_ans + 1 - k
        c_tu = -2 * m_ans - k
        
        dau_b = '+' if b_tu >= 0 else '-'
        abs_b = abs(b_tu)
        str_b = 'xy' if abs_b == 1 else '%sxy' % abs_b
        dau_c = '+' if c_tu >= 0 else '-'
        abs_c = abs(c_tu)
        str_c = 'y^2' if abs_c == 1 else '%sy^2' % abs_c
        
        tu_val = a_tu * (k**2) + b_tu * k + c_tu
        mau_val = k**2 + k - 2
        kq_str = str(m_ans)
        
        noidungcauhoi = ('Cho các số thực $x, y \\neq 0$ thỏa mãn $\\dfrac{x}{y} = %s$. Tính giá trị của phân thức $M = \\dfrac{%sx^2 %s %s %s %s}{x^2 + xy - 2y^2}$.'
                         % (k, a_tu, dau_b, str_b, dau_c, str_c))
        
        loigiai = ('Từ giả thiết $\\dfrac{x}{y} = %s$ ($y \\neq 0$), suy ra $x = %sy$.\\\n'
                   'Thay $x = %sy$ vào phân thức $M$, ta được:\\\n'
                   '$M = \\dfrac{%s(%sy)^2 %s %s(%sy)y %s %s}{(%sy)^2 + (%sy)y - 2y^2} = \\dfrac{%sy^2}{%sy^2} = %s$.'
                   % (k, k, k, a_tu, k, dau_b, abs_b, k, dau_c, str_c, k, k, tu_val, mau_val, m_ans))
        
        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
