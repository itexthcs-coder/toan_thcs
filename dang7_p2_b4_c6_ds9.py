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


def bt_dang7_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        dan_dau = random.choice([500000, 600000, 800000, 1000000, 1200000])
        ti_le = random.choice([2, 4, 5, 6, 8, 10])
        he_so_1 = Decimal(1) + Decimal(ti_le) / Decimal(100)
        he_so_2 = he_so_1 ** 2
        dan_sau = int(Decimal(dan_dau) * he_so_2)
        dan_nam_3 = int(Decimal(dan_sau) * he_so_1)
        moc_so_sanh = dan_nam_3 + random.choice([3000, 5000, 8000])

        noidungcauhoi = ('''Theo thống kê của một đô thị vệ tinh, dân số của thành phố tăng trưởng đều qua các năm. Cách đây $2\\text{ năm}$, dân số thành phố là $%s\\text{ người}$, đến nay dân số đã đạt $%s\\text{ người}$. Gọi $x\\%%$ là tỉ lệ tăng dân số trung bình hằng năm của thành phố ($x > 0$).''' % (fmt_num(dan_dau), fmt_num(dan_sau)))

        nb_da_1_d = '\\True Dân số của thành phố sau năm thứ nhất là $%s\\left(1 + \\frac{x}{100}\\right)$ người' % (fmt_num(dan_dau))
        nb_da_1_s = 'Dân số của thành phố sau năm thứ nhất là $%s(1 + x)$ người' % (fmt_num(dan_dau))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Sau năm thứ nhất, dân số tăng thêm $x\\%%$ nên dân số đạt $%s + %s \\cdot \\frac{x}{100} = %s\\left(1 + \\frac{x}{100}\\right)$ (người).''' % (fmt_num(dan_dau), fmt_num(dan_dau), fmt_num(dan_dau)))

        th_da_1_d = '\\True Phương trình tìm tỉ lệ tăng dân số là $\\left(1 + \\frac{x}{100}\\right)^2 = %s$' % (fmt_num(he_so_2))
        th_da_1_s = 'Phương trình tìm tỉ lệ tăng dân số là $1 + \\frac{2x}{100} = %s$' % (fmt_num(he_so_2))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Sau $2\\text{ năm}$, dân số thành phố là $%s\\left(1 + \\frac{x}{100}\\right)^2 = %s \\Leftrightarrow \\left(1 + \\frac{x}{100}\\right)^2 = %s$.''' % (fmt_num(dan_dau), fmt_num(dan_sau), fmt_num(he_so_2)))

        vd_da_1_d = '\\True Tỉ lệ tăng dân số trung bình hằng năm của thành phố là $%s\\%%$' % (fmt_num(ti_le))
        vd_da_1_s = 'Tỉ lệ tăng dân số trung bình hằng năm của thành phố là $%s\\%%$' % (fmt_num(ti_le + 1))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Từ $\\left(1 + \\frac{x}{100}\\right)^2 = %s$, vì $x > 0$ nên $1 + \\frac{x}{100} = %s \\Leftrightarrow \\frac{x}{100} = %s \\Leftrightarrow x = %s$. Vậy tỉ lệ tăng dân số trung bình là $%s\\%%$.''' % (fmt_num(he_so_2), fmt_num(he_so_1), fmt_num(he_so_1 - 1), fmt_num(ti_le), fmt_num(ti_le)))

        vdc_da_1_d = '\\True Nếu giữ nguyên tốc độ tăng trưởng này, sau $1\\text{ năm}$ nữa dân số thành phố sẽ là $%s\\text{ người}$' % (fmt_num(dan_nam_3))
        vdc_da_1_s = 'Nếu giữ nguyên tốc độ tăng trưởng này, sau $1\\text{ năm}$ nữa dân số thành phố sẽ vượt mốc $%s\\text{ người}$' % (fmt_num(moc_so_sanh))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Sau $1\\text{ năm}$ nữa, dân số của thành phố sẽ là $%s \\cdot %s = %s\\text{ (người)}$ (chưa vượt mốc $%s\\text{ người}$).''' % (fmt_num(dan_sau), fmt_num(he_so_1), fmt_num(dan_nam_3), fmt_num(moc_so_sanh)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
