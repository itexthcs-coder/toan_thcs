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


def bt_dang19_p2_b2_c6_ds8(self):
    # Dạng 19: Thực tế năng suất & sản xuất - Bài toán thời gian hoàn thành đơn hàng
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        tong_ao = 1200
        ngay_dau = 5
        tang_them = 20

        noidungcauhoi = ('Một phân xưởng may nhận đơn hàng sản xuất $%s$ chiếc áo. Trong $%s$ ngày đầu, mỗi ngày phân xưởng may được $x$ chiếc áo ($x \\in \\mathbb{N}^*, x < 240$). Những ngày sau đó, nhờ cải tiến kỹ thuật nên mỗi ngày phân xưởng may tăng thêm $%s$ chiếc áo so với ban đầu. Xét tính đúng sai của các khẳng định sau:' % (tong_ao, ngay_dau, tang_them))

        # Ý a
        nb_da_1_d = '\\True Số áo phân xưởng còn phải may sau $%s$ ngày đầu là $%s - %sx$ (chiếc)' % (ngay_dau, tong_ao, ngay_dau)
        nb_da_1_s = 'Số áo phân xưởng còn phải may sau $%s$ ngày đầu là $%s + %sx$ (chiếc)' % (ngay_dau, tong_ao, ngay_dau)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Trong $%s$ ngày đầu phân xưởng may được $%sx$ chiếc áo nên số áo còn lại là $%s - %sx$ (chiếc).' % (ngay_dau, ngay_dau, tong_ao, ngay_dau))
        list_nb_2 = [loigiai_nb_1]

        # Ý b
        th_da_1_d = '\\True Phân thức biểu thị số ngày phân xưởng hoàn thành số áo còn lại là $\\dfrac{%s - %sx}{x + %s}$ (ngày)' % (tong_ao, ngay_dau, tang_them)
        th_da_1_s = 'Phân thức biểu thị số ngày phân xưởng hoàn thành số áo còn lại là $\\dfrac{%s}{x + %s}$ (ngày)' % (tong_ao, tang_them)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Năng suất những ngày sau là $(x + %s)$ chiếc/ngày nên số ngày hoàn thành số áo còn lại là $\\dfrac{%s - %sx}{x + %s}$ (ngày).' % (tang_them, tong_ao, ngay_dau, tang_them))
        list_th_2 = [loigiai_th_1]

        # Ý c
        vd_da_1_d = '\\True Với $x = 100$, phân thức ở ý b) có giá trị bằng $\\dfrac{35}{6}$ ngày'
        vd_da_1_s = 'Với $x = 100$, phân thức ở ý b) có giá trị bằng $5$ ngày'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Thay $x = 100$ vào phân thức $\\dfrac{%s - %sx}{x + %s}$, ta được: $\\dfrac{1200 - 500}{100 + 20} = \\dfrac{700}{120} = \\dfrac{35}{6}$ (ngày).' % (tong_ao, ngay_dau, tang_them))
        list_vd_2 = [loigiai_vd_1]

        # Ý d
        vdc_da_1_d = '\\True Nếu mỗi ngày ban đầu phân xưởng may được $100$ chiếc áo thì tổng thời gian hoàn thành toàn bộ đơn hàng là $\\dfrac{65}{6}$ ngày'
        vdc_da_1_s = 'Nếu mỗi ngày ban đầu phân xưởng may được $100$ chiếc áo thì tổng thời gian hoàn thành toàn bộ đơn hàng là $10$ ngày'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Tổng thời gian hoàn thành đơn hàng là $5 + \\dfrac{35}{6} = \\dfrac{65}{6}$ (ngày).')
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

    # Xuất câu hỏi trắc nghiệm đúng sai
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
