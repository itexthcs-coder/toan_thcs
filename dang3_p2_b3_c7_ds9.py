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


def bt_dang3_p2_b3_c7_ds9(self):
    n = random.choice([200, 400])
    m1 = (n * 45) // 200
    m3 = (n * 25) // 100
    m4 = (n * 10) // 100
    hieu_34 = m3 - m4

    noidungcauhoi = ('''Một siêu thị điện máy khảo sát $%s$ khách hàng về mức chi tiêu (đơn vị: triệu đồng) khi mua sắm trong dịp lễ và thu được bảng tần số tương đối ghép nhóm sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức chi tiêu (triệu đồng) & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ \\\\
\\hline
Tần số tương đối & $22,5\\%%$ & $42,5\\%%$ & $25\\%%$ & $10\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (n))

    list_nb_da_1 = [
        '\\True Nhóm khách hàng chi tiêu từ $2$ triệu đến dưới $4$ triệu đồng chiếm tỉ lệ lớn nhất',
        'Nhóm khách hàng chi tiêu từ $4$ triệu đến dưới $6$ triệu đồng chiếm tỉ lệ lớn nhất'
    ]
    loigiai_nb_1 = ('''Nhóm $[2; 4)$ có tần số tương đối bằng $42,5\\%%$, lớn nhất trong tất cả các nhóm.''')

    list_th_da_1 = [
        '\\True Có $%s$ khách hàng chi tiêu dưới $2$ triệu đồng' % m1,
        'Có $%s$ khách hàng chi tiêu dưới $2$ triệu đồng' % (m1 + 20)
    ]
    loigiai_th_1 = ('''Số khách hàng chi tiêu dưới $2$ triệu đồng (thuộc nhóm $[0; 2)$) là: $\\dfrac{%s \\cdot 22,5}{100} = %s$ (khách hàng).''' % (n, m1))

    list_vd_da_1 = [
        '\\True Số khách hàng chi tiêu từ $4$ triệu đồng trở lên ít hơn số khách hàng chi tiêu từ $2$ triệu đến dưới $4$ triệu đồng',
        'Số khách hàng chi tiêu từ $4$ triệu đồng trở lên nhiều hơn số khách hàng chi tiêu từ $2$ triệu đến dưới $4$ triệu đồng'
    ]
    loigiai_vd_1 = ('''Tỉ lệ khách hàng chi tiêu từ $4$ triệu đồng trở lên là $25\\%% + 10\\%% = 35\\%% < 42,5\\%%$ nên số khách hàng này ít hơn nhóm $[2; 4)$.''')

    list_vdc_da_1 = [
        '\\True Nhóm $[4; 6)$ có nhiều hơn nhóm $[6; 8)$ đúng $%s$ khách hàng' % hieu_34,
        'Nhóm $[4; 6)$ có nhiều hơn nhóm $[6; 8)$ đúng $%s$ khách hàng' % (hieu_34 + 15)
    ]
    loigiai_vdc_1 = ('''Số khách hàng nhóm $[4; 6)$ là $\\dfrac{%s \\cdot 25}{100} = %s$; nhóm $[6; 8)$ là $\\dfrac{%s \\cdot 10}{100} = %s$. Hiệu số là $%s - %s = %s$ (khách hàng).''' % (n, m3, n, m4, m3, m4, hieu_34))

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
