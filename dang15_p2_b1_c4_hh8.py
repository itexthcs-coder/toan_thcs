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


def bt_dang15_p2_b1_c4_hh8(self):
    n = random.choice([3, 4])
    s_abc = (n ** 2) * random.choice([2, 3, 4])
    s_abn = s_abc // n
    s_amn = s_abc // (n ** 2)
    s_bmnc = s_abc - s_amn
    ts_an_ac = Rational(1, n)

    noidungcauhoi = ("""Cho $\\Delta ABC$ có diện tích bằng $%s\\text{ cm}^2$. Trên cạnh $AB$ lấy điểm $M$ sao cho $\\dfrac{AM}{AB} = \\dfrac{1}{%s}$, qua $M$ kẻ đường thẳng song song với $BC$ cắt $AC$ tại $N$. Nối $B$ với $N$ (như hình vẽ bên dưới). Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (M) at ($(A)!0.3333!(B)$);
\\coordinate (N) at ($(A)!0.3333!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);
\\draw[line width=1pt, dashed] (B)--(N);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                     % (s_abc, n))

    nb_da_1_d = '\\True $\\dfrac{AN}{AC} = %s$' % (latex(ts_an_ac))
    nb_da_1_s = '$\\dfrac{AN}{AC} = %s$' % (latex(Rational(n - 1, n)))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Xét $\\Delta ABC$ có $MN // BC$, theo định lí Thalès trong tam giác ta có $\\dfrac{AN}{AC} = \\dfrac{AM}{AB} = %s$."""
                    % (latex(ts_an_ac)))

    th_da_1_d = '\\True Diện tích $\\Delta ABN$ bằng $%s\\text{ cm}^2$' % (s_abn)
    th_da_1_s = 'Diện tích $\\Delta ABN$ bằng $%s\\text{ cm}^2$' % (s_amn)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Hai tam giác $ABN$ và $ABC$ có chung đường cao hạ từ đỉnh $B$ xuống cạnh $AC$, nên $\\dfrac{S_{\\Delta ABN}}{S_{\\Delta ABC}} = \\dfrac{AN}{AC} = %s \\Rightarrow S_{\\Delta ABN} = %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$."""
                    % (latex(ts_an_ac), latex(ts_an_ac), s_abc, s_abn))

    vd_da_1_d = '\\True Diện tích $\\Delta AMN$ bằng $%s\\text{ cm}^2$' % (s_amn)
    vd_da_1_s = 'Diện tích $\\Delta AMN$ bằng $%s\\text{ cm}^2$' % (s_abn // 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Hai tam giác $AMN$ và $ABN$ có chung đường cao hạ từ đỉnh $N$ xuống cạnh $AB$, nên $\\dfrac{S_{\\Delta AMN}}{S_{\\Delta ABN}} = \\dfrac{AM}{AB} = %s \\Rightarrow S_{\\Delta AMN} = %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$."""
                    % (latex(ts_an_ac), latex(ts_an_ac), s_abn, s_amn))

    vdc_da_1_d = '\\True Diện tích tứ giác $BMNC$ bằng $%s\\text{ cm}^2$' % (s_bmnc)
    vdc_da_1_s = 'Diện tích tứ giác $BMNC$ bằng $%s\\text{ cm}^2$' % (s_abc - s_abn)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Diện tích tứ giác $BMNC$ là $S_{BMNC} = S_{\\Delta ABC} - S_{\\Delta AMN} = %s - %s = %s\\text{ (cm}^2\\text{)}$."""
                     % (s_abc, s_amn, s_bmnc))

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
