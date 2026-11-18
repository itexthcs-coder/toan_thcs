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


def bt_dang13_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            v_tai = random.choice([40, 45, 48, 50, 60])
            dv = random.choice([10, 12, 15, 20])
            v_con = v_tai + dv
            phut_sau = random.choice([30, 45])
            gio_sau = phut_sau / 60.0
            num = gio_sau * v_tai * v_con
            if num.is_integer() and int(num) % dv == 0:
                s_ab = int(num) // dv
                break

        gio_xp = random.choice([6, 7, 8])
        t_tai_di = s_ab / v_tai
        gio_den = gio_xp + int(t_tai_di)
        phut_den = int(round((t_tai_di - int(t_tai_di)) * 60))

        noidungcauhoi = ('''Lúc $%s\\text{ giờ}$ sáng, một xe tải chở hàng xuất phát từ kho A đi đến cảng B cách nhau $%s\\text{ km}$. Sau đó $%s\\text{ phút}$, một xe bán tải cũng xuất phát từ kho A đi đến cảng B trên cùng tuyến đường với vận tốc lớn hơn vận tốc xe tải là $%s\\text{ km/h}$. Hai xe đến cảng B cùng một lúc. Gọi $x\\text{ (km/h)}$ là vận tốc của xe tải ($x > 0$).''' % (fmt_num(gio_xp), fmt_num(s_ab), fmt_num(phut_sau), fmt_num(dv)))

        nb_da_1_d = '\\True Thời gian xe bán tải đi từ A đến B ít hơn thời gian xe tải đi là $%s\\text{ giờ}$' % (fmt_num(gio_sau))
        nb_da_1_s = 'Thời gian xe bán tải đi từ A đến B nhiều hơn thời gian xe tải đi là $%s\\text{ giờ}$' % (fmt_num(gio_sau))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì xe bán tải xuất phát sau xe tải $%s\\text{ phút} = %s\\text{ giờ}$ nhưng hai xe đến nơi cùng lúc nên thời gian đi của xe bán tải ít hơn xe tải là $%s\\text{ giờ}$.''' % (fmt_num(phut_sau), fmt_num(gio_sau), fmt_num(gio_sau)))

        th_da_1_d = '\\True Phương trình biểu thị mối quan hệ thời gian của hai xe là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_sau))
        th_da_1_s = 'Phương trình biểu thị mối quan hệ thời gian của hai xe là $\\frac{%s}{x} + \\frac{%s}{x + %s} = %s$' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_sau))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thời gian xe tải đi là $\\frac{%s}{x}\\text{ (giờ)}$, thời gian xe bán tải đi là $\\frac{%s}{x + %s}\\text{ (giờ)}$. \\\\ Ta có phương trình: $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$.''' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_sau)))

        vd_da_1_d = '\\True Vận tốc của xe tải là $%s\\text{ km/h}$ và vận tốc của xe bán tải là $%s\\text{ km/h}$' % (fmt_num(v_tai), fmt_num(v_con))
        vd_da_1_s = 'Vận tốc của xe tải là $%s\\text{ km/h}$ và vận tốc của xe bán tải là $%s\\text{ km/h}$' % (fmt_num(v_con), fmt_num(v_tai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        c_eq = int(s_ab * dv / gio_sau)
        delta = dv**2 + 4 * c_eq
        sqrt_delta = int(math.isqrt(delta))
        loigiai_vd_1 = ('''Khử mẫu phương trình $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$, ta được: $x^2 + %sx - %s = 0$. \\\\ Ta có $\\Delta = %s^2 + 4 \\cdot %s = %s$, $\\sqrt{\\Delta} = %s$. \\\\ Nghiệm dương của phương trình là $x = %s\\text{ (km/h)}$. Vậy vận tốc xe tải là $%s\\text{ km/h}$, vận tốc xe bán tải là $%s + %s = %s\\text{ km/h}$.''' % (fmt_num(s_ab), fmt_num(s_ab), fmt_num(dv), fmt_num(gio_sau), fmt_num(dv), fmt_num(c_eq), fmt_num(dv), fmt_num(c_eq), fmt_num(delta), fmt_num(sqrt_delta), fmt_num(v_tai), fmt_num(v_tai), fmt_num(v_tai), fmt_num(dv), fmt_num(v_con)))

        vdc_da_1_d = '\\True Hai xe cùng có mặt tại cảng B vào lúc $%s\\text{ giờ } %s\\text{ phút}$ sáng' % (fmt_num(gio_den), fmt_num(phut_den))
        vdc_da_1_s = 'Hai xe cùng có mặt tại cảng B vào lúc $%s\\text{ giờ } %s\\text{ phút}$ sáng' % (fmt_num(gio_den + 1), fmt_num(phut_den))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Thời gian xe tải đi từ A đến B là $\\frac{%s}{%s} = %s\\text{ giờ} = %s\\text{ giờ } %s\\text{ phút}$. \\\\ Xuất phát lúc $%s\\text{ giờ}$ nên hai xe cùng tới cảng B vào lúc $%s\\text{ giờ } %s\\text{ phút}$ sáng.''' % (fmt_num(s_ab), fmt_num(v_tai), fmt_num(t_tai_di), fmt_num(int(t_tai_di)), fmt_num(phut_den), fmt_num(gio_xp), fmt_num(gio_den), fmt_num(phut_den)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

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
