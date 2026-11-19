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


def bt_dang10_p2_b3_c9_hh9(self):
    bc = random.choice([8, 10, 12, 14, 16])
    r_val = bc // 2
    gocABD = 30 + 45
    gocACD = 180 - gocABD

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (O) at (2,0);
\\coordinate (A) at (1,1.732);
\\coordinate (D) at (2,-2);
\\draw[line width=1pt] (B)--(A)--(C)--(D)--cycle;
\\draw[line width=1pt] (B)--(C);
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (D) circle (1pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đoạn thẳng $BC = %s\\text{ cm}$. Trên hai nửa mặt phẳng đối nhau bờ $BC$, vẽ hai tam giác vuông $ABC$ vuông tại $A$ có $\\widehat{ABC} = 30^\\circ$ và $DBC$ vuông tại $D$ có $\\widehat{DBC} = 45^\\circ$. Xét tính đúng sai của các khẳng định sau:%s''' % (bc, hinhve))

    nb_da_1_d = '\\True Tứ giác $ABDC$ nội tiếp đường tròn đường kính $BC$'
    nb_da_1_s = 'Tứ giác $ABDC$ nội tiếp đường tròn đường kính $AD$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Gọi $O$ là trung điểm của $BC$. Vì các tam giác $ABC$ và $DBC$ lần lượt vuông tại $A$ và $D$ nên $OA = OB = OC = OD = \\dfrac{BC}{2}$. Suy ra tứ giác $ABDC$ nội tiếp đường tròn đường kính $BC$.''')

    th_da_1_d = '\\True Bán kính đường tròn ngoại tiếp tứ giác $ABDC$ bằng $%s\\text{ cm}$' % (r_val)
    th_da_1_s = 'Bán kính đường tròn ngoại tiếp tứ giác $ABDC$ bằng $%s\\text{ cm}$' % (bc)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Bán kính đường tròn ngoại tiếp tứ giác $ABDC$ là $R = \\dfrac{BC}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.''' % (bc, r_val))

    vd_da_1_d = '\\True Số đo góc $\\widehat{ABD} = %s^\\circ$ và $\\widehat{ACD} = %s^\\circ$' % (gocABD, gocACD)
    vd_da_1_s = 'Số đo góc $\\widehat{ABD} = %s^\\circ$ và $\\widehat{ACD} = %s^\\circ$' % (gocABD, gocABD)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $A$ và $D$ nằm trên hai nửa mặt phẳng đối nhau bờ $BC$ nên $\\widehat{ABD} = \\widehat{ABC} + \\widehat{DBC} = 30^\\circ + 45^\\circ = 75^\\circ$. Do tứ giác $ABDC$ nội tiếp nên $\\widehat{ACD} = 180^\\circ - 75^\\circ = 105^\\circ$.''')

    vdc_da_1_d = '\\True Độ dài cạnh $AC = %s\\text{ cm}$' % (r_val)
    vdc_da_1_s = 'Độ dài cạnh $AC = %s\\sqrt{3}\\text{ cm}$' % (r_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Xét tam giác $ABC$ vuông tại $A$, ta có $AC = BC \\cdot \\sin 30^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (cm)}$.''' % (bc, r_val))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
