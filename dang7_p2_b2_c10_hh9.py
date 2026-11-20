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


def bt_dang7_p2_b2_c10_hh9(self):
    n_list = [8, 27, 64]
    n = random.choice(n_list)
    k = round(n**(1/3))
    r = randint(2, 4)
    R = k * r
    V_nho = Rational(4, 3) * r**3
    V_lon = Rational(4, 3) * R**3
    S_tong_nho = n * 4 * r**2
    S_lon = 4 * R**2

    noidungcauhoi = ('''Người ta đun nóng chảy hoàn toàn $%s$ viên bi sắt đặc hình cầu giống hệt nhau, mỗi viên có bán kính $r = %s\\text{ cm}$, rồi đúc lại thành một khối cầu lớn duy nhất (coi hao hụt không đáng kể).''' % (n, r))

    nb_da_1_d = '\\True Thể tích của khối cầu lớn bằng tổng thể tích của $%s$ viên bi nhỏ và bằng $%s\\pi\\text{ cm}^3$' % (n, latex(V_lon))
    nb_da_1_s = 'Thể tích của khối cầu lớn bằng $%s\\pi\\text{ cm}^3$' % latex(V_nho)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo nguyên tắc bảo toàn thể tích: $V_{\\text{lớn}} = %s \\cdot V_{\\text{nhỏ}} = %s \\cdot \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (n, n, r, latex(V_lon)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bán kính của khối cầu lớn bằng $%s\\text{ cm}$' % (R)
    th_da_1_s = 'Bán kính của khối cầu lớn bằng $%s\\text{ cm}$' % (n * r)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $\\dfrac{4}{3}\\pi R^3 = %s \\cdot \\dfrac{4}{3}\\pi r^3 \\Rightarrow R^3 = %s r^3 \\Rightarrow R = %sr = %s \\cdot %s = %s\\text{ (cm)}$.''' % (n, n, k, k, r, R))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích bề mặt của khối cầu lớn bằng $%s\\pi\\text{ cm}^2$' % (S_lon)
    vd_da_1_s = 'Diện tích bề mặt của khối cầu lớn bằng $%s\\pi\\text{ cm}^2$' % (S_tong_nho)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Diện tích mặt cầu lớn là $S_{\\text{lớn}} = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (R, S_lon))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tổng diện tích bề mặt của $%s$ viên bi nhỏ ban đầu lớn hơn diện tích bề mặt khối cầu lớn một lượng là $%s\\pi\\text{ cm}^2$' % (n, S_tong_nho - S_lon)
    vdc_da_1_s = 'Tổng diện tích bề mặt của $%s$ viên bi nhỏ ban đầu bằng diện tích bề mặt khối cầu lớn' % (n)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tổng diện tích $%s$ viên bi nhỏ là $%s \\cdot 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nPhần diện tích giảm đi sau khi đúc là $%s\\pi - %s\\pi = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (n, n, r, S_tong_nho, S_tong_nho, S_lon, S_tong_nho - S_lon))
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
