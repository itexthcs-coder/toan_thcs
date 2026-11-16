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


def bt_dang20_p2_b1_c5_hh9(self):
    # Khai báo biến
    bo_chinh_xac = [(5, 6, 8, 48, '9,6'), (10, 12, 16, 192, '19,2'), (15, 18, 24, 432, '28,8')]
    R, ma, mb, dien_tich, mp_str = random.choice(bo_chinh_xac)
    ab = 2 * R

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (M) at (106:1.8);
\\coordinate (N) at (-74:1.8);
\\coordinate (P) at (-106:1.8);
\\coordinate (H) at (-0.496,0);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt] (A)--(M)--(B)--(N)--cycle;
\\draw[line width=1pt] (M)--(P);
\\draw[line width=1pt, dashed] (M)--(N);
\\fill (O) circle (1pt) node[below right] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below right] {$N$};
\\fill (P) circle (1pt) node[below left] {$P$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$ và điểm $M \\in (O)$ sao cho $MA = %s\\text{ cm}$. Gọi $N$ là điểm đối xứng với $M$ qua tâm $O$, và $P$ là điểm đối xứng với $M$ qua đường thẳng $AB$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (R, ma, tikz_code))

    nb_da_1_d = '\\True Độ dài đoạn thẳng $MB$ bằng $%s\\text{ cm}$' % mb
    nb_da_1_s = 'Độ dài đoạn thẳng $MB$ bằng $%s\\text{ cm}$' % (ab - ma)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tam giác $AMB$ có đường trung tuyến $MO = R = \\dfrac{AB}{2}$ nên tam giác $AMB$ vuông tại $M$. Áp dụng định lí Pythagore, ta có $MB = \\sqrt{AB^2 - MA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$.''' % (ab, ma, mb))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tứ giác $AMBN$ là hình chữ nhật có diện tích bằng $%s\\text{ cm}^2$' % dien_tich
    th_da_1_s = 'Tứ giác $AMBN$ là hình thoi có diện tích bằng $%s\\text{ cm}^2$' % (dien_tich // 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $O$ là trung điểm của hai đường chéo $AB$ và $MN$ và $AB = MN = %s\\text{ cm}$ nên $AMBN$ là hình chữ nhật. Diện tích hình chữ nhật $AMBN$ là $S = MA \\cdot MB = %s \\cdot %s = %s\\text{ cm}^2$.''' % (ab, ma, mb, dien_tich))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $MP$ bằng $%s\\text{ cm}$' % mp_str
    vd_da_1_s = 'Độ dài đoạn thẳng $MP$ bằng $%s\\text{ cm}$' % ma
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Gọi $H$ là giao điểm của $MP$ và $AB$. Vì $P$ đối xứng với $M$ qua $AB$ nên $MH \\perp AB$ và $MP = 2MH$. Trong tam giác $AMB$ vuông tại $M$ có đường cao $MH$, ta có $MH \\cdot AB = MA \\cdot MB \\Rightarrow MH = \\dfrac{%s \\cdot %s}{%s}$. Vậy $MP = 2MH = %s\\text{ cm}$.''' % (ma, mb, ab, mp_str))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Ba điểm $N, O, P$ không thẳng hàng'
    vdc_da_1_s = 'Ba điểm $N, O, P$ thẳng hàng'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $N$ đối xứng với $M$ qua $O$ nên ba điểm $N, O, M$ thẳng hàng. Vì $M \\notin AB$ nên điểm $P$ đối xứng với $M$ qua $AB$ không trùng với $M$, do đó đường thẳng $OP$ không trùng với đường thẳng $OM$. Vậy ba điểm $N, O, P$ không thẳng hàng.''')
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
