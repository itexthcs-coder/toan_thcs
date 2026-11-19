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


def bt_dang6_p2_b3_c9_hh9(self):
    gocA = randint(45, 70)
    gocEBD = 90 - gocA
    gocEID = 2 * gocEBD

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (I) at (2,0);
\\coordinate (A) at (1.5,2.8);
\\coordinate (D) at ($(A)!(B)!(C)$);
\\coordinate (E) at ($(A)!(C)!(B)$);
\\coordinate (H) at (intersection of B--D and C--E);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (B)--(D) (C)--(E) (E)--(D);
\\draw[line width=1pt, dashed] (I)--(E) (I)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (I) circle (1pt) node[below] {$I$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho tam giác $ABC$ nhọn có hai đường cao $BD$ và $CE$ cắt nhau tại trực tâm $H$ ($D \\in AC, E \\in AB$). Gọi $I$ là trung điểm của đoạn thẳng $BC$. Xét tính đúng sai của các khẳng định sau:%s''' % (hinhve))

    nb_da_1_d = '\\True Bốn điểm $B, E, D, C$ cùng nằm trên một đường tròn tâm $I$'
    nb_da_1_s = 'Bốn điểm $B, E, D, C$ cùng nằm trên một đường tròn tâm $H$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì các tam giác $BEC$ và $BDC$ lần lượt vuông tại $E$ và $D$ có $I$ là trung điểm cạnh huyền $BC$ nên $IB = IC = IE = ID = \\dfrac{BC}{2}$. Suy ra bốn điểm $B, E, D, C$ cùng nằm trên đường tròn tâm $I$.''')

    th_da_1_d = '\\True Tứ giác $AEHD$ nội tiếp đường tròn có tâm là trung điểm của đoạn thẳng $AH$'
    th_da_1_s = 'Tứ giác $AEHD$ nội tiếp đường tròn có tâm là giao điểm của $AH$ và $ED$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Gọi $K$ là trung điểm của $AH$. Các tam giác vuông $AEH$ và $ADH$ có chung cạnh huyền $AH$ nên $KA = KH = KE = KD = \\dfrac{AH}{2}$. Vậy tứ giác $AEHD$ nội tiếp đường tròn tâm $K$ là trung điểm của $AH$.''')

    vd_da_1_d = '\\True $\\widehat{AED} = \\widehat{ACB}$'
    vd_da_1_s = '$\\widehat{AED} + \\widehat{ABC} = 180^\\circ$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì tứ giác $BEDC$ nội tiếp nên $\\widehat{BED} + \\widehat{BCD} = 180^\\circ$. Mà $\\widehat{AED} + \\widehat{BED} = 180^\\circ$ (hai góc kề bù) nên $\\widehat{AED} = \\widehat{BCD} = \\widehat{ACB}$.''')

    vdc_da_1_d = '\\True Nếu $\\widehat{BAC} = %s^\\circ$ thì $\\widehat{EID} = %s^\\circ$' % (gocA, gocEID)
    vdc_da_1_s = 'Nếu $\\widehat{BAC} = %s^\\circ$ thì $\\widehat{EID} = %s^\\circ$' % (gocA, 2 * gocA)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Trong tam giác $ABD$ vuông tại $D$, ta có $\\widehat{EBD} = 90^\\circ - \\widehat{BAC} = 90^\\circ - %s^\\circ = %s^\\circ$. Xét đường tròn $(I)$, góc ở tâm $\\widehat{EID}$ và góc nội tiếp $\\widehat{EBD}$ cùng chắn cung $ED$ nên $\\widehat{EID} = 2\\widehat{EBD} = 2 \\cdot %s^\\circ = %s^\\circ$.''' % (gocA, gocEBD, gocEBD, gocEID))

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
