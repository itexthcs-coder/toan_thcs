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


def bt_dang1_p2_b1_c3_hh8(self):
    # Random bộ đỉnh
    bo_dinh = [
        ('A', 'B', 'C', 'D'),
        ('M', 'N', 'P', 'Q'),
        ('E', 'F', 'G', 'H'),
        ('P', 'Q', 'R', 'S')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4
    c1, c2, c3, c4 = d1+d2, d2+d3, d3+d4, d4+d1

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.2,0);
    \\coordinate (C) at (2.7,2.1);
    \\coordinate (D) at (0.4,1.9);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\fill (A) circle (1pt) node[below left] {$%s$};
    \\fill (B) circle (1pt) node[below right] {$%s$};
    \\fill (C) circle (1pt) node[above right] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4)

    noidungcauhoi = ('''Cho bốn đoạn thẳng $%s$, $%s$, $%s$, $%s$ khép kín tạo thành một hình phẳng (minh họa hình vẽ tứ giác $%s$). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (c1, c2, c3, c4, ten_tg, hinh_ve))

    # Mệnh đề a
    nb_da_1_d = '\\True Nếu ba điểm $%s$, $%s$, $%s$ thẳng hàng thì hình gồm bốn đoạn thẳng $%s$, $%s$, $%s$, $%s$ không phải là một tứ giác' % (d1, d2, d3, c1, c2, c3, c4)
    nb_da_1_s = 'Nếu ba điểm $%s$, $%s$, $%s$ thẳng hàng thì hình gồm bốn đoạn thẳng $%s$, $%s$, $%s$, $%s$ vẫn là một tứ giác' % (d1, d2, d3, c1, c2, c3, c4)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo định nghĩa, tứ giác $%s$ là hình gồm bốn đoạn thẳng $%s$, $%s$, $%s$, $%s$ trong đó không có hai đoạn thẳng nào nằm trên cùng một đường thẳng. Nếu $%s$, $%s$, $%s$ thẳng hàng thì $%s$ và $%s$ cùng nằm trên một đường thẳng nên hình đó không phải là tứ giác.'''
                    % (ten_tg, c1, c2, c3, c4, d1, d2, d3, c1, c2))

    # Mệnh đề b
    th_da_1_d = '\\True Trong tứ giác $%s$, hai cạnh $%s$ và $%s$ được gọi là hai cạnh kề nhau' % (ten_tg, c1, c2)
    th_da_1_s = 'Trong tứ giác $%s$, hai cạnh $%s$ và $%s$ được gọi là hai cạnh đối nhau' % (ten_tg, c1, c2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Trong tứ giác $%s$, hai cạnh $%s$ và $%s$ có chung đỉnh $%s$ nên là hai cạnh kề nhau (hai cạnh đối nhau là hai cạnh không kề nhau, chẳng hạn $%s$ và $%s$).'''
                    % (ten_tg, c1, c2, d2, c1, c3))

    # Mệnh đề c
    vd_da_1_d = '\\True Nếu không có hai đoạn thẳng nào trong bốn đoạn thẳng trên nằm trên cùng một đường thẳng thì hình đó là một tứ giác'
    vd_da_1_s = 'Chỉ khi bốn đoạn thẳng có độ dài bằng nhau và không có hai đoạn thẳng nào thẳng hàng thì hình đó mới là một tứ giác'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Theo định nghĩa tứ giác, hình gồm bốn đoạn thẳng $%s$, $%s$, $%s$, $%s$ khép kín trong đó không có hai đoạn thẳng nào nằm trên cùng một đường thẳng chính là tứ giác $%s$.'''
                    % (c1, c2, c3, c4, ten_tg))

    # Mệnh đề d
    vdc_da_1_d = '\\True Một tứ giác luôn có bốn đỉnh, bốn cạnh và hai đường chéo'
    vdc_da_1_s = 'Một tứ giác luôn có bốn đỉnh, bốn cạnh và bốn đường chéo'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tứ giác $%s$ có bốn đỉnh là $%s, %s, %s, %s$; bốn cạnh là $%s, %s, %s, %s$ và chỉ có hai đường chéo là $%s$ và $%s$.'''
                     % (ten_tg, d1, d2, d3, d4, c1, c2, c3, c4, d1+d3, d2+d4))

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
