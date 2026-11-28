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


def bt_dang13_p3_b3_c8_ds8(self):
    # Dạng 13: Bài toán Y tế - Dự báo số ca điều trị ngoại trú từ số liệu khám ngoại trú
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_kham = random.choice([500, 600, 640, 800])
        p_noi_tru = random.choice([0.12, 0.15, 0.16, 0.2])
        while (Decimal(str(p_noi_tru)) * Decimal(n_kham)) % 1 != 0:
            p_noi_tru = random.choice([0.1, 0.15, 0.2, 0.25])
        k_noi_tru = int(Decimal(str(p_noi_tru)) * Decimal(n_kham))
        k_ngoai_tru = n_kham - k_noi_tru
        n_tuan_toi = random.choice([900, 1000, 1100, 1200])

        val_raw = Decimal(n_tuan_toi * k_ngoai_tru) / Decimal(n_kham)
        kq = val_raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)
        p_ngoai_str = str((Decimal(k_ngoai_tru) / Decimal(n_kham)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Thống kê tại khoa Nhi của một bệnh viện trong tuần cao điểm cho thấy trong $%s$ bệnh nhi đến khám sốt virus, có $%s$ trẻ phải nhập viện điều trị nội trú. Nếu tuần tiếp theo dự kiến có $%s$ bệnh nhi đến khám với triệu chứng tương tự, hãy dự đoán có khoảng bao nhiêu trẻ chỉ cần điều trị ngoại trú (không phải nhập viện)?'''
                         % (n_kham, k_noi_tru, n_tuan_toi))

        loigiai = ('''Trong $%s$ bệnh nhi đến khám, số trẻ điều trị ngoại trú là: $%s - %s = %s$ (trẻ).\\\\
Xác suất thực nghiệm của biến cố $E$: ``Bệnh nhi chỉ cần điều trị ngoại trú'' là $\\dfrac{%s}{%s} = %s$.\\\\
Vậy xác suất của biến cố $E$ được ước lượng là $P(E) \\approx %s$.\\\\
Dự đoán trong $%s$ bệnh nhi tuần tới có khoảng $%s \\cdot %s = %s$ trẻ chỉ cần điều trị ngoại trú.'''
                   % (n_kham, n_kham, k_noi_tru, k_ngoai_tru, k_ngoai_tru, n_kham, p_ngoai_str, p_ngoai_str, n_tuan_toi, n_tuan_toi, p_ngoai_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
