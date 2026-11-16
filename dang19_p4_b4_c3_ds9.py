# -*- coding: utf-8 -*-
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

def bt_dang19_p4_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        V = randint(20, 90)
        while round(V**(1/3))**3 == V:
            V = randint(20, 90)
        d = random.choice([0.5, 1.0, 1.5])
        d_str = str(d).replace('.', ',')
        canh_bon = V**(1/3)
        canh_bon_round = Decimal(str(canh_bon)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
        canh_bon_str = str(canh_bon_round).replace('.', ',')

        canh_rao = float(canh_bon_round) + 2*d
        canh_rao_str = str(round(canh_rao, 3)).replace('.', ',')

        chu_vi = Decimal(str(4 * canh_rao)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        chu_vi_str = str(chu_vi).replace('.', ',')

        noidungcauhoi = ('''Tại một quảng trường trung tâm, người ta dự định xây dựng một đài phun nước có bồn chứa dạng hình lập phương với sức chứa $%s\\text{ m}^3$ nước. Để đảm bảo mỹ quan và an toàn, xung quanh miệng bồn được lắp một hàng rào bảo vệ hình vuông cách đều các mép bồn một khoảng $%s\\text{ m}$ về mỗi phía. Tính chu vi của hàng rào bảo vệ đó (làm tròn kết quả đến chữ số thập phân thứ nhất).'''
                         % (str(V), d_str))

        loigiai = ('''Gọi độ dài cạnh của bồn chứa hình lập phương là $a\\text{ (m)}$ ($a > 0$). \\\\
                   Vì thể tích bồn là $%s\\text{ m}^3$ nên: $a = \\sqrt[3]{%s} \\approx %s\\text{ (m)}$. \\\\
                   Vì hàng rào bảo vệ cách đều mỗi mép bồn $%s\\text{ m}$ về hai phía nên độ dài mỗi cạnh của hàng rào hình vuông là: \\\\
                   $b = a + 2 \\cdot %s \\approx %s + %s = %s\\text{ (m)}$. \\\\
                   Chu vi của hàng rào bảo vệ là: \\\\
                   $C = 4 \\cdot b \\approx 4 \\cdot %s \\approx %s\\text{ (m)}$.'''
                   % (str(V), str(V), canh_bon_str,
                      d_str, d_str, canh_bon_str, str(2*d).replace('.', ','), canh_rao_str,
                      canh_rao_str, chu_vi_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
