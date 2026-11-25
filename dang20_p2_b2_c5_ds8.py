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


def bt_dang20_p2_b2_c5_ds8(self):
    # Dạng 20 (Vận dụng - Thực tế): Phân tích dữ liệu y tế và lựa chọn biểu đồ đa mục tiêu
    so_thang = random.choice([12, 18, 24])
    so_moc = so_thang + 1
    
    noidungcauhoi = ("""Một phòng khám dinh dưỡng theo dõi cân nặng của bé Minh từ lúc sơ sinh đến $%s$ tháng tuổi (đo định kì mỗi tháng một lần, gồm $%s$ mốc thời gian) và đồng thời khảo sát tỉ lệ phần trăm của $4$ nhóm chất dinh dưỡng (Chất đạm, Chất béo, Tinh bột, Vitamin và khoáng chất) trong khẩu phần ăn hằng ngày của bé. Xét tính đúng sai của các khẳng định sau:"""
                     % (so_thang, so_moc))
    
    nb_da_1_d = '\\True Để theo dõi sự phát triển cân nặng của bé Minh qua $%s$ mốc thời gian liên tục, bác sĩ nên dùng biểu đồ đoạn thẳng thay vì biểu đồ cột' % so_moc
    nb_da_1_s = 'Để theo dõi sự phát triển cân nặng của bé Minh qua $%s$ mốc thời gian liên tục, bác sĩ nên dùng biểu đồ hình quạt tròn' % so_moc
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Cân nặng thay đổi liên tục theo các mốc thời gian ($%s$ mốc quan sát) nên biểu đồ đoạn thẳng giúp thấy rõ đường cong tăng trưởng của bé.""" % so_moc)
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Để tư vấn cho phụ huynh thấy rõ tỉ lệ phần trăm của $4$ nhóm chất dinh dưỡng trong khẩu phần ăn chuẩn, bác sĩ nên dùng biểu đồ hình quạt tròn'
    th_da_1_s = 'Để thể hiện tỉ lệ phần trăm của $4$ nhóm chất dinh dưỡng trong khẩu phần ăn chuẩn, bác sĩ nên dùng biểu đồ tranh'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Khẩu phần ăn chuẩn là một tổng thể ($100\\%%$) chia thành $4$ nhóm chất nên biểu đồ hình quạt tròn thể hiện trực quan nhất tỉ trọng từng nhóm chất.""")
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Nếu muốn so sánh cân nặng của bé Minh với cân nặng chuẩn của Tổ chức Y tế Thế giới (WHO) tại các mốc $0, 3, 6, 9, 12$ tháng tuổi, có thể dùng biểu đồ cột kép'
    vd_da_1_s = 'Không thể dùng biểu đồ cột kép để so sánh cân nặng của bé Minh với cân nặng chuẩn của WHO tại các mốc tháng tuổi'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tại $5$ mốc thời gian xác định ($0, 3, 6, 9, 12$ tháng tuổi), việc đối chiếu hai tập dữ liệu (bé Minh và chuẩn WHO) thực hiện rất trực quan bằng biểu đồ cột kép.""")
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Cả hai bộ dữ liệu (cân nặng theo $%s$ tháng và tỉ lệ $4$ nhóm chất) đều nên biểu diễn chung trên một biểu đồ tranh duy nhất' % so_thang
    vdc_da_1_d = 'Hai bộ dữ liệu trên có bản chất và đơn vị hoàn toàn khác nhau nên cần biểu diễn bằng hai loại biểu đồ riêng biệt phù hợp với từng mục đích'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Cân nặng (số thập phân biến thiên theo thời gian) và cơ cấu dinh dưỡng (tỉ lệ phần trăm) có bản chất và đơn vị khác nhau, không thể gộp chung vào một biểu đồ tranh duy nhất.""")
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
