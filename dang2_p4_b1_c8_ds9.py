# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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


def bt_dang2_p4_b1_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Dạng 2: Rút 2 quả cầu không hoàn lại từ hộp đựng 4 quả cầu màu Đỏ, Xanh, Vàng, Trắng
        mau_list = random.sample(['Đỏ', 'Xanh', 'Vàng', 'Trắng', 'Tím'], 4)
        m1, m2, m3, m4 = mau_list[0], mau_list[1], mau_list[2], mau_list[3]
        noidungcauhoi = ('''Một túi vải kín đựng $4$ quả cầu có cùng kích thước và khối lượng được sơn $4$ màu khác nhau: %s, %s, %s, %s. Lấy ngẫu nhiên lần lượt hai quả cầu từ túi, quả cầu lấy ra lần đầu không trả lại vào túi.\\\\
a) Mô tả phép thử và điều kiện của mỗi cặp kết quả $(a, b)$ thu được.\\\\
b) Liệt kê tất cả các phần tử của không gian mẫu $\\Omega$ và tính số phần tử của $\\Omega$.'''
                         % (m1, m2, m3, m4))
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Phép thử là lấy ngẫu nhiên lần lượt hai quả cầu từ túi mà quả cầu lấy ra lần đầu không trả lại vào túi. Kết quả của phép thử là cặp $(a, b)$, trong đó $a$ là màu của quả cầu lấy ra lần thứ nhất và $b$ là màu của quả cầu lấy ra lần thứ hai. Vì không trả lại quả cầu lần đầu vào túi nên $a$ và $b$ phải khác màu nhau ($a \\neq b$).
\\item Liệt kê tất cả các cặp $(a, b)$ với $a \\neq b$, ta được không gian mẫu:\\\\
$\\Omega = \\{(\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s}); (\\text{%s}, \\text{%s})\\}$.\\\\
Vậy không gian mẫu $\\Omega$ có $4 \\cdot 3 = 12$ phần tử.
\\end{enumEX}'''
                   % (m1, m2, m1, m3, m1, m4,
                      m2, m1, m2, m3, m2, m4,
                      m3, m1, m3, m2, m3, m4,
                      m4, m1, m4, m2, m4, m3))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
