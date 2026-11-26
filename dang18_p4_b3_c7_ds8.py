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

def bt_dang18_p4_b3_c7_ds8(self):
    # Dạng 18 (Thực tế): Hàm số chuyển đổi thang đo nhiệt độ giữa độ C và độ F
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c_patient = random.choice([38, 39, 40])
        f_patient = round(1.8 * c_patient + 32, 1)
        f_patient_str = str(f_patient).replace('.', ',')
        if f_patient_str.endswith(',0'):
            f_patient_str = f_patient_str[:-2]

        c_norm = 37
        f_norm_str = '98,6'

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (8.5,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (8.5,0.8);\n'
            '\\draw[line width=1pt] (2.5,0) -- (2.5,1.6) (4.5,0) -- (4.5,1.6) (6.5,0) -- (6.5,1.6);\n'
            '\\node at (1.25,1.2) {Nhiệt độ $C$ ($^\\circ\\text{C}$)};\n'
            '\\node at (1.25,0.4) {Nhiệt độ $F$ ($^\\circ\\text{F}$)};\n'
            '\\node at (3.5,1.2) {$0$};\n'
            '\\node at (3.5,0.4) {$32$};\n'
            '\\node at (5.5,1.2) {$37$};\n'
            '\\node at (5.5,0.4) {$?$};\n'
            '\\node at (7.5,1.2) {$100$};\n'
            '\\node at (7.5,0.4) {$212$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Trong y tế và đời sống quốc tế, công thức hàm số chuyển đổi từ nhiệt độ $C$ ($^\\circ\\text{C}$) sang nhiệt độ $F$ ($^\\circ\\text{F}$) là $F = 1,8C + 32$ (kèm bảng giá trị tham khảo):\\ %s'
        ) % (bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Nhiệt độ đóng băng của nước tinh khiết là $0^\\circ\\text{C}$, tương ứng với $32^\\circ\\text{F}$'
        nb_da_1_s = 'Nhiệt độ đóng băng của nước tinh khiết là $0^\\circ\\text{C}$, tương ứng với $0^\\circ\\text{F}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Thay $C = 0$ vào công thức ta có $F = 1,8 \\cdot 0 + 32 = 32^\\circ\\text{F}$.'

        # Thông hiểu
        th_da_1_d = '\\True Thân nhiệt bình thường của người là $37^\\circ\\text{C}$ tương ứng với $%s^\\circ\\text{F}$' % (f_norm_str)
        th_da_1_s = 'Thân nhiệt bình thường của người là $37^\\circ\\text{C}$ tương ứng với $96,8^\\circ\\text{F}$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Với $C = 37$, ta tính được $F = 1,8 \\cdot 37 + 32 = 66,6 + 32 = 98,6^\\circ\\text{F}$.'

        # Vận dụng
        vd_da_1_d = '\\True Một bệnh nhân đo nhiệt kế báo $%s^\\circ\\text{F}$ thì nhiệt độ cơ thể người đó là $%s^\\circ\\text{C}$ (đang bị sốt)' % (f_patient_str, c_patient)
        vd_da_1_s = 'Một bệnh nhân đo nhiệt kế báo $%s^\\circ\\text{F}$ thì nhiệt độ cơ thể người đó là $%s^\\circ\\text{C}$ (bình thường)' % (f_patient_str, c_patient - 2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Thay $F = %s$ vào công thức: $1,8C + 32 = %s \\Leftrightarrow 1,8C = %s \\Leftrightarrow C = %s^\\circ\\text{C}$ (cao hơn $37,5^\\circ\\text{C}$ nên bệnh nhân đang bị sốt).'
        ) % (f_patient_str, f_patient_str, str(round(f_patient - 32, 1)).replace('.', ','), c_patient)

        # Vận dụng cao
        vdc_da_1_d = '\\True Tại nhiệt độ $-40^\\circ\\text{C}$, số đo trên thang độ C và thang độ F có giá trị bằng nhau'
        vdc_da_1_s = 'Không tồn tại nhiệt độ nào mà số đo trên thang độ C và thang độ F bằng nhau'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Đặt $F = C$, ta có phương trình $C = 1,8C + 32 \\Leftrightarrow -0,8C = 32 \\Leftrightarrow C = -40$. Vậy $-40^\\circ\\text{C} = -40^\\circ\\text{F}$.'

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
