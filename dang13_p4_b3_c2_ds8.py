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


def bt_dang13_p4_b3_c2_ds8(self):
    # Dạng 13: Chứng minh biểu thức đại số nguyên luôn chia hết cho một hằng số với mọi n nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(2, 4)
        b = randint(2, 4)
        uoc_chung = 6 * b
        # T = (an + b)^3 - (an - b)^3 = 2b * [3a^2n^2 + b^2] = 6b * a^2 * n^2 + 2b^3

        noidungcauhoi = ('''Chứng minh rằng với mọi số nguyên $n$, biểu thức $T = (%sn + %s)^3 - (%sn - %s)^3$ luôn chia hết cho $%s$.'''
                         % (a, b, a, b, uoc_chung))

        loigiai = ('''Áp dụng hằng đẳng thức hiệu hai lập phương, ta có
                    \\begin{align*}
                    T &= (%sn + %s)^3 - (%sn - %s)^3 \\\\
                    &= \\left[(%sn + %s) - (%sn - %s)\\right]\\left[(%sn + %s)^2 + (%sn + %s)(%sn - %s) + (%sn - %s)^2\\right] \\\\
                    &= %s\\left[(%sn^2 + %sn + %s) + (%sn^2 - %s) + (%sn^2 - %sn + %s)\\right] \\\\
                    &= %s(%sn^2 + %s) \\\\
                    &= %sn^2 + %s.
                    \\end{align*}
                    Ta thấy $%sn^2 = %s \\cdot %sn^2$ chia hết cho $%s$ và $%s = %s \\cdot %s$ chia hết cho $%s$ với mọi số nguyên $n$.\\\\
                    Vậy $T$ luôn chia hết cho $%s$ với mọi số nguyên $n$.'''
                   % (a, b, a, b,
                      a, b, a, b, a, b, a, b, a, b, a, b,
                      2*b, a**2, 2*a*b, b**2, a**2, b**2, a**2, 2*a*b, b**2,
                      2*b, 3*(a**2), b**2,
                      6*b*(a**2), 2*(b**3),
                      6*b*(a**2), uoc_chung, a**2, uoc_chung, 2*(b**3), uoc_chung, (b**2)//3 if (b**2)%3==0 else '', uoc_chung,
                      uoc_chung))

        # Sửa lại hệ số chia hết luôn đúng với mọi b: T = 2b(3a^2n^2 + b^2) luôn chia hết cho 2b
        uoc_chuan = 2 * b
        noidungcauhoi = ('''Chứng minh rằng với mọi số nguyên $n$, biểu thức $T = (%sn + %s)^3 - (%sn - %s)^3$ luôn chia hết cho $%s$.'''
                         % (a, b, a, b, uoc_chuan))

        loigiai = ('''Áp dụng hằng đẳng thức hiệu hai lập phương, ta có
                    \\begin{align*}
                    T &= (%sn + %s)^3 - (%sn - %s)^3 \\\\
                    &= \\left[(%sn + %s) - (%sn - %s)\\right]\\left[(%sn + %s)^2 + (%sn + %s)(%sn - %s) + (%sn - %s)^2\\right] \\\\
                    &= %s\\left[(%sn^2 + %sn + %s) + (%sn^2 - %s) + (%sn^2 - %sn + %s)\\right] \\\\
                    &= %s(%sn^2 + %s).
                    \\end{align*}
                    Vì $n$ là số nguyên nên $%sn^2 + %s$ là một số nguyên, do đó $T$ luôn chia hết cho $%s$.'''
                   % (a, b, a, b,
                      a, b, a, b, a, b, a, b, a, b, a, b,
                      uoc_chuan, a**2, 2*a*b, b**2, a**2, b**2, a**2, 2*a*b, b**2,
                      uoc_chuan, 3*(a**2), b**2,
                      3*(a**2), b**2, uoc_chuan))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
