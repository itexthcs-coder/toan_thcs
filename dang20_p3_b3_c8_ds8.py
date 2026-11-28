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


def bt_dang20_p3_b3_c8_ds8(self):
    # Dạng 20: Tổng hợp dữ liệu nhiều mẫu độc lập để nâng cao độ chính xác dự báo
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n1 = random.choice([200, 300, 400])
        n2 = random.choice([400, 500, 600])
        tong_n = n1 + n2
        k1 = random.randint(5, 12)
        k2 = random.randint(8, 16)
        tong_k = k1 + k2
        n_kien = random.choice([3200, 4000, 4800, 5600])

        val_raw = Decimal(n_kien * tong_k) / Decimal(tong_n)
        kq = val_raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)
        val_raw_str = str(val_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Hai tổ kiểm tra chất lượng độc lập cùng kiểm tra một loại linh kiện điện tử, kết quả được ghi trong bảng sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|}
\\hline
Đơn vị kiểm tra & Số linh kiện kiểm tra & Số linh kiện bị lỗi \\\\
\\hline
Tổ 1 & $%s$ & $%s$ \\\\
\\hline
Tổ 2 & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Gộp dữ liệu của cả hai tổ để ước lượng xác suất, hãy dự đoán trong một kiện hàng gồm $%s$ linh kiện loại này có khoảng bao nhiêu linh kiện bị lỗi (làm tròn kết quả đến hàng đơn vị)?'''
                         % (n1, k1, n2, k2, n_kien))

        loigiai = ('''Gộp dữ liệu của cả hai tổ, tổng số linh kiện được kiểm tra là: $%s + %s = %s$ (linh kiện).\\\\
Tổng số linh kiện bị lỗi được phát hiện là: $%s + %s = %s$ (linh kiện).\\\\
Xác suất thực nghiệm của biến cố $E$: ``Linh kiện điện tử bị lỗi'' là $\\dfrac{%s}{%s}$.\\\\
Gọi $k$ là số linh kiện bị lỗi trong kiện hàng gồm $%s$ linh kiện.\\\\
Ta có $\\dfrac{k}{%s} \\approx \\dfrac{%s}{%s}$, suy ra $k \\approx %s \\cdot \\dfrac{%s}{%s} = %s \\approx %s$.\\\\
Vậy dự đoán trong kiện hàng đó có khoảng $%s$ linh kiện bị lỗi.'''
                   % (n1, n2, tong_n, k1, k2, tong_k, tong_k, tong_n, n_kien, n_kien, tong_k, tong_n, n_kien, tong_k, tong_n, val_raw_str, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
