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


def bt_dang14_p2_b1_c8_ds8(self):
    # Dạng 14: Chọn ngẫu nhiên gói dịch vụ/tour du lịch phân theo địa điểm
    hg = random.randint(4, 6)
    sp_tour = random.randint(3, 5)
    hl = random.randint(3, 4)
    nb_tour = 2
    tong = hg + sp_tour + hl + nb_tour

    noidungcauhoi = (f"Một công ty du lịch thiết kế ${tong}$ tour khám phá miền Bắc: ${hg}$ tour đi Hà Giang, ${sp_tour}$ tour đi Sa Pa, ${hl}$ tour đi Hạ Long và ${nb_tour}$ tour đi Ninh Bình. Một du khách bốc thăm ngẫu nhiên $1$ tour trúng thưởng.")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${tong}$ kết quả có thể xảy ra."
    nb_da_1_s = "Có $4$ kết quả có thể xảy ra."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Mỗi tour được bốc thăm là một kết quả riêng biệt nên có ${hg} + {sp_tour} + {hl} + {nb_tour} = {tong}$ kết quả có thể.")

    # Thông hiểu
    hop_nui = hg + sp_tour
    th_da_1_d = f"\\True Biến cố \\textit{{``Du khách trúng tour đi vùng núi (Hà Giang hoặc Sa Pa)''}} có ${hop_nui}$ kết quả thuận lợi."
    th_da_1_s = f"Biến cố \\textit{{``Du khách trúng tour đi vùng núi (Hà Giang hoặc Sa Pa)''}} có ${abs(hg - sp_tour) + 1}$ kết quả thuận lợi."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Tổng số tour đi Hà Giang và Sa Pa là ${hg} + {sp_tour} = {hop_nui}$ tour nên có ${hop_nui}$ kết quả thuận lợi.")

    # Vận dụng 1
    not_hl = tong - hl
    vd_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Du khách không trúng tour đi Hạ Long''}} là ${not_hl}$."
    vd_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Du khách không trúng tour đi Hạ Long''}} là ${hl}$."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Số tour không đi Hạ Long là ${tong} - {hl} = {not_hl}$ tour nên có ${not_hl}$ kết quả thuận lợi.")

    # Vận dụng 2
    vdc_da_1_d = "\\True Biến cố \\textit{``Du khách trúng tour đi Ninh Bình''} có ít kết quả thuận lợi nhất trong bốn địa điểm trên."
    vdc_da_1_s = "Biến cố \\textit{``Du khách trúng tour đi Hạ Long''} có ít kết quả thuận lợi nhất trong bốn địa điểm trên."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Tour đi Ninh Bình chỉ có ${nb_tour}$ tour (ít hơn so với ${hg}$, ${sp_tour}$ và ${hl}$) nên có ít kết quả thuận lợi nhất.")

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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
