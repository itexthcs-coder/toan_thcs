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


def bt_dang19_p3_b3_c8_ds8(self):
    # Dạng 19: Phân tích dữ liệu truyền thông số (Tỉ lệ nhấp chuột CTR)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_hien_thi = random.choice([10000, 12500, 20000, 25000])
        k_nhap = random.choice([250, 325, 450, 550])
        while (60000 * k_nhap) % n_hien_thi != 0:
            k_nhap = random.choice([250, 300, 325, 400, 500, 600])
        n_them = random.choice([40000, 50000, 60000, 80000])
        while (n_them * k_nhap) % n_hien_thi != 0:
            n_them = random.choice([50000, 60000, 75000, 80000])
        kq_int = (n_them * k_nhap) // n_hien_thi
        kq_str = str(kq_int)

        p_str = str((Decimal(k_nhap) / Decimal(n_hien_thi)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Một chiến dịch quảng cáo trực tuyến hiển thị $%s$ lượt tới người dùng và thu về $%s$ lượt nhấp chuột vào liên kết sản phẩm. Nếu doanh nghiệp chi ngân sách để quảng cáo hiển thị thêm $%s$ lượt với hiệu quả tương đương, dự đoán số lượt nhấp chuột thu về là khoảng bao nhiêu?'''
                         % (n_hien_thi, k_nhap, n_them))

        loigiai = ('''Xác suất thực nghiệm của biến cố $E$: ``Người dùng nhấp chuột vào liên kết quảng cáo'' là $\\dfrac{%s}{%s} = %s$.\\
Vậy xác suất của biến cố $E$ được ước lượng là $P(E) \\approx %s$.\\
Dự đoán trong $%s$ lượt hiển thị thêm, số lượt nhấp chuột thu về là: $%s \\cdot %s = %s$ (lượt).'''
                   % (k_nhap, n_hien_thi, p_str, p_str, n_them, n_them, p_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
