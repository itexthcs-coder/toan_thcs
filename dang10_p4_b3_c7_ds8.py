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

def bt_dang10_p4_b3_c7_ds8(self):
    # Dạng 10: Tính độ dài đoạn thẳng song song trục tọa độ và diện tích tam giác trên Oxy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xA = random.choice([-4, -3, -2])
        xB = random.choice([2, 3, 4, 5])
        y_base = random.choice([1, 2])
        xC = random.choice([-1, 0, 1, 2])
        h_tri = random.choice([4, 6])
        yC = y_base + h_tri

        len_AB = xB - xA
        area_ABC = (len_AB * h_tri) // 2

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-0.8) -- (0,3.2) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-1.8,0.8);\n'
            '\\coordinate (B) at (2.2,0.8);\n'
            '\\coordinate (C) at (0.5,2.6);\n'
            '\\coordinate (H) at (0.5,0.8);\n'
            '\\draw[line width=1pt] (A) -- (B) -- (C) -- cycle;\n'
            '\\draw[line width=1pt, dashed] (C) -- (H);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above] {$C$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Trên mặt phẳng tọa độ $Oxy$ (đơn vị trên hai trục tọa độ là $1\\text{ cm}$), xét ba điểm $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$ như hình vẽ minh họa:\\ %s'
        ) % (xA, y_base, xB, y_base, xC, yC, hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Hai điểm $A$ và $B$ có cùng tung độ bằng $%s$ nên đường thẳng $AB$ song song với trục hoành $Ox$' % (y_base)
        nb_da_1_s = 'Hai điểm $A$ và $B$ có cùng tung độ bằng $%s$ nên đường thẳng $AB$ song song với trục tung $Oy$' % (y_base)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Vì $y_A = y_B = %s \\neq 0$ nên đường thẳng $AB$ song song với trục hoành $Ox$.' % (y_base)

        # Thông hiểu
        th_da_1_d = '\\True Độ dài đoạn thẳng $AB$ bằng $%s\\text{ cm}$' % (len_AB)
        th_da_1_s = 'Độ dài đoạn thẳng $AB$ bằng $%s\\text{ cm}$' % (xB + xA)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Vì $AB // Ox$ nên độ dài đoạn $AB = |x_B - x_A| = |%s - (%s)| = %s\\text{ (cm)}$.' % (xB, xA, len_AB)

        # Vận dụng
        vd_da_1_d = '\\True Đường cao $CH$ hạ từ $C$ xuống đường thẳng $AB$ có độ dài bằng $%s\\text{ cm}$' % (h_tri)
        vd_da_1_s = 'Đường cao $CH$ hạ từ $C$ xuống đường thẳng $AB$ có độ dài bằng $%s\\text{ cm}$' % (yC)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Chân đường cao $H$ nằm trên đường thẳng $AB$ nên $y_H = %s$. Độ dài đường cao $CH = |y_C - y_H| = |%s - %s| = %s\\text{ (cm)}$.' % (y_base, yC, y_base, h_tri)

        # Vận dụng cao
        vdc_da_1_d = '\\True Diện tích của tam giác $ABC$ bằng $%s\\text{ cm}^2$' % (area_ABC)
        vdc_da_1_s = 'Diện tích của tam giác $ABC$ bằng $%s\\text{ cm}^2$' % (area_ABC * 2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Diện tích tam giác $ABC$ là $S_{ABC} = \\dfrac{1}{2} \\cdot AB \\cdot CH = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$. ' % (len_AB, h_tri, area_ABC)

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
