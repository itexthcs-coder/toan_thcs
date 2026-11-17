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

def bt_dang17_p2_b2_c5_hh9(self):
    p_bo = 25
    p_dap = 40
    p_buyt = 20
    p_khac = 15

    g_bo = 90
    g_dap = 144
    g_buyt = 72
    g_khac = 54
    tong_bo_buyt = g_bo + g_buyt

    noidungcauhoi = ('''Một biểu đồ hình quạt tròn tâm $O$ biểu diễn tỉ lệ các loại phương tiện đến trường của học sinh một trường THCS như sau: Đi bộ chiếm $%s\\%%$, Xe đạp chiếm $%s\\%%$, Xe buýt chiếm $%s\\%%$, Phương tiện khác chiếm $%s\\%%$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.8);
    \\draw[line width=1pt] (O)--(0:1.8) (O)--(90:1.8) (O)--(234:1.8) (O)--(306:1.8);
    \\fill (O) circle (1.2pt);
    \\node at (45:1.1) {$25\\%%$};
    \\node at (162:1.1) {$40\\%%$};
    \\node at (270:1.1) {$20\\%%$};
    \\node at (333:1.1) {$15\\%%$};
    \\end{tikzpicture}
    \\end{center}''' % (p_bo, p_dap, p_buyt, p_khac))

    nb_da_1_d = '\\True Hình quạt tròn biểu diễn nhóm học sinh đi bộ có góc ở tâm bằng $%s^\\circ$' % (g_bo)
    nb_da_1_s = 'Hình quạt tròn biểu diễn nhóm học sinh đi bộ có góc ở tâm bằng $%s^\\circ$' % (p_bo)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Cả đường tròn ứng với $360^\\circ$, do đó nhóm đi bộ chiếm $%s\\%%$ có góc ở tâm bằng $%s\\%% \\cdot 360^\\circ = %s^\\circ$.''' % (p_bo, p_bo, g_bo))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Cung tròn ứng với nhóm học sinh đi xe đạp có số đo bằng $%s^\\circ$' % (g_dap)
    th_da_1_s = 'Cung tròn ứng với nhóm học sinh đi xe đạp có số đo bằng $%s^\\circ$' % (g_buyt)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Nhóm học sinh đi xe đạp chiếm $%s\\%%$ nên cung tròn tương ứng có số đo bằng $%s\\%% \\cdot 360^\\circ = %s^\\circ$.''' % (p_dap, p_dap, g_dap))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tổng số đo hai cung tròn ứng với nhóm đi bộ và đi xe buýt bằng $%s^\\circ$' % (tong_bo_buyt)
    vd_da_1_s = 'Tổng số đo hai cung tròn ứng với nhóm đi bộ và đi xe buýt bằng $%s^\\circ$' % (180)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Nhóm đi xe buýt có số đo cung là $%s\\%% \\cdot 360^\\circ = %s^\\circ$. \\\\ Tổng số đo hai cung tròn ứng với nhóm đi bộ và đi xe buýt là $%s^\\circ + %s^\\circ = %s^\\circ$.''' % (p_buyt, g_buyt, g_bo, g_buyt, tong_bo_buyt))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Cung tròn ứng với nhóm học sinh đi bằng phương tiện khác là một cung nhỏ có số đo bằng $%s^\\circ$' % (g_khac)
    vdc_da_1_s = 'Cung tròn ứng với nhóm học sinh đi bằng phương tiện khác là một cung lớn có số đo bằng $%s^\\circ$' % (360 - g_khac)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Nhóm phương tiện khác chiếm $%s\\%%$ nên cung tròn tương ứng có số đo bằng $%s\\%% \\cdot 360^\\circ = %s^\\circ < 180^\\circ$, đây là một cung nhỏ.''' % (p_khac, p_khac, g_khac))
    list_vdc_2 = [loigiai_vdc_1]

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
