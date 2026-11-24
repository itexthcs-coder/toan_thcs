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


def bt_dang20_p2_b1_c5_ds8(self):
    # Dạng 20: Vận dụng - Tổng hợp quy trình thống kê thực tiễn tại địa phương
    m1 = str(round(random.uniform(7.5, 9.5), 1)).replace('.', ',')
    m2 = str(round(random.uniform(10.0, 12.5), 1)).replace('.', ',')
    m3 = str(round(random.uniform(13.0, 16.5), 1)).replace('.', ',')

    bang_tn = (
        "\\begin{center}\n"
        "\\begin{tabular}{|l|c|c|c|}\n"
        "\\hline\n"
        "\\textbf{Người được hỏi} & \\textbf{Trình độ học vấn} & \\textbf{Nghề nghiệp mong muốn} & \\textbf{Thu nhập kì vọng (triệu đồng)} \\\\\n"
        "\\hline\n"
        "Bạn A & THPT & Kĩ thuật viên cơ khí & $%s$ \\\\\n"
        "\\hline\n"
        "Bạn B & Trung cấp & Thiết kế đồ họa & $%s$ \\\\\n"
        "\\hline\n"
        "Bạn C & Cao đẳng & Lập trình viên & $%s$ \\\\\n"
        "\\hline\n"
        "\\end{tabular}\n"
        "\\end{center}"
        % (m1, m2, m3)
    )

    noidungcauhoi = ('''Đoàn thanh niên xã muốn khảo sát nhu cầu học nghề của thanh niên trong độ tuổi từ $18$ đến $25$ tại địa phương. Kết quả thử nghiệm trên $3$ thanh niên đầu tiên được ghi lại trong bảng sau:
%s''' % bang_tn)

    nb_da_1_d = '\\True Cột \\textit{Trình độ học vấn} là dữ liệu không là số, có thể sắp thứ tự'
    nb_da_1_s = 'Cột \\textit{Trình độ học vấn} là dữ liệu không là số, không thể sắp thứ tự'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Trình độ học vấn (THCS, THPT, Trung cấp, Cao đẳng, Đại học) là dữ liệu không là số nhưng có thể sắp xếp theo thứ tự bậc đào tạo từ thấp đến cao.'''
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Cột \\textit{Nghề nghiệp mong muốn} là dữ liệu không là số, không thể sắp thứ tự'
    th_da_1_s = 'Cột \\textit{Nghề nghiệp mong muốn} là dữ liệu không là số, có thể sắp thứ tự'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Tên các ngành nghề mong muốn là dữ liệu định danh bằng chữ, không có sự phân chia thứ bậc cao thấp nên không thể sắp thứ tự.'''
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Cột \\textit{Thu nhập kì vọng (triệu đồng)} là số liệu liên tục'
    vd_da_1_s = 'Cột \\textit{Thu nhập kì vọng (triệu đồng)} là số liệu rời rạc'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Mức thu nhập kì vọng (tính theo triệu đồng) có thể nhận giá trị thực tùy ý trong một khoảng nên là số liệu liên tục.'''
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu đoàn thanh niên chỉ phỏng vấn các bạn đang học tại trường Cao đẳng nghề của huyện thì dữ liệu thu được không đảm bảo tính đại diện cho toàn bộ thanh niên từ $18$ đến $25$ tuổi trong xã'
    vdc_da_1_s = 'Nếu đoàn thanh niên chỉ phỏng vấn các bạn đang học tại trường Cao đẳng nghề của huyện thì dữ liệu thu được sẽ phản ánh chính xác nhu cầu của toàn bộ thanh niên từ $18$ đến $25$ tuổi trong xã'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '''Thanh niên từ $18$ đến $25$ tuổi trong xã còn bao gồm những người đang lao động tự do, học đại học hoặc chưa có việc làm; do đó chỉ hỏi sinh viên trường Cao đẳng nghề sẽ không đảm bảo tính đại diện.'''
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
