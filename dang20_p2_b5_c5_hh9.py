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


def bt_dang20_p2_b5_c5_hh9(self):
    def fmt(val):
        if isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val).replace('.', ',')

    R = random.choice([6, 8, 10])
    r = 2
    hieu_r = R - r
    oi = 2.5
    ik = r + r
    ok = R - r

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (1.25,0);
\\coordinate (K1) at (0.625,1.9);
\\coordinate (K2) at (0.625,-1.9);
\\draw[line width=1pt] (O) circle (3cm);
\\draw[line width=1pt] (I) circle (1cm);
\\draw[line width=1pt] (K1) circle (1cm);
\\draw[line width=1pt, dashed] (K2) circle (1cm);
\\draw[line width=1pt] (O)--(I)--(K1)--cycle;
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (I) circle (1pt) node[right] {$I$};
\\fill (K1) circle (1pt) node[above] {$K_1$};
\\fill (K2) circle (1pt) node[below] {$K_2$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Một nhà thiết kế vẽ logo trên phần mềm đồ họa gồm một hình tròn lớn $(O; %s\\text{ cm})$ và một hình tròn nhỏ $(I; %s\\text{ cm})$ sao cho hình tròn nhỏ nằm hoàn toàn bên trong hình tròn lớn (không chạm viền).
%s""" % (fmt(R), fmt(r), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Khoảng cách $OI$ giữa hai tâm bắt buộc phải nhỏ hơn $%s\\text{ cm}$' % (fmt(hieu_r))
    nb_da_1_s = 'Khoảng cách $OI$ giữa hai tâm bắt buộc phải lớn hơn $%s\\text{ cm}$' % (fmt(hieu_r))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Để hình tròn $(I; %s\\text{ cm})$ nằm hoàn toàn bên trong $(O; %s\\text{ cm})$ mà không chạm viền (tức đường tròn $(O)$ đựng đường tròn $(I)$), ta phải có $OI < R - r = %s - %s = %s\\text{ cm}$.""" % (fmt(r), fmt(R), fmt(R), fmt(r), fmt(hieu_r)))

    # Thông hiểu
    th_da_1_d = '\\True Nếu nhà thiết kế đặt $OI = %s\\text{ cm}$ thì hình tròn nhỏ sẽ chạm vào viền trong của hình tròn lớn tại một điểm' % (fmt(hieu_r))
    th_da_1_s = 'Nếu nhà thiết kế đặt $OI = %s\\text{ cm}$ thì hình tròn nhỏ sẽ cắt viền hình tròn lớn tại hai điểm' % (fmt(hieu_r))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Khi $OI = %s\\text{ cm} = R - r$, hai đường tròn $(O)$ và $(I)$ tiếp xúc trong với nhau nên có duy nhất một điểm chung trên viền.""" % (fmt(hieu_r)))

    # Vận dụng
    vd_da_1_d = '\\True Khi $OI = %s\\text{ cm}$, nếu vẽ thêm một đường tròn thứ ba $(K; %s\\text{ cm})$ tiếp xúc ngoài với $(I)$ và tiếp xúc trong với $(O)$ thì tâm $K$ luôn thỏa mãn $IK = %s\\text{ cm}$ và $OK = %s\\text{ cm}$' % (fmt(oi), fmt(r), fmt(ik), fmt(ok))
    vd_da_1_s = 'Khi $OI = %s\\text{ cm}$, nếu vẽ thêm một đường tròn thứ ba $(K; %s\\text{ cm})$ tiếp xúc ngoài với $(I)$ và tiếp xúc trong với $(O)$ thì tâm $K$ thỏa mãn $IK = %s\\text{ cm}$ và $OK = %s\\text{ cm}$' % (fmt(oi), fmt(r), fmt(r), fmt(R))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Vì $(K; %s\\text{ cm})$ tiếp xúc ngoài với $(I; %s\\text{ cm})$ nên $IK = %s + %s = %s\\text{ cm}$. Vì $(K; %s\\text{ cm})$ tiếp xúc trong với $(O; %s\\text{ cm})$ nên $OK = %s - %s = %s\\text{ cm}$.""" % (fmt(r), fmt(r), fmt(r), fmt(r), fmt(ik), fmt(r), fmt(R), fmt(R), fmt(r), fmt(ok)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Với điều kiện ở ý c), tồn tại đúng $2$ vị trí của điểm $K$ trên bản vẽ tạo ra hai hình tròn $(K_1), (K_2)$ đối xứng nhau qua đường thẳng $OI$'
    vdc_da_1_s = 'Với điều kiện ở ý c), chỉ tồn tại duy nhất $1$ vị trí của điểm $K$ nằm trên đường thẳng $OI$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Ta cần dựng tam giác $OIK$ biết ba cạnh $OI = %s\\text{ cm}$, $IK = %s\\text{ cm}$, $OK = %s\\text{ cm}$. Bộ ba độ dài này thỏa mãn bất đẳng thức tam giác ($%s + %s = %s > %s$) nên dựng được đúng $2$ điểm $K_1, K_2$ ở hai nửa mặt phẳng đối nhau bờ $OI$, đối xứng nhau qua đường thẳng $OI$.""" % (fmt(oi), fmt(ik), fmt(ok), fmt(ik), fmt(ok), fmt(ik + ok), fmt(oi)))

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
