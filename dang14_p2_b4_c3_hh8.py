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


def bt_dang14_p2_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc_len = random.choice([6, 8, 10, 12, 14, 16])
        min_np = bc_len // 2

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,3);
\\coordinate (A) at (0,0);
\\coordinate (C) at (3,0);
\\coordinate (M) at (1.2,1.8);
\\coordinate (N) at (0,1.8);
\\coordinate (P) at (1.2,0);
\\draw[line width=1pt] (B)--(A)--(C)--cycle (M)--(N) (M)--(P) (A)--(M) (N)--(P);
\\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
\\draw[line width=1pt] (0,1.58)--(0.22,1.58)--(0.22,1.8);
\\draw[line width=1pt] (0.98,0)--(0.98,0.22)--(1.2,0.22);
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (N) circle (1pt) node[left] {$N$};
\\fill (P) circle (1pt) node[below] {$P$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho $\\triangle ABC$ vuông cân tại $A$ có cạnh huyền $BC = %s\\text{ cm}$. Lấy điểm $M$ bất kì trên cạnh huyền $BC$ ($M$ khác $B$ và $C$). Gọi $N$ và $P$ lần lượt là hình chiếu vuông góc của $M$ trên các cạnh $AB$ và $AC$. Xét tính đúng – sai của các mệnh đề sau: %s'''
                         % (bc_len, hinh_ve))

        nb_da_1_d = '\\True Tứ giác $MPAN$ là hình chữ nhật với mọi vị trí của điểm $M$ trên cạnh $BC$'
        nb_da_1_s = 'Tứ giác $MPAN$ chỉ là hình chữ nhật khi $M$ là trung điểm của $BC$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Xét tứ giác $MPAN$ có $\\widehat{NAP} = \\widehat{ANM} = \\widehat{APM} = 90^\\circ$ nên $MPAN$ luôn là hình chữ nhật với mọi vị trí của $M$ trên $BC$.''')

        th_da_1_d = '\\True Độ dài đoạn thẳng $NP$ luôn bằng độ dài đoạn thẳng $AM$'
        th_da_1_s = 'Độ dài đoạn thẳng $NP$ luôn bằng một nửa độ dài đoạn thẳng $AM$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Trong hình chữ nhật $MPAN$, hai đường chéo $NP$ và $AM$ bằng nhau nên $NP = AM$.''')

        vd_da_1_d = '\\True Đoạn thẳng $NP$ đạt độ dài nhỏ nhất khi và chỉ khi $M$ là trung điểm của cạnh huyền $BC$'
        vd_da_1_s = 'Đoạn thẳng $NP$ đạt độ dài nhỏ nhất khi $M$ tiến sát về đỉnh $B$ hoặc đỉnh $C$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì $NP = AM$ nên $NP$ nhỏ nhất khi $AM$ nhỏ nhất. Trong $\\triangle ABC$, $AM$ nhỏ nhất khi $AM \\perp BC$. Do $\\triangle ABC$ vuông cân tại $A$ nên đường cao ứng với cạnh huyền đồng thời là đường trung tuyến, tức $M$ là trung điểm của $BC$.''')

        vdc_da_1_d = '\\True Giá trị nhỏ nhất của độ dài đoạn thẳng $NP$ là $%s\\text{ cm}$' % (min_np)
        vdc_da_1_s = 'Giá trị nhỏ nhất của độ dài đoạn thẳng $NP$ là $%s\\text{ cm}$' % (bc_len)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $M$ là trung điểm của $BC$, đường trung tuyến $AM$ ứng với cạnh huyền $BC$ của $\\triangle ABC$ vuông tại $A$ có độ dài $AM = \\dfrac{1}{2}BC = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$. Vậy $NP$ nhỏ nhất bằng $%s\\text{ cm}$.'''
                         % (bc_len, min_np, min_np))
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

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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
