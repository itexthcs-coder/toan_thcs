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

def bt_dang20_p2_b2_c5_hh9(self):
    so_mieng = random.choice([8, 10, 12])
    so_dk = so_mieng // 2
    goc_1_mieng = 360 // so_mieng
    mieng_an = so_dk - 1
    cung_an = mieng_an * goc_1_mieng
    cung_con = 360 - cung_an
    mieng_an_nhieu = so_dk + 1
    cung_an_nhieu = mieng_an_nhieu * goc_1_mieng

    noidungcauhoi = ('''Một chiếc bánh pizza hình tròn tâm $O$ được cắt từ tâm ra mép bánh thành $%s$ miếng hình quạt bằng nhau bởi $%s$ đường kính (như hình vẽ minh họa).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.8);
    \\foreach \\k in {0,45,90,135} {
        \\draw[line width=1pt] (\\k:1.8)--(\\k+180:1.8);
    }
    \\fill (O) circle (1.2pt) node[below right] {$O$};
    \\end{tikzpicture}
    \\end{center}''' % (so_mieng, so_dk))

    nb_da_1_d = '\\True Mỗi đường cắt xuyên qua tâm bánh là một đường kính và là dây cung lớn nhất của chiếc bánh'
    nb_da_1_s = 'Mỗi đường cắt xuyên qua tâm bánh là một bán kính của chiếc bánh'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Mỗi đường cắt thẳng đi qua hai điểm trên mép bánh và đi qua tâm $O$ là một đường kính, đồng thời là dây cung lớn nhất của đường tròn mặt bánh.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Phần viền bánh cong của mỗi miếng pizza là một cung nhỏ có số đo bằng $%s^\\circ$' % (goc_1_mieng)
    th_da_1_s = 'Phần viền bánh cong của mỗi miếng pizza là một cung nhỏ có số đo bằng $%s^\\circ$' % (goc_1_mieng * 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Chiếc bánh hình tròn $360^\\circ$ chia làm $%s$ phần bằng nhau nên phần viền cong của mỗi miếng có số đo bằng $\\dfrac{360^\\circ}{%s} = %s^\\circ$.''' % (so_mieng, so_mieng, goc_1_mieng))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu một người ăn hết $%s$ miếng pizza liền kề nhau thì phần viền bánh cong còn lại của chiếc bánh là một cung lớn có số đo bằng $%s^\\circ$' % (mieng_an, cung_con)
    vd_da_1_s = 'Nếu một người ăn hết $%s$ miếng pizza liền kề nhau thì phần viền bánh cong còn lại của chiếc bánh có số đo bằng $%s^\\circ$' % (mieng_an, cung_an)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Phần viền bánh của $%s$ miếng đã ăn có số đo là $%s \\cdot %s^\\circ = %s^\\circ$. \\\\ Phần viền bánh cong còn lại có số đo là $360^\\circ - %s^\\circ = %s^\\circ > 180^\\circ$ nên là một cung lớn.''' % (mieng_an, mieng_an, goc_1_mieng, cung_an, cung_an, cung_con))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu một người ăn hết $%s$ miếng pizza liền kề nhau thì phần viền bánh cong của $%s$ miếng đã ăn là một cung lớn có số đo bằng $%s^\\circ$' % (mieng_an_nhieu, mieng_an_nhieu, cung_an_nhieu)
    vdc_da_1_s = 'Nếu một người ăn hết $%s$ miếng pizza liền kề nhau thì phần viền bánh cong của $%s$ miếng đã ăn là một cung nhỏ có số đo bằng $%s^\\circ$' % (mieng_an_nhieu, mieng_an_nhieu, cung_an_nhieu)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tổng số đo phần viền bánh cong của $%s$ miếng đã ăn là $%s \\cdot %s^\\circ = %s^\\circ$. \\\\ Vì $%s^\\circ > 180^\\circ$ nên đây là một cung lớn chứ không phải cung nhỏ.''' % (mieng_an_nhieu, mieng_an_nhieu, goc_1_mieng, cung_an_nhieu, cung_an_nhieu))
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
