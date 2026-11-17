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


def bt_dang12_p2_b1_c6_ds9(self):
    k_val = random.choice([1, 2, 3])
    n_val = k_val ** 2 + 1
    a_sym = k_val - sqrt(n_val)
    x_conj = k_val + sqrt(n_val)
    y_conj = expand(a_sym * (x_conj ** 2))

    noidungcauhoi = (
        'Cho hàm số $y = (%s)x^2$.' % (latex(a_sym))
    )

    nb_da_1_d = '\\True Hệ số $a = %s$ là một số âm' % (latex(a_sym))
    nb_da_1_s = 'Hệ số $a = %s$ là một số dương' % (latex(a_sym))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Ta có $%s = \\sqrt{%s}$ và $%s < %s$ nên $\\sqrt{%s} < \\sqrt{%s}$, suy ra hệ số $a = %s < 0$.' % (str(k_val), str(k_val**2), str(k_val**2), str(n_val), str(k_val**2), str(n_val), latex(a_sym))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đồ thị của hàm số nằm hoàn toàn phía dưới trục hoành (trừ gốc toạ độ $O$)'
    th_da_1_s = 'Đồ thị của hàm số nằm hoàn toàn phía trên trục hoành (trừ gốc toạ độ $O$)'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Vì hệ số $a = %s < 0$ nên đồ thị của hàm số là một đường parabol nằm phía dưới trục hoành và đi qua gốc toạ độ $O(0;0)$.' % (latex(a_sym))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Với mọi $x \\ne 0$, ta luôn có $(%s)x^2 < 0$' % (latex(a_sym))
    vd_da_1_s = 'Với mọi $x \\ne 0$, ta luôn có $(%s)x^2 > 0$' % (latex(a_sym))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Với mọi $x \\ne 0$, ta có $x^2 > 0$ và $%s < 0$ nên tích $(%s)x^2 < 0$.' % (latex(a_sym), latex(a_sym))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khi $x = %s$, giá trị của hàm số là $y = %s$' % (latex(x_conj), latex(y_conj))
    vdc_da_1_s = 'Khi $x = %s$, giá trị của hàm số là $y = -1$' % (latex(x_conj))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Thay $x = %s$ vào công thức hàm số ta được: \\\\ $y = (%s)(%s)^2 = [(%s)(%s)](%s) = (%s - %s)(%s) = -1 \\cdot (%s) = %s$.' % (latex(x_conj), latex(a_sym), latex(x_conj), latex(a_sym), latex(x_conj), latex(x_conj), str(k_val**2), str(n_val), latex(x_conj), latex(x_conj), latex(y_conj))
    )
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
