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

def bt_dang19_p4_b3_c7_ds8(self):
    # Dạng 19 (Thực tế): Phân tích dữ liệu khảo sát thời gian tự học và điểm số trên mặt phẳng tọa độ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # 5 học sinh: Minh(1,5; 7), Lan(2; 8,5), Hùng(2,5; 9), Mai(2; 7,5), Tuấn(3; 9,5)
        y_minh = random.choice([6, 7])
        y_mai = random.choice([7, 8])
        y_lan = y_mai + 1
        y_hung = 9
        y_tuan = 10

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (4.5,0) node[below] {$x$ (giờ)};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {$y$ (điểm)};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (M) at (1.5,1.8);\n'
            '\\coordinate (Ma) at (2.0,2.1);\n'
            '\\coordinate (L) at (2.0,2.5);\n'
            '\\coordinate (H) at (2.5,2.7);\n'
            '\\coordinate (T) at (3.0,3.0);\n'
            '\\draw[line width=1pt, dashed] (2.0,0) node[below] {$2,0$} -- (L);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (M) circle (1pt) node[left] {Minh $(1,5; %s)$};\n'
            '\\fill (Ma) circle (1pt) node[right] {Mai $(2,0; %s)$};\n'
            '\\fill (L) circle (1pt) node[left] {Lan $(2,0; %s)$};\n'
            '\\fill (H) circle (1pt) node[right] {Hùng $(2,5; %s)$};\n'
            '\\fill (T) circle (1pt) node[above] {Tuấn $(3,0; %s)$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (y_minh, y_mai, y_lan, y_hung, y_tuan)

        noidungcauhoi = (
            'Kết quả khảo sát số giờ tự học mỗi ngày $x$ (giờ) và điểm kiểm tra môn Toán $y$ (điểm) của $5$ học sinh tổ 1 được biểu diễn trên mặt phẳng tọa độ $Oxy$ như hình vẽ dưới đây:\\ %s'
        ) % (hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Trong nhóm khảo sát, bạn Tuấn có thời gian tự học nhiều nhất ($3,0$ giờ) và đạt điểm cao nhất ($%s$ điểm)' % (y_tuan)
        nb_da_1_s = 'Trong nhóm khảo sát, bạn Hùng có thời gian tự học nhiều nhất ($3,0$ giờ) và đạt điểm cao nhất ($%s$ điểm)' % (y_tuan)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Quan sát điểm biểu diễn cao nhất và xa trục tung nhất là điểm ứng với bạn Tuấn có tọa độ $(3,0; %s)$.' % (y_tuan)

        # Thông hiểu
        th_da_1_d = '\\True Hai bạn Lan và Mai có cùng số giờ tự học là $2,0$ giờ nhưng đạt hai mức điểm khác nhau là $%s$ điểm và $%s$ điểm' % (y_lan, y_mai)
        th_da_1_s = 'Hai bạn Lan và Mai có cùng số giờ tự học là $2,0$ giờ và đạt cùng một mức điểm bằng nhau'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Trên đồ thị, hai điểm biểu diễn của Lan $(2,0; %s)$ và Mai $(2,0; %s)$ có cùng hoành độ $x = 2,0$ nhưng tung độ khác nhau.' % (y_lan, y_mai)

        # Vận dụng
        vd_da_1_d = '\\True Theo dữ liệu khảo sát trên, điểm Toán $y$ không phải là một hàm số của số giờ tự học $x$'
        vd_da_1_s = 'Theo dữ liệu khảo sát trên, điểm Toán $y$ là một hàm số của số giờ tự học $x$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Vì ứng với giá trị $x = 2,0$ giờ có tới hai giá trị khác nhau của $y$ là $%s$ (Lan) và $%s$ (Mai) nên $y$ không phải là hàm số của $x$.' % (y_lan, y_mai)

        # Vận dụng cao
        vdc_da_1_d = '\\True Ngược lại, trong bảng số liệu của $5$ bạn này thì số giờ tự học $x$ lại là một hàm số của điểm Toán $y$'
        vdc_da_1_s = 'Trong bảng số liệu của $5$ bạn này, số giờ tự học $x$ cũng không phải là hàm số của điểm Toán $y$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Điểm số của $5$ bạn là $%s; %s; %s; %s; %s$ đôi một khác nhau, nên ứng với mỗi điểm số $y$ chỉ xác định duy nhất một số giờ tự học $x$. '
            'Do đó $x$ là hàm số của $y$.'
        ) % (y_minh, y_mai, y_lan, y_hung, y_tuan)

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
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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

        content = (
            '\\begin{minipage}{\\textwidth} \n'
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
            '\\end{ex}\n \\end{minipage}\n\n'
        )
        return content
