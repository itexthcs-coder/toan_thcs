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


def bt_dang17_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    m1, m2, m3, m4 = 16 * k, 24 * k, 30 * k, 10 * k
    n = 80 * k
    n_sau = 120 * k
    du_kien_qua = (n_sau * 30) // 80

    noidungcauhoi = ('''Một đại lý phân phối gạo thống kê khối lượng gạo mỗi lần nhập kho của các cửa hàng bán lẻ trong tháng qua như sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Khối lượng nhập (tạ) & $[5; 10)$ & $[10; 15)$ & $[15; 20)$ & $[20; 25)$ \\\\
\\hline
Số lượt nhập & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Đại lý áp dụng chính sách: tặng quà tri ân cho các lượt nhập từ $15$ tạ đến dưới $20$ tạ, và chiết khấu $5\\%%$ cho các lượt nhập từ $20$ tạ trở lên.''' % (m1, m2, m3, m4))

    list_nb_da_1 = [
        '\\True Tổng số lượt nhập gạo trong tháng là $%s$ lượt' % n,
        'Tổng số lượt nhập gạo trong tháng là $%s$ lượt' % (n - 10)
    ]
    loigiai_nb_1 = ('''Tổng số lượt nhập gạo là $n = %s + %s + %s + %s = %s$ (lượt).''' % (m1, m2, m3, m4, n))

    list_th_da_1 = [
        '\\True Có $50\\%%$ số lượt nhập gạo được hưởng ưu đãi (nhận quà tri ân hoặc chiết khấu)',
        'Có $37,5\\%%$ số lượt nhập gạo được hưởng ưu đãi (nhận quà tri ân hoặc chiết khấu)'
    ]
    loigiai_th_1 = ('''Số lượt nhập từ $15$ tạ trở lên là $%s + %s = %s$ lượt, chiếm $\\dfrac{%s}{%s} \\cdot 100\\%% = 50\\%%$.''' % (m3, m4, m3 + m4, m3 + m4, n))

    list_vd_da_1 = [
        '\\True Tỉ lệ lượt nhập được chiết khấu $5\\%%$ là $12,5\\%%$',
        'Tỉ lệ lượt nhập được chiết khấu $5\\%%$ là $10\\%%$'
    ]
    loigiai_vd_1 = ('''Tỉ lệ lượt nhập thuộc nhóm $[20; 25)$ là $\\dfrac{%s}{%s} \\cdot 100\\%% = 12,5\\%%$.''' % (m4, n))

    list_vdc_da_1 = [
        '\\True Nếu tháng sau tổng số lượt nhập tăng lên $%s$ lượt với cơ cấu tần số tương đối giữ nguyên thì dự kiến có $%s$ lượt được tặng quà tri ân' % (n_sau, du_kien_qua),
        'Nếu tháng sau tổng số lượt nhập tăng lên $%s$ lượt với cơ cấu tần số tương đối giữ nguyên thì dự kiến có $%s$ lượt được tặng quà tri ân' % (n_sau, du_kien_qua + 5)
    ]
    loigiai_vdc_1 = ('''Tỉ lệ lượt nhập tặng quà tri ân là $\\dfrac{%s}{%s} = 37,5\\%%$. Với $%s$ lượt, số lượt dự kiến là $%s \\cdot 37,5\\%% = %s$ (lượt).''' % (m3, n, n_sau, n_sau, du_kien_qua))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

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
