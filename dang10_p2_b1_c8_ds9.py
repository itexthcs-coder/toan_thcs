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


def bt_dang10_p2_b1_c8_ds9(self):
    n = random.randint(4, 6)
    ans = n * (n - 1) // 2
    noidungcauhoi = ("""Trong một giải đấu bóng đá mini giao hữu có $%s$ đội bóng tham gia thi đấu vòng tròn một lượt (hai đội bất kì gặp nhau đúng một trận). Ban tổ chức bốc thăm ngẫu nhiên một cặp đấu để đá trận khai mạc.""" % (n))
    # Ý 1
    st_1_d = '\\True ' + ('Trong phép thử bốc thăm một cặp đấu, trận đội $1$ gặp đội $2$ và trận đội $2$ gặp đội $1$ là cùng một kết quả')
    st_1_s = ('Trong phép thử bốc thăm một cặp đấu, trận đội $1$ gặp đội $2$ và trận đội $2$ gặp đội $1$ là hai kết quả khác nhau')
    sol_1_d = ('Đúng. Hai đội gặp nhau đúng một trận nên không phân biệt thứ tự đội nào viết trước, đội nào viết sau.')
    sol_1_s = ('Sai. Vì thi đấu vòng tròn một lượt nên cặp đấu giữa hai đội không phân biệt thứ tự.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Không gian mẫu của phép thử có $%s$ phần tử' % (ans))
    st_2_s = ('Không gian mẫu của phép thử có $%s$ phần tử' % (n * (n - 1)))
    sol_2_d = ('Đúng. Mỗi trận đấu là một tập hợp gồm $2$ đội khác nhau trong $%s$ đội nên có $\\dfrac{%s \\cdot %s}{2} = %s$ cặp đấu.' % (n, n, n - 1, ans))
    sol_2_s = ('Sai. Do không phân biệt thứ tự nên số cặp đấu là $\\dfrac{%s \\cdot %s}{2} = %s$.' % (n, n - 1, ans))
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Nếu lập bảng vuông $%s \\times %s$ thì các ô trên đường chéo chính và một nửa bảng đối xứng qua đường chéo chính bị loại bỏ' % (n, n))
    st_3_s = ('Nếu lập bảng vuông $%s \\times %s$ thì tất cả $%s$ ô trong bảng đều là phần tử của không gian mẫu' % (n, n, n * n))
    sol_3_d = ('Đúng. Ta loại bỏ $%s$ ô trùng tên đội và chia đôi $%s$ ô còn lại do tính đối xứng của cặp đấu.' % (n, n * (n - 1)))
    sol_3_s = ('Sai. Phải loại bỏ các ô trên đường chéo chính và một nửa bảng đối xứng do không phân biệt thứ tự.')
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Nếu có thêm $1$ đội bóng nữa tham gia thì không gian mẫu tăng thêm $%s$ cặp đấu' % (n))
    st_4_s = ('Nếu có thêm $1$ đội bóng nữa tham gia thì không gian mẫu tăng thêm $1$ cặp đấu')
    sol_4_d = ('Đúng. Đội bóng mới sẽ tạo ra thêm $%s$ cặp đấu mới với $%s$ đội bóng ban đầu.' % (n, n))
    sol_4_s = ('Sai. Đội bóng thứ $%s$ ghép cặp được với cả $%s$ đội trước đó nên tăng thêm $%s$ cặp đấu.' % (n + 1, n, n))
    pair_4 = [(st_4_d, sol_4_d), (st_4_s, sol_4_s)]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        c1 = random.choice(pair_1)
        c2 = random.choice(pair_2)
        c3 = random.choice(pair_3)
        c4 = random.choice(pair_4)
        answers = [c1[0], c2[0], c3[0], c4[0]]
        if 1 <= count_true_answers(answers) <= 3:
            break

    shuffled_answers_nb = [c1[0]]
    shuffled_solutions_nb = [c1[1]]
    shuffled_answers_th = [c2[0]]
    shuffled_solutions_th = [c2[1]]
    shuffled_answers_vd = [c3[0]]
    shuffled_solutions_vd = [c3[1]]
    shuffled_answers_vdc = [c4[0]]
    shuffled_solutions_vdc = [c4[1]]

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
