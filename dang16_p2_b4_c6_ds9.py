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


def bt_dang16_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (6, 12, 4, 0),
            (8, 12, 4, 48),
            (10, 15, 6, 0),
            (12, 24, 8, 0),
            (6, 10, 3, 45)
        ]
        t1, t2, gio_chung, phut_chung = random.choice(bo_so)
        chenh = t2 - t1
        t_chung_rat = Rational(t1 * t2, t1 + t2)
        nang_suat_chung = Rational(1, t_chung_rat)

        str_tg_chung = ('%s\\text{ giờ } %s\\text{ phút}' % (fmt_num(gio_chung), fmt_num(phut_chung))) if phut_chung > 0 else ('%s\\text{ giờ}' % fmt_num(gio_chung))

        noidungcauhoi = ('''Hai đội công nhân cùng thi công trải nhựa một đoạn đường. Nếu cả hai đội cùng làm chung thì sau $%s$ sẽ hoàn thành toàn bộ công việc. Nếu làm riêng thì đội thứ nhất hoàn thành công việc nhanh hơn đội thứ hai là $%s\\text{ giờ}$. Gọi $x\\text{ (giờ)}$ là thời gian đội thứ nhất làm riêng để hoàn thành công việc.''' % (str_tg_chung, fmt_num(chenh)))

        nb_da_1_d = '\\True Điều kiện thích hợp của ẩn $x$ là $x > 0$'
        nb_da_1_s = 'Điều kiện thích hợp của ẩn $x$ là $x > %s$' % (fmt_num(chenh))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì $x$ là thời gian đội thứ nhất làm riêng và đội thứ hai mất $x + %s$ (giờ) nên điều kiện của ẩn chỉ cần $x > 0$.''' % (fmt_num(chenh)))

        th_da_1_d = '\\True Trong $1\\text{ giờ}$, cả hai đội làm chung được $%s$ (công việc)' % (latex(nang_suat_chung))
        th_da_1_s = 'Trong $1\\text{ giờ}$, cả hai đội làm chung được $%s$ (công việc)' % (latex(t_chung_rat))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Đổi $%s = %s\\text{ giờ}$. Trong $1\\text{ giờ}$, cả hai đội làm chung được $1 : %s = %s$ (công việc).''' % (str_tg_chung, latex(t_chung_rat), latex(t_chung_rat), latex(nang_suat_chung)))

        vd_da_1_d = '\\True Phương trình biểu thị năng suất làm chung của hai đội là $\\frac{1}{x} + \\frac{1}{x + %s} = %s$' % (fmt_num(chenh), latex(nang_suat_chung))
        vd_da_1_s = 'Phương trình biểu thị năng suất làm chung của hai đội là $\\frac{1}{x} + \\frac{1}{x - %s} = %s$' % (fmt_num(chenh), latex(nang_suat_chung))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Trong $1\\text{ giờ}$, đội một làm được $\\frac{1}{x}$ công việc, đội hai làm được $\\frac{1}{x + %s}$ công việc. \\\\ Ta có phương trình: $\\frac{1}{x} + \\frac{1}{x + %s} = %s$.''' % (fmt_num(chenh), fmt_num(chenh), latex(nang_suat_chung)))

        vdc_da_1_d = '\\True Nếu làm riêng, đội thứ hai mất $%s\\text{ giờ}$ để trải nhựa xong đoạn đường đó' % (fmt_num(t2))
        vdc_da_1_s = 'Nếu làm riêng, đội thứ hai mất $%s\\text{ giờ}$ để trải nhựa xong đoạn đường đó' % (fmt_num(t1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        tu_s = nang_suat_chung.p
        mau_s = nang_suat_chung.q
        loigiai_vdc_1 = ('''Quy đồng khử mẫu phương trình $\\frac{1}{x} + \\frac{1}{x + %s} = \\frac{%s}{%s}$, ta được: \\\\ $%s(2x + %s) = %sx(x + %s) \\Leftrightarrow %sx^2 + %sx - %s = 0$. \\\\ Giải phương trình bậc hai này ta tìm được nghiệm dương duy nhất là $x = %s\\text{ (giờ)}$. \\\\ Vậy đội thứ nhất làm riêng mất $%s\\text{ giờ}$, đội thứ hai làm riêng mất $%s + %s = %s\\text{ giờ}$.''' % (fmt_num(chenh), fmt_num(tu_s), fmt_num(mau_s), fmt_num(mau_s), fmt_num(chenh), fmt_num(tu_s), fmt_num(chenh), fmt_num(tu_s), fmt_num(tu_s * chenh - 2 * mau_s), fmt_num(mau_s * chenh), fmt_num(t1), fmt_num(t1), fmt_num(t1), fmt_num(chenh), fmt_num(t2)))

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
