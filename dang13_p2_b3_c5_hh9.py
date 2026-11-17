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
from PyQt5.QtGui import QTextCursor, QFont
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








def bt_dang13_p2_b3_c5_hh9(self):
    R_bia = random.choice([20, 25])
    r1, r2, r3 = 5, 10, 15
    S_bia = (R_bia**2) * pi
    S_vong8 = (r3**2 - r2**2) * pi
    xs_8 = Rational(r3**2 - r2**2, R_bia**2)
    xs_9_10 = Rational(r2**2, R_bia**2)

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \fill[blue!20] (0,0) circle (2cm);
        \fill[white] (0,0) circle (1.5cm);
        \fill[yellow!30] (0,0) circle (1.0cm);
        \fill[red!30] (0,0) circle (0.5cm);
        \draw[thick] (0,0) circle (2cm);
        \draw[thick] (0,0) circle (1.5cm);
        \draw[thick] (0,0) circle (1.0cm);
        \draw[thick] (0,0) circle (0.5cm);
        \node at (0,0) {\tiny 10};
        \node at (0,0.75cm) {\tiny 9};
        \node at (0,1.25cm) {\tiny 8};
        \node at (0,1.75cm) {\tiny 7};
    \end{tikzpicture}
    \end{center}"""())

    noidungcauhoi = (r"""Một tấm bia tròn dùng để luyện tập ném phi tiêu được tạo bởi bốn đường tròn đồng tâm lần lượt có bán kính là $5\text{ cm}, 10\text{ cm}, 15\text{ cm}$ và $%d\text{ cm}$ (như hình vẽ). Vòng tính điểm $10$ là hình tròn trong cùng, vòng $9$ nằm giữa đường tròn thứ nhất và thứ hai, vòng $8$ nằm giữa đường tròn thứ hai và thứ ba, vòng $7$ nằm ngoài cùng. Giả sử người chơi ném phi tiêu ngẫu nhiên và luôn trúng bia. Xét tính đúng sai của các khẳng định sau:
    %s""" % (R_bia, hinh_ve))

    nb_da_1_d = '\\True Diện tích toàn bộ tấm bia là $%s\\text{ cm}^2$' % latex(S_bia)
    nb_da_1_s = 'Diện tích toàn bộ tấm bia là $%s\\text{ cm}^2$' % latex(2 * R_bia * pi)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Diện tích toàn bộ tấm bia hình tròn bán kính %d\text{ cm} là $S = \pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (R_bia, R_bia, latex(S_bia)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích của vòng điểm $8$ bằng $%s\\text{ cm}^2$' % latex(S_vong8)
    th_da_1_s = 'Diện tích của vòng điểm $8$ bằng $%s\\text{ cm}^2$' % latex(25 * pi)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Vòng $8$ là hình vành khuyên giữa hai đường tròn bán kính $15\text{ cm}$ và $10\text{ cm}$ nên có diện tích $S_8 = \pi(15^2 - 10^2) = 125\pi\text{ (cm}^2\text{)}$.""" )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Xác suất để người chơi ném trúng vòng điểm $8$ bằng $%s$' % latex(xs_8)
    vd_da_1_s = 'Xác suất để người chơi ném trúng vòng điểm $8$ bằng $%s$' % latex(xs_8 * 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Xác suất ném trúng vòng $8$ là $P(A) = \dfrac{S_8}{S} = \dfrac{125\pi}{%s} = %s$.""" % (latex(S_bia), latex(xs_8)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xác suất để người chơi ném trúng vùng có điểm từ $9$ trở lên (vòng $9$ hoặc vòng $10$) bằng $%s$' % latex(xs_9_10)
    vdc_da_1_s = 'Xác suất để người chơi ném trúng vùng có điểm từ $9$ trở lên (vòng $9$ hoặc vòng $10$) bằng $%s$' % latex(Rational(75, R_bia**2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Vùng điểm từ $9$ trở lên là hình tròn bán kính $10\text{ cm}$, có diện tích $100\pi\text{ cm}^2$. \\ Xác suất cần tìm là $P(B) = \dfrac{100\pi}{%s} = %s$.""" % (latex(S_bia), latex(xs_9_10)))
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
