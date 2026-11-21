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


def bt_dang20_p2_b3_c2_ds8(self):
    # Dạng 20 (Thực tế): Quy tắc tính nhẩm bình phương số tự nhiên có tận cùng bằng 5
    a_so = randint(4, 8)
    so_2cs = a_so * 10 + 5
    tich_2cs = a_so * (a_so + 1)
    kq_2cs = tich_2cs * 100 + 25

    a_3cs = random.choice([10, 11, 12])
    so_3cs = a_3cs * 10 + 5
    tich_3cs = a_3cs * (a_3cs + 1)
    kq_3cs = tich_3cs * 100 + 25

    noidungcauhoi = ('''Một số tự nhiên có hai chữ số và có chữ số hàng đơn vị bằng $5$ được viết dưới dạng $\\overline{a5} = 10a + 5$ (với $a \\in \\mathbb{N}, 1 \\le a \\le 9$). Xét tính đúng sai của các khẳng định sau:''')

    nb_da_1_d = '\\True Bình phương của số $\\overline{a5}$ được biểu diễn bởi biểu thức $(10a + 5)^2$'
    nb_da_1_s = 'Bình phương của số $\\overline{a5}$ được biểu diễn bởi biểu thức $10a^2 + 25$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $\\overline{a5} = 10a + 5$ nên bình phương của số đó là $(10a + 5)^2$.''')

    th_da_1_d = '\\True Khai triển và biến đổi biểu thức trên, ta được $(10a + 5)^2 = 100a(a + 1) + 25$'
    th_da_1_s = 'Khai triển và biến đổi biểu thức trên, ta được $(10a + 5)^2 = 100a^2 + 25$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $(10a + 5)^2 = 100a^2 + 100a + 25 = 100a(a + 1) + 25$.''')

    vd_da_1_d = '\\True Dựa vào công thức trên, để tính nhẩm $%s^2$, ta lấy $%s \\cdot %s = %s$ rồi viết thêm $25$ vào sau để được $%s$' % (so_2cs, a_so, a_so + 1, tich_2cs, kq_2cs)
    vd_da_1_s = 'Dựa vào công thức trên, để tính nhẩm $%s^2$, ta lấy $%s^2 = %s$ rồi viết thêm $25$ vào sau để được $%s25$' % (so_2cs, a_so, a_so**2, a_so**2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Với $a = %s$, ta có $%s^2 = 100 \\cdot %s \\cdot (%s + 1) + 25 = 100 \\cdot %s + 25 = %s$.''' % (a_so, so_2cs, a_so, a_so, tich_2cs, kq_2cs))

    vdc_da_1_d = '\\True Áp dụng quy tắc tương tự cho số $%s^2$, kết quả thu được là $%s$' % (so_3cs, kq_3cs)
    vdc_da_1_s = 'Áp dụng quy tắc tương tự cho số $%s^2$, kết quả thu được là $%s25$' % (so_3cs, a_3cs**2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Với $a = %s$, ta lấy $%s \\cdot %s = %s$, viết thêm $25$ vào sau ta được $%s^2 = %s$.''' % (a_3cs, a_3cs, a_3cs + 1, tich_3cs, so_3cs, kq_3cs))

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
