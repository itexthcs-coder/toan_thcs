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


def bt_dang14_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    m1, m2, m3 = 40 * k, 100 * k, 60 * k
    n = 200 * k

    noidungcauhoi = ('''Khảo sát thời gian (đơn vị: giờ) sử dụng mạng xã hội mỗi tuần của $%s$ học sinh, người ta chia thành $3$ nhóm có độ dài \textbf{không bằng nhau}: $[0; 5)$ có $%s$ học sinh; $[5; 10)$ có $%s$ học sinh; $[10; 20)$ có $%s$ học sinh. Để vẽ biểu đồ tần số tương đối dạng cột sao cho diện tích mỗi cột tỉ lệ với tần số tương đối của nhóm đó, chiều cao cột được tính theo công thức mật độ $y_i = \\dfrac{f_i}{l_i}$ (với $f_i$ là tần số tương đối tính theo $\\%%$, $l_i$ là độ dài nhóm).''' % (n, m1, m2, m3))

    list_nb_da_1 = [
        '\\True Tần số tương đối của nhóm $[10; 20)$ là $30\\%%$',
        'Tần số tương đối của nhóm $[10; 20)$ là $60\\%%$'
    ]
    loigiai_nb_1 = ('''Tần số tương đối của nhóm $[10; 20)$ là: $f_3 = \\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$.''' % (m3, n))

    list_th_da_1 = [
        '\\True Độ dài của nhóm $[10; 20)$ gấp đôi độ dài của nhóm $[5; 10)$',
        'Độ dài của nhóm $[10; 20)$ bằng độ dài của nhóm $[5; 10)$'
    ]
    loigiai_th_1 = ('''Độ dài nhóm $[10; 20)$ là $l_3 = 20 - 10 = 10$ (giờ), gấp đôi độ dài nhóm $[5; 10)$ là $l_2 = 10 - 5 = 5$ (giờ).''')

    list_vd_da_1 = [
        '\\True Trên biểu đồ, chiều cao của cột biểu diễn nhóm $[10; 20)$ thấp hơn chiều cao của cột biểu diễn nhóm $[0; 5)$',
        'Trên biểu đồ, chiều cao của cột biểu diễn nhóm $[10; 20)$ cao hơn chiều cao của cột biểu diễn nhóm $[0; 5)$'
    ]
    loigiai_vd_1 = ('''Ta có $y_1 = \\dfrac{20}{5} = 4$ và $y_3 = \\dfrac{30}{10} = 3 < 4$ nên cột biểu diễn nhóm $[10; 20)$ thấp hơn cột nhóm $[0; 5)$.''')

    list_vdc_da_1 = [
        '\\True Cột biểu diễn nhóm $[5; 10)$ có chiều cao gấp $2,5$ lần chiều cao của cột biểu diễn nhóm $[0; 5)$',
        'Cột biểu diễn nhóm $[5; 10)$ có chiều cao gấp $2$ lần chiều cao của cột biểu diễn nhóm $[0; 5)$'
    ]
    loigiai_vdc_1 = ('''Chiều cao cột nhóm $[5; 10)$ là $y_2 = \\dfrac{50}{5} = 10$. Tỉ số $\\dfrac{y_2}{y_1} = \\dfrac{10}{4} = 2,5$.''')

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
