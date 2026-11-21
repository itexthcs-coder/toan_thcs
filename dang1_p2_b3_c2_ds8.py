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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang1_p2_b3_c2_ds8(self):
    # Dạng 1: Phân tích và kiểm tra tính đúng sai của hằng đẳng thức tổng hai lập phương có hệ số kép
    a = randint(2, 5)
    b = randint(2, 5)
    while math.gcd(a, b) != 1:
        b = randint(2, 5)
    a2, ab, b2 = a**2, a*b, b**2
    a3, b3 = a**3, b**3

    noidungcauhoi = ('''Cho đa thức $P(x, y) = %sx^3 + %sy^3$. Xét tính đúng sai của các khẳng định sau:''' % (a3, b3))

    nb_da_1_d = '\\True Đa thức $P(x, y)$ có thể viết dưới dạng $(%sx)^3 + (%sy)^3$' % (a, b)
    nb_da_1_s = 'Đa thức $P(x, y)$ có thể viết dưới dạng $(%sx)^3 + (%sy)^3$' % (a2, b2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $%sx^3 = (%sx)^3$ và $%sy^3 = (%sy)^3$ nên $P(x, y) = (%sx)^3 + (%sy)^3$.''' % (a3, a, b3, b, a, b))

    th_da_1_d = '\\True Nhân tử thứ nhất khi phân tích $P(x, y)$ thành tích là $%sx + %sy$' % (a, b)
    th_da_1_s = 'Nhân tử thứ nhất khi phân tích $P(x, y)$ thành tích là $%sx - %sy$' % (a, b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Áp dụng hằng đẳng thức tổng hai lập phương: $P(x, y) = (%sx)^3 + (%sy)^3 = (%sx + %sy)(%sx^2 - %sxy + %sy^2)$. Nhân tử thứ nhất là $%sx + %sy$.''' % (a, b, a, b, a2, ab, b2, a, b))

    vd_da_1_d = '\\True Bình phương thiếu của hiệu trong khai triển $P(x, y)$ là $%sx^2 - %sxy + %sy^2$' % (a2, ab, b2)
    vd_da_1_s = 'Bình phương thiếu của hiệu trong khai triển $P(x, y)$ là $%sx^2 - %sxy + %sy^2$' % (a2, 2*ab, b2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Bình phương thiếu của hiệu trong khai triển $P(x, y)$ là $(%sx)^2 - (%sx)(%sy) + (%sy)^2 = %sx^2 - %sxy + %sy^2$.''' % (a, a, b, b, a2, ab, b2))

    vdc_da_1_d = '\\True Giá trị của $P(x, y)$ tại $x = \\frac{1}{%s}$ và $y = -\\frac{1}{%s}$ bằng $0$' % (a, b)
    vdc_da_1_s = 'Giá trị của $P(x, y)$ tại $x = \\frac{1}{%s}$ và $y = -\\frac{1}{%s}$ bằng $2$' % (a, b)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tại $x = \\frac{1}{%s}$ và $y = -\\frac{1}{%s}$, ta có $%sx + %sy = %s \\cdot \\frac{1}{%s} + %s \\cdot \\left(-\\frac{1}{%s}\\right) = 1 - 1 = 0$, do đó $P(x, y) = 0$.''' % (a, b, a, b, a, a, b, b))

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
