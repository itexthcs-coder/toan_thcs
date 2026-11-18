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


def bt_dang18_p2_b3_c7_ds9(self):
    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Thời gian (phút)};
\\draw[->, line width=1pt] (0,0) -- (0,4.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {1/10, 2/20, 3/30, 4/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1,0) rectangle (2,1.5);
\\node[above] at (1.5,1.5) {$15\\%%$};
\\draw[line width=1pt] (2,0) rectangle (3,3.5);
\\node[above] at (2.5,3.5) {$35\\%%$};
\\draw[line width=1pt] (3,0) rectangle (4,3.0);
\\node[above] at (3.5,3.0) {$30\\%%$};
\\draw[line width=1pt] (4,0) rectangle (5,2.0);
\\node[above] at (4.5,2.0) {$20\\%%$};
\\node[below] at (1,0) {$0$};
\\node[below] at (2,0) {$5$};
\\node[below] at (3,0) {$10$};
\\node[below] at (4,0) {$15$};
\\node[below] at (5,0) {$20$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Trên một hệ trục tọa độ của biểu đồ tần số tương đối ghép nhóm dạng cột như hình vẽ dưới đây, bề rộng mỗi cột trên trục ngang là $1\\text{ cm}$ (ứng với độ dài nhóm $5$ phút) và trên trục đứng $1\\text{ cm}$ ứng với $10\\%%$ tần số tương đối:
%s''' % (tikz_code))

    list_nb_da_1 = [
        '\\True Chiều cao của cột cao nhất trên hình vẽ là $3,5\\text{ cm}$',
        'Chiều cao của cột cao nhất trên hình vẽ là $3,0\\text{ cm}$'
    ]
    loigiai_nb_1 = ('''Cột cao nhất ứng với $35\\%%$ nên có chiều cao trên hình vẽ là $\\dfrac{35}{10} = 3,5\\text{ (cm)}$.''')

    list_th_da_1 = [
        '\\True Diện tích của hình chữ nhật biểu diễn nhóm $[10; 15)$ trên hình vẽ là $3\\text{ cm}^2$',
        'Diện tích của hình chữ nhật biểu diễn nhóm $[10; 15)$ trên hình vẽ là $15\\text{ cm}^2$'
    ]
    loigiai_th_1 = ('''Cột nhóm $[10; 15)$ có đáy $1\\text{ cm}$, chiều cao $\\dfrac{30}{10} = 3\\text{ cm}$ nên có diện tích là $1 \\cdot 3 = 3\\text{ (cm}^2\\text{)}$.''')

    list_vd_da_1 = [
        '\\True Tổng diện tích của cả $4$ cột hình chữ nhật trên biểu đồ bằng $10\\text{ cm}^2$',
        'Tổng diện tích của cả $4$ cột hình chữ nhật trên biểu đồ bằng $100\\text{ cm}^2$'
    ]
    loigiai_vd_1 = ('''Tổng diện tích cả $4$ cột là $1 \\cdot (1,5 + 3,5 + 3,0 + 2,0) = 10\\text{ (cm}^2\\text{)}$.''')

    list_vdc_da_1 = [
        '\\True Diện tích cột biểu diễn nhóm $[5; 10)$ lớn hơn diện tích cột biểu diễn nhóm $[0; 5)$ là $2\\text{ cm}^2$',
        'Diện tích cột biểu diễn nhóm $[5; 10)$ gấp đôi diện tích cột biểu diễn nhóm $[0; 5)$'
    ]
    loigiai_vdc_1 = ('''Diện tích cột nhóm $[5; 10)$ là $3,5\\text{ cm}^2$, cột nhóm $[0; 5)$ là $1,5\\text{ cm}^2$, hiệu diện tích là $3,5 - 1,5 = 2\\text{ (cm}^2\\text{)}$.''')

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
