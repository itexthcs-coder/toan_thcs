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


def bt_dang17_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        m1, m2, m3, m4 = 44 * k, 76 * k, 52 * k, 28 * k
        n = 200 * k
        so_don_free = m3 + m4
        tong_tien = so_don_free * 30

        noidungcauhoi = ('''Một cửa hàng kinh doanh trực tuyến thống kê giá trị mỗi đơn hàng (đơn vị: nghìn đồng) của $%s$ khách hàng trong ngày hội mua sắm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Giá trị đơn hàng (nghìn đồng) & $[100; 250)$ & $[250; 400)$ & $[400; 550)$ & $[550; 700]$ \\\\
\\hline
Số đơn hàng & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Cửa hàng áp dụng chính sách miễn phí vận chuyển (trị giá $30$ nghìn đồng/đơn) cho tất cả các đơn hàng có giá trị từ $400$ nghìn đồng trở lên.\\
a) Lập bảng tần số tương đối ghép nhóm và tính tỉ lệ đơn hàng được miễn phí vận chuyển.\\
b) Tính tổng số tiền phí vận chuyển mà cửa hàng đã hỗ trợ cho khách hàng trong ngày hôm đó.''' % (n, m1, m2, m3, m4))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Với cỡ mẫu $n = %s$, tần số tương đối của các nhóm lần lượt là: $22\\%%$; $38\\%%$; $26\\%%$; $14\\%%$. Ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Giá trị đơn hàng (nghìn đồng) & $[100; 250)$ & $[250; 400)$ & $[400; 550)$ & $[550; 700]$ \\\\
\\hline
Tần số tương đối & $22\\%%$ & $38\\%%$ & $26\\%%$ & $14\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
Tỉ lệ đơn hàng được miễn phí vận chuyển (từ $400$ nghìn đồng trở lên) là: $26\\%% + 14\\%% = 40\\%%$.
\\item Số đơn hàng được miễn phí vận chuyển là: $%s + %s = %s$ (đơn hàng).\\
Tổng số tiền phí vận chuyển cửa hàng đã hỗ trợ cho khách hàng là:
$$%s \\cdot 30 = %s \\text{ (nghìn đồng)}.$$
\\end{enumEX}''' % (n, m3, m4, so_don_free, so_don_free, tong_tien))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
