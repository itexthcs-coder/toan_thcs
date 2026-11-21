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


def bt_dang2_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('M', 'N', 'P', 'Q'),
        ('A', 'B', 'C', 'D'),
        ('E', 'F', 'G', 'H')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0.5,0);
    \\coordinate (B) at (3.5,0);
    \\coordinate (C) at (3,2.1);
    \\coordinate (D) at (0.2,1.9);
    \\coordinate (L) at (-0.5,0);
    \\coordinate (R) at (4.3,0);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\draw[line width=1pt, dashed] (L)--(A) (B)--(R);
    \\fill (A) circle (1pt) node[below] {$%s$};
    \\fill (B) circle (1pt) node[below] {$%s$};
    \\fill (C) circle (1pt) node[above right] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\node[below] at (R) {$d$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4)

    noidungcauhoi = ('''Cho tứ giác $%s$ và đường thẳng $d$ đi qua hai đỉnh $%s$ và $%s$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_tg, d1, d2, hinh_ve))

    nb_da_1_d = '\\True Nếu $%s$ là tứ giác lồi thì hai đỉnh $%s$ và $%s$ luôn nằm về một phía đối với đường thẳng $d$' % (ten_tg, d3, d4)
    nb_da_1_s = 'Nếu $%s$ là tứ giác lồi thì hai đỉnh $%s$ và $%s$ nằm về hai phía khác nhau đối với đường thẳng $d$' % (ten_tg, d3, d4)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo định nghĩa tứ giác lồi: Tứ giác lồi là tứ giác mà hai đỉnh thuộc một cạnh bất kì luôn nằm về một phía của đường thẳng đi qua hai đỉnh còn lại. Do đó hai đỉnh $%s$ và $%s$ nằm về một phía đối với đường thẳng $d$ đi qua $%s$ và $%s$.'''
                    % (d3, d4, d1, d2))

    th_da_1_d = '\\True Nếu đường thẳng $d$ cắt đoạn thẳng $%s$ tại một điểm nằm giữa $%s$ và $%s$ thì $%s$ không phải là tứ giác lồi' % (d3+d4, d3, d4, ten_tg)
    th_da_1_s = 'Nếu đường thẳng $d$ cắt đoạn thẳng $%s$ tại một điểm nằm giữa $%s$ và $%s$ thì $%s$ vẫn là tứ giác lồi' % (d3+d4, d3, d4, ten_tg)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Nếu đường thẳng $d$ cắt đoạn thẳng $%s$ tại một điểm nằm giữa $%s$ và $%s$ thì hai đỉnh $%s$ và $%s$ nằm về hai phía đối với đường thẳng $d$, vi phạm định nghĩa tứ giác lồi nên $%s$ không phải là tứ giác lồi.'''
                    % (d3+d4, d3, d4, d3, d4, ten_tg))

    vd_da_1_d = '\\True Nếu $%s$ là tứ giác lồi thì hai đỉnh $%s$ và $%s$ cũng nằm về một phía đối với đường thẳng đi qua hai đỉnh $%s$ và $%s$' % (ten_tg, d1, d4, d2, d3)
    vd_da_1_s = 'Nếu $%s$ là tứ giác lồi thì tính chất nằm về một phía chỉ đúng với đường thẳng đi qua $%s$ và $%s$' % (ten_tg, d1, d2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Tính chất của tứ giác lồi đúng với đường thẳng chứa bất kì cạnh nào của tứ giác, do đó hai đỉnh $%s$ và $%s$ cũng nằm về một phía đối với đường thẳng đi qua $%s$ và $%s$.'''
                    % (d1, d4, d2, d3))

    vdc_da_1_d = '\\True Không phải mọi hình gồm bốn đoạn thẳng khép kín không có hai cạnh nào cùng nằm trên một đường thẳng đều là tứ giác lồi'
    vdc_da_1_s = 'Mọi hình gồm bốn đoạn thẳng khép kín không có hai cạnh nào cùng nằm trên một đường thẳng đều là tứ giác lồi'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Một hình gồm bốn đoạn thẳng khép kín không có hai cạnh nào thẳng hàng là một tứ giác, nhưng tứ giác đó có thể là tứ giác lồi hoặc tứ giác lõm (chẳng hạn Hình 3.2b, 3.2c trong sách giáo khoa không phải tứ giác lồi).''')

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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
