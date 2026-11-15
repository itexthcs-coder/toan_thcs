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


def bt_dang18_p2_b3_c2_ds9(self):
    d1 = random.choice([7, 8])
    d2 = 8
    d3 = random.choice([8, 9])
    gk = random.choice([7, 8])
    tong_hien_tai = d1 + d2 + d3 + 2 * gk
    ck_min = Rational(64 - tong_hien_tai, 3)

    noidungcauhoi = ('''Điểm đánh giá môn Toán học kì I của bạn Hùng gồm: $3$ bài kiểm tra thường xuyên (hệ số $1$) đạt lần lượt là $%s$; $%s$; $%s$; điểm kiểm tra giữa kì (hệ số $2$) đạt $%s$. Hùng muốn đạt danh hiệu Học sinh Giỏi nên điểm trung bình môn Toán cả kì phải từ $8$ trở lên. Gọi $x$ ($0 \\le x \\le 10$) là điểm bài kiểm tra cuối kì (hệ số $3$) của Hùng. Xét tính đúng sai của các khẳng định sau:''' % (latex(d1), latex(d2), latex(d3), latex(gk)))

    nb_da_1_d = '\\True Tổng hệ số của tất cả các bài kiểm tra môn Toán trong học kì I là $8$'
    nb_da_1_s = 'Tổng hệ số của tất cả các bài kiểm tra môn Toán trong học kì I là $5$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng hệ số bằng $1 + 1 + 1 + 2 + 3 = 8$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Điểm trung bình môn Toán của Hùng được tính bởi biểu thức $\\dfrac{%s + 3x}{8}$' % (latex(tong_hien_tai))
    th_da_1_s = 'Điểm trung bình môn Toán của Hùng được tính bởi biểu thức $\\dfrac{%s + x}{8}$' % (latex(tong_hien_tai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tổng điểm nhân hệ số là $%s + %s + %s + 2 \\cdot %s + 3x = %s + 3x$, chia cho tổng hệ số $8$ ta được $\\dfrac{%s + 3x}{8}$.''' % (latex(d1), latex(d2), latex(d3), latex(gk), latex(tong_hien_tai), latex(tong_hien_tai)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Bất phương trình để Hùng đạt mục tiêu là $%s + 3x \\ge 64$' % (latex(tong_hien_tai))
    vd_da_1_s = 'Bất phương trình để Hùng đạt mục tiêu là $%s + 3x > 64$' % (latex(tong_hien_tai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\dfrac{%s + 3x}{8} \\ge 8 \\Leftrightarrow %s + 3x \\ge 64$.''' % (latex(tong_hien_tai), latex(tong_hien_tai)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Hùng cần đạt tối thiểu $%s$ điểm ở bài kiểm tra cuối kì mới đạt được mục tiêu đề ra' % (latex(ck_min))
    vdc_da_1_s = 'Hùng cần đạt tối thiểu $%s$ điểm ở bài kiểm tra cuối kì mới đạt được mục tiêu đề ra' % (latex(ck_min + 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình $3x \\ge %s \\Leftrightarrow x \\ge %s$.''' % (latex(64 - tong_hien_tai), latex(ck_min)))
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
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
