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


def bt_dang20_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r_cm = random.choice([30, 40, 50])
        r_m = Rational(r_cm, 100)
        r_dec = Decimal(str(float(r_m))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
        r_str = str(r_dec).replace('.', ',')
        om = randint(3, 6)
        sin_val = float(r_m) / om
        goc_amo = math.degrees(math.asin(sin_val))
        goc_amb = 2 * goc_amo
        goc_amo_dec = Decimal(str(goc_amo)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        goc_amb_dec = Decimal(str(goc_amb)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        goc_amo_str = str(goc_amo_dec).replace('.', ',')
        goc_amb_str = str(goc_amb_dec)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tại một khúc cua khuất tầm nhìn, người ta đặt một gương cầu lồi có mặt cắt ngang là cung tròn tâm $O$, bán kính $R = %s\\text{ m}$. Hai tia sáng giới hạn vùng quan sát từ mắt người lái xe tại điểm $M$ tới hai mép gương tiếp xúc với mặt gương lần lượt tại $A$ và $B$. Biết khoảng cách từ mắt người lái xe đến tâm gương là $MO = %s\\text{ m}$. Tính góc mở $\\widehat{AMB}$ của chùm tia tiếp tuyến giới hạn vùng quan sát (làm tròn kết quả đến độ). \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate (M) at (-4,0);
            \\coordinate (A) at (-0.64,1.46);
            \\coordinate (B) at (-0.64,-1.46);
            \\draw[line width=1pt] (A) arc (113.6:246.4:1.6);
            \\draw[line width=1pt] (M)--(A) (M)--(B);
            \\draw[line width=1pt, dashed] (M)--(O) (O)--(A) (O)--(B);
            \\fill (O) circle (1pt) node[right] {$O$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
        \\end{tikzpicture}
        \\end{center}'''
        %(r_str, latex(om)))

        # Nội dung lời giải
        loigiai = ('''Vì hai tia sáng $MA$ và $MB$ tiếp xúc với cung tròn mặt gương $(O; %s\\text{ m})$ lần lượt tại $A$ và $B$ nên $MA$ và $MB$ là hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $M$. \\\\
        Theo tính chất của hai tiếp tuyến cắt nhau, ta có $\\widehat{OAM} = 90^\\circ$ và $MO$ là tia phân giác của góc $\\widehat{AMB}$. \\\\
        Xét tam giác $OAM$ vuông tại $A$ ($OA = R = %s\\text{ m}$, $OM = %s\\text{ m}$), ta có: \\\\
        $\\sin \\widehat{AMO} = \\dfrac{OA}{OM} = \\dfrac{%s}{%s} \\Rightarrow \\widehat{AMO} \\approx %s^\\circ$. \\\\
        Vậy góc mở $\\widehat{AMB}$ của chùm tia tiếp tuyến giới hạn vùng quan sát là: \\\\
        $\\widehat{AMB} = 2\\widehat{AMO} \\approx 2 \\cdot %s^\\circ \\approx %s^\\circ$.'''
        %(r_str, r_str, latex(om), r_str, latex(om), goc_amo_str, goc_amo_str, goc_amb_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
