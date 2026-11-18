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


def bt_dang7_p2_b2_c7_ds9(self):
    p_huu_co = random.choice([52, 55, 58])
    p_vo_co = 100 - p_huu_co - 36
    tong_xy = 36
    y_val = 12
    x_val = 24

    bang = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|c|c|c|c|}\n'
        '\\hline\n'
        'Loại rác & Rác hữu cơ & Rác nhựa & Giấy và bìa & Rác vô cơ khác \\\\ \n'
        '\\hline\n'
        'Tần số tương đối & $%s\\%%$ & $x\\%%$ & $y\\%%$ & $%s\\%%$ \\\\ \n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}'
    ) % (p_huu_co, p_vo_co)

    noidungcauhoi = ('Bảng tần số tương đối thống kê khối lượng các loại rác thải sinh hoạt thu gom được trong một ngày tại một khu dân cư như sau:%sBiết rằng tỉ lệ rác nhựa gấp đôi tỉ lệ giấy và bìa ($x = 2y$). Xét tính đúng sai của các khẳng định sau:' % (bang))

    nb_da_1_d = '\\True Tổng tỉ lệ của rác nhựa và giấy và bìa là $x + y = %s$' % (tong_xy)
    nb_da_1_s = 'Tổng tỉ lệ của rác nhựa và giấy và bìa là $x + y = %s$' % (tong_xy + 6)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Vì tổng các tần số tương đối bằng $100\\%%$ nên $x + y = 100 - (%s + %s) = %s$.' % (p_huu_co, p_vo_co, tong_xy))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tần số tương đối của rác nhựa là $%s\\%%$' % (x_val)
    th_da_1_s = 'Tần số tương đối của rác nhựa là $%s\\%%$' % (y_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Thay $x = 2y$ vào $x + y = %s$ ta được $3y = %s \\Rightarrow y = %s$, suy ra $x = 2 \\cdot %s = %s$. Vậy rác nhựa chiếm $%s\\%%$.' % (tong_xy, tong_xy, y_val, y_val, x_val, x_val))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tần số tương đối của giấy và bìa là $%s\\%%$' % (y_val)
    vd_da_1_s = 'Tần số tương đối của giấy và bìa là $18\\%%$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Theo kết quả giải hệ trên, tần số tương đối của giấy và bìa là $y = %s\\%%$.' % (y_val))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Rác hữu cơ chiếm hơn một nửa tổng lượng rác thải thu gom được trong ngày'
    vdc_da_1_s = 'Rác hữu cơ chiếm ít hơn một nửa tổng lượng rác thải thu gom được trong ngày'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Vì tần số tương đối của rác hữu cơ là $%s\\%% > 50\\%%$ nên rác hữu cơ chiếm hơn một nửa tổng lượng rác thải.' % (p_huu_co))
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
