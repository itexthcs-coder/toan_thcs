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


def bt_dang18_p2_b2_c5_ds8(self):
    # Dạng 18 (Vận dụng - Thực tế): Theo dõi tăng trưởng năng suất lúa qua các năm bằng biểu đồ đoạn thẳng
    def fmt_vn(val):
        return f"{val:.1f}".replace(".", ",")
        
    d = Decimal(str(random.choice([0.0, 1.0, 2.0])))
    y21 = Decimal('58.5') + d
    y22 = Decimal('60.0') + d
    y23 = Decimal('59.2') + d
    y24 = Decimal('62.4') + d
    y25 = Decimal('64.5') + d
    
    giam_23 = y22 - y23
    tang_tong = y25 - y21
    
    noidungcauhoi = ("""Bảng số liệu sau ghi lại năng suất lúa trung bình (đơn vị: tạ/ha) của một hợp tác xã nông nghiệp qua $5$ năm liên tiếp:\\\\
    \begin{center}
    \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    \textbf{Năm} & $2021$ & $2022$ & $2023$ & $2024$ & $2025$ \\\\
    \hline
    \textbf{Năng suất (tạ/ha)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \hline
    \end{tabular}
    \end{center}
    Xét tính đúng sai của các khẳng định sau:""" % (fmt_vn(y21), fmt_vn(y22), fmt_vn(y23), fmt_vn(y24), fmt_vn(y25)))
    
    nb_da_1_d = '\\True Biểu đồ đoạn thẳng là lựa chọn tối ưu để thể hiện xu hướng biến động năng suất lúa của hợp tác xã qua $5$ năm'
    nb_da_1_s = 'Biểu đồ hình quạt tròn là lựa chọn tối ưu để thể hiện xu hướng biến động năng suất lúa qua $5$ năm'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Dữ liệu ghi lại sự biến đổi của năng suất lúa qua các mốc thời gian liên tục ($2021 - 2025$) nên biểu đồ đoạn thẳng là lựa chọn tối ưu.""")
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Năng suất lúa giảm nhẹ vào năm $2023$ (giảm $%s\\text{ tạ/ha}$ so với năm $2022$), sau đó tăng liên tục trong hai năm $2024$ và $2025$' % fmt_vn(giam_23)
    th_da_1_s = 'Năng suất lúa tăng liên tục qua tất cả các năm từ $2021$ đến $2025$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Từ năm $2022$ ($%s\\text{ tạ/ha}$) sang năm $2023$ ($%s\\text{ tạ/ha}$), năng suất giảm $%s - %s = %s\\text{ tạ/ha}$, sau đó tăng lên $%s$ và $%s\\text{ tạ/ha}$."""
                    % (fmt_vn(y22), fmt_vn(y23), fmt_vn(y22), fmt_vn(y23), fmt_vn(giam_23), fmt_vn(y24), fmt_vn(y25)))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_s = '\\True Có thể dùng biểu đồ tranh để biểu diễn chính xác bảng số liệu trên vì có tới $5$ mốc thời gian'
    vd_da_1_d = 'Không nên dùng biểu đồ tranh để biểu diễn bảng số liệu trên vì các số liệu đều là số thập phân lẻ'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Các số liệu năng suất đều là số thập phân lẻ nên không phù hợp để vẽ biểu đồ tranh.""")
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_d = '\\True So với năm $2021$, năng suất lúa năm $2025$ đã tăng thêm $%s\\text{ tạ/ha}$' % fmt_vn(tang_tong)
    vdc_da_1_s = 'So với năm $2021$, năng suất lúa năm $2025$ đã tăng thêm $%s\\text{ tạ/ha}$' % fmt_vn(tang_tong + Decimal('1.0'))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Mức tăng năng suất từ năm $2021$ đến năm $2025$ là: $%s - %s = %s$ (tạ/ha).""" % (fmt_vn(y25), fmt_vn(y21), fmt_vn(tang_tong)))
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
