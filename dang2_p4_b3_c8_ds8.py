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


def bt_dang2_p4_b3_c8_ds8(self):
    # Dạng 2: Ước lượng quần thể cá trong ao bằng phương pháp bắt – đánh dấu – thả lại
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
        # M: số cá đánh dấu ban đầu, n2: số cá bắt lần 2, k2: số cá có dấu
        cfg = random.choice([
            (120, 150, 18),
            (100, 160, 16),
            (150, 200, 24),
            (90, 140, 14),
            (140, 180, 21),
            (160, 250, 32)
        ])
        M, n2, k2 = cfg
        frac_b = Fraction(k2, n2)
        p_dec = Decimal(k2) / Decimal(n2)
        p_str = fmt_dec(p_dec)
        total_fish = round_int(Decimal(M) / p_dec)
        
        noidungcauhoi = ('''Để ước lượng số lượng cá chép đang nuôi trong một hồ lớn, người ta dùng lưới bắt ngẫu nhiên $%s$ con cá chép, gắn thẻ đánh dấu vào vây rồi thả lại xuống hồ. Một tuần sau, người ta lại bắt ngẫu nhiên $%s$ con cá chép từ hồ đó thì thấy có $%s$ con có gắn thẻ đánh dấu.\\
a) Tính xác suất thực nghiệm của biến cố $B$: "Con cá bắt được ở lần thứ hai có gắn thẻ đánh dấu".\\
b) Từ kết quả trên, hãy ước lượng tổng số cá chép hiện có trong hồ.'''
                         % (fmt_int(M), fmt_int(n2), fmt_int(k2)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ con cá chép bắt ngẫu nhiên ở lần thứ hai, có $%s$ con có gắn thẻ đánh dấu.\\
Vậy xác suất thực nghiệm của biến cố $B$ là $\\dfrac{%s}{%s} = \\dfrac{%s}{%s} = %s$.
\\item Gọi $N$ là tổng số cá chép hiện có trong hồ ($N \\in \\mathbb{N}^*$).\\
Do có $%s$ con cá được gắn thẻ đánh dấu trong tổng số $N$ con cá của hồ nên xác suất bắt được một con cá có gắn thẻ đánh dấu là $\\dfrac{%s}{N}$.\\
Ước lượng xác suất của biến cố $B$ qua xác suất thực nghiệm ở câu a, ta có: $\\dfrac{%s}{N} \\approx %s$.\\
Suy ra $N \\approx \\dfrac{%s}{%s} = %s$.\\
Vậy tổng số cá chép hiện có trong hồ được ước lượng là khoảng $%s$ con.
\\end{enumEX}'''
                   % (fmt_int(n2), fmt_int(k2), fmt_int(k2), fmt_int(n2),
                      frac_b.numerator, frac_b.denominator, p_str,
                      fmt_int(M), fmt_int(M), fmt_int(M), p_str,
                      fmt_int(M), p_str, fmt_int(total_fish), fmt_int(total_fish)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
