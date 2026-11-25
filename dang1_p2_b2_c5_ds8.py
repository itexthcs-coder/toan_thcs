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


def bt_dang1_p2_b2_c5_ds8(self):
    # Dạng 1 (Thông hiểu - Thuần túy toán học): Quy tắc chọn biểu đồ theo bản chất biến số và số mốc quan sát
    u = random.choice([20, 25, 30, 50])
    n_moc = random.choice([30, 35, 40, 45])
    
    noidungcauhoi = ("""Cho bốn tập dữ liệu $A, B, C, D$ cùng ghi lại giá trị của đại lượng $Y$ theo biến $X$:
    \\begin{itemize}
    \\item Tập $A$: $X$ nhận $4$ giá trị là các nhóm phân loại độc lập; $Y$ là số nguyên chia hết cho $%s$.
    \\item Tập $B$: $X$ là chuỗi $%s$ mốc thời gian liên tiếp; $Y$ là số thực dương.
    \\item Tập $C$: $X$ nhận $5$ giá trị phân loại; $Y$ là tỉ lệ phần trăm của từng thành phần trong một tổng thể ($100\\%%$).
    \\item Tập $D$: $X$ nhận $4$ giá trị phân loại; $Y$ là các số thập phân lẻ đến hai chữ số sau dấu phẩy.
    \\end{itemize}
    Xét tính đúng sai của các khẳng định sau:""" % (u, n_moc))
    
    nb_da_1_d = '\\True Có thể dùng biểu đồ tranh với quy ước $1$ biểu tượng ứng với $%s$ đơn vị để biểu diễn tập dữ liệu $A$' % u
    nb_da_1_s = 'Không thể dùng biểu đồ tranh để biểu diễn tập dữ liệu $A$ vì $Y$ chia hết cho $%s$' % u
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Tập dữ liệu $A$ gồm $4$ nhóm phân loại độc lập và giá trị $Y$ chia hết cho $%s$ nên có thể dùng biểu đồ tranh với quy ước $1$ biểu tượng ứng với $%s$ đơn vị.""" % (u, u))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_s = '\\True Tập dữ liệu $B$ nên biểu diễn bằng biểu đồ cột thay vì biểu đồ đoạn thẳng để dễ so sánh chiều cao các cột'
    th_da_1_d = 'Tập dữ liệu $B$ nên biểu diễn bằng biểu đồ đoạn thẳng để thấy rõ xu hướng biến thiên theo thời gian'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tập dữ liệu $B$ có tới $%s$ mốc thời gian liên tiếp. Khi số lượng thời điểm quan sát rất nhiều, ta nên dùng biểu đồ đoạn thẳng để thấy rõ xu hướng biến động theo thời gian, tránh vẽ biểu đồ cột gây rối mắt.""" % n_moc)
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Biểu đồ hình quạt tròn là lựa chọn phù hợp nhất cho tập dữ liệu $C$'
    vd_da_1_s = 'Biểu đồ đoạn thẳng là lựa chọn phù hợp nhất cho tập dữ liệu $C$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tập dữ liệu $C$ biểu diễn cơ cấu tỉ lệ phần trăm của $5$ thành phần trong một tổng thể ($100\\%%$) nên biểu đồ hình quạt tròn là phù hợp nhất.""")
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Tập dữ liệu $D$ biểu diễn tốt nhất bằng biểu đồ tranh bằng cách làm tròn tất cả các số liệu về hàng chục'
    vdc_da_1_d = 'Tập dữ liệu $D$ biểu diễn chính xác và trực quan nhất bằng biểu đồ cột'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Tập dữ liệu $D$ gồm các số thập phân lẻ đến hai chữ số sau dấu phẩy và không thay đổi theo thời gian nên biểu diễn chính xác nhất bằng biểu đồ cột. Việc làm tròn tùy tiện về hàng chục để vẽ biểu đồ tranh làm sai lệch nghiêm trọng dữ liệu gốc.""")
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
