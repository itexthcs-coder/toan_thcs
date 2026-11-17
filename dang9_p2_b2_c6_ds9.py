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


def bt_dang9_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        x_kep = Rational(-random.choice([3, 4, 5]), random.choice([2, 7]))
        d_val = random.choice([13, 17, 21])
        val_x1 = (1 + math.sqrt(d_val)) / 4
        val_round = str(Decimal(str(val_x1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        val_wrong = str(Decimal(str(val_x1 + 0.12)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = (('Một học sinh sử dụng máy tính cầm tay để giải ba phương trình bậc hai và thu được kết quả hiển thị trên màn hình như sau: \\\\ ' +
                          '\\begin{center}\n' +
                          '\\begin{tabular}{|c|l|}\n' +
                          '\\hline\n' +
                          '\\textbf{Phương trình} & \\textbf{Kết quả hiển thị trên màn hình} \\\\ \n' +
                          '\\hline\n' +
                          '(I) & Chỉ hiển thị một giá trị $X = %s$ \\\\ \n' +
                          '\\hline\n' +
                          '(II) & Hiển thị $X_1 = \\frac{1}{2} + \\frac{\\sqrt{5}}{2}i$ và $X_2 = \\frac{1}{2} - \\frac{\\sqrt{5}}{2}i$ \\\\ \n' +
                          '\\hline\n' +
                          '(III) & Hiển thị $X_1 = \\frac{1 + \\sqrt{%s}}{4}$ và $X_2 = \\frac{1 - \\sqrt{%s}}{4}$ \\\\ \n' +
                          '\\hline\n' +
                          '\\end{tabular}\n' +
                          '\\end{center}\n' +
                          'Xét tính đúng sai của các khẳng định sau:') % (latex(x_kep), d_val, d_val))

        nb_da_1_d = '\\True Để chuyển kết quả $X_1$ ở phương trình (III) sang số thập phân gần đúng, học sinh đó cần bấm phím $\\text{S} \\Leftrightarrow \\text{D}$'
        nb_da_1_s = 'Để chuyển kết quả $X_1$ ở phương trình (III) sang số thập phân gần đúng, học sinh đó cần bấm phím $\\text{AC}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Theo quy tắc sử dụng máy tính cầm tay, phím $\\text{S} \\Leftrightarrow \\text{D}$ được dùng để chuyển đổi hiển thị kết quả từ dạng căn thức/phân số sang số thập phân.')

        th_da_1_d = '\\True Phương trình (I) có biệt thức $\\Delta = 0$'
        th_da_1_s = 'Phương trình (I) vô nghiệm vì chỉ hiển thị một chữ $X$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Máy tính chỉ hiển thị một kết quả $X = %s$ (không có $X_1, X_2$) nghĩa là phương trình (I) có nghiệm kép, tương đương với biệt thức $\\Delta = 0$.' % (latex(x_kep)))

        vd_da_1_d = '\\True Phương trình (II) vô nghiệm trên tập số thực'
        vd_da_1_s = 'Phương trình (II) có hai nghiệm phân biệt'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Kết quả hiển thị trên màn hình có chứa đơn vị ảo $i$ nên phương trình (II) vô nghiệm trong tập số thực.')

        vdc_da_1_d = '\\True Giá trị gần đúng làm tròn đến hàng phần trăm của nghiệm $X_1$ ở phương trình (III) là $%s$' % (val_round)
        vdc_da_1_s = 'Giá trị gần đúng làm tròn đến hàng phần trăm của nghiệm $X_1$ ở phương trình (III) là $%s$' % (val_wrong)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Sử dụng máy tính cầm tay tính giá trị $\\frac{1 + \\sqrt{%s}}{4}$ và làm tròn đến chữ số thập phân thứ hai (hàng phần trăm), ta được kết quả xấp xỉ là $%s$.' % (d_val, val_round))

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

        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
