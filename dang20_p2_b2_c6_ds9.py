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


def bt_dang20_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        t = symbols('t')
        t1_val = random.choice([2, 3])
        t2_val = t1_val + random.choice([2, 4])
        t_end = t1_val + t2_val
        b_val = 0.4 * t_end
        b_str = str(round(b_val, 1)).replace('.', ',')

        c_threshold = round(0.4 * t1_val * t2_val, 1)
        c_th_str = str(c_threshold).replace('.', ',')

        t_test = 1
        c_test = round(-0.4 * (t_test**2) + b_val * t_test, 1)
        c_test_str = str(c_test).replace('.', ',')

        duration = t2_val - t1_val

        noidungcauhoi = ('Sau khi một bệnh nhân uống một liều thuốc giảm đau, nồng độ thuốc $C$ (tính bằng $\\text{mg/lít}$) trong máu sau $t$ giờ được ước tính theo mô hình bậc hai $C(t) = -0,4t^2 + %st$ với $0 \\le t \\le %s$. Xét tính đúng sai của các khẳng định sau:' % (b_str, t_end))

        nb_da_1_d = '\\True Sau $1$ giờ kể từ khi uống thuốc, nồng độ thuốc trong máu đạt $%s \\text{ mg/lít}$' % (c_test_str)
        nb_da_1_s = 'Sau $1$ giờ kể từ khi uống thuốc, nồng độ thuốc trong máu đạt $%s \\text{ mg/lít}$' % (b_str)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thay $t = 1$ vào công thức ta được: $C(1) = -0,4 \\cdot 1^2 + %s \\cdot 1 = %s \\text{ (mg/lít)}$.' % (b_str, c_test_str))

        th_da_1_d = '\\True Sau đúng $%s$ giờ kể từ khi uống, lượng thuốc này được đào thải hoàn toàn khỏi máu ($C = 0$)' % (t_end)
        th_da_1_s = 'Sau đúng $%s$ giờ kể từ khi uống, lượng thuốc này được đào thải hoàn toàn khỏi máu ($C = 0$)' % (t_end // 2)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Giải phương trình $-0,4t^2 + %st = 0 \\Leftrightarrow -0,4t(t - %s) = 0 \\Leftrightarrow t = 0$ (lúc mới uống) hoặc $t = %s$ (đào thải hết).' % (b_str, t_end, t_end))

        vd_da_1_d = '\\True Thuốc chỉ phát huy tác dụng giảm đau khi nồng độ trong máu đạt từ $%s \\text{ mg/lít}$ trở lên, thời điểm đầu tiên thuốc bắt đầu có tác dụng là sau $%s$ giờ kể từ khi uống' % (c_th_str, t1_val)
        vd_da_1_s = 'Thuốc chỉ phát huy tác dụng giảm đau khi nồng độ trong máu đạt từ $%s \\text{ mg/lít}$ trở lên, thời điểm đầu tiên thuốc bắt đầu có tác dụng là sau $%s$ giờ kể từ khi uống' % (c_th_str, t2_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Giải phương trình $-0,4t^2 + %st = %s \\Leftrightarrow 0,4t^2 - %st + %s = 0 \\Leftrightarrow t^2 - %st + %s = 0 \\Leftrightarrow t_1 = %s$ hoặc $t_2 = %s$. \\\\ Vậy thời điểm đầu tiên thuốc bắt đầu có tác dụng là sau $%s$ giờ.' % (b_str, c_th_str, b_str, c_th_str, t_end, t1_val * t2_val, t1_val, t2_val, t1_val))

        vdc_da_1_d = '\\True Tổng thời gian thuốc duy trì tác dụng giảm đau (nồng độ $\\ge %s \\text{ mg/lít}$) là $%s$ giờ' % (c_th_str, duration)
        vdc_da_1_s = 'Tổng thời gian thuốc duy trì tác dụng giảm đau (nồng độ $\\ge %s \\text{ mg/lít}$) là $%s$ giờ' % (c_th_str, duration + 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Nồng độ thuốc đạt từ $%s \\text{ mg/lít}$ trở lên trong khoảng thời gian từ $t = %s$ giờ đến $t = %s$ giờ. \\\\ Vậy tổng thời gian duy trì tác dụng là $%s - %s = %s$ giờ.' % (c_th_str, t1_val, t2_val, t2_val, t1_val, duration))

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
