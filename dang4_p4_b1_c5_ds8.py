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


def bt_dang4_p4_b1_c5_ds8(self):
    # Dạng 4: Làm sạch và phân tích dữ liệu khảo sát giấc ngủ học sinh
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            g1 = random.randint(70, 85)
            g2 = random.randint(70, 85)
            g3 = random.randint(70, 85)
            g4 = random.randint(70, 85)
            g5 = random.randint(70, 85)
            if len({g1, g2, g3, g4, g5}) >= 4 and (g1 + g2 + g3 + g4 + g5) % 5 == 0:
                break
        g_sai = random.randint(25, 31)
        g_sai_str = "%s,5" % g_sai
        thuc_sai = "%s,5" % random.choice([1, 2])

        def fmt1(v):
            s = str(Decimal(v) / Decimal(10)).replace('.', ',')
            if s.endswith(',0'):
                return s[:-2]
            return s

        d1_list = ["0", "1", "0", "2", thuc_sai, "1"]
        random.shuffle(d1_list)
        d1_str = ";\\; ".join(d1_list)

        d2_list = [fmt1(g1), fmt1(g2), fmt1(g3), g_sai_str, fmt1(g4), fmt1(g5)]
        random.shuffle(d2_list)
        d2_str = ";\\; ".join(d2_list)

        tb_ngu = Decimal(g1 + g2 + g3 + g4 + g5) / Decimal(50)
        tb_str = str(tb_ngu).replace('.', ',')
        if tb_str.endswith(',0'):
            tb_str = tb_str[:-2]

        noidungcauhoi = ('''Khảo sát tình hình giấc ngủ của $6$ bạn học sinh lớp $8C$, bạn tổ trưởng ghi lại hai dãy dữ liệu sau:\\\\
- \\textbf{Dãy 1} (Số lần thức giấc giữa đêm): $%s$.\\\\
- \\textbf{Dãy 2} (Tổng thời gian ngủ trong ngày, đơn vị: giờ): $%s$.\\\\
a) Phân loại hai dãy dữ liệu trên.\\\\
b) Chỉ ra các giá trị không hợp lí trong từng dãy dữ liệu, giải thích nguyên nhân và tính giá trị trung bình của các số liệu hợp lí ở Dãy $2$.'''
                         % (d1_str, d2_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Phân loại dữ liệu:\\\\
- Dãy $1$ (số lần thức giấc) thu được từ phép đếm nên thuộc loại \\textbf{số liệu rời rạc}.\\\\
- Dãy $2$ (tổng thời gian ngủ tính theo giờ) thu được từ phép đo thời gian nên thuộc loại \\textbf{số liệu liên tục}.
\\item Kiểm tra tính hợp lí và tính trung bình:\\\\
- Ở Dãy $1$, giá trị không hợp lí là $%s$ vì số lần thức giấc phải là một số tự nhiên, không thể là số thập phân.\\\\
- Ở Dãy $2$, giá trị không hợp lí là $%s$ vì một ngày chỉ có $24$ giờ nên tổng thời gian ngủ trong ngày không thể vượt quá $24$ giờ.\\\\
- Loại bỏ giá trị $%s$, năm số liệu hợp lí còn lại ở Dãy $2$ là $%s;\\; %s;\\; %s;\\; %s;\\; %s$. Giá trị trung bình của chúng là:
$$\\dfrac{%s + %s + %s + %s + %s}{5} = %s\\text{ (giờ)}.$$
\\end{enumEX}'''
                   % (thuc_sai, g_sai_str, g_sai_str,
                      fmt1(g1), fmt1(g2), fmt1(g3), fmt1(g4), fmt1(g5),
                      fmt1(g1), fmt1(g2), fmt1(g3), fmt1(g4), fmt1(g5), tb_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
