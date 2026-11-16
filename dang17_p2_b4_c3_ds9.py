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


def bt_dang17_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        base_edge = random.choice([7, 8, 9])
        base_vol = base_edge**3
        vol_target = base_vol + 1
        edge_exact = vol_target**(1/3)
        edge_r2 = round(edge_exact, 2)
        edge_r2_str = f"{edge_r2:.2f}".replace('.', ',')
        edge_r2_wrong_str = f"{edge_r2 + 0.01:.2f}".replace('.', ',')
        area_5_faces = 5 * (base_edge**2)
        area_6_faces = 6 * (base_edge**2)

        noidungcauhoi = ('Một người thợ cơ khí muốn gò một thùng tôn hình lập phương không có nắp để chứa được đúng $%s\\text{ lít}$ nước (biết $1\\text{ lít} = 1\\text{ dm}^3$). Xét tính đúng sai của các khẳng định sau:' % (vol_target))

        nb_da_1_d = '\\True Độ dài cạnh của thùng tôn hình lập phương tính theo decimét là $\\sqrt[3]{%s}\\text{ dm}$.' % (vol_target)
        nb_da_1_s = 'Độ dài cạnh của thùng tôn hình lập phương tính theo decimét là $\\sqrt{%s}\\text{ dm}$.' % (vol_target)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thể tích hình lập phương cạnh $x$ là $V = x^3 = %s\\text{ dm}^3$, suy ra $x = \\sqrt[3]{%s}\\text{ dm}$.' % (vol_target, vol_target))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Cạnh của thùng tôn dài hơn $%s\\text{ dm}$ một chút vì $%s^3 = %s < %s$.' % (base_edge, base_edge, base_vol, vol_target)
        th_da_1_s = 'Cạnh của thùng tôn ngắn hơn $%s\\text{ dm}$ một chút vì $%s^3 = %s < %s$.' % (base_edge, base_edge, base_vol, vol_target)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Vì $%s^3 = %s < %s$ nên $\\sqrt[3]{%s} > \\sqrt[3]{%s} = %s$, tức là cạnh thùng dài hơn $%s\\text{ dm}$ một chút.' % (base_edge, base_vol, vol_target, vol_target, base_vol, base_edge, base_edge))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Sử dụng máy tính cầm tay, độ dài cạnh thùng làm tròn đến chữ số thập phân thứ hai là $%s\\text{ dm}$.' % (edge_r2_str)
        vd_da_1_s = 'Sử dụng máy tính cầm tay, độ dài cạnh thùng làm tròn đến chữ số thập phân thứ hai là $%s\\text{ dm}$.' % (edge_r2_wrong_str)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Bấm máy tính cầm tay ta được $\\sqrt[3]{%s} \\approx %s$, làm tròn đến chữ số thập phân thứ hai được $%s\\text{ dm}$.' % (vol_target, f"{edge_exact:.6f}".replace('.', ','), edge_r2_str))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Diện tích tôn tối thiểu cần dùng để làm chiếc thùng không nắp này (lấy cạnh bằng $%s\\text{ dm}$) là $%s\\text{ dm}^2$.' % (base_edge, area_5_faces)
        vdc_da_1_s = 'Diện tích tôn tối thiểu cần dùng để làm chiếc thùng không nắp này (lấy cạnh bằng $%s\\text{ dm}$) là $%s\\text{ dm}^2$.' % (base_edge, area_6_faces)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Vì thùng hình lập phương không có nắp nên chỉ gồm $5$ mặt hình vuông. Diện tích tôn tối thiểu là $5 \\cdot %s^2 = %s\\text{ dm}^2$.' % (base_edge, area_5_faces))
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

        combined_nb = list(zip([nb_da_1], list_nb_2))
        combined_th = list(zip([th_da_1], list_th_2))
        combined_vd = list(zip([vd_da_1], list_vd_2))
        combined_vdc = list(zip([vdc_da_1], list_vdc_2))

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
