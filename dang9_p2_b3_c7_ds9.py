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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang9_p2_b3_c7_ds9(self):
    k = random.choice([1, 2])
    m1, m2, m3, m4 = 8 * k, 22 * k, 15 * k, 5 * k
    n = 50 * k

    noidungcauhoi = ('''Cho bảng thống kê khối lượng (đơn vị: $\\text{g}$) của $%s$ quả trứng gà tại một trang trại chăn nuôi:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Khối lượng ($\\text{g}$) & $[45; 50)$ & $[50; 55)$ & $[55; 60)$ & $[60; 65)$ \\\\
\\hline
Số quả trứng & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Người ta muốn vẽ biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng cho bảng số liệu trên.''' % (n, m1, m2, m3, m4))

    list_nb_da_1 = [
        '\\True Các giá trị đại diện lần lượt của $4$ nhóm là $47,5$; $52,5$; $57,5$; $62,5$',
        'Các giá trị đại diện lần lượt của $4$ nhóm là $45$; $50$; $55$; $60$'
    ]
    loigiai_nb_1 = ('''Giá trị đại diện là trung bình cộng hai đầu mút của mỗi nhóm, lần lượt là $47,5$; $52,5$; $57,5$; $62,5$.''')

    list_th_da_1 = [
        '\\True Điểm biểu diễn nhóm $[50; 55)$ trên mặt phẳng tọa độ có tọa độ là $(52,5; 44)$',
        'Điểm biểu diễn nhóm $[50; 55)$ trên mặt phẳng tọa độ có tọa độ là $(52,5; %s)$' % m2
    ]
    loigiai_th_1 = ('''Tần số tương đối của nhóm $[50; 55)$ là $\\dfrac{%s}{%s} \\cdot 100\\%% = 44\\%%$ nên tọa độ điểm biểu diễn là $(52,5; 44)$.''' % (m2, n))

    list_vd_da_1 = [
        '\\True Đường gấp khúc nối các điểm trên biểu đồ đạt đỉnh cao nhất tại hoành độ $52,5$',
        'Đường gấp khúc nối các điểm trên biểu đồ đạt đỉnh cao nhất tại hoành độ $57,5$'
    ]
    loigiai_vd_1 = ('''Nhóm $[50; 55)$ có tần số tương đối cao nhất ($44\\%%$) nên đường gấp khúc đạt đỉnh tại hoành độ $52,5$.''')

    list_vdc_da_1 = [
        '\\True Tổng tung độ của điểm đầu tiên và điểm cuối cùng trên biểu đồ bằng $26\\%%$',
        'Tổng tung độ của điểm đầu tiên và điểm cuối cùng trên biểu đồ bằng $13\\%%$'
    ]
    loigiai_vdc_1 = ('''Tần số tương đối nhóm đầu là $\\dfrac{%s}{%s} \\cdot 100\\%% = 16\\%%$, nhóm cuối là $\\dfrac{%s}{%s} \\cdot 100\\%% = 10\\%%$. Tổng bằng $16\\%% + 10\\%% = 26\\%%$.''' % (m1, n, m4, n))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

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
