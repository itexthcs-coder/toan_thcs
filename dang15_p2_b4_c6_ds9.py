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


def bt_dang15_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        von_1 = random.choice([100, 150, 200])
        von_2 = random.choice([50, 80, 100])
        lai_pt = random.choice([5, 6, 7, 8, 10])
        x_val = Decimal(lai_pt) / Decimal(100)
        t_val = Decimal(1) + x_val
        tong_nhan = (Decimal(von_1) * t_val + Decimal(von_2)) * t_val

        noidungcauhoi = ('''Đầu năm thứ nhất, anh Tuấn gửi tiết kiệm $%s\\text{ triệu đồng}$ vào ngân hàng với kì hạn $12\\text{ tháng}$. Hết năm thứ nhất, anh Tuấn không rút tiền ra mà tiếp tục gửi lại toàn bộ gốc và lãi, đồng thời nộp thêm vào sổ tiết kiệm $%s\\text{ triệu đồng}$ nữa cũng với kì hạn $12\\text{ tháng}$. Hết năm thứ hai, anh Tuấn tất toán sổ và nhận được tổng cộng $%s\\text{ triệu đồng}$. Giả sử lãi suất không đổi trong suốt $2\\text{ năm}$ là $x$ ($x > 0$, viết dưới dạng số thập phân).''' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan)))

        nb_da_1_d = '\\True Tổng số tiền gốc bắt đầu tính lãi ở năm thứ hai là $%s(1 + x) + %s$ (triệu đồng)' % (fmt_num(von_1), fmt_num(von_2))
        nb_da_1_s = 'Tổng số tiền gốc bắt đầu tính lãi ở năm thứ hai là $%s + %s$ (triệu đồng)' % (fmt_num(von_1), fmt_num(von_2))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Sau năm thứ nhất, cả gốc và lãi là $%s(1 + x)$ triệu đồng. Gửi thêm $%s$ triệu đồng nên tổng số tiền gốc bắt đầu tính lãi ở năm thứ hai là $%s(1 + x) + %s$ (triệu đồng).''' % (fmt_num(von_1), fmt_num(von_2), fmt_num(von_1), fmt_num(von_2)))

        th_da_1_d = '\\True Phương trình biểu thị số tiền nhận được sau hai năm là $[%s(1 + x) + %s](1 + x) = %s$' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan))
        th_da_1_s = 'Phương trình biểu thị số tiền nhận được sau hai năm là $%s(1 + x)^2 + %s = %s$' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Hết năm thứ hai, số tiền cả gốc lẫn lãi thu được là $[%s(1 + x) + %s](1 + x) = %s$.''' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan)))

        vd_da_1_d = '\\True Đặt $t = 1 + x$ ($t > 1$), ta thu được phương trình bậc hai $%st^2 + %st - %s = 0$' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan))
        vd_da_1_s = 'Đặt $t = 1 + x$ ($t > 1$), ta thu được phương trình bậc hai $%st^2 - %st - %s = 0$' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Thay $t = 1 + x$ vào phương trình $[%s(1 + x) + %s](1 + x) = %s$, ta được $(%st + %s)t = %s \\Leftrightarrow %st^2 + %st - %s = 0$.''' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan), fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan), fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan)))

        vdc_da_1_d = '\\True Lãi suất tiết kiệm của ngân hàng là $%s\\%%/\\text{năm}$' % (fmt_num(lai_pt))
        vdc_da_1_s = 'Lãi suất tiết kiệm của ngân hàng là $%s\\%%/\\text{năm}$' % (fmt_num(lai_pt + 1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Giải phương trình bậc hai $%st^2 + %st - %s = 0$ với điều kiện $t > 1$, ta tìm được nghiệm $t = %s$. \\\\ Suy ra $1 + x = %s \\Leftrightarrow x = %s = %s\\%%$. Vậy lãi suất tiết kiệm là $%s\\%%/\\text{năm}$.''' % (fmt_num(von_1), fmt_num(von_2), fmt_num(tong_nhan), fmt_num(t_val), fmt_num(t_val), fmt_num(x_val), fmt_num(lai_pt), fmt_num(lai_pt)))

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
