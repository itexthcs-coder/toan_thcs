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

def bt_dang11_p2_b2_c5_hh9(self):
    phut = random.choice([12, 18, 24, 36, 42, 48])
    cung_phut = phut * 6
    cung_gio = phut // 2
    gio_dung = random.choice([2, 4, 5])
    cung_gio_dung = gio_dung * 30

    noidungcauhoi = ('''Trên mặt một chiếc đồng hồ treo tường có $12$ vạch số chia đường tròn mặt đồng hồ thành $12$ cung bằng nhau và $60$ vạch chia phút (như hình vẽ). Xét chuyển động của kim giờ và kim phút sau khoảng thời gian $%s$ phút:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.8);
    \\foreach \\x in {1,...,12} {
        \\draw[line width=1pt] (90-30*\\x:1.65)--(90-30*\\x:1.8);
        \\node at (90-30*\\x:1.4) {\\x};
    }
    \\draw[line width=1pt] (O)--(150:1.05);
    \\draw[line width=1pt] (O)--(30:1.5);
    \\fill (O) circle (1.2pt);
    \\end{tikzpicture}
    \\end{center}''' % (phut))

    nb_da_1_d = '\\True Sau mỗi phút, đầu kim phút vạch nên một cung có số đo bằng $6^\\circ$'
    nb_da_1_s = 'Sau mỗi phút, đầu kim phút vạch nên một cung có số đo bằng $30^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong $60$ phút, đầu kim phút quay đúng một vòng tròn $360^\\circ$, do đó sau mỗi phút đầu kim phút vạch nên một cung có số đo bằng $\\dfrac{360^\\circ}{60} = 6^\\circ$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Sau $%s$ phút, đầu kim phút vạch nên một cung có số đo bằng $%s^\\circ$' % (phut, cung_phut)
    th_da_1_s = 'Sau $%s$ phút, đầu kim phút vạch nên một cung có số đo bằng $%s^\\circ$' % (phut, cung_gio)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Sau $%s$ phút, đầu kim phút vạch nên một cung có số đo bằng $%s \\cdot 6^\\circ = %s^\\circ$.''' % (phut, phut, cung_phut))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Sau $%s$ phút, đầu kim giờ vạch nên một cung có số đo bằng $%s^\\circ$' % (phut, cung_gio)
    vd_da_1_s = 'Sau $%s$ phút, đầu kim giờ vạch nên một cung có số đo bằng $%s^\\circ$' % (phut, phut)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong $60$ phút, đầu kim giờ quay được $\\dfrac{360^\\circ}{12} = 30^\\circ$. \\\\ Vậy sau $%s$ phút, đầu kim giờ vạch nên một cung có số đo bằng $\\dfrac{%s}{60} \\cdot 30^\\circ = %s^\\circ$.''' % (phut, phut, cung_gio))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tại thời điểm đúng $%s$ giờ $00$ phút, góc ở tâm tạo bởi kim giờ và kim phút chắn cung nhỏ có số đo bằng $%s^\\circ$' % (gio_dung, cung_gio_dung)
    vdc_da_1_s = 'Tại thời điểm đúng $%s$ giờ $00$ phút, góc ở tâm tạo bởi kim giờ và kim phút chắn cung nhỏ có số đo bằng $%s^\\circ$' % (gio_dung, 360 - cung_gio_dung)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Lúc $%s$ giờ đúng, kim giờ chỉ đúng số $%s$ và kim phút chỉ đúng số $12$, cách nhau $%s$ khoảng giờ nên cung nhỏ bị chắn có số đo bằng $%s \\cdot 30^\\circ = %s^\\circ$.''' % (gio_dung, gio_dung, gio_dung, gio_dung, cung_gio_dung))
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
