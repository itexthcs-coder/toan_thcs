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


def bt_dang18_p2_b1_c3_hh8(self):
    g1 = random.randint(105, 125)
    g2 = random.randint(80, 95)
    g3 = random.randint(85, 100)
    g4 = 360 - (g1 + g2 + g3)

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (P1) at (1.8,0.2);
    \\coordinate (P2) at (1.5,1.5);
    \\coordinate (P3) at (0.2,1.6);
    \\coordinate (P4) at (-1.5,1.4);
    \\coordinate (P5) at (-1.7,-0.2);
    \\coordinate (P6) at (-1.4,-1.5);
    \\coordinate (P7) at (-0.2,-1.6);
    \\coordinate (P8) at (1.6,-1.3);
    \\draw[line width=1pt] (O)--(P1)--(P2)--(P3)--(O) (O)--(P3)--(P4)--(P5)--(O) (O)--(P5)--(P6)--(P7)--(O) (O)--(P7)--(P8)--(P1)--(O);
    \\fill (O) circle (1pt);
    \\node at (0.35,0.25) {$1$};
    \\node at (-0.25,0.35) {$2$};
    \\node at (-0.35,-0.25) {$3$};
    \\node at (0.25,-0.35) {$4$};
    \\end{tikzpicture}
    \\end{center}'''

    noidungcauhoi = ('''Một người thợ sử dụng các viên gạch lát nền hình tứ giác $ABCD$ giống hệt nhau có $\\widehat{A} = %s^\\circ$, $\\widehat{B} = %s^\\circ$, $\\widehat{C} = %s^\\circ$ để lát kín một khoảng sân phẳng sao cho tại mỗi điểm chung luôn ghép vừa khít bốn đỉnh khác nhau của bốn viên gạch (minh họa hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (g1, g2, g3, hinh_ve))

    nb_da_1_d = '\\True Số đo góc còn lại $\\widehat{D}$ của mỗi viên gạch bằng $%s^\\circ$' % (g4)
    nb_da_1_s = 'Số đo góc còn lại $\\widehat{D}$ của mỗi viên gạch bằng $%s^\\circ$' % (g4 + 10)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong tứ giác $ABCD$, ta có $\\widehat{D} = 360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = 360^\\circ - %s^\\circ = %s^\\circ$.'''
                    % (g1, g2, g3, g1+g2+g3, g4))

    th_da_1_d = '\\True Tại mỗi điểm chung của bốn viên gạch, tổng số đo bốn góc ghép lại bằng $360^\\circ$ nên mặt phẳng được lát kín mà không có khe hở'
    th_da_1_s = 'Tại mỗi điểm chung của bốn viên gạch, tổng số đo bốn góc ghép lại bằng $180^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Bốn góc tại điểm chung chính là bốn góc $A, B, C, D$ của tứ giác nên tổng số đo bằng $\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = 360^\\circ$, tạo thành một góc đầy vừa khít.''')

    vd_da_1_d = '\\True Nếu người thợ ghép bốn góc $A$ của bốn viên gạch đó quanh một điểm chung thì không thể vừa khít vì $4 \\cdot %s^\\circ > 360^\\circ$' % (g1)
    vd_da_1_s = 'Nếu người thợ ghép bốn góc $A$ của bốn viên gạch đó quanh một điểm chung thì cũng tạo thành một góc đầy $360^\\circ$ vừa khít'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Nếu ghép bốn góc $A$ lại thì tổng số đo bằng $4 \\cdot %s^\\circ = %s^\\circ > 360^\\circ$ nên các viên gạch sẽ chồng lấn lên nhau, không thể ghép vừa khít.'''
                    % (g1, 4*g1))

    vdc_da_1_d = '\\True Mọi viên gạch hình tứ giác lồi bất kì đều có thể dùng để lát kín mặt phẳng theo quy luật ghép bốn đỉnh khác nhau tại một điểm'
    vdc_da_1_s = 'Chỉ những viên gạch hình vuông hoặc hình chữ nhật mới có thể lát kín mặt phẳng'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì tổng bốn góc trong của mọi tứ giác luôn bằng $360^\\circ$ nên khi ghép bốn đỉnh khác nhau của bốn viên gạch tứ giác bất kì quanh một điểm chung, tổng số đo luôn bằng $360^\\circ$ và lát kín được mặt phẳng.''')

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
