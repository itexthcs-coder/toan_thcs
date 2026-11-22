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


def bt_dang1_p2_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = random.choice([('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q'), ('E', 'F', 'G', 'H')])
        dA, dB, dC, dD = bo_diem

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (0,2.2);
\\coordinate (%s) at (4,2.2);
\\coordinate (%s) at (4,0);
\\coordinate (%s) at (0,0);
\\draw[line width=1pt] (%s)--(%s)--(%s)--(%s)--cycle;
\\draw[line width=1pt] (0,1.98)--(0.22,1.98)--(0.22,2.2);
\\draw[line width=1pt] (3.78,2.2)--(3.78,1.98)--(4,1.98);
\\draw[line width=1pt] (3.78,0)--(3.78,0.22)--(4,0.22);
\\fill (%s) circle (1pt) node[above left] {$%s$};
\\fill (%s) circle (1pt) node[above right] {$%s$};
\\fill (%s) circle (1pt) node[below right] {$%s$};
\\fill (%s) circle (1pt) node[below left] {$%s$};
\\end{tikzpicture}
\\end{center}'''
        % (dA, dB, dC, dD, dA, dB, dC, dD, dA, dA, dB, dB, dC, dC, dD, dD))

        noidungcauhoi = ('''Cho tứ giác $%s%s%s%s$ có $\\widehat{%s} = 90^\\circ$, $\\widehat{%s} = 90^\\circ$ và $\\widehat{%s} = 90^\\circ$. Xét tính đúng – sai của các mệnh đề sau: %s'''
                         % (dA, dB, dC, dD, dA, dB, dC, hinh_ve))

        nb_da_1_d = '\\True Số đo của góc $\\widehat{%s}$ bằng $90^\\circ$' % (dD)
        nb_da_1_s = 'Số đo của góc $\\widehat{%s}$ bằng $60^\\circ$' % (dD)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Tổng bốn góc trong tứ giác $%s%s%s%s$ bằng $360^\\circ$ nên $\\widehat{%s} = 360^\\circ - (\\widehat{%s} + \\widehat{%s} + \\widehat{%s}) = 360^\\circ - 270^\\circ = 90^\\circ$.'''
                        % (dA, dB, dC, dD, dD, dA, dB, dC))

        th_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình chữ nhật' % (dA, dB, dC, dD)
        th_da_1_s = 'Tứ giác $%s%s%s%s$ chỉ là hình thang vuông nhưng không phải hình chữ nhật' % (dA, dB, dC, dD)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Tứ giác $%s%s%s%s$ có ba góc vuông (và góc còn lại cũng vuông) nên theo chú ý về định nghĩa hình chữ nhật, $%s%s%s%s$ là hình chữ nhật.'''
                        % (dA, dB, dC, dD, dA, dB, dC, dD))

        vd_da_1_d = '\\True Hai đường chéo $%s%s$ và $%s%s$ bằng nhau và cắt nhau tại trung điểm của mỗi đường' % (dA, dC, dB, dD)
        vd_da_1_s = 'Hai đường chéo $%s%s$ và $%s%s$ luôn vuông góc với nhau' % (dA, dC, dB, dD)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì $%s%s%s%s$ là hình chữ nhật nên hai đường chéo $%s%s$ và $%s%s$ bằng nhau và cắt nhau tại trung điểm của mỗi đường (không nhất thiết vuông góc).'''
                        % (dA, dB, dC, dD, dA, dC, dB, dD))

        vdc_da_1_d = '\\True Tứ giác $%s%s%s%s$ có hai cặp cạnh đối song song và bằng nhau' % (dA, dB, dC, dD)
        vdc_da_1_s = 'Tứ giác $%s%s%s%s$ không phải là hình bình hành' % (dA, dB, dC, dD)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Hình chữ nhật $%s%s%s%s$ cũng là một hình bình hành nên có tất cả các tính chất của hình bình hành, suy ra hai cặp cạnh đối song song và bằng nhau.'''
                         % (dA, dB, dC, dD))
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

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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
