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


def bt_dang19_p4_b3_c8_ds8(self):
    # Dạng 19: Thực nghiệm tung đồng thời ba đồng xu và đối chiếu xác suất lí thuyết
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
        n_tung = random.choice([160, 200])
        if n_tung == 160:
            s0 = random.choice([18, 19, 21])
            s1 = random.choice([58, 61, 62])
            s2 = random.choice([58, 62])
            s3 = n_tung - s0 - s1 - s2
        else:
            s0 = random.choice([23, 24, 26])
            s1 = random.choice([74, 76, 77])
            s2 = random.choice([73, 74, 76])
            s3 = n_tung - s0 - s1 - s2
            
        k_g = s2 + s3
        p_tn = Decimal(k_g) / Decimal(n_tung)
        p_tn_str = fmt_dec(p_tn)
        p_lt = Decimal('0.5')
        chenh_lech = abs(p_tn - p_lt)
        chenh_lech_str = fmt_dec(chenh_lech)
        
        noidungcauhoi = ('''Bạn Minh tung đồng thời $3$ đồng xu cân đối và đồng chất trong $%s$ lần. Kết quả về số mặt ngửa ($N$) xuất hiện trong mỗi lần tung được thống kê lại như sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Số mặt ngửa xuất hiện & $0$ & $1$ & $2$ & $3$ \\
\\hline
Số lần & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
a) Tính xác suất thực nghiệm của biến cố $G$: "Có ít nhất $2$ đồng xu xuất hiện mặt ngửa".\\
b) Tính xác suất lí thuyết của biến cố $G$ bằng cách liệt kê các kết quả đồng khả năng khi tung $3$ đồng xu (kí hiệu $N$ là mặt ngửa, $S$ là mặt sấp), từ đó tính độ chênh lệch giữa xác suất thực nghiệm và xác suất lí thuyết.'''
                         % (n_tung, s0, s1, s2, s3))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ lần tung, số lần có ít nhất $2$ đồng xu xuất hiện mặt ngửa ($2$ mặt ngửa hoặc $3$ mặt ngửa) là: $%s + %s = %s$ (lần).\\
Vậy xác suất thực nghiệm của biến cố $G$ là $\\dfrac{%s}{%s} = %s$.
\\item Khi tung đồng thời $3$ đồng xu cân đối và đồng chất, có $8$ kết quả có thể đồng khả năng là: $NNN; NNS; NSN; SNN; NSS; SNS; SSN; SSS$.\\
Có $4$ kết quả thuận lợi cho biến cố $G$ ("Có ít nhất $2$ đồng xu xuất hiện mặt ngửa") là: $NNN; NNS; NSN; SNN$.\\
Xác suất lí thuyết của biến cố $G$ là: $P(G) = \\dfrac{4}{8} = 0,5$.\\
Độ chênh lệch giữa xác suất thực nghiệm và xác suất lí thuyết của biến cố $G$ là: $|%s - 0,5| = %s$.
\\end{enumEX}'''
                   % (n_tung, s2, s3, k_g, k_g, n_tung, p_tn_str,
                      p_tn_str, chenh_lech_str))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
