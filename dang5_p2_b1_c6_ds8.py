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


def bt_dang5_p2_b1_c6_ds8(self):
    # Dạng 5: Kiểm tra tính bằng nhau của hai phân thức có sử dụng quy tắc đổi dấu cả tử và mẫu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([6, 7, 8, 9])
        
        noidungcauhoi = ('Cho phân thức $K = \\dfrac{%s - x}{x - %s}$ (với $x \\neq %s$). Xét tính đúng sai của các khẳng định sau:'
                         % (a, b, b))
        
        nb_da_1_d = '\\True $\\dfrac{%s - x}{x - %s} = \\dfrac{x - %s}{%s - x}$' % (a, b, a, b)
        nb_da_1_s = '$\\dfrac{%s - x}{x - %s} = \\dfrac{x - %s}{x - %s}$' % (a, b, a, b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Khi đổi dấu cả tử thức và mẫu thức của một phân thức thì được một phân thức bằng phân thức đã cho, hoặc kiểm tra tích chéo: $(%s - x)(%s - x) = (x - %s)(x - %s)$.' % (a, b, b, a)
        loigiai_nb_s = 'Sai. Nếu chỉ đổi dấu tử thức mà giữ nguyên mẫu thức thì hai phân thức đối nhau chứ không bằng nhau.'
        
        th_da_1_d = '\\True $\\dfrac{%s - x}{x - %s} = \\dfrac{-(x - %s)}{x - %s}$' % (a, b, a, b)
        th_da_1_s = '$\\dfrac{%s - x}{x - %s} = \\dfrac{-(x + %s)}{x - %s}$' % (a, b, a, b)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Vì $%s - x = -(x - %s)$ nên tử thức của hai phân thức bằng nhau và mẫu thức giữ nguyên.' % (a, a)
        loigiai_th_s = 'Sai. Ta có $%s - x = -(x - %s)$, không bằng $-(x + %s)$.' % (a, a, a)
        
        vd_da_1_d = '\\True $\\dfrac{%s - x}{x - %s} \\neq \\dfrac{%s - x}{%s - x}$ (với $x \\neq %s$)' % (a, b, a, b, a)
        vd_da_1_s = '$\\dfrac{%s - x}{x - %s} = \\dfrac{%s - x}{%s - x}$ với mọi $x \\neq %s$' % (a, b, a, b, b)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Giữ nguyên tử thức mà đổi dấu mẫu thức thì không thu được phân thức bằng phân thức ban đầu (khi tử thức khác $0$).'
        loigiai_vd_s = 'Sai. Hai mẫu thức $x - %s$ và $%s - x$ đối nhau trong khi tử thức $%s - x$ giống nhau nên hai phân thức đối nhau.' % (b, b, a)
        
        vdc_da_1_d = '\\True $\\dfrac{%s - x}{x - %s} = \\dfrac{(x - %s)^2}{(x - %s)(%s - x)}$ (với $x \\neq %s, x \\neq %s$)' % (a, b, a, b, a, a, b)
        vdc_da_1_s = '$\\dfrac{%s - x}{x - %s} = \\dfrac{(x - %s)^2}{(x - %s)(x - %s)}$ (với $x \\neq %s, x \\neq %s$)' % (a, b, a, b, a, a, b)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Ta có $(%s - x)(x - %s)(%s - x) = (x - %s)^2(x - %s)$ nên hai phân thức bằng nhau.' % (a, b, a, a, b)
        loigiai_vdc_s = 'Sai. Tích chéo cho thấy $(%s - x)(x - %s)(x - %s) = -(x - %s)^2(x - %s) \\neq (x - %s)(x - %s)^2$.' % (a, b, a, a, b, b, a)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
