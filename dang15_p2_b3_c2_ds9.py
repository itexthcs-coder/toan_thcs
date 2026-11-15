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


def bt_dang15_p2_b3_c2_ds9(self):
    tong_cau = random.choice([25, 30])
    diem_tang = random.choice([5, 10])
    diem_dung = random.choice([2, 3])
    diem_sai = random.choice([1, 2])
    he_so_x = diem_dung + diem_sai
    hang_so = diem_tang - diem_sai * tong_cau
    cau_dung_min = random.randint(18, 22)
    diem_chuan = he_so_x * cau_dung_min + hang_so - random.randint(0, he_so_x - 1)

    noidungcauhoi = ('''Trong một vòng thi kiến thức gồm $%s$ câu hỏi, mỗi thí sinh được tặng sẵn $%s$ điểm. Trả lời đúng mỗi câu được cộng $%s$ điểm, trả lời sai hoặc bỏ qua mỗi câu bị trừ $%s$ điểm. Thí sinh cần đạt từ $%s$ điểm trở lên mới được vào vòng chung kết. Gọi $x$ ($x \\in \\mathbb{N}, x \\le %s$) là số câu thí sinh trả lời đúng. Xét tính đúng sai của các khẳng định sau:''' % (latex(tong_cau), latex(diem_tang), latex(diem_dung), latex(diem_sai), latex(diem_chuan), latex(tong_cau)))

    nb_da_1_d = '\\True Số câu thí sinh trả lời sai hoặc bỏ qua là $%s - x$ (câu)' % (latex(tong_cau))
    nb_da_1_s = 'Số câu thí sinh trả lời sai hoặc bỏ qua là $x - %s$ (câu)' % (latex(tong_cau))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì tổng số câu là $%s$ và số câu đúng là $x$ nên số câu sai hoặc bỏ qua là $%s - x$.''' % (latex(tong_cau), latex(tong_cau)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tổng số điểm thí sinh đạt được sau khi hoàn thành $%s$ câu hỏi là $%s + %sx - %s(%s - x)$' % (latex(tong_cau), latex(diem_tang), latex(diem_dung), latex(diem_sai), latex(tong_cau))
    th_da_1_s = 'Tổng số điểm thí sinh đạt được sau khi hoàn thành $%s$ câu hỏi là $%s + %sx + %s(%s - x)$' % (latex(tong_cau), latex(diem_tang), latex(diem_dung), latex(diem_sai), latex(tong_cau))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Điểm đạt được bằng điểm tặng sẵn cộng điểm câu đúng trừ đi điểm bị phạt câu sai: $%s + %sx - %s(%s - x)$.''' % (latex(diem_tang), latex(diem_dung), latex(diem_sai), latex(tong_cau)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Để vào vòng chung kết, số câu trả lời đúng $x$ phải thỏa mãn bất phương trình $%sx + (%s) \\ge %s$' % (latex(he_so_x), latex(hang_so), latex(diem_chuan))
    vd_da_1_s = 'Để vào vòng chung kết, số câu trả lời đúng $x$ phải thỏa mãn bất phương trình $%sx + (%s) > %s$' % (latex(he_so_x), latex(hang_so), latex(diem_chuan))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Rút gọn biểu thức điểm số ta được $%sx + (%s)$. Cần đạt từ $%s$ điểm trở lên nên $%sx + (%s) \\ge %s$.''' % (latex(he_so_x), latex(hang_so), latex(diem_chuan), latex(he_so_x), latex(hang_so), latex(diem_chuan)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi mới đủ điều kiện vào vòng chung kết' % (latex(cau_dung_min))
    vdc_da_1_s = 'Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi mới đủ điều kiện vào vòng chung kết' % (latex(cau_dung_min - 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình $%sx \\ge %s \\Leftrightarrow x \\ge \\dfrac{%s}{%s}$. Vì $x \\in \\mathbb{N}$ nên thí sinh cần đúng ít nhất $%s$ câu.''' % (latex(he_so_x), latex(diem_chuan - hang_so), latex(diem_chuan - hang_so), latex(he_so_x), latex(cau_dung_min)))
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
