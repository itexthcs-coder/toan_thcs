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


def bt_dang19_p2_b3_c2_ds9(self):
    chi_phi_bien_doi = random.choice([30, 35, 40])
    lai_gop_sp = random.choice([20, 25, 30])
    gia_ban = chi_phi_bien_doi + lai_gop_sp
    hoa_von = random.choice([400, 500, 600])
    chi_phi_co_dinh = lai_gop_sp * hoa_von

    noidungcauhoi = ('''Một xưởng thủ công làm lồng đèn Trung thu có chi phí cố định (thuê mặt bằng, điện nước) là $%s$ nghìn đồng/tháng. Chi phí nguyên vật liệu và nhân công để làm ra mỗi chiếc lồng đèn là $%s$ nghìn đồng. Xưởng bán ra thị trường với giá $%s$ nghìn đồng/chiếc. Gọi $x$ ($x \\in \\mathbb{N}^*$) là số chiếc lồng đèn bán được trong tháng. Xét tính đúng sai của các khẳng định sau:''' % (latex(chi_phi_co_dinh), latex(chi_phi_bien_doi), latex(gia_ban)))

    nb_da_1_d = '\\True Tổng chi phí của xưởng khi sản xuất $x$ chiếc lồng đèn là $%s + %sx$ (nghìn đồng)' % (latex(chi_phi_co_dinh), latex(chi_phi_bien_doi))
    nb_da_1_s = 'Tổng chi phí của xưởng khi sản xuất $x$ chiếc lồng đèn là $%sx + %s$ (nghìn đồng)' % (latex(chi_phi_co_dinh), latex(chi_phi_bien_doi))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng chi phí bằng chi phí cố định $%s$ nghìn đồng cộng với chi phí sản xuất $x$ chiếc là $%sx$ nghìn đồng.''' % (latex(chi_phi_co_dinh), latex(chi_phi_bien_doi)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Doanh thu khi bán hết $x$ chiếc lồng đèn là $%sx$ (nghìn đồng)' % (latex(gia_ban))
    th_da_1_s = 'Doanh thu khi bán hết $x$ chiếc lồng đèn là $%sx$ (nghìn đồng)' % (latex(lai_gop_sp))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Bán $x$ chiếc với giá $%s$ nghìn đồng/chiếc thu được doanh thu là $%sx$ (nghìn đồng).''' % (latex(gia_ban), latex(gia_ban)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Để xưởng bắt đầu có lãi (doanh thu lớn hơn tổng chi phí), số sản phẩm bán được phải thỏa mãn $%sx > %s$' % (latex(lai_gop_sp), latex(chi_phi_co_dinh))
    vd_da_1_s = 'Để xưởng bắt đầu có lãi (doanh thu lớn hơn tổng chi phí), số sản phẩm bán được phải thỏa mãn $%sx \\ge %s$' % (latex(lai_gop_sp), latex(chi_phi_co_dinh))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Để có lãi thì $%sx > %s + %sx \\Leftrightarrow %sx > %s$.''' % (latex(gia_ban), latex(chi_phi_co_dinh), latex(chi_phi_bien_doi), latex(lai_gop_sp), latex(chi_phi_co_dinh)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xưởng cần bán được ít nhất $%s$ chiếc lồng đèn mới bắt đầu có lãi' % (latex(hoa_von + 1))
    vdc_da_1_s = 'Xưởng cần bán được ít nhất $%s$ chiếc lồng đèn mới bắt đầu có lãi' % (latex(hoa_von))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $x > %s$ và $x \\in \\mathbb{N}^*$ nên xưởng phải bán ít nhất $%s$ chiếc mới có lãi (bán $%s$ chiếc là hòa vốn).''' % (latex(hoa_von), latex(hoa_von + 1), latex(hoa_von)))
    list_vdc_2 = [loigiai_vdc_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
