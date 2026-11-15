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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang5_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a, b = random.sample([3, 4, 5, 6, 7, 8, 9, 12], 2)
        ans_true = a * b

        noidungcauhoi = ('''Trong giờ học, bạn An biến đổi biểu thức $K = \\sqrt{(-%d)^2 \\cdot (-%d)^2}$ theo các bước sau:\\\\
\\textit{Bước 1:} $K = \\sqrt{(-%d)^2} \\cdot \\sqrt{(-%d)^2}$\\\\
\\textit{Bước 2:} $K = (-%d) \\cdot (-%d)$\\\\
\\textit{Bước 3:} $K = %d$.\\\\
Xét tính đúng sai của các nhận xét về bài làm của bạn An:''' % (a, b, a, b, a, b, ans_true))

        nb_da_1_d = '\\True Kết quả cuối cùng $K = %d$ của bạn An là đúng' % (ans_true)
        nb_da_1_s = 'Kết quả cuối cùng phải là $K = -%d$' % (ans_true)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $K = \\sqrt{(-%d)^2 \\cdot (-%d)^2} = \\sqrt{%d \\cdot %d} = %d \\cdot %d = %d$. Vậy kết quả cuối cùng của bạn An là đúng.''' % (a, b, a**2, b**2, a, b, ans_true))

        th_da_1_d = '\\True Phép biến đổi ở \\textit{Bước 1} là đúng vì $(- %d)^2 > 0$ và $(- %d)^2 > 0$' % (a, b)
        th_da_1_s = 'Phép biến đổi ở \\textit{Bước 1} là sai vì $-%d < 0$ và $-%d < 0$ nên không thể tách thành tích hai căn thức' % (a, b)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Vì $(- %d)^2 = %d > 0$ và $(- %d)^2 = %d > 0$ nên cả hai thừa số dưới dấu căn đều không âm, do đó \\textit{Bước 1} áp dụng quy tắc khai phương một tích là hoàn toàn đúng.''' % (a, a**2, b, b**2))

        vd_da_1_d = '\\True Ở \\textit{Bước 2}, bạn An đã mắc sai lầm vì $\\sqrt{(-%d)^2} = |-%d| = %d$ chứ không phải $-%d$' % (a, a, a, a)
        vd_da_1_s = 'Ở \\textit{Bước 2}, bạn An biến đổi hoàn toàn chính xác theo định nghĩa căn bậc hai'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Theo hằng đẳng thức $\\sqrt{A^2} = |A|$, căn bậc hai số học của một số không âm luôn không âm nên $\\sqrt{(-%d)^2} = |-%d| = %d$ và $\\sqrt{(-%d)^2} = |-%d| = %d$. Bạn An viết bằng số âm là sai bản chất.''' % (a, a, a, b, b, b))

        vdc_da_1_d = '\\True Nếu áp dụng cách viết sai của bạn An cho biểu thức $\\sqrt{(-%d)^2 \\cdot %d^2}$ thì sẽ dẫn đến kết quả sai là $-%d$' % (a, b, ans_true)
        vdc_da_1_s = 'Cách làm của bạn An vẫn cho kết quả đúng khi áp dụng cho biểu thức $\\sqrt{(-%d)^2 \\cdot %d^2}$' % (a, b)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Nếu viết $\\sqrt{(-%d)^2 \\cdot %d^2} = (-%d) \\cdot %d = -%d$ thì kết quả bị âm (sai), do hai dấu trừ không tự triệt tiêu như ở bài trên.''' % (a, b, a, b, ans_true))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

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
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
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
               '\\end{ex}\n \end{minipage} \n\n')
    return content
