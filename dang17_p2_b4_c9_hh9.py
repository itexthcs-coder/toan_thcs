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


def bt_dang17_p2_b4_c9_hh9(self):
    so_khoang = random.choice([2, 3, 5])
    goc_b = so_khoang * 45

    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (O) circle (1.7);
\\foreach \\i in {0,45,...,315} {
    \\draw[line width=1pt] (O)--(\\i:1.7);
    \\fill (\\i:1.7) circle (1pt);
}
\\draw[line width=1pt] (-0.8,-2.1)--(O)--(0.8,-2.1);
\\fill (O) circle (1pt) node[below] {$O$};
\\node[above] at (90:1.7) {Cao nhất};
\\node[below] at (270:1.7) {$A$};
\\node[below left] at (225:1.7) {$B$};
\\end{tikzpicture}
\\end{center}'''

    noidungcauhoi = ('''Một vòng quay mặt trời (đu quay) trong công viên giải trí có $8$ cabin được gắn cách đều nhau trên vành tròn tâm $O$, tạo thành các đỉnh của một bát giác đều (như hình vẽ). Tại thời điểm bắt đầu xét, cabin $A$ đang ở vị trí thấp nhất, còn cabin $B$ đang ở vị trí cách vị trí cao nhất đúng $%s$ khoảng cabin tính theo chiều quay của kim đồng hồ. Xét tính đúng sai của các khẳng định sau: %s''' % (so_khoang, hinh_tikz))

    nb_da_1_d = '\\True Hai cabin liên tiếp bất kì tạo với tâm $O$ của vòng quay một góc ở tâm bằng $45^\\circ$'
    nb_da_1_s = 'Hai cabin liên tiếp bất kì tạo với tâm $O$ của vòng quay một góc ở tâm bằng $60^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $8$ cabin chia đường tròn thành $8$ cung bằng nhau nên góc ở tâm chắn giữa hai cabin liên tiếp bằng $\\frac{360^\\circ}{8} = 45^\\circ$.''')

    th_da_1_d = '\\True Để cabin $B$ di chuyển đến vị trí cao nhất thì vòng quay phải quay thuận chiều kim đồng hồ quanh tâm $O$ một góc $%s^\\circ$' % (goc_b)
    th_da_1_s = 'Để cabin $B$ di chuyển đến vị trí cao nhất thì vòng quay phải quay thuận chiều kim đồng hồ quanh tâm $O$ một góc $%s^\\circ$' % (360 - goc_b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Từ vị trí cabin $B$ đi thuận chiều kim đồng hồ đến vị trí cao nhất qua $%s$ khoảng cabin, nên góc quay cần thiết là $%s \\cdot 45^\\circ = %s^\\circ$.''' % (so_khoang, so_khoang, goc_b))

    vd_da_1_d = '\\True Để cabin $A$ (từ vị trí thấp nhất) di chuyển lên vị trí cao nhất thì vòng quay phải quay một góc $180^\\circ$'
    vd_da_1_s = 'Để cabin $A$ (từ vị trí thấp nhất) di chuyển lên vị trí cao nhất thì vòng quay phải quay một góc $135^\\circ$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vị trí thấp nhất và vị trí cao nhất đối xứng nhau qua tâm $O$ (cách nhau $4$ khoảng cabin) nên góc quay bằng $4 \\cdot 45^\\circ = 180^\\circ$.''')

    vdc_da_1_d = '\\True Khi vòng quay quay thuận chiều kim đồng hồ quanh tâm $O$ một góc $90^\\circ$ thì hình dáng tổng thể của vòng quay vẫn được giữ nguyên'
    vdc_da_1_s = 'Chỉ khi vòng quay quay đủ một vòng $360^\\circ$ thì hình dáng tổng thể của vòng quay mới được giữ nguyên'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $90^\\circ = 2 \\cdot 45^\\circ$ nên phép quay thuận chiều $90^\\circ$ tâm $O$ biến mỗi đỉnh của bát giác đều thành một đỉnh của bát giác đều đó, giữ nguyên hình dáng tổng thể của vòng quay.''')

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
