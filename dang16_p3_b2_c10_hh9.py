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


def bt_dang16_p3_b2_c10_hh9(self):
    d = random.choice([1.4, 1.6, 1.8, 2.0])
    h = random.choice([3.0, 3.5, 4.0, 4.2])
    R = d / 2
    # S_tp = S_xq_tru + S_cau = 2*pi*R*h + 4*pi*R^2 = pi * d * (h + d)
    S_exact = math.pi * d * (h + d)
    S_round = Decimal(str(S_exact)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    kq_str = str(S_round).replace('.', ',')

    def fmt(val):
        return str(val).replace('.', ',')

    noidungcauhoi = ('''Một xưởng cơ khí chế tạo một bồn chứa nhiên liệu kín có dạng gồm một thân hình trụ chiều dài $h = %s\\text{ m}$ và hai nắp ở hai đầu là hai nửa hình cầu có đường kính bằng đường kính đáy hình trụ và bằng $%s\\text{ m}$. Tính diện tích thép tấm tối thiểu cần dùng để làm vỏ bồn chứa đó (coi các mối hàn không đáng kể, làm tròn kết quả đến hàng phần trăm của $\\text{m}^2$).'''
                     % (fmt(h), fmt(d)))

    loigiai = ('''Bán kính đáy của phần hình trụ và bán kính của hai nửa hình cầu là: $R = \\dfrac{%s}{2} = %s\\text{ (m)}$.\\\nHai nắp dạng nửa hình cầu ghép lại có diện tích bằng diện tích một mặt cầu bán kính $R = %s\\text{ m}$:
$$S_{\\text{cầu}} = 4\\pi R^2 = 4\\pi \\cdot (%s)^2 = %s\\pi\\text{ (m}^2\\text{)}.$$
Diện tích xung quanh của phần thân hình trụ là:
$$S_{\\text{trụ}} = 2\\pi R h = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (m}^2\\text{)}.$$
Tổng diện tích thép tấm tối thiểu cần dùng là:
$$S = S_{\\text{cầu}} + S_{\\text{trụ}} = %s\\pi + %s\\pi \\approx %s\\text{ (m}^2\\text{)}.$$'''
               % (fmt(d), fmt(R), fmt(R), fmt(R), fmt(round(4 * (R**2), 4)), fmt(R), fmt(h), fmt(round(2 * R * h, 4)), fmt(round(4 * (R**2), 4)), fmt(round(2 * R * h, 4)), kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
