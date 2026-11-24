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


def bt_dang11_p2_b1_c5_ds8(self):
    # Dạng 11: Vận dụng - Thiết kế khảo sát thói quen đọc sách toàn trường
    so_lop_khoi = random.choice([4, 5, 6])
    so_hs_chon = random.choice([5, 6, 8])
    tong_mau = 4 * so_lop_khoi * so_hs_chon

    noidungcauhoi = ('''Ban chấp hành Đoàn trường muốn ước lượng thời gian đọc sách trung bình mỗi tuần (đơn vị: giờ) của học sinh toàn trường (gồm $4$ khối $6, 7, 8, 9$, mỗi khối có $%s$ lớp) để đề xuất mua bổ sung sách cho thư viện.'''
                     % so_lop_khoi)

    nb_da_1_d = '\\True Dữ liệu cần thu thập về thời gian đọc sách (tính theo giờ) thuộc loại số liệu liên tục'
    nb_da_1_s = 'Dữ liệu cần thu thập về thời gian đọc sách (tính theo giờ) thuộc loại số liệu rời rạc'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Thời gian đọc sách tính theo giờ là đại lượng đo lường có thể nhận giá trị thực tùy ý trong một khoảng (ví dụ $2,5$ giờ; $4,25$ giờ) nên là số liệu liên tục.'''
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Nếu chỉ phát phiếu khảo sát cho toàn bộ học sinh lớp $9A$ thì dữ liệu thu được không đảm bảo tính đại diện cho toàn trường'
    th_da_1_s = 'Nếu chỉ phát phiếu khảo sát cho toàn bộ học sinh lớp $9A$ thì dữ liệu thu được vẫn đảm bảo tính đại diện cho toàn trường'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Học sinh khối $9$ có lịch học và thói quen đọc sách khác với các khối $6, 7, 8$ nên chỉ khảo sát một lớp $9A$ sẽ không đại diện cho toàn trường.'''
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Cách thu thập hợp lí là chọn ngẫu nhiên mỗi lớp $%s$ học sinh (tổng cộng $%s$ học sinh) và phát bảng hỏi trực tiếp' % (so_hs_chon, tong_mau)
    vd_da_1_s = 'Cách thu thập hợp lí là chỉ phỏng vấn các bạn học sinh đang ngồi đọc sách trong thư viện vào giờ ra chơi'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Chọn ngẫu nhiên học sinh ở tất cả các lớp thuộc cả $4$ khối giúp mẫu khảo sát phân bố đều và đảm bảo tính đại diện cho toàn trường; còn nếu chỉ hỏi trong thư viện thì kết quả sẽ bị lệch về nhóm học sinh chăm đọc sách.'''
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu trong phiếu khảo sát thu được một kết quả ghi thời gian đọc sách là $200$ giờ/tuần thì cần loại bỏ vì một tuần chỉ có $168$ giờ'
    vdc_da_1_s = 'Nếu trong phiếu khảo sát thu được một kết quả ghi thời gian đọc sách là $200$ giờ/tuần thì vẫn giữ lại vì đó là số liệu liên tục'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '''Một tuần có $7 \\times 24 = 168$ giờ nên thời gian đọc sách mỗi tuần không thể đạt tới $200$ giờ. Đây là giá trị không hợp lí cần loại bỏ trước khi tính toán.'''
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
