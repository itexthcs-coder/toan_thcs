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


def bt_dang17_p2_b1_c6_ds8(self):
    # Dạng 17: Mô hình hóa bài toán năng suất lao động - sản xuất công nghiệp
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (1200, 10, 50, 40), # 1200/50=24, 1200/60=20 (sớm 4 ngày); x=40 -> 1200/50=24
            (600, 10, 20, 30),  # 600/20=30, 600/30=20 (sớm 10 ngày); x=30 -> 600/40=15
            (900, 15, 30, 45)   # 900/30=30, 900/45=20 (sớm 10 ngày); x=45 -> 900/60=15
        ]
        tong_sp, vuot, x1, x2 = random.choice(scenarios)
        t_kh = tong_sp // x1
        t_tt = tong_sp // (x1 + vuot)
        som = t_kh - t_tt
        t_tt2 = tong_sp // (x2 + vuot)
        
        noidungcauhoi = ('Một xưởng may theo kế hoạch phải may xong $%s$ bộ đồng phục học sinh trong một thời gian quy định. Giả sử mỗi ngày theo kế hoạch xưởng may được $x$ bộ đồng phục ($x \\in \\mathbb{N}^*$). Nhờ cải tiến kỹ thuật, thực tế mỗi ngày xưởng may vượt mức $%s$ bộ so với kế hoạch. Xét tính đúng sai của các khẳng định sau:'
                         % (tong_sp, vuot))
        
        nb_da_1_d = '\\True Phân thức biểu thị số ngày hoàn thành công việc theo kế hoạch là $\\dfrac{%s}{x}$ (ngày)' % tong_sp
        nb_da_1_s = 'Phân thức biểu thị số ngày hoàn thành công việc theo kế hoạch là $\\dfrac{x}{%s}$ (ngày)' % tong_sp
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Thời gian hoàn thành bằng tổng số sản phẩm chia cho năng suất mỗi ngày: $\\dfrac{%s}{x}$ (ngày).' % tong_sp
        loigiai_nb_s = 'Sai. Số ngày hoàn thành phải bằng tổng số sản phẩm chia cho số sản phẩm làm được trong một ngày: $\\dfrac{%s}{x}$ (ngày).' % tong_sp
        
        th_da_1_d = '\\True Phân thức biểu thị số ngày thực tế xưởng hoàn thành $%s$ bộ đồng phục là $\\dfrac{%s}{x + %s}$ (ngày)' % (tong_sp, tong_sp, vuot)
        th_da_1_s = 'Phân thức biểu thị số ngày thực tế xưởng hoàn thành $%s$ bộ đồng phục là $\\dfrac{%s}{x - %s}$ (ngày)' % (tong_sp, tong_sp, vuot)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Thực tế mỗi ngày may được $x + %s$ bộ nên số ngày thực tế hoàn thành là $\\dfrac{%s}{x + %s}$ (ngày).' % (vuot, tong_sp, vuot)
        loigiai_th_s = 'Sai. Vì xưởng may vượt mức $%s$ bộ mỗi ngày nên năng suất thực tế là $x + %s$ (bộ/ngày).' % (vuot, vuot)
        
        vd_da_1_d = '\\True Nếu theo kế hoạch mỗi ngày xưởng may được $%s$ bộ thì thực tế xưởng hoàn thành sớm hơn kế hoạch $%s$ ngày' % (x1, som)
        vd_da_1_s = 'Nếu theo kế hoạch mỗi ngày xưởng may được $%s$ bộ thì thực tế xưởng hoàn thành sớm hơn kế hoạch $%s$ ngày' % (x1, som + 2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Với $x = %s$: số ngày theo kế hoạch là $\\dfrac{%s}{%s} = %s$ ngày; số ngày thực tế là $\\dfrac{%s}{%s + %s} = %s$ ngày. Xưởng hoàn thành sớm hơn $%s - %s = %s$ ngày.' % (x1, tong_sp, x1, t_kh, tong_sp, x1, vuot, t_tt, t_kh, t_tt, som)
        loigiai_vd_s = 'Sai. Thời gian theo kế hoạch là $%s$ ngày và thực tế là $%s$ ngày, nên xưởng hoàn thành sớm hơn $%s$ ngày chứ không phải $%s$ ngày.' % (t_kh, t_tt, som, som + 2)
        
        vdc_da_1_d = '\\True Khi $x = %s$, thời gian thực tế xưởng hoàn thành công việc là $%s$ ngày' % (x2, t_tt2)
        vdc_da_1_s = 'Khi $x = %s$, thời gian thực tế xưởng hoàn thành công việc là $%s$ ngày' % (x2, tong_sp // x2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Thay $x = %s$ vào phân thức $\\dfrac{%s}{x + %s}$, ta được $\\dfrac{%s}{%s + %s} = %s$ (ngày).' % (x2, tong_sp, vuot, tong_sp, x2, vuot, t_tt2)
        loigiai_vdc_s = 'Sai. $%s$ ngày là thời gian theo kế hoạch; thời gian thực tế là $\\dfrac{%s}{%s + %s} = %s$ ngày.' % (tong_sp // x2, tong_sp, x2, vuot, t_tt2)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
