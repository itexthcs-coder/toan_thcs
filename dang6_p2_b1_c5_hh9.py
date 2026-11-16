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


def bt_dang6_p2_b1_c5_hh9(self):
    # Khai báo biến
    bo_so = [(5, 8, 4, 3), (10, 16, 8, 6), (13, 24, 12, 5), (15, 24, 12, 9)]
    R, ab, ah, oh = random.choice(bo_so)
    hm = oh + R

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.44,-1.08);
\\coordinate (B) at (1.44,-1.08);
\\coordinate (H) at (0,-1.08);
\\coordinate (M) at (0,1.8);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt] (0,-2.2)--(0,2.2) node[right] {$d$};
\\draw[line width=1pt] (O)--(A);
\\draw[line width=1pt] (0,-0.88)--(0.2,-0.88)--(0.2,-1.08);
\\fill (O) circle (1pt) node[above left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và hai điểm phân biệt $A, B$ cùng thuộc $(O)$ sao cho $AB = %s\\text{ cm}$. Gọi $d$ là đường trung trực của đoạn thẳng $AB$, $H$ là giao điểm của $d$ với $AB$ và $M$ là giao điểm (khác phía với $H$ qua $O$) của đường thẳng $d$ với đường tròn $(O)$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (R, ab, tikz_code))

    nb_da_1_d = '\\True Đường thẳng $d$ đi qua tâm $O$ của đường tròn $(O)$'
    nb_da_1_s = 'Đường thẳng $d$ không đi qua tâm $O$ của đường tròn $(O)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $A, B \\in (O)$ nên $OA = OB = R$, suy ra $O$ cách đều hai đầu mút của đoạn thẳng $AB$. Do đó tâm $O$ nằm trên đường trung trực $d$ của $AB$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đường thẳng $d$ là một trục đối xứng của đường tròn $(O)$'
    th_da_1_s = 'Đường thẳng $AB$ là một trục đối xứng của đường tròn $(O)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì đường thẳng $d$ đi qua tâm $O$ của đường tròn $(O)$ nên $d$ là một trục đối xứng của đường tròn $(O)$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $OH$ bằng $%s\\text{ cm}$' % oh
    vd_da_1_s = 'Độ dài đoạn thẳng $OH$ bằng $%s\\text{ cm}$' % ah
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $H$ là trung điểm của $AB$ nên $AH = \\dfrac{AB}{2} = %s\\text{ cm}$. Áp dụng định lí Pythagore cho tam giác $OHA$ vuông tại $H$, ta có $OH = \\sqrt{OA^2 - AH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$.''' % (ah, R, ah, oh))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khoảng cách từ điểm $M$ đến điểm $H$ bằng $%s\\text{ cm}$' % hm
    vdc_da_1_s = 'Khoảng cách từ điểm $M$ đến điểm $H$ bằng $%s\\text{ cm}$' % (R - oh)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì điểm $O$ nằm giữa $H$ và $M$ trên đường thẳng $d$ nên $HM = HO + OM = %s + %s = %s\\text{ cm}$.''' % (oh, R, hm))
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
