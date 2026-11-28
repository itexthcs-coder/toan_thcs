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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def fmt_frac(f):
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)


def fmt_dec(val, digits=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*digits) if digits > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = str(d).rstrip('0').rstrip('.') if digits > 0 else str(d)
    if s == '-0':
        s = '0'
    return s.replace('.', ',')


def bt_dang15_p2_b2_c8_ds8(self):
    # Dạng 15: Kết hợp tính xác suất với cấu tạo số tự nhiên (Số có hai chữ số)
    digits = random.choice([[1, 2, 3, 4], [1, 2, 4, 5], [2, 3, 4, 5]])
    nums = [10*a + b for a in digits for b in digits if a != b]
    tong = len(nums)

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (6.2,1.4);\n'
        '\\node at (3.1,0.7) {Tập chữ số: $\\{%s\\}$ $\\longrightarrow$ Số $\\overline{ab}$ ($a \\neq b$)};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % ('; '.join(str(d) for d in digits))

    noidungcauhoi = (
        'Viết ngẫu nhiên một số tự nhiên có hai chữ số khác nhau từ các chữ số $%s$. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % ('; '.join(str(d) for d in digits), tikz_hinh)
    )

    nb_da_1_d = '\\True Có tất cả $%s$ số tự nhiên có thể viết được' % (tong)
    nb_da_1_s = 'Có tất cả $16$ số tự nhiên có thể viết được'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Chữ số hàng chục có $4$ cách chọn, chữ số hàng đơn vị có $3$ cách chọn (do khác chữ số hàng chục) nên có $4 \\cdot 3 = 12$ số tự nhiên có hai chữ số khác nhau.'
    list_nb_2 = [loigiai_nb_1]

    chan = [x for x in nums if x % 2 == 0]
    p_chan = Fraction(len(chan), tong)
    p_chan_sai = Fraction(len(chan) + 1, tong)
    th_da_1_d = '\\True Xác suất để số viết được là số chẵn bằng $%s$' % (fmt_frac(p_chan))
    th_da_1_s = 'Xác suất để số viết được là số chẵn bằng $%s$' % (fmt_frac(p_chan_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Các số chẵn viết được là: $%s$ (gồm $%s$ số). \\ Vậy xác suất để số viết được là số chẵn bằng $\\dfrac{%s}{%s} = %s$.' % ('; '.join(str(x) for x in chan), len(chan), len(chan), tong, fmt_frac(p_chan))
    list_th_2 = [loigiai_th_1]

    chia3 = [x for x in nums if x % 3 == 0]
    p_chia3 = Fraction(len(chia3), tong)
    p_chia3_sai = Fraction(len(chia3) + 2, tong)
    vd_da_1_d = '\\True Xác suất để số viết được chia hết cho $3$ bằng $%s$' % (fmt_frac(p_chia3))
    vd_da_1_s = 'Xác suất để số viết được chia hết cho $3$ bằng $%s$' % (fmt_frac(p_chia3_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Các số viết được chia hết cho $3$ là: $%s$ (gồm $%s$ số). \\ Vậy xác suất để số viết được chia hết cho $3$ bằng $\\dfrac{%s}{%s} = %s$.' % ('; '.join(str(x) for x in chia3), len(chia3), len(chia3), tong, fmt_frac(p_chia3))
    list_vd_2 = [loigiai_vd_1]

    lon30 = [x for x in nums if x > 30]
    p_lon30 = Fraction(len(lon30), tong)
    p_lon30_sai = Fraction(len(lon30) - 1, tong)
    vdc_da_1_d = '\\True Xác suất để số viết được lớn hơn $30$ bằng $%s$' % (fmt_frac(p_lon30))
    vdc_da_1_s = 'Xác suất để số viết được lớn hơn $30$ bằng $%s$' % (fmt_frac(p_lon30_sai))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Các số viết được lớn hơn $30$ là: $%s$ (gồm $%s$ số). \\ Vậy xác suất để số viết được lớn hơn $30$ bằng $\\dfrac{%s}{%s} = %s$.' % ('; '.join(str(x) for x in lon30), len(lon30), len(lon30), tong, fmt_frac(p_lon30))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
