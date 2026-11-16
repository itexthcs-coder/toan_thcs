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


def bt_dang11_p2_b1_c5_hh9(self):
    # Khai báo biến
    xi = random.randint(1, 3)
    yi = -random.randint(1, 3)
    R = 5
    xa = xi + 3
    ya = yi + 4
    io_sq = xi**2 + yi**2
    rem_sq = R**2 - xi**2
    xb1 = 2 * xi - xa
    yb1 = 2 * yi - ya

    noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho điểm $I(%s; %s)$ và đường tròn $(I; %s)$. Xét tính đúng sai của các khẳng định sau:'''
                     % (xi, yi, R))

    nb_da_1_d = '\\True Điểm $A(%s; %s)$ nằm trên đường tròn $(I; %s)$' % (xa, ya, R)
    nb_da_1_s = 'Điểm $A(%s; %s)$ nằm bên ngoài đường tròn $(I; %s)$' % (xa, ya, R)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta tính khoảng cách từ tâm $I(%s; %s)$ đến điểm $A(%s; %s)$:\\\\
$IA = \\sqrt{(%s - %s)^2 + (%s - (%s))^2} = \\sqrt{3^2 + 4^2} = %s = R$. Vậy điểm $A$ nằm trên đường tròn $(I; %s)$.''' % (xi, yi, xa, ya, xa, xi, ya, yi, R, R))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Gốc tọa độ $O(0; 0)$ nằm bên trong đường tròn $(I; %s)$' % R
    th_da_1_s = 'Gốc tọa độ $O(0; 0)$ nằm bên ngoài đường tròn $(I; %s)$' % R
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $IO = \\sqrt{%s^2 + (%s)^2} = \\sqrt{%s} < %s = R$. Vậy gốc tọa độ $O(0; 0)$ nằm bên trong đường tròn $(I; %s)$.''' % (xi, yi, io_sq, R, R))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đường tròn $(I; %s)$ cắt trục tung $Oy$ tại hai điểm có tung độ lần lượt là $y_1 = \\sqrt{%s} %s$ và $y_2 = -\\sqrt{%s} %s$' % (R, rem_sq, yi, rem_sq, yi)
    vd_da_1_s = 'Đường tròn $(I; %s)$ không cắt trục tung $Oy$' % R
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Gọi $M(0; y)$ là giao điểm của $(I; %s)$ với trục tung $Oy$. Khi đó $IM = %s \\Leftrightarrow (0 - %s)^2 + (y - (%s))^2 = %s \\Leftrightarrow (y + %s)^2 = %s \\Leftrightarrow y = \\pm\\sqrt{%s} %s$.''' % (R, R, xi, yi, R**2, -yi, rem_sq, rem_sq, yi))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = "\\True Điểm $B'(%s; %s)$ đối xứng với $A$ qua tâm $I$ và thuộc đường tròn $(I; %s)$" % (xb1, yb1, R)
    vdc_da_1_s = "Điểm $B'(%s; %s)$ đối xứng với $A$ qua tâm $I$ nhưng không thuộc đường tròn $(I; %s)$" % (xb1, yb1, R)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $I$ là trung điểm của $AB'$ nên $x_{B'} = 2 \\cdot %s - %s = %s$ và $y_{B'} = 2 \\cdot (%s) - %s = %s$. Do $I$ là tâm đối xứng của $(I; %s)$ và $A \\in (I)$ nên $B' \\in (I; %s)$.''' % (xi, xa, xb1, yi, ya, yb1, R, R))
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
