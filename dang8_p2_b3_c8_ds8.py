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

def fmt_dec(val, places=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*places) if places > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = format(d, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')

def fmt_frac(num, den):
    f = Fraction(num, den)
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang8_p2_b3_c8_ds8(self):
    # Dạng 8: Chọn ngẫu nhiên số có 3 chữ số khác nhau lập từ tập 4 chữ số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tap = random.choice([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
        chan_cnt = sum(1 for x in tap if x % 2 == 0)
        p_chan = fmt_frac(chan_cnt, 4)
        p_chan_sai = fmt_frac(4 - chan_cnt, 4) if chan_cnt != 2 else '\\dfrac{1}{4}'

        # Bộ 3 chữ số có tổng chia hết cho 3
        bo_chia3 = [c for c in itertools.combinations(tap, 3) if sum(c) % 3 == 0]
        so_chia3 = len(bo_chia3) * 6
        p_chia3 = fmt_frac(so_chia3, 24)
        p_chia3_sai = fmt_frac(so_chia3 + 6, 24) if so_chia3 < 18 else '\\dfrac{1}{4}'

        moc = tap[2] * 100
        so_lon = 2 * 6
        p_lon = fmt_frac(so_lon, 24)
        p_lon_sai = '\\dfrac{1}{4}'

        tap_str = '; '.join(map(str, tap))
        noidungcauhoi = (
            'Viết ngẫu nhiên một số tự nhiên có ba chữ số khác nhau được lập từ các chữ số $\\{%s\\}$. Xét tính đúng sai của các khẳng định sau:'
            % tap_str
        )

        nb_da_1_d = '\\True Có tất cả $24$ số tự nhiên có thể lập được theo quy tắc trên'
        nb_da_1_s = 'Có tất cả $64$ số tự nhiên có thể lập được theo quy tắc trên'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất để số được chọn là số chẵn bằng $%s$' % p_chan
        th_da_1_s = 'Xác suất để số được chọn là số chẵn bằng $%s$' % p_chan_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất để số được chọn chia hết cho $3$ là $%s$' % p_chia3
        vd_da_1_s = 'Xác suất để số được chọn chia hết cho $3$ là $%s$' % p_chia3_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất để số được chọn lớn hơn $%s$ bằng $%s$' % (moc, p_lon)
        vdc_da_1_s = 'Xác suất để số được chọn lớn hơn $%s$ bằng $%s$' % (moc, p_lon_sai)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Số các số tự nhiên có ba chữ số khác nhau lập từ $4$ chữ số đã cho là $4 \\cdot 3 \\cdot 2 = 24$ (số).'
        )
        loigiai_th_1 = (
            'Trong tập $\\{%s\\}$ có $%s$ chữ số chẵn nên có $%s \\cdot 3 \\cdot 2 = %s$ số chẵn.\\'
            'Xác suất để số được chọn là số chẵn bằng $\\dfrac{%s}{24} = %s$.'
            % (tap_str, chan_cnt, chan_cnt, chan_cnt * 6, chan_cnt * 6, p_chan)
        )
        loigiai_vd_1 = (
            'Từ $4$ chữ số đã cho, có $%s$ bộ ba chữ số có tổng chia hết cho $3$, mỗi bộ lập được $3 \\cdot 2 \\cdot 1 = 6$ số.\\'
            'Vậy có $%s \\cdot 6 = %s$ số chia hết cho $3$, xác suất tương ứng là $\\dfrac{%s}{24} = %s$.'
            % (len(bo_chia3), len(bo_chia3), so_chia3, so_chia3, p_chia3)
        )
        loigiai_vdc_1 = (
            'Để số lập được lớn hơn $%s$, chữ số hàng trăm có $2$ cách chọn (là $%s$ hoặc $%s$).\\'
            'Do đó có $2 \\cdot 3 \\cdot 2 = 12$ số thỏa mãn, xác suất là $\\dfrac{12}{24} = %s$.'
            % (moc, tap[2], tap[3], p_lon)
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
