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

def bt_dang17_p2_b1_c2_ds8(self):
    # Khai báo biến
    a0 = randint(30, 45)
    b0 = randint(10, 20)
    dt_con_lai = a0**2 - b0**2

    dai_hcn = randint(36, 48)
    rong_hcn = randint(10, 18)
    while (dai_hcn + rong_hcn) % 2 != 0:
        rong_hcn = randint(10, 18)
    a_tim_duoc = (dai_hcn + rong_hcn) // 2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Từ một tấm bìa hình vuông có cạnh dài $a\\text{ (cm)}$, bác thợ thủ công cắt bỏ đi một hình vuông nhỏ ở góc có cạnh dài $b\\text{ (cm)}$ ($a > b > 0$). Phần bìa còn lại được cắt ghép thành một hình chữ nhật. Xét tính đúng sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Diện tích phần bìa còn lại sau khi cắt là $a^2 - b^2\\text{ (cm}^2)$.'
    nb_da_1_s = 'Diện tích phần bìa còn lại sau khi cắt là $(a - b)^2\\text{ (cm}^2)$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ('''Diện tích tấm bìa ban đầu là $a^2\\text{ (cm}^2)$, phần cắt bỏ có diện tích là $b^2\\text{ (cm}^2)$ nên diện tích phần bìa còn lại là $a^2 - b^2\\text{ (cm}^2)$.''')
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Nếu hình chữ nhật ghép được có một cạnh bằng $a - b\\text{ (cm)}$ thì cạnh còn lại của nó dài $a + b\\text{ (cm)}$.'
    th_da_1_s = 'Nếu hình chữ nhật ghép được có một cạnh bằng $a - b\\text{ (cm)}$ thì cạnh còn lại của nó dài $a - b\\text{ (cm)}$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ('''Vì diện tích không đổi khi cắt ghép nên diện tích hình chữ nhật bằng $a^2 - b^2 = (a - b)(a + b)$. Do một cạnh bằng $a - b$ nên cạnh còn lại dài $a + b\\text{ (cm)}$.''')
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Khi $a = %s\\text{ cm}$ và $b = %s\\text{ cm}$, diện tích phần bìa còn lại là $%s\\text{ cm}^2$.' % (latex(a0), latex(b0), latex(dt_con_lai))
    vd_da_1_s = 'Khi $a = %s\\text{ cm}$ và $b = %s\\text{ cm}$, diện tích phần bìa còn lại là $%s\\text{ cm}^2$.' % (latex(a0), latex(b0), latex((a0 - b0)**2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ('''Thay $a = %s, b = %s$: $a^2 - b^2 = (%s - %s)(%s + %s) = %s \\cdot %s = %s\\text{ cm}^2$.'''
                    % (latex(a0), latex(b0), latex(a0), latex(b0), latex(a0), latex(b0), latex(a0 - b0), latex(a0 + b0), latex(dt_con_lai)))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu chiều dài và chiều rộng của hình chữ nhật ghép được lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$ thì cạnh tấm bìa ban đầu là $a = %s\\text{ cm}$.' % (latex(dai_hcn), latex(rong_hcn), latex(a_tim_duoc))
    vdc_da_1_s = 'Nếu chiều dài và chiều rộng của hình chữ nhật ghép được lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$ thì cạnh tấm bìa ban đầu là $a = %s\\text{ cm}$.' % (latex(dai_hcn), latex(rong_hcn), latex(dai_hcn - rong_hcn))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ('''Ta có $a + b = %s$ và $a - b = %s$. Cộng vế theo vế suy ra $2a = %s \\Rightarrow a = %s\\text{ cm}$.'''
                     % (latex(dai_hcn), latex(rong_hcn), latex(dai_hcn + rong_hcn), latex(a_tim_duoc)))
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
