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


def bt_dang16_p2_b2_c4_hh9(self):
    qd = 200
    goc = 21
    rad = math.radians(goc)
    sau_str = str(Decimal(str(qd * math.sin(rad))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    qd2_val = qd / math.sin(rad)
    qd2_str = str(Decimal(str(qd2_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    tg_str = str(Decimal(str(qd2_val / 2.5)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    noidungcauhoi = ('''Trong một đợt diễn tập tìm kiếm cứu nạn trên biển, một tàu lặn xuất phát từ mặt nước biển và di chuyển theo đường thẳng tạo với mặt biển một góc nghiêng $%s^\\circ$ để lặn xuống khảo sát đáy biển. Xét tính đúng sai của các khẳng định sau:'''
                     % (goc))

    # a)
    nb_da_1_d = '\\True Khi tàu lặn đi được quãng đường $%s\\text{ m}$ theo phương lặn, độ sâu của tàu so với mặt nước biển (làm tròn đến mét) là $%s\\text{ m}$' % (qd, sau_str)
    nb_da_1_s = 'Khi tàu lặn đi được quãng đường $%s\\text{ m}$ theo phương lặn, độ sâu của tàu so với mặt nước biển (làm tròn đến mét) là $187\\text{ m}$' % qd
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Độ sâu của tàu so với mặt nước biển là $h = %s \\cdot \\sin %s^\\circ \\approx 71,67\\text{ (m)} \\approx %s\\text{ (m)}$.''' % (qd, goc, sau_str))
    list_nb_2 = [loigiai_nb_1]

    # b)
    th_da_1_d = '\\True Khi tàu lặn đạt độ sâu $%s\\text{ m}$ so với mặt nước biển, quãng đường tàu đã di chuyển theo phương lặn (làm tròn đến mét) là $%s\\text{ m}$' % (qd, qd2_str)
    th_da_1_s = 'Khi tàu lặn đạt độ sâu $%s\\text{ m}$ so với mặt nước biển, quãng đường tàu đã di chuyển theo phương lặn (làm tròn đến mét) là $521\\text{ m}$' % qd
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Khi ở độ sâu $%s\\text{ m}$, quãng đường tàu đã di chuyển là $s = \\dfrac{%s}{\\sin %s^\\circ} \\approx 558,09\\text{ (m)} \\approx %s\\text{ (m)}$.''' % (qd, qd, goc, qd2_str))
    list_th_2 = [loigiai_th_1]

    # c)
    vd_da_1_d = '\\True Với vận tốc lặn không đổi $9\\text{ km/h}$ (tức $2,5\\text{ m/s}$), thời gian để tàu lặn từ mặt nước xuống độ sâu $%s\\text{ m}$ (làm tròn đến giây) là $%s\\text{ giây}$' % (qd, tg_str)
    vd_da_1_s = 'Với vận tốc lặn không đổi $9\\text{ km/h}$, thời gian để tàu lặn xuống độ sâu $%s\\text{ m}$ là $150\\text{ giây}$' % qd
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Đổi $9\\text{ km/h} = 2,5\\text{ m/s}$. Thời gian tàu lặn xuống độ sâu $%s\\text{ m}$ là $t \\approx \\dfrac{558,09}{2,5} \\approx 223,24\\text{ (giây)} \\approx %s\\text{ (giây)}$.''' % (qd, tg_str))
    list_vd_2 = [loigiai_vd_1]

    # d)
    vdc_da_1_d = '\\True Nếu tàu giữ nguyên vận tốc $9\\text{ km/h}$ nhưng điều chỉnh góc lặn lớn hơn $%s^\\circ$ so với mặt nước biển thì thời gian đạt độ sâu $%s\\text{ m}$ sẽ ngắn hơn $%s\\text{ giây}$' % (goc, qd, tg_str)
    vdc_da_1_s = 'Nếu tàu giữ nguyên vận tốc $9\\text{ km/h}$ nhưng điều chỉnh góc lặn nhỏ hơn $%s^\\circ$ so với mặt nước biển thì thời gian đạt độ sâu $%s\\text{ m}$ sẽ ngắn hơn $%s\\text{ giây}$' % (goc, qd, tg_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi góc lặn $\\alpha$ tăng thì $\\sin \\alpha$ tăng, làm quãng đường lặn $s = \\dfrac{%s}{\\sin \\alpha}$ giảm đi nên thời gian lặn sẽ ngắn hơn.''' % qd)
    list_vdc_2 = [loigiai_vdc_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
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
