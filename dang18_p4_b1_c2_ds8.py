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

def bt_dang18_p4_b1_c2_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = random.choice([20, 30, 40])
        dai_str = '%s,5' % m
        rong_str = '%s,5' % (m - 1)
        dt_int = m**2 - 1
        dt_str = '%s,75' % dt_int
        don_gia = 400
        tong_tien_nghin = 400 * (m**2) - 100

        # Nội dung câu hỏi
        noidungcauhoi = ('''Sàn của một phòng hội nghị hình chữ nhật có chiều dài $%s\\text{ m}$ và chiều rộng $%s\\text{ m}$. Đơn giá thi công sàn gỗ trọn gói là $%s\\text{ nghìn đồng/m}^2$.\\\\
a) Vận dụng hằng đẳng thức hiệu hai bình phương để tính nhẩm diện tích sàn phòng hội nghị.\\\\
b) Tính tổng chi phí thi công sàn gỗ của phòng hội nghị đó (đơn vị: nghìn đồng).'''
                         % (dai_str, rong_str, latex(don_gia)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Áp dụng hằng đẳng thức hiệu hai bình phương, diện tích sàn phòng hội nghị là:
\\begin{align*}
S &= %s \\cdot %s = (%s + 0,5)(%s - 0,5) \\\\
  &= %s^2 - 0,5^2 = %s - 0,25 = %s\\text{ (m}^2).
\\end{align*} \n
\\item Tổng chi phí thi công sàn gỗ của phòng hội nghị là:
$$%s \\cdot %s = (%s - 0,25) \\cdot %s = %s - 100 = %s\\text{ (nghìn đồng)}.$$ \n
\\end{enumEX} \n'''
                   % (dai_str, rong_str, latex(m), latex(m),
                      latex(m), latex(m**2), dt_str,
                      dt_str, latex(don_gia), latex(m**2), latex(don_gia),
                      latex(400 * (m**2)), latex(tong_tien_nghin)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
