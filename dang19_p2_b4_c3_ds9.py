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


def bt_dang19_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        edge_dm = random.choice([3, 4, 5])
        vol_max = edge_dm**3
        vol_half = Rational(vol_max, 2)
        vol_half_str = str(float(vol_half)).replace('.0', '').replace('.', ',')
        h_cm = int(edge_dm * 10 / 2)
        stone_vol = int(vol_half) + 1
        vol_empty = vol_max - vol_half
        vol_empty_str = str(float(vol_empty)).replace('.0', '').replace('.', ',')

        noidungcauhoi = ('Một bể cá cảnh mini bằng kính dạng hình lập phương hiện đang chứa nước với mực nước cao bằng một nửa chiều cao của bể. Biết thể tích nước hiện có trong bể là $%s\\text{ lít}$ ($1\\text{ lít} = 1\\text{ dm}^3$). Xét tính đúng sai của các khẳng định sau:' % (vol_half_str))

        nb_da_1_d = '\\True Thể tích tối đa mà bể cá có thể chứa được khi đổ đầy nước là $%s\\text{ dm}^3$.' % (vol_max)
        nb_da_1_s = 'Thể tích tối đa mà bể cá có thể chứa được khi đổ đầy nước là $%s\\text{ dm}^3$.' % (vol_max * 2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Vì mực nước cao bằng một nửa chiều cao bể nên thể tích tối đa của bể gấp đôi thể tích nước hiện có: $V = 2 \\cdot %s = %s\\text{ dm}^3$.' % (vol_half_str, vol_max))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Độ dài cạnh của bể cá hình lập phương là $\\sqrt[3]{%s} = %s\\text{ dm}$.' % (vol_max, edge_dm)
        th_da_1_s = 'Độ dài cạnh của bể cá hình lập phương là $%s\\text{ dm}$.' % (edge_dm + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Độ dài cạnh của bể cá hình lập phương là $a = \\sqrt[3]{%s} = %s\\text{ dm}$.' % (vol_max, edge_dm))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Chiều cao của mực nước hiện tại trong bể là $%s\\text{ cm}$.' % (h_cm)
        vd_da_1_s = 'Chiều cao của mực nước hiện tại trong bể là $%s\\text{ cm}$.' % (edge_dm * 10)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Đổi $%s\\text{ dm} = %s\\text{ cm}$. Chiều cao mực nước hiện tại bằng một nửa chiều cao bể nên bằng $\\dfrac{%s}{2} = %s\\text{ cm}$.' % (edge_dm, edge_dm * 10, edge_dm * 10, h_cm))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Nếu thả chìm hoàn toàn vào bể một hòn đá non bộ có thể tích $%s\\text{ dm}^3$ thì nước trong bể sẽ bị tràn ra ngoài.' % (stone_vol)
        vdc_da_1_s = 'Nếu thả chìm hoàn toàn vào bể một hòn đá non bộ có thể tích $%s\\text{ dm}^3$ thì nước trong bể sẽ không bị tràn ra ngoài.' % (stone_vol)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Phần thể tích trống còn lại của bể là $%s - %s = %s\\text{ dm}^3$. Vì thể tích hòn đá là $%s\\text{ dm}^3 > %s\\text{ dm}^3$ nên nước sẽ bị tràn ra ngoài.' % (vol_max, vol_half_str, vol_empty_str, stone_vol, vol_empty_str))
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
