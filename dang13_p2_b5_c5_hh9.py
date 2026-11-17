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


def bt_dang13_p2_b5_c5_hh9(self):
    def fmt(val):
        if isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val).replace('.', ',')

    rm = random.randint(5, 8)
    rn = random.randint(3, rm - 1)
    mn = rm + rn
    dich = 1.5
    mn_moi = mn - dich

    noidungcauhoi = ("""Trên một mảnh vườn phẳng, người ta lắp đặt hai vòi phun nước xoay tròn tự động tại hai điểm $M$ và $N$ cách nhau $%s\\text{ m}$. Vòi $M$ phun nước đều trong phạm vi hình tròn bán kính $%s\\text{ m}$, vòi $N$ phun nước đều trong phạm vi hình tròn bán kính $%s\\text{ m}$.""" % (fmt(mn), fmt(rm), fmt(rn)))

    # Nhận biết
    nb_da_1_d = '\\True Hai vùng được tưới nước chỉ chạm nhau tại duy nhất một điểm trên đoạn thẳng $MN$'
    nb_da_1_s = 'Hai vùng được tưới nước cắt nhau tạo thành một vùng giao nhau rộng lớn'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Ta có $R_M + R_N = %s + %s = %s\\text{ m} = MN$. Hai đường tròn biên giới tiếp xúc ngoài với nhau nên hai vùng tưới chỉ chạm nhau tại duy nhất một tiếp điểm trên đoạn $MN$.""" % (fmt(rm), fmt(rn), fmt(mn)))

    # Thông hiểu
    th_da_1_d = '\\True Không có khu vực diện tích nào trên vườn bị tưới chồng lấn nước từ cả hai vòi'
    th_da_1_s = 'Có một phần diện tích hình trăng khuyết bị tưới chồng lấn nước từ cả hai vòi'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì hai hình tròn chỉ tiếp xúc ngoài tại $1$ điểm duy nhất nên phần bên trong của hai hình tròn không giao nhau, do đó không có khu vực diện tích nào bị tưới chồng lấn.""")

    # Vận dụng
    vd_da_1_d = '\\True Nếu dịch chuyển vòi $N$ lại gần vòi $M$ thêm $%s\\text{ m}$ (giữ nguyên bán kính phun) thì hai đường tròn biên giới của vùng tưới sẽ cắt nhau' % (fmt(dich))
    vd_da_1_s = 'Nếu dịch chuyển vòi $N$ lại gần vòi $M$ thêm $%s\\text{ m}$ (giữ nguyên bán kính phun) thì vùng tưới vòi $M$ đựng vùng tưới vòi $N$' % (fmt(dich))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Khoảng cách mới là $MN' = %s - %s = %s\\text{ m}$. Ta có $R_M - R_N = %s\\text{ m} < %s\\text{ m} < R_M + R_N = %s\\text{ m}$ nên hai đường tròn biên giới cắt nhau.""" % (fmt(mn), fmt(dich), fmt(mn_moi), fmt(rm - rn), fmt(mn_moi), fmt(mn)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu giữ nguyên vị trí $M, N$ ($MN = %s\\text{ m}$) và muốn có vùng tưới giao nhau để cây ở giữa nhận đủ nước thì tổng bán kính phun của hai vòi phải lớn hơn $%s\\text{ m}$' % (fmt(mn), fmt(mn))
    vdc_da_1_s = 'Nếu giữ nguyên vị trí $M, N$ ($MN = %s\\text{ m}$) và muốn có vùng tưới giao nhau thì tổng bán kính phun của hai vòi phải nhỏ hơn $%s\\text{ m}$' % (fmt(mn), fmt(mn))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Để hai hình tròn có vùng giao nhau (hai đường tròn cắt nhau), điều kiện cần thiết là $R'_M + R'_N > MN = %s\\text{ m}$ (đồng thời $|R'_M - R'_N| < %s\\text{ m}$).""" % (fmt(mn), fmt(mn)))

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
