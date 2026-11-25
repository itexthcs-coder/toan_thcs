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


def bt_dang20_p3_b2_c5_ds8(self):
    # Dạng 20 (Vận dụng): Tìm số biểu tượng nguyên tối ưu khi cho phép dùng nửa biểu tượng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        half_k = random.choice([5, 6, 8, 9])
        k = 2 * half_k
        v6, v7, v8, v9 = 3 * half_k, 4 * half_k, 5 * half_k, 6 * half_k
        tong_nguyen = 8
        kq_str = str(tong_nguyen)
        
        noidungcauhoi = ("""Một trường THCS thống kê số học sinh đạt giải cấp thành phố của bốn khối lớp: Khối 6 có $%s$ em, Khối 7 có $%s$ em, Khối 8 có $%s$ em và Khối 9 có $%s$ em. Nếu vẽ biểu đồ tranh trong đó quy ước mỗi biểu tượng nguyên ứng với $k$ học sinh và mỗi nửa biểu tượng ứng với $\\dfrac{k}{2}$ học sinh (với $k$ là số nguyên dương chẵn lớn nhất có thể sao cho có ít nhất một khối dùng nửa biểu tượng), thì tổng số biểu tượng nguyên (không tính nửa biểu tượng) cần vẽ cho cả bốn khối là bao nhiêu?"""
                         % (v6, v7, v8, v9))
        
        loigiai = ("""Vì mỗi nửa biểu tượng ứng với $\\dfrac{k}{2}$ học sinh nên để biểu diễn chính xác cả bốn số liệu mà không phải chia nhỏ hơn nửa biểu tượng, thì $\\dfrac{k}{2}$ phải là ước chung của $%s, %s, %s, %s$.\\\\
        Để $k$ lớn nhất có thể, ta chọn $\\dfrac{k}{2} = \\text{ƯCLN}(%s, %s, %s, %s) = %s \\Rightarrow k = %s$.\\\\
        Khi đó số biểu tượng của từng khối là:\\\\
        - Khối 6: $%s = 1 \\cdot %s + %s$ (gồm $1$ biểu tượng nguyên và $1$ nửa biểu tượng).\\\\
        - Khối 7: $%s = 2 \\cdot %s$ (gồm $2$ biểu tượng nguyên).\\\\
        - Khối 8: $%s = 2 \\cdot %s + %s$ (gồm $2$ biểu tượng nguyên và $1$ nửa biểu tượng).\\\\
        - Khối 9: $%s = 3 \\cdot %s$ (gồm $3$ biểu tượng nguyên).\\\\
        Vậy tổng số biểu tượng nguyên cần vẽ cho cả bốn khối là: $1 + 2 + 2 + 3 = %s$ (biểu tượng)."""
                   % (v6, v7, v8, v9, v6, v7, v8, v9, half_k, k,
                      v6, k, half_k, v7, k, v8, k, half_k, v9, k, tong_nguyen))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
