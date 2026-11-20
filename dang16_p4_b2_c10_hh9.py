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


def bt_dang16_p4_b2_c10_hh9(self):
    d = random.choice([2, 3, 4])
    R = d / 2
    R_str = str(R).replace('.', ',') if d % 2 != 0 else str(int(R))
    V_yeucau = random.choice([20, 25, 30, 35]) # m^3
    V_cau = (4 / 3) * math.pi * (R**3)
    h_tru = (V_yeucau - V_cau) / (math.pi * (R**2))
    h_round = Decimal(str(h_tru)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    h_str = str(h_round).replace('.', ',')
    L_tong = Decimal(str(float(h_round) + d)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    L_str = str(L_tong).replace('.', ',')

    noidungcauhoi = ('''Một công ty năng lượng cần thiết kế một bồn chứa khí hóa lỏng có dạng gồm một thân hình trụ ở giữa và hai nắp ở hai đầu là hai nửa hình cầu có cùng đường kính bằng $%s\\text{ m}$. Biết dung tích thiết kế của bồn chứa là $%s\\text{ m}^3$ (bỏ qua độ dày thành bồn).\\\na) Tính tổng thể tích của hai nắp dạng nửa hình cầu ở hai đầu bồn chứa (làm tròn đến hàng phần trăm của $\\text{m}^3$).\\\nb) Tính chiều dài $h$ của phần thân hình trụ ở giữa (làm tròn đến hàng phần trăm của $\\text{m}$).\\\nc) Tính tổng chiều dài toàn bộ của bồn chứa khí đó.'''
                     % (d, V_yeucau))

    V_cau_round = Decimal(str(V_cau)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    V_cau_str = str(V_cau_round).replace('.', ',')

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính của hai nửa hình cầu (cũng là bán kính đáy thân trụ) là: $R = \\dfrac{%s}{2} = %s\\text{ (m)}$.\\\nHai nắp dạng nửa hình cầu ghép lại tạo thành một hình cầu bán kính $R = %s\\text{ m}$, có thể tích là:
$$V_{\\text{cầu}} = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot (%s)^3 \\approx %s\\text{ (m}^3\\text{)}.$$
\\item Thể tích phần thân hình trụ cần đạt là: $V_{\\text{trụ}} = V - V_{\\text{cầu}} \\approx %s - %s = %s\\text{ (m}^3\\text{)}$.\\\nChiều dài phần thân hình trụ là:
$$h = \\dfrac{V_{\\text{trụ}}}{\\pi R^2} \\approx \\dfrac{%s}{\\pi \\cdot (%s)^2} \\approx %s\\text{ (m)}.$$
\\item Tổng chiều dài toàn bộ của bồn chứa khí là:
$$L = h + 2R \\approx %s + %s = %s\\text{ (m)}.$$
\\end{enumEX}'''
               % (d, R_str, R_str, R_str, V_cau_str, V_yeucau, V_cau_str, str(Decimal(str(V_yeucau)) - V_cau_round).replace('.', ','), str(Decimal(str(V_yeucau)) - V_cau_round).replace('.', ','), R_str, h_str, h_str, d, L_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
