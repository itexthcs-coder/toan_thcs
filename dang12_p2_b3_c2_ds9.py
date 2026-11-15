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


def bt_dang12_p2_b3_c2_ds9(self):
    lai_suat_phan_tram = random.choice([5, 6, 8])
    lai_suat_thap_phan = Rational(lai_suat_phan_tram, 100)
    tien_goc_min = random.choice([300, 400, 500, 600])
    lai_muc_tieu = int(tien_goc_min * lai_suat_phan_tram / 100)
    tien_gui_thu = tien_goc_min + 50
    lai_thu = Rational(tien_gui_thu * lai_suat_phan_tram, 100)
    vuot_muc_tieu = lai_thu - lai_muc_tieu

    noidungcauhoi = ('''Cô Hoa dự định gửi một khoản tiền $x$ (triệu đồng) vào ngân hàng với kì hạn $1$ năm, lãi suất $%s\\%%$/năm. Cô muốn số tiền lãi nhận được sau $1$ năm ít nhất là $%s$ triệu đồng. Xét tính đúng sai của các khẳng định sau:''' % (latex(lai_suat_phan_tram), latex(lai_muc_tieu)))

    nb_da_1_d = '\\True Số tiền lãi cô Hoa nhận được sau $1$ năm là $%sx$ (triệu đồng)' % (latex(lai_suat_thap_phan))
    nb_da_1_s = 'Số tiền lãi cô Hoa nhận được sau $1$ năm là $%sx$ (triệu đồng)' % (latex(lai_suat_phan_tram))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Với lãi suất $%s\\%%$/năm, tiền lãi sau $1$ năm của $x$ triệu đồng là $\\dfrac{%s}{100}x = %sx$ (triệu đồng).''' % (latex(lai_suat_phan_tram), latex(lai_suat_phan_tram), latex(lai_suat_thap_phan)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bất phương trình mô tả yêu cầu của cô Hoa là $%sx \\ge %s$' % (latex(lai_suat_thap_phan), latex(lai_muc_tieu))
    th_da_1_s = 'Bất phương trình mô tả yêu cầu của cô Hoa là $%sx \\le %s$' % (latex(lai_suat_thap_phan), latex(lai_muc_tieu))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì số tiền lãi ít nhất là $%s$ triệu đồng nên ta có bất phương trình $%sx \\ge %s$.''' % (latex(lai_muc_tieu), latex(lai_suat_thap_phan), latex(lai_muc_tieu)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Số tiền cô Hoa cần gửi ít nhất là $%s$ triệu đồng' % (latex(tien_goc_min))
    vd_da_1_s = 'Số tiền cô Hoa cần gửi ít nhất là $%s$ triệu đồng' % (latex(tien_goc_min // 10))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải bất phương trình $%sx \\ge %s \\Leftrightarrow x \\ge %s : %s = %s$. Vậy cần gửi ít nhất $%s$ triệu đồng.''' % (latex(lai_suat_thap_phan), latex(lai_muc_tieu), latex(lai_muc_tieu), latex(lai_suat_thap_phan), latex(tien_goc_min), latex(tien_goc_min)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu cô Hoa gửi $%s$ triệu đồng thì tiền lãi sau $1$ năm vượt mục tiêu đề ra là $%s$ triệu đồng' % (latex(tien_gui_thu), latex(vuot_muc_tieu))
    vdc_da_1_s = 'Nếu cô Hoa gửi $%s$ triệu đồng thì tiền lãi sau $1$ năm vượt mục tiêu đề ra là $%s$ triệu đồng' % (latex(tien_gui_thu), latex(vuot_muc_tieu + 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi gửi $%s$ triệu đồng, tiền lãi nhận được là $%s \\cdot %s = %s$ (triệu đồng), vượt mục tiêu là $%s - %s = %s$ (triệu đồng).''' % (latex(tien_gui_thu), latex(tien_gui_thu), latex(lai_suat_thap_phan), latex(lai_thu), latex(lai_thu), latex(lai_muc_tieu), latex(vuot_muc_tieu)))
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
