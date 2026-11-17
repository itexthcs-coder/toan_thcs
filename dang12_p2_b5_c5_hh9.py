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


def bt_dang12_p2_b5_c5_hh9(self):
    def fmt(val):
        if isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val).replace('.', ',')

    ab = random.choice([6, 7, 8])
    ra = ab - 2.5
    rb = ab - 3.5
    kc_nguoi = round(ab - rb + 0.3, 1)
    kc_den_b = round(ab - kc_nguoi, 1)
    rb_moi = ab + ra + 0.5

    noidungcauhoi = ("""Hai trạm phát sóng điện thoại đặt tại hai vị trí $A$ và $B$ cách nhau $%s\\text{ km}$. Trạm $A$ có bán kính phủ sóng là $%s\\text{ km}$, trạm $B$ có bán kính phủ sóng là $%s\\text{ km}$ (xem vùng phủ sóng mỗi trạm là một hình tròn).""" % (fmt(ab), fmt(ra), fmt(rb)))

    # Nhận biết
    nb_da_1_d = '\\True Biên giới vùng phủ sóng của hai trạm là hai đường tròn cắt nhau'
    nb_da_1_s = 'Biên giới vùng phủ sóng của hai trạm là hai đường tròn ở ngoài nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Ta có $R_A - R_B = %s - %s = %s\\text{ km}$ và $R_A + R_B = %s + %s = %s\\text{ km}$. Vì $%s < AB = %s < %s$ nên biên giới vùng phủ sóng của hai trạm là hai đường tròn cắt nhau.""" % (fmt(ra), fmt(rb), fmt(round(ra - rb, 1)), fmt(ra), fmt(rb), fmt(round(ra + rb, 1)), fmt(round(ra - rb, 1)), fmt(ab), fmt(round(ra + rb, 1))))

    # Thông hiểu
    th_da_1_d = '\\True Tồn tại đúng hai vị trí trên mặt đất nằm đồng thời trên ranh giới ngoài cùng của cả hai trạm'
    th_da_1_s = 'Chỉ có duy nhất một vị trí trên mặt đất nằm đồng thời trên ranh giới ngoài cùng của cả hai trạm'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì hai đường tròn biên giới vùng phủ sóng cắt nhau nên chúng có đúng $2$ giao điểm. Đó chính là hai vị trí nằm đồng thời trên ranh giới ngoài cùng của cả hai trạm.""")

    # Vận dụng
    vd_da_1_d = '\\True Một người đứng trên đoạn thẳng nối $A$ và $B$, cách $A$ một khoảng $%s\\text{ km}$ sẽ nhận được sóng của cả hai trạm' % (fmt(kc_nguoi))
    vd_da_1_s = 'Một người đứng trên đoạn thẳng nối $A$ và $B$, cách $A$ một khoảng $%s\\text{ km}$ sẽ chỉ nhận được sóng của trạm $A$' % (fmt(kc_nguoi))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Khoảng cách từ người đó đến trạm $A$ là $%s\\text{ km} < R_A = %s\\text{ km}$ và đến trạm $B$ là $%s - %s = %s\\text{ km} < R_B = %s\\text{ km}$. Do đó người này nằm trong vùng phủ sóng của cả hai trạm.""" % (fmt(kc_nguoi), fmt(ra), fmt(ab), fmt(kc_nguoi), fmt(kc_den_b), fmt(rb)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu nâng cấp trạm $B$ để bán kính phủ sóng tăng lên $%s\\text{ km}$ thì vùng phủ sóng của trạm $B$ sẽ bao trùm hoàn toàn vùng phủ sóng của trạm $A$' % (fmt(rb_moi))
    vdc_da_1_s = 'Nếu nâng cấp trạm $B$ để bán kính phủ sóng tăng lên $%s\\text{ km}$ thì hai vùng phủ sóng vẫn chỉ giao nhau một phần' % (fmt(rb_moi))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Khi bán kính mới của trạm $B$ là $R'_B = %s\\text{ km}$, ta có $R'_B - R_A = %s - %s = %s\\text{ km} > AB = %s\\text{ km}$. Đường tròn $(B; R'_B)$ đựng đường tròn $(A; R_A)$ nên vùng phủ sóng trạm $B$ bao trùm hoàn toàn vùng phủ sóng trạm $A$.""" % (fmt(rb_moi), fmt(rb_moi), fmt(ra), fmt(round(rb_moi - ra, 1)), fmt(ab)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
