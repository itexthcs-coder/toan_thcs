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


def bt_dang11_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.randint(2, 4)
    R1 = 3 * k
    R2 = 2 * k
    kc = R1 + R2
    R3 = R2 - 2
    vong1 = 2
    vong2 = 3

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (0,0);
\\coordinate (O2) at (3.5,0);
\\coordinate (T) at (2.1,0);
\\draw[line width=1pt] (O1) circle (2.1cm);
\\draw[line width=1pt] (O2) circle (1.4cm);
\\draw[line width=1pt] (O1)--(O2);
\\fill (O1) circle (1pt) node[left] {$O_1$};
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (T) circle (1pt) node[above right] {$T$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Trong một hộp số cơ khí, hai bánh răng hình tròn $(O_1)$ và $(O_2)$ ăn khớp ngoài với nhau (mô hình hóa là hai đường tròn tiếp xúc ngoài). Bánh răng chủ động $(O_1)$ có bán kính $R_1 = %s\\text{ cm}$, bánh răng bị động $(O_2)$ có bán kính $R_2 = %s\\text{ cm}$.
%s""" % (fmt(R1), fmt(R2), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Khoảng cách giữa hai trục quay $O_1$ và $O_2$ bằng $%s\\text{ cm}$' % (fmt(kc))
    nb_da_1_s = 'Khoảng cách giữa hai trục quay $O_1$ và $O_2$ bằng $%s\\text{ cm}$' % (fmt(R1 - R2))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì hai bánh răng ăn khớp ngoài (hai đường tròn tiếp xúc ngoài) nên khoảng cách giữa hai trục quay là $O_1O_2 = R_1 + R_2 = %s + %s = %s\\text{ cm}$.""" % (fmt(R1), fmt(R2), fmt(kc)))

    # Thông hiểu
    th_da_1_d = '\\True Điểm ăn khớp $T$ (tiếp điểm) của hai bánh răng luôn nằm trên đoạn thẳng nối hai trục $O_1O_2$'
    th_da_1_s = 'Điểm ăn khớp $T$ của hai bánh răng nằm ngoài đường thẳng nối hai trục $O_1O_2$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Theo tính chất của hai đường tròn tiếp xúc ngoài, tiếp điểm $T$ luôn thẳng hàng và nằm giữa hai tâm $O_1, O_2$.""")

    # Vận dụng
    vd_da_1_d = '\\True Nếu thay bánh răng $(O_2)$ bằng bánh răng $(O_3)$ có bán kính $%s\\text{ cm}$ mà giữ nguyên khoảng cách hai trục là $%s\\text{ cm}$ thì hai bánh răng mới ở ngoài nhau' % (fmt(R3), fmt(kc))
    vd_da_1_s = 'Nếu thay bánh răng $(O_2)$ bằng bánh răng $(O_3)$ có bán kính $%s\\text{ cm}$ mà giữ nguyên khoảng cách hai trục là $%s\\text{ cm}$ thì hai bánh răng mới cắt nhau' % (fmt(R3), fmt(kc))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Tổng hai bán kính mới là $R_1 + R_3 = %s + %s = %s\\text{ cm} < O_1O_2 = %s\\text{ cm}$. Vì $O_1O_2 > R_1 + R_3$ nên hai đường tròn ở ngoài nhau (hai bánh răng không chạm tới nhau).""" % (fmt(R1), fmt(R3), fmt(R1 + R3), fmt(kc)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Khi bánh răng $(O_1)$ quay được $%s$ vòng thì bánh răng $(O_2)$ quay được $%s$ vòng' % (fmt(vong1), fmt(vong2))
    vdc_da_1_s = 'Khi bánh răng $(O_1)$ quay được $%s$ vòng thì bánh răng $(O_2)$ quay được $%s$ vòng' % (fmt(vong2), fmt(vong1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Khi ăn khớp không trượt, quãng đường di chuyển trên vành của hai bánh răng bằng nhau: $n_1 \\cdot 2\\pi R_1 = n_2 \\cdot 2\\pi R_2 \\Rightarrow n_2 = n_1 \\cdot \\frac{R_1}{R_2} = %s \\cdot \\frac{%s}{%s} = %s$ vòng.""" % (fmt(vong1), fmt(R1), fmt(R2), fmt(vong2)))

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
