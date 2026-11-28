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


def bt_dang7_p3_b3_c8_ds8(self):
    # Dạng 7: Ước lượng tổng số cá thể trong quần thể bằng phương pháp bắt - thả lại
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k_danh_dau = random.choice([60, 80, 90, 100, 120])
        n_bat_lai = random.choice([120, 150, 180, 200])
        k_co_dau = random.choice([10, 12, 15, 16, 20])
        while (k_danh_dau * n_bat_lai) % k_co_dau != 0:
            k_co_dau = random.choice([10, 12, 15, 16, 20, 24, 25])
        tong_ca = (k_danh_dau * n_bat_lai) // k_co_dau
        kq_str = str(tong_ca)

        p_dec = (Decimal(k_co_dau) / Decimal(n_bat_lai)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Để ước lượng số cá chép trong một hồ nuôi, người ta bắt lên $%s$ con cá chép, đánh dấu vào vây rồi thả lại xuống hồ. Một tuần sau, người ta bắt ngẫu nhiên $%s$ con cá chép từ hồ đó thì thấy có $%s$ con có dấu trên vây. Hãy ước lượng tổng số cá chép có trong hồ.'''
                         % (k_danh_dau, n_bat_lai, k_co_dau))

        loigiai = ('''Trong $%s$ con cá chép bắt lại, có $%s$ con có dấu trên vây nên xác suất thực nghiệm bắt được cá có dấu là $\\dfrac{%s}{%s} = %s$.\\\\
Gọi $N$ là tổng số cá chép có trong hồ. Vì có $%s$ con cá được đánh dấu nên xác suất chọn ngẫu nhiên một con cá có dấu là $\\dfrac{%s}{N}$.\\\\
Ước lượng xác suất bằng xác suất thực nghiệm, ta có: $\\dfrac{%s}{N} \\approx \\dfrac{%s}{%s}$.\\\\
Suy ra $N \\approx \\dfrac{%s \\cdot %s}{%s} = %s$.\\\\
Vậy ước lượng có khoảng $%s$ con cá chép trong hồ.'''
                   % (n_bat_lai, k_co_dau, k_co_dau, n_bat_lai, p_str, k_danh_dau, k_danh_dau, k_danh_dau, k_co_dau, n_bat_lai, k_danh_dau, n_bat_lai, k_co_dau, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
