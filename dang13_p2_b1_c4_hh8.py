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


def bt_dang13_p2_b1_c4_hh8(self):
    m_ratio = random.choice([2, 3])
    # BM = m_ratio * MC => CM/MB = 1/m_ratio
    # N trung diem AM => P trung diem AK => AP = PK
    # CK/KP = CM/MB = 1/m_ratio => KP = m_ratio * CK => AP = m_ratio * CK
    # AC = AP + PK + KC = (2*m_ratio + 1) CK
    tong_phan = 2 * m_ratio + 1
    ts_ap_ac = Rational(m_ratio, tong_phan)
    ac_len = tong_phan * 3
    pc_len = (m_ratio + 1) * 3
    ap_len = m_ratio * 3

    noidungcauhoi = ("""Cho $\\Delta ABC$, trên cạnh $BC$ lấy điểm $M$ sao cho $BM = %s MC$. Gọi $N$ là trung điểm của đoạn thẳng $AM$. Tia $BN$ cắt cạnh $AC$ tại $P$. Qua $M$ kẻ đường thẳng song song với $BP$ cắt $AC$ tại $K$ (như hình vẽ bên dưới). Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (M) at ($(B)!0.6667!(C)$);
\\coordinate (N) at ($(A)!0.5!(M)$);
\\coordinate (P) at (intersection of B--N and A--C);
\\coordinate (K) at ($(P)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(M) (B)--(P);
\\draw[line width=1pt, dashed] (M)--(K);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[left] {$N$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (K) circle (1pt) node[right] {$K$};
\\end{tikzpicture}
\\end{center}"""
                     % (m_ratio))

    nb_da_1_d = '\\True $P$ là trung điểm của đoạn thẳng $AK$'
    nb_da_1_s = '$K$ là trung điểm của đoạn thẳng $PC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Xét $\\Delta AMK$ có $N$ là trung điểm của $AM$ và $NP // MK$, theo định lí Thalès ta có $\\dfrac{AP}{PK} = \\dfrac{AN}{NM} = 1 \\Rightarrow AP = PK$, hay $P$ là trung điểm của đoạn thẳng $AK$.""")

    th_da_1_d = '\\True $\\dfrac{CK}{KP} = \\dfrac{CM}{MB} = \\dfrac{1}{%s}$' % (m_ratio)
    th_da_1_s = '$\\dfrac{CK}{KP} = %s$' % (m_ratio)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Xét $\\Delta CBP$ có $MK // BP$, theo định lí Thalès trong tam giác ta có $\\dfrac{CK}{KP} = \\dfrac{CM}{MB} = \\dfrac{1}{%s}$."""
                    % (m_ratio))

    vd_da_1_d = '\\True Tỉ số $\\dfrac{AP}{AC}$ bằng $%s$' % (latex(ts_ap_ac))
    vd_da_1_s = 'Tỉ số $\\dfrac{AP}{AC}$ bằng $%s$' % (latex(Rational(1, m_ratio + 1)))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Từ $\\dfrac{CK}{KP} = \\dfrac{1}{%s}$ suy ra $KP = %s CK$, mà $AP = KP = %s CK$. \\\\ Do đó $AC = AP + PK + KC = %s CK + %s CK + CK = %s CK$, suy ra $\\dfrac{AP}{AC} = %s$."""
                    % (m_ratio, m_ratio, m_ratio, m_ratio, m_ratio, tong_phan, latex(ts_ap_ac)))

    vdc_da_1_d = '\\True Nếu $AC = %s\\text{ cm}$ thì độ dài đoạn thẳng $PC$ bằng $%s\\text{ cm}$' % (ac_len, pc_len)
    vdc_da_1_s = 'Nếu $AC = %s\\text{ cm}$ thì độ dài đoạn thẳng $PC$ bằng $%s\\text{ cm}$' % (ac_len, ap_len)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Khi $AC = %s\\text{ cm}$, ta có $AP = %s \\cdot %s = %s\\text{ (cm)}$, suy ra $PC = AC - AP = %s - %s = %s\\text{ (cm)}$."""
                     % (ac_len, latex(ts_ap_ac), ac_len, ap_len, ac_len, ap_len, pc_len))

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
