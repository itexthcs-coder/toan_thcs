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


def bt_dang16_p2_b2_c10_hh9(self):
    d = random.choice([30, 40, 50, 60])
    R = d // 2
    gia_son = random.choice([150000, 180000, 200000]) # đồng / m^2
    S_cm2 = 4 * math.pi * (R**2)
    S_m2 = S_cm2 / 10000
    S_m2_round = Decimal(str(S_m2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    tien_round = Decimal(str(float(S_m2_round) * gia_son)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    V_cm3_round = Decimal(str((4 / 3) * math.pi * (R**3))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    def fmt(val):
        return str(val).replace('.', ',')

    noidungcauhoi = ('''Trong một công viên có đặt một quả cầu đá trang trí dạng hình cầu đặc với đường kính bằng $%s\\text{ cm}$. Người ta muốn sơn phủ toàn bộ bề mặt ngoài của quả cầu này với chi phí tiền sơn và nhân công là $%s$ đồng cho mỗi $\\text{m}^2$.''' % (d, gia_son))

    nb_da_1_d = '\\True Bán kính của quả cầu đá trang trí bằng $%s\\text{ cm}$' % (R)
    nb_da_1_s = 'Bán kính của quả cầu đá trang trí bằng $%s\\text{ cm}$' % (d)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Bán kính của quả cầu đá là $R = \\dfrac{%s}{2} = %s\\text{ (cm)}$.''' % (d, R))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích bề mặt cần sơn của quả cầu bằng $%s\\pi\\text{ cm}^2$' % (4 * R**2)
    th_da_1_s = 'Diện tích bề mặt cần sơn của quả cầu bằng $%s\\pi\\text{ cm}^2$' % (R**2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Diện tích bề mặt quả cầu là $S = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (R, 4 * R**2))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Thể tích của quả cầu đá bằng khoảng $%s\\text{ cm}^3$ (làm tròn đến hàng đơn vị)' % (V_cm3_round)
    vd_da_1_s = 'Thể tích của quả cầu đá bằng khoảng $%s\\text{ cm}^3$ (làm tròn đến hàng đơn vị)' % (V_cm3_round + Decimal('1200'))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Thể tích quả cầu đá là $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 \\approx %s\\text{ (cm}^3\\text{)}$.''' % (R, V_cm3_round))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu làm tròn diện tích bề mặt đến hàng phần trăm của $\\text{m}^2$ thì chi phí sơn quả cầu bằng $%s$ đồng' % (tien_round)
    vdc_da_1_s = 'Nếu làm tròn diện tích bề mặt đến hàng phần trăm của $\\text{m}^2$ thì chi phí sơn quả cầu bằng $%s$ đồng' % (tien_round + Decimal('50000'))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Đổi $S = %s\\pi\\text{ cm}^2 \\approx %s\\text{ m}^2$. Chi phí sơn là $%s \\cdot %s = %s$ (đồng).''' % (4 * R**2, fmt(S_m2_round), fmt(S_m2_round), gia_son, tien_round))
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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
