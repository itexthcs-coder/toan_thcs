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


def bt_dang10_p2_b1_c1_ds8(self):
    # Dạng 10: Rút gọn hiệu hai đơn thức đồng dạng phân số, tính giá trị và xét dấu biểu thức
    mau = random.choice([2, 3, 5])
    k = random.choice([2, 3, 4])
    tu1 = 1
    tu2 = tu1 + k * mau
    m = random.choice([2, 4])
    n = random.choice([4, 6])
    x0 = random.choice([-2, 2])
    gt_s = -k * (x0 ** m) * (1 ** n)

    noidungcauhoi = ('Cho biểu thức $S = \\frac{%s}{%s}x^{%s}y^{%s} - \\frac{%s}{%s}x^{%s}y^{%s}$.'
                     % (tu1, mau, m, n, tu2, mau, m, n))

    nb_da_1_d = '\\True Hai hạng tử của $S$ là hai đơn thức đồng dạng.'
    nb_da_1_s = 'Hai hạng tử của $S$ không phải là hai đơn thức đồng dạng.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Hai hạng tử đều có hệ số khác $0$ và có cùng phần biến là $x^{%s}y^{%s}$ nên chúng là hai đơn thức đồng dạng.'
                    % (m, n))

    th_da_1_d = '\\True Sau khi rút gọn, ta được $S = -%sx^{%s}y^{%s}$.' % (k, m, n)
    th_da_1_s = 'Sau khi rút gọn, ta được $S = %sx^{%s}y^{%s}$.' % (k, m, n)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Ta có: $S = \\left(\\frac{%s}{%s} - \\frac{%s}{%s}\\right)x^{%s}y^{%s} = \\frac{-%s}{%s}x^{%s}y^{%s} = -%sx^{%s}y^{%s}$.'
                    % (tu1, mau, tu2, mau, m, n, k * mau, mau, m, n, k, m, n))

    vd_da_1_d = '\\True Giá trị của $S$ tại $x = %s$ và $y = 1$ bằng $%s$.' % (x0, gt_s)
    vd_da_1_s = 'Giá trị của $S$ tại $x = %s$ và $y = 1$ bằng $%s$.' % (x0, -gt_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Thay $x = %s$ và $y = 1$ vào $S = -%sx^{%s}y^{%s}$, ta được: $S = -%s \\cdot (%s)^{%s} \\cdot 1^{%s} = -%s \\cdot %s \\cdot 1 = %s$.'
                    % (x0, k, m, n, k, x0, m, n, k, x0 ** m, gt_s))

    vdc_da_1_d = '\\True Với mọi giá trị của $x \\neq 0$ và $y \\neq 0$, giá trị của biểu thức $S$ luôn âm.'
    vdc_da_1_s = 'Có giá trị của $x \\neq 0$ và $y \\neq 0$ làm cho biểu thức $S$ nhận giá trị dương.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Vì $%s$ và $%s$ đều là số mũ chẵn nên $x^{%s} > 0$ và $y^{%s} > 0$ với mọi $x \\neq 0, y \\neq 0$. Do đó $S = -%sx^{%s}y^{%s} < 0$ với mọi $x \\neq 0, y \\neq 0$.'
                     % (m, n, m, n, k, m, n))

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

    combined = list(zip([nb_da_1, th_da_1, vd_da_1, vdc_da_1],
                        [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers[0]) + '}\n'
               '{' + str(shuffled_answers[1]) + '}\n'
               '{' + str(shuffled_answers[2]) + '}\n'
               '{' + str(shuffled_answers[3]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions[0]) + '\n'
               '\\item ' + str(shuffled_solutions[1]) + '\n'
               '\\item ' + str(shuffled_solutions[2]) + '\n'
               '\\item ' + str(shuffled_solutions[3]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
