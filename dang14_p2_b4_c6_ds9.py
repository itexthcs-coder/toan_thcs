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


def bt_dang14_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x_kh = random.choice([80, 100, 120, 150])
        ngay_kh = random.choice([15, 20, 25])
        tong_sp_kh = x_kh * ngay_kh
        vuot_ngay = random.choice([20, 25, 30])
        som_ngay = random.choice([2, 3, 4])
        ngay_tt = ngay_kh - som_ngay
        tong_sp_tt = (x_kh + vuot_ngay) * ngay_tt
        sp_du = tong_sp_tt - tong_sp_kh

        noidungcauhoi = ('''Một xí nghiệp may nhận đơn hàng sản xuất $%s\\text{ bộ đồng phục}$ trong một thời gian quy định. Nhờ cải tiến dây chuyền, mỗi ngày xí nghiệp may vượt mức $%s\\text{ bộ}$ so với kế hoạch. Do đó, trước thời hạn quy định $%s\\text{ ngày}$, xí nghiệp không những hoàn thành đơn hàng mà còn may dư thêm được $%s\\text{ bộ}$. Gọi $x$ là số bộ đồng phục mỗi ngày xí nghiệp phải may theo kế hoạch ($x \\in \\mathbb{N}^*$).''' % (fmt_num(tong_sp_kh), fmt_num(vuot_ngay), fmt_num(som_ngay), fmt_num(sp_du)))

        nb_da_1_d = '\\True Thời gian hoàn thành đơn hàng theo kế hoạch là $\\frac{%s}{x}$ (ngày)' % (fmt_num(tong_sp_kh))
        nb_da_1_s = 'Thời gian hoàn thành đơn hàng theo kế hoạch là $\\frac{x}{%s}$ (ngày)' % (fmt_num(tong_sp_kh))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Theo kế hoạch, xí nghiệp sản xuất $%s$ bộ với năng suất $x$ bộ/ngày nên thời gian hoàn thành là $\\frac{%s}{x}$ (ngày).''' % (fmt_num(tong_sp_kh), fmt_num(tong_sp_kh)))

        th_da_1_d = '\\True Thời gian thực tế xí nghiệp đã làm việc là $\\frac{%s}{x + %s}$ (ngày)' % (fmt_num(tong_sp_tt), fmt_num(vuot_ngay))
        th_da_1_s = 'Thời gian thực tế xí nghiệp đã làm việc là $\\frac{%s}{x + %s}$ (ngày)' % (fmt_num(tong_sp_kh), fmt_num(vuot_ngay))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thực tế xí nghiệp may được $%s + %s = %s$ bộ với năng suất $x + %s$ bộ/ngày nên thời gian thực tế làm việc là $\\frac{%s}{x + %s}$ (ngày).''' % (fmt_num(tong_sp_kh), fmt_num(sp_du), fmt_num(tong_sp_tt), fmt_num(vuot_ngay), fmt_num(tong_sp_tt), fmt_num(vuot_ngay)))

        vd_da_1_d = '\\True Phương trình lập được từ bài toán là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(tong_sp_kh), fmt_num(tong_sp_tt), fmt_num(vuot_ngay), fmt_num(som_ngay))
        vd_da_1_s = 'Phương trình lập được từ bài toán là $\\frac{%s}{x + %s} - \\frac{%s}{x} = %s$' % (fmt_num(tong_sp_tt), fmt_num(vuot_ngay), fmt_num(tong_sp_kh), fmt_num(som_ngay))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì hoàn thành trước thời hạn $%s\\text{ ngày}$ nên thời gian kế hoạch nhiều hơn thời gian thực tế là $%s\\text{ ngày}$. Ta có phương trình: $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$.''' % (fmt_num(som_ngay), fmt_num(som_ngay), fmt_num(tong_sp_kh), fmt_num(tong_sp_tt), fmt_num(vuot_ngay), fmt_num(som_ngay)))

        vdc_da_1_d = '\\True Theo kế hoạch, mỗi ngày xí nghiệp phải may $%s\\text{ bộ đồng phục}$' % (fmt_num(x_kh))
        vdc_da_1_s = 'Theo kế hoạch, mỗi ngày xí nghiệp phải may $%s\\text{ bộ đồng phục}$' % (fmt_num(x_kh + vuot_ngay))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Quy đồng khử mẫu phương trình $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$, ta được: \\\\ $%s(x + %s) - %sx = %sx(x + %s) \\Leftrightarrow %sx^2 + %sx - %s = 0$. \\\\ Giải phương trình bậc hai này ta tìm được nghiệm nguyên dương duy nhất là $x = %s$. \\\\ Vậy theo kế hoạch, mỗi ngày xí nghiệp phải may $%s\\text{ bộ đồng phục}$.''' % (fmt_num(tong_sp_kh), fmt_num(tong_sp_tt), fmt_num(vuot_ngay), fmt_num(som_ngay), fmt_num(tong_sp_kh), fmt_num(vuot_ngay), fmt_num(tong_sp_tt), fmt_num(som_ngay), fmt_num(vuot_ngay), fmt_num(som_ngay), fmt_num(som_ngay * vuot_ngay + sp_du), fmt_num(tong_sp_kh * vuot_ngay), fmt_num(x_kh), fmt_num(x_kh)))

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
