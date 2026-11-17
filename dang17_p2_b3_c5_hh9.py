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








def bt_dang17_p2_b3_c5_hh9(self):
    r_gio, r_phut = random.choice([(9, 12), (6, 12), (12, 18)])
    phut = random.choice([15, 20, 30])
    goc_phut = phut * 6
    goc_gio = Rational(phut, 2)

    l_phut = Rational(goc_phut, 180) * r_phut * pi
    Sq_phut = Rational(goc_phut, 360) * (r_phut**2) * pi
    l_gio = Rational(goc_gio, 180) * r_gio * pi

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \draw[thick] (0,0) circle (1.8cm);
        \foreach \a in {0,30,...,330} \draw (\a:1.65cm) -- (\a:1.8cm);
        \draw[very thick] (0,0) -- (90:1.0cm);
        \draw[thick, red] (0,0) -- (-30:1.5cm);
        \fill (0,0) circle (2pt);
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Một chiếc đồng hồ treo tường có kim giờ dài $%d\text{ cm}$ và kim phút dài $%d\text{ cm}$. Xét chuyển động của hai kim này trong khoảng thời gian từ $12\text{ giờ } 00\text{ phút}$ đến $12\text{ giờ } %d\text{ phút}$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % (r_gio, r_phut, phut, hinh_ve))

    nb_da_1_d = '\\True Trong $%d\\text{ phút}$, đầu mút kim phút vạch nên một cung tròn có số đo bằng $%d^\\circ$' % (phut, goc_phut)
    nb_da_1_s = 'Trong $%d\\text{ phút}$, đầu mút kim phút vạch nên một cung tròn có số đo bằng $%d^\\circ$' % (phut, goc_phut // 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Trong $60\text{ phút}$, kim phút quay đủ $360^\circ$, nên trong $%d\text{ phút}$ kim phút quay được góc $\dfrac{%d}{60} \cdot 360^\circ = %d^\circ$.""" % (phut, phut, goc_phut))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Quãng đường đầu mút kim phút đi được trong $%d\\text{ phút}$ là $%s\\text{ cm}$' % (phut, latex(l_phut))
    th_da_1_s = 'Quãng đường đầu mút kim phút đi được trong $%d\\text{ phút}$ là $%s\\text{ cm}$' % (phut, latex(2 * l_phut))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Độ dài cung tròn đầu mút kim phút đi được là $l = \dfrac{%d}{180}\pi \cdot %d = %s\text{ (cm)}$.""" % (goc_phut, r_phut, latex(l_phut)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích hình quạt tròn mà kim phút quét được trong $%d\\text{ phút}$ bằng $%s\\text{ cm}^2$' % (phut, latex(Sq_phut))
    vd_da_1_s = 'Diện tích hình quạt tròn mà kim phút quét được trong $%d\\text{ phút}$ bằng $%s\\text{ cm}^2$' % (phut, latex(Sq_phut / 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Diện tích hình quạt tròn kim phút quét được là $S_q = \dfrac{%d}{360}\pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (goc_phut, r_phut, latex(Sq_phut)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Trong cùng khoảng thời gian $%d\\text{ phút}$ đó, đầu mút kim giờ vạch nên một cung tròn có độ dài bằng $%s\\text{ cm}$' % (phut, latex(l_gio))
    vdc_da_1_s = 'Trong cùng khoảng thời gian $%d\\text{ phút}$ đó, đầu mút kim giờ vạch nên một cung tròn có độ dài bằng $%s\\text{ cm}$' % (phut, latex(2 * l_gio))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Trong $60\text{ phút}$ kim giờ quay được $30^\circ$, nên trong $%d\text{ phút}$ kim giờ quay được góc $%s^\circ$. \\ Độ dài cung kim giờ vạch nên là $l_{\text{giờ}} = \dfrac{%s}{180}\pi \cdot %d = %s\text{ (cm)}$.""" % (phut, latex(goc_gio), latex(goc_gio), r_gio, latex(l_gio)))
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
