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


def bt_dang14_p2_b2_c5_ds8(self):
    # Dạng 14 (Vận dụng - Thuần túy toán học): Phân tích sự thay đổi cơ cấu phần trăm qua hai thời điểm bằng hai biểu đồ quạt tròn
    k = random.choice([1, 2, 3])
    s1 = 200 * k
    s2 = 300 * k
    a1 = s1 * 40 // 100
    a2 = s2 * 30 // 100
    b1 = s1 * 60 // 100
    b2 = s2 * 70 // 100
    diff_a = a2 - a1
    
    noidungcauhoi = ("""Hai biểu đồ hình quạt tròn biểu diễn cơ cấu hai thành phần $A$ và $B$ của một đại lượng $S$ tại hai thời điểm $T_1$ và $T_2$:
    \\begin{itemize}
    \\item Tại $T_1$ (tổng $S_1 = %s$): thành phần $A$ chiếm $40\\%%$, thành phần $B$ chiếm $60\\%%$.
    \\item Tại $T_2$ (tổng $S_2 = %s$): thành phần $A$ chiếm $30\\%%$, thành phần $B$ chiếm $70\\%%$.
    \\end{itemize}
    Xét tính đúng sai của các khẳng định sau:""" % (s1, s2))
    
    nb_da_1_d = '\\True Tại thời điểm $T_1$, giá trị tuyệt đối của thành phần $A$ là $%s$' % a1
    nb_da_1_s = 'Tại thời điểm $T_1$, giá trị tuyệt đối của thành phần $A$ là $%s$' % (a1 + 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tại $T_1$, giá trị của thành phần $A$ là: $%s \\cdot 40\\%% = %s$.""" % (s1, a1))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Tại thời điểm $T_2$, giá trị tuyệt đối của thành phần $A$ là $%s$' % a2
    th_da_1_s = 'Tại thời điểm $T_2$, giá trị tuyệt đối của thành phần $A$ là $%s$' % (s2 * 40 // 100)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tại $T_2$, giá trị của thành phần $A$ là: $%s \\cdot 30\\%% = %s$.""" % (s2, a2))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Mặc dù tỉ trọng của $A$ giảm từ $40\\%%$ xuống $30\\%%$, nhưng giá trị tuyệt đối của $A$ tại $T_2$ vẫn tăng thêm $%s$ đơn vị so với $T_1$' % diff_a
    vd_da_1_s = 'Vì tỉ trọng của $A$ giảm từ $40\\%%$ xuống $30\\%%$ nên giá trị tuyệt đối của $A$ tại $T_2$ giảm đi $%s$ đơn vị so với $T_1$' % diff_a
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Giá trị tuyệt đối của $A$ tăng từ $%s$ lên $%s$, tức là tăng thêm $%s - %s = %s$ đơn vị (do tổng thể $S$ tăng mạnh từ $%s$ lên $%s$).""" % (a1, a2, a2, a1, diff_a, s1, s2))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Nếu dùng biểu đồ cột kép để so sánh giá trị tuyệt đối của $A$ và $B$ tại hai thời điểm $T_1, T_2$ thì cột của $B$ tại $T_2$ thấp hơn cột của $B$ tại $T_1$'
    vdc_da_1_d = 'Nếu dùng biểu đồ cột kép để so sánh giá trị tuyệt đối của $A$ và $B$ tại hai thời điểm $T_1, T_2$ thì cột của $B$ tại $T_2$ cao hơn cột của $B$ tại $T_1$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Giá trị của $B$ tại $T_1$ là $%s \\cdot 60\\%% = %s$; tại $T_2$ là $%s \\cdot 70\\%% = %s > %s$ nên cột của $B$ tại $T_2$ cao hơn tại $T_1$.""" % (s1, b1, s2, b2, b1))
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
