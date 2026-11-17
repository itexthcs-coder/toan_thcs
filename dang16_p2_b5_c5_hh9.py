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


def bt_dang16_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    r_dao = random.randint(10, 14)
    R_vong = r_dao + random.randint(10, 14)
    r_bon = random.randint(3, 5)
    kc_ngan = random.randint(2, 4)
    oi = R_vong + r_bon + kc_ngan
    r_bon_moi = r_bon + kc_ngan

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (3.2,0);
\\draw[line width=1pt] (O) circle (1.2cm);
\\draw[line width=1pt] (O) circle (2.4cm);
\\draw[line width=1pt] (I) circle (0.5cm);
\\draw[line width=1pt, dashed] (O)--(I);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (I) circle (1pt) node[right] {$I$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Một vòng xuyến giao thông được thiết kế gồm đảo trung tâm hình tròn tâm $O$ bán kính $r = %s\\text{ m}$ và mép ngoài mặt đường bao quanh cũng là đường tròn đồng tâm $O$ bán kính $R = %s\\text{ m}$. Gần đó có một bồn hoa trang trí hình tròn tâm $I$ bán kính $r' = %s\\text{ m}$, biết tâm $I$ cách tâm $O$ một khoảng $OI = %s\\text{ m}$.
%s""" % (fmt(r_dao), fmt(R_vong), fmt(r_bon), fmt(oi), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Đảo trung tâm và mép ngoài vòng xuyến là hai đường tròn không giao nhau và có khoảng cách giữa hai tâm bằng $0$'
    nb_da_1_s = 'Đảo trung tâm và mép ngoài vòng xuyến là hai đường tròn tiếp xúc trong với nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Đảo trung tâm $(O; %s\\text{ m})$ và mép ngoài $(O; %s\\text{ m})$ có cùng tâm $O$ và bán kính khác nhau nên là hai đường tròn đồng tâm (không giao nhau), khoảng cách hai tâm bằng $0$.""" % (fmt(r_dao), fmt(R_vong)))

    # Thông hiểu
    th_da_1_d = '\\True Bồn hoa tâm $I$ và mép ngoài vòng xuyến là hai đường tròn nằm ngoài nhau'
    th_da_1_s = 'Bồn hoa tâm $I$ và mép ngoài vòng xuyến là hai đường tròn tiếp xúc ngoài'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Ta có $R + r' = %s + %s = %s\\text{ m}$. Vì $OI = %s\\text{ m} > %s\\text{ m}$ nên bồn hoa $(I)$ và mép ngoài $(O)$ là hai đường tròn nằm ngoài nhau.""" % (fmt(R_vong), fmt(r_bon), fmt(R_vong + r_bon), fmt(oi), fmt(R_vong + r_bon)))

    # Vận dụng
    vd_da_1_d = '\\True Khoảng cách ngắn nhất từ mép bồn hoa đến mép ngoài vòng xuyến bằng $%s\\text{ m}$' % (fmt(kc_ngan))
    vd_da_1_s = 'Khoảng cách ngắn nhất từ mép bồn hoa đến mép ngoài vòng xuyến bằng $%s\\text{ m}$' % (fmt(oi - R_vong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Khoảng cách ngắn nhất từ mép bồn hoa đến mép ngoài vòng xuyến đo dọc theo đoạn nối tâm $OI$ và bằng $OI - (R + r') = %s - %s = %s\\text{ m}$.""" % (fmt(oi), fmt(R_vong + r_bon), fmt(kc_ngan)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu mở rộng bán kính bồn hoa lên $%s\\text{ m}$ (giữ nguyên tâm $I$) thì bồn hoa sẽ chạm vào mép ngoài của vòng xuyến tại đúng $1$ điểm' % (fmt(r_bon_moi))
    vdc_da_1_s = 'Nếu mở rộng bán kính bồn hoa lên $%s\\text{ m}$ (giữ nguyên tâm $I$) thì bồn hoa sẽ lấn vào phần mặt đường vòng xuyến' % (fmt(r_bon_moi))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Khi bán kính mới của bồn hoa là $r'' = %s\\text{ m}$, ta có $R + r'' = %s + %s = %s\\text{ m} = OI$. Hai đường tròn tiếp xúc ngoài nên bồn hoa chạm vào mép ngoài vòng xuyến tại đúng $1$ điểm.""" % (fmt(r_bon_moi), fmt(R_vong), fmt(r_bon_moi), fmt(oi)))

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
