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


def bt_dang17_p4_b2_c10_hh9(self):
    d = 4 # cm (đường kính chuẩn bóng bàn 40mm = 4cm)
    R = 2
    so_bong = random.choice([3, 4, 5])
    h_hop = so_bong * d
    S_tp_hop = 2 * math.pi * R * h_hop + 2 * math.pi * (R**2)
    S_tp_round = Decimal(str(S_tp_hop)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    S_tp_str = str(S_tp_round).replace('.', ',')
    V_hop = math.pi * (R**2) * h_hop
    V_bong = so_bong * (4 / 3) * math.pi * (R**3)
    V_trong = Decimal(str(V_hop - V_bong)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    V_trong_str = str(V_trong).replace('.', ',')

    noidungcauhoi = ('''Một ống đựng bóng bàn có dạng hình trụ chứa vừa khít $%s$ quả bóng bàn xếp thẳng đứng dọc theo trục của ống. Biết mỗi quả bóng bàn có dạng hình cầu với đường kính chuẩn bằng $4\\text{ cm}$ (bỏ qua độ dày vỏ ống).\\\na) Tính chiều cao và diện tích toàn phần của ống đựng bóng bàn (làm tròn kết quả diện tích đến hàng phần trăm của $\\text{cm}^2$).\\\nb) Tính thể tích phần không gian trống bên trong ống đựng bóng không bị các quả bóng chiếm chỗ (làm tròn đến hàng phần trăm của $\\text{cm}^3$).\\\nc) Chứng minh rằng tỉ lệ phần trăm thể tích không gian trống trong ống không phụ thuộc vào số lượng quả bóng xếp vừa khít trong ống.'''
                     % (so_bong))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính đáy ống hình trụ và bán kính mỗi quả bóng là $R = \\dfrac{4}{2} = 2\\text{ (cm)}$.\\\nChiều cao của ống đựng bóng là: $h = %s \\cdot 4 = %s\\text{ (cm)}$.\\\nDiện tích toàn phần của ống hình trụ (có cả hai nắp) là:
$$S_{\\text{tp}} = 2\\pi R h + 2\\pi R^2 = 2\\pi \\cdot 2 \\cdot %s + 2\\pi \\cdot 2^2 = %s\\pi \\approx %s\\text{ (cm}^2\\text{)}.$$
\\item Thể tích của ống hình trụ là: $V_{\\text{ống}} = \\pi R^2 h = \\pi \\cdot 2^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nTổng thể tích của $%s$ quả bóng bàn là: $V_{\\text{bóng}} = %s \\cdot \\dfrac{4}{3}\\pi \\cdot 2^3 = \\dfrac{%s\\pi}{3}\\text{ (cm}^3\\text{)}$.\\\nThể tích phần không gian trống trong ống là:
$$V_{\\text{trống}} = V_{\\text{ống}} - V_{\\text{bóng}} = %s\\pi - \\dfrac{%s\\pi}{3} = \\dfrac{%s\\pi}{3} \\approx %s\\text{ (cm}^3\\text{)}.$$
\\item Giả sử ống hình trụ chứa vừa khít $n$ quả bóng bàn bán kính $R$ ($n \\in \\mathbb{N}^*$), khi đó chiều cao ống là $h = 2nR$.\\\nTa có $V_{\\text{ống}} = \\pi R^2 (2nR) = 2n\\pi R^3$ và tổng thể tích $n$ quả bóng là $V_{\\text{bóng}} = n \\cdot \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}n\\pi R^3$.\\\nTỉ lệ phần trăm thể tích không gian trống trong ống là:
$$\\dfrac{V_{\\text{ống}} - V_{\\text{bóng}}}{V_{\\text{ống}}} \\cdot 100\\%% = \\dfrac{2n\\pi R^3 - \\dfrac{4}{3}n\\pi R^3}{2n\\pi R^3} \\cdot 100\\%% = \\dfrac{1}{3} \\cdot 100\\%% = 33,33\\%%,$$
không phụ thuộc vào số lượng quả bóng $n$.
\\end{enumEX}'''
               % (so_bong, h_hop, h_hop, 4 * h_hop + 8, S_tp_str, h_hop, 4 * h_hop, so_bong, so_bong, 32 * so_bong, 4 * h_hop, 32 * so_bong, 12 * h_hop - 32 * so_bong, V_trong_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
