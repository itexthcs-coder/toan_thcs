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


def bt_dang17_p4_b1_c1_ds8(self):
    # Dạng 17: Ứng dụng cộng đơn thức đồng dạng giải bài toán chi phí quà từ thiện theo hai cách
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gia_vo = random.choice(['7,5', '8,5', '9,5'])
        gia_but = random.choice(['3,5', '4,5', '5,5'])
        tong_1 = int(Rational(gia_vo.replace(',', '.')) + Rational(gia_but.replace(',', '.')))
        x0 = random.choice([4, 5, 6])
        y0 = random.choice([30, 40, 50])
        tong_tien = tong_1 * x0 * y0

        noidungcauhoi = ('Một câu lạc bộ tình nguyện chuẩn bị $y$ phần quà gửi tặng các em học sinh vùng cao. Mỗi phần quà gồm $x$ quyển vở (giá $%s\\text{ nghìn đồng/quyển}$) và $x$ chiếc bút bi (giá $%s\\text{ nghìn đồng/chiếc}$). \\\\\n'
                         'a) Viết đơn thức thu gọn biểu thị tổng số tiền (nghìn đồng) mua toàn bộ $y$ phần quà theo hai cách lập luận khác nhau. \\\\\n'
                         'b) Nếu câu lạc bộ chuẩn bị $y = %s$ phần quà, mỗi phần gồm $x = %s$ quyển vở và $%s$ chiếc bút bi thì tổng chi phí là bao nhiêu nghìn đồng?'
                         % (gia_vo, gia_but, y0, x0, x0))

        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item \\textbf{Cách 1:} Tổng tiền mua vở trong $y$ phần quà là $%sxy$ (nghìn đồng), tổng tiền mua bút bi là $%sxy$ (nghìn đồng). Do đó tổng chi phí là:\n'
                   '\\begin{align*}\n'
                   'T = %sxy + %sxy = (%s + %s)xy = %sxy\\text{ (nghìn đồng)}.\n'
                   '\\end{align*}\n'
                   '\\textbf{Cách 2:} Giá tiền mỗi phần quà là $%sx + %sx = %sx$ (nghìn đồng), do đó $y$ phần quà có tổng giá trị là:\n'
                   '\\begin{align*}\n'
                   'T = %sx \\cdot y = %sxy\\text{ (nghìn đồng)}.\n'
                   '\\end{align*} \n'
                   '\\item Thay $x = %s$ và $y = %s$ vào $T = %sxy$, ta được tổng chi phí là:\n'
                   '\\begin{align*}\n'
                   'T = %s \\cdot %s \\cdot %s = %s\\text{ (nghìn đồng)}.\n'
                   '\\end{align*} \n'
                   '\\end{enumEX} \n'
                   % (gia_vo, gia_but, gia_vo, gia_but, gia_vo, gia_but, tong_1,
                      gia_vo, gia_but, tong_1, tong_1, tong_1,
                      x0, y0, tong_1, tong_1, x0, y0, tong_tien))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
