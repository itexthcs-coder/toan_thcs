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


def bt_dang3_p2_b1_c5_ds8(self):
    # Dạng 3: Kiểm tra tính hợp lí và bản chất số liệu trong đời sống gia đình
    sai_bg = "%s,5" % random.randint(1, 2)
    e1 = str(round(random.uniform(150.2, 189.8), 1)).replace('.', ',')
    e2 = str(round(random.uniform(190.5, 225.4), 1)).replace('.', ',')
    e3 = str(round(random.uniform(160.1, 185.9), 1)).replace('.', ',')
    e4 = str(round(random.uniform(230.2, 265.8), 1)).replace('.', ',')

    noidungcauhoi = ('''Bạn Mai thực hiện phỏng vấn $4$ gia đình hàng xóm về sinh hoạt hằng ngày và ghi lại hai dãy dữ liệu sau:\\\\
- \\textbf{Dãy 1} (Số bộ bàn ghế trong phòng khách): $1;\\; 2;\\; 1;\\; %s$.\\\\
- \\textbf{Dãy 2} (Lượng điện tiêu thụ trong tháng của gia đình, đơn vị: $\\text{kWh}$): $%s;\\; %s;\\; %s;\\; %s$.'''
                     % (sai_bg, e1, e2, e3, e4))

    nb_da_1_d = '\\True Phương pháp thu thập dữ liệu của bạn Mai là phương pháp thu thập trực tiếp'
    nb_da_1_s = 'Phương pháp thu thập dữ liệu của bạn Mai là phương pháp thu thập gián tiếp'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Bạn Mai trực tiếp phỏng vấn các gia đình hàng xóm nên đây là phương pháp thu thập dữ liệu trực tiếp.'''
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Dãy $1$ là số liệu rời rạc và có giá trị $%s$ không hợp lí' % sai_bg
    th_da_1_s = 'Dãy $1$ là số liệu liên tục và tất cả các giá trị đều hợp lí'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Số bộ bàn ghế trong phòng khách thu được từ phép đếm nên là số liệu rời rạc, chỉ nhận giá trị nguyên không âm; do đó giá trị thập phân $%s$ là không hợp lí.''' % sai_bg
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Dãy $2$ là số liệu liên tục và tất cả các giá trị đều hợp lí'
    vd_da_1_s = 'Dãy $2$ là số liệu rời rạc và có giá trị không hợp lí'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Lượng điện tiêu thụ (tính theo $\\text{kWh}$) là đại lượng đo lường có thể nhận giá trị thực tùy ý trong một khoảng nên là số liệu liên tục; các mức tiêu thụ $%s;\\; %s;\\; %s;\\; %s\\,\\text{kWh}$ đều phù hợp với thực tế sinh hoạt hộ gia đình.''' % (e1, e2, e3, e4)
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Dù đổi đơn vị đo ở Dãy $2$ sang $\\text{Wh}$ thì Dãy $2$ vẫn là số liệu liên tục'
    vdc_da_1_s = 'Nếu đổi đơn vị đo ở Dãy $2$ sang $\\text{Wh}$ để các số đều nguyên thì Dãy $2$ trở thành số liệu rời rạc'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '''Việc thay đổi đơn vị đo từ $\\text{kWh}$ sang $\\text{Wh}$ không làm thay đổi bản chất đại lượng đo lường liên tục của điện năng tiêu thụ.'''
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
