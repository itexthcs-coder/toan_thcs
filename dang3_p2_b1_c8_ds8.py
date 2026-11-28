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


def bt_dang3_p2_b1_c8_ds8(self):
    # Dạng 3: Viết ngẫu nhiên một số tự nhiên có hai chữ số nhỏ hơn M
    M = random.choice([22, 24, 25, 26, 28])
    nums = list(range(10, M))
    tong = len(nums)
    div5 = [x for x in nums if x % 5 == 0]
    sum5 = [x for x in nums if (x // 10 + x % 10) == 5]
    primes = [x for x in nums if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
    composites = [x for x in nums if x not in primes]

    noidungcauhoi = (f"Thầy giáo viết ngẫu nhiên một số tự nhiên có hai chữ số nhỏ hơn ${M}$ lên bảng.")

    # Nhận biết
    nb_da_1_d = f"\\True Có tất cả ${tong}$ kết quả có thể xảy ra."
    nb_da_1_s = f"Có tất cả ${tong + 1}$ kết quả có thể xảy ra."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Các số tự nhiên có hai chữ số nhỏ hơn ${M}$ là từ $10$ đến ${M - 1}$. Số các số là $({M - 1} - 10) + 1 = {tong}$. Vậy có ${tong}$ kết quả có thể.")

    # Thông hiểu
    th_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Số được viết là số chia hết cho $5$''}} là ${len(div5)}$."
    th_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Số được viết là số chia hết cho $5$''}} là ${len(div5) + 1}$."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    str_div5 = "; ".join(map(str, div5))
    loigiai_th_1 = (f"Trong các số từ $10$ đến ${M - 1}$, các số chia hết cho $5$ là ${str_div5}$. Có ${len(div5)}$ kết quả thuận lợi.")

    # Vận dụng 1
    str_sum5 = "; ".join(map(str, sum5))
    vd_da_1_d = f"\\True Biến cố \\textit{{``Số được viết có tổng hai chữ số bằng $5$''}} có ${len(sum5)}$ kết quả thuận lợi là ${str_sum5}$."
    vd_da_1_s = f"Biến cố \\textit{{``Số được viết có tổng hai chữ số bằng $5$''}} có ${len(sum5) + 1}$ kết quả thuận lợi."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Các số có hai chữ số nhỏ hơn ${M}$ có tổng hai chữ số bằng $5$ là ${str_sum5}$. Có ${len(sum5)}$ kết quả thuận lợi.")

    # Vận dụng 2
    str_primes = "; ".join(map(str, primes))
    vdc_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Số được viết là hợp số''}} là ${len(composites)}$."
    vdc_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Số được viết là hợp số''}} bằng với số kết quả thuận lợi cho biến cố \\textit{{``Số được viết là số nguyên tố''}}."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Từ $10$ đến ${M - 1}$ có ${len(primes)}$ số nguyên tố là ${str_primes}$ và có ${tong} - {len(primes)} = {len(composites)}$ hợp số (do ${len(composites)} \\neq {len(primes)}$).")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
