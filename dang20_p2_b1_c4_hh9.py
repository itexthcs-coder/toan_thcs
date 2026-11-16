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


def bt_dang20_p2_b1_c4_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = symbols('R', positive=True)
        he_so = random.choice([1, 2, 3])
        ban_kinh = he_so * R
        duong_kinh = 2 * ban_kinh
        BC_expr = ban_kinh
        BH_expr = Rational(1, 2) * ban_kinh
        AH_expr = Rational(3, 2) * ban_kinh
        CH_expr = Rational(1, 2) * ban_kinh * sqrt(3)
        S_ACH = Rational(1, 2) * AH_expr * CH_expr

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (A) at (-2.4,0);\n"
            "\\coordinate (B) at (2.4,0);\n"
            "\\coordinate (C) at (1.2,2.08);\n"
            "\\coordinate (H) at (1.2,0);\n"
            "\\draw[line width=1pt] (2.4,0) arc (0:180:2.4);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n"
            "\\draw[line width=1pt] (C)--(H);\n"
            "\\draw[line width=1pt] (1.2,0.22)--(1.42,0.22)--(1.42,0);\n"
            "\\fill (O) circle (1pt) node[below] {$O$};\n"
            "\\fill (A) circle (1pt) node[below left] {$A$};\n"
            "\\fill (B) circle (1pt) node[below right] {$B$};\n"
            "\\fill (C) circle (1pt) node[above right] {$C$};\n"
            "\\fill (H) circle (1pt) node[below] {$H$};\n"
            "\\node at (-1.55,0.22) {$30^\\circ$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            "Cho nửa đường tròn tâm $O$ đường kính $AB = %s$ ($R > 0$). Lấy điểm $C$ trên nửa đường tròn sao cho $\\widehat{CAB} = 30^\\circ$. Kẻ $CH \\perp AB$ tại $H$.\n%s"
            % (latex(duong_kinh), hinh_ve)
        )

        nb_da_1_d = "\\True Tam giác $ABC$ vuông tại $C$"
        nb_da_1_s = "Tam giác $ABC$ vuông tại $B$"
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            "Vì điểm $C$ nằm trên nửa đường tròn đường kính $AB$ nên $\\widehat{ACB} = 90^\\circ$, hay tam giác $ABC$ vuông tại $C$."
        )
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = "\\True Độ dài dây cung $BC$ bằng $%s$" % (latex(BC_expr))
        th_da_1_s = "Độ dài dây cung $BC$ bằng $%s$" % (latex(ban_kinh * sqrt(3)))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            "Xét tam giác $ABC$ vuông tại $C$, ta có $BC = AB \\cdot \\sin \\widehat{CAB} = %s \\cdot \\sin 30^\\circ = %s \\cdot \\dfrac{1}{2} = %s$."
            % (latex(duong_kinh), latex(duong_kinh), latex(BC_expr))
        )
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = "\\True Độ dài đoạn thẳng $BH$ bằng $%s$" % (latex(BH_expr))
        vd_da_1_s = "Độ dài đoạn thẳng $BH$ bằng $%s$" % (latex(CH_expr))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            "Trong tam giác $ABC$ vuông tại $C$, ta có $\\widehat{CBA} = 90^\\circ - 30^\\circ = 60^\\circ$. \\\\ "
            "Xét tam giác $BHC$ vuông tại $H$, ta có $BH = BC \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s$."
            % (latex(BC_expr), latex(BH_expr))
        )
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = "\\True Diện tích tam giác $ACH$ bằng $%s$" % (latex(S_ACH))
        vdc_da_1_s = "Diện tích tam giác $ACH$ bằng $%s$" % (latex(2 * S_ACH))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            "Ta có $AH = AB - BH = %s - %s = %s$. \\\\ "
            "Trong tam giác $BHC$ vuông tại $H$, ta có $CH = BC \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s$. \\\\ "
            "Vậy diện tích tam giác $ACH$ vuông tại $H$ là $S_{ACH} = \\dfrac{1}{2} \\cdot AH \\cdot CH = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s$."
            % (latex(duong_kinh), latex(BH_expr), latex(AH_expr), latex(BC_expr), latex(CH_expr), latex(AH_expr), latex(CH_expr), latex(S_ACH))
        )
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

    content = (
        '\\begin{minipage}{\\textwidth} \n'
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
        '\\end{ex}\n \\end{minipage}\n\n'
    )
    return content
