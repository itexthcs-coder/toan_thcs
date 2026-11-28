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


def bt_dang1_p4_b3_c8_ds8(self):
    # Dạng 1: Dự báo tỉ lệ nảy mầm và tính lượng hạt giống cần gieo (Nông nghiệp)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_int(n):
            return '{:,}'.format(int(n)).replace(',', '\\,')
        
        def fmt_dec(val, places=None):
            if places is not None:
                d = Decimal(str(val)).quantize(Decimal(places), rounding=ROUND_HALF_UP)
                s = format(d, 'f')
            else:
                s = str(val)
            return s.replace('.', ',')
        
        def round_int(val):
            return int(Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        
        def round_ten(val):
            return int(Decimal(str(val)).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
        n = random.choice([200, 250, 300, 400, 500])
        # Chọn p đẹp để k nguyên và chia hết hoặc số đẹp
        p_choice = random.choice([
            (250, 232, 18560),
            (200, 184, 14720),
            (250, 225, 16200),
            (400, 368, 22080),
            (500, 465, 27900),
            (300, 276, 19320)
        ])
        n, k, target = p_choice
        frac_p = Fraction(k, n)
        p_dec = Decimal(k) / Decimal(n)
        p_str = fmt_dec(p_dec)
        p_pct = fmt_dec(p_dec * 100)
        hat_can = round_ten(Decimal(target) / p_dec)
        
        noidungcauhoi = ('''Một trạm khuyến nông gieo thử nghiệm $%s$ hạt giống ngô lai thế hệ mới trên một lô đất mẫu thì thấy có $%s$ hạt nảy mầm khỏe mạnh.\\
a) Hãy ước lượng xác suất của biến cố $A$: "Một hạt giống ngô nảy mầm khỏe mạnh".\\
b) Một hợp tác xã cần gieo trồng để thu được khoảng $%s$ cây ngô giống đạt chuẩn. Hỏi hợp tác xã đó cần chuẩn bị khoảng bao nhiêu hạt giống (làm tròn đến hàng chục)?'''
                         % (fmt_int(n), fmt_int(k), fmt_int(target)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ hạt giống ngô được gieo thử nghiệm, biến cố $A$ xảy ra $%s$ lần.\\
Xác suất thực nghiệm của biến cố $A$ là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất của biến cố $A$ được ước lượng là $%s$ (hay $%s\\%%$).
\\item Gọi $N$ là số hạt giống ngô mà hợp tác xã cần chuẩn bị ($N \\in \\mathbb{N}^*$).\\
Vì xác suất một hạt giống nảy mầm khỏe mạnh được ước lượng là $P(A) \\approx %s$ nên số cây ngô đạt chuẩn thu được khoảng $N \\cdot %s$.\\
Theo đề bài, ta có $N \\cdot %s \\approx %s$, suy ra $N \\approx \\dfrac{%s}{%s} = %s$.\\
Làm tròn kết quả đến hàng chục, hợp tác xã đó cần chuẩn bị khoảng $%s$ hạt giống.
\\end{enumEX}'''
                   % (fmt_int(n), fmt_int(k), fmt_int(k), fmt_int(n), p_str, p_pct,
                      p_str, p_pct,
                      p_str, p_str, p_str, fmt_int(target), fmt_int(target), p_str,
                      fmt_int(round_int(Decimal(target) / p_dec)), fmt_int(hat_can)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
