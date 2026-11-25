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


def bt_dang9_p2_b2_c5_ds8(self):
    # Dạng 9 (Vận dụng - Thuần túy toán học): Thiết kế biểu đồ cột kép từ bảng hai chiều theo hai mục đích đối lập
    k = random.choice([0, 10, 20])
    i1, i2, i3 = 40 + k, 55 + k, 65 + k
    j1, j2, j3 = 50 + k, 45 + k, 65 + k
    tong_i = i1 + i2 + i3
    
    noidungcauhoi = ("""Cho bảng số liệu hai chiều kích thước $2 \\times 3$ gồm hai đối tượng $I, II$ và ba tiêu chí $K_1, K_2, K_3$:\\\\
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|}
    \\hline
    \\textbf{Đối tượng / Tiêu chí} & $K_1$ & $K_2$ & $K_3$ \\\\
    \\hline
    \\textbf{Đối tượng $I$} & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\textbf{Đối tượng $II$} & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Xét tính đúng sai của các khẳng định sau:""" % (i1, i2, i3, j1, j2, j3))
    
    nb_da_1_d = '\\True Để so sánh trực tiếp đối tượng $I$ và đối tượng $II$ trong từng tiêu chí $K_1, K_2, K_3$, trục ngang của biểu đồ cột kép phải chia làm $3$ nhóm là $K_1, K_2, K_3$, mỗi nhóm gồm $2$ cột'
    nb_da_1_s = 'Để so sánh trực tiếp đối tượng $I$ và đối tượng $II$ trong từng tiêu chí, trục ngang phải chia làm $2$ nhóm là $I$ và $II$, mỗi nhóm gồm $2$ cột'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Muốn so sánh đối tượng $I$ và $II$ trong từng tiêu chí thì mỗi nhóm trên trục ngang ứng với một tiêu chí ($K_1, K_2, K_3$) và gồm $2$ cột đứng cạnh nhau của $I$ và $II$.""")
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Nếu trục ngang chia làm $2$ nhóm là $I$ và $II$, mỗi nhóm gồm $3$ cột thì ta đang so sánh nội bộ các tiêu chí $K_1, K_2, K_3$ trong từng đối tượng'
    th_da_1_s = 'Không thể chia trục ngang thành $2$ nhóm là $I$ và $II$ vì mỗi nhóm sẽ có $4$ cột'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Khi chia trục ngang thành $2$ nhóm là $I$ và $II$, mỗi nhóm gồm $3$ cột ứng với $K_1, K_2, K_3$, giúp so sánh trực tiếp độ lớn giữa các tiêu chí trong nội bộ từng đối tượng.""")
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Tại tiêu chí $K_3$, hai cột của đối tượng $I$ và đối tượng $II$ có chiều cao bằng nhau (cùng bằng $%s$)' % i3
    vd_da_1_s = 'Tại tiêu chí $K_3$, cột của đối tượng $I$ cao hơn cột của đối tượng $II$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tại tiêu chí $K_3$, giá trị của cả đối tượng $I$ và $II$ đều bằng $%s$ nên hai cột có chiều cao bằng nhau.""" % i3)
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Tổng giá trị ba tiêu chí của đối tượng $I$ lớn hơn tổng giá trị ba tiêu chí của đối tượng $II$'
    vdc_da_1_d = 'Tổng giá trị ba tiêu chí của đối tượng $I$ bằng tổng giá trị ba tiêu chí của đối tượng $II$ (cùng bằng $%s$)' % tong_i
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Tổng ba tiêu chí của $I$ là $%s + %s + %s = %s$; của $II$ là $%s + %s + %s = %s$. Hai tổng này bằng nhau."""
                     % (i1, i2, i3, tong_i, j1, j2, j3, tong_i))
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
