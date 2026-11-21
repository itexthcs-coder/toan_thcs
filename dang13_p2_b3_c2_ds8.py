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


def bt_dang13_p2_b3_c2_ds8(self):
    # Dạng 13: Phân tích đa thức thành nhân tử bằng phương pháp nhóm hạng tử kết hợp tổng hai lập phương
    b = randint(2, 5)
    m = randint(2, 5)
    b2, b3 = b**2, b**3
    heso_giua = m - b

    noidungcauhoi = ('''Cho đa thức $F(x) = x^3 + %s + %sx(x + %s)$. Xét tính đúng sai của các khẳng định sau:''' % (b3, m, b))

    nb_da_1_d = '\\True Hai hạng tử đầu $x^3 + %s$ phân tích thành $(x + %s)(x^2 - %sx + %s)$' % (b3, b, b, b2)
    nb_da_1_s = 'Hai hạng tử đầu $x^3 + %s$ phân tích thành $(x + %s)(x^2 + %sx + %s)$' % (b3, b, b, b2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $x^3 + %s = x^3 + %s^3 = (x + %s)(x^2 - %sx + %s)$.''' % (b3, b, b, b, b2))

    th_da_1_d = '\\True Đa thức $F(x)$ có nhân tử chung là $x + %s$' % (b)
    th_da_1_s = 'Đa thức $F(x)$ có nhân tử chung là $x - %s$' % (b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $F(x) = (x + %s)(x^2 - %sx + %s) + %sx(x + %s)$, nên có nhân tử chung là $x + %s$.''' % (b, b, b2, m, b, b))

    if heso_giua > 0:
        dt_str = 'x^2 + %sx + %s' % (heso_giua, b2) if heso_giua != 1 else 'x^2 + x + %s' % (b2)
        dt_sai = 'x^2 + %sx + %s' % (m + b, b2)
    elif heso_giua < 0:
        dt_str = 'x^2 - %sx + %s' % (abs(heso_giua), b2) if heso_giua != -1 else 'x^2 - x + %s' % (b2)
        dt_sai = 'x^2 + %sx + %s' % (m + b, b2)
    else:
        dt_str = 'x^2 + %s' % (b2)
        dt_sai = 'x^2 + %sx + %s' % (2*b, b2)

    vd_da_1_d = '\\True Sau khi đặt nhân tử chung và thu gọn, ta được $F(x) = (x + %s)(%s)$' % (b, dt_str)
    vd_da_1_s = 'Sau khi đặt nhân tử chung và thu gọn, ta được $F(x) = (x + %s)(%s)$' % (b, dt_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $F(x) = (x + %s)(x^2 - %sx + %s + %sx) = (x + %s)(%s)$.''' % (b, b, b2, m, b, dt_str))

    vdc_da_1_d = '\\True Tại $x = -%s$, giá trị của $F(x)$ bằng $0$' % (b)
    vdc_da_1_s = 'Tại $x = -%s$, giá trị của $F(x)$ bằng $%s$' % (b, b3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tại $x = -%s$, nhân tử $x + %s = -%s + %s = 0$, suy ra $F(-%s) = 0$.''' % (b, b, b, b, b))

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
