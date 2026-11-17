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








def bt_dang11_p2_b3_c5_hh9(self):
    p_xedap, p_dibo, p_duadon = random.choice([(35, 45, 20), (30, 50, 20), (25, 50, 25)])
    R_val = random.choice([4, 5, 6])

    goc_xedap = int(p_xedap * 360 / 100)
    goc_dibo = int(p_dibo * 360 / 100)
    goc_duadon = int(p_duadon * 360 / 100)

    Sq_duadon = Rational(goc_duadon, 360) * (R_val**2) * pi
    l_xedap = Rational(goc_xedap, 180) * R_val * pi

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \fill[cyan!25] (0,0) -- (0:1.8cm) arc (0:%d:1.8cm) -- cycle;
        \fill[orange!25] (0,0) -- (%d:1.8cm) arc (%d:%d:1.8cm) -- cycle;
        \fill[green!25] (0,0) -- (%d:1.8cm) arc (%d:360:1.8cm) -- cycle;
        \draw[thick] (0,0) circle (1.8cm);
        \draw (0,0) -- (0:1.8cm);
        \draw (0,0) -- (%d:1.8cm);
        \draw (0,0) -- (%d:1.8cm);
        \node at (%d:1.1cm) {\scriptsize $%d\%%$};
        \node at (%d:1.1cm) {\scriptsize $%d\%%$};
        \node at (%d:1.1cm) {\scriptsize $%d\%%$};
    \end{tikzpicture}
    \end{center}""" % (goc_xedap, goc_xedap, goc_xedap, goc_xedap+goc_dibo, goc_xedap+goc_dibo, goc_xedap+goc_dibo, goc_xedap, goc_xedap+goc_dibo, goc_xedap//2, p_xedap, goc_xedap + goc_dibo//2, p_dibo, goc_xedap + goc_dibo + goc_duadon//2, p_duadon))

    noidungcauhoi = (r"""Trong một khảo sát về phương tiện đi học của $500$ học sinh tại một trường THCS, có $%d\%%$ học sinh đi xe đạp, $%d\%%$ học sinh đi bộ và $%d\%%$ học sinh được bố mẹ đưa đón. Để biểu diễn số liệu này trên biểu đồ hình quạt tròn bán kính $R = %d\text{ cm}$ (như hình vẽ), xét tính đúng sai của các khẳng định sau:
    %s""" % (p_xedap, p_dibo, p_duadon, R_val, hinh_ve))

    nb_da_1_d = '\\True Hình quạt tròn biểu diễn số học sinh đi xe đạp ứng với cung có số đo $%d^\\circ$' % goc_xedap
    nb_da_1_s = 'Hình quạt tròn biểu diễn số học sinh đi xe đạp ứng với cung có số đo $%d^\\circ$' % p_xedap
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Số đo cung biểu diễn số học sinh đi xe đạp là $%d\%% \cdot 360^\circ = %d^\circ$.""" % (p_xedap, goc_xedap))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Góc ở tâm của hình quạt tròn biểu diễn số học sinh đi bộ bằng $%d^\\circ$' % goc_dibo
    th_da_1_s = 'Góc ở tâm của hình quạt tròn biểu diễn số học sinh đi bộ bằng $%d^\\circ$' % (goc_dibo + 18)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Góc ở tâm biểu diễn số học sinh đi bộ bằng $%d\%% \cdot 360^\circ = %d^\circ$.""" % (p_dibo, goc_dibo))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích phần hình quạt tròn biểu diễn số học sinh được bố mẹ đưa đón bằng $%s\\text{ cm}^2$' % latex(Sq_duadon)
    vd_da_1_s = 'Diện tích phần hình quạt tròn biểu diễn số học sinh được bố mẹ đưa đón bằng $%s\\text{ cm}^2$' % latex(2 * Sq_duadon)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Góc ở tâm phần đưa đón là $%d^\circ$, diện tích hình quạt tương ứng là $S_q = \dfrac{%d}{360}\pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (goc_duadon, goc_duadon, R_val, latex(Sq_duadon)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Độ dài cung tròn giới hạn phần biểu diễn số học sinh đi xe đạp bằng $%s\\text{ cm}$' % latex(l_xedap)
    vdc_da_1_s = 'Độ dài cung tròn giới hạn phần biểu diễn số học sinh đi xe đạp bằng $%s\\text{ cm}$' % latex(l_xedap + pi)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Độ dài cung tròn giới hạn phần đi xe đạp là $l = \dfrac{%d}{180}\pi \cdot %d = %s\text{ (cm)}$.""" % (goc_xedap, R_val, latex(l_xedap)))
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
