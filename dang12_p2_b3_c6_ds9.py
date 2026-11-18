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

def bt_dang12_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a, b, hyp = random.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13)])
        k = random.choice([1, 2])
        c = hyp * k
        xA = Rational(c, a)
        yB = Rational(c, b)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-0.8,0) -- (3.8,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,3) node[left] {$y$};
\\coordinate (O) at (0,0);
\\coordinate (A) at (3,0);
\\coordinate (B) at (0,2.25);
\\coordinate (H) at (1.08,1.44);
\\draw[line width=1pt] (-0.4,2.55) -- (3.5,-0.375) node[above right] {$(d)$};
\\draw[line width=1pt, dashed] (O) -- (H);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, xét đường thẳng $(d)$ là tập nghiệm của phương trình $%sx + %sy = %s$. Gọi $H$ là hình chiếu vuông góc của gốc tọa độ $O(0; 0)$ lên đường thẳng $(d)$ (như hình vẽ minh họa). %s'''
                         % (a, b, c, hinh_ve))

        # Nhận biết
        nb_da_1_d = '\\True Đường thẳng $(d)$ cắt trục $Ox$ tại $A\\left(%s; 0\\right)$ và cắt trục $Oy$ tại $B\\left(0; %s\\right)$' % (latex(xA), latex(yB))
        nb_da_1_s = 'Đường thẳng $(d)$ đi qua gốc tọa độ $O(0; 0)$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Cho $y = 0 \\Rightarrow %sx = %s \\Leftrightarrow x = %s$, nên $A\\left(%s; 0\\right)$. Cho $x = 0 \\Rightarrow %sy = %s \\Leftrightarrow y = %s$, nên $B\\left(0; %s\\right)$.'''
                        % (a, c, latex(xA), latex(xA), b, c, latex(yB), latex(yB)))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Đường thẳng $(d)$ đi qua góc phần tư thứ nhất, thứ hai và thứ tư của mặt phẳng tọa độ'
        th_da_1_s = 'Đường thẳng $(d)$ đi qua góc phần tư thứ ba của mặt phẳng tọa độ'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Vì $OA = %s > 0$ và $OB = %s > 0$ nên đường thẳng $(d)$ nằm ở phía trên bên phải gốc tọa độ, đi qua các góc phần tư thứ nhất, thứ hai và thứ tư (không đi qua góc phần tư thứ ba).'''
                        % (latex(xA), latex(yB)))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Khoảng cách từ gốc tọa độ $O(0; 0)$ đến đường thẳng $(d)$ bằng $%s$' % (k)
        vd_da_1_s = 'Khoảng cách từ gốc tọa độ $O(0; 0)$ đến đường thẳng $(d)$ bằng $%s$' % (c)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Trong tam giác vuông $OAB$ có đường cao $OH$, áp dụng hệ thức lượng trong tam giác vuông ta có $\\dfrac{1}{OH^2} = \\dfrac{1}{OA^2} + \\dfrac{1}{OB^2} = \\dfrac{%s^2}{%s^2} + \\dfrac{%s^2}{%s^2} = \\dfrac{%s^2}{%s^2} = \\dfrac{1}{%s^2}$. Suy ra $OH = %s$.'''
                        % (a, c, b, c, hyp, c, k, k))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Cặp số $(0; 0)$ không phải là nghiệm của phương trình đã cho'
        vdc_da_1_s = 'Độ dài đoạn thẳng $AB$ nối hai giao điểm với các trục tọa độ bằng $%s$' % (c)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Thay $x = 0$ và $y = 0$ vào vế trái phương trình ta được $%s \\cdot 0 + %s \\cdot 0 = 0 \\neq %s$, nên $(0; 0)$ không phải là nghiệm của phương trình.'''
                         % (a, b, c))
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
