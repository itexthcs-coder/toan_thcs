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


def bt_dang20_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        von = 800
        gia_cu = 1000
        sl_cu = 100
        x_lan = random.choice([10, 15])
        x_ans = 10 * x_lan
        gia_moi = gia_cu + x_ans
        loi_nhuan = (gia_moi - von) * (sl_cu - 2 * x_lan)
        c_s = 5 * (loi_nhuan - 20000)
        delta_p = 150**2 - c_s
        sqrt_dp = int(math.isqrt(delta_p))
        x1 = 150 - sqrt_dp
        x2 = 150 + sqrt_dp

        noidungcauhoi = ('''Một cửa hàng nhập về một loại đồng hồ thông minh với giá vốn $%s$ nghìn đồng/chiếc. Nếu bán với giá $%s$ nghìn đồng/chiếc thì mỗi tháng bán được $%s$ chiếc. Khảo sát thị trường cho thấy cứ tăng giá bán thêm $10$ nghìn đồng/chiếc thì số lượng bán ra giảm đi $2$ chiếc. Hỏi cửa hàng cần bán mỗi chiếc đồng hồ với giá bao nhiêu nghìn đồng (chọn mức giá thấp hơn) để đạt tổng lợi nhuận trong tháng là $%s$ nghìn đồng?'''
                         % (str(von), str(gia_cu), str(sl_cu), str(loi_nhuan)))

        loigiai = ('''Gọi số tiền cần tăng thêm so với giá bán cũ là $x$ (nghìn đồng). Điều kiện: $0 < x < 500$.\\\\
                   Khi đó, giá bán mới của mỗi chiếc đồng hồ là $%s + x$ (nghìn đồng), lợi nhuận thu được trên mỗi chiếc là $(%s + x) - %s = 200 + x$ (nghìn đồng).\\\\
                   Cứ tăng giá $10$ nghìn đồng thì số lượng bán ra giảm $2$ chiếc, tức là tăng $1$ nghìn đồng thì giảm $0,2$ chiếc. Do đó số lượng bán ra giảm đi $0,2x$ chiếc, còn lại $%s - 0,2x$ (chiếc).\\\\
                   Theo đề bài, tổng lợi nhuận trong tháng đạt $%s$ nghìn đồng nên ta có phương trình:\\\\
                   $(200 + x)(%s - 0,2x) = %s$\\\\
                   $20\\,000 + 60x - 0,2x^2 = %s$\\\\
                   $0,2x^2 - 60x + %s = 0$ hay $x^2 - 300x + %s = 0$.\\\\
                   Ta có: $\\Delta' = (-150)^2 - 1 \\cdot %s = %s$; $\\sqrt{\\Delta'} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = 150 - %s = %s$ (thỏa mãn điều kiện); $x_2 = 150 + %s = %s$ (thỏa mãn điều kiện).\\\\
                   Để chọn mức giá bán thấp hơn, ta nhận $x = %s$.\\\\
                   Vậy cửa hàng cần bán mỗi chiếc đồng hồ với giá là $%s + %s = %s$ nghìn đồng.'''
                   % (str(gia_cu), str(gia_cu), str(von), str(sl_cu), str(loi_nhuan),
                      str(sl_cu), str(loi_nhuan), str(loi_nhuan),
                      str(loi_nhuan - 20000), str(c_s),
                      str(c_s), str(delta_p), str(sqrt_dp),
                      str(sqrt_dp), str(x1), str(sqrt_dp), str(x2),
                      str(x1), str(gia_cu), str(x1), str(gia_moi)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(gia_moi))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
