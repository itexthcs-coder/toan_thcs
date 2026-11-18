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


def bt_dang15_p2_b1_c8_ds9(self):
    ans = 16
    noidungcauhoi = ("""Một tấm bìa hình vuông được chia làm $4$ ô vuông bằng nhau ghi các số $1; 2; 3; 4$. Một bạn tung một đồng xu nhỏ rơi ngẫu nhiên vào một trong $4$ ô vuông đó hai lần liên tiếp và quan sát số ghi trên ô vuông đồng xu rơi vào ở mỗi lần.""" % ())
    # Ý 1
    st_1_d = '\\True ' + ('Không gian mẫu của phép thử có $16$ phần tử')
    st_1_s = ('Không gian mẫu của phép thử có $12$ phần tử')
    sol_1_d = ('Đúng. Lần $1$ đồng xu có thể rơi vào $1$ trong $4$ ô, lần $2$ cũng có thể rơi vào $1$ trong $4$ ô nên có $4 \\cdot 4 = 16$ phần tử.')
    sol_1_s = ('Sai. Lần tung thứ hai đồng xu vẫn có thể rơi lại vào ô của lần thứ nhất nên có $4 \\cdot 4 = 16$ phần tử.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Số kết quả mà tổng hai số ghi trên hai ô vuông đồng xu rơi vào bằng $5$ là $4$')
    st_2_s = ('Số kết quả mà tổng hai số ghi trên hai ô vuông đồng xu rơi vào bằng $5$ là $2$')
    sol_2_d = ('Đúng. Các cặp $(a, b)$ có $a + b = 5$ là $(1, 4); (4, 1); (2, 3); (3, 2)$, gồm $4$ kết quả.')
    sol_2_s = ('Sai. Vì tung hai lần liên tiếp nên có $4$ kết quả: $(1, 4); (4, 1); (2, 3); (3, 2)$.')
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Số kết quả mà tích hai số ghi trên hai ô vuông là một số lẻ bằng $4$')
    st_3_s = ('Số kết quả mà tích hai số ghi trên hai ô vuông là một số lẻ bằng $8$')
    sol_3_d = ('Đúng. Tích hai số là số lẻ khi cả hai lần đều rơi vào ô số lẻ ($1$ hoặc $3$), do đó có $2 \\cdot 2 = 4$ kết quả: $(1, 1); (1, 3); (3, 1); (3, 3)$.')
    sol_3_s = ('Sai. Cả hai lần phải rơi vào ô $1$ hoặc $3$ nên chỉ có $2 \\cdot 2 = 4$ kết quả.')
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Số kết quả mà hai lần đồng xu rơi vào hai ô có số hiệu hơn kém nhau $1$ đơn vị là $6$')
    st_4_s = ('Số kết quả mà hai lần đồng xu rơi vào hai ô có số hiệu hơn kém nhau $1$ đơn vị là $3$')
    sol_4_d = ('Đúng. Các cặp có $|a - b| = 1$ là $(1, 2); (2, 1); (2, 3); (3, 2); (3, 4); (4, 3)$, gồm $6$ kết quả.')
    sol_4_s = ('Sai. Có $6$ kết quả thỏa mãn điều kiện trên.')
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
