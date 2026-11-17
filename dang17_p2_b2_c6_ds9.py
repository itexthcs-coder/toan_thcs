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


def bt_dang17_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        k_half = random.choice([10, 12, 15])
        L_wire = 4 * k_half
        max_x = 2 * k_half
        diff_x = random.choice([2, 3])
        x1_val = k_half - diff_x
        x2_val = k_half + diff_x
        area_target = 2 * x1_val * x2_val
        area_over = 2 * (k_half**2) + 10

        tikz_fig = ('\\begin{center}\n' +
                    '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
                    '\\draw[line width=2pt] (-0.5,2.5) -- (5.5,2.5) node[above, midway] {Bức tường gạch có sẵn};\n' +
                    '\\draw[line width=1pt] (0.5,2.5) -- (0.5,0) node[left, midway] {$x$} -- (4.5,0) -- (4.5,2.5) node[right, midway] {$x$};\n' +
                    '\\end{tikzpicture}\n' +
                    '\\end{center}')

        noidungcauhoi = ('Bác An có một lưới thép dài $%s \\text{ m}$ và dự định dùng toàn bộ lưới thép này để rào ba mặt của một mảnh vườn hình chữ nhật giáp với một bức tường gạch có sẵn (bức tường đóng vai trò là một cạnh chiều dài của mảnh vườn nên không cần rào, như hình vẽ). Gọi chiều rộng của mảnh vườn là $x \\text{ (m)}$ ($0 < x < %s$).\n%s\nXét tính đúng sai của các khẳng định sau:' % (L_wire, max_x, tikz_fig))

        nb_da_1_d = '\\True Chiều dài của mảnh vườn được biểu diễn theo $x$ là $%s - 2x \\text{ (m)}$' % (L_wire)
        nb_da_1_s = 'Chiều dài của mảnh vườn được biểu diễn theo $x$ là $%s - x \\text{ (m)}$' % (L_wire)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Vì lưới thép dùng để rào $2$ cạnh chiều rộng và $1$ cạnh chiều dài nên chiều dài của mảnh vườn là $%s - 2x \\text{ (m)}$.' % (L_wire))

        th_da_1_d = '\\True Diện tích $S$ của mảnh vườn được tính theo công thức $S = -2x^2 + %sx \\text{ (m}^2\\text{)}$' % (L_wire)
        th_da_1_s = 'Diện tích $S$ của mảnh vườn được tính theo công thức $S = -x^2 + %sx \\text{ (m}^2\\text{)}$' % (L_wire)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Diện tích mảnh vườn hình chữ nhật là $S = x(%s - 2x) = -2x^2 + %sx \\text{ (m}^2\\text{)}$.' % (L_wire, L_wire))

        vd_da_1_d = '\\True Để diện tích mảnh vườn bằng $%s \\text{ m}^2$ thì chiều rộng $x$ có thể nhận hai giá trị là $%s \\text{ m}$ hoặc $%s \\text{ m}$' % (area_target, x1_val, x2_val)
        vd_da_1_s = 'Để diện tích mảnh vườn bằng $%s \\text{ m}^2$ thì chiều rộng $x$ chỉ nhận một giá trị duy nhất là $%s \\text{ m}$' % (area_target, x1_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Giải phương trình $-2x^2 + %sx = %s \\Leftrightarrow x^2 - %sx + %s = 0$. \\\\ Có $\\Delta\\prime = (-%s)^2 - %s = %s \\Rightarrow x_1 = %s$ và $x_2 = %s$ (cả hai đều thỏa mãn $0 < x < %s$).' % (L_wire, area_target, 2*k_half, area_target // 2, k_half, area_target // 2, diff_x**2, x1_val, x2_val, max_x))

        vdc_da_1_d = '\\True Với $%s \\text{ m}$ lưới thép đó, bác An không thể rào được mảnh vườn có diện tích đạt $%s \\text{ m}^2$' % (L_wire, area_over)
        vdc_da_1_s = 'Với $%s \\text{ m}$ lưới thép đó, bác An có thể rào được mảnh vườn có diện tích đạt $%s \\text{ m}^2$' % (L_wire, area_over)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Xét phương trình $-2x^2 + %sx = %s \\Leftrightarrow x^2 - %sx + %s = 0$. \\\\ Có $\\Delta\\prime = (-%s)^2 - %s = -5 < 0$ (phương trình vô nghiệm). Vậy không thể rào được mảnh vườn có diện tích đạt $%s \\text{ m}^2$.' % (L_wire, area_over, 2*k_half, area_over // 2, k_half, area_over // 2, area_over))

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
