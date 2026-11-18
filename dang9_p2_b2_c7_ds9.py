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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang9_p2_b2_c7_ds9(self):
    hieu_nguoi = random.choice([30, 45, 60])
    tong_n = int(hieu_nguoi * 100 / 30)
    m_lt = int(tong_n * 50 / 100)
    m_kt = int(tong_n * 30 / 100)
    m_tk = int(tong_n * 20 / 100)

    hinh_quat = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) circle (2);\n'
        '\\draw[line width=1pt] (0,0) -- (0:2);\n'
        '\\draw[line width=1pt] (0,0) -- (180:2);\n'
        '\\draw[line width=1pt] (0,0) -- (288:2);\n'
        '\\node at (90:1.1) {$50\%$};\n'
        '\\node at (234:1.1) {$30\%$};\n'
        '\\node at (324:1.1) {$20\%$};\n'
        '\\node[right] at (2.3, 0.7) {Lập trình viên: $50\%$};\n'
        '\\node[right] at (2.3, 0.0) {Kiểm thử phần mềm: $30\%$};\n'
        '\\node[right] at (2.3, -0.7) {Thiết kế đồ họa: $20\%$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây biểu diễn tỉ lệ ứng viên nộp hồ sơ vào 3 vị trí của một công ty công nghệ:%sBiết số ứng viên nộp vào vị trí Lập trình viên nhiều hơn vị trí Thiết kế đồ họa là $%s$ người. Xét tính đúng sai của các khẳng định sau:' % (hinh_quat, hieu_nguoi))

    nb_da_1_d = '\\True Tỉ lệ ứng viên vị trí Lập trình viên hơn vị trí Thiết kế đồ họa là $30\\%%$'
    nb_da_1_s = 'Tỉ lệ ứng viên vị trí Lập trình viên hơn vị trí Thiết kế đồ họa là $20\\%%$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Chênh lệch tỉ lệ phần trăm giữa vị trí Lập trình viên và Thiết kế đồ họa là $50\\%% - 20\\%% = 30\\%%$.')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tổng số ứng viên đã nộp hồ sơ vào công ty là $%s$ người' % (tong_n)
    th_da_1_s = 'Tổng số ứng viên đã nộp hồ sơ vào công ty là $%s$ người' % (tong_n + 30)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Vì $30\\%%$ tổng số ứng viên ứng với $%s$ người nên tổng số ứng viên là $n = %s : 30\\%% = %s$ (người).' % (hieu_nguoi, hieu_nguoi, tong_n))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Số ứng viên nộp vào vị trí Kiểm thử phần mềm là $%s$ người' % (m_kt)
    vd_da_1_s = 'Số ứng viên nộp vào vị trí Kiểm thử phần mềm là $%s$ người' % (m_tk)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Số ứng viên vị trí Kiểm thử phần mềm là $%s \\cdot 30\\%% = %s$ (người).' % (tong_n, m_kt))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tổng số ứng viên của hai vị trí Kiểm thử phần mềm và Thiết kế đồ họa bằng số ứng viên vị trí Lập trình viên'
    vdc_da_1_s = 'Tổng số ứng viên của hai vị trí Kiểm thử phần mềm và Thiết kế đồ họa nhiều hơn vị trí Lập trình viên'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng tỉ lệ của Kiểm thử phần mềm và Thiết kế đồ họa là $30\\%% + 20\\%% = 50\\%%$, bằng đúng tỉ lệ của Lập trình viên ($50\\%%$, tức cùng bằng $%s$ người).' % (m_lt))
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

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
