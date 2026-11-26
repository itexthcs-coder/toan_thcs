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


def bt_dang17_p2_b2_c7_ds8(self):
    # Dạng 17 (Thực tế): Tính giá tiền nước bậc thang (3 bậc) kèm 15% VAT và phí BVMT
    a_ans, d1, d2, m3_dung = random.choice([
        (7000, 1500, 2000, 24),   # 10a + 10(a+1500) + 4(a+3500) = 24a + 29000 = 168000 + 29000 = 197000 * 1.15 = 226550
        (6500, 1500, 2500, 26),   # 10a + 10(a+1500) + 6(a+4000) = 26a + 39000 = 169000 + 39000 = 208000 * 1.15 = 239200
        (8000, 2000, 2500, 22),   # 10a + 10(a+2000) + 2(a+4500) = 22a + 29000 = 176000 + 29000 = 205000 * 1.15 = 235750
        (6000, 1000, 2000, 25)    # 10a + 10(a+1000) + 5(a+3000) = 25a + 25000 = 150000 + 25000 = 175000 * 1.15 = 201250
    ])
    b3 = m3_dung - 20
    d_tong_b3 = d1 + d2
    tien_chua_thue = m3_dung * a_ans + 10 * d1 + b3 * d_tong_b3
    tong_thanh_toan = int(round(tien_chua_thue * 1.15))

    def fmt_num(n):
        return f"{n:,}".replace(",", "\,")

    noidungcauhoi = "Để khuyến khích tiết kiệm nước sạch, công ty cấp nước áp dụng biểu giá lũy tiến theo bậc thang như sau:\\\\- Bậc 1: Từ $0\\text{ m}^3$ đến $10\\text{ m}^3$ đầu tiên tính giá $a$ (đồng/$\\text{m}^3$).\\\\- Bậc 2: Trên $10\\text{ m}^3$ đến $20\\text{ m}^3$, mỗi mét khối đắt hơn $%s$ đồng so với Bậc 1.\\\\- Bậc 3: Trên $20\\text{ m}^3$, mỗi mét khối đắt hơn $%s$ đồng so với Bậc 2.\\\\Ngoài tiền nước, khách hàng phải trả thêm $5\\%%$ thuế giá trị gia tăng (VAT) và $10\\%%$ phí bảo vệ môi trường (tổng cộng cộng thêm $15\\%%$ trên tổng tiền nước chưa thuế và phí). Tháng vừa qua, gia đình cô Lan sử dụng hết $%s\\text{ m}^3$ nước và thanh toán tổng cộng $%s$ đồng. Xét tính đúng, sai của các khẳng định sau:" % (
        fmt_num(d1), fmt_num(d2), m3_dung, fmt_num(tong_thanh_toan)
    )

    nb_da_1_d = '\\True Tổng tiền nước của gia đình cô Lan trước khi tính thêm $15\\%%$ thuế và phí là $%s$ đồng.' % fmt_num(tien_chua_thue)
    nb_da_1_s = 'Tổng tiền nước của gia đình cô Lan trước khi tính thêm $15\\%%$ thuế và phí là $%s$ đồng.' % fmt_num(int(round(tong_thanh_toan * 0.85)))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Tổng tiền nước trước thuế và phí là $\\dfrac{%s}{115\\%%} = %s$ (đồng).' % (fmt_num(tong_thanh_toan), fmt_num(tien_chua_thue))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Trong $%s\\text{ m}^3$ nước đã dùng, có $10\\text{ m}^3$ tính theo Bậc 1, $10\\text{ m}^3$ tính theo Bậc 2 và $%s\\text{ m}^3$ tính theo Bậc 3.' % (m3_dung, b3)
    th_da_1_s = 'Trong $%s\\text{ m}^3$ nước đã dùng, có $10\\text{ m}^3$ tính theo Bậc 1 và $%s\\text{ m}^3$ tính theo Bậc 3.' % (m3_dung, m3_dung - 10)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Vì $%s = 10 + 10 + %s$ nên có $10\\text{ m}^3$ tính theo Bậc 1, $10\\text{ m}^3$ tính theo Bậc 2 và $%s\\text{ m}^3$ tính theo Bậc 3.' % (m3_dung, b3, b3)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Giá mỗi mét khối nước ở Bậc 3 được biểu diễn theo $a$ là $a + %s$ (đồng).' % fmt_num(d_tong_b3)
    vd_da_1_s = 'Giá mỗi mét khối nước ở Bậc 3 được biểu diễn theo $a$ là $a + %s$ (đồng).' % fmt_num(d2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Giá nước Bậc 2 là $a + %s$ (đồng/$\\text{m}^3$), giá nước Bậc 3 đắt hơn Bậc 2 là $%s$ đồng nên giá Bậc 3 là $(a + %s) + %s = a + %s$ (đồng/$\\text{m}^3$).' % (
        fmt_num(d1), fmt_num(d2), fmt_num(d1), fmt_num(d2), fmt_num(d_tong_b3)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Giá của mỗi mét khối nước ở Bậc 1 là $a = %s$ đồng.' % fmt_num(a_ans)
    vdc_da_1_s = 'Giá của mỗi mét khối nước ở Bậc 1 là $a = %s$ đồng.' % fmt_num(a_ans + 500)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Ta có phương trình: $10a + 10(a + %s) + %s(a + %s) = %s \\Leftrightarrow %sa + %s = %s \\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$ (đồng).' % (
        fmt_num(d1), b3, fmt_num(d_tong_b3), fmt_num(tien_chua_thue),
        m3_dung, fmt_num(10 * d1 + b3 * d_tong_b3), fmt_num(tien_chua_thue),
        m3_dung, fmt_num(m3_dung * a_ans), fmt_num(a_ans)
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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
