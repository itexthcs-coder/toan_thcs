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


def bt_dang14_p2_b2_c7_ds9(self):
    hinh_hai_quat = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) circle (1.5);\n'
        '\\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (216:1.5);\n'
        '\\node at (108:0.85) {$60\\%$};\n'
        '\\node at (288:0.85) {$40\\%$};\n'
        '\\node[below] at (0,-1.7) {Chi nhánh A ($400$ triệu)};\n'
        '\\draw[line width=1pt] (4.5,0) circle (1.5);\n'
        '\\draw[line width=1pt] (4.5,0) -- ++(0:1.5) (4.5,0) -- ++(162:1.5);\n'
        '\\node at (4.5,0) [shift={(81:0.85)}] {$45\\%$};\n'
        '\\node at (4.5,0) [shift={(261:0.85)}] {$55\\%$};\n'
        '\\node[below] at (4.5,-1.7) {Chi nhánh B ($600$ triệu)};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = ('Hai biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu doanh thu (gồm Bán lẻ và Bán sỉ) của Chi nhánh A (tổng doanh thu $400$ triệu đồng) và Chi nhánh B (tổng doanh thu $600$ triệu đồng) trong tháng 10 (phần cung lớn hơn ở Chi nhánh A là Bán lẻ, ở Chi nhánh B là Bán sỉ):%sXét tính đúng sai của các khẳng định sau:' % (hinh_hai_quat))

    nb_da_1_d = '\\True Tỉ trọng doanh thu Bán lẻ của Chi nhánh A cao hơn của Chi nhánh B'
    nb_da_1_s = 'Tỉ trọng doanh thu Bán sỉ của Chi nhánh A cao hơn của Chi nhánh B'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tỉ trọng doanh thu Bán lẻ của Chi nhánh A là $60\\%$, cao hơn Chi nhánh B ($45\\%$).')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Doanh thu Bán lẻ thực tế của Chi nhánh A nhỏ hơn doanh thu Bán lẻ thực tế của Chi nhánh B'
    th_da_1_s = 'Doanh thu Bán lẻ thực tế của Chi nhánh A lớn hơn doanh thu Bán lẻ thực tế của Chi nhánh B'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Doanh thu Bán lẻ của Chi nhánh A là $400 \\cdot 60\\% = 240$ triệu đồng; của Chi nhánh B là $600 \\cdot 45\\% = 270$ triệu đồng. Vì $240 < 270$ nên Chi nhánh A nhỏ hơn Chi nhánh B.')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Doanh thu Bán sỉ của Chi nhánh B nhiều hơn doanh thu Bán sỉ của Chi nhánh A là $170$ triệu đồng'
    vd_da_1_s = 'Doanh thu Bán sỉ của Chi nhánh B nhiều hơn doanh thu Bán sỉ của Chi nhánh A là $150$ triệu đồng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Doanh thu Bán sỉ của Chi nhánh B là $600 \\cdot 55\\% = 330$ triệu đồng; của Chi nhánh A là $400 \\cdot 40\\% = 160$ triệu đồng. Chênh lệch là $330 - 160 = 170$ triệu đồng.')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tính chung cả hai chi nhánh, tần số tương đối của doanh thu Bán lẻ là $51\\%$'
    vdc_da_1_s = 'Tính chung cả hai chi nhánh, tần số tương đối của doanh thu Bán lẻ là $52,5\\%$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng doanh thu Bán lẻ cả hai chi nhánh là $240 + 270 = 510$ triệu đồng trên tổng doanh thu $400 + 600 = 1000$ triệu đồng, chiếm tỉ lệ $\\frac{510}{1000} \\cdot 100\\% = 51\\%$.')
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

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
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
