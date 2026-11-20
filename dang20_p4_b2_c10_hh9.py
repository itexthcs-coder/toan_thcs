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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p4_b2_c10_hh9(self):
    # V_nuacau = 2/3 * pi * R^3. Chọn R = 3 cm => V_nuacau = 18*pi cm^3; h_non = 4*R = 12 cm => l_non = sqrt(R^2 + h^2) = 3*sqrt(17)
    # Hoặc chọn R = 3 cm, h_non = 4 cm => V_nuacau = 18*pi, V_non = 12*pi => V_tong = 30*pi cm^3, l_non = 5 cm!
    k = random.choice([1, 2])
    R = 3 * k
    h_non = 4 * k
    l_non = 5 * k
    V_nuacau = (2 * R**3) // 3
    V_non = (R**2 * h_non) // 3
    V_tong = V_nuacau + V_non
    S_xq_non = R * l_non

    noidungcauhoi = ('''Một chiếc kem ốc quế gồm hai phần: phần vỏ bánh phía dưới có dạng hình nón chiều cao $h = %s\\text{ cm}$, phần kem phía trên có dạng nửa hình cầu đặt khít lên miệng vỏ bánh hình nón (có cùng bán kính đáy $R$). Biết thể tích phần kem nửa hình cầu phía trên bằng $%s\\pi\\text{ cm}^3$.\\\na) Tính bán kính $R$ của phần kem nửa hình cầu và đường kính miệng vỏ bánh hình nón.\\\nb) Tính tổng thể tích của cả chiếc kem ốc quế (tính theo $\\pi$).\\\nc) Người ta dùng một tờ giấy bạc hình quạt tròn vừa khít để bọc kín mặt xung quanh của chiếc vỏ bánh hình nón (bỏ qua mép dán). Tính diện tích tờ giấy bạc cần dùng (làm tròn đến hàng phần mười của $\\text{cm}^2$).'''
                     % (h_non, V_nuacau))

    S_giay_round = Decimal(str(S_xq_non * math.pi)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    S_giay_str = str(S_giay_round).replace('.', ',')

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $R$ ($\\text{cm}$) là bán kính của phần kem nửa hình cầu ($R > 0$).\\\nTa có thể tích nửa hình cầu là:
$$V_{\\text{trên}} = \\dfrac{1}{2} \\cdot \\dfrac{4}{3}\\pi R^3 = \\dfrac{2}{3}\\pi R^3 = %s\\pi \\Rightarrow R^3 = %s \\Rightarrow R = %s\\text{ (cm)}.$$
Đường kính miệng vỏ bánh hình nón là: $d = 2R = 2 \\cdot %s = %s\\text{ (cm)}$.
\\item Thể tích phần vỏ bánh hình nón phía dưới là:
$$V_{\\text{dưới}} = \\dfrac{1}{3}\\pi R^2 h = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Tổng thể tích của cả chiếc kem ốc quế là:
$$V = V_{\\text{trên}} + V_{\\text{dưới}} = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Độ dài đường sinh của vỏ bánh hình nón là: $l = \\sqrt{R^2 + h^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.\\\nDiện tích tờ giấy bạc cần dùng chính là diện tích xung quanh của hình nón:
$$S_{\\text{xq}} = \\pi R l = \\pi \\cdot %s \\cdot %s = %s\\pi \\approx %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
               % (V_nuacau, R**3, R, R, 2 * R, R, h_non, V_non, V_nuacau, V_non, V_tong, R, h_non, l_non, R, l_non, S_xq_non, S_giay_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
