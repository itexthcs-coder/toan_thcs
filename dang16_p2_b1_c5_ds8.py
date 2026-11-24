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


def bt_dang16_p2_b1_c5_ds8(self):
    # Dạng 16: Vận dụng - Khảo sát thói quen sử dụng thiết bị điện tử của học sinh
    so_hs_ks = random.choice([60, 80, 100])
    gio_vo_li = random.choice([25, 26, 28, 30])

    noidungcauhoi = ('''Nhóm nghiên cứu của lớp $8D$ muốn tìm hiểu thời gian sử dụng điện thoại thông minh mỗi ngày (đơn vị: giờ) và ứng dụng được học sinh khối $8$ sử dụng nhiều nhất (ví dụ: \\textit{YouTube, TikTok, Zalo, Học trực tuyến}).'''
                     % ())

    nb_da_1_d = '\\True Dữ liệu về tên ứng dụng được sử dụng nhiều nhất thuộc loại dữ liệu không là số, không thể sắp thứ tự'
    nb_da_1_s = 'Dữ liệu về tên ứng dụng được sử dụng nhiều nhất thuộc loại dữ liệu không là số, có thể sắp thứ tự'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Tên các ứng dụng điện thoại là dữ liệu định danh bằng chữ, không phải là số và không có thứ bậc cao thấp nên không thể sắp thứ tự.'''
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Dữ liệu về thời gian sử dụng điện thoại mỗi ngày (đơn vị: giờ) thuộc loại số liệu liên tục'
    th_da_1_s = 'Dữ liệu về thời gian sử dụng điện thoại mỗi ngày (đơn vị: giờ) thuộc loại số liệu rời rạc'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Thời gian sử dụng điện thoại mỗi ngày là đại lượng đo lường có thể nhận giá trị thực tùy ý trong khoảng từ $0$ đến $24$ giờ nên là số liệu liên tục.'''
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu nhóm lập biểu mẫu khảo sát trực tuyến và gửi ngẫu nhiên cho $%s$ học sinh ở tất cả các lớp khối $8$ thì đó là thu thập trực tiếp bằng bảng hỏi' % so_hs_ks
    vd_da_1_s = 'Nếu nhóm lập biểu mẫu khảo sát trực tuyến và gửi ngẫu nhiên cho $%s$ học sinh ở tất cả các lớp khối $8$ thì đó là thu thập gián tiếp' % so_hs_ks
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Nhóm nghiên cứu tự thiết kế bảng hỏi và thu thập câu trả lời trực tiếp từ đối tượng khảo sát (qua biểu mẫu trực tuyến) nên đây là phương pháp thu thập dữ liệu trực tiếp.'''
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Trong kết quả thu về có một phiếu ghi thời gian sử dụng là $%s$ giờ/ngày; ta cần loại bỏ số liệu này vì một ngày chỉ có $24$ giờ' % gio_vo_li
    vdc_da_1_s = 'Trong kết quả thu về có một phiếu ghi thời gian sử dụng là $%s$ giờ/ngày; ta vẫn giữ nguyên số liệu này để tính trung bình' % gio_vo_li
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '''Một ngày chỉ có $24$ giờ nên thời gian sử dụng điện thoại không thể bằng $%s$ giờ/ngày. Đây là dữ liệu không hợp lí cần loại bỏ.''' % gio_vo_li
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
