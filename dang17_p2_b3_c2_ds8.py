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


def bt_dang17_p2_b3_c2_ds8(self):
    # Dạng 17 (Thực tế): Tổng thể tích hai bể chứa hình lập phương
    k = randint(2, 3)
    k2, k3 = k**2, k**3
    tong_canh = randint(5, 8)
    tich_canh = randint(4, 9)
    V_tong = tong_canh**3 - 3 * tich_canh * tong_canh
    a_val = randint(1, 2)
    b_val = randint(1, 3)
    V_cu_the = k3 * (a_val**3) + (b_val**3)

    noidungcauhoi = ('''Một xưởng sản xuất có hai bể chứa nước hình lập phương: bể thứ nhất có cạnh dài $%sa$ ($\\text{m}$), bể thứ hai có cạnh dài $b$ ($\\text{m}$) (với $a, b > 0$). Xét tính đúng sai của các khẳng định sau:''' % (k))

    nb_da_1_d = '\\True Tổng thể tích của cả hai bể chứa là $V = %sa^3 + b^3$ ($\\text{m}^3$)' % (k3)
    nb_da_1_s = 'Tổng thể tích của cả hai bể chứa là $V = %sa^3 + b^3$ ($\\text{m}^3$)' % (k)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Thể tích bể thứ nhất là $(%sa)^3 = %sa^3$ ($\\text{m}^3$), thể tích bể thứ hai là $b^3$ ($\\text{m}^3$), nên tổng thể tích là $V = %sa^3 + b^3$ ($\\text{m}^3$).''' % (k, k3, k3))

    th_da_1_d = '\\True Phân tích đa thức $V$ thành tích, ta được $V = (%sa + b)(%sa^2 - %sab + b^2)$' % (k, k2, k)
    th_da_1_s = 'Phân tích đa thức $V$ thành tích, ta được $V = (%sa + b)(%sa^2 + %sab + b^2)$' % (k, k2, k)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Áp dụng hằng đẳng thức tổng hai lập phương: $V = (%sa)^3 + b^3 = (%sa + b)(%sa^2 - %sab + b^2)$.''' % (k, k, k2, k))

    vd_da_1_d = '\\True Nếu tổng độ dài hai cạnh $%sa + b = %s\\text{ m}$ và tích $%sab = %s\\text{ m}^2$, thì tổng thể tích hai bể là $%s\\text{ m}^3$' % (k, tong_canh, k, tich_canh, V_tong)
    vd_da_1_s = 'Nếu tổng độ dài hai cạnh $%sa + b = %s\\text{ m}$ và tích $%sab = %s\\text{ m}^2$, thì tổng thể tích hai bể là $%s\\text{ m}^3$' % (k, tong_canh, k, tich_canh, tong_canh**3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $V = (%sa)^3 + b^3 = (%sa + b)^3 - 3(%sa)b(%sa + b) = %s^3 - 3 \\cdot %s \\cdot %s = %s$ ($\\text{m}^3$).''' % (k, k, k, k, tong_canh, tich_canh, tong_canh, V_tong))

    vdc_da_1_d = '\\True Khi $a = %s\\text{ m}$ và $b = %s\\text{ m}$, tổng thể tích hai bể bằng $%s\\text{ m}^3$' % (a_val, b_val, V_cu_the)
    vdc_da_1_s = 'Khi $a = %s\\text{ m}$ và $b = %s\\text{ m}$, tổng thể tích hai bể bằng $%s\\text{ m}^3$' % (a_val, b_val, k*(a_val**3) + b_val**3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi $a = %s$ và $b = %s$, ta có $V = %s \\cdot %s^3 + %s^3 = %s$ ($\\text{m}^3$).''' % (a_val, b_val, k3, a_val, b_val, V_cu_the))

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
